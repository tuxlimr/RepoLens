"""Shared contracts for RepoLens. All agents/modules MUST use these types.

Analyzer produces ArchitectureModel; API stores it as JSON; report/mermaid
renderers consume it; frontend mirrors it in frontend/lib/types.ts.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional


@dataclass
class RepoMetadata:
    owner: str
    name: str
    full_name: str  # owner/name
    html_url: str
    description: Optional[str] = None
    stars: int = 0
    forks: int = 0
    open_issues: int = 0
    language: Optional[str] = None
    license: Optional[str] = None
    default_branch: str = "main"
    commit_sha: Optional[str] = None
    topics: list[str] = field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    retrieved_at: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class SourceRef:
    path: str
    start_line: Optional[int] = None
    end_line: Optional[int] = None
    url: Optional[str] = None  # GitHub blob URL, filled by API layer

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Component:
    id: str  # slug, safe for Mermaid node ids: [a-z0-9_]
    name: str
    kind: str  # entrypoint|core|api|service|data|external|config|test|cli|worker|library|unknown
    responsibility: str = ""
    paths: list[str] = field(default_factory=list)
    evidence: list[SourceRef] = field(default_factory=list)
    confidence: float = 0.5  # 0..1
    inferred: bool = False  # True = interpretation, False = observed fact

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["evidence"] = [e if isinstance(e, dict) else asdict(e) for e in self.evidence]
        return d


@dataclass
class Relationship:
    source: str  # Component.id
    target: str  # Component.id
    label: str = ""
    kind: str = "depends_on"  # imports|calls|reads|writes|depends_on|routes_to

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Detection:
    name: str  # e.g. "FastAPI", "pytest", "PostgreSQL"
    category: str  # framework|library|database|tooling|ci|packaging
    confidence: float = 0.5
    evidence: list[SourceRef] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["evidence"] = [e if isinstance(e, dict) else asdict(e) for e in self.evidence]
        return d


@dataclass
class FileInfo:
    path: str
    size: int = 0
    category: str = "source"  # source|manifest|config|test|docs|ci|container|data|other
    language: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ArchitectureModel:
    components: list[Component] = field(default_factory=list)
    relationships: list[Relationship] = field(default_factory=list)
    detections: list[Detection] = field(default_factory=list)
    entry_points: list[SourceRef] = field(default_factory=list)
    files: list[FileInfo] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    summary: str = ""  # deterministic 1-paragraph overview (no LLM required)
    stats: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "components": [c.to_dict() for c in self.components],
            "relationships": [r.to_dict() for r in self.relationships],
            "detections": [d.to_dict() for d in self.detections],
            "entry_points": [e.to_dict() if hasattr(e, "to_dict") else e for e in self.entry_points],
            "files": [f.to_dict() for f in self.files],
            "limitations": list(self.limitations),
            "summary": self.summary,
            "stats": dict(self.stats),
        }
