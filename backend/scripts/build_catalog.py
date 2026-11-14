"""Check public Python repositories and write structure.md plus the report set.

Each successful repository gets four files under catalog/repos/<owner>/<name>/:

- structure.md  — directory structure, entry points, components
- report.md     — full architecture report (12 sections, Mermaid included)
- diagram.mmd   — Mermaid block diagram
- meta.json     — metadata, including the analysed commit SHA

Every document names the commit that was downloaded. The run resumes from
catalog/_state.json and stops after CATALOG_TARGET successes (default 500).

Usage (from the backend directory):

    python scripts/build_catalog.py
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

import httpx

BACKEND = Path(__file__).resolve().parents[1]
ROOT = BACKEND.parent
sys.path.insert(0, str(BACKEND))

from app.analyzer import (  # noqa: E402
    analyze_files,
    model_to_mermaid,
    model_to_markdown,
    model_to_structure_md,
)
from app.github_client import GitHubClient, GithubError  # noqa: E402
from app.models import RepoMetadata  # noqa: E402

CATALOG = ROOT / "catalog"
REPOS = CATALOG / "repos"
STATE_PATH = CATALOG / "_state.json"
TARGET = int(os.environ.get("CATALOG_TARGET", "500"))
CONCURRENCY = int(os.environ.get("CATALOG_CONCURRENCY", "3"))
# GitHub `size` is kilobytes. Keep snapshots inside the analyser's archive budget
# so a check produces a real tree, report, and commit SHA instead of a rejection.
ECOSYSTEMS = {
    "python": {
        "dir": ROOT / "catalog",
        "title": "RepoLens Python catalog",
        "note": "Selection: `language:python`, `fork:false`, GitHub size under 50 MB, `stars:>5000`, highest stars first. A 2,500–5,000 star band is used only if that is not enough to reach the target.",
        "queries": [
            "language:python stars:>5000 fork:false size:<50000",
            "language:python stars:2500..5000 fork:false size:<50000",
        ],
    },
    "javascript": {
        "dir": ROOT / "catalog" / "javascript",
        "title": "RepoLens JavaScript catalog",
        "note": "Selection: `language:javascript`, `fork:false`, GitHub size under 50 MB, `stars:>5000`, highest stars first. A 2,000–5,000 star band is used only if that is not enough to reach the target.",
        "queries": [
            "language:javascript stars:>5000 fork:false size:<50000",
            "language:javascript stars:2000..5000 fork:false size:<50000",
        ],
    },
    "react": {
        "dir": ROOT / "catalog" / "react",
        "title": "RepoLens React catalog",
        "note": "Selection: GitHub topic `react` (JavaScript and TypeScript), `fork:false`, GitHub size under 50 MB, `stars:>5000`, highest stars first. Lower star bands (down to 1,000) are used only if that is not enough to reach the target.",
        "queries": [
            "topic:react stars:>5000 fork:false size:<50000",
            "topic:react stars:2000..5000 fork:false size:<50000",
            "topic:react stars:1000..2000 fork:false size:<50000",
        ],
    },
}
ECOSYSTEM_NAME = "python"
ECOSYSTEM_TITLE = ECOSYSTEMS["python"]["title"]
SELECTION_NOTE = ECOSYSTEMS["python"]["note"]
QUERIES = ECOSYSTEMS["python"]["queries"]
SKIP_STATUSES = {"completed", "too_large", "not_found"}
HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "RepoLens/0.1 (architecture catalog; static analysis only)",
    "X-GitHub-Api-Version": "2022-11-28",
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"successes": 0, "results": {}}


def _save_state(state: dict) -> None:
    CATALOG.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2), encoding="utf-8")
    tmp.replace(STATE_PATH)


def _classify(exc: BaseException) -> str:
    msg = str(exc).lower()
    if "too large" in msg:
        return "too_large"
    if "not found" in msg or "404" in msg:
        return "not_found"
    if "rate limit" in msg or "429" in msg or "403" in msg:
        return "rate_limit"
    if "timeout" in msg or "timed out" in msg:
        return "timeout"
    return "error"


def _parse_item(item: dict) -> dict:
    full = item["full_name"]
    owner, name = full.split("/", 1)
    lic = item.get("license") or {}
    spdx = None
    if isinstance(lic, dict):
        spdx = lic.get("spdx_id")
        if spdx in (None, "NOASSERTION"):
            spdx = lic.get("name")
    return {
        "owner": owner,
        "name": name,
        "full_name": full,
        "html_url": item.get("html_url") or f"https://github.com/{full}",
        "description": item.get("description"),
        "stars": int(item.get("stargazers_count") or 0),
        "forks": int(item.get("forks_count") or 0),
        "language": item.get("language") or "Python",
        "license": spdx,
        "default_branch": item.get("default_branch") or "HEAD",
        "topics": list(item.get("topics") or []),
        "archived": bool(item.get("archived")),
    }


async def _search_page(client: httpx.AsyncClient, query: str, page: int) -> list[dict]:
    delay = 3.0
    for _attempt in range(6):
        resp = await client.get(
            "https://api.github.com/search/repositories",
            params={"q": query, "sort": "stars", "order": "desc", "per_page": 100, "page": page},
            headers=HEADERS,
        )
        if resp.status_code == 200:
            remaining = resp.headers.get("x-ratelimit-remaining")
            if remaining == "0":
                reset = int(resp.headers.get("x-ratelimit-reset") or "0")
                wait = max(1, reset - int(datetime.now(timezone.utc).timestamp()) + 1)
                print(f"search rate limit hit; sleeping {wait}s", flush=True)
                await asyncio.sleep(min(wait, 70))
            return list(resp.json().get("items") or [])
        if resp.status_code in (403, 429):
            retry = resp.headers.get("retry-after")
            wait = float(retry) if retry else delay
            print(f"search throttled ({resp.status_code}); sleeping {wait:.0f}s", flush=True)
            await asyncio.sleep(wait)
            delay = min(delay * 2, 60)
            continue
        if resp.status_code == 422:
            return []
        resp.raise_for_status()
    return []


def _write_index(state: dict) -> None:
    results = state.get("results") or {}
    done = [r for r in results.values() if r.get("status") == "completed" and r.get("commit_sha")]
    done.sort(key=lambda r: (-int(r.get("stars") or 0), r.get("full_name") or ""))
    failed = [r for r in results.values() if r.get("status") != "completed"]
    failed.sort(key=lambda r: (-int(r.get("stars") or 0), r.get("full_name") or ""))
    lines = [
        f"# {ECOSYSTEM_TITLE}",
        "",
        "Repositories checked with static analysis only (repository code was not executed).",
        "Every completed row is pinned to the **commit that was downloaded**.",
        "",
        f"- Completed snapshots: **{len(done)}**",
        f"- Checked without a full snapshot: **{len(failed)}** (archive over the size limit, missing, or error)",
        f"- {SELECTION_NOTE}",
        "",
        "| # | Repository | Stars | Analysed commit | Structure | Report | Diagram |",
        "| --- | --- | ---: | --- | --- | --- | --- |",
    ]
    for i, row in enumerate(done, start=1):
        owner, name = row["owner"], row["name"]
        sha = row["commit_sha"]
        rel = f"repos/{owner}/{name}"
        commit_url = f"https://github.com/{owner}/{name}/commit/{sha}"
        repo_url = row.get("html_url") or f"https://github.com/{owner}/{name}"
        lines.append(
            f"| {i} | [{owner}/{name}]({repo_url}) | {row.get('stars', 0)} | "
            f"[`{sha}`]({commit_url}) | [structure.md]({rel}/structure.md) | "
            f"[report.md]({rel}/report.md) | [diagram.mmd]({rel}/diagram.mmd) |"
        )
    lines += ["", "## Checked, no full snapshot", ""]
    if not failed:
        lines.append("None.")
    else:
        lines += [
            "| Repository | Stars | Commit | Status | Detail |",
            "| --- | ---: | --- | --- | --- |",
        ]
        for row in failed:
            sha = row.get("commit_sha") or ""
            commit = f"`{sha}`" if sha else "—"
            detail = (row.get("error") or "").replace("|", "/")[:180]
            lines.append(
                f"| {row.get('full_name')} | {row.get('stars', 0)} | {commit} | {row.get('status')} | {detail} |"
            )
    lines.append("")
    CATALOG.mkdir(parents=True, exist_ok=True)
    text = "\n".join(lines)
    (CATALOG / "INDEX.md").write_text(text, encoding="utf-8")
    commits = ["full_name\tstars\tcommit_sha\tstatus"]
    for row in sorted(results.values(), key=lambda r: (-int(r.get("stars") or 0), r.get("full_name") or "")):
        commits.append(
            f"{row.get('full_name')}\t{row.get('stars', 0)}\t{row.get('commit_sha') or ''}\t{row.get('status')}"
        )
    (CATALOG / "commits.tsv").write_text("\n".join(commits) + "\n", encoding="utf-8")


async def _analyse_one(item: dict, state: dict, lock: asyncio.Lock) -> None:
    full = item["full_name"]
    async with lock:
        if state["successes"] >= TARGET:
            return
        previous = state["results"].get(full)
        if previous and previous.get("status") in SKIP_STATUSES:
            return
        state["results"][full] = {**item, "status": "in_progress", "started_at": _now()}
    owner, name = item["owner"], item["name"]
    client = GitHubClient(owner, name, timeout=180)
    try:
        files = None
        last_exc: Exception | None = None
        for attempt in range(3):
            try:
                client = GitHubClient(owner, name, timeout=180)
                files = await client.fetch_files_via_tarball(None, owner, name)
                last_exc = None
                break
            except (GithubError, httpx.HTTPError, TimeoutError) as exc:
                last_exc = exc
                if _classify(exc) not in {"rate_limit", "timeout"}:
                    raise
                await asyncio.sleep(8 * (attempt + 1))
        if last_exc is not None or files is None:
            raise last_exc or GithubError(f"no files returned for {full}")
        sha = getattr(client, "last_tarball_sha", None)
        if not sha or len(sha) < 40:
            raise GithubError(f"commit SHA was not resolved for {full}")
        metadata = RepoMetadata(
            owner=owner,
            name=name,
            full_name=full,
            html_url=item["html_url"],
            description=item.get("description"),
            stars=item["stars"],
            forks=item["forks"],
            language=item.get("language") or "Python",
            license=item.get("license"),
            default_branch=item.get("default_branch") or "HEAD",
            commit_sha=sha,
            topics=list(item.get("topics") or []),
            retrieved_at=_now(),
        )
        model = await asyncio.to_thread(analyze_files, files, metadata)
        if item.get("archived"):
            model.limitations.append("The GitHub repository was marked archived at selection time.")
        structure = model_to_structure_md(model, metadata)
        report = model_to_markdown(model, metadata)
        diagram = (
            f"%% Repository: {full}\n"
            f"%% Analysed commit: {sha}\n"
            f"%% Commit reference: {item['html_url'].rstrip('/')}/commit/{sha}\n"
            + model_to_mermaid(model)
        )
        if sha not in structure or sha not in report or sha not in diagram:
            raise RuntimeError("generated documents are missing the analysed commit SHA")
        out = REPOS / owner / name
        out.mkdir(parents=True, exist_ok=True)
        (out / "structure.md").write_text(structure, encoding="utf-8")
        (out / "report.md").write_text(report, encoding="utf-8")
        (out / "diagram.mmd").write_text(diagram, encoding="utf-8")
        meta_doc = {
            "owner": owner,
            "name": name,
            "full_name": full,
            "html_url": item["html_url"],
            "description": item.get("description"),
            "stars": item["stars"],
            "forks": item["forks"],
            "license": item.get("license"),
            "language": item.get("language"),
            "default_branch": item.get("default_branch"),
            "topics": item.get("topics") or [],
            "archived": item.get("archived", False),
            "commit_sha": sha,
            "commit_url": f"{item['html_url'].rstrip('/')}/commit/{sha}",
            "tree_url": f"{item['html_url'].rstrip('/')}/tree/{sha}",
            "analysed_at": metadata.retrieved_at,
            "status": "completed",
            "files_fetched": len(files),
            "files_analysed": len(model.files),
            "components": [c.name for c in model.components],
            "detections": [d.name for d in model.detections],
            "entry_points": [ref.path for ref in model.entry_points],
        }
        (out / "meta.json").write_text(json.dumps(meta_doc, indent=2), encoding="utf-8")
        async with lock:
            state["results"][full] = {**item, **meta_doc, "status": "completed", "error": None}
            state["successes"] = sum(1 for r in state["results"].values() if r.get("status") == "completed")
            successes = state["successes"]
            _save_state(state)
            if successes % 10 == 0 or successes >= TARGET:
                _write_index(state)
        print(f"[{successes}/{TARGET}] ok {full} {sha[:12]} files={len(model.files)}", flush=True)
    except Exception as exc:
        status = _classify(exc)
        sha = getattr(client, "last_tarball_sha", None)
        message = str(exc).replace("\n", " ")[:300]
        async with lock:
            state["results"][full] = {
                **item,
                "status": status,
                "commit_sha": sha,
                "error": message,
                "finished_at": _now(),
            }
            state["successes"] = sum(1 for r in state["results"].values() if r.get("status") == "completed")
            _save_state(state)
        print(f"[--/{TARGET}] {status} {full} {sha or '-'} {message[:140]}", flush=True)
        if status == "error":
            traceback.print_exc()


async def _run() -> None:
    CATALOG.mkdir(parents=True, exist_ok=True)
    state = _load_state()
    state["successes"] = sum(1 for r in state.get("results", {}).values() if r.get("status") == "completed")
    print(f"resume ecosystem={ECOSYSTEM_NAME} successes={state['successes']} target={TARGET} concurrency={CONCURRENCY}", flush=True)
    lock = asyncio.Lock()
    sem = asyncio.Semaphore(CONCURRENCY)
    queued = {k for k, v in state.get("results", {}).items() if v.get("status") in SKIP_STATUSES}

    async def guarded(item: dict) -> None:
        async with sem:
            async with lock:
                if state["successes"] >= TARGET:
                    return
            try:
                await asyncio.wait_for(_analyse_one(item, state, lock), timeout=240)
            except asyncio.TimeoutError:
                full = item["full_name"]
                async with lock:
                    if state["results"].get(full, {}).get("status") != "completed":
                        state["results"][full] = {**item, "status": "timeout", "error": "analysis exceeded 240s", "finished_at": _now()}
                        _save_state(state)
                print(f"[--/{TARGET}] timeout {full}", flush=True)

    async with httpx.AsyncClient(timeout=60, follow_redirects=True) as http:
        for query in QUERIES:
            if state["successes"] >= TARGET:
                break
            print(f"query: {query}", flush=True)
            for page in range(1, 11):
                if state["successes"] >= TARGET:
                    break
                items = await _search_page(http, query, page)
                if not items:
                    print(f"no more results for page {page}", flush=True)
                    break
                pending = []
                for raw in items:
                    item = _parse_item(raw)
                    if item["full_name"] in queued:
                        continue
                    queued.add(item["full_name"])
                    pending.append(asyncio.create_task(guarded(item)))
                if pending:
                    await asyncio.gather(*pending)
                print(f"page {page} done; successes={state['successes']}", flush=True)
                if state["successes"] >= TARGET:
                    break
    _write_index(state)
    print(f"finished ecosystem={ECOSYSTEM_NAME} successes={state['successes']} index={CATALOG / 'INDEX.md'}", flush=True)


def _bind(name: str) -> None:
    global CATALOG, REPOS, STATE_PATH, QUERIES, ECOSYSTEM_NAME, ECOSYSTEM_TITLE, SELECTION_NOTE
    cfg = ECOSYSTEMS[name]
    CATALOG = cfg["dir"]
    REPOS = CATALOG / "repos"
    STATE_PATH = CATALOG / "_state.json"
    QUERIES = cfg["queries"]
    ECOSYSTEM_NAME = name
    ECOSYSTEM_TITLE = cfg["title"]
    SELECTION_NOTE = cfg["note"]


def _write_overview() -> None:
    lines = [
        "# RepoLens catalogs",
        "",
        "Static checks only: repository code was not executed. Each completed repository has `structure.md`, `report.md`, `diagram.mmd`, and `meta.json`, pinned to the downloaded commit.",
        "",
    ]
    for name, cfg in ECOSYSTEMS.items():
        state_path = cfg["dir"] / "_state.json"
        count = 0
        if state_path.exists():
            data = json.loads(state_path.read_text(encoding="utf-8"))
            count = sum(1 for row in data.get("results", {}).values() if row.get("status") == "completed" and row.get("commit_sha"))
        rel = "INDEX.md" if name == "python" else f"{name}/INDEX.md"
        lines.append(f"- **{name}**: {count} completed snapshots — [{rel}]({rel})")
    lines.append("")
    overview = ROOT / "catalog" / "OVERVIEW.md"
    overview.parent.mkdir(parents=True, exist_ok=True)
    overview.write_text("\n".join(lines), encoding="utf-8")


async def _main(names: list[str]) -> None:
    for name in names:
        _bind(name)
        print(f"=== ecosystem {name} ===", flush=True)
        await _run()
        _write_overview()


if __name__ == "__main__":
    choice = sys.argv[1] if len(sys.argv) > 1 else "all"
    if choice == "all":
        selected = list(ECOSYSTEMS)
    elif choice in ECOSYSTEMS:
        selected = [choice]
    else:
        raise SystemExit(f"unknown ecosystem {choice!r}; choose all, python, javascript, or react")
    asyncio.run(_main(selected))
