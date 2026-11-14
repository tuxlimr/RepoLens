# Project structure: whyour/qinglong

**Analysed commit:** `2ddb592800fd0d30734ac3e20cfa35be16a85f39`

**Commit reference:** [2ddb592800fd0d30734ac3e20cfa35be16a85f39](https://github.com/whyour/qinglong/commit/2ddb592800fd0d30734ac3e20cfa35be16a85f39)

**Tree at this commit:** [whyour/qinglong@2ddb592800fd](https://github.com/whyour/qinglong/tree/2ddb592800fd0d30734ac3e20cfa35be16a85f39)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | whyour/qinglong |
| Description | 支持 Python3、JavaScript、Shell、Typescript 的定时任务管理平台（Timed task management platform supporting Python3, JavaScript, Shell, Typescript） |
| Stars | 20100 |
| Forks | 3230 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `2ddb592800fd0d30734ac3e20cfa35be16a85f39` |
| Retrieved at | 2026-11-14T19:11:16.845626+00:00 |
| Files in this snapshot | 667 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  agents/  (1 files)
    ql.agent.md
  workflows/  (4 files)
    build-docker-image.yml
    cli-package.yml
    release-readiness.yml
    validate.yml
  PULL_REQUEST_TEMPLATE.md
  config.yml
back/  (132 files)
  api/  (16 files)
    clientIp.ts
    config.ts
    cron.ts
    dashboard.ts
    dependence.ts
    env.ts
    health.ts
    index.ts
    log.ts
    open.ts
    retention.ts
    script.ts
    subscription.ts
    system.ts
    update.ts
    user.ts
  bootstrap/  (2 files)
    database.ts
    upgradeProbe.ts
  config/  (9 files)
    const.ts
    container.ts
    grpcCerts.ts
    http.ts
    index.ts
    serverEnv.ts
    share.ts
    subscription.ts
    util.ts
  data/  (12 files)
    cron.ts
    cronStats.ts
    cronView.ts
    dependence.ts
    env.ts
    index.ts
    notify.ts
    open.ts
    runningInstance.ts
    sock.ts
    subscription.ts
    system.ts
  interface/  (1 files)
    schedule.ts
  loaders/  (13 files)
    app.ts
    bootAfter.ts
    db.ts
    depInjector.ts
    deps.ts
    express.ts
    httpApplication.ts
    initData.ts
    initFile.ts
    initTask.ts
    logger.ts
    server.ts
    sock.ts
  middlewares/  (4 files)
    monitoring.ts
    protectedPathCase.ts
    uniqueConstraintError.ts
    validationErrors.ts
  protos/  (6 files)
    api.proto
    api.ts
    cron.proto
    cron.ts
    health.proto
    health.ts
  schedule/  (7 files)
    addCron.ts
    api.ts
    client.ts
    data.ts
    delCron.ts
    health.ts
    setConcurrency.ts
  services/  (21 files)
    config.ts
    cron.ts
    cronView.ts
    dependence.ts
    env.ts
    grpc.ts
    health.ts
    http.ts
    log.ts
    metrics.ts
    notify.ts
    open.ts
    retention.ts
    schedule.ts
    script.ts
    scriptHistory.ts
    sock.ts
    sshKey.ts
    subscription.ts
    system.ts
    user.ts
  shared/  (36 files)
    auth.ts
    authMutation.ts
    childProcess.ts
    clientIp.ts
    cronCommand.ts
    cronSchedule.ts
    cronScheduler.ts
    errors.ts
    fileAccess.ts
    i18n.ts
    interface.ts
    languageSync.ts
    linuxMirror.ts
    logPath.ts
    logReader.ts
    logStreamManager.ts
    loginThrottle.ts
    notificationAudit.ts
    pLimit.ts
    password.ts
    retention.ts
    runCron.ts
    runtimeBuild.ts
    schedulerMutationLock.ts
    … 12 more files
  types/  (1 files)
    express.d.ts
  validation/  (1 files)
    schedule.ts
  app.ts
  token.ts
  tsconfig.json
cli/  (187 files)
  scripts/  (4 files)
    build.cjs
    entrypoints.cjs
    test.cjs
    verify-package.cjs
  skills/  (6 files)
    qinglong-cli/  (3 files)
      … 3 files under this directory
    qinglong-local/  (3 files)
      … 3 files under this directory
  src/  (78 files)
    compatibility/  (3 files)
      … 3 files under this directory
    entrypoints/  (6 files)
      … 6 files under this directory
    internal/  (44 files)
      … 44 files under this directory
    remote/  (13 files)
      … 13 files under this directory
    shared/  (12 files)
      … 12 files under this directory
  test/  (91 files)
    compatibility/  (2 files)
      … 2 files under this directory
    fixtures/  (1 files)
      … 1 files under this directory
    helpers/  (1 files)
      … 1 files under this directory
    integration/  (8 files)
      … 8 files under this directory
    internal/  (35 files)
      … 35 files under this directory
    linux/  (31 files)
      … 31 files under this directory
    remote/  (9 files)
      … 9 files under this directory
    shared/  (4 files)
      … 4 files under this directory
  .gitignore
  LICENSE
  LOCAL.en.md
  LOCAL.md
  README.en.md
  README.md
  package.json
  tsconfig.json
deploy/  (4 files)
  kubernetes/  (4 files)
    base/  (2 files)
      … 2 files under this directory
    overlays/  (1 files)
      … 1 files under this directory
    README.md
docker/  (10 files)
  Dockerfile
  Dockerfile.310
  Dockerfile.debian
  Dockerfile.debian310
  Dockerfile.upgrade-bundle
  build-manifest.cjs
  docker-compose.yml
  docker-entrypoint.sh
  install-node-debian.sh
  verify-build.cjs
docs/  (13 files)
  development/  (5 files)
    node-cron-migration.md
    notification-audit.md
    platform-upgrade-bundles.md
    python-dependency-sources.md
    task-startup.md
  releases/  (6 files)
    2.22.0-validation.md
    2.22.0.md
    2.23.0.md
    2.24.0-dev.0.md
    2.24.0.md
    2.25.0-rc.0.md
  PROJECT_ARCHITECTURE.md
  script-history.md
sample/  (9 files)
  auth.sample.json
  config.sample.sh
  extra.sample.sh
  notify.js
  notify.py
  ql_sample.js
  ql_sample.py
  task.sample.sh
  tool.ts
scripts/  (13 files)
  benchmark-execution.cjs
  benchmark-script-history.cjs
  build-bundle-installer.cjs
  build-upgrade-bundle.cjs
  prepare-npm-package.cjs
  publish-static.sh
  publish-upgrade-bundles.cjs
  publish-upgrade-info.cjs
  sync-static.sh
  verify-image-node-layers.py
  verify-panel-package.cjs
  wait-for-mirror.sh
  write-build-info.cjs
shell/  (26 files)
  lang/  (2 files)
    en.sh
    zh.sh
  preload/  (6 files)
    client.js
    client.py
    esm-loader.mjs
    notificationAudit.js
    sitecustomize.js
    sitecustomize.py
  api.sh
  bot.sh
  check.sh
  env.sh
  install-bundle.cjs
  install-package.cjs
  node-runtime-probe.cjs
  node_path_cache.sh
  otask.sh
  pub.sh
  rmlog.sh
  share.sh
  start-simplify.sh
  start.sh
  task-timeout.sh
  task.sh
  update.sh
  upgrade.cjs
src/  (96 files)
  components/  (7 files)
    UpgradeNotice.tsx
    copy.tsx
    iconfont.tsx
    index.less
    name.tsx
    tag.tsx
    terminal.tsx
  hooks/  (4 files)
    useFilterTreeData.ts
    useScrollHeight.ts
    useTableScrollHeight.ts
    useUpgrade.ts
  layouts/  (3 files)
    defaultProps.tsx
    index.less
    index.tsx
  locales/  (2 files)
    en-US.json
    zh-CN.json
  pages/  (63 files)
    config/  (2 files)
      … 2 files under this directory
    crontab/  (9 files)
      … 9 files under this directory
    dashboard/  (2 files)
      … 2 files under this directory
    dependence/  (5 files)
      … 5 files under this directory
    diff/  (2 files)
      … 2 files under this directory
    env/  (4 files)
      … 4 files under this directory
    error/  (2 files)
      … 2 files under this directory
    initialization/  (2 files)
      … 2 files under this directory
    log/  (2 files)
      … 2 files under this directory
    login/  (2 files)
      … 2 files under this directory
    script/  (12 files)
      … 12 files under this directory
    setting/  (14 files)
      … 14 files under this directory
    subscription/  (4 files)
      … 4 files under this directory
    404.tsx
  styles/  (1 files)
    variable.less
  utils/  (14 files)
    codemirror/  (2 files)
      … 2 files under this directory
    monaco/  (1 files)
      … 1 files under this directory
    config.ts
    const.ts
    date.ts
    hooks.ts
    http.tsx
    httpError.ts
    index.ts
    init.ts
    navigationTiming.ts
    type.ts
    websocket.ts
  app.ts
  loading.tsx
test/  (147 files)
  back/  (130 files)
    advisory-input-security.test.cjs
    api-fallback.test.cjs
    app-scope-security.test.cjs
    armv6-worker-readiness.test.cjs
    auth-security.test.cjs
    build-provenance.test.cjs
    code-scanning-security.test.cjs
    cron-calendar-boundaries.test.cjs
    cron-log-name.test.cjs
    cron-macros.test.cjs
    cron-parser-compatibility.test.cjs
    cron-schedule-compatibility.test.cjs
    cron-scheduler-routing.test.cjs
    cron-validation.test.cjs
    dashboard-failures.test.cjs
    database-bootstrap.test.cjs
    dependence-cache-status.test.cjs
    dependence-refresh-api.test.cjs
    deprecated-file-routes.test.cjs
    dev-e2e-regressions.test.cjs
    draft-path-security.test.cjs
    dynamic-locales.test.cjs
    ecosystem.test.cjs
    env-import-security.test.cjs
    … 106 more files
  fixtures/  (2 files)
    cron-calendar-boundaries.json
    legacy-cron.json
  front/  (12 files)
    codemirror-language.test.cjs
    cron-log-pagination.test.cjs
    dependence-refresh.test.cjs
    diff-file-routing.test.cjs
    editor-locale.test.cjs
    http-auth.test.cjs
    http-error.test.cjs
    navigation-timing.test.cjs
    notify-log-locales.test.cjs
    responsive-layout.test.cjs
    script-history-save.test.cjs
    update-progress.test.cjs
  helpers/  (3 files)
    load-security-module.cjs
    manual-upgrade-fixture.cjs
    upgrade-fixture.cjs
.dockerignore
.editorconfig
.env.example
.gitignore
.nvmrc
.prettierignore
.prettierrc
.umirc.ts
AGENTS.md
LICENSE
README-NODE.md
README-en.md
README.md
SECURITY.md
ecosystem.config.js
nodemon.json
package.json
tsconfig.json
typings.d.ts
version.yaml
```

## Entry points

- [sample/notify.py:1437](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/sample/notify.py#L1437)
- [shell/update.sh](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/shell/update.sh)
- [shell/task.sh](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/shell/task.sh)
- [shell/start.sh](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/shell/start.sh)
- [back/api/index.ts](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/back/api/index.ts)
- [back/app.ts](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/back/app.ts)
- [back/config/index.ts](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/back/config/index.ts)
- [back/data/index.ts](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/back/data/index.ts)
- [back/loaders/app.ts](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/back/loaders/app.ts)
- [back/loaders/server.ts](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/back/loaders/server.ts)
- [cli/src/compatibility/main.ts](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/cli/src/compatibility/main.ts)
- [cli/src/entrypoints/index.ts](https://github.com/whyour/qinglong/blob/2ddb592800fd0d30734ac3e20cfa35be16a85f39/cli/src/entrypoints/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 19 file(s) under api layer (observed from repository paths and static analysis). |
| app.ts package | library | Observed | Groups 1 file(s) under app.ts package (observed from repository paths and static analysis). |
| back package | library | Observed | Groups 70 file(s) under back package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 77 file(s) under cli package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 6 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 33 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 4 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: WeCom. Observed top-level functions: add_notify_function, aibotk, audited_notification, ba… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Client, CreateCronParams, CreateEnvParams, CronDetailParams, CronItem, CronResponse. Observe… |
| hooks package | library | Observed | Groups 4 file(s) under hooks package (observed from repository paths and static analysis). |
| layouts package | library | Observed | Groups 2 file(s) under layouts package (observed from repository paths and static analysis). |
| loading.tsx package | library | Observed | Groups 1 file(s) under loading.tsx package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 48 file(s) under pages package (observed from repository paths and static analysis). |
| sample package | library | Observed | Groups 7 file(s) under sample package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 13 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 21 file(s) under service / domain layer (observed from repository paths and static analysis). |
| shell package | library | Observed | Groups 25 file(s) under shell package (observed from repository paths and static analysis). Observed top-level functions: expand_range, handle_sigterm, run, try_parse_int. |
| Tests | test | Observed | Groups 234 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 14 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/config.yml` (config)
- `.github/workflows/build-docker-image.yml` (ci)
- `.github/workflows/cli-package.yml` (ci)
- `.github/workflows/release-readiness.yml` (ci)
- `.github/workflows/validate.yml` (ci)
- `back/tsconfig.json` (config)
- `cli/package.json` (manifest)
- `cli/test/linux/Dockerfile` (container)
- `cli/test/linux/Dockerfile.alpine` (container)
- `cli/test/linux/Dockerfile.services` (container)
- `cli/test/linux/Dockerfile.ssh` (container)
- `cli/tsconfig.json` (config)
- `deploy/kubernetes/base/kustomization.yaml` (config)
- `deploy/kubernetes/base/qinglong.yaml` (config)
- `deploy/kubernetes/overlays/example/kustomization.yaml` (config)
- `docker/Dockerfile` (container)
- `docker/Dockerfile.310` (container)
- `docker/Dockerfile.debian` (container)
- `docker/Dockerfile.debian310` (container)
- `docker/Dockerfile.upgrade-bundle` (container)
- `docker/docker-compose.yml` (container)
- `nodemon.json` (config)
- `package.json` (manifest)
- `sample/auth.sample.json` (config)
- `src/locales/en-US.json` (config)
- `src/locales/zh-CN.json` (config)
- `tsconfig.json` (config)
- `version.yaml` (config)

## Top-level layout

- `cli` — 187 analysed file(s)
- `test` — 147 analysed file(s)
- `back` — 132 analysed file(s)
- `src` — 96 analysed file(s)
- `shell` — 26 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `docs` — 13 analysed file(s)
- `scripts` — 13 analysed file(s)
- `.github` — 10 analysed file(s)
- `docker` — 10 analysed file(s)
- `sample` — 9 analysed file(s)
- `deploy` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2ddb592800fd0d30734ac3e20cfa35be16a85f39` is the revision these paths and observations refer to.
