# Project structure: coderamp-labs/gitingest

**Analysed commit:** `4e259a02fe72115bee538271622f1234a81c8e1a`

**Commit reference:** [4e259a02fe72115bee538271622f1234a81c8e1a](https://github.com/coderamp-labs/gitingest/commit/4e259a02fe72115bee538271622f1234a81c8e1a)

**Tree at this commit:** [coderamp-labs/gitingest@4e259a02fe72](https://github.com/coderamp-labs/gitingest/tree/4e259a02fe72115bee538271622f1234a81c8e1a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | coderamp-labs/gitingest |
| Description | Replace 'hub' with 'ingest' in any GitHub URL to get a prompt-friendly extract of a codebase  |
| Stars | 16139 |
| Forks | 1217 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `4e259a02fe72115bee538271622f1234a81c8e1a` |
| Retrieved at | 2026-11-14T19:08:56.277744+00:00 |
| Files in this snapshot | 120 |

## Directory tree

```text
.docker/  (1 files)
  minio/  (1 files)
    setup.sh
.github/  (14 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    feature_request.yml
  workflows/  (12 files)
    ci.yml
    codeql.yml
    dependency-review.yml
    deploy-pr.yml
    docker-build.ecr.yml
    docker-build.ghcr.yml
    pr-title-check.yml
    publish_to_pypi.yml
    rebase-needed.yml
    release-please.yml
    scorecard.yml
    stale.yml
.vscode/  (1 files)
  launch.json
src/  (69 files)
  gitingest/  (27 files)
    schemas/  (4 files)
      … 4 files under this directory
    utils/  (15 files)
      … 15 files under this directory
    __init__.py
    __main__.py
    clone.py
    config.py
    entrypoint.py
    ingestion.py
    output_formatter.py
    query_parser.py
  server/  (25 files)
    routers/  (4 files)
      … 4 files under this directory
    templates/  (10 files)
      … 10 files under this directory
    __init__.py
    __main__.py
    form_types.py
    main.py
    metrics_server.py
    models.py
    query_processor.py
    routers_utils.py
    s3_utils.py
    server_config.py
    server_utils.py
  static/  (17 files)
    favicons/  (1 files)
      … 1 files under this directory
    icons/  (5 files)
      … 5 files under this directory
    js/  (6 files)
      … 6 files under this directory
    svg/  (3 files)
      … 3 files under this directory
    llms.txt
    robots.txt
tests/  (16 files)
  query_parser/  (3 files)
    __init__.py
    test_git_host_agnostic.py
    test_query_parser.py
  server/  (2 files)
    __init__.py
    test_flow_integration.py
  .pylintrc
  __init__.py
  conftest.py
  test_cli.py
  test_clone.py
  test_git_utils.py
  test_gitignore_feature.py
  test_ingestion.py
  test_notebook_utils.py
  test_pattern_utils.py
  test_summary.py
.dockerignore
.env.example
.gitignore
.pre-commit-config.yaml
.release-please-manifest.json
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
SECURITY.md
compose.yml
eslint.config.cjs
pyproject.toml
release-please-config.json
renovate.json
requirements-dev.txt
requirements.txt
```

## Entry points

- [src/gitingest/__main__.py](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/src/gitingest/__main__.py)
- [src/server/__main__.py:12](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/src/server/__main__.py#L12)
- [src/server/main.py:59](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/src/server/main.py#L59)
- [src/server/metrics_server.py:14](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/src/server/metrics_server.py#L14)
- [src/static/js/index.js](https://github.com/coderamp-labs/gitingest/blob/4e259a02fe72115bee538271622f1234a81c8e1a/src/static/js/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /{full_path:path}, GET /, POST /api/ingest, GET /api/{user}/{repository}, GET /api/download/file/{ingest_id}. O… |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: IngestErrorResponse, IngestRequest, IngestSuccessResponse, PatternType, QueryForm, S3Metadata. |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /health, HEAD /, GET /robots.txt, GET /llms.txt,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| gitingest package | library | Observed | Groups 25 file(s) under gitingest package (observed from repository paths and static analysis). Observed top-level classes: AsyncTimeoutError, CloneConfig, FileSystemNode, FileSystemNodeType, FileSystemStats, IngestionQ… |
| server package | library | Observed | Groups 7 file(s) under server package (observed from repository paths and static analysis). Observed top-level classes: Colors, S3UploadError. Observed top-level functions: _build_s3_url, _check_object_tags, _check_s3_c… |
| static package | library | Observed | Groups 6 file(s) under static package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: PatternScenario. Observed top-level functions: _assert_basic_repo_fields, _calculate_expected_lines, _fake_… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/dependency-review.yml` (ci)
- `.github/workflows/deploy-pr.yml` (ci)
- `.github/workflows/docker-build.ecr.yml` (ci)
- `.github/workflows/docker-build.ghcr.yml` (ci)
- `.github/workflows/pr-title-check.yml` (ci)
- `.github/workflows/publish_to_pypi.yml` (ci)
- `.github/workflows/rebase-needed.yml` (ci)
- `.github/workflows/release-please.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.release-please-manifest.json` (config)
- `.vscode/launch.json` (config)
- `Dockerfile` (container)
- `compose.yml` (container)
- `pyproject.toml` (manifest)
- `release-please-config.json` (config)
- `renovate.json` (config)
- `requirements-dev.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `src` — 69 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `tests` — 16 analysed file(s)
- `.github` — 14 analysed file(s)
- `.docker` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4e259a02fe72115bee538271622f1234a81c8e1a` is the revision these paths and observations refer to.
