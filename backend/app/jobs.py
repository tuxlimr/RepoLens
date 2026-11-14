"""Background analysis jobs. NEVER executes repository code."""
from __future__ import annotations

import asyncio
import inspect
import json
import logging
import re
from datetime import datetime, timezone
from typing import Any, Callable, Optional

from app import db as db_module
from app.db import Analysis, Report, Repository
from app.github_client import GitHubClient
from app.models import RepoMetadata

logger = logging.getLogger(__name__)

TOOL_VERSION = "0.1.0"


def get_client(owner: str, repo: str) -> GitHubClient:
    """Module-level factory — tests can monkeypatch this."""
    return GitHubClient(owner, repo)


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _sanitise_error(exc: BaseException) -> str:
    msg = str(exc) or exc.__class__.__name__
    # Strip anything token-like
    msg = re.sub(r"(ghp|gho|github_pat)_[A-Za-z0-9_]+", "[redacted]", msg)
    msg = re.sub(r"Bearer\s+\S+", "Bearer [redacted]", msg, flags=re.I)
    msg = re.sub(r"(token|api[_-]?key|secret|password)\s*[:=]\s*\S+", r"\1=[redacted]", msg, flags=re.I)
    return msg[:500]


def fill_source_ref_urls(model: Any, owner: str, repo: str, sha: Optional[str]) -> None:
    if not sha:
        return
    base = f"https://github.com/{owner}/{repo}/blob/{sha}"

    def fill(ref: Any) -> None:
        path = ref.get("path") if isinstance(ref, dict) else getattr(ref, "path", None)
        if not path:
            return
        start = ref.get("start_line") if isinstance(ref, dict) else getattr(ref, "start_line", None)
        end = ref.get("end_line") if isinstance(ref, dict) else getattr(ref, "end_line", None)
        url = f"{base}/{path}"
        if start:
            url += f"#L{start}"
            if end and end != start:
                url += f"-L{end}"
        if isinstance(ref, dict):
            ref["url"] = url
        else:
            try:
                ref.url = url
            except Exception:
                pass

    for comp in getattr(model, "components", []) or []:
        evidence = comp.get("evidence", []) if isinstance(comp, dict) else getattr(comp, "evidence", [])
        for ref in evidence or []:
            fill(ref)
    for det in getattr(model, "detections", []) or []:
        evidence = det.get("evidence", []) if isinstance(det, dict) else getattr(det, "evidence", [])
        for ref in evidence or []:
            fill(ref)
    for ref in getattr(model, "entry_points", []) or []:
        fill(ref)


async def _maybe_await(value):
    if inspect.isawaitable(value):
        return await value
    return value


async def _call_first_ok(func: Callable, arg_options: list[tuple]):
    """Try calling func with each arg tuple until one doesn't raise TypeError."""
    last_type_error = None
    for args in arg_options:
        try:
            return await _maybe_await(func(*args))
        except TypeError as exc:
            last_type_error = exc
            continue
    if last_type_error is not None:
        raise last_type_error
    return await _maybe_await(func())


async def _fetch_with_client(client: Any, owner: str, repo: str):
    try:
        metadata = await _call_first_ok(client.get_repo, [(owner, repo), ()])
    except Exception:
        # GitHub core-API rate limit (60/hr unauthenticated) must not block
        # analysis: codeload tarball download is a separate quota. Fall back
        # to minimal metadata; the report states this limitation explicitly.
        logger.warning("GitHub metadata fetch failed for %s/%s; using minimal metadata", owner, repo)
        metadata = RepoMetadata(
            owner=owner, name=repo, full_name=f"{owner}/{repo}",
            html_url=f"https://github.com/{owner}/{repo}", default_branch="HEAD",
        )
        metadata.__dict__["_metadata_fallback"] = True
    branch = getattr(metadata, "default_branch", None) or "main"
    sha = None
    if hasattr(client, "get_head_sha"):
        try:
            sha = await _call_first_ok(client.get_head_sha, [(branch, owner, repo), (branch,), ()])
        except Exception:
            sha = getattr(metadata, "commit_sha", None)
    if sha and hasattr(metadata, "commit_sha"):
        try:
            metadata.commit_sha = sha
        except Exception:
            pass
    files: dict[str, str] = {}
    if hasattr(client, "fetch_files_via_tarball"):
        # Preferred: one codeload request, avoids per-file API rate limits.
        files = await _call_first_ok(client.fetch_files_via_tarball, [(sha, owner, repo), (sha,)])
    elif hasattr(client, "get_tree") and hasattr(client, "fetch_text_files"):
        tree = await _call_first_ok(client.get_tree, [(sha, owner, repo), (sha,)])
        files = await _call_first_ok(client.fetch_text_files, [(tree, owner, repo, sha), (tree, owner, repo), (tree,)])
    elif hasattr(client, "fetch_text_files"):
        files = await _call_first_ok(client.fetch_text_files, [([], owner, repo, sha), (owner, repo), ()])
    if not sha:
        sha = getattr(client, "last_tarball_sha", None)
        if sha and hasattr(metadata, "commit_sha"):
            try:
                metadata.commit_sha = sha
            except Exception:
                pass
    return metadata, files, sha


def _normalise_fetch_result(result: Any):
    """fetch_override may return (metadata, files), (metadata, files, sha), or dict."""
    if isinstance(result, dict) and "metadata" in result:
        metadata = result["metadata"]
        files = result.get("files") or {}
        sha = result.get("sha") or result.get("commit_sha") or getattr(metadata, "commit_sha", None)
        return metadata, files, sha
    if isinstance(result, (tuple, list)):
        if len(result) == 3:
            return result[0], result[1], result[2]
        if len(result) == 2:
            metadata, files = result
            return metadata, files, getattr(metadata, "commit_sha", None)
    raise ValueError("fetch_override must return (metadata, files) or (metadata, files, sha)")


def run_analysis(analysis_id: int, client: Any = None, fetch_override: Optional[Callable] = None) -> Optional[int]:
    """Run one analysis synchronously. Returns report id or None on failure."""
    session = db_module.get_session()
    try:
        analysis = session.get(Analysis, analysis_id)
        if analysis is None:
            return None
        repo_row = session.get(Repository, analysis.repository_id)
        if repo_row is None:
            analysis.status = "failed"
            analysis.error = "Repository not found"
            analysis.finished_at = _utcnow()
            session.commit()
            return None
        owner, name = repo_row.owner, repo_row.name
        analysis.status = "running"
        analysis.tool_version = TOOL_VERSION
        session.commit()

        # --- Fetch ---
        if fetch_override is not None:
            result = fetch_override(owner, name)
            if inspect.isawaitable(result):
                result = asyncio.run(_maybe_await(result))
            metadata, files, sha = _normalise_fetch_result(result)
        else:
            effective_client = client if client is not None else get_client(owner, name)
            metadata, files, sha = asyncio.run(_fetch_with_client(effective_client, owner, name))

        if metadata is None:
            metadata = RepoMetadata(owner=owner, name=name, full_name=f"{owner}/{name}", html_url=f"https://github.com/{owner}/{name}")
        files = files or {}
        sha = sha or getattr(metadata, "commit_sha", None)
        branch = getattr(metadata, "default_branch", None)

        # --- Analyse (static only) ---
        from app.analyzer import analyze_files, model_to_markdown, model_to_mermaid

        model = analyze_files(files, metadata)
        if getattr(metadata, "__dict__", {}).get("_metadata_fallback"):
            model.limitations.append(
                "Repository metadata (stars, description, licence) was unavailable because the GitHub API rate limit was reached; analysis used the repository archive at HEAD with minimal metadata."
            )
        fill_source_ref_urls(model, owner, name, sha)

        # --- Optional LLM polish (no-op without key, never fatal) ---
        try:
            from app.synthesis import polish_summary
            polished = polish_summary(model, metadata)
            if polished:
                model.summary = polished
        except Exception:
            logger.warning("Synthesis failed, keeping deterministic summary", exc_info=True)

        mermaid = model_to_mermaid(model)
        markdown = model_to_markdown(model, metadata)

        # --- Persist ---
        version = db_module.next_version(session, repo_row.id)
        metadata_dict = metadata.to_dict() if hasattr(metadata, "to_dict") else dict(metadata)  # type: ignore[arg-type]
        if sha and not metadata_dict.get("commit_sha"):
            metadata_dict["commit_sha"] = sha
        model_dict = model.to_dict() if hasattr(model, "to_dict") else model
        repo_row.metadata_json = json.dumps(metadata_dict)
        repo_row.html_url = metadata_dict.get("html_url") or repo_row.html_url
        repo_row.updated_at = _utcnow()

        report = Report(
            analysis_id=analysis.id,
            repository_id=repo_row.id,
            commit_sha=sha,
            version=version,
            markdown=markdown or "",
            mermaid=mermaid or "",
            model_json=json.dumps(model_dict),
            metadata_json=json.dumps(metadata_dict),
        )
        session.add(report)
        session.flush()
        analysis.commit_sha = sha
        analysis.branch = branch
        analysis.status = "completed"
        analysis.error = None
        analysis.finished_at = _utcnow()
        session.commit()
        return report.id
    except Exception as exc:
        logger.exception("Analysis %s failed", analysis_id)
        try:
            session.rollback()
            analysis = session.get(Analysis, analysis_id)
            if analysis is not None:
                analysis.status = "failed"
                analysis.error = _sanitise_error(exc)
                analysis.finished_at = _utcnow()
                session.commit()
        except Exception:
            session.rollback()
        return None
    finally:
        session.close()
