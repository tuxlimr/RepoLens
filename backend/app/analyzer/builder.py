"""Build the ArchitectureModel: meaningful components + import relationships."""
from __future__ import annotations
from ..models import ArchitectureModel, Component, Relationship, SourceRef
from .detect import EXTERNAL_IMPORTS
from .sanitize import sanitize_text, slugify

ENTRY_BASENAMES = {"main.py", "__main__.py", "app.py", "wsgi.py", "asgi.py", "manage.py", "run.py", "server.py", "cli.py"}
API_PARTS = {"api", "routes", "routers", "endpoints", "controllers", "views", "handlers"}
DATA_PARTS = {"data", "db", "database", "models", "repositories", "repository", "persistence", "storage"}
EXTERNAL_PARTS = {"integrations", "integration", "clients", "client", "external", "gateways", "adapters"}
SERVICE_PARTS = {"services", "service", "core", "domain", "logic", "business", "use_cases", "usecases"}
CONFIG_PARTS = {"config", "configs", "settings", "conf"}

def _module_name(path):
    p = path[:-3] if path.endswith(".py") else path
    parts = [x for x in p.split("/") if x]
    if parts and parts[0] == "src":
        parts = parts[1:]
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)

def _top_package(path):
    parts = [x for x in path.split("/") if x]
    if parts and parts[0] == "src" and len(parts) > 1:
        return parts[1]
    return parts[0] if len(parts) > 1 else ""

def _component_for_file(path, category, info):
    parts = [x for x in path.lower().split("/") if x]
    name = parts[-1] if parts else path
    dirs = set(parts[:-1])
    if category == "test":
        return "tests", "Tests", "test", False
    # Hidden dirs (.devcontainer, .github internals), docs and examples are
    # supporting material, not architectural components.
    if parts and (parts[0].startswith(".") or parts[0] in {"docs", "doc", "examples", "example"}):
        return None
    if category in {"manifest", "config", "ci", "container"}:
        return "config", "Configuration and deployment", "config", False
    if category != "source" and not path.endswith(".py"):
        return None
    if name in ENTRY_BASENAMES or (info and info.app_factories) or (info and info.has_main_guard):
        return "entrypoint", "Application entry point", "entrypoint", False
    if dirs & API_PARTS or (info and info.routes):
        return "api_layer", "API layer", "api", False
    if dirs & DATA_PARTS or name in {"models.py", "model.py", "db.py", "database.py", "schemas.py"}:
        return "data_layer", "Data layer", "data", False
    if dirs & EXTERNAL_PARTS or name.endswith(("_client.py", "_api.py")) or name == "client.py":
        return "external_integrations", "External integrations", "external", False
    if dirs & CONFIG_PARTS or name in {"config.py", "settings.py"}:
        return "config", "Configuration and deployment", "config", False
    if dirs & SERVICE_PARTS or name in {"service.py", "services.py"} or name.endswith("_service.py"):
        return "service_layer", "Service / domain layer", "service", False
    top = _top_package(path)
    if top:
        return slugify(top), f"{sanitize_text(top, 40)} package", "library", False
    return "core", "Core modules", "core", False

def _responsibility(name, paths, modules):
    infos = [modules[p] for p in paths if p in modules]
    classes = sorted({c.name for m in infos for c in m.classes})
    funcs = sorted({f.name for m in infos for f in m.functions})
    routes = [r for m in infos for r in m.routes]
    factories = sorted({f for m in infos for _, f, _ in m.app_factories})
    bits = [f"Groups {len(paths)} file(s) under {name.lower()} (observed from repository paths and static analysis)."]
    if factories:
        bits.append(f"Observed application object created via {', '.join(factories)}.")
    if routes:
        bits.append("Observed routes: " + ", ".join(f"{r.method} {r.route_path or '(path not a literal)'}" for r in routes[:5]) + ".")
    if classes:
        bits.append(f"Observed top-level classes: {', '.join(classes[:6])}.")
    if funcs:
        bits.append(f"Observed top-level functions: {', '.join(funcs[:6])}.")
    return sanitize_text(" ".join(bits), 600)

def _meta_get(metadata, key, default=None):
    if metadata is None:
        return default
    if isinstance(metadata, dict):
        return metadata.get(key, default)
    return getattr(metadata, key, default)

def build_model(files, infos, skipped, limit_notes, py_modules, unparsed, detections, console_scripts, env_keys, metadata=None):
    groups, file_component = {}, {}
    for info_file in sorted(infos, key=lambda f: f.path):
        path = info_file.path
        grouped = _component_for_file(path, info_file.category, py_modules.get(path))
        if grouped is None:
            continue
        cid, cname, kind, inferred = grouped
        file_component[path] = cid
        groups.setdefault(cid, {"name": cname, "kind": kind, "inferred": inferred, "paths": []})["paths"].append(path)

    external_refs = []
    for path in sorted(py_modules):
        for imp in py_modules[path].imports:
            top = imp.module.split(".")[0].lower() if imp.module else ""
            if top in EXTERNAL_IMPORTS and file_component.get(path) != "external_integrations":
                external_refs.append(SourceRef(path=path, start_line=imp.line, end_line=imp.line))
    if external_refs and "external_integrations" not in groups:
        groups["external_integrations"] = {"name": "External integrations", "kind": "external", "inferred": True, "paths": [], "extra_evidence": external_refs[:6]}
    db_dets = [d for d in detections if d.category == "database"]
    if db_dets and "data_layer" not in groups and "external_integrations" not in groups:
        groups["data_layer"] = {"name": "Data layer", "kind": "data", "inferred": True, "paths": [], "extra_evidence": [r for d in db_dets for r in d.evidence][:6]}

    components = []
    for cid in sorted(groups):
        bucket = groups[cid]
        paths = sorted(bucket["paths"])
        evidence = []
        for p in paths[:8]:
            mod = py_modules.get(p)
            line = None
            if mod:
                symbols = mod.classes + mod.functions
                line = min((s.line for s in symbols), default=None)
                if mod.app_factories:
                    line = mod.app_factories[0][2]
            evidence.append(SourceRef(path=p, start_line=line, end_line=line))
        evidence.extend(bucket.get("extra_evidence", []))
        seen, uniq = set(), []
        for r in evidence:
            k = (r.path, r.start_line, r.end_line)
            if k not in seen:
                seen.add(k); uniq.append(r)
        components.append(Component(id=cid, name=bucket["name"], kind=bucket["kind"],
            responsibility=_responsibility(bucket["name"], paths, py_modules),
            paths=paths, evidence=uniq[:10], confidence=0.7 if bucket["inferred"] else 0.85,
            inferred=bool(bucket["inferred"])))
    component_ids = {c.id for c in components}

    # Entry points: one per file (earliest evidence), excluding tests,
    # examples and docs (they contain many incidental main-guards/CLI demos).
    entry_points = []
    _seen_entry_paths: set[str] = set()

    def add_entry(ref, force=False):
        if ref.path in _seen_entry_paths and not force:
            return
        _seen_entry_paths.add(ref.path)
        entry_points.append(ref)

    def _is_noise_path(p: str) -> bool:
        segs = {s.lower() for s in p.split("/")}
        return bool(segs & {"tests", "test", "examples", "example", "docs", "doc"}) or "/test_" in p.lower()

    module_to_path = {_module_name(p): p for p in py_modules}
    for _script, target in sorted(console_scripts.items()):
        mod_name = target.split(":")[0]
        if mod_name in module_to_path and not _is_noise_path(module_to_path[mod_name]):
            add_entry(SourceRef(path=module_to_path[mod_name]), force=True)
    for path in sorted(py_modules):
        if _is_noise_path(path):
            continue
        info = py_modules[path]
        base = path.rsplit("/", 1)[-1]
        lines = []
        if base in ENTRY_BASENAMES:
            lines.append(info.app_factories[0][2] if info.app_factories else info.main_guard_line)
        if info.has_main_guard:
            lines.append(info.main_guard_line)
        lines += [line for _v, _f, line in info.app_factories]
        lines += [cmd.line for cmd in info.cli_commands]
        lines = [ln for ln in lines if ln]
        if lines:
            ln = min(lines)
            add_entry(SourceRef(path=path, start_line=ln, end_line=ln))
    entry_points.sort(key=lambda r: (0 if "/src/" in f"/{r.path}" or r.path.startswith("src/") else 1, r.path))
    del entry_points[12:]

    relationships, seen_edges = [], set()
    def add_edge(src, tgt, label="imports", kind="imports"):
        if src == tgt or src not in component_ids or tgt not in component_ids:
            return
        key = (src, tgt, label)
        if key not in seen_edges:
            seen_edges.add(key); relationships.append(Relationship(source=src, target=tgt, label=label, kind=kind))
    for path in sorted(py_modules):
        src_comp = file_component.get(path)
        if not src_comp:
            continue
        info = py_modules[path]
        own_module = _module_name(path)
        for imp in info.imports:
            target_module = imp.module
            if imp.level:
                base_parts = own_module.split(".")[:-imp.level] if own_module else []
                target_module = ".".join([x for x in base_parts + ([imp.module] if imp.module else []) if x])
            best_path, best_len = None, -1
            for mod_name, mod_path in module_to_path.items():
                if target_module == mod_name or target_module.startswith(mod_name + "."):
                    if len(mod_name) > best_len:
                        best_path, best_len = mod_path, len(mod_name)
            if best_path and best_path != path:
                tgt = file_component.get(best_path)
                if tgt:
                    add_edge(src_comp, tgt); continue
            top = imp.module.split(".")[0].lower() if imp.module else ""
            if top in EXTERNAL_IMPORTS:
                tgt = "data_layer" if top in {"sqlalchemy", "sqlite3", "aiosqlite", "psycopg", "psycopg2", "asyncpg", "pymongo", "motor", "pymysql", "aiomysql", "redis"} else "external_integrations"
                if tgt in component_ids:
                    add_edge(src_comp, tgt)
    relationships.sort(key=lambda r: (r.source, r.target, r.label))

    limitations = [
        "Static analysis only: repository code was not executed, installed, or imported at runtime.",
        "Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.",
    ]
    limitations.extend(limit_notes)
    if skipped:
        reasons = {}
        for _p, reason in skipped:
            reasons[reason] = reasons.get(reason, 0) + 1
        detail = "; ".join(f"{n} x {sanitize_text(r, 120)}" for r, n in sorted(reasons.items()))
        limitations.append(f"{len(skipped)} file(s) were skipped during inventory ({detail}).")
    for path in sorted(unparsed):
        limitations.append(f"File {sanitize_text(path, 200)} could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.")
    if not entry_points:
        limitations.append("No clear application entry point was observed in the analysed files.")
    if not detections:
        limitations.append("No known frameworks or libraries were detected from imports or manifests.")
    limitations.append("Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.")

    routes_stat = []
    for path in sorted(py_modules):
        for r in py_modules[path].routes:
            routes_stat.append({"method": r.method, "route_path": r.route_path, "function": r.function, "path": path, "line": r.line, "component": file_component.get(path)})
    stats = {
        "total_files_provided": len(files) + len(skipped), "analysed_files": len(infos), "skipped_files": len(skipped),
        "python_files": sum(1 for f in infos if f.path.endswith(".py")), "test_files": sum(1 for f in infos if f.category == "test"),
        "component_count": len(components), "relationship_count": len(relationships), "detection_count": len(detections),
        "entry_point_count": len(entry_points), "routes": routes_stat,
        "env_example_keys": {p: list(v) for p, v in sorted(env_keys.items())},
        "console_scripts": dict(sorted(console_scripts.items())),
        "categories": {cat: sum(1 for f in infos if f.category == cat) for cat in sorted({f.category for f in infos})},
    }
    summary = _summary(infos, components, detections, entry_points, metadata)
    return ArchitectureModel(components=components, relationships=relationships, detections=detections, entry_points=entry_points, files=list(infos), limitations=limitations, summary=summary, stats=stats)

def _summary(infos, components, detections, entry_points, metadata):
    full_name = _meta_get(metadata, "full_name"); desc = _meta_get(metadata, "description")
    head = ""
    if full_name:
        head = sanitize_text(full_name, 120)
        if desc:
            head += f" - {sanitize_text(desc, 200)}"
        head += ". "
    py_count = sum(1 for f in infos if f.path.endswith(".py"))
    det_names = ", ".join(d.name for d in detections[:6]) or "no known frameworks/libraries"
    comp_names = ", ".join(c.name for c in components[:8]) or "no components"
    entry_txt = ""
    if entry_points:
        entry_txt = f" Observed entry point(s): {', '.join(sorted({r.path for r in entry_points})[:3])}."
    text = (f"{head}This repository was analysed statically from {len(infos)} file(s) ({py_count} Python). "
            f"Detected technologies (observed from imports/manifests): {det_names}. "
            f"Files are grouped into {len(components)} component(s): {comp_names}.{entry_txt} "
            "Findings below distinguish observed facts from inferred interpretation.")
    return sanitize_text(text, 900)
