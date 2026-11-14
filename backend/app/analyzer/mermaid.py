"""Mermaid diagram generation from an ArchitectureModel."""
from __future__ import annotations
import re
from .sanitize import sanitize_label
MAX_NODES = 25

def model_to_mermaid(model):
    components = list(getattr(model, "components", []) or [])
    lines = ["flowchart TD"]
    if not components:
        lines.append('    no_components["No components detected"]')
        return "\n".join(lines) + "\n"
    merged_note = None
    if len(components) > MAX_NODES:
        def importance(c):
            degree = sum(1 for r in model.relationships if r.source == c.id or r.target == c.id)
            return (len(getattr(c, "paths", []) or []), degree)
        ranked = sorted(components, key=lambda c: (-importance(c)[0], -importance(c)[1], c.id))
        keep = ranked[:MAX_NODES - 1]
        keep_ids = {c.id for c in keep}
        merged_note = len(components) - len(keep)
        id_map = {c.id: (c.id if c.id in keep_ids else "other") for c in model.components}
        components = sorted(keep, key=lambda c: c.id)
    else:
        id_map = {c.id: c.id for c in components}
        components = sorted(components, key=lambda c: c.id)
    known_ids = {c.id for c in components}
    if merged_note:
        known_ids.add("other")
    by_kind = {}
    for c in components:
        by_kind.setdefault(str(c.kind or "unknown"), []).append(c)
    multi_kind = len(by_kind) > 1
    for kind in sorted(by_kind):
        members = sorted(by_kind[kind], key=lambda c: c.id)
        if multi_kind:
            gid = re.sub(r"[^a-z0-9_]+", "_", kind.lower()).strip("_") or "group"
            lines.append(f"    subgraph {gid}_group")
            indent = "        "
        else:
            indent = "    "
        for c in members:
            cid = c.id if re.fullmatch(r"[a-z0-9_]+", c.id or "") else re.sub(r"[^a-z0-9_]+", "_", (c.id or "node").lower())
            label = sanitize_label(c.name, 50) or sanitize_label(cid, 50)
            lines.append(f'{indent}{cid}["{label}"]')
        if multi_kind:
            lines.append("    end")
    if merged_note:
        lines.append(f'    other["Other components ({merged_note} merged)"]')
        lines.append(f"    %% Note: {merged_note} smaller component(s) merged into 'other' to keep the diagram readable.")
    seen = set()
    for rel in sorted(model.relationships or [], key=lambda r: (r.source, r.target, r.label)):
        src = id_map.get(rel.source, rel.source); tgt = id_map.get(rel.target, rel.target)
        if src not in known_ids or tgt not in known_ids or src == tgt:
            continue
        if not re.fullmatch(r"[a-z0-9_]+", src or "") or not re.fullmatch(r"[a-z0-9_]+", tgt or ""):
            continue
        label = sanitize_label(rel.label or rel.kind or "depends_on", 30)
        key = (src, tgt, label)
        if key not in seen:
            seen.add(key)
            lines.append(f"    {src} -->|{label}| {tgt}" if label else f"    {src} --> {tgt}")
    return "\n".join(lines) + "\n"
