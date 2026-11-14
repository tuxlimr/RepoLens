"""Markdown report generation (spec section 6B, all 12 sections)."""
from __future__ import annotations
from urllib.parse import quote
from ..models import SourceRef
from .mermaid import model_to_mermaid
from .sanitize import sanitize_text

def _meta(metadata, key, default=None):
    if metadata is None:
        return default
    if isinstance(metadata, dict):
        return metadata.get(key, default)
    return getattr(metadata, key, default)

def _blob_url(metadata, ref):
    html_url = _meta(metadata, "html_url")
    if not html_url:
        return None
    refname = _meta(metadata, "commit_sha") or _meta(metadata, "default_branch") or "main"
    url = f"{str(html_url).rstrip('/')}/blob/{refname}/{quote(ref.path)}"
    if ref.start_line:
        url += f"#L{ref.start_line}"
        if ref.end_line and ref.end_line != ref.start_line:
            url += f"-L{ref.end_line}"
    return url

def _ref_text(metadata, ref):
    loc = ref.path
    if ref.start_line:
        loc += f":{ref.start_line}"
        if ref.end_line and ref.end_line != ref.start_line:
            loc += f"-{ref.end_line}"
    url = _blob_url(metadata, ref)
    return f"[{loc}]({url})" if url else f"`{loc}`"

def _status(inferred):
    return "Inferred" if inferred else "Observed"

def model_to_markdown(model, metadata=None):
    components = sorted(model.components or [], key=lambda c: c.id)
    detections = sorted(model.detections or [], key=lambda d: (d.category, d.name.lower()))
    files = sorted(model.files or [], key=lambda f: f.path)
    comp_by_id = {c.id: c for c in components}
    full_name = _meta(metadata, "full_name") or _meta(metadata, "name") or "Repository"
    out = []
    add = out.append
    add(f"# Architecture report: {sanitize_text(full_name, 120)}"); add("")
    add("> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed."); add("")
    # 1
    add("## 1. Repository at a glance"); add("")
    add("| Item | Value |"); add("| --- | --- |")
    add(f"| Repository | {sanitize_text(full_name, 120)} |")
    desc = _meta(metadata, "description")
    add(f"| Description | {sanitize_text(desc, 300) if desc else 'Not provided'} |")
    language = _meta(metadata, "language")
    langs = sorted({f.language for f in files if f.language})
    add(f"| Language | {sanitize_text(language, 60) if language else (', '.join(langs) if langs else 'Not detected')} |")
    add(f"| Stars | {_meta(metadata, 'stars', 'Not provided')} |")
    lic = _meta(metadata, "license")
    add(f"| Licence | {sanitize_text(lic, 80) if lic else 'Not detected'} |")
    commit = _meta(metadata, "commit_sha"); branch = _meta(metadata, "default_branch")
    add(f"| Analysed commit / branch | {sanitize_text(commit, 80) if commit else 'Not provided'}{' / ' + sanitize_text(branch, 60) if branch else ''} |")
    frameworks = [d.name for d in detections if d.category == "framework"]
    add(f"| Framework(s) | {', '.join(frameworks) if frameworks else 'None detected'} |")
    add(f"| Files analysed | {len(files)} |"); add(f"| Components | {len(components)} |"); add("")
    # 2
    add("## 2. Architecture in one minute"); add("")
    add(sanitize_text(model.summary) or "No summary could be derived from the analysed files."); add("")
    # 3
    add("## 3. High-level block diagram"); add("")
    add("```mermaid"); add(model_to_mermaid(model).rstrip()); add("```"); add("")
    # 4
    add("## 4. Main components"); add("")
    if not components:
        add("No components were identified from the analysed files."); add("")
    for c in components:
        add(f"### {sanitize_text(c.name, 120)} (`{c.id}`)"); add("")
        add(f"- **Kind:** {sanitize_text(c.kind, 40)}")
        add(f"- **Status:** {_status(bool(c.inferred))}")
        add(f"- **Confidence:** {c.confidence:.2f}")
        add(f"- **Responsibility:** {sanitize_text(c.responsibility) or 'Not established from evidence.'}")
        if c.paths:
            add("- **Paths:** " + ", ".join("`" + sanitize_text(p, 200) + "`" for p in c.paths))
        if c.evidence:
            add("- **Evidence:** " + "; ".join(_ref_text(metadata, r) for r in c.evidence))
        add("")
    # 5
    add("## 5. Execution flow"); add("")
    if model.entry_points:
        add("**Observed** entry point(s):"); add("")
        for ref in sorted(model.entry_points, key=lambda r: (r.path, r.start_line or 0)):
            add(f"- {_ref_text(metadata, ref)}")
        add("")
    else:
        add("No entry point was observed; the startup flow below is therefore limited."); add("")
    routes = (model.stats or {}).get("routes") or []
    if routes:
        add("**Observed** routes (from decorators):"); add("")
        for r in routes:
            add(f"- `{sanitize_text(r.get('method', ''), 20)} {sanitize_text(r.get('route_path', ''), 120)}` -> `{sanitize_text(r.get('function', ''), 80)}` in `{sanitize_text(r.get('path', ''), 200)}:{r.get('line', '')}`")
        add("")
    add("Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):"); add("")
    add("1. Execution starts at an observed entry point listed above, if present.")
    step = 2; seen_flow = set()
    for rel in sorted(model.relationships or [], key=lambda r: (r.source, r.target)):
        if (rel.source, rel.target) in seen_flow:
            continue
        seen_flow.add((rel.source, rel.target))
        src = comp_by_id.get(rel.source); tgt = comp_by_id.get(rel.target)
        if src and tgt:
            add(f"{step}. `{src.id}` {sanitize_text(rel.label or rel.kind, 40)} `{tgt.id}` ({sanitize_text(src.name, 60)} -> {sanitize_text(tgt.name, 60)}).")
            step += 1
        if step > 9:
            break
    if step == 2:
        add("2. No internal import relationships between components were observed.")
    add("")
    # 6
    add("## 6. Project structure"); add("")
    if not files:
        add("No files were analysed."); add("")
    by_top = {}
    for f in files:
        top = f.path.split("/", 1)[0] if "/" in f.path else "(root)"
        by_top.setdefault(top, []).append(f)
    for top in sorted(by_top):
        add(f"### `{sanitize_text(top, 120)}`"); add("")
        for f in sorted(by_top[top], key=lambda x: x.path):
            add(f"- `{sanitize_text(f.path, 240)}` - {sanitize_text(f.category, 30)}{', ' + sanitize_text(f.language, 30) if f.language else ''} ({f.size} bytes)")
        add("")
    # 7
    add("## 7. Key dependencies and integrations"); add("")
    if not detections:
        add("No known dependencies or integrations were detected from imports or manifests."); add("")
    else:
        add("| Name | Category | Status | Confidence | Evidence |"); add("| --- | --- | --- | --- | --- |")
        for d in detections:
            status = "Inferred" if d.confidence < 0.6 else "Observed"
            ev = "; ".join(_ref_text(metadata, r) for r in d.evidence[:4]) or "-"
            add(f"| {sanitize_text(d.name, 80)} | {sanitize_text(d.category, 40)} | {status} | {d.confidence:.2f} | {ev} |")
        add("")
    # 8
    add("## 8. Data and state"); add("")
    db_dets = [d for d in detections if d.category == "database"]
    data_comps = [c for c in components if c.kind == "data"]
    for d in db_dets:
        status = "Inferred" if d.confidence < 0.6 else "Observed"
        add(f"- **{sanitize_text(d.name, 80)}** ({status}, confidence {d.confidence:.2f}) - evidence: {'; '.join(_ref_text(metadata, r) for r in d.evidence[:4]) or '-'}")
    for c in data_comps:
        add(f"- Data component `{c.id}` ({_status(bool(c.inferred))}): {sanitize_text(c.responsibility, 300)}")
    if not db_dets and not data_comps:
        add("No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.")
    add("")
    # 9
    add("## 9. Configuration and deployment clues"); add("")
    config_files = [f for f in files if f.category in {"config", "manifest", "ci", "container"}]
    if config_files:
        for f in config_files:
            add(f"- `{sanitize_text(f.path, 240)}` ({sanitize_text(f.category, 30)})")
    else:
        add("No configuration, manifest, CI, or container files were observed.")
    env_keys = (model.stats or {}).get("env_example_keys") or {}
    if env_keys:
        add(""); add("Environment variable *names* seen in example env files (values never recorded):"); add("")
        for path in sorted(env_keys):
            add(f"- `{sanitize_text(path, 200)}`: " + ", ".join(f"`{sanitize_text(k, 60)}`" for k in env_keys[path]))
    scripts = (model.stats or {}).get("console_scripts") or {}
    if scripts:
        add(""); add("Console scripts declared in packaging metadata (**Observed**):"); add("")
        for name_s in sorted(scripts):
            add(f"- `{sanitize_text(name_s, 60)}` -> `{sanitize_text(scripts[name_s], 120)}`")
    add("")
    # 10
    add("## 10. Design observations"); add("")
    observations = []
    kinds = {c.kind for c in components}
    if "api" in kinds or "entrypoint" in kinds:
        observations.append("An entry/API layer is separated from other code (Inferred from paths and decorators).")
    if "data" in kinds:
        observations.append("Data-related code is grouped separately, suggesting a data-layer boundary (Inferred).")
    if "service" in kinds:
        observations.append("Service/domain code is distinct from entry and data code, suggesting layered separation (Inferred).")
    if "test" in kinds:
        observations.append("Tests are present alongside source code (Observed from test file paths).")
    if "external" in kinds:
        observations.append("External integrations appear isolated behind a boundary component (Inferred from imports/paths).")
    if len(components) <= 1:
        observations.append("The analysed code appears small or monolithic; few component boundaries were observed.")
    for obs in observations:
        add(f"- {obs}")
    if not observations:
        add("- No strong design patterns could be established from the available evidence.")
    add(""); add("These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design."); add("")
    # 11
    add("## 11. Limitations and unknowns"); add("")
    if model.limitations:
        for lim in model.limitations:
            add(f"- {sanitize_text(lim, 500)}")
    else:
        add("- Static analysis only; repository code was not executed.")
    add("")
    # 12
    add("## 12. Source references"); add("")
    refs = []
    for c in components:
        refs.extend(c.evidence)
    for d in detections:
        refs.extend(d.evidence)
    refs.extend(model.entry_points or [])
    seen, uniq = set(), []
    for r in sorted(refs, key=lambda x: (x.path, x.start_line or 0)):
        key = (r.path, r.start_line, r.end_line)
        if key not in seen:
            seen.add(key); uniq.append(r)
    if uniq:
        for r in uniq:
            add(f"- {_ref_text(metadata, r)}")
    else:
        add("No source references were recorded.")
    add("")
    return sanitize_text("\n".join(out))
