# Project structure: sanic-org/sanic

**Analysed commit:** `5ffc7b3710838eaf016d2f9612a86a08626915e5`

**Commit reference:** [5ffc7b3710838eaf016d2f9612a86a08626915e5](https://github.com/sanic-org/sanic/commit/5ffc7b3710838eaf016d2f9612a86a08626915e5)

**Tree at this commit:** [sanic-org/sanic@5ffc7b371083](https://github.com/sanic-org/sanic/tree/5ffc7b3710838eaf016d2f9612a86a08626915e5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sanic-org/sanic |
| Description |  Accelerate your web app development  | Build fast. Run fast. |
| Stars | 18633 |
| Forks | 1618 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `5ffc7b3710838eaf016d2f9612a86a08626915e5` |
| Retrieved at | 2026-11-14T19:08:22.599429+00:00 |
| Files in this snapshot | 635 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (4 files)
    bug-report.yml
    config.yml
    feature-request.yml
    rfc.yml
  workflows/  (5 files)
    codeql-analysis.yml
    coverage-upload.yml
    coverage.yml
    publish-release.yml
    tests.yml
  CODEOWNERS
  FUNDING.yml
  stale.yml
changelogs/  (4 files)
  .gitignore
  1892.removal.rst
  1904.feature.rst
  1970.misc.rst
docker/  (2 files)
  Dockerfile
  Dockerfile-base
docs/  (26 files)
  _static/  (2 files)
    .gitkeep
    custom.css
  _templates/  (1 files)
    banner.html
  sanic/  (18 files)
    api/  (7 files)
      … 7 files under this directory
    releases/  (8 files)
      … 8 files under this directory
    api_reference.rst
    changelog.rst
    contributing.rst
  Makefile
  conf.py
  index.html
  index.rst
  make.bat
examples/  (38 files)
  request_stream/  (2 files)
    client.py
    server.py
  static/  (1 files)
    robots.txt
  Dockerfile
  add_task_sanic.py
  amending_request_object.py
  authorized_sanic.py
  blueprint_middlware_execution_order.py
  blueprints.py
  delayed_response.py
  docker-compose.yml
  exception_monitoring.py
  hello_world.py
  http_redirect.py
  limit_concurrency.py
  log_request_id.py
  logdna_example.py
  modify_header_example.py
  override_logging.py
  pytest_xdist.py
  raygun_example.py
  redirect_example.py
  request_timeout.py
  rollbar_example.py
  run_asgi.py
  run_async.py
  run_async_advanced.py
  … 11 more files
guide/  (270 files)
  config/  (3 files)
    en/  (3 files)
      … 3 files under this directory
  content/  (102 files)
    en/  (102 files)
      … 102 files under this directory
  public/  (11 files)
    assets/  (6 files)
      … 6 files under this directory
    web/  (4 files)
      … 4 files under this directory
    index.html
  style/  (110 files)
    bulma/  (66 files)
      … 66 files under this directory
    bulma-prefers-dark/  (36 files)
      … 36 files under this directory
    colors.scss
    elements.scss
    general.scss
    home.scss
    index.scss
    menu.scss
    overrides.scss
    theme.scss
  webapp/  (41 files)
    display/  (30 files)
      … 30 files under this directory
    endpoint/  (4 files)
      … 4 files under this directory
    worker/  (6 files)
      … 6 files under this directory
    __init__.py
  Procfile
  requirements.txt
  server.py
sanic/  (136 files)
  application/  (7 files)
    __init__.py
    constants.py
    ext.py
    logo.py
    motd.py
    spinner.py
    state.py
  base/  (3 files)
    __init__.py
    meta.py
    root.py
  cli/  (9 files)
    __init__.py
    app.py
    arguments.py
    base.py
    console.py
    daemon.py
    executor.py
    inspector.py
    inspector_client.py
  cookies/  (3 files)
    __init__.py
    request.py
    response.py
  handlers/  (4 files)
    __init__.py
    content_range.py
    directory.py
    error.py
  http/  (8 files)
    tls/  (3 files)
      … 3 files under this directory
    __init__.py
    constants.py
    http1.py
    http3.py
    stream.py
  logging/  (8 files)
    __init__.py
    color.py
    default.py
    deprecation.py
    filter.py
    formatter.py
    loggers.py
    setup.py
  mixins/  (10 files)
    __init__.py
    base.py
    commands.py
    exceptions.py
    listeners.py
    middleware.py
    routes.py
    signals.py
    startup.py
    static.py
  models/  (8 files)
    __init__.py
    asgi.py
    ctx_types.py
    futures.py
    handler_types.py
    http_types.py
    protocol_types.py
    server_types.py
  pages/  (8 files)
    styles/  (3 files)
      … 3 files under this directory
    __init__.py
    base.py
    css.py
    directory_page.py
    error.py
  request/  (4 files)
    __init__.py
    form.py
    parameters.py
    types.py
  response/  (3 files)
    __init__.py
    convenience.py
    types.py
  server/  (15 files)
    protocols/  (4 files)
      … 4 files under this directory
    websockets/  (4 files)
      … 4 files under this directory
    __init__.py
    async_server.py
    events.py
    goodbye.py
    loop.py
    runners.py
    socket.py
  startup/  (2 files)
    __init__.py
    errors.py
  touchup/  (7 files)
    schemes/  (4 files)
      … 4 files under this directory
    __init__.py
    meta.py
    service.py
  types/  (3 files)
    __init__.py
    hashable_dict.py
    shared_ctx.py
  worker/  (12 files)
    __init__.py
    constants.py
    daemon.py
    inspector.py
    loader.py
    manager.py
    multiplexer.py
    process.py
    reloader.py
    restarter.py
    serve.py
    state.py
  __init__.py
  __main__.py
  __version__.py
  app.py
  asgi.py
  blueprint_group.py
  blueprints.py
  compat.py
  config.py
  constants.py
  errorpages.py
  exceptions.py
  headers.py
  helpers.py
  log.py
  middleware.py
  py.typed
  router.py
  signals.py
  simple.py
  utils.py
  views.py
scripts/  (3 files)
  changelog.py
  pyproject.toml
  release.py
tests/  (125 files)
  benchmark/  (1 files)
    test_route_resolution_benchmark.py
  certs/  (1 files)
    createcerts.py
  fake/  (1 files)
    server.py
  http3/  (4 files)
    __init__.py
    test_http_receiver.py
    test_server.py
    test_session_ticket_store.py
  performance/  (3 files)
    sanic/  (3 files)
      … 3 files under this directory
  static/  (7 files)
    bp/  (2 files)
      … 2 files under this directory
    nested/  (1 files)
      … 1 files under this directory
    app_test_config.py
    decode me.txt
    test.file
    test.html
  typing/  (8 files)
    samples/  (7 files)
      … 7 files under this directory
    test_typing.py
  worker/  (13 files)
    conftest.py
    test_inspector.py
    test_loader.py
    test_manager.py
    test_multiplexer.py
    test_reloader.py
    test_restarter.py
    test_runner.py
    test_shared_ctx.py
    test_socket.py
    test_startup.py
    test_state.py
    test_worker_serve.py
  __init__.py
  asyncmock.py
  client.py
  conftest.py
  skip_test_custom_protocol.py
  test_app.py
  test_asgi.py
  test_bad_request.py
  test_base.py
  test_blueprint_copy.py
  test_blueprint_group.py
  test_blueprints.py
  test_cancellederror.py
  test_cli.py
  test_coffee.py
  test_config.py
  test_constants.py
  test_cookies.py
  test_create_task.py
  test_custom_request.py
  test_daemon.py
  test_deprecation.py
  test_dynamic_routes.py
  test_errorpages.py
  … 63 more files
.appveyor.yml
.coveragerc
.gitattributes
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
Makefile
README.rst
SECURITY.md
bandit.baseline
codecov.yml
crowdin.yml
pyproject.toml
readthedocs.yml
setup.py
tox.ini
```

## Entry points

- [guide/content/en/migrate.py:120](https://github.com/sanic-org/sanic/blob/5ffc7b3710838eaf016d2f9612a86a08626915e5/guide/content/en/migrate.py#L120)
- [sanic/__main__.py](https://github.com/sanic-org/sanic/blob/5ffc7b3710838eaf016d2f9612a86a08626915e5/sanic/__main__.py)
- [scripts/changelog.py:8](https://github.com/sanic-org/sanic/blob/5ffc7b3710838eaf016d2f9612a86a08626915e5/scripts/changelog.py#L8)
- [scripts/release.py:283](https://github.com/sanic-org/sanic/blob/5ffc7b3710838eaf016d2f9612a86a08626915e5/scripts/release.py#L283)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 5 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET (path not a literal). Observed top-level classes: ContentRangeHandler, DirectoryHandler, ErrorHandler. Observed… |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config, DescriptorMeta, DetailedConverter, PyTest. Observed top-level functions: _au… |
| Data layer | data | Observed | Groups 8 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ConnInfo, Credentials, FutureCommand, FutureException, FutureListener, FutureMiddleware. |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ASGIApp, Directory, Lifespan, MainLayout, MockProtocol, MockTransport. Observed top-level… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: InspectorClient. |
| guide package | library | Observed | Groups 39 file(s) under guide package (observed from repository paths and static analysis). Observed top-level classes: Attributes, BaseLayout, BaseRenderer, Column, DocObject, DocsRenderer. Observed top-level functions… |
| sanic package | library | Observed | Groups 112 file(s) under sanic package (observed from repository paths and static analysis). Observed top-level classes: AcceptList, AltSvcCheck, AppLoader, ApplicationGroup, ApplicationServerInfo, ApplicationState. Obs… |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: TouchUp. |
| Tests | test | Observed | Groups 125 file(s) under tests (observed from repository paths and static analysis). Observed routes: GET /, ROUTE /, ROUTE /, ROUTE /sync, ROUTE /text/<name>/<butt:int>. Observed top-level classes: AsyncMock, ConfigTes… |

## Important files

- `.appveyor.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/rfc.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/coverage-upload.yml` (ci)
- `.github/workflows/coverage.yml` (ci)
- `.github/workflows/publish-release.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `MANIFEST.in` (manifest)
- `codecov.yml` (config)
- `crowdin.yml` (config)
- `docker/Dockerfile` (container)
- `docker/Dockerfile-base` (container)
- `examples/Dockerfile` (container)
- `examples/docker-compose.yml` (container)
- `guide/config/en/general.yaml` (config)
- `guide/config/en/navbar.yaml` (config)
- `guide/config/en/sidebar.yaml` (config)
- `guide/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `readthedocs.yml` (config)
- `sanic/logging/setup.py` (manifest)
- `scripts/pyproject.toml` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `guide` — 270 analysed file(s)
- `sanic` — 136 analysed file(s)
- `tests` — 125 analysed file(s)
- `examples` — 38 analysed file(s)
- `docs` — 26 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 12 analysed file(s)
- `changelogs` — 4 analysed file(s)
- `scripts` — 3 analysed file(s)
- `docker` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (7 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5ffc7b3710838eaf016d2f9612a86a08626915e5` is the revision these paths and observations refer to.
