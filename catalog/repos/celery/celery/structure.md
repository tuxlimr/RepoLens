# Project structure: celery/celery

**Analysed commit:** `9c2f238334331db43f15956f131235fd3bb70fd1`

**Commit reference:** [9c2f238334331db43f15956f131235fd3bb70fd1](https://github.com/celery/celery/commit/9c2f238334331db43f15956f131235fd3bb70fd1)

**Tree at this commit:** [celery/celery@9c2f23833433](https://github.com/celery/celery/tree/9c2f238334331db43f15956f131235fd3bb70fd1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | celery/celery |
| Description | Distributed Task Queue (development branch) |
| Stars | 29194 |
| Forks | 5263 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `9c2f238334331db43f15956f131235fd3bb70fd1` |
| Retrieved at | 2026-11-14T19:07:14.384650+00:00 |
| Files in this snapshot | 797 |

## Directory tree

```text
.github/  (23 files)
  ISSUE_TEMPLATE/  (8 files)
    Bug-Report.md
    Documentation-Bug-Report.md
    Enhancement.md
    Feature-Request.md
    Major-Version-Release-Checklist.md
    Minor-Version-Release-Checklist.md
    Patch-Version-Release-Checklist.md
    config.yml
  workflows/  (8 files)
    codeql-analysis.yml
    docker.yml
    integration-tests.yml
    linter.yml
    python-package.yml
    semgrep.yml
    smoke-tests-dev.yml
    smoke-tests.yml
  Agents.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  copilot-instructions.md
  dependabot.yml
  opencollective.yml
celery/  (163 files)
  app/  (16 files)
    __init__.py
    amqp.py
    annotations.py
    autoretry.py
    backends.py
    base.py
    builtins.py
    control.py
    defaults.py
    events.py
    log.py
    registry.py
    routes.py
    task.py
    trace.py
    utils.py
  apps/  (4 files)
    __init__.py
    beat.py
    multi.py
    worker.py
  backends/  (22 files)
    database/  (3 files)
      … 3 files under this directory
    __init__.py
    arangodb.py
    asynchronous.py
    azureblockblob.py
    base.py
    cache.py
    cassandra.py
    consul.py
    cosmosdbsql.py
    couchbase.py
    couchdb.py
    dynamodb.py
    elasticsearch.py
    filesystem.py
    gcs.py
    mongodb.py
    redis.py
    rpc.py
    s3.py
  bin/  (18 files)
    __init__.py
    amqp.py
    base.py
    beat.py
    call.py
    celery.py
    control.py
    events.py
    graph.py
    list.py
    logtool.py
    migrate.py
    multi.py
    purge.py
    result.py
    shell.py
    upgrade.py
    worker.py
  concurrency/  (8 files)
    __init__.py
    asynpool.py
    base.py
    eventlet.py
    gevent.py
    prefork.py
    solo.py
    thread.py
  contrib/  (14 files)
    django/  (2 files)
      … 2 files under this directory
    testing/  (6 files)
      … 6 files under this directory
    __init__.py
    abortable.py
    migrate.py
    pytest.py
    rdb.py
    sphinx.py
  events/  (8 files)
    __init__.py
    cursesmon.py
    dispatcher.py
    dumper.py
    event.py
    receiver.py
    snapshot.py
    state.py
  fixups/  (2 files)
    __init__.py
    django.py
  loaders/  (4 files)
    __init__.py
    app.py
    base.py
    default.py
  security/  (5 files)
    __init__.py
    certificate.py
    key.py
    serialization.py
    utils.py
  utils/  (27 files)
    dispatch/  (4 files)
      … 4 files under this directory
    static/  (1 files)
      … 1 files under this directory
    __init__.py
    abstract.py
    annotations.py
    collections.py
    debug.py
    deprecated.py
    functional.py
    graph.py
    imports.py
    iso8601.py
    log.py
    nodenames.py
    objects.py
    quorum_queues.py
    saferepr.py
    serialization.py
    sysinfo.py
    term.py
    text.py
    threads.py
    time.py
    timer2.py
  worker/  (22 files)
    consumer/  (11 files)
      … 11 files under this directory
    __init__.py
    autoscale.py
    components.py
    control.py
    heartbeat.py
    loops.py
    pidbox.py
    request.py
    state.py
    strategy.py
    worker.py
  __init__.py
  __main__.py
  _state.py
  beat.py
  bootsteps.py
  canvas.py
  exceptions.py
  local.py
  platforms.py
  result.py
  schedules.py
  signals.py
  states.py
docker/  (7 files)
  docs/  (2 files)
    Dockerfile
    start
  scripts/  (2 files)
    create-linux-user.sh
    install-couchbase.sh
  Dockerfile
  docker-compose.yml
  entrypoint
docs/  (257 files)
  _ext/  (1 files)
    celerydocs.py
  _static/  (1 files)
    .keep
  _templates/  (1 files)
    sidebardonations.html
  django/  (2 files)
    first-steps-with-django.rst
    index.rst
  getting-started/  (12 files)
    backends-and-brokers/  (7 files)
      … 7 files under this directory
    first-steps-with-celery.rst
    index.rst
    introduction.rst
    next-steps.rst
    resources.rst
  history/  (37 files)
    changelog-1.0.rst
    changelog-2.0.rst
    changelog-2.1.rst
    changelog-2.2.rst
    changelog-2.3.rst
    changelog-2.4.rst
    changelog-2.5.rst
    changelog-3.0.rst
    changelog-3.1.rst
    changelog-4.0.rst
    changelog-4.1.rst
    changelog-4.2.rst
    changelog-4.3.rst
    changelog-4.4.rst
    changelog-5.0.rst
    changelog-5.1.rst
    changelog-5.3.rst
    changelog-5.4.rst
    changelog-5.5.rst
    changelog-5.6.rst
    changelog-5.7.rst
    index.rst
    whatsnew-2.5.rst
    whatsnew-3.0.rst
    … 13 more files
  images/  (3 files)
    blacksmith-logo-white-on-black.svg
    cloudamqp-logo-lightbg.svg
    dragonfly.svg
  includes/  (3 files)
    installation.txt
    introduction.txt
    resources.txt
  internals/  (75 files)
    reference/  (69 files)
      … 69 files under this directory
    app-overview.rst
    deprecation.rst
    guide.rst
    index.rst
    protocol.rst
    worker.rst
  reference/  (78 files)
    celery.app.amqp.rst
    celery.app.autoretry.rst
    celery.app.backends.rst
    celery.app.builtins.rst
    celery.app.control.rst
    celery.app.defaults.rst
    celery.app.events.rst
    celery.app.log.rst
    celery.app.registry.rst
    celery.app.rst
    celery.app.task.rst
    celery.app.utils.rst
    celery.apps.beat.rst
    celery.apps.multi.rst
    celery.apps.worker.rst
    celery.beat.rst
    celery.bin.amqp.rst
    celery.bin.base.rst
    celery.bin.beat.rst
    celery.bin.call.rst
    celery.bin.celery.rst
    celery.bin.control.rst
    celery.bin.events.rst
    celery.bin.graph.rst
    … 54 more files
  sec/  (3 files)
    CELERYSA-0001.txt
    CELERYSA-0002.txt
    CELERYSA-0003.txt
  templates/  (1 files)
    readme.txt
  tutorials/  (4 files)
    daemonizing.html
    debugging.html
    index.rst
    task-cookbook.rst
  userguide/  (21 files)
    concurrency/  (3 files)
      … 3 files under this directory
    application.rst
    calling.rst
    canvas.rst
    configuration.rst
    daemonizing.rst
    debugging.rst
    extending.rst
    index.rst
    monitoring.rst
    optimizing.rst
    periodic-tasks.rst
    routing.rst
    security.rst
    signals.rst
    sphinx.rst
    tasks.rst
    testing.rst
    workers.rst
  AUTHORS.txt
  Makefile
  THANKS
  changelog.rst
  changelog_formatter.py
  community.rst
  conf.py
  configuration.html
  contributing.rst
  copyright.rst
  faq.rst
  glossary.rst
  index.rst
  make.bat
  spelling_wordlist.txt
examples/  (50 files)
  app/  (1 files)
    myapp.py
  celery_http_gateway/  (6 files)
    README.rst
    __init__.py
    manage.py
    settings.py
    tasks.py
    urls.py
  django/  (14 files)
    demoapp/  (6 files)
      … 6 files under this directory
    proj/  (5 files)
      … 5 files under this directory
    README.rst
    manage.py
    requirements.txt
  eventlet/  (5 files)
    README.rst
    bulk_task_producer.py
    celeryconfig.py
    tasks.py
    webcrawler.py
  gevent/  (3 files)
    README.rst
    celeryconfig.py
    tasks.py
  next-steps/  (4 files)
    proj/  (3 files)
      … 3 files under this directory
    setup.py
  periodic-tasks/  (1 files)
    myapp.py
  pydantic/  (2 files)
    __init__.py
    tasks.py
  quorum-queues/  (4 files)
    declare_queue.py
    myapp.py
    setup_cluster.sh
    test_cluster.sh
  resultgraph/  (1 files)
    tasks.py
  security/  (1 files)
    mysecureapp.py
  stamping/  (6 files)
    config.py
    examples.py
    myapp.py
    revoke_example.py
    tasks.py
    visitors.py
  tutorial/  (1 files)
    tasks.py
  README.rst
extra/  (21 files)
  WindowsCMD-AzureWebJob/  (4 files)
    Celery/  (2 files)
      … 2 files under this directory
    CeleryBeat/  (2 files)
      … 2 files under this directory
  bash-completion/  (1 files)
    celery.bash
  generic-init.d/  (2 files)
    celerybeat
    celeryd
  macOS/  (2 files)
    org.celeryq.beat.plist
    org.celeryq.worker.plist
  release/  (3 files)
    attribution.py
    gen-cert.sh
    sphinx2rst_config.py
  supervisord/  (4 files)
    celery.sh
    celerybeat.conf
    celeryd.conf
    supervisord.conf
  systemd/  (4 files)
    celery.conf
    celery.service
    celery.tmpfiles
    celerybeat.service
  zsh-completion/  (1 files)
    celery.zsh
helm-chart/  (8 files)
  templates/  (4 files)
    _helpers.tpl
    configmap.yaml
    deployment.yaml
    serviceaccount.yaml
  .helmignore
  Chart.yaml
  README.rst
  values.yaml
requirements/  (50 files)
  deps/  (1 files)
    mock.txt
  extras/  (37 files)
    arangodb.txt
    auth.txt
    azureblockblob.txt
    brotli.txt
    cassandra.txt
    consul.txt
    cosmosdbsql.txt
    couchbase.txt
    couchdb.txt
    django.txt
    dynamodb.txt
    elasticsearch.txt
    eventlet.txt
    gcpubsub.txt
    gcs.txt
    gevent.txt
    librabbitmq.txt
    memcache.txt
    mongodb.txt
    msgpack.txt
    pydantic.txt
    pymemcache.txt
    pyro.txt
    pytest.txt
    … 13 more files
  README.rst
  constraints.txt
  default.txt
  dev.txt
  docs.txt
  pkgutils.txt
  security.txt
  test-ci-base.txt
  test-ci-default.txt
  test-integration.txt
  test-pypy3.txt
  test.txt
t/  (199 files)
  benchmarks/  (1 files)
    bench_worker.py
  integration/  (26 files)
    __init__.py
    conftest.py
    django_settings.py
    serialization_config.py
    tasks.py
    test_backend.py
    test_backend_leak_in_fixture_teardown.py
    test_beat.py
    test_cache_backend.py
    test_canvas.py
    test_connection_recovery.py
    test_database_backend.py
    test_events_state_memory_leak.py
    test_group_chains.py
    test_inspect.py
    test_loader.py
    test_logfile_format.py
    test_mem_leak_in_exception_handling.py
    test_redis_backend.py
    test_request_backend_down.py
    test_security.py
    test_serialization.py
    test_tasks.py
    test_upgrade.py
    … 2 more files
  smoke/  (67 files)
    operations/  (4 files)
      … 4 files under this directory
    tests/  (50 files)
      … 50 files under this directory
    workers/  (8 files)
      … 8 files under this directory
    __init__.py
    conftest.py
    redis.conf
    signals.py
    tasks.py
  unit/  (102 files)
    app/  (20 files)
      … 20 files under this directory
    apps/  (4 files)
      … 4 files under this directory
    backends/  (20 files)
      … 20 files under this directory
    bin/  (16 files)
      … 16 files under this directory
    concurrency/  (8 files)
      … 8 files under this directory
    contrib/  (15 files)
      … 15 files under this directory
    events/  (6 files)
      … 6 files under this directory
    fixups/  (2 files)
      … 2 files under this directory
    security/  (6 files)
      … 6 files under this directory
    tasks/  (3 files)
      … 3 files under this directory
    __init__.py
    conftest.py
  __init__.py
  canvas_helpers.py
  skip.py
.bumpversion.cfg
.dockerignore
.editorconfig
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
CONTRIBUTING.rst
CONTRIBUTORS.txt
Changelog.rst
LICENSE
MANIFEST.in
Makefile
README.rst
SECURITY.md
TODO
bandit.json
pyproject.toml
setup.cfg
setup.py
```

## Entry points

- [celery/__main__.py](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/__main__.py)
- [celery/bin/amqp.py:64](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/amqp.py#L64)
- [celery/bin/beat.py:62](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/beat.py#L62)
- [celery/bin/call.py:58](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/call.py#L58)
- [celery/bin/celery.py:113](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/celery.py#L113)
- [celery/bin/control.py:129](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/control.py#L129)
- [celery/bin/events.py:83](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/events.py#L83)
- [celery/bin/graph.py:14](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/graph.py#L14)
- [celery/bin/list.py:10](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/list.py#L10)
- [celery/bin/logtool.py:116](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/logtool.py#L116)
- [celery/bin/migrate.py:48](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/migrate.py#L48)
- [celery/bin/multi.py:472](https://github.com/celery/celery/blob/9c2f238334331db43f15956f131235fd3bb70fd1/celery/bin/multi.py#L472)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| celery package | library | Observed | Groups 153 file(s) under celery package (observed from repository paths and static analysis). Observed top-level classes: AMQP, AMQPContext, AbortableAsyncResult, AbortableTask, Agent, AlreadyRegistered. Observed top-le… |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: _add_default, _add_doc, _pip_requirement, _reqs, _strip_comments, extras. |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DatabaseBackend, SessionManager, Task, TaskExtended, TaskSet. Observed top-level functions: _after_fork… |
| docker package | library | Observed | Groups 2 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Celery. Observed top-level classes: AppLoader, ConnMock, CursesMonitor, Displ… |
| External integrations | external | Observed | Groups 5 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AddParameterModel, AddResultModel, ClassBasedAutoRetryTask, ExpectedException, UnpickleableE… |
| extra package | library | Observed | Groups 3 file(s) under extra package (observed from repository paths and static analysis). |
| t package | library | Observed | Groups 34 file(s) under t package (observed from repository paths and static analysis). Observed top-level classes: AltSmokeWorkerContainer, CeleryLatestWorkerContainer, OtherSmokeWorkerContainer, SecurityCase, SmokeWor… |
| Tests | test | Observed | Groups 148 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Celery. Observed routes: PATCH celery.app.base.set_default_app, PATCH celery.security.setup_se… |

## Important files

- `.bumpversion.cfg` (config)
- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/opencollective.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/integration-tests.yml` (ci)
- `.github/workflows/linter.yml` (ci)
- `.github/workflows/python-package.yml` (ci)
- `.github/workflows/semgrep.yml` (ci)
- `.github/workflows/smoke-tests-dev.yml` (ci)
- `.github/workflows/smoke-tests.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `bandit.json` (config)
- `docker/Dockerfile` (container)
- `docker/docker-compose.yml` (container)
- `docker/docs/Dockerfile` (container)
- `examples/django/requirements.txt` (manifest)
- `examples/next-steps/setup.py` (manifest)
- `helm-chart/Chart.yaml` (config)
- `helm-chart/templates/configmap.yaml` (config)
- `helm-chart/templates/deployment.yaml` (config)
- `helm-chart/templates/serviceaccount.yaml` (config)
- `helm-chart/values.yaml` (config)
- `pyproject.toml` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `docs` — 257 analysed file(s)
- `t` — 199 analysed file(s)
- `celery` — 163 analysed file(s)
- `examples` — 50 analysed file(s)
- `requirements` — 50 analysed file(s)
- `.github` — 23 analysed file(s)
- `extra` — 21 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `helm-chart` — 8 analysed file(s)
- `docker` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9c2f238334331db43f15956f131235fd3bb70fd1` is the revision these paths and observations refer to.
