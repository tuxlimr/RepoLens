# Project structure: idank/explainshell

**Analysed commit:** `827ebe38da9822a10e89946551e377330a9de35e`

**Commit reference:** [827ebe38da9822a10e89946551e377330a9de35e](https://github.com/idank/explainshell/commit/827ebe38da9822a10e89946551e377330a9de35e)

**Tree at this commit:** [idank/explainshell@827ebe38da98](https://github.com/idank/explainshell/tree/827ebe38da9822a10e89946551e377330a9de35e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | idank/explainshell |
| Description | match command-line arguments to their help text |
| Stars | 14342 |
| Forks | 857 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `827ebe38da9822a10e89946551e377330a9de35e` |
| Retrieved at | 2026-11-14T19:09:28.044705+00:00 |
| Files in this snapshot | 145 |

## Directory tree

```text
.claude/  (6 files)
  skills/  (5 files)
    eval-llm/  (1 files)
      … 1 files under this directory
    eval-render/  (1 files)
      … 1 files under this directory
    mandoc-fix/  (2 files)
      … 2 files under this directory
    my-plan/  (1 files)
      … 1 files under this directory
  .gitignore
.github/  (2 files)
  workflows/  (2 files)
    ci.yml
    do-deploy.yml
explainshell/  (57 files)
  extraction/  (17 files)
    llm/  (9 files)
      … 9 files under this directory
    __init__.py
    common.py
    manifest.py
    postprocess.py
    prefilter.py
    report.py
    runner.py
    types.py
  logger/  (2 files)
    __init__.py
    json_logging.py
  web/  (24 files)
    static/  (8 files)
      … 8 files under this directory
    templates/  (12 files)
      … 12 files under this directory
    __init__.py
    helpers.py
    markdown.py
    views.py
  __init__.py
  caching_store.py
  config.py
  db_check.py
  diff.py
  errors.py
  help_constants.py
  manager.py
  manpage.py
  matcher.py
  models.py
  roff_utils.py
  store.py
  util.py
plans/  (1 files)
  positional-prefix-matching.md
prod/  (23 files)
  botshed/  (4 files)
    go.mod
    go.sum
    module.go
    module_test.go
  datadog/  (13 files)
    dashboards/  (1 files)
      … 1 files under this directory
    logs/  (6 files)
      … 6 files under this directory
    monitors/  (1 files)
      … 1 files under this directory
    synthetics/  (3 files)
      … 3 files under this directory
    README.md
    apply.py
  digitalocean/  (1 files)
    app.yaml
  docker/  (3 files)
    Caddyfile
    Dockerfile
    start.sh
  integration-test.sh
  smoke-test.sh
tests/  (32 files)
  e2e/  (1 files)
    e2e.spec.js
  evals/  (8 files)
    llm/  (2 files)
      … 2 files under this directory
    render/  (4 files)
      … 4 files under this directory
    __init__.py
    _common.py
  extraction/  (11 files)
    llm/  (6 files)
      … 6 files under this directory
    __init__.py
    test_manifest.py
    test_postprocess.py
    test_prefilter.py
    test_runner.py
  __init__.py
  conftest.py
  helpers.py
  test_caching_store.py
  test_db_check.py
  test_json_logging.py
  test_manager.py
  test_manpage.py
  test_matcher.py
  test_postprocess_ubuntu_archive.py
  test_store.py
  test_web_views.py
tools/  (8 files)
  experiments/  (1 files)
    eval_size_routing.py
  bench_src_index.py
  download-latest-db.sh
  fetch_manned.py
  loadtest.py
  migrate_mongo_to_sqlite.py
  postprocess_ubuntu_archive.py
  upload-live-db.sh
.dockerignore
.env.example
.gitignore
.gitmodules
CLAUDE.md
LICENSE
Makefile
README.md
biome.json
package.json
playwright.config.js
requirements-dev.txt
requirements-extraction.txt
requirements.txt
ruff.toml
runserver.py
```

## Entry points

- [explainshell/manager.py:494](https://github.com/idank/explainshell/blob/827ebe38da9822a10e89946551e377330a9de35e/explainshell/manager.py#L494)
- [explainshell/web/__init__.py:96](https://github.com/idank/explainshell/blob/827ebe38da9822a10e89946551e377330a9de35e/explainshell/web/__init__.py#L96)
- [prod/datadog/apply.py:283](https://github.com/idank/explainshell/blob/827ebe38da9822a10e89946551e377330a9de35e/prod/datadog/apply.py#L283)
- [runserver.py:8](https://github.com/idank/explainshell/blob/827ebe38da9822a10e89946551e377330a9de35e/runserver.py#L8)
- [tools/bench_src_index.py:269](https://github.com/idank/explainshell/blob/827ebe38da9822a10e89946551e377330a9de35e/tools/bench_src_index.py#L269)
- [tools/experiments/eval_size_routing.py:215](https://github.com/idank/explainshell/blob/827ebe38da9822a10e89946551e377330a9de35e/tools/experiments/eval_size_routing.py#L215)
- [tools/fetch_manned.py:791](https://github.com/idank/explainshell/blob/827ebe38da9822a10e89946551e377330a9de35e/tools/fetch_manned.py#L791)
- [tools/loadtest.py:810](https://github.com/idank/explainshell/blob/827ebe38da9822a10e89946551e377330a9de35e/tools/loadtest.py#L810)
- [tools/migrate_mongo_to_sqlite.py:208](https://github.com/idank/explainshell/blob/827ebe38da9822a10e89946551e377330a9de35e/tools/migrate_mongo_to_sqlite.py#L208)
- [tools/postprocess_ubuntu_archive.py:211](https://github.com/idank/explainshell/blob/827ebe38da9822a10e89946551e377330a9de35e/tools/postprocess_ubuntu_archive.py#L211)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). Observed routes: ROUTE /, ROUTE /manpage/<distro>/, ROUTE /manpage/<distro>/<release>/, ROUTE /manpage/<distro>/<release>/<section>/… |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: parse_distro_release, source_from_path. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ExtractionMeta, Option, ParsedManpage, RawManpage. |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed top-level classes: Dashboard, LogsIndex, LogsMetric, LogsPipe… |
| explainshell package | library | Observed | Groups 34 file(s) under explainshell package (observed from repository paths and static analysis). Observed top-level classes: AlreadyStored, BatchEntry, BatchExtractor, BatchManifest, BatchManifestEntry, BatchManifestW… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| prod package | library | Observed | Groups 5 file(s) under prod package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 32 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH explainshell.extraction.common.roff_utils.detect_nested_cmd, PATCH explainshell.extraction.common.manpage.get_sy… |
| tools package | library | Observed | Groups 2 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/do-deploy.yml` (ci)
- `biome.json` (config)
- `package.json` (manifest)
- `prod/botshed/go.mod` (manifest)
- `prod/datadog/dashboards/overview.json` (config)
- `prod/datadog/logs/index_main.json` (config)
- `prod/datadog/logs/metrics/parse_errors.json` (config)
- `prod/datadog/logs/metrics/request_duration.json` (config)
- `prod/datadog/logs/metrics/requests.json` (config)
- `prod/datadog/logs/metrics/requests_by_country.json` (config)
- `prod/datadog/logs/pipeline.json` (config)
- `prod/datadog/monitors/5xx_rate.json` (config)
- `prod/datadog/synthetics/explain_keyword.json` (config)
- `prod/datadog/synthetics/homepage.json` (config)
- `prod/datadog/synthetics/ssl.json` (config)
- `prod/digitalocean/app.yaml` (config)
- `prod/docker/Dockerfile` (container)
- `requirements-dev.txt` (manifest)
- `requirements-extraction.txt` (manifest)
- `requirements.txt` (manifest)
- `ruff.toml` (config)

## Top-level layout

- `explainshell` — 57 analysed file(s)
- `tests` — 32 analysed file(s)
- `prod` — 23 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `tools` — 8 analysed file(s)
- `.claude` — 6 analysed file(s)
- `.github` — 2 analysed file(s)
- `plans` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (6 x generated/minified file excluded; 1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `827ebe38da9822a10e89946551e377330a9de35e` is the revision these paths and observations refer to.
