# Project structure: g1879/DrissionPage

**Analysed commit:** `7761b855300a2dc4efc32c000be8150b60d21b97`

**Commit reference:** [7761b855300a2dc4efc32c000be8150b60d21b97](https://github.com/g1879/DrissionPage/commit/7761b855300a2dc4efc32c000be8150b60d21b97)

**Tree at this commit:** [g1879/DrissionPage@7761b855300a](https://github.com/g1879/DrissionPage/tree/7761b855300a2dc4efc32c000be8150b60d21b97)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | g1879/DrissionPage |
| Description | Python based web automation tool. Powerful and elegant. |
| Stars | 12576 |
| Forks | 1144 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `7761b855300a2dc4efc32c000be8150b60d21b97` |
| Retrieved at | 2026-11-14T19:10:04.455156+00:00 |
| Files in this snapshot | 167 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    drissionpage-tests.yml
DrissionPage/  (82 files)
  _base/  (4 files)
    base.py
    base.pyi
    driver.py
    driver.pyi
  _browsers/  (4 files)
    chromium.py
    chromium.pyi
    chromium_context.py
    chromium_context.pyi
  _configs/  (7 files)
    chromium_options.py
    chromium_options.pyi
    configs.ini
    options_manage.py
    options_manage.pyi
    session_options.py
    session_options.pyi
  _elements/  (6 files)
    chromium_element.py
    chromium_element.pyi
    none_element.py
    none_element.pyi
    session_element.py
    session_element.pyi
  _functions/  (19 files)
    browser.py
    browser.pyi
    by.py
    cli.py
    cookies.py
    cookies.pyi
    elements.py
    elements.pyi
    keys.py
    keys.pyi
    locator.py
    locator.pyi
    settings.py
    settings.pyi
    texts.py
    tools.py
    tools.pyi
    web.py
    web.pyi
  _pages/  (8 files)
    chromium_base.py
    chromium_base.pyi
    chromium_frame.py
    chromium_frame.pyi
    chromium_tab.py
    chromium_tab.pyi
    session_page.py
    session_page.pyi
  _units/  (28 files)
    actions.py
    actions.pyi
    clicker.py
    clicker.pyi
    console.py
    console.pyi
    cookies_setter.py
    cookies_setter.pyi
    downloader.py
    downloader.pyi
    listener.py
    listener.pyi
    perm_setter.py
    perm_setter.pyi
    rect.py
    rect.pyi
    screencast.py
    screencast.pyi
    scroller.py
    scroller.pyi
    selector.py
    selector.pyi
    setter.py
    setter.pyi
    … 4 more files
  __init__.py
  __init__.pyi
  common.py
  errors.py
  items.py
  version.py
tests/  (78 files)
  feature_cases/  (54 files)
    __init__.py
    browser_interaction_server.py
    core_feature_server.py
    ssr_test_site.py
    test_api_behavior_changes.py
    test_base_page_contracts.py
    test_browser_contexts.py
    test_browser_download.py
    test_browser_helper_contracts.py
    test_browser_lifecycle_extra_contracts.py
    test_chromium_base_extra_contracts.py
    test_chromium_browser_contracts.py
    test_chromium_element_contracts.py
    test_chromium_element_extra_contracts.py
    test_chromium_options_environment.py
    test_chromium_tab_management.py
    test_collection_action_contracts.py
    test_config_session_contracts.py
    test_console_and_cookie_formats.py
    test_cookie_setters.py
    test_cross_origin_iframe_elements.py
    test_cross_origin_iframe_listener.py
    test_download_management.py
    test_element_core_behaviors.py
    … 30 more files
  regression_cases/  (14 files)
    __init__.py
    test_alert_on_open.py
    test_api_surface.py
    test_console_and_tabs.py
    test_context_get_tabs_as_id.py
    test_context_isolation.py
    test_download_browser.py
    test_iframe_non_screenshot.py
    test_listener_ws_sse.py
    test_locator_behavior.py
    test_locator_explicit_syntax.py
    test_navigation_result.py
    test_no_browser_contract_gaps.py
    test_session_timeout.py
  README.md
  check_ci_retry.py
  check_runner_quality.py
  check_workflow_quality.py
  ci.sh
  feature_manifest.py
  run.py
  run.sh
  runner.py
  support.py
.coveragerc
.gitignore
LICENSE
MANIFEST.in
README.md
requirements.txt
```

## Entry points

- [DrissionPage/_functions/cli.py:52](https://github.com/g1879/DrissionPage/blob/7761b855300a2dc4efc32c000be8150b60d21b97/DrissionPage/_functions/cli.py#L52)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Settings. |
| DrissionPage package | library | Observed | Groups 42 file(s) under drissionpage package (observed from repository paths and static analysis). Observed top-level classes: Actions, Alert, AlertExistsError, BaseElement, BaseError, BaseListener. Observed top-level f… |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main, set_paths. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 78 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Click. Observed top-level classes: ActionLog, Case, ElementScroll, FakeActionElement, FakeActio… |

## Important files

- `.github/workflows/drissionpage-tests.yml` (ci)
- `DrissionPage/_configs/configs.ini` (config)
- `MANIFEST.in` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `DrissionPage` — 82 analysed file(s)
- `tests` — 78 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7761b855300a2dc4efc32c000be8150b60d21b97` is the revision these paths and observations refer to.
