"""GitHub API client (async, httpx). Never executes repository code."""
from __future__ import annotations

import base64
import re
from datetime import datetime, timezone
from typing import Any, Optional
from urllib.parse import urlparse

import httpx

from app.config import settings
from app.models import RepoMetadata

BINARY_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico", ".webp", ".svgz",
    ".pdf", ".zip", ".tar", ".gz", ".bz2", ".xz", ".7z", ".rar",
    ".exe", ".dll", ".so", ".dylib", ".bin", ".dat", ".class", ".pyc",
    ".pyo", ".o", ".a", ".jar", ".war", ".mp3", ".mp4", ".mov", ".avi",
    ".woff", ".woff2", ".ttf", ".eot", ".otf", ".db", ".sqlite", ".sqlite3",
    ".pickle", ".pkl", ".npy", ".npz", ".parquet", ".feather", ".wasm",
    ".min.js", ".map",
}

_OWNER_REPO_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")


class GithubError(Exception):
    """Raised for GitHub API failures with a user-safe message."""


def parse_github_url(url: str) -> tuple[str, str]:
    """Parse a GitHub repo URL into (owner, repo). Raises ValueError."""
    if not url or not isinstance(url, str):
        raise ValueError("Invalid GitHub URL")
    raw = url.strip()
    if not raw:
        raise ValueError("Invalid GitHub URL")
    # Allow schemeless github.com/owner/repo
    candidate = raw if "://" in raw else f"https://{raw}"
    parsed = urlparse(candidate)
    host = (parsed.hostname or "").lower()
    if host not in ("github.com", "www.github.com"):
        raise ValueError("Only github.com repository URLs are supported")
    if parsed.scheme not in ("https", "http"):
        raise ValueError("Invalid GitHub URL")
    parts = [p for p in parsed.path.split("/") if p != ""]
    if len(parts) != 2:
        raise ValueError("GitHub URL must be of the form https://github.com/owner/repo")
    owner, repo = parts
    if repo.endswith(".git"):
        repo = repo[:-4]
    if not owner or not repo or not _OWNER_REPO_RE.match(owner) or not _OWNER_REPO_RE.match(repo):
        raise ValueError("Invalid GitHub owner or repository name")
    if repo in (".", "..") or owner in (".", ".."):
        raise ValueError("Invalid GitHub owner or repository name")
    return owner, repo


def _is_binary_path(path: str) -> bool:
    lower = path.lower()
    return any(lower.endswith(ext) for ext in BINARY_EXTENSIONS)


class GitHubClient:
    """Async GitHub client. May be bound to owner/repo or pass them per-call."""

    def __init__(
        self,
        owner: Optional[str] = None,
        repo: Optional[str] = None,
        token: Optional[str] = None,
        timeout: float = 30.0,
        transport: Optional[httpx.AsyncBaseTransport] = None,
    ):
        self.owner = owner
        self.repo = repo
        self.token = token if token is not None else settings.github_token
        self.timeout = timeout
        self.transport = transport
        self.base_url = "https://api.github.com"

    def _resolve(self, owner: Optional[str], repo: Optional[str]) -> tuple[str, str]:
        o = owner or self.owner
        r = repo or self.repo
        if not o or not r:
            raise GithubError("GitHub owner and repository are required")
        return o, r

    def _headers(self, extra: Optional[dict] = None) -> dict[str, str]:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "RepoLens/0.1 (+https://github.com)",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if extra:
            headers.update(extra)
        return headers

    def _handle_error(self, resp: httpx.Response, owner: str, repo: str) -> None:
        if resp.status_code == 404:
            raise GithubError(f"Repository {owner}/{repo} not found (it may be private or does not exist)")
        if resp.status_code in (403, 429):
            remaining = resp.headers.get("x-ratelimit-remaining", "")
            # GitHub returns 403 for rate limit as well as abuse/forbidden
            if remaining == "0" or resp.status_code == 429 or "rate limit" in resp.text.lower():
                raise GithubError("GitHub API rate limit exceeded; try again later or provide a GITHUB_TOKEN")
            raise GithubError("GitHub API request forbidden (403); the repository may be private or rate-limited")
        if resp.status_code >= 400:
            raise GithubError(f"GitHub API error ({resp.status_code}) for {owner}/{repo}")

    async def _get_json(self, client: httpx.AsyncClient, path: str, owner: str, repo: str) -> Any:
        resp = await client.get(f"{self.base_url}{path}", headers=self._headers())
        self._handle_error(resp, owner, repo)
        return resp.json()

    def _client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(timeout=self.timeout, transport=self.transport, follow_redirects=True)

    async def get_repo(self, owner: Optional[str] = None, repo: Optional[str] = None) -> RepoMetadata:
        o, r = self._resolve(owner, repo)
        async with self._client() as client:
            data = await self._get_json(client, f"/repos/{o}/{r}", o, r)
        license_obj = data.get("license") or {}
        return RepoMetadata(
            owner=data.get("owner", {}).get("login", o),
            name=data.get("name", r),
            full_name=data.get("full_name", f"{o}/{r}"),
            html_url=data.get("html_url", f"https://github.com/{o}/{r}"),
            description=data.get("description"),
            stars=int(data.get("stargazers_count") or 0),
            forks=int(data.get("forks_count") or 0),
            open_issues=int(data.get("open_issues_count") or 0),
            language=data.get("language"),
            license=license_obj.get("spdx_id") if isinstance(license_obj, dict) else None,
            default_branch=data.get("default_branch") or "main",
            topics=list(data.get("topics") or []),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            retrieved_at=datetime.now(timezone.utc).isoformat(),
        )

    async def get_head_sha(self, branch: Optional[str] = None, owner: Optional[str] = None, repo: Optional[str] = None) -> str:
        o, r = self._resolve(owner, repo)
        b = branch or "HEAD"
        async with self._client() as client:
            data = await self._get_json(client, f"/repos/{o}/{r}/commits/{b}", o, r)
        sha = data.get("sha")
        if not sha:
            raise GithubError(f"Could not resolve commit SHA for {o}/{r}@{b}")
        return str(sha)

    async def get_tree(self, sha: str, owner: Optional[str] = None, repo: Optional[str] = None) -> list[dict]:
        o, r = self._resolve(owner, repo)
        async with self._client() as client:
            data = await self._get_json(client, f"/repos/{o}/{r}/git/trees/{sha}?recursive=1", o, r)
        tree = data.get("tree") if isinstance(data, dict) else None
        return list(tree or [])

    async def fetch_files_via_tarball(
        self,
        sha: str,
        owner: Optional[str] = None,
        repo: Optional[str] = None,
    ) -> dict[str, str]:
        """Fetch the whole repo as ONE codeload tarball request.

        The git-blobs API costs one request per file and exhausts the
        unauthenticated 60 req/hr rate limit on any real repo; codeload is a
        single download. Files are extracted in memory only — nothing is
        written to disk or executed. Same size/count limits apply.
        """
        import io
        import tarfile

        o, r = self._resolve(owner, repo)
        ref = sha or "HEAD"
        # github.com/archive redirects to codeload with the resolved commit
        # SHA in the final URL, so we recover the exact analysed commit
        # without spending a rate-limited API call.
        url = f"https://github.com/{o}/{r}/archive/{ref}.tar.gz"
        files: dict[str, str] = {}
        total = 0
        async with self._client() as client:
            resp = await client.get(url, headers=self._headers())
            if resp.status_code == 404:
                raise GithubError(f"Repository {o}/{r} not found (it may be private or does not exist)")
            if resp.status_code in (403, 429):
                raise GithubError("GitHub download rate limit exceeded; try again later or provide a GITHUB_TOKEN")
            if resp.status_code >= 400:
                raise GithubError(f"GitHub download error ({resp.status_code}) for {o}/{r}")
            payload = resp.content
            final_segment = str(resp.url).rstrip("/").rsplit("/", 1)[-1]
            self.last_tarball_sha = (
                final_segment if len(final_segment) == 40 and all(c in "0123456789abcdef" for c in final_segment) else None
            )
        max_archive = 60_000_000
        if len(payload) > max_archive:
            raise GithubError("Repository archive too large for MVP analysis limits")
        try:
            with tarfile.open(fileobj=io.BytesIO(payload), mode="r:gz") as tar:
                members = tar.getmembers()
                # Top-level dir is "<repo>-<full sha>": recover the commit SHA
                # for free, without an extra (rate-limited) API call.
                self.last_tarball_sha = None
                if members:
                    suffix = members[0].name.split("/", 1)[0].rsplit("-", 1)[-1]
                    if len(suffix) == 40 and all(c in "0123456789abcdef" for c in suffix):
                        self.last_tarball_sha = suffix
                for member in members:
                    if len(files) >= settings.max_files or total >= settings.max_total_bytes:
                        break
                    if not member.isfile():
                        continue
                    # Strip "<repo>-<sha>/" top-level prefix
                    parts = member.name.split("/", 1)
                    path = parts[1] if len(parts) == 2 else member.name
                    if not path or _is_binary_path(path):
                        continue
                    if member.size > settings.max_file_bytes:
                        continue
                    fh = tar.extractfile(member)
                    if fh is None:
                        continue
                    raw = fh.read()
                    if b"\x00" in raw[:1024] or total + len(raw) > settings.max_total_bytes:
                        continue
                    files[path] = raw.decode("utf-8", errors="replace")
                    total += len(raw)
        except GithubError:
            raise
        except Exception as exc:
            raise GithubError(f"Could not unpack repository archive for {o}/{r}: {exc}") from exc
        return files

    async def fetch_text_files(
        self,
        tree: list[dict],
        owner: Optional[str] = None,
        repo: Optional[str] = None,
        sha: Optional[str] = None,
    ) -> dict[str, str]:
        o, r = self._resolve(owner, repo)
        files: dict[str, str] = {}
        total = 0
        async with self._client() as client:
            for entry in tree or []:
                if len(files) >= settings.max_files or total >= settings.max_total_bytes:
                    break
                if entry.get("type") != "blob":
                    continue
                path = entry.get("path") or ""
                if not path or _is_binary_path(path):
                    continue
                size = entry.get("size")
                if isinstance(size, int) and size > settings.max_file_bytes:
                    continue
                blob_sha = entry.get("sha")
                if not blob_sha:
                    continue
                resp = await client.get(f"{self.base_url}/repos/{o}/{r}/git/blobs/{blob_sha}", headers=self._headers())
                self._handle_error(resp, o, r)
                data = resp.json()
                content_b64 = data.get("content") or ""
                raw_size = data.get("size")
                if isinstance(raw_size, int) and raw_size > settings.max_file_bytes:
                    continue
                try:
                    raw = base64.b64decode(content_b64)
                except Exception:
                    continue
                if len(raw) > settings.max_file_bytes:
                    continue
                if b"\x00" in raw[:1024]:
                    continue
                if total + len(raw) > settings.max_total_bytes:
                    continue
                text = raw.decode("utf-8", errors="replace")
                files[path] = text
                total += len(raw)
        return files

    # Sync convenience wrappers (for non-async callers)
    def get_repo_sync(self, owner: Optional[str] = None, repo: Optional[str] = None) -> RepoMetadata:
        import asyncio
        return asyncio.run(self.get_repo(owner, repo))
