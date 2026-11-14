"""Framework / library / database / tooling detection from evidence only."""
from __future__ import annotations
import json, re, tomllib
from ..models import Detection, SourceRef
from .sanitize import sanitize_text

KNOWN = {
    "fastapi": ("FastAPI", "framework"), "flask": ("Flask", "framework"), "django": ("Django", "framework"),
    "starlette": ("Starlette", "framework"), "click": ("Click", "library"), "typer": ("Typer", "framework"),
    "celery": ("Celery", "library"), "sqlalchemy": ("SQLAlchemy", "library"), "pydantic": ("Pydantic", "library"),
    "requests": ("requests", "library"), "httpx": ("httpx", "library"), "aiohttp": ("aiohttp", "library"),
    "pytest": ("pytest", "tooling"), "unittest": ("unittest", "tooling"), "uvicorn": ("Uvicorn", "library"),
    "gunicorn": ("Gunicorn", "library"), "pandas": ("pandas", "library"), "numpy": ("NumPy", "library"),
    "redis": ("Redis", "database"), "psycopg": ("PostgreSQL", "database"), "psycopg2": ("PostgreSQL", "database"),
    "asyncpg": ("PostgreSQL", "database"), "pg8000": ("PostgreSQL", "database"), "pymongo": ("MongoDB", "database"),
    "motor": ("MongoDB", "database"), "mysql": ("MySQL", "database"), "pymysql": ("MySQL", "database"),
    "aiomysql": ("MySQL", "database"), "sqlite3": ("SQLite", "database"), "aiosqlite": ("SQLite", "database"),
    "boto3": ("AWS (boto3)", "library"), "alembic": ("Alembic", "tooling"), "setuptools": ("setuptools", "packaging"),
    "poetry": ("Poetry", "packaging"), "flask_sqlalchemy": ("SQLAlchemy", "library"), "tortoise": ("Tortoise ORM", "library"),
    "peewee": ("Peewee", "library"), "kafka": ("Kafka", "library"), "pika": ("RabbitMQ (pika)", "library"), "kombu": ("Kombu", "library"),
    "react": ("React", "framework"), "react_dom": ("React", "framework"), "next": ("Next.js", "framework"),
    "vue": ("Vue", "framework"), "express": ("Express", "framework"), "fastify": ("Fastify", "framework"),
    "koa": ("Koa", "framework"), "electron": ("Electron", "framework"), "svelte": ("Svelte", "framework"),
    "vite": ("Vite", "tooling"), "webpack": ("webpack", "tooling"), "typescript": ("TypeScript", "tooling"),
    "jest": ("Jest", "tooling"), "vitest": ("Vitest", "tooling"), "redux": ("Redux", "library"),
    "react_router": ("React Router", "library"), "react_router_dom": ("React Router", "library"),
    "@reduxjs/toolkit": ("Redux Toolkit", "library"), "@nestjs/core": ("NestJS", "framework"),
    "tailwindcss": ("Tailwind CSS", "library"), "axios": ("axios", "library"), "prisma": ("Prisma", "library"),
    "mongoose": ("MongoDB", "database"),
}
EXTERNAL_IMPORTS = {"requests", "httpx", "aiohttp", "boto3", "redis", "psycopg", "psycopg2", "asyncpg", "pymongo", "motor", "pymysql", "aiomysql", "sqlite3", "aiosqlite", "sqlalchemy", "kafka", "pika", "urllib3", "socket"}
DEP_NAME_RE = re.compile(r"^\s*([A-Za-z0-9_.\-]+)")

def _norm(name):
    return re.sub(r"[-_.]+", "_", name.strip().lower())

def _find_line(content, needle):
    low = needle.lower()
    for i, line in enumerate(content.splitlines(), start=1):
        if low in line.lower():
            return i
    return None

def _dep_names_from_requirements(content):
    names = []
    for raw in content.splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", "-")):
            continue
        m = DEP_NAME_RE.match(line.split(";")[0])
        if m:
            names.append(m.group(1))
    return names

def _dep_names_from_pyproject(content):
    deps, scripts = [], {}
    try:
        data = tomllib.loads(content)
    except Exception:
        for line in content.splitlines():
            for m in re.finditer(r'["\']([A-Za-z0-9_.\-]+)[^"\']*["\']', line):
                deps.append(m.group(1))
        return deps, scripts
    project = data.get("project", {}) if isinstance(data, dict) else {}
    if isinstance(project, dict):
        for dep in project.get("dependencies", []) or []:
            if isinstance(dep, str):
                m = DEP_NAME_RE.match(dep)
                if m: deps.append(m.group(1))
        optional = project.get("optional-dependencies", {}) or {}
        if isinstance(optional, dict):
            for group in optional.values():
                for dep in group or []:
                    if isinstance(dep, str):
                        m = DEP_NAME_RE.match(dep)
                        if m: deps.append(m.group(1))
        raw_scripts = project.get("scripts", {}) or {}
        if isinstance(raw_scripts, dict):
            for k, v in raw_scripts.items():
                if isinstance(v, str):
                    scripts[sanitize_text(k, 60)] = sanitize_text(v, 120)
    build = data.get("build-system", {}) if isinstance(data, dict) else {}
    if isinstance(build, dict):
        for dep in build.get("requires", []) or []:
            if isinstance(dep, str):
                m = DEP_NAME_RE.match(dep)
                if m: deps.append(m.group(1))
    tool = data.get("tool", {}) if isinstance(data, dict) else {}
    poetry = tool.get("poetry", {}) if isinstance(tool, dict) else {}
    if isinstance(poetry, dict):
        deps.append("poetry")
        for section in ("dependencies", "dev-dependencies"):
            table = poetry.get(section, {}) or {}
            if isinstance(table, dict):
                deps.extend(str(k) for k in table.keys())
    return deps, scripts

def _dep_names_from_setup_py(content):
    deps, scripts = [], {}
    for m in re.finditer(r'["\']([A-Za-z0-9_.\-]+)(?:\s*(?:[<>=!~].*)?)?["\']', content):
        if _norm(m.group(1)) in KNOWN or _norm(m.group(1)) == "setuptools":
            deps.append(m.group(1))
    for m in re.finditer(r'["\']([A-Za-z0-9_\-]+)\s*=\s*([A-Za-z0-9_.]+:[A-Za-z0-9_]+)["\']', content):
        scripts[sanitize_text(m.group(1), 60)] = sanitize_text(m.group(2), 120)
    return deps, scripts

def _env_keys(content):
    keys = []
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key = line.split("=", 1)[0].strip().removeprefix("export ").strip()
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
            keys.append(key)
    return sorted(set(keys))

def _dep_names_from_package_json(content):
    try:
        data = json.loads(content)
    except Exception:
        return [], {}
    if not isinstance(data, dict):
        return [], {}
    deps = []
    for section in ("dependencies", "devDependencies", "peerDependencies"):
        table = data.get(section) or {}
        if isinstance(table, dict):
            deps.extend(str(key) for key in table.keys())
    return deps, {}

def parse_manifests(files):
    dep_names, scripts, env_keys = {}, {}, {}
    for path in sorted(files):
        name = path.rsplit("/", 1)[-1].lower()
        content = files[path]
        if name.startswith("requirements") and name.endswith(".txt"):
            dep_names[path] = _dep_names_from_requirements(content)
        elif name == "pyproject.toml":
            deps, sc = _dep_names_from_pyproject(content); dep_names[path] = deps; scripts.update(sc)
        elif name == "setup.py":
            deps, sc = _dep_names_from_setup_py(content); dep_names[path] = deps; scripts.update(sc)
        elif name == "setup.cfg":
            dep_names[path] = _dep_names_from_requirements(content)
        elif name == "pipfile":
            dep_names[path] = [m.group(1) for line in content.splitlines() if (m := re.match(r"\s*([A-Za-z0-9_.\-]+)\s*=", line))]
        elif name == "package.json":
            deps, sc = _dep_names_from_package_json(content)
            dep_names[path] = deps
            scripts.update(sc)
        elif name in {".env.example", ".env.sample", ".env.template"}:
            env_keys[path] = _env_keys(content)
    return dep_names, scripts, env_keys

def detect(files, py_modules, dep_names, env_keys):
    found = {}
    def add(name, category, confidence, ref):
        key = name.lower()
        if key in found:
            det = found[key]
            det.confidence = max(det.confidence, min(0.95, confidence + 0.05))
            if ref not in det.evidence:
                det.evidence.append(ref)
        else:
            found[key] = Detection(name=name, category=category, confidence=confidence, evidence=[ref])
    for path in sorted(py_modules):
        for imp in py_modules[path].imports:
            top = _norm(imp.module.split(".")[0]) if imp.module else ""
            if top in KNOWN:
                name, cat = KNOWN[top]
                add(name, cat, 0.9, SourceRef(path=path, start_line=imp.line, end_line=imp.line))
    for path in sorted(dep_names):
        content = files.get(path, "")
        for dep in dep_names[path]:
            key = _norm(dep)
            if key in KNOWN:
                name, cat = KNOWN[key]
                line = _find_line(content, dep)
                add(name, cat, 0.85, SourceRef(path=path, start_line=line, end_line=line))
    for path in sorted(files):
        low = path.lower(); name = low.rsplit("/", 1)[-1]; content = files[path]
        if name in {"docker-compose.yml", "docker-compose.yaml", "compose.yml", "compose.yaml"}:
            for image, disp in (("postgres", "PostgreSQL"), ("mysql", "MySQL"), ("mongo", "MongoDB"), ("redis", "Redis")):
                line = _find_line(content, image)
                if line:
                    add(disp, "database", 0.8, SourceRef(path=path, start_line=line, end_line=line))
            add("Docker Compose", "tooling", 0.85, SourceRef(path=path))
        if name.startswith("dockerfile"):
            add("Docker", "tooling", 0.85, SourceRef(path=path))
        if ".github/workflows" in low:
            add("GitHub Actions", "ci", 0.85, SourceRef(path=path))
            line = _find_line(content, "pytest")
            if line:
                add("pytest", "tooling", 0.75, SourceRef(path=path, start_line=line, end_line=line))
            line = _find_line(content, "docker")
            if line:
                add("Docker", "tooling", 0.7, SourceRef(path=path, start_line=line, end_line=line))
    for path in sorted(env_keys):
        for key in env_keys[path]:
            ku = key.upper(); line = _find_line(files.get(path, ""), key)
            ref = SourceRef(path=path, start_line=line, end_line=line)
            if "POSTGRES" in ku:
                add("PostgreSQL", "database", 0.55, ref)
            elif "REDIS" in ku:
                add("Redis", "database", 0.55, ref)
            elif "MONGO" in ku:
                add("MongoDB", "database", 0.55, ref)
            elif ku in {"DATABASE_URL", "DB_URL", "SQLALCHEMY_DATABASE_URI"}:
                add("Database (unspecified)", "database", 0.45, ref)
    for det in found.values():
        det.evidence.sort(key=lambda r: (r.path, r.start_line or 0)); det.evidence = det.evidence[:8]
    return sorted(found.values(), key=lambda d: (d.category, d.name.lower()))
