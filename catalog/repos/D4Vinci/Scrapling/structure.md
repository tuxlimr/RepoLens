# Project structure: D4Vinci/Scrapling

**Analysed commit:** `bb223f2f5fc8f743772751a5ce283ef7851ca6be`

**Commit reference:** [bb223f2f5fc8f743772751a5ce283ef7851ca6be](https://github.com/D4Vinci/Scrapling/commit/bb223f2f5fc8f743772751a5ce283ef7851ca6be)

**Tree at this commit:** [D4Vinci/Scrapling@bb223f2f5fc8](https://github.com/D4Vinci/Scrapling/tree/bb223f2f5fc8f743772751a5ce283ef7851ca6be)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | D4Vinci/Scrapling |
| Description | 🕷️ The BEST Web Scraping framework that handles everything from a single request to a full-scale crawl! Don't be shy, join here: https://discord.gg/EMgGbDceNQ and follow here for daily tips and tricks: https://x.com/Scrapling_dev |
| Stars | 102861 |
| Forks | 10716 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `bb223f2f5fc8f743772751a5ce283ef7851ca6be` |
| Retrieved at | 2026-11-14T19:06:08.004897+00:00 |
| Files in this snapshot | 551 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (5 files)
    01-bug_report.yml
    02-feature_request.yml
    03-other.yml
    04-docs_issue.yml
    config.yml
  workflows/  (5 files)
    code-quality.yml
    docker-build.yml
    release-and-publish.yml
    stale.yml
    tests.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
agent-skill/  (26 files)
  Scrapling-Skill/  (25 files)
    examples/  (5 files)
      … 5 files under this directory
    references/  (18 files)
      … 18 files under this directory
    LICENSE.txt
    SKILL.md
  README.md
docs/  (414 files)
  ai/  (3 files)
    agent-skill.md
    building-rag-systems.md
    mcp-server.md
  api-reference/  (7 files)
    custom-types.md
    fetchers.md
    mcp-server.md
    proxy-rotation.md
    response.md
    selector.md
    spiders.md
  assets/  (3 files)
    javascripts/  (1 files)
      … 1 files under this directory
    cover_dark.svg
    cover_light.svg
  cli/  (3 files)
    extract-commands.md
    interactive-shell.md
    overview.md
  development/  (2 files)
    adaptive_storage_system.md
    scrapling_custom_types.md
  fetching/  (3 files)
    choosing.md
    static.md
    stealthy.md
  integrations/  (1 files)
    scrapy.md
  locales/  (342 files)
    ar/  (38 files)
      … 38 files under this directory
    de/  (38 files)
      … 38 files under this directory
    es/  (38 files)
      … 38 files under this directory
    fr/  (38 files)
      … 38 files under this directory
    ja/  (38 files)
      … 38 files under this directory
    ko/  (38 files)
      … 38 files under this directory
    pt-BR/  (38 files)
      … 38 files under this directory
    ru/  (38 files)
      … 38 files under this directory
    zh/  (38 files)
      … 38 files under this directory
  overrides/  (20 files)
    api/  (19 files)
      … 19 files under this directory
    main.html
  parsing/  (3 files)
    adaptive.md
    main_classes.md
    selection.md
  spiders/  (8 files)
    advanced.md
    architecture.md
    generic-templates.md
    getting-started.md
    platform-templates.md
    proxy-blocking.md
    requests-responses.md
    sessions.md
  stylesheets/  (1 files)
    extra.css
  tutorials/  (2 files)
    migrating_from_beautifulsoup.md
    replacing_ai.md
  README_AR.md
  README_CN.md
  README_DE.md
  README_ES.md
  README_FR.md
  README_JP.md
  README_KR.md
  README_PT_BR.md
  README_RU.md
  benchmarks.md
  changelog.md
  donate.md
  index.md
  migrating-to-v0.5.md
  overview.md
  requirements.txt
includes/  (1 files)
  sponsors.html
scrapling/  (63 files)
  core/  (16 files)
    ai/  (5 files)
      … 5 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    __init__.py
    _shell_signatures.py
    _types.py
    custom_types.py
    mixins.py
    shell.py
    storage.py
    translator.py
  engines/  (19 files)
    _browsers/  (9 files)
      … 9 files under this directory
    toolbelt/  (7 files)
      … 7 files under this directory
    __init__.py
    constants.py
    static.py
  fetchers/  (3 files)
    __init__.py
    requests.py
    stealth_chrome.py
  integrations/  (2 files)
    __init__.py
    scrapy.py
  spiders/  (19 files)
    templates/  (7 files)
      … 7 files under this directory
    __init__.py
    cache.py
    checkpoint.py
    engine.py
    links.py
    request.py
    result.py
    robotstxt.py
    scheduler.py
    session.py
    spider.py
    throttle.py
  __init__.py
  cli.py
  parser.py
  py.typed
tests/  (15 files)
  ai/  (6 files)
    __init__.py
    test_ai_mcp.py
    test_browser_actions.py
    test_browser_buttons.py
    test_browser_dialog.py
    test_browser_dialog_live.py
  cli/  (1 files)
    __init__.py
  core/  (1 files)
    __init__.py
  fetchers/  (3 files)
    async/  (1 files)
      … 1 files under this directory
    sync/  (1 files)
      … 1 files under this directory
    __init__.py
  integrations/  (1 files)
    __init__.py
  parser/  (1 files)
    __init__.py
  spiders/  (1 files)
    __init__.py
  __init__.py
.bandit.yml
.dockerignore
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
AI_POLICY.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
MANIFEST.in
README.md
ROADMAP.md
benchmarks.py
cleanup.py
pyproject.toml
pytest.ini
ruff.toml
server.json
setup.cfg
```

## Entry points

- [benchmarks.py:121](https://github.com/D4Vinci/Scrapling/blob/bb223f2f5fc8f743772751a5ce283ef7851ca6be/benchmarks.py#L121)
- [cleanup.py:41](https://github.com/D4Vinci/Scrapling/blob/bb223f2f5fc8f743772751a5ce283ef7851ca6be/cleanup.py#L41)
- [scrapling/cli.py](https://github.com/D4Vinci/Scrapling/blob/bb223f2f5fc8f743772751a5ce283ef7851ca6be/scrapling/cli.py)
- [scrapling/cli.py](https://github.com/D4Vinci/Scrapling/blob/bb223f2f5fc8f743772751a5ce283ef7851ca6be/scrapling/cli.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| agent-skill package | library | Observed | Groups 3 file(s) under agent-skill package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: NetworkRequestsModel, QuotesSpider, ResponseModel, ScraplingMCPServer, SessionClosedModel,… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: convert_response, scrapling_response. |
| scrapling package | library | Observed | Groups 43 file(s) under scrapling package (observed from repository paths and static analysis). Observed top-level classes: AsyncFetcher, AsyncFetcherClient, AsyncRemoteSession, AsyncSession, AsyncStealthySession, AutoT… |
| Service / domain layer | service | Observed | Groups 15 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AttributesHandler, Convertor, CurlParser, CustomShell, HTMLTranslator, LoggerProxy. Observ… |
| Tests | test | Observed | Groups 15 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestBrowserFetchForwarding, TestExecutablePath, TestMCPServerAuthentication, TestModeSplitContract, TestNor… |

## Important files

- `.bandit.yml` (config)
- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/01-bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/02-feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/03-other.yml` (config)
- `.github/ISSUE_TEMPLATE/04-docs_issue.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/code-quality.yml` (ci)
- `.github/workflows/docker-build.yml` (ci)
- `.github/workflows/release-and-publish.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `docs/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `ruff.toml` (config)
- `server.json` (config)
- `setup.cfg` (manifest)

## Top-level layout

- `docs` — 414 analysed file(s)
- `scrapling` — 63 analysed file(s)
- `agent-skill` — 26 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `tests` — 15 analysed file(s)
- `.github` — 12 analysed file(s)
- `includes` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bb223f2f5fc8f743772751a5ce283ef7851ca6be` is the revision these paths and observations refer to.
