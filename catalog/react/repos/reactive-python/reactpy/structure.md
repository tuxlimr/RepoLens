# Project structure: reactive-python/reactpy

**Analysed commit:** `4b765d44986a29071d7b09cbeb63b2826da6e411`

**Commit reference:** [4b765d44986a29071d7b09cbeb63b2826da6e411](https://github.com/reactive-python/reactpy/commit/4b765d44986a29071d7b09cbeb63b2826da6e411)

**Tree at this commit:** [reactive-python/reactpy@4b765d44986a](https://github.com/reactive-python/reactpy/tree/4b765d44986a29071d7b09cbeb63b2826da6e411)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reactive-python/reactpy |
| Description | It's React, but in Python |
| Stars | 8151 |
| Forks | 330 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `4b765d44986a29071d7b09cbeb63b2826da6e411` |
| Retrieved at | 2026-11-14T19:13:42.734398+00:00 |
| Files in this snapshot | 344 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (2 files)
    config.yml
    issue-form.yml
  workflows/  (4 files)
    .hatch-run.yml
    check.yml
    codeql-analysis.yml
    publish.yml
  CODEOWNERS
  FUNDING.yml
  copilot-instructions.md
  pull_request_template.md
branding/  (4 files)
  svg/  (4 files)
    reactpy-logo-landscape-padded.svg
    reactpy-logo-landscape.svg
    reactpy-logo-square-padded.svg
    reactpy-logo-square.svg
docs/  (154 files)
  docs_app/  (5 files)
    __init__.py
    app.py
    dev.py
    examples.py
    prod.py
  source/  (144 files)
    _custom_js/  (4 files)
      … 4 files under this directory
    _exts/  (8 files)
      … 8 files under this directory
    _static/  (6 files)
      … 6 files under this directory
    about/  (3 files)
      … 3 files under this directory
    guides/  (102 files)
      … 102 files under this directory
    reference/  (19 files)
      … 19 files under this directory
    conf.py
    index.rst
  .gitignore
  Dockerfile
  README.md
  main.py
  pyproject.toml
src/  (88 files)
  build_scripts/  (8 files)
    build_js_app.py
    build_js_client.py
    build_py_wheel.py
    clean_js_dir.py
    copy_dir.py
    delete_old_coverage.py
    install_deps.py
    install_playwright.py
  js/  (25 files)
    packages/  (21 files)
      … 21 files under this directory
    .gitignore
    eslint.config.mjs
    package.json
    tsconfig.json
  reactpy/  (55 files)
    _console/  (5 files)
      … 5 files under this directory
    core/  (11 files)
      … 11 files under this directory
    executors/  (12 files)
      … 12 files under this directory
    reactjs/  (4 files)
      … 4 files under this directory
    static/  (1 files)
      … 1 files under this directory
    templatetags/  (2 files)
      … 2 files under this directory
    testing/  (5 files)
      … 5 files under this directory
    web/  (3 files)
      … 3 files under this directory
    __init__.py
    _event_proxy.py
    _html.py
    _option.py
    _warnings.py
    config.py
    logging.py
    py.typed
    transforms.py
    types.py
    utils.py
    widgets.py
tests/  (79 files)
  templates/  (3 files)
    index.html
    jinja_bad_kwargs.html
    pyscript.html
  test_asgi/  (9 files)
    pyscript_components/  (3 files)
      … 3 files under this directory
    __init__.py
    test_init.py
    test_middleware.py
    test_pyscript.py
    test_standalone.py
    test_utils.py
  test_console/  (3 files)
    __init__.py
    test_rewrite_keys.py
    test_rewrite_props.py
  test_core/  (9 files)
    __init__.py
    test_component.py
    test_event_inspect.py
    test_event_proxy.py
    test_events.py
    test_hooks.py
    test_layout.py
    test_serve.py
    test_vdom.py
  test_pyscript/  (6 files)
    pyscript_components/  (3 files)
      … 3 files under this directory
    __init__.py
    test_components.py
    test_utils.py
  test_reactjs/  (17 files)
    js_fixtures/  (13 files)
      … 13 files under this directory
    __init__.py
    test_modules.py
    test_modules_from_npm.py
    test_utils.py
  test_web/  (14 files)
    js_fixtures/  (12 files)
      … 12 files under this directory
    __init__.py
    test_module.py
  tooling/  (6 files)
    __init__.py
    aio.py
    common.py
    hooks.py
    layout.py
    select.py
  __init__.py
  conftest.py
  sample.py
  test_build_py_wheel.py
  test_client.py
  test_config.py
  test_html.py
  test_option.py
  test_sample.py
  test_testing.py
  test_utils.py
  test_widgets.py
.editorconfig
.gitignore
.pre-commit-config.yaml
.prettierrc
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
README.md
pyproject.toml
```

## Entry points

- [src/build_scripts/build_py_wheel.py:149](https://github.com/reactive-python/reactpy/blob/4b765d44986a29071d7b09cbeb63b2826da6e411/src/build_scripts/build_py_wheel.py#L149)
- [src/build_scripts/copy_dir.py:24](https://github.com/reactive-python/reactpy/blob/4b765d44986a29071d7b09cbeb63b2826da6e411/src/build_scripts/copy_dir.py#L24)
- [src/build_scripts/install_deps.py:43](https://github.com/reactive-python/reactpy/blob/4b765d44986a29071d7b09cbeb63b2826da6e411/src/build_scripts/install_deps.py#L43)
- [src/reactpy/_console/cli.py](https://github.com/reactive-python/reactpy/blob/4b765d44986a29071d7b09cbeb63b2826da6e411/src/reactpy/_console/cli.py)
- [src/reactpy/_console/rewrite_keys.py:18](https://github.com/reactive-python/reactpy/blob/4b765d44986a29071d7b09cbeb63b2826da6e411/src/reactpy/_console/rewrite_keys.py#L18)
- [src/reactpy/_console/rewrite_props.py:20](https://github.com/reactive-python/reactpy/blob/4b765d44986a29071d7b09cbeb63b2826da6e411/src/reactpy/_console/rewrite_props.py#L20)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| build_scripts package | library | Observed | Groups 4 file(s) under build_scripts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: boolean. |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _build_packaged_static_assets, _hatch_build_command, _hatch_command, _matching_reactpy_w… |
| External integrations | external | Observed | Groups 12 file(s) under external integrations (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 5 file(s) under js package (observed from repository paths and static analysis). |
| reactpy package | library | Observed | Groups 40 file(s) under reactpy package (observed from repository paths and static analysis). Observed top-level classes: AsgiV2Protocol, BackendFixture, BaseEventHandler, BaseLayout, ChangedNode, Component. Observed to… |
| Service / domain layer | service | Observed | Groups 11 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: EffectFunc, EventHandler, Layout, LifeCycleHook, ThreadLocal, Vdom. Observed top-level fun… |
| Tests | test | Observed | Groups 80 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CannedClient, ElementInfo, Event, FakeClient, LayoutRunner, Method. Observed top-level functions: Counter,… |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/issue-form.yml` (config)
- `.github/workflows/.hatch-run.yml` (ci)
- `.github/workflows/check.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `docs/Dockerfile` (container)
- `docs/pyproject.toml` (manifest)
- `docs/source/_custom_js/package.json` (manifest)
- `docs/source/guides/adding-interactivity/components-with-state/_examples/adding_state_variable/data.json` (config)
- `docs/source/guides/adding-interactivity/components-with-state/_examples/isolated_state/data.json` (config)
- `docs/source/guides/adding-interactivity/components-with-state/_examples/multiple_state_variables/data.json` (config)
- `docs/source/guides/adding-interactivity/components-with-state/_examples/when_variables_are_not_enough/data.json` (config)
- `docs/source/guides/managing-state/sharing-component-state/_examples/filterable_list/data.json` (config)
- `docs/source/reference/_static/vdom-json-schema.json` (config)
- `pyproject.toml` (manifest)
- `src/js/package.json` (manifest)
- `src/js/packages/@reactpy/app/package.json` (manifest)
- `src/js/packages/@reactpy/app/tsconfig.json` (config)
- `src/js/packages/@reactpy/client/package.json` (manifest)
- `src/js/packages/@reactpy/client/tsconfig.json` (config)
- `src/js/tsconfig.json` (config)

## Top-level layout

- `docs` — 154 analysed file(s)
- `src` — 88 analysed file(s)
- `tests` — 79 analysed file(s)
- `.github` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `branding` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4b765d44986a29071d7b09cbeb63b2826da6e411` is the revision these paths and observations refer to.
