# Project structure: openspug/spug

**Analysed commit:** `90ecc4c74ca72f8c62a80656f3c088af80b90ef7`

**Commit reference:** [90ecc4c74ca72f8c62a80656f3c088af80b90ef7](https://github.com/openspug/spug/commit/90ecc4c74ca72f8c62a80656f3c088af80b90ef7)

**Tree at this commit:** [openspug/spug@90ecc4c74ca7](https://github.com/openspug/spug/tree/90ecc4c74ca72f8c62a80656f3c088af80b90ef7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openspug/spug |
| Description | Spug is a lightweight agent-free automatic operation and maintenance platform designed for small and medium-sized enterprises. It integrates host management, host batch execution, host online terminal, file management, application release and deployment, pipelines, online task planning, configurati… |
| Stars | 11111 |
| Forks | 2197 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | 4.0 |
| Analysed commit | `90ecc4c74ca72f8c62a80656f3c088af80b90ef7` |
| Retrieved at | 2026-11-14T19:12:25.690065+00:00 |
| Files in this snapshot | 484 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (1 files)
    bug-report.md
  workflows/  (2 files)
    docker-image.yml
    github_to_gitee.yml
  FUNDING.yml
docker/  (2 files)
  entrypoint.sh
  init_spug
docs/  (11 files)
  docker/  (8 files)
    Dockerfile
    docker-compose.yml
    entrypoint.sh
    init_spug
    nginx.conf
    redis.conf
    spug.ini
    ssh_config
  FQA.md
  i18n.md
  install.sh
spug_api/  (149 files)
  apps/  (107 files)
    account/  (10 files)
      … 10 files under this directory
    alarm/  (4 files)
      … 4 files under this directory
    apis/  (8 files)
      … 8 files under this directory
    app/  (5 files)
      … 5 files under this directory
    config/  (5 files)
      … 5 files under this directory
    credential/  (4 files)
      … 4 files under this directory
    deploy/  (8 files)
      … 8 files under this directory
    exec/  (7 files)
      … 7 files under this directory
    file/  (4 files)
      … 4 files under this directory
    home/  (6 files)
      … 6 files under this directory
    host/  (8 files)
      … 8 files under this directory
    monitor/  (8 files)
      … 8 files under this directory
    notify/  (4 files)
      … 4 files under this directory
    pipeline/  (6 files)
      … 6 files under this directory
    repository/  (5 files)
      … 5 files under this directory
    schedule/  (9 files)
      … 9 files under this directory
    setting/  (6 files)
      … 6 files under this directory
  consumer/  (5 files)
    __init__.py
    consumers.py
    routing.py
    tests.py
    utils.py
  libs/  (18 files)
    __init__.py
    channel.py
    decorators.py
    executor.py
    gitlib.py
    helper.py
    ldap.py
    locale.py
    mail.py
    middleware.py
    mixins.py
    parser.py
    push.py
    spug.py
    ssh.py
    utils.py
    validators.py
    webhook.py
  logs/  (1 files)
    .gitkeep
  repos/  (1 files)
    .gitkeep
  spug/  (5 files)
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
  storage/  (2 files)
    deploy/  (1 files)
      … 1 files under this directory
    transfer/  (1 files)
      … 1 files under this directory
  tools/  (7 files)
    migrate.py
    start-api.sh
    start-monitor.sh
    start-scheduler.sh
    start-worker.sh
    start-ws.sh
    supervisor-spug.ini
  .gitignore
  manage.py
  requirements.txt
spug_web/  (275 files)
  public/  (3 files)
    index.html
    manifest.json
    robots.txt
  src/  (267 files)
    components/  (17 files)
      … 17 files under this directory
    layout/  (6 files)
      … 6 files under this directory
    libs/  (8 files)
      … 8 files under this directory
    locales/  (16 files)
      … 16 files under this directory
    pages/  (213 files)
      … 213 files under this directory
    App.js
    gStore.js
    index.js
    index.less
    routes.js
    serviceWorker.js
    setupProxy.js
  .gitignore
  README.md
  config-overrides.js
  jsconfig.json
  package.json
spug_web2/  (34 files)
  public/  (1 files)
    vite.svg
  src/  (27 files)
    components/  (6 files)
      … 6 files under this directory
    layout/  (3 files)
      … 3 files under this directory
    libs/  (4 files)
      … 4 files under this directory
    pages/  (8 files)
      … 8 files under this directory
    App.jsx
    error-page.jsx
    i18n.js
    index.css
    main.jsx
    routes.jsx
  .eslintrc.cjs
  .gitignore
  README.md
  index.html
  package.json
  vite.config.js
.dockerignore
.gitignore
Dockerfile
LICENSE
README-zh_CN.md
README.md
SECURITY-zh_CN.md
SECURITY.md
docker-compose.yml
```

## Entry points

- [spug_api/manage.py:23](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_api/manage.py#L23)
- [spug_api/tools/migrate.py:36](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_api/tools/migrate.py#L36)
- [spug_web/src/App.js](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_web/src/App.js)
- [spug_web/src/components/index.js](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_web/src/components/index.js)
- [spug_web/src/index.js](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_web/src/index.js)
- [spug_web/src/layout/index.js](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_web/src/layout/index.js)
- [spug_web/src/libs/index.js](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_web/src/libs/index.js)
- [spug_web2/src/App.jsx](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_web2/src/App.jsx)
- [spug_web2/src/components/index.js](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_web2/src/components/index.js)
- [spug_web2/src/layout/index.jsx](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_web2/src/layout/index.jsx)
- [spug_web2/src/libs/app.js](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_web2/src/libs/app.js)
- [spug_web2/src/libs/index.js](https://github.com/openspug/spug/blob/90ecc4c74ca72f8c62a80656f3c088af80b90ef7/spug_web2/src/libs/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 35 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigView, EnvironmentView, HistoryView, ServiceView. Observed top-level functions:… |
| Data layer | data | Observed | Groups 25 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Alarm, App, Config, ConfigHistory, Contact, Credential. Observed top-level functions: _build, dispatch… |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Version. Observed top-level functions: main. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| spug_api package | library | Observed | Groups 113 file(s) under spug_api package (observed from repository paths and static analysis). Observed top-level classes: AdminView, AlarmView, AppSetting, AppView, Argument, AttrDict. Observed top-level functions: _d… |
| spug_web package | library | Observed | Groups 206 file(s) under spug_web package (observed from repository paths and static analysis). |
| spug_web2 package | library | Observed | Groups 22 file(s) under spug_web2 package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/workflows/docker-image.yml` (ci)
- `.github/workflows/github_to_gitee.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `docs/docker/Dockerfile` (container)
- `docs/docker/docker-compose.yml` (container)
- `docs/docker/spug.ini` (config)
- `spug_api/requirements.txt` (manifest)
- `spug_api/tools/supervisor-spug.ini` (config)
- `spug_web/jsconfig.json` (config)
- `spug_web/package.json` (manifest)
- `spug_web/public/manifest.json` (config)
- `spug_web2/package.json` (manifest)

## Top-level layout

- `spug_web` — 275 analysed file(s)
- `spug_api` — 149 analysed file(s)
- `spug_web2` — 34 analysed file(s)
- `docs` — 11 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 4 analysed file(s)
- `docker` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `90ecc4c74ca72f8c62a80656f3c088af80b90ef7` is the revision these paths and observations refer to.
