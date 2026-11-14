# Project structure: MatrixTM/MHDDoS

**Analysed commit:** `bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9`

**Commit reference:** [bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9](https://github.com/MatrixTM/MHDDoS/commit/bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9)

**Tree at this commit:** [MatrixTM/MHDDoS@bf66ccc3bbad](https://github.com/MatrixTM/MHDDoS/tree/bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | MatrixTM/MHDDoS |
| Description | Best DDoS Attack Script  Python3, (Cyber / DDos) Attack With 60 Methods |
| Stars | 17022 |
| Forks | 3656 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9` |
| Retrieved at | 2026-11-14T19:08:37.244958+00:00 |
| Files in this snapshot | 54 |

## Directory tree

```text
.github/  (16 files)
  DISCUSSION_TEMPLATE/  (5 files)
    announcements.yml
    general.yml
    ideas.yml
    q-a.yml
    show-and-tell.yml
  ISSUE_TEMPLATE/  (6 files)
    bug_report.yml
    bypass_request.yml
    config.yml
    documentation.yml
    feature_request.yml
    method_request.yml
  workflows/  (3 files)
    codeql-analysis.yml
    docker-image.yml
    release.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
files/  (3 files)
  proxies/  (1 files)
    http.txt
  referers.txt
  useragent.txt
web/  (21 files)
  public/  (8 files)
    locales/  (4 files)
      … 4 files under this directory
    app.js
    i18n.js
    index.html
    style.css
  scripts/  (4 files)
    install.bat
    install.sh
    start.bat
    start.sh
  src/  (1 files)
    server.ts
  static/  (2 files)
    css/  (1 files)
      … 1 files under this directory
    js/  (1 files)
      … 1 files under this directory
  templates/  (1 files)
    index.html
  .env.example
  app.py
  package.json
  requirements.txt
  tsconfig.json
.dockerignore
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
SECURITY.md
SUPPORT.md
config.json
docker-compose.yml
pyproject.toml
requirements.txt
start.py
```

## Entry points

- [start.py:2301](https://github.com/MatrixTM/MHDDoS/blob/bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9/start.py#L2301)
- [web/app.py:38](https://github.com/MatrixTM/MHDDoS/blob/bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9/web/app.py#L38)
- [web/public/app.js](https://github.com/MatrixTM/MHDDoS/blob/bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9/web/public/app.js)
- [web/src/server.ts](https://github.com/MatrixTM/MHDDoS/blob/bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9/web/src/server.ts)
- [web/static/js/app.js](https://github.com/MatrixTM/MHDDoS/blob/bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9/web/static/js/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /api/methods, ROUTE /api/system/stats,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| web package | library | Observed | Groups 6 file(s) under web package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/DISCUSSION_TEMPLATE/announcements.yml` (config)
- `.github/DISCUSSION_TEMPLATE/general.yml` (config)
- `.github/DISCUSSION_TEMPLATE/ideas.yml` (config)
- `.github/DISCUSSION_TEMPLATE/q-a.yml` (config)
- `.github/DISCUSSION_TEMPLATE/show-and-tell.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/bypass_request.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/method_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/docker-image.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `Dockerfile` (container)
- `config.json` (config)
- `docker-compose.yml` (container)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `web/.env.example` (config)
- `web/package.json` (manifest)
- `web/public/locales/manifest.json` (config)
- `web/requirements.txt` (manifest)
- `web/tsconfig.json` (config)

## Top-level layout

- `web` — 21 analysed file(s)
- `.github` — 16 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `files` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bf66ccc3bbadd50dc5fed6955ba315fa8a1721b9` is the revision these paths and observations refer to.
