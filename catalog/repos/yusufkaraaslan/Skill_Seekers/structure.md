# Project structure: yusufkaraaslan/Skill_Seekers

**Analysed commit:** `5b5d8dfca263fa76e6daae9f292890b311ef36aa`

**Commit reference:** [5b5d8dfca263fa76e6daae9f292890b311ef36aa](https://github.com/yusufkaraaslan/Skill_Seekers/commit/5b5d8dfca263fa76e6daae9f292890b311ef36aa)

**Tree at this commit:** [yusufkaraaslan/Skill_Seekers@5b5d8dfca263](https://github.com/yusufkaraaslan/Skill_Seekers/tree/5b5d8dfca263fa76e6daae9f292890b311ef36aa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yusufkaraaslan/Skill_Seekers |
| Description | Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection |
| Stars | 15309 |
| Forks | 1557 |
| Licence | MIT |
| Language | Python |
| Default branch | development |
| Analysed commit | `5b5d8dfca263fa76e6daae9f292890b311ef36aa` |
| Retrieved at | 2026-11-14T19:09:05.976585+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.claude/  (1 files)
  mcp_config.example.json
.codex-plugin/  (1 files)
  plugin.json
.github/  (14 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    documentation.md
    feature_request.md
    mcp_tool.md
  workflows/  (7 files)
    docker-publish.yml
    quality-metrics.yml
    release.yml
    scheduled-updates.yml
    test-vector-dbs.yml
    tests.yml
    vector-db-export.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  create_issues.sh
.vscode/  (1 files)
  settings.json
api/  (6 files)
  .gitignore
  README.md
  __init__.py
  config_analyzer.py
  main.py
  requirements.txt
configs/  (12 files)
  astrovalley_unified.json
  blender-unified.json
  claude-code-unified.json
  claude-code.json
  godot.json
  godot_unified.json
  httpx_comprehensive.json
  medusa-mercurjs.json
  react.json
  unity-addressables.json
  unity-dotween.json
  unity-spine.json
distribution/  (10 files)
  claude-plugin/  (7 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (3 files)
      … 3 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    .mcp.json
    README.md
  github-action/  (2 files)
    README.md
    action.yml
  smithery/  (1 files)
    README.md
docs/  (726 files)
  UML/  (717 files)
    html/  (717 files)
      … 717 files under this directory
  ARCHITECTURE.md
  BEST_PRACTICES.md
  BUG_AUDIT.md
  DOCKER_DEPLOYMENT.md
  FAQ.md
  KUBERNETES_DEPLOYMENT.md
  PRODUCTION_DEPLOYMENT.md
  README.md
  TROUBLESHOOTING.md
.dockerignore
.env.example
.gitignore
.gitmodules
.mcp.json
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
Dockerfile
Dockerfile.mcp
LICENSE
QWEN.md
README.ar.md
README.de.md
README.es.md
README.fr.md
README.hi.md
README.ja.md
README.ko.md
README.md
README.pt-BR.md
README.ru.md
README.tr.md
README.zh-CN.md
… 5 more files
```

## Entry points

- [api/main.py:16](https://github.com/yusufkaraaslan/Skill_Seekers/blob/5b5d8dfca263fa76e6daae9f292890b311ef36aa/api/main.py#L16)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: ConfigAnalyzer. |
| Configuration and deployment | config | Observed | Groups 20 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /, GET /api/configs, GET /api/configs/{name}, GE… |

## Important files

- `.claude/mcp_config.example.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.dockerignore` (container)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/docker-publish.yml` (ci)
- `.github/workflows/quality-metrics.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/scheduled-updates.yml` (ci)
- `.github/workflows/test-vector-dbs.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/vector-db-export.yml` (ci)
- `.mcp.json` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `Dockerfile.mcp` (container)
- `api/requirements.txt` (manifest)
- `codecov.yml` (config)
- `configs/astrovalley_unified.json` (config)
- `configs/blender-unified.json` (config)
- `configs/claude-code-unified.json` (config)
- `configs/claude-code.json` (config)
- `configs/godot.json` (config)
- `configs/godot_unified.json` (config)
- `configs/httpx_comprehensive.json` (config)
- `configs/medusa-mercurjs.json` (config)
- `configs/react.json` (config)
- `configs/unity-addressables.json` (config)
- `configs/unity-dotween.json` (config)
- `configs/unity-spine.json` (config)
- `distribution/claude-plugin/.claude-plugin/plugin.json` (config)
- `distribution/claude-plugin/.mcp.json` (config)
- `distribution/github-action/action.yml` (config)
- `docker-compose.yml` (container)

## Top-level layout

- `docs` — 726 analysed file(s)
- `(root files)` — 29 analysed file(s)
- `.github` — 14 analysed file(s)
- `configs` — 12 analysed file(s)
- `distribution` — 10 analysed file(s)
- `api` — 6 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5b5d8dfca263fa76e6daae9f292890b311ef36aa` is the revision these paths and observations refer to.
