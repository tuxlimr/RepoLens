# Project structure: pallets/flask

**Analysed commit:** `49943b5a94413a530761350f04e896f76e8d620e`

**Commit reference:** [49943b5a94413a530761350f04e896f76e8d620e](https://github.com/pallets/flask/commit/49943b5a94413a530761350f04e896f76e8d620e)

**Tree at this commit:** [pallets/flask@49943b5a9441](https://github.com/pallets/flask/tree/49943b5a94413a530761350f04e896f76e8d620e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pallets/flask |
| Description | The Python micro framework for building web applications. |
| Stars | 75116 |
| Forks | 17330 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `49943b5a94413a530761350f04e896f76e8d620e` |
| Retrieved at | 2026-11-14T19:06:13.197322+00:00 |
| Files in this snapshot | 229 |

## Directory tree

```text
.devcontainer/  (2 files)
  devcontainer.json
  on-create-command.sh
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    config.yml
    feature-request.md
  workflows/  (5 files)
    lock.yaml
    pre-commit.yaml
    publish.yaml
    tests.yaml
    zizmor.yaml
  pull_request_template.md
docs/  (82 files)
  _static/  (3 files)
    flask-icon.svg
    flask-logo.svg
    flask-name.svg
  deploying/  (11 files)
    apache-httpd.rst
    asgi.rst
    eventlet.rst
    gevent.rst
    gunicorn.rst
    index.rst
    mod_wsgi.rst
    nginx.rst
    proxy_fix.rst
    uwsgi.rst
    waitress.rst
  patterns/  (25 files)
    appdispatch.rst
    appfactories.rst
    caching.rst
    celery.rst
    deferredcallbacks.rst
    favicon.rst
    fileuploads.rst
    flashing.rst
    index.rst
    javascript.rst
    jquery.rst
    lazyloading.rst
    methodoverrides.rst
    mongoengine.rst
    packages.rst
    requestchecksum.rst
    singlepageapplications.rst
    sqlalchemy.rst
    sqlite3.rst
    streaming.rst
    subclassing.rst
    templateinheritance.rst
    urlprocessors.rst
    viewdecorators.rst
    … 1 more files
  tutorial/  (12 files)
    blog.rst
    database.rst
    deploy.rst
    factory.rst
    index.rst
    install.rst
    layout.rst
    next.rst
    static.rst
    templates.rst
    tests.rst
    views.rst
  Makefile
  api.rst
  appcontext.rst
  async-await.rst
  blueprints.rst
  changes.rst
  cli.rst
  conf.py
  config.rst
  contributing.rst
  debugging.rst
  design.rst
  errorhandling.rst
  extensiondev.rst
  extensions.rst
  gevent.rst
  index.rst
  installation.rst
  license.rst
  lifecycle.rst
  logging.rst
  make.bat
  quickstart.rst
  reqcontext.rst
  … 7 more files
examples/  (42 files)
  celery/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    README.md
    make_celery.py
    pyproject.toml
    requirements.txt
  javascript/  (12 files)
    js_example/  (6 files)
      … 6 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    .gitignore
    LICENSE.txt
    README.rst
    pyproject.toml
  tutorial/  (22 files)
    flaskr/  (12 files)
      … 12 files under this directory
    tests/  (6 files)
      … 6 files under this directory
    .gitignore
    LICENSE.txt
    README.rst
    pyproject.toml
src/  (26 files)
  flask/  (26 files)
    json/  (3 files)
      … 3 files under this directory
    sansio/  (4 files)
      … 4 files under this directory
    __init__.py
    __main__.py
    app.py
    blueprints.py
    cli.py
    config.py
    ctx.py
    debughelpers.py
    globals.py
    helpers.py
    logging.py
    py.typed
    sessions.py
    signals.py
    templating.py
    testing.py
    typing.py
    views.py
    wrappers.py
tests/  (60 files)
  static/  (3 files)
    config.json
    config.toml
    index.html
  templates/  (9 files)
    nested/  (1 files)
      … 1 files under this directory
    _macro.html
    context_template.html
    escaping_template.html
    mail.txt
    non_escaping_template.txt
    simple_template.html
    template_filter.html
    template_test.html
  test_apps/  (22 files)
    blueprintapp/  (8 files)
      … 8 files under this directory
    cliapp/  (9 files)
      … 9 files under this directory
    helloworld/  (2 files)
      … 2 files under this directory
    subdomaintestmodule/  (2 files)
      … 2 files under this directory
    .flaskenv
  type_check/  (3 files)
    typing_app_decorators.py
    typing_error_handler.py
    typing_route.py
  conftest.py
  test_appctx.py
  test_async.py
  test_basic.py
  test_blueprints.py
  test_cli.py
  test_config.py
  test_converters.py
  test_helpers.py
  test_instance_config.py
  test_json.py
  test_json_tag.py
  test_logging.py
  test_regression.py
  test_reqctx.py
  test_request.py
  test_session_interface.py
  test_signals.py
  test_subclassing.py
  test_templating.py
  test_testing.py
  test_user_error_handler.py
  test_views.py
.editorconfig
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
CHANGES.rst
LICENSE.txt
README.md
pyproject.toml
```

## Entry points

- [src/flask/cli.py](https://github.com/pallets/flask/blob/49943b5a94413a530761350f04e896f76e8d620e/src/flask/cli.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, ConfigAttribute. |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: App, AppGroup, CertParamType, Flask, FlaskGroup, NoAppException. Observed top-level functi… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| flask package | library | Observed | Groups 19 file(s) under flask package (observed from repository paths and static analysis). Observed top-level classes: AppContext, Blueprint, BlueprintSetupState, DebugFilesKeyError, DefaultJSONProvider, DispatchingJin… |
| Tests | test | Observed | Groups 68 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Flask, Group. Observed routes: ROUTE /, ROUTE /index2, ROUTE /, ROUTE /missing, ROUTE /. Observ… |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/lock.yaml` (ci)
- `.github/workflows/pre-commit.yaml` (ci)
- `.github/workflows/publish.yaml` (ci)
- `.github/workflows/tests.yaml` (ci)
- `.github/workflows/zizmor.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `examples/celery/pyproject.toml` (manifest)
- `examples/celery/requirements.txt` (manifest)
- `examples/javascript/pyproject.toml` (manifest)
- `examples/tutorial/pyproject.toml` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `docs` — 82 analysed file(s)
- `tests` — 60 analysed file(s)
- `examples` — 42 analysed file(s)
- `src` — 26 analysed file(s)
- `.github` — 9 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.devcontainer` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `49943b5a94413a530761350f04e896f76e8d620e` is the revision these paths and observations refer to.
