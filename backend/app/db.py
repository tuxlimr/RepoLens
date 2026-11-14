"""SQLAlchemy 2.0 persistence layer for RepoLens."""
from __future__ import annotations

import json
import os
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Any, Iterator, Optional

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    create_engine,
    func,
    select,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

from app.config import settings


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    pass


class Repository(Base):
    __tablename__ = "repositories"
    __table_args__ = (UniqueConstraint("owner", "name", name="uq_repository_owner_name"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    owner: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    html_url: Mapped[str] = mapped_column(String(1024), nullable=False, default="")
    metadata_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_utcnow, onupdate=_utcnow)


class Analysis(Base):
    __tablename__ = "analyses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    repository_id: Mapped[int] = mapped_column(ForeignKey("repositories.id"), nullable=False, index=True)
    commit_sha: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    branch: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="queued", index=True)
    error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_utcnow)
    finished_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    tool_version: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)


class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    analysis_id: Mapped[Optional[int]] = mapped_column(ForeignKey("analyses.id"), nullable=True, index=True)
    repository_id: Mapped[int] = mapped_column(ForeignKey("repositories.id"), nullable=False, index=True)
    commit_sha: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    markdown: Mapped[str] = mapped_column(Text, nullable=False, default="")
    mermaid: Mapped[str] = mapped_column(Text, nullable=False, default="")
    model_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")
    metadata_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_utcnow)


class Catalog(Base):
    """One evaluation corpus: python, javascript, or react."""

    __tablename__ = "catalogs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ecosystem: Mapped[str] = mapped_column(String(32), nullable=False, unique=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    selection_note: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    loaded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_utcnow)


class CatalogSnapshot(Base):
    """A repository checked for one catalog, pinned to the downloaded commit.

    Pipeline reports stay in ``reports``. A snapshot is the corpus row: the
    same GitHub repository can appear in more than one ecosystem, and a live
    analysis of that repository is a separate versioned report.
    """

    __tablename__ = "catalog_snapshots"
    __table_args__ = (
        UniqueConstraint("catalog_id", "repository_id", "commit_sha", name="uq_catalog_repo_commit"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    catalog_id: Mapped[int] = mapped_column(ForeignKey("catalogs.id"), nullable=False, index=True)
    repository_id: Mapped[int] = mapped_column(ForeignKey("repositories.id"), nullable=False, index=True)
    commit_sha: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    commit_url: Mapped[Optional[str]] = mapped_column(String(1024), nullable=True)
    tree_url: Mapped[Optional[str]] = mapped_column(String(1024), nullable=True)
    stars: Mapped[int] = mapped_column(Integer, nullable=False, default=0, index=True)
    forks: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    language: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    license: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    default_branch: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    archived: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    analysed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="completed", index=True)
    error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    files_fetched: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    files_analysed: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    components_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    detections_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    entry_points_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    model_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")
    structure_markdown: Mapped[str] = mapped_column(Text, nullable=False, default="")
    report_markdown: Mapped[str] = mapped_column(Text, nullable=False, default="")
    mermaid: Mapped[str] = mapped_column(Text, nullable=False, default="")
    source_path: Mapped[Optional[str]] = mapped_column(String(1024), nullable=True)


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    repository_id: Mapped[int] = mapped_column(ForeignKey("repositories.id"), nullable=False, index=True)
    provider: Mapped[str] = mapped_column(String(64), nullable=False, default="mock")
    provider_ref: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    amount_cents: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    currency: Mapped[str] = mapped_column(String(16), nullable=False, default="USD")
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="mock_paid")
    analysis_id: Mapped[Optional[int]] = mapped_column(ForeignKey("analyses.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_utcnow)


# --- Engine / session management -------------------------------------------
_engine = None
_SessionLocal: Optional[sessionmaker] = None


def _make_engine(database_url: str):
    connect_args: dict[str, Any] = {}
    if database_url.startswith("sqlite"):
        # Extract filesystem path e.g. sqlite:///./repolens.db or sqlite:////abs/path
        connect_args["check_same_thread"] = False
        path_part = database_url.split(":///", 1)[-1] if ":///" in database_url else ""
        if path_part and path_part != ":memory:" and not path_part.startswith(":memory:"):
            # Handle sqlite:///./x and sqlite:////abs/x (path_part for ////abs is /abs)
            directory = os.path.dirname(os.path.abspath(path_part)) if not os.path.isabs(path_part) else os.path.dirname(path_part)
            if directory:
                os.makedirs(directory, exist_ok=True)
    return create_engine(database_url, connect_args=connect_args, future=True)


def init_db(database_url: Optional[str] = None):
    """Create (or recreate) engine + tables. Returns engine."""
    global _engine, _SessionLocal
    url = database_url or settings.database_url
    if _engine is not None:
        try:
            _engine.dispose()
        except Exception:
            pass
    _engine = _make_engine(url)
    _SessionLocal = sessionmaker(bind=_engine, autoflush=False, autocommit=False, expire_on_commit=False, class_=Session)
    Base.metadata.create_all(_engine)
    return _engine


def get_engine():
    if _engine is None:
        init_db()
    return _engine


def get_session_factory() -> sessionmaker:
    if _SessionLocal is None:
        init_db()
    assert _SessionLocal is not None
    return _SessionLocal


# session factory alias convenient for tests / callers
def SessionLocal() -> Session:  # noqa: N802 - factory-style name
    return get_session_factory()()


def get_session() -> Session:
    return get_session_factory()()


@contextmanager
def session_scope() -> Iterator[Session]:
    session = get_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def get_db() -> Iterator[Session]:
    session = get_session()
    try:
        yield session
    finally:
        session.close()


# --- Helpers ----------------------------------------------------------------

def get_or_create_repository(
    session: Session,
    owner: str,
    name: str,
    html_url: Optional[str] = None,
    metadata: Any = None,
) -> Repository:
    repo = session.execute(
        select(Repository).where(Repository.owner == owner, Repository.name == name)
    ).scalar_one_or_none()
    url = html_url or f"https://github.com/{owner}/{name}"
    metadata_json = None
    if metadata is not None:
        metadata_json = metadata if isinstance(metadata, str) else json.dumps(
            metadata.to_dict() if hasattr(metadata, "to_dict") else metadata
        )
    if repo is None:
        repo = Repository(owner=owner, name=name, html_url=url, metadata_json=metadata_json, updated_at=_utcnow())
        session.add(repo)
        session.flush()
    else:
        repo.html_url = url or repo.html_url
        if metadata_json is not None:
            repo.metadata_json = metadata_json
        repo.updated_at = _utcnow()
        session.flush()
    return repo


def get_repository(session: Session, owner: str, name: str) -> Optional[Repository]:
    return session.execute(
        select(Repository).where(Repository.owner == owner, Repository.name == name)
    ).scalar_one_or_none()


def latest_report(session: Session, owner: str, name: str) -> Optional[Report]:
    repo = get_repository(session, owner, name)
    if repo is None:
        return None
    return session.execute(
        select(Report).where(Report.repository_id == repo.id).order_by(Report.version.desc(), Report.id.desc())
    ).scalars().first()


def list_reports(
    session: Session,
    owner: Optional[str] = None,
    name: Optional[str] = None,
    limit: int = 50,
) -> list[Report]:
    stmt = select(Report).order_by(Report.created_at.desc(), Report.id.desc())
    if owner is not None and name is not None:
        repo = get_repository(session, owner, name)
        if repo is None:
            return []
        stmt = select(Report).where(Report.repository_id == repo.id).order_by(Report.version.desc(), Report.id.desc())
    elif owner is not None:
        stmt = stmt.join(Repository, Report.repository_id == Repository.id).where(Repository.owner == owner)
    if limit:
        stmt = stmt.limit(limit)
    return list(session.execute(stmt).scalars().all())


def ensure_catalog(session: Session, ecosystem: str, title: str, selection_note: str = "") -> Catalog:
    catalog = session.execute(select(Catalog).where(Catalog.ecosystem == ecosystem)).scalar_one_or_none()
    if catalog is None:
        catalog = Catalog(ecosystem=ecosystem, title=title, selection_note=selection_note, loaded_at=_utcnow())
        session.add(catalog)
        session.flush()
    else:
        catalog.title = title
        catalog.selection_note = selection_note
        catalog.loaded_at = _utcnow()
        session.flush()
    return catalog


def catalog_snapshot_for_repository(session: Session, owner: str, name: str) -> Optional[CatalogSnapshot]:
    """Best completed snapshot when a repository was checked in more than one catalog."""
    repo = get_repository(session, owner, name)
    if repo is None:
        return None
    return session.execute(
        select(CatalogSnapshot)
        .where(
            CatalogSnapshot.repository_id == repo.id,
            CatalogSnapshot.status == "completed",
            CatalogSnapshot.commit_sha != "",
        )
        .order_by(CatalogSnapshot.files_analysed.desc(), CatalogSnapshot.stars.desc(), CatalogSnapshot.id.desc())
    ).scalars().first()


def next_version(session: Session, repository_id: int) -> int:
    current = session.execute(
        select(func.max(Report.version)).where(Report.repository_id == repository_id)
    ).scalar_one_or_none()
    return int(current or 0) + 1
