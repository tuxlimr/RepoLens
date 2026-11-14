"""JavaScript and TypeScript signals from paths and package.json.

There is no JavaScript AST in this pass, and repository code is never executed.
"""
from __future__ import annotations

import json

from ..models import SourceRef

_ENTRY_NAMES = {
    "index.js", "index.jsx", "index.ts", "index.tsx",
    "main.js", "main.ts", "main.jsx", "main.tsx",
    "app.js", "app.jsx", "app.ts", "app.tsx",
    "page.js", "page.jsx", "page.ts", "page.tsx",
    "server.js", "server.ts",
}
_SKIP = {
    "test", "tests", "__tests__", "node_modules", "dist", "build",
    "docs", "doc", "examples", "example", "coverage", ".next",
}
_JS_SUFFIXES = (".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs")


def augment_javascript(model, files: dict[str, str]) -> None:
    js_files = [path for path in files if path.lower().endswith(_JS_SUFFIXES)]
    if not js_files:
        return
    have = {ref.path for ref in model.entry_points}
    added: list[str] = []
    for ref in _manifest_entries(files) + _conventional_entries(files):
        if ref.path in have or len(model.entry_points) >= 12:
            continue
        model.entry_points.append(ref)
        have.add(ref.path)
        added.append(ref.path)
    if added:
        model.stats["javascript_entry_points"] = added
    if not any(path.endswith(".py") for path in files):
        model.limitations.append(
            "JavaScript and TypeScript files were inventoried from paths and package manifests. "
            "They were not parsed with a full language AST, and repository code was not executed."
        )


def _manifest_entries(files: dict[str, str]) -> list[SourceRef]:
    refs: list[SourceRef] = []
    for path in sorted(files):
        if path.rsplit("/", 1)[-1] != "package.json":
            continue
        try:
            data = json.loads(files[path])
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        relatives: list[str] = []
        if isinstance(data.get("main"), str):
            relatives.append(data["main"])
        bin_field = data.get("bin")
        if isinstance(bin_field, str):
            relatives.append(bin_field)
        elif isinstance(bin_field, dict):
            relatives.extend(value for value in bin_field.values() if isinstance(value, str))
        base = path.rsplit("/", 1)[0] if "/" in path else ""
        for relative in relatives:
            relative = relative.replace("\\", "/").lstrip("./")
            full = f"{base}/{relative}" if base else relative
            if full in files:
                refs.append(SourceRef(path=full))
    return refs


def _conventional_entries(files: dict[str, str]) -> list[SourceRef]:
    refs: list[SourceRef] = []
    for path in sorted(files):
        parts = [part.lower() for part in path.split("/")]
        if set(parts) & _SKIP or parts[-1] not in _ENTRY_NAMES or len(parts) > 4:
            continue
        refs.append(SourceRef(path=path))
    return refs
