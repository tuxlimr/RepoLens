# Project structure: locustio/locust

**Analysed commit:** `3debc468b53f10d00cb7b449c8f6086f2e5c5be1`

**Commit reference:** [3debc468b53f10d00cb7b449c8f6086f2e5c5be1](https://github.com/locustio/locust/commit/3debc468b53f10d00cb7b449c8f6086f2e5c5be1)

**Tree at this commit:** [locustio/locust@3debc468b53f](https://github.com/locustio/locust/tree/3debc468b53f10d00cb7b449c8f6086f2e5c5be1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | locustio/locust |
| Description | Write scalable load tests in plain Python 🚗💨 |
| Stars | 28285 |
| Forks | 3275 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `3debc468b53f10d00cb7b449c8f6086f2e5c5be1` |
| Retrieved at | 2026-11-14T19:07:16.873399+00:00 |
| Files in this snapshot | 408 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.yml
    config.yml
    feature_request.yml
  workflows/  (2 files)
    stale.yml
    tests.yml
  CONTRIBUTING.md
  dependabot.yaml
.vscode/  (4 files)
  extensions.json
  launch.json
  launch_locust.json
  settings.json
benchmarks/  (1 files)
  dispatch.py
docs/  (36 files)
  _ext/  (1 files)
    llms_txt.py
  _static/  (2 files)
    azure-logo.svg
    theme-overrides.css
  _templates/  (1 files)
    footer.html
  images/  (1 files)
    microsoft_logo.svg
  ai-docs.rst
  api.rst
  asyncio.rst
  changelog.rst
  conf.py
  configuration.rst
  developing-locust.rst
  extending-locust.rst
  extensions.rst
  faq.rst
  further-reading.rst
  history.rst
  hosted-load-testing.rst
  increase-performance.rst
  increasing-request-rate.rst
  index.rst
  installation.rst
  kubernetes-operator.rst
  logging.rst
  quickstart.rst
  running-distributed.rst
  running-in-debugger.rst
  running-in-docker.rst
  running-without-web-ui.rst
  … 7 more files
examples/  (84 files)
  azure/  (4 files)
    README.md
    grpc.yaml
    postgres.yaml
    requirements.txt
  custom_shape/  (5 files)
    double_wave.py
    stages.py
    staging_user_classes.py
    step_load.py
    wait_user_count.py
  custom_xmlrpc_client/  (2 files)
    server.py
    xmlrpc_locustfile.py
  dispatch_test_scripts/  (5 files)
    locustfile.py
    run-distributed-headless.sh
    run-distributed-web.sh
    run-local-headless.sh
    run-local-web.sh
  docker-compose/  (1 files)
    docker-compose.yml
  grpc/  (6 files)
    grpc_user.py
    hello.proto
    hello_pb2.py
    hello_pb2_grpc.py
    hello_server.py
    locustfile.py
  milvus/  (2 files)
    README.md
    locustfile.py
  mongodb/  (2 files)
    README.md
    locustfile.py
  mqtt/  (4 files)
    mosquitto_config/  (1 files)
      … 1 files under this directory
    README.md
    locustfile.py
    locustfile_custom_mqtt_client.py
  postgres/  (2 files)
    README.md
    locustfile.py
  qdrant/  (2 files)
    README.md
    locustfile.py
  sdk_session_patching/  (1 files)
    session_patch_locustfile.py
  socketio/  (2 files)
    echo_server.py
    socketio_ex.py
  terraform/  (7 files)
    aws/  (7 files)
      … 7 files under this directory
  vagrant/  (2 files)
    README.md
    supervisord.conf
  web_ui_auth/  (2 files)
    basic.py
    custom_form.py
  add_command_line_argument.py
  basic.py
  bottlenecked_server.py
  browse_docs_sequence_test.py
  browse_docs_test.py
  csrf_form_authentication.py
  custom_messages.py
  custom_wait_function.py
  debugging.py
  debugging_advanced.py
  dns_ex.py
  dynamic_user_credentials.py
  events.py
  extend_web_ui.py
  fast_http_locust.py
  locustfile.py
  manual_stats_reporting.py
  markov_taskset.py
  multiple_hosts.py
  nested_inline_tasksets.py
  open_closed_workload.py
  openai_ex.py
  poisson_demo.py
  response_validations.py
  … 11 more files
locust/  (253 files)
  contrib/  (11 files)
    __init__.py
    csv_request_logger.py
    dns.py
    fasthttp.py
    milvus.py
    mongodb.py
    mqtt.py
    oai.py
    postgres.py
    qdrant.py
    socketio.py
  rpc/  (3 files)
    __init__.py
    protocol.py
    zmqrpc.py
  test/  (41 files)
    __init__.py
    fake_module1_for_env_test.py
    fake_module2_for_env_test.py
    mock_locustfile.py
    mock_logging.py
    subprocess_utils.py
    test_csv_request_logger.py
    test_date.py
    test_debugging.py
    test_dispatch.py
    test_env.py
    test_event.py
    test_fasthttp.py
    test_html_filename.py
    test_http.py
    test_interruptible_task.py
    test_load_locustfile.py
    test_locust_class.py
    test_log.py
    test_main.py
    test_markov_taskset.py
    test_mongodb.py
    test_oai.py
    test_old_wait_api.py
    … 17 more files
  user/  (7 files)
    __init__.py
    inspectuser.py
    markov_taskset.py
    sequential_taskset.py
    task.py
    users.py
    wait_time.py
  util/  (10 files)
    __init__.py
    cache.py
    date.py
    deprecation.py
    directory.py
    exception_handler.py
    load_locustfile.py
    rounding.py
    timespan.py
    url.py
  webui/  (162 files)
    src/  (146 files)
      … 146 files under this directory
    .gitignore
    .prettierrc
    .yarnrc.yml
    LICENSE
    README.md
    auth.html
    dev.html
    eslint.config.mjs
    index.html
    package.json
    report.html
    tsconfig.json
    vite.config.ts
    vite.lib.config.ts
    vite.report.config.ts
    vitest.config.ts
  __init__.py
  __main__.py
  argument_parser.py
  clients.py
  debug.py
  dispatch.py
  env.py
  event.py
  exception.py
  html.py
  input_events.py
  log.py
  main.py
  opentelemetry.py
  py.typed
  runners.py
  shape.py
  stats.py
  web.py
pytest_locust/  (1 files)
  plugin.py
.coveragerc
.dockerignore
.git-blame-ignore-revs
.gitattributes
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
AGENTS.md
CHANGELOG.md
Dockerfile
Dockerfile.ci
Dockerfile.otel
LICENSE
Makefile
README.md
SECURITY.md
Vagrantfile
_typos.toml
generate_changelog.py
hatch_build.py
package.json
pyproject.toml
```

## Entry points

- [benchmarks/dispatch.py:50](https://github.com/locustio/locust/blob/3debc468b53f10d00cb7b449c8f6086f2e5c5be1/benchmarks/dispatch.py#L50)
- [locust/main.py](https://github.com/locustio/locust/blob/3debc468b53f10d00cb7b449c8f6086f2e5c5be1/locust/main.py)
- [locust/runners.py:249](https://github.com/locustio/locust/blob/3debc468b53f10d00cb7b449c8f6086f2e5c5be1/locust/runners.py#L249)
- [locust/web.py:159](https://github.com/locustio/locust/blob/3debc468b53f10d00cb7b449c8f6086f2e5c5be1/locust/web.py#L159)
- [locust/webui/src/App.tsx](https://github.com/locustio/locust/blob/3debc468b53f10d00cb7b449c8f6086f2e5c5be1/locust/webui/src/App.tsx)
- [locust/webui/src/index.tsx](https://github.com/locustio/locust/blob/3debc468b53f10d00cb7b449c8f6086f2e5c5be1/locust/webui/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: BuildFrontend. |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask, Group. Observed top-level classes: AuthArgs, AuthProvider, CustomForm,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| locust package | library | Observed | Groups 158 file(s) under locust package (observed from repository paths and static analysis). Observed top-level classes: BaseClient, BaseSocket, CSVWriter, CatchResponseError, Client, CsvRequestLogger. Observed top-lev… |
| pytest_locust package | library | Observed | Groups 1 file(s) under pytest_locust package (observed from repository paths and static analysis). Observed top-level classes: NoOpEvent. Observed top-level functions: fastsession, pytest_addoption, pytest_configure, se… |
| Tests | test | Observed | Groups 80 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Flask, Group. Observed routes: PATCH sys.stderr.write, PATCH locust.runners.HEARTBEAT_INTERVAL,… |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yaml` (config)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/launch_locust.json` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `Dockerfile.ci` (container)
- `Dockerfile.otel` (container)
- `_typos.toml` (config)
- `examples/azure/grpc.yaml` (config)
- `examples/azure/postgres.yaml` (config)
- `examples/azure/requirements.txt` (manifest)
- `examples/docker-compose/docker-compose.yml` (container)
- `locust/webui/.yarnrc.yml` (config)
- `locust/webui/package.json` (manifest)
- `locust/webui/tsconfig.json` (config)
- `package.json` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `locust` — 253 analysed file(s)
- `examples` — 84 analysed file(s)
- `docs` — 36 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `.github` — 7 analysed file(s)
- `.vscode` — 4 analysed file(s)
- `benchmarks` — 1 analysed file(s)
- `pytest_locust` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3debc468b53f10d00cb7b449c8f6086f2e5c5be1` is the revision these paths and observations refer to.
