"""RepoLens analysis engine — public interface.

Pure static analysis: no network, no code execution, no following of
instructions embedded in repository content (all repo text is untrusted).
"""
from __future__ import annotations

from ..config import settings
from ..models import ArchitectureModel, RepoMetadata
from .builder import build_model
from .detect import detect, parse_manifests
from .inventory import inventory_files, normalise_path
from .javascript import augment_javascript
from .mermaid import model_to_mermaid
from .python_ast import parse_python_file
from .report import model_to_markdown
from .structure_doc import model_to_structure_md

__all__ = ["analyze_files", "model_to_mermaid", "model_to_markdown", "model_to_structure_md"]


def analyze_files(files: dict[str, str], metadata: RepoMetadata | dict | None = None) -> ArchitectureModel:
    """Analyse an in-memory repository snapshot.

    ``files`` maps repo-relative paths to text content. Pure and
    deterministic: identical input yields an identical model.
    """
    raw = {str(k): (v if isinstance(v, str) else str(v)) for k, v in (files or {}).items()}
    kept, infos, skipped, limit_notes = inventory_files(
        raw,
        max_files=int(getattr(settings, "max_files", 800)),
        max_file_bytes=int(getattr(settings, "max_file_bytes", 200_000)),
        max_total_bytes=int(getattr(settings, "max_total_bytes", 8_000_000)),
    )

    py_modules = {}
    unparsed: list[str] = []
    for path in sorted(kept):
        if path.endswith(".py"):
            info = parse_python_file(path, kept[path])
            if info is None:
                unparsed.append(path)
            else:
                py_modules[path] = info

    dep_names, console_scripts, env_keys = parse_manifests(kept)
    detections = detect(kept, py_modules, dep_names, env_keys)

    model = build_model(
        kept, infos, skipped, limit_notes, py_modules, unparsed,
        detections, console_scripts, env_keys, metadata=metadata,
    )
    # Total provided counts every input path, including skipped ones.
    model.stats["total_files_provided"] = len(raw)
    model.stats["unparsed_files"] = sorted(unparsed)
    augment_javascript(model, kept)
    return model
