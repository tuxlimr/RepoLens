"""Load catalog snapshots into the RepoLens database.

Pipeline reports stay in ``reports``. Each checked repository becomes one
``catalog_snapshots`` row per ecosystem, pinned to the commit that was
downloaded. Re-running updates nothing already stored for that catalog,
repository, and commit.

Usage (from the repository root or backend/):

    python backend/scripts/load_catalog.py
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
ROOT = BACKEND.parent
sys.path.insert(0, str(BACKEND))

from sqlalchemy import select  # noqa: E402

from app.db import (  # noqa: E402
    CatalogSnapshot,
    Repository,
    ensure_catalog,
    get_session,
    init_db,
)

CORPORA = [
    (
        "python",
        "RepoLens Python catalog",
        "Public Python repositories, forks excluded, GitHub size under 50 MB, highest stars above 5,000.",
        ROOT / "catalog",
    ),
    (
        "javascript",
        "RepoLens JavaScript catalog",
        "Public JavaScript repositories, forks excluded, GitHub size under 50 MB, highest stars above 5,000.",
        ROOT / "catalog" / "javascript",
    ),
    (
        "react",
        "RepoLens React catalog",
        "Public repositories tagged topic:react, forks excluded, GitHub size under 50 MB. Star floor drops below 5,000 only to reach the catalog size.",
        ROOT / "catalog" / "react",
    ),
]


def _slug(text: str, used: set[str]) -> str:
    base = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_") or "component"
    base = base[:48]
    candidate = base
    n = 2
    while candidate in used:
        candidate = f"{base}_{n}"
        n += 1
    used.add(candidate)
    return candidate


def _summary(report: str, description: str | None) -> str:
    marker = "## 2. Architecture in one minute"
    if marker in report:
        body = report.split(marker, 1)[1].split("\n## ", 1)[0].strip()
        if body:
            return body[:1500]
    return (description or "").strip()


def _model(meta: dict, report: str) -> dict:
    used: set[str] = set()
    components = [
        {
            "id": _slug(str(name), used),
            "name": name,
            "kind": "unknown",
            "responsibility": "",
            "paths": [],
            "evidence": [],
            "confidence": 0.6,
            "inferred": True,
        }
        for name in meta.get("components") or []
    ]
    return {
        "components": components,
        "relationships": [],
        "detections": [
            {"name": name, "category": "library", "confidence": 0.7, "evidence": []}
            for name in meta.get("detections") or []
        ],
        "entry_points": [
            {"path": path, "start_line": None, "end_line": None, "url": None}
            for path in meta.get("entry_points") or []
        ],
        "files": [],
        "limitations": [
            "Catalog snapshot pinned to the analysed commit. It was loaded from the on-disk catalog, not produced by a fresh analysis job.",
        ],
        "summary": _summary(report, meta.get("description")),
        "stats": {
            "files_fetched": int(meta.get("files_fetched") or 0),
            "files_analysed": int(meta.get("files_analysed") or 0),
            "catalog": True,
        },
    }


def _when(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def _read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load() -> None:
    db_path = BACKEND / "repolens.db"
    init_db("sqlite:///" + db_path.resolve().as_posix())
    session = get_session()
    added = 0
    skipped = 0
    try:
        repos = {(row.owner, row.name): row for row in session.execute(select(Repository)).scalars()}
        existing = set(
            session.execute(
                select(CatalogSnapshot.catalog_id, CatalogSnapshot.repository_id, CatalogSnapshot.commit_sha)
            ).all()
        )
        for ecosystem, title, note, base in CORPORA:
            catalog = ensure_catalog(session, ecosystem, title, note)
            state_path = base / "_state.json"
            if not state_path.exists():
                print(f"missing {state_path}", flush=True)
                continue
            state = json.loads(state_path.read_text(encoding="utf-8"))
            for row in state.get("results", {}).values():
                owner, name = row.get("owner"), row.get("name")
                if not owner or not name:
                    continue
                folder = base / "repos" / owner / name
                meta_path = folder / "meta.json"
                meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else dict(row)
                sha = str(meta.get("commit_sha") or row.get("commit_sha") or "")
                if len(sha) < 7:
                    skipped += 1
                    continue
                repo = repos.get((owner, name))
                if repo is None:
                    repo = Repository(
                        owner=owner,
                        name=name,
                        html_url=meta.get("html_url") or f"https://github.com/{owner}/{name}",
                        metadata_json=json.dumps({k: meta.get(k) for k in (
                            "owner", "name", "full_name", "html_url", "description", "stars", "forks",
                            "language", "license", "default_branch", "commit_sha", "topics",
                        )}),
                    )
                    session.add(repo)
                    session.flush()
                    repos[(owner, name)] = repo
                key = (catalog.id, repo.id, sha)
                if key in existing:
                    skipped += 1
                    continue
                report = _read(folder / "report.md")
                structure = _read(folder / "structure.md")
                mermaid = _read(folder / "diagram.mmd")
                status = str(meta.get("status") or row.get("status") or "completed")
                if status == "completed" and not report:
                    status = "missing_files"
                snapshot = CatalogSnapshot(
                    catalog_id=catalog.id,
                    repository_id=repo.id,
                    commit_sha=sha,
                    commit_url=meta.get("commit_url") or f"https://github.com/{owner}/{name}/commit/{sha}",
                    tree_url=meta.get("tree_url") or f"https://github.com/{owner}/{name}/tree/{sha}",
                    stars=int(meta.get("stars") or row.get("stars") or 0),
                    forks=int(meta.get("forks") or row.get("forks") or 0),
                    language=meta.get("language") or row.get("language"),
                    license=meta.get("license") or row.get("license"),
                    description=meta.get("description") or row.get("description"),
                    default_branch=meta.get("default_branch") or row.get("default_branch"),
                    archived=bool(meta.get("archived") or row.get("archived")),
                    analysed_at=_when(meta.get("analysed_at") or row.get("finished_at")),
                    status=status,
                    error=row.get("error"),
                    files_fetched=int(meta.get("files_fetched") or 0),
                    files_analysed=int(meta.get("files_analysed") or 0),
                    components_json=json.dumps(meta.get("components") or []),
                    detections_json=json.dumps(meta.get("detections") or []),
                    entry_points_json=json.dumps(meta.get("entry_points") or []),
                    model_json=json.dumps(_model(meta, report)),
                    structure_markdown=structure,
                    report_markdown=report,
                    mermaid=mermaid,
                    source_path=folder.relative_to(ROOT).as_posix(),
                )
                session.add(snapshot)
                existing.add(key)
                added += 1
                if added % 50 == 0:
                    session.commit()
                    print(f"committed {added} new snapshots ({ecosystem})", flush=True)
            session.commit()
            print(f"ecosystem {ecosystem} flushed", flush=True)
        session.commit()
        print(f"done added={added} skipped={skipped}", flush=True)
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    load()
