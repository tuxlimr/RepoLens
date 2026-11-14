"""API tests — no network. GitHub fetch is monkeypatched; DB is temp sqlite."""
from __future__ import annotations

import sys
import types
from pathlib import Path

import pytest

# Make `app` importable whether pytest runs from repo root or backend/
BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

# --- Stub analyzer only if the real one is not present yet -----------------
try:
    import app.analyzer as _analyzer  # noqa: F401
    if not hasattr(_analyzer, "analyze_files"):
        raise ImportError("analyzer incomplete")
except Exception:
    stub = types.ModuleType("app.analyzer")
    from app.models import ArchitectureModel, Component, SourceRef

    def analyze_files(files, metadata=None):
        comp = Component(
            id="app", name="App", kind="entrypoint", responsibility="Demo app",
            paths=list(files)[:5], evidence=[SourceRef(path="main.py", start_line=1, end_line=3)],
        )
        return ArchitectureModel(
            components=[comp], entry_points=[SourceRef(path="main.py", start_line=1)],
            summary=f"Demo summary for {getattr(metadata, 'full_name', 'repo')}.",
        )

    def model_to_mermaid(model):
        return "flowchart TD\n    app[App]"

    def model_to_markdown(model, metadata=None):
        return f"# Architecture\n\n{model.summary}\n"

    stub.analyze_files = analyze_files
    stub.model_to_mermaid = model_to_mermaid
    stub.model_to_markdown = model_to_markdown
    sys.modules["app.analyzer"] = stub

from fastapi.testclient import TestClient  # noqa: E402

from app import db as db_module  # noqa: E402
from app import jobs  # noqa: E402
from app.main import app  # noqa: E402
from app.models import RepoMetadata  # noqa: E402

FAKE_SHA = "abc123deadbeef"
FAKE_FILES = {
    "main.py": "from fastapi import FastAPI\napp = FastAPI()\n\n@app.get('/')\ndef root():\n    return {'ok': True}\n",
    "requirements.txt": "fastapi\nhttpx\n",
    "README.md": "# Demo\nA demo repo.\n",
}


class FakeGitHubClient:
    """Matches the async GitHubClient surface used by jobs._fetch_with_client."""

    async def get_repo(self):
        return RepoMetadata(
            owner="psf", name="requests", full_name="psf/requests",
            html_url="https://github.com/psf/requests", description="Demo",
            stars=53000, forks=1000, language="Python", license="Apache-2.0",
            default_branch="main", commit_sha=FAKE_SHA, topics=["http"],
        )

    async def get_head_sha(self, branch=None):
        return FAKE_SHA

    async def get_tree(self, sha=None):
        return [{"type": "blob", "path": p, "sha": "blob1", "size": len(c)} for p, c in FAKE_FILES.items()]

    async def fetch_text_files(self, tree=None):
        return dict(FAKE_FILES)


@pytest.fixture()
def client(tmp_path, monkeypatch):
    db_module.init_db(f"sqlite:///{tmp_path / 'test.db'}")
    monkeypatch.setattr(jobs, "get_client", lambda owner, repo: FakeGitHubClient())
    # Ensure synthesis never hits network in tests (settings is frozen)
    import app.synthesis as synthesis_module
    monkeypatch.setattr(synthesis_module, "polish_summary", lambda model, metadata=None: getattr(model, "summary", ""))
    with TestClient(app) as c:
        yield c
    db_module.init_db(f"sqlite:///{tmp_path / 'teardown.db'}")


def _analysis_count() -> int:
    from sqlalchemy import func, select
    session = db_module.get_session()
    try:
        return session.execute(select(func.count()).select_from(db_module.Analysis)).scalar_one()
    finally:
        session.close()


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_bad_url_422(client):
    for bad in ["not-a-url", "https://gitlab.com/a/b", "https://github.com/onlyowner", ""]:
        resp = client.post("/api/analyze", json={"url": bad})
        assert resp.status_code == 422, (bad, resp.text)


def test_analyze_completed_and_cached_flow(client):
    resp = client.post("/api/analyze", json={"url": "https://github.com/psf/requests"})
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["status"] == "queued"
    analysis_id = body["analysis_id"]

    # Background task should have completed by now (TestClient runs it)
    status = client.get(f"/api/analyses/{analysis_id}")
    assert status.status_code == 200
    assert status.json()["status"] == "completed", status.json()

    # Report retrievable
    report_resp = client.get("/api/reports/psf/requests")
    assert report_resp.status_code == 200, report_resp.text
    report = report_resp.json()
    assert report["version"] == 1
    assert report["commit_sha"] == FAKE_SHA
    assert report["repository"]["full_name"] == "psf/requests"
    assert report["mermaid"]
    assert report["markdown"]
    assert report["model"]["components"]

    # Versions + markdown download + repository + recent list
    versions = client.get("/api/reports/psf/requests/versions")
    assert versions.status_code == 200 and len(versions.json()) == 1
    md = client.get("/api/reports/psf/requests/markdown")
    assert md.status_code == 200
    assert "attachment" in md.headers.get("content-disposition", "")
    assert md.text == report["markdown"]
    assert client.get("/api/repositories/psf/requests").json()["full_name"] == "psf/requests"
    recent = client.get("/api/reports").json()
    assert any(r["owner"] == "psf" and r["name"] == "requests" for r in recent)

    # Cached flow: no new analysis created
    before = _analysis_count()
    cached = client.post("/api/analyze", json={"url": "https://github.com/psf/requests"})
    assert cached.status_code == 200
    assert cached.json()["status"] == "cached"
    assert cached.json()["report"]["version"] == 1
    assert _analysis_count() == before


def test_catalog_snapshot_is_served_as_cached_report(client):
    session = db_module.get_session()
    try:
        catalog = db_module.ensure_catalog(session, "python", "Python catalog", "test corpus")
        repo = db_module.get_or_create_repository(
            session, "demo", "widget", html_url="https://github.com/demo/widget",
            metadata={"owner": "demo", "name": "widget", "full_name": "demo/widget", "stars": 9000, "commit_sha": "a" * 40},
        )
        session.add(db_module.CatalogSnapshot(
            catalog_id=catalog.id,
            repository_id=repo.id,
            commit_sha="a" * 40,
            stars=9000,
            status="completed",
            report_markdown="# Architecture report: demo/widget\n\ncommit " + ("a" * 40),
            structure_markdown="# Project structure\n\n**Analysed commit:** `" + ("a" * 40) + "`",
            mermaid="%% Analysed commit: " + ("a" * 40) + "\nflowchart TD\n    app[App]",
            model_json='{"components":[{"id":"app","name":"App","kind":"core","responsibility":"Demo","paths":[],"evidence":[],"confidence":0.6,"inferred":false}],"relationships":[],"detections":[],"entry_points":[],"files":[],"limitations":[],"summary":"A widget.","stats":{}}',
        ))
        session.commit()
    finally:
        session.close()

    before = _analysis_count()
    cached = client.post("/api/analyze", json={"url": "https://github.com/demo/widget"})
    assert cached.status_code == 200, cached.text
    assert cached.json()["status"] == "cached"
    assert cached.json()["report"]["commit_sha"] == "a" * 40
    assert cached.json()["report"]["source"] == "catalog"
    assert _analysis_count() == before

    report = client.get("/api/reports/demo/widget")
    assert report.status_code == 200
    assert report.json()["markdown"].startswith("# Architecture report")
    assert client.get("/api/reports/demo/widget/markdown").status_code == 200
    catalogs = client.get("/api/catalogs").json()
    assert any(item["ecosystem"] == "python" and item["completed"] == 1 for item in catalogs)


def test_report_not_found(client):
    assert client.get("/api/reports/nope/missing").status_code == 404
    assert client.get("/api/repositories/nope/missing").status_code == 404
    assert client.get("/api/analyses/9999").status_code == 404


def test_payments_fresh_creates_mock_payment_and_queues(client):
    resp = client.post("/api/payments/fresh", json={"url": "https://github.com/psf/requests.git"})
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["status"] == "queued"
    assert body["analysis_id"]
    payment = body["payment"]
    assert payment["provider"] == "mock"
    assert payment["status"] == "mock_paid"
    assert payment["amount_cents"] > 0
    assert "no real charge" in payment["note"].lower()
    # Analysis completed via background task and produced a report
    assert client.get(f"/api/analyses/{body['analysis_id']}").json()["status"] == "completed"
    session = db_module.get_session()
    try:
        from sqlalchemy import select
        payments = session.execute(select(db_module.Payment)).scalars().all()
        assert len(payments) == 1 and payments[0].analysis_id == body["analysis_id"]
    finally:
        session.close()


def test_examples(client):
    resp = client.get("/api/examples")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) >= 5
    assert all(e["stars"] > 5000 for e in data)
    names = {e["repo"] for e in data}
    assert {"requests", "fastapi", "django", "flask", "pandas"} <= names


def test_parse_github_url_variants():
    from app.github_client import parse_github_url
    assert parse_github_url("https://github.com/psf/requests") == ("psf", "requests")
    assert parse_github_url("https://github.com/psf/requests/") == ("psf", "requests")
    assert parse_github_url("https://github.com/psf/requests.git") == ("psf", "requests")
    assert parse_github_url("github.com/psf/requests") == ("psf", "requests")
    with pytest.raises(ValueError):
        parse_github_url("https://example.com/psf/requests")
    with pytest.raises(ValueError):
        parse_github_url("https://github.com/psf")
