"""RepoLens FastAPI application."""
from __future__ import annotations

import json
import uuid
from datetime import datetime
from typing import Any, Optional

from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app import db as db_module
from app.config import settings
from app.db import Analysis, Catalog, CatalogSnapshot, Payment, Report, Repository
from app.github_client import parse_github_url
from app.jobs import TOOL_VERSION, run_analysis

app = FastAPI(title="RepoLens")

_cors = [o.strip() for o in settings.cors_origins.split(",") if o.strip()] or ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_module.init_db()


class AnalyzeRequest(BaseModel):
    url: str
    fresh: bool = False


class PaymentFreshRequest(BaseModel):
    url: str


EXAMPLES: list[dict[str, Any]] = [
    {"owner": "psf", "repo": "requests", "name": "requests", "url": "https://github.com/psf/requests", "stars": 53000, "language": "Python", "blurb": "A simple, yet elegant, HTTP library for Python."},
    {"owner": "fastapi", "repo": "fastapi", "name": "fastapi", "url": "https://github.com/fastapi/fastapi", "stars": 78000, "language": "Python", "blurb": "Modern, fast web framework for building APIs with Python type hints."},
    {"owner": "django", "repo": "django", "name": "django", "url": "https://github.com/django/django", "stars": 82000, "language": "Python", "blurb": "The high-level Python web framework that encourages rapid development."},
    {"owner": "pallets", "repo": "flask", "name": "flask", "url": "https://github.com/pallets/flask", "stars": 68000, "language": "Python", "blurb": "A lightweight WSGI web application framework."},
    {"owner": "pandas-dev", "repo": "pandas", "name": "pandas", "url": "https://github.com/pandas-dev/pandas", "stars": 45000, "language": "Python", "blurb": "Powerful data structures and data analysis tools for Python."},
    {"owner": "scikit-learn", "repo": "scikit-learn", "name": "scikit-learn", "url": "https://github.com/scikit-learn/scikit-learn", "stars": 61000, "language": "Python", "blurb": "Machine learning library for Python."},
    {"owner": "pytest-dev", "repo": "pytest", "name": "pytest", "url": "https://github.com/pytest-dev/pytest", "stars": 13000, "language": "Python", "blurb": "A mature full-featured Python testing framework."},
    {"owner": "encode", "repo": "httpx", "name": "httpx", "url": "https://github.com/encode/httpx", "stars": 14000, "language": "Python", "blurb": "A next generation HTTP client for Python."},
]


def _iso(value: Optional[datetime]) -> Optional[str]:
    return value.isoformat() if value else None


def _parse_json(text: Optional[str], default: Any) -> Any:
    if not text:
        return default
    try:
        return json.loads(text)
    except Exception:
        return default


def _repo_payload(repo: Repository) -> dict[str, Any]:
    stored = _parse_json(repo.metadata_json, None)
    if isinstance(stored, dict) and stored:
        return stored
    return {
        "owner": repo.owner,
        "name": repo.name,
        "full_name": f"{repo.owner}/{repo.name}",
        "html_url": repo.html_url,
    }


def _snapshot_payload(snapshot: CatalogSnapshot, repo: Repository, catalog: Optional[Catalog]) -> dict[str, Any]:
    metadata = _parse_json(repo.metadata_json, None)
    if not isinstance(metadata, dict) or not metadata:
        metadata = {
            "owner": repo.owner,
            "name": repo.name,
            "full_name": f"{repo.owner}/{repo.name}",
            "html_url": repo.html_url,
            "description": snapshot.description,
            "stars": snapshot.stars,
            "forks": snapshot.forks,
            "language": snapshot.language,
            "license": snapshot.license,
            "default_branch": snapshot.default_branch,
            "commit_sha": snapshot.commit_sha,
        }
    return {
        "id": snapshot.id,
        "analysis_id": None,
        "version": 1,
        "commit_sha": snapshot.commit_sha,
        "analysed_at": _iso(snapshot.analysed_at),
        "created_at": _iso(snapshot.analysed_at),
        "source": "catalog",
        "ecosystem": catalog.ecosystem if catalog else None,
        "repository": metadata,
        "model": _parse_json(snapshot.model_json, {}),
        "mermaid": snapshot.mermaid,
        "markdown": snapshot.report_markdown,
    }


def _cached_document(session: Session, owner: str, name: str) -> Optional[dict[str, Any]]:
    """Pipeline report wins. Otherwise serve the catalog snapshot for this repository."""
    report = db_module.latest_report(session, owner, name)
    if report is not None:
        return _report_payload(report, session)
    snapshot = db_module.catalog_snapshot_for_repository(session, owner, name)
    if snapshot is None:
        return None
    repo = session.get(Repository, snapshot.repository_id)
    catalog = session.get(Catalog, snapshot.catalog_id)
    if repo is None:
        return None
    return _snapshot_payload(snapshot, repo, catalog)


def _report_payload(report: Report, session: Session) -> dict[str, Any]:
    repo = session.get(Repository, report.repository_id)
    metadata = _parse_json(report.metadata_json, None)
    if not isinstance(metadata, dict) or not metadata:
        metadata = _repo_payload(repo) if repo else {}
    return {
        "id": report.id,
        "analysis_id": report.analysis_id,
        "version": report.version,
        "commit_sha": report.commit_sha,
        "analysed_at": _iso(report.created_at),
        "created_at": _iso(report.created_at),
        "repository": metadata,
        "model": _parse_json(report.model_json, {}),
        "mermaid": report.mermaid,
        "markdown": report.markdown,
    }


def _queue_analysis(session: Session, repo: Repository, background: BackgroundTasks) -> Analysis:
    analysis = Analysis(repository_id=repo.id, status="queued", tool_version=TOOL_VERSION)
    session.add(analysis)
    session.commit()
    session.refresh(analysis)
    background.add_task(run_analysis, analysis.id)
    return analysis


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/analyze")
def analyze(payload: AnalyzeRequest, background: BackgroundTasks, session: Session = Depends(db_module.get_db)):
    try:
        owner, name = parse_github_url(payload.url)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    repo = db_module.get_or_create_repository(session, owner, name, html_url=f"https://github.com/{owner}/{name}")
    session.commit()
    if not payload.fresh:
        cached = _cached_document(session, owner, name)
        if cached is not None:
            return {"status": "cached", "report": cached}
    analysis = _queue_analysis(session, repo, background)
    return {
        "status": "queued",
        "analysis_id": analysis.id,
        "repository": _repo_payload(repo),
    }


@app.get("/api/analyses/{analysis_id}")
def get_analysis(analysis_id: int, session: Session = Depends(db_module.get_db)):
    analysis = session.get(Analysis, analysis_id)
    if analysis is None:
        raise HTTPException(status_code=404, detail="Analysis not found")
    repo = session.get(Repository, analysis.repository_id)
    report = session.execute(
        select(Report).where(Report.analysis_id == analysis.id).order_by(Report.id.desc())
    ).scalars().first()
    result: dict[str, Any] = {
        "id": analysis.id,
        "analysis_id": analysis.id,
        "status": analysis.status,
        "error": analysis.error,
        "commit_sha": analysis.commit_sha,
        "branch": analysis.branch,
        "created_at": _iso(analysis.created_at),
        "finished_at": _iso(analysis.finished_at),
        "repository": _repo_payload(repo) if repo else None,
    }
    if report is not None:
        result["report"] = {"id": report.id, "version": report.version, "commit_sha": report.commit_sha}
        result["report_id"] = report.id
    else:
        result["report"] = None
    return result


@app.get("/api/reports")
def recent_reports(session: Session = Depends(db_module.get_db)):
    reports = db_module.list_reports(session, limit=50)
    out = []
    for r in reports:
        repo = session.get(Repository, r.repository_id)
        metadata = _parse_json(r.metadata_json, {}) or {}
        out.append({
            "id": r.id,
            "owner": repo.owner if repo else metadata.get("owner"),
            "name": repo.name if repo else metadata.get("name"),
            "repo": f"{repo.owner}/{repo.name}" if repo else metadata.get("full_name"),
            "stars": metadata.get("stars", 0),
            "version": r.version,
            "commit_sha": r.commit_sha,
            "analysed_at": _iso(r.created_at),
        })
    return out


@app.get("/api/catalogs")
def list_catalogs(session: Session = Depends(db_module.get_db)):
    catalogs = session.execute(select(Catalog).order_by(Catalog.ecosystem)).scalars().all()
    out = []
    for catalog in catalogs:
        completed = session.execute(
            select(func.count()).select_from(CatalogSnapshot).where(
                CatalogSnapshot.catalog_id == catalog.id,
                CatalogSnapshot.status == "completed",
            )
        ).scalar_one()
        out.append({
            "ecosystem": catalog.ecosystem,
            "title": catalog.title,
            "selection_note": catalog.selection_note,
            "completed": completed,
            "loaded_at": _iso(catalog.loaded_at),
        })
    return out


@app.get("/api/catalogs/{ecosystem}")
def list_catalog_snapshots(
    ecosystem: str,
    limit: int = 50,
    offset: int = 0,
    q: str = "",
    session: Session = Depends(db_module.get_db),
):
    catalog = session.execute(select(Catalog).where(Catalog.ecosystem == ecosystem)).scalar_one_or_none()
    if catalog is None:
        raise HTTPException(status_code=404, detail="Catalog not found")
    limit = min(max(limit, 1), 200)
    offset = max(offset, 0)
    filters = [CatalogSnapshot.catalog_id == catalog.id, CatalogSnapshot.status == "completed"]
    needle = q.strip().lower()
    if needle:
        like = f"%{needle}%"
        filters.append(or_(
            func.lower(Repository.owner).like(like),
            func.lower(Repository.name).like(like),
            func.lower(Repository.owner + "/" + Repository.name).like(like),
        ))
    total = session.execute(
        select(func.count())
        .select_from(CatalogSnapshot)
        .join(Repository, CatalogSnapshot.repository_id == Repository.id)
        .where(*filters)
    ).scalar_one()
    rows = session.execute(
        select(CatalogSnapshot, Repository)
        .join(Repository, CatalogSnapshot.repository_id == Repository.id)
        .where(*filters)
        .order_by(CatalogSnapshot.stars.desc(), Repository.owner, Repository.name)
        .offset(offset)
        .limit(limit)
    ).all()
    return {
        "ecosystem": catalog.ecosystem,
        "total": total,
        "snapshots": [
            {
                "owner": repo.owner,
                "name": repo.name,
                "description": (snap.description or "")[:240] or None,
                "stars": snap.stars,
                "language": snap.language,
                "commit_sha": snap.commit_sha,
                "commit_url": snap.commit_url,
                "analysed_at": _iso(snap.analysed_at),
                "files_analysed": snap.files_analysed,
            }
            for snap, repo in rows
        ],
    }


@app.get("/api/reports/{owner}/{repo_name}")
def get_report(owner: str, repo_name: str, session: Session = Depends(db_module.get_db)):
    document = _cached_document(session, owner, repo_name)
    if document is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return document


@app.get("/api/reports/{owner}/{repo_name}/versions")
def get_report_versions(owner: str, repo_name: str, session: Session = Depends(db_module.get_db)):
    repo = db_module.get_repository(session, owner, repo_name)
    if repo is None:
        raise HTTPException(status_code=404, detail="Repository not found")
    reports = db_module.list_reports(session, owner, repo_name)
    return [
        {
            "id": r.id,
            "version": r.version,
            "commit_sha": r.commit_sha,
            "analysed_at": _iso(r.created_at),
            "analysis_id": r.analysis_id,
        }
        for r in reports
    ]


@app.get("/api/reports/{owner}/{repo_name}/markdown")
def get_report_markdown(owner: str, repo_name: str, session: Session = Depends(db_module.get_db)):
    document = _cached_document(session, owner, repo_name)
    if document is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return PlainTextResponse(
        content=document.get("markdown") or "",
        media_type="text/markdown",
        headers={"Content-Disposition": f'attachment; filename="{repo_name}-architecture.md"'},
    )


@app.get("/api/examples")
def examples():
    return EXAMPLES


@app.post("/api/payments/fresh")
def payment_fresh(payload: PaymentFreshRequest, background: BackgroundTasks, session: Session = Depends(db_module.get_db)):
    try:
        owner, name = parse_github_url(payload.url)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    repo = db_module.get_or_create_repository(session, owner, name, html_url=f"https://github.com/{owner}/{name}")
    session.commit()
    analysis = _queue_analysis(session, repo, background)
    payment = Payment(
        repository_id=repo.id,
        provider="mock",
        provider_ref=f"mock_{uuid.uuid4().hex[:16]}",
        amount_cents=settings.fresh_analysis_price_cents,
        currency="USD",
        status="mock_paid",
        analysis_id=analysis.id,
    )
    session.add(payment)
    session.commit()
    session.refresh(payment)
    return {
        "status": "queued",
        "analysis_id": analysis.id,
        "payment": {
            "id": payment.id,
            "provider": payment.provider,
            "provider_ref": payment.provider_ref,
            "amount_cents": payment.amount_cents,
            "currency": payment.currency,
            "status": payment.status,
            "analysis_id": payment.analysis_id,
            "created_at": _iso(payment.created_at),
            "note": "Mock payment only — no real charge was made and no payment provider is integrated.",
        },
        "note": "Mock payment only — no real charge was made and no payment provider is integrated.",
    }


@app.get("/api/repositories/{owner}/{repo_name}")
def get_repository(owner: str, repo_name: str, session: Session = Depends(db_module.get_db)):
    repo = db_module.get_repository(session, owner, repo_name)
    if repo is None:
        raise HTTPException(status_code=404, detail="Repository not found")
    return _repo_payload(repo)
