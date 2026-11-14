# Project structure: microsoft/playwright-python

**Analysed commit:** `86a5f5a81010b1dbd155263e99782442b61d0cb2`

**Commit reference:** [86a5f5a81010b1dbd155263e99782442b61d0cb2](https://github.com/microsoft/playwright-python/commit/86a5f5a81010b1dbd155263e99782442b61d0cb2)

**Tree at this commit:** [microsoft/playwright-python@86a5f5a81010](https://github.com/microsoft/playwright-python/tree/86a5f5a81010b1dbd155263e99782442b61d0cb2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/playwright-python |
| Description | Python version of the Playwright testing and automation library. |
| Stars | 15108 |
| Forks | 1256 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `86a5f5a81010b1dbd155263e99782442b61d0cb2` |
| Retrieved at | 2026-11-14T19:09:07.156992+00:00 |
| Files in this snapshot | 788 |

## Directory tree

```text
.azure-pipelines/  (2 files)
  guardian/  (1 files)
    SDL/  (1 files)
      … 1 files under this directory
  publish-docker.yml
.claude/  (3 files)
  skills/  (3 files)
    playwright-patch-release/  (1 files)
      … 1 files under this directory
    playwright-release/  (1 files)
      … 1 files under this directory
    playwright-roll/  (1 files)
      … 1 files under this directory
.github/  (15 files)
  ISSUE_TEMPLATE/  (6 files)
    bug.yml
    config.yml
    documentation.yml
    feature.yml
    question.yml
    regression.yml
  workflows/  (8 files)
    agent-patch-release.yml
    agent-review.yml
    agent-roll.yml
    agent-task.yml
    agent-triage.yml
    ci.yml
    publish.yml
    test_docker.yml
  dependabot.yml
examples/  (11 files)
  todomvc/  (11 files)
    mvctests/  (10 files)
      … 10 files under this directory
    requirements.txt
playwright/  (104 files)
  _impl/  (97 files)
    __pyinstaller/  (3 files)
      … 3 files under this directory
    isomorphic/  (9 files)
      … 9 files under this directory
    protocol/  (4 files)
      … 4 files under this directory
    utils/  (9 files)
      … 9 files under this directory
    AGENTS.md
    __init__.py
    _api_classes.py
    _api_structures.py
    _assertions.py
    _async_base.py
    _driver.py
    _errors.py
    _form_data.py
    _greenlets.py
    _helper.py
    _impl_to_api_mapping.py
    _map.py
    _protocol.py
    _protocol_check.py
    _signature.py
    _sync_base.py
    artifact.py
    assertions.py
    browser.py
    browser_context.py
    browser_type.py
    cdp_session.py
    channel_owner.py
    … 48 more files
  async_api/  (2 files)
    __init__.py
    _context_manager.py
  sync_api/  (2 files)
    __init__.py
    _context_manager.py
  __init__.py
  __main__.py
  py.typed
scripts/  (13 files)
  codegen/  (4 files)
    compare_api.py
    generate_api.js
    generate_protocol.py
    python_rules.js
  build_driver.py
  check_test_registry.py
  lint.sh
  pytest_dot_reporter.py
  pytest_line_reporter.py
  update_api.sh
  update_node_version.py
  update_versions.py
  upstream.py
tests/  (622 files)
  assets/  (371 files)
    axe-core/  (4 files)
      … 4 files under this directory
    cached/  (3 files)
      … 3 files under this directory
    client-certificates/  (4 files)
      … 4 files under this directory
    csscoverage/  (9 files)
      … 9 files under this directory
    es6/  (4 files)
      … 4 files under this directory
    evals/  (2 files)
      … 2 files under this directory
    extension-mv3-simple/  (3 files)
      … 3 files under this directory
    extension-mv3-sw-lifecycle/  (2 files)
      … 2 files under this directory
    extension-mv3-with-logging/  (3 files)
      … 3 files under this directory
    frames/  (10 files)
      … 10 files under this directory
    input/  (17 files)
      … 17 files under this directory
    jscoverage/  (9 files)
      … 9 files under this directory
    load-event/  (2 files)
      … 2 files under this directory
    modernizr/  (5 files)
      … 5 files under this directory
    multi-value-rdn/  (1 files)
      … 1 files under this directory
    network-tab/  (3 files)
      … 3 files under this directory
    popup/  (2 files)
      … 2 files under this directory
    screenshots/  (4 files)
      … 4 files under this directory
    selenium-grid/  (2 files)
      … 2 files under this directory
    serviceworkers/  (13 files)
      … 13 files under this directory
    shared-worker/  (2 files)
      … 2 files under this directory
    to-do-notifications/  (6 files)
      … 6 files under this directory
    wasm/  (1 files)
      … 1 files under this directory
    webfont/  (4 files)
      … 4 files under this directory
    worker/  (5 files)
      … 5 files under this directory
    wpt/  (173 files)
      … 173 files under this directory
    background-color.html
    beforeunload.html
    button-overlay-oopif.html
    callback.js
    checkerboard.html
    client.py
    codicon.css
    consolelog.html
    counter.html
    csp.html
    css-transition.html
    deep-shadow.html
    device-motion.html
    device-orientation.html
    dom.html
    download-blob.html
    drag-n-drop.html
    dummy_bad_browser_executable.js
    dynamic-oopif.html
    empty-standard-mode.html
    empty.html
    error.html
    file to upload.txt
    file-to-upload-2.txt
    … 54 more files
  async/  (249 files)
    library/  (100 files)
      … 100 files under this directory
    page/  (127 files)
      … 127 files under this directory
    python/  (20 files)
      … 20 files under this directory
    __init__.py
    conftest.py
  AGENTS.md
  __init__.py
.gitattributes
.gitignore
.pre-commit-config.yaml
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DRIVER_VERSION
LICENSE
NODE_VERSION
README.md
SECURITY.md
SUPPORT.md
local-requirements.txt
pyproject.toml
requirements.txt
setup.cfg
setup.py
test.sh
```

## Entry points

- [playwright/__main__.py](https://github.com/microsoft/playwright-python/blob/86a5f5a81010b1dbd155263e99782442b61d0cb2/playwright/__main__.py)
- [scripts/build_driver.py:296](https://github.com/microsoft/playwright-python/blob/86a5f5a81010b1dbd155263e99782442b61d0cb2/scripts/build_driver.py#L296)
- [scripts/check_test_registry.py:295](https://github.com/microsoft/playwright-python/blob/86a5f5a81010b1dbd155263e99782442b61d0cb2/scripts/check_test_registry.py#L295)
- [scripts/codegen/compare_api.py:496](https://github.com/microsoft/playwright-python/blob/86a5f5a81010b1dbd155263e99782442b61d0cb2/scripts/codegen/compare_api.py#L496)
- [scripts/codegen/generate_protocol.py:763](https://github.com/microsoft/playwright-python/blob/86a5f5a81010b1dbd155263e99782442b61d0cb2/scripts/codegen/generate_protocol.py#L763)
- [scripts/update_node_version.py:52](https://github.com/microsoft/playwright-python/blob/86a5f5a81010b1dbd155263e99782442b61d0cb2/scripts/update_node_version.py#L52)
- [scripts/update_versions.py:39](https://github.com/microsoft/playwright-python/blob/86a5f5a81010b1dbd155263e99782442b61d0cb2/scripts/update_versions.py#L39)
- [scripts/upstream.py:331](https://github.com/microsoft/playwright-python/blob/86a5f5a81010b1dbd155263e99782442b61d0cb2/scripts/upstream.py#L331)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: PlaywrightBDistWheelCommand, PlaywrightSDistCommand. Observed top-level functions: dr… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Command, Converter, Difference, Entry, Func, Interface. Observed top-level functions: _bod… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). |
| playwright package | library | Observed | Groups 99 file(s) under playwright package (observed from repository paths and static analysis). Observed top-level classes: APIRequest, APIRequestContext, APIRequestContextChannel, APIRequestContextCookiesResult, APIRe… |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: DotStatus, LineStatus. Observed top-level functions: pytest_configure. |
| Tests | test | Observed | Groups 630 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CdpEventWaiter, HarPage, StalledRoute, TraceViewerPage. Observed top-level functions: _download_route, _fr… |

## Important files

- `.azure-pipelines/publish-docker.yml` (config)
- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/feature.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/ISSUE_TEMPLATE/regression.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/agent-patch-release.yml` (ci)
- `.github/workflows/agent-review.yml` (ci)
- `.github/workflows/agent-roll.yml` (ci)
- `.github/workflows/agent-task.yml` (ci)
- `.github/workflows/agent-triage.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test_docker.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `examples/todomvc/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `tests` — 622 analysed file(s)
- `playwright` — 104 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 15 analysed file(s)
- `scripts` — 13 analysed file(s)
- `examples` — 11 analysed file(s)
- `.claude` — 3 analysed file(s)
- `.azure-pipelines` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 12 file(s) were skipped during inventory (12 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `86a5f5a81010b1dbd155263e99782442b61d0cb2` is the revision these paths and observations refer to.
