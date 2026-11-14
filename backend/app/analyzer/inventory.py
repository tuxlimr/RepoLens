"""Repository inventory: categorise files and exclude unsafe/irrelevant ones."""
from __future__ import annotations
import posixpath
from ..models import FileInfo
from .sanitize import is_secret_path

SKIPPED_DIRS = {"node_modules", ".git", ".hg", ".svn", "dist", "build", "__pycache__", ".venv", "venv", ".tox", ".mypy_cache", ".pytest_cache", "vendor", "vendored", "site-packages", ".idea", ".eggs", "htmlcov", "target"}
LOCKFILES = {"pipfile.lock", "poetry.lock", "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "pdm.lock", "uv.lock", "composer.lock", "cargo.lock"}
BINARY_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".bmp", ".webp", ".svgz", ".pdf", ".zip", ".tar", ".gz", ".bz2", ".xz", ".7z", ".whl", ".egg", ".pyc", ".pyo", ".so", ".dll", ".exe", ".bin", ".woff", ".woff2", ".ttf", ".eot", ".mp3", ".mp4", ".mov", ".avi", ".db", ".sqlite", ".sqlite3", ".class", ".jar", ".parquet", ".npy", ".npz", ".pickle", ".pkl"}
MANIFEST_NAMES = {"requirements.txt", "requirements-dev.txt", "requirements-test.txt", "pyproject.toml", "setup.py", "setup.cfg", "pipfile", "package.json", "go.mod", "cargo.toml", "pom.xml", "build.gradle", "manifest.in", "environment.yml", "conda.yml"}
SOURCE_EXTS = {".py": "Python", ".js": "JavaScript", ".jsx": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript", ".ts": "TypeScript", ".tsx": "TypeScript", ".vue": "Vue", ".svelte": "Svelte", ".java": "Java", ".go": "Go", ".rs": "Rust", ".rb": "Ruby", ".php": "PHP", ".c": "C", ".cpp": "C++", ".h": "C/C++", ".cs": "C#", ".sh": "Shell", ".sql": "SQL"}

def normalise_path(path):
    p = str(path).replace("\\", "/")
    while p.startswith("./"):
        p = p[2:]
    return posixpath.normpath(p) if p not in {"", "."} else p

def skip_reason(path, content=None):
    p = normalise_path(path)
    parts = [part for part in p.split("/") if part]
    name = parts[-1].lower() if parts else ""
    if is_secret_path(p):
        return "likely secret file excluded"
    if any(part in SKIPPED_DIRS for part in parts):
        return "vendored/generated directory excluded"
    if name in LOCKFILES:
        return "lockfile excluded"
    if name.endswith((".min.js", ".min.css", ".map")):
        return "generated/minified file excluded"
    ext = posixpath.splitext(name)[1]
    if ext in BINARY_EXTS:
        return "binary file excluded"
    if content is not None and "\x00" in content[:4096]:
        return "binary-looking content excluded"
    return None

def categorise(path):
    p = normalise_path(path)
    low = p.lower()
    parts = low.split("/")
    name = parts[-1]
    ext = posixpath.splitext(name)[1]
    if ".github/workflows" in low or name in {".gitlab-ci.yml", "azure-pipelines.yml"} or ".circleci" in parts or name == ".travis.yml":
        return "ci", "YAML"
    if name.startswith("dockerfile") or name in {"docker-compose.yml", "docker-compose.yaml", "compose.yml", "compose.yaml", ".dockerignore"}:
        return "container", None
    if "test" in parts or "tests" in parts or name.startswith("test_") or name.endswith(("_test.py", "_tests.py")) or name == "conftest.py":
        return "test", SOURCE_EXTS.get(ext)
    if name in MANIFEST_NAMES or (name.startswith("requirements") and name.endswith(".txt")):
        return "manifest", SOURCE_EXTS.get(ext)
    if name in {".env.example", ".env.sample", ".env.template"} or ext in {".toml", ".ini", ".cfg", ".yaml", ".yml", ".json"} or name in {".editorconfig", "pytest.ini", "tox.ini"}:
        return "config", None
    if ext in {".md", ".rst"} or "docs" in parts or name in {"license", "license.txt", "notice"}:
        return "docs", None
    if ext in {".csv", ".tsv", ".sql", ".jsonl"}:
        return "data", SOURCE_EXTS.get(ext)
    if ext in SOURCE_EXTS:
        return "source", SOURCE_EXTS[ext]
    if ext == ".txt":
        return "docs", None
    return "other", None

def inventory_files(files, max_files, max_file_bytes, max_total_bytes):
    kept, infos, skipped, limit_notes = {}, [], [], []
    total = 0
    limit_hit = False
    for raw_path in sorted(files, key=lambda x: normalise_path(x)):
        path = normalise_path(raw_path)
        content = files[raw_path]
        if not isinstance(content, str):
            content = str(content)
        reason = skip_reason(path, content)
        if reason:
            skipped.append((path, reason)); continue
        size = len(content.encode("utf-8", errors="ignore"))
        if size > max_file_bytes:
            skipped.append((path, f"file exceeds per-file size limit ({max_file_bytes} bytes)")); continue
        if len(kept) >= max_files or total + size > max_total_bytes:
            skipped.append((path, "repository size/file-count limit reached")); limit_hit = True; continue
        category, language = categorise(path)
        kept[path] = content; total += size
        infos.append(FileInfo(path=path, size=size, category=category, language=language))
    if limit_hit:
        limit_notes.append("Analysis limits were reached (max files/total bytes from settings); some files were skipped.")
    return kept, infos, skipped, limit_notes
