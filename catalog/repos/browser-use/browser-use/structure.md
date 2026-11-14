# Project structure: browser-use/browser-use

**Analysed commit:** `e717df1839a2d7368b108de6694f01e9c659b0de`

**Commit reference:** [e717df1839a2d7368b108de6694f01e9c659b0de](https://github.com/browser-use/browser-use/commit/e717df1839a2d7368b108de6694f01e9c659b0de)

**Tree at this commit:** [browser-use/browser-use@e717df1839a2](https://github.com/browser-use/browser-use/tree/e717df1839a2d7368b108de6694f01e9c659b0de)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | browser-use/browser-use |
| Description | Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API. |
| Stars | 121013 |
| Forks | 13536 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `e717df1839a2d7368b108de6694f01e9c659b0de` |
| Retrieved at | 2026-11-14T19:06:04.702969+00:00 |
| Files in this snapshot | 137 |

## Directory tree

```text
.github/  (16 files)
  ISSUE_TEMPLATE/  (5 files)
    1_element_detection_bug.yml
    2_bug_report.yml
    3_feature_request.yml
    4_docs_issue.yml
    config.yml
  workflows/  (8 files)
    claude.yml
    docker.yml
    install-script.yml
    lint.yml
    package.yaml
    publish.yml
    stale-bot.yml
    test.yaml
  .git-blame-ignore-revs
  CONTRIBUTING.md
  SECURITY.md
bin/  (3 files)
  lint.sh
  setup.sh
  test.sh
browser_use/  (51 files)
  agent/  (6 files)
    __init__.py
    judge.py
    loop.py
    prompt.py
    service.py
    views.py
  browser/  (3 files)
    __init__.py
    browser.py
    local.py
  llm/  (1 files)
    __init__.py
  mcp/  (4 files)
    .dxtignore
    __init__.py
    __main__.py
    cli_mcp.py
  repl/  (8 files)
    __init__.py
    captcha.py
    capture.py
    highlight.py
    network_idle.py
    page_info.py
    session.py
    worker.py
  skills/  (5 files)
    browser-use/  (1 files)
      … 1 files under this directory
    README.md
    __init__.py
    browser_use.py
    install.py
  telemetry/  (6 files)
    __init__.py
    feedback.py
    recorder.py
    service.py
    stats.py
    views.py
  README.md
  __init__.py
  __main__.py
  auth.py
  ax.py
  cli.py
  config.py
  domains.py
  exceptions.py
  harness_cloud.py
  legacy.py
  logging_config.py
  py.typed
  remote_upload.py
  search.py
  tools.py
  update_check.py
  utils.py
docker/  (1 files)
  smoke.py
examples/  (1 files)
  simple.py
scripts/  (1 files)
  sync_browser_harness_skill.py
skills/  (19 files)
  browser-use/  (1 files)
    SKILL.md
  cloud/  (12 files)
    references/  (11 files)
      … 11 files under this directory
    SKILL.md
  open-source/  (1 files)
    SKILL.md
  qa/  (3 files)
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  remote-browser/  (1 files)
    SKILL.md
  x402/  (1 files)
    SKILL.md
static/  (5 files)
  readme/  (5 files)
    README.md
    which-product-dark-mobile.svg
    which-product-dark.svg
    which-product-light-mobile.svg
    which-product-light.svg
tests/  (24 files)
  ci/  (24 files)
    conftest.py
    test_agent.py
    test_browser.py
    test_browser_use_cli.py
    test_browser_use_skill_install_docs.py
    test_captcha.py
    test_compaction.py
    test_compat.py
    test_domains.py
    test_harness_cloud.py
    test_highlight.py
    test_judge.py
    test_keyed_redirects.py
    test_llm.py
    test_local_browser.py
    test_login.py
    test_loop.py
    test_messages.py
    test_repl.py
    test_search.py
    test_telemetry.py
    test_tls.py
    test_ultrafast.py
    test_workflows.py
.dockerignore
.env.example
.gitattributes
.gitignore
.pre-commit-config.yaml
.python-version
AGENTS.md
CLAUDE.md
CLOUD.md
Dockerfile
LICENSE
MIGRATING.md
README.md
context7.json
pyproject.toml
server.json
```

## Entry points

- [browser_use/__main__.py:7](https://github.com/browser-use/browser-use/blob/e717df1839a2d7368b108de6694f01e9c659b0de/browser_use/__main__.py#L7)
- [browser_use/cli.py](https://github.com/browser-use/browser-use/blob/e717df1839a2d7368b108de6694f01e9c659b0de/browser_use/cli.py)
- [browser_use/cli.py](https://github.com/browser-use/browser-use/blob/e717df1839a2d7368b108de6694f01e9c659b0de/browser_use/cli.py)
- [browser_use/cli.py](https://github.com/browser-use/browser-use/blob/e717df1839a2d7368b108de6694f01e9c659b0de/browser_use/cli.py)
- [browser_use/mcp/__main__.py:8](https://github.com/browser-use/browser-use/blob/e717df1839a2d7368b108de6694f01e9c659b0de/browser_use/mcp/__main__.py#L8)
- [browser_use/mcp/cli_mcp.py:900](https://github.com/browser-use/browser-use/blob/e717df1839a2d7368b108de6694f01e9c659b0de/browser_use/mcp/cli_mcp.py#L900)
- [browser_use/repl/worker.py:1244](https://github.com/browser-use/browser-use/blob/e717df1839a2d7368b108de6694f01e9c659b0de/browser_use/repl/worker.py#L1244)
- [docker/smoke.py:34](https://github.com/browser-use/browser-use/blob/e717df1839a2d7368b108de6694f01e9c659b0de/docker/smoke.py#L34)
- [scripts/sync_browser_harness_skill.py:118](https://github.com/browser-use/browser-use/blob/e717df1839a2d7368b108de6694f01e9c659b0de/scripts/sync_browser_harness_skill.py#L118)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 3 file(s) under bin package (observed from repository paths and static analysis). |
| browser_use package | library | Observed | Groups 38 file(s) under browser_use package (observed from repository paths and static analysis). Observed top-level classes: ActionResult, AgentHistoryList, AgentTelemetryEvent, AxHelpers, BaseTelemetryEvent, Browser.… |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. Observed top-level functions: is_running_in_docker, load_env. |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CLIMCPServer, CellStats, CountedBu, HarnessMismatch, NoBrowserError, _CellStream. Observed… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 2 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: Agent, Job, ProductTelemetry. Observed top-level functions: _alive, _check_task_arg, _once_… |
| Tests | test | Observed | Groups 24 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeAuthServer, FakeCloudBrowser, FakeRepl, Handler, LastMessages, Page. Observed top-level functions: _cho… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/1_element_detection_bug.yml` (config)
- `.github/ISSUE_TEMPLATE/2_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/3_feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/4_docs_issue.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/claude.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/install-script.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/package.yaml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/stale-bot.yml` (ci)
- `.github/workflows/test.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `context7.json` (config)
- `pyproject.toml` (manifest)
- `server.json` (config)

## Top-level layout

- `browser_use` — 51 analysed file(s)
- `tests` — 24 analysed file(s)
- `skills` — 19 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 16 analysed file(s)
- `static` — 5 analysed file(s)
- `bin` — 3 analysed file(s)
- `docker` — 1 analysed file(s)
- `examples` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e717df1839a2d7368b108de6694f01e9c659b0de` is the revision these paths and observations refer to.
