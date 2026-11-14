"""Readable project-structure document. Requires the analysed commit SHA."""
from __future__ import annotations

from .report import _meta, _ref_text
from .sanitize import sanitize_text

_MAX_DEPTH = 3
_MAX_ENTRIES = 24


def model_to_structure_md(model, metadata=None) -> str:
    """Project structure for one repository snapshot.

    The analysed commit is mandatory: every structure document must be
    reproducible against a specific Git revision.
    """
    sha = str(_meta(metadata, "commit_sha") or "").strip()
    if not sha:
        raise ValueError("commit SHA is required to write structure.md")

    full_name = _meta(metadata, "full_name") or _meta(metadata, "name") or "repository"
    html_url = str(_meta(metadata, "html_url") or "").rstrip("/")
    branch = _meta(metadata, "default_branch") or ""
    commit_url = f"{html_url}/commit/{sha}" if html_url else ""
    tree_url = f"{html_url}/tree/{sha}" if html_url else ""

    files = sorted(model.files or [], key=lambda f: f.path)
    paths = [f.path for f in files]
    out: list[str] = []
    add = out.append

    add(f"# Project structure: {sanitize_text(full_name, 160)}")
    add("")
    add(f"**Analysed commit:** `{sha}`")
    add("")
    if commit_url:
        add(f"**Commit reference:** [{sha}]({commit_url})")
        add("")
    if tree_url:
        add(f"**Tree at this commit:** [{full_name}@{sha[:12]}]({tree_url})")
        add("")
    add("Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.")
    add("")
    add("| Item | Value |")
    add("| --- | --- |")
    add(f"| Repository | {sanitize_text(full_name, 160)} |")
    desc = _meta(metadata, "description")
    add(f"| Description | {sanitize_text(desc, 300) if desc else 'Not provided'} |")
    add(f"| Stars | {_meta(metadata, 'stars', 'Not provided')} |")
    add(f"| Forks | {_meta(metadata, 'forks', 'Not provided')} |")
    lic = _meta(metadata, "license")
    add(f"| Licence | {sanitize_text(lic, 80) if lic else 'Not detected'} |")
    add(f"| Language | {sanitize_text(_meta(metadata, 'language') or 'Python', 40)} |")
    add(f"| Default branch | {sanitize_text(branch, 80) if branch else 'Not provided'} |")
    add(f"| Analysed commit | `{sha}` |")
    retrieved = _meta(metadata, "retrieved_at")
    add(f"| Retrieved at | {sanitize_text(retrieved, 40) if retrieved else 'Not recorded'} |")
    add(f"| Files in this snapshot | {len(files)} |")
    add("")

    add("## Directory tree")
    add("")
    if not paths:
        add("No files were kept for this commit.")
        add("")
    else:
        add("```text")
        out.extend(_render_tree(paths))
        add("```")
        add("")

    add("## Entry points")
    add("")
    if model.entry_points:
        for ref in model.entry_points:
            add(f"- {_ref_text(metadata, ref)}")
        add("")
    else:
        add("No application entry point was observed at this commit.")
        add("")

    add("## Main components")
    add("")
    components = list(model.components or [])
    if not components:
        add("No components were identified from the analysed files.")
        add("")
    else:
        add("| Component | Kind | Status | Responsibility |")
        add("| --- | --- | --- | --- |")
        for comp in components:
            status = "Inferred" if comp.inferred else "Observed"
            add(
                f"| {sanitize_text(comp.name, 80)} | {sanitize_text(comp.kind, 24)} | {status} | "
                f"{sanitize_text(comp.responsibility, 220)} |"
            )
        add("")

    add("## Important files")
    add("")
    important = [f for f in files if f.category in {"manifest", "config", "ci", "container"}]
    if important:
        for f in important:
            add(f"- `{sanitize_text(f.path, 240)}` ({sanitize_text(f.category, 24)})")
        add("")
    else:
        add("No manifest, config, CI, or container files were observed in the analysed set.")
        add("")

    add("## Top-level layout")
    add("")
    counts: dict[str, int] = {}
    for path in paths:
        top = path.split("/", 1)[0] if "/" in path else "(root files)"
        counts[top] = counts.get(top, 0) + 1
    if counts:
        for name, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
            add(f"- `{sanitize_text(name, 120)}` — {count} analysed file(s)")
        add("")
    else:
        add("No top-level layout to report.")
        add("")

    add("## Limitations")
    add("")
    limitations = list(model.limitations or [])
    if limitations:
        for item in limitations:
            add(f"- {sanitize_text(item, 500)}")
    else:
        add("- None recorded beyond the static-analysis boundary.")
    add("")
    add(f"Commit `{sha}` is the revision these paths and observations refer to.")
    add("")
    return "\n".join(out)


def _render_tree(paths: list[str]) -> list[str]:
    lines: list[str] = []

    def walk(prefix: str, depth: int) -> None:
        groups: dict[str, list[str]] = {}
        files: list[str] = []
        for path in paths:
            if prefix:
                if not path.startswith(prefix + "/"):
                    continue
                rest = path[len(prefix) + 1 :]
            else:
                rest = path
            if "/" not in rest:
                files.append(rest)
            else:
                head = rest.split("/", 1)[0]
                groups.setdefault(head, []).append(path)
        indent = "  " * depth
        for name in sorted(groups):
            child_prefix = f"{prefix}/{name}" if prefix else name
            count = len(groups[name])
            lines.append(f"{indent}{name}/  ({count} files)")
            if depth + 1 < _MAX_DEPTH:
                walk(child_prefix, depth + 1)
            else:
                lines.append(f"{indent}  … {count} files under this directory")
        shown = sorted(files)[:_MAX_ENTRIES]
        for name in shown:
            lines.append(f"{indent}{name}")
        if len(files) > len(shown):
            lines.append(f"{indent}… {len(files) - len(shown)} more files")

    walk("", 0)
    return lines
