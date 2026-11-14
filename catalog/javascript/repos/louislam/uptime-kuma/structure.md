# Project structure: louislam/uptime-kuma

**Analysed commit:** `7e5075d12c85f7282f9c7b7d6821d56aa3acc688`

**Commit reference:** [7e5075d12c85f7282f9c7b7d6821d56aa3acc688](https://github.com/louislam/uptime-kuma/commit/7e5075d12c85f7282f9c7b7d6821d56aa3acc688)

**Tree at this commit:** [louislam/uptime-kuma@7e5075d12c85](https://github.com/louislam/uptime-kuma/tree/7e5075d12c85f7282f9c7b7d6821d56aa3acc688)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | louislam/uptime-kuma |
| Description | A fancy self-hosted monitoring tool |
| Stars | 94164 |
| Forks | 8769 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `7e5075d12c85f7282f9c7b7d6821d56aa3acc688` |
| Retrieved at | 2026-11-14T19:10:33.417089+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (33 files)
  ISSUE_TEMPLATE/  (4 files)
    ask_for_help.yml
    bug_report.yml
    config.yml
    feature_request.yml
  actions/  (1 files)
    setup-atlascloud/  (1 files)
      … 1 files under this directory
  config/  (1 files)
    exclude.txt
  workflows/  (21 files)
    ai-slop.yml
    auto-test.yml
    autofix.yml
    build-docker-base.yml
    build-docker-pr-test.yml
    build-docker-push.yml
    close-incorrect-issue.yml
    codeql-analysis.yml
    conflict-labeler.yml
    deleted-pr.yml
    duplicate-issues.yml
    mark-as-draft-on-requesting-changes.yml
    new-contributor-pr.yml
    npm-update.yml
    pr-description-check.yml
    pr-title.yml
    prevent-file-change.yml
    release-nightly.yml
    release.yml
    stale-bot.yml
    validate.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  REVIEW_GUIDELINES.md
  copilot-instructions.md
  dependabot.yml
  opencode-models.json
db/  (122 files)
  knex_migrations/  (66 files)
    2023-08-16-0000-create-uptime.js
    2023-08-18-0301-heartbeat.js
    2023-09-29-0000-heartbeat-retires.js
    2023-10-08-0000-mqtt-query.js
    2023-10-11-1915-push-token-to-32.js
    2023-10-16-0000-create-remote-browsers.js
    2023-12-20-0000-alter-status-page.js
    2023-12-21-0000-stat-ping-min-max.js
    2023-12-22-0000-hourly-uptime.js
    2024-01-22-0000-stats-extras.js
    2024-04-26-0000-snmp-monitor.js
    2024-08-24-000-add-cache-bust.js
    2024-08-24-0000-conditions.js
    2024-10-1315-rabbitmq-monitor.js
    2024-10-31-0000-fix-snmp-monitor.js
    2024-11-27-1927-fix-info-json-data-type.js
    2025-01-01-0000-add-smtp.js
    2025-02-15-2312-add-wstest.js
    2025-02-17-2142-generalize-analytics.js
    2025-03-04-0000-ping-advanced-options.js
    2025-03-25-0127-fix-5721.js
    2025-05-09-0000-add-custom-url.js
    2025-06-03-0000-add-ip-family.js
    2025-06-11-0000-add-manual-monitor.js
    … 42 more files
  old_migrations/  (55 files)
    README.md
    patch-2fa-invalidate-used-token.sql
    patch-2fa.sql
    patch-add-certificate-expiry-status-page.sql
    patch-add-clickable-status-page-link.sql
    patch-add-description-monitor.sql
    patch-add-docker-columns.sql
    patch-add-gamedig-given-port.sql
    patch-add-gamedig-monitor.sql
    patch-add-google-analytics-status-page-tag.sql
    patch-add-invert-keyword.sql
    patch-add-other-auth.sql
    patch-add-parent-monitor.sql
    patch-add-radius-monitor.sql
    patch-add-retry-interval-monitor.sql
    patch-add-sqlserver-monitor.sql
    patch-add-timeout-monitor.sql
    patch-added-json-query.sql
    patch-added-kafka-producer.sql
    patch-added-mqtt-monitor.sql
    patch-api-key-table.sql
    patch-fix-kafka-producer-booleans.sql
    patch-group-table.sql
    patch-grpc-monitor.sql
    … 31 more files
  knex_init_db.js
docker/  (6 files)
  etc/  (2 files)
    nscd.conf
    sudoers
  builder-go.dockerfile
  debian-base.dockerfile
  docker-compose-dev.yml
  dockerfile
extra/  (66 files)
  docker-latest-warning/  (3 files)
    Dockerfile.latest-warning
    docker-latest-warning.js
    package.json
  kuma-pr/  (3 files)
    index.mjs
    package.json
    pr-lib.mjs
  push-examples/  (14 files)
    bash-curl/  (1 files)
      … 1 files under this directory
    csharp/  (1 files)
      … 1 files under this directory
    docker/  (1 files)
      … 1 files under this directory
    go/  (1 files)
      … 1 files under this directory
    java/  (1 files)
      … 1 files under this directory
    javascript-fetch/  (2 files)
      … 2 files under this directory
    php/  (1 files)
      … 1 files under this directory
    powershell/  (1 files)
      … 1 files under this directory
    python/  (1 files)
      … 1 files under this directory
    typescript-fetch/  (3 files)
      … 3 files under this directory
    .gitignore
  release/  (15 files)
    build-and-upload-assets.mjs
    build-images.mjs
    create-draft-release.mjs
    create-release.mjs
    generate-changelog.mjs
    install-deps.mjs
    lib.mjs
    merge-pr.mjs
    nightly.mjs
    prepare-release.mjs
    release.mjs
    update-version.mjs
    update-wiki.mjs
    upload-artifacts-beta.mjs
    upload-artifacts.mjs
  uptime-kuma-push/  (5 files)
    .gitignore
    Dockerfile
    build.js
    package.json
    uptime-kuma-push.go
  build-healthcheck.js
  check-knex-filenames.mjs
  check-lang-json.js
  check-package-json.mjs
  checkout-pr.mjs
  close-incorrect-issue.mjs
  compile-install-script.ps1
  coverage-report.mjs
  deploy-demo-server.js
  download-dist.js
  healthcheck.go
  mark-as-nightly.js
  precompile-server.js
  prepare-v1-test-db.mjs
  prepare-v2-test-db.mjs
  rdap-dns.json
  rebase-pr.js
  remove-2fa.js
  remove-empty-lang-keys.js
  remove-playwright-test-data.js
  reset-migrate-aggregate-table-state.js
  reset-password.mts
  run-backend-tests.mjs
  simple-dns-server.js
  … 2 more files
public/  (3 files)
  icon.svg
  manifest.json
  serviceWorker.js
server/  (247 files)
  analytics/  (6 files)
    analytics.js
    google-analytics.js
    matomo-analytics.js
    plausible-analytics.js
    rybbit-analytics.js
    umami-analytics.js
  jobs/  (2 files)
    clear-old-data.js
    incremental-vacuum.js
  model/  (13 files)
    api_key.js
    docker_host.js
    domain_expiry.js
    group.js
    heartbeat.js
    incident.js
    maintenance.js
    monitor.js
    proxy.js
    remote_browser.js
    status_page.js
    tag.js
    user.js
  modules/  (28 files)
    axios-ntlm/  (5 files)
      … 5 files under this directory
    ping/  (17 files)
      … 17 files under this directory
    prometheus-api-metrics/  (6 files)
      … 6 files under this directory
  monitor-conditions/  (4 files)
    evaluator.js
    expression.js
    operators.js
    variables.js
  monitor-types/  (28 files)
    dns.js
    gamedig.js
    globalping.js
    group.js
    grpc.js
    manual.js
    mongodb.js
    monitor-type.js
    mqtt.js
    mssql.js
    mysql.js
    ntp.js
    oracledb.js
    ping.js
    pm2.js
    postgres.js
    rabbitmq.js
    real-browser-monitor-type.js
    redis.js
    sftp.js
    sip-options.js
    smtp.js
    snmp.js
    steam.js
    … 4 more files
  notification-providers/  (112 files)
    360messenger.js
    46elks.js
    HaloPSA.js
    Webpush.js
    alerta.js
    alertnow.js
    aliyun-sms.js
    amootsms.js
    apprise.js
    bale.js
    bark.js
    bearsms.js
    bitrix24.js
    brevo.js
    call-me-bot.js
    cellsynt.js
    clicksendsms.js
    clickup.js
    dingding.js
    discord.js
    egosms.js
    evolution.js
    feishu.js
    flashduty.js
    … 88 more files
  routers/  (4 files)
    api-router.js
    better-auth-router.ts
    mcp-router.ts
    status-page-router.js
  socket-handlers/  (11 files)
    api-key-socket-handler.js
    better-auth-socket-handler.ts
    chart-socket-handler.js
    cloudflared-socket-handler.js
    database-socket-handler.js
    docker-socket-handler.js
    general-socket-handler.js
    maintenance-socket-handler.js
    proxy-socket-handler.js
    remote-browser-socket-handler.js
    status-page-socket-handler.js
  util/  (1 files)
    pm2.js
  utils/  (5 files)
    knex/  (1 files)
      … 1 files under this directory
    array-with-key.js
    limit-queue.js
    response-cache.js
    simple-migration-server.js
  auth.ts
  better-auth.ts
  check-version.js
  client.js
  compact-monitor.ts
  config.js
  database.js
  docker.js
  embedded-mariadb.js
  heartbeat-emit.ts
  image-data-uri.js
  initial-admin.ts
  jobs.js
  login-lists.ts
  monitor-stats.ts
  monitor-tls.ts
  notification.js
  password-hash.js
  prometheus-monitor.ts
  prometheus.js
  proxy.js
  radius-client.js
  rate-limiter.js
  remote-browser.js
  … 9 more files
src/  (288 files)
  assets/  (5 files)
    app.scss
    localization.scss
    multiselect.scss
    vars.scss
    vue-datepicker.scss
  components/  (167 files)
    notifications/  (112 files)
      … 112 files under this directory
    settings/  (12 files)
      … 12 files under this directory
    APIKeyDialog.vue
    ActionInput.vue
    ActionSelect.vue
    BadgeLinkGeneratorDialog.vue
    CertificateInfo.vue
    CertificateInfoRow.vue
    Confirm.vue
    CopyableInput.vue
    CountUp.vue
    CreateGroupDialog.vue
    Datetime.vue
    DockerHostDialog.vue
    EditMonitorCondition.vue
    EditMonitorConditionGroup.vue
    EditMonitorConditions.vue
    HeartbeatBar.vue
    HiddenInput.vue
    IncidentEditForm.vue
    IncidentHistory.vue
    IncidentManageModal.vue
    Login.vue
    MaintenanceTime.vue
    MonitorList.vue
    MonitorListFilter.vue
    … 19 more files
  lang/  (81 files)
    README.md
    ab.json
    af.json
    ang.json
    ar-SY.json
    ar.json
    az.json
    bar.json
    be.json
    bg-BG.json
    bn.json
    ca.json
    ca@valencia.json
    ckb.json
    cs-CZ.json
    da-DK.json
    de-CH.json
    de-DE.json
    el-GR.json
    en.json
    en_GB.json
    enm.json
    es-ES.json
    et-EE.json
    … 57 more files
  layouts/  (2 files)
    EmptyLayout.vue
    Layout.vue
  mixins/  (6 files)
    datetime.js
    lang.js
    mobile.js
    public.js
    socket.js
    theme.js
  pages/  (14 files)
    AddStatusPage.vue
    Dashboard.vue
    DashboardHome.vue
    Details.vue
    EditMaintenance.vue
    Entry.vue
    List.vue
    ManageMaintenance.vue
    ManageStatusPage.vue
    NotFound.vue
    Settings.vue
    Setup.vue
    SetupDatabase.vue
    StatusPage.vue
  App.vue
  auth-client.ts
  beat-state.ts
  beat-version-throttle.ts
  dashboard-progress.ts
  heartbeat-history.ts
  i18n.js
  icon.js
  main.js
  monitor-list-window.ts
  router.js
  util-frontend.ts
  util.ts
test/  (14 files)
  backend-test/  (14 files)
    monitor-conditions/  (3 files)
      … 3 files under this directory
    monitors/  (9 files)
      … 9 files under this directory
    README.md
    check-translations.test.js
.dockerignore
.editorconfig
.eslintrc.js
.gitignore
.prettierignore
.prettierrc.js
.stylelintrc
.ws-context
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
compose.yaml
ecosystem.config.js
index.html
package.json
playwright.config.js
```

## Entry points

- [extra/kuma-pr/index.mjs](https://github.com/louislam/uptime-kuma/blob/7e5075d12c85f7282f9c7b7d6821d56aa3acc688/extra/kuma-pr/index.mjs)
- [extra/push-examples/javascript-fetch/index.js](https://github.com/louislam/uptime-kuma/blob/7e5075d12c85f7282f9c7b7d6821d56aa3acc688/extra/push-examples/javascript-fetch/index.js)
- [extra/push-examples/typescript-fetch/index.ts](https://github.com/louislam/uptime-kuma/blob/7e5075d12c85f7282f9c7b7d6821d56aa3acc688/extra/push-examples/typescript-fetch/index.ts)
- [server/modules/ping/index.js](https://github.com/louislam/uptime-kuma/blob/7e5075d12c85f7282f9c7b7d6821d56aa3acc688/server/modules/ping/index.js)
- [server/modules/prometheus-api-metrics/index.js](https://github.com/louislam/uptime-kuma/blob/7e5075d12c85f7282f9c7b7d6821d56aa3acc688/server/modules/prometheus-api-metrics/index.js)
- [server/server.js](https://github.com/louislam/uptime-kuma/blob/7e5075d12c85f7282f9c7b7d6821d56aa3acc688/server/server.js)
- [src/components/notifications/index.js](https://github.com/louislam/uptime-kuma/blob/7e5075d12c85f7282f9c7b7d6821d56aa3acc688/src/components/notifications/index.js)
- [src/main.js](https://github.com/louislam/uptime-kuma/blob/7e5075d12c85f7282f9c7b7d6821d56aa3acc688/src/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| App.vue package | library | Observed | Groups 1 file(s) under app.vue package (observed from repository paths and static analysis). |
| auth-client.ts package | library | Observed | Groups 1 file(s) under auth-client.ts package (observed from repository paths and static analysis). |
| beat-state.ts package | library | Observed | Groups 1 file(s) under beat-state.ts package (observed from repository paths and static analysis). |
| beat-version-throttle.ts package | library | Observed | Groups 1 file(s) under beat-version-throttle.ts package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 155 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 105 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| dashboard-progress.ts package | library | Observed | Groups 1 file(s) under dashboard-progress.ts package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 66 file(s) under data layer (observed from repository paths and static analysis). |
| extra package | library | Observed | Groups 52 file(s) under extra package (observed from repository paths and static analysis). |
| heartbeat-history.ts package | library | Observed | Groups 1 file(s) under heartbeat-history.ts package (observed from repository paths and static analysis). |
| i18n.js package | library | Observed | Groups 1 file(s) under i18n.js package (observed from repository paths and static analysis). |
| icon.js package | library | Observed | Groups 1 file(s) under icon.js package (observed from repository paths and static analysis). |
| layouts package | library | Observed | Groups 2 file(s) under layouts package (observed from repository paths and static analysis). |
| main.js package | library | Observed | Groups 1 file(s) under main.js package (observed from repository paths and static analysis). |
| mixins package | library | Observed | Groups 6 file(s) under mixins package (observed from repository paths and static analysis). |
| monitor-list-window.ts package | library | Observed | Groups 1 file(s) under monitor-list-window.ts package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 14 file(s) under pages package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| router.js package | library | Observed | Groups 1 file(s) under router.js package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 239 file(s) under server package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). |
| util-frontend.ts package | library | Observed | Groups 1 file(s) under util-frontend.ts package (observed from repository paths and static analysis). |
| util.ts package | library | Observed | Groups 1 file(s) under util.ts package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/ask_for_help.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/actions/setup-atlascloud/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/opencode-models.json` (config)
- `.github/workflows/ai-slop.yml` (ci)
- `.github/workflows/auto-test.yml` (ci)
- `.github/workflows/autofix.yml` (ci)
- `.github/workflows/build-docker-base.yml` (ci)
- `.github/workflows/build-docker-pr-test.yml` (ci)
- `.github/workflows/build-docker-push.yml` (ci)
- `.github/workflows/close-incorrect-issue.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/conflict-labeler.yml` (ci)
- `.github/workflows/deleted-pr.yml` (ci)
- `.github/workflows/duplicate-issues.yml` (ci)
- `.github/workflows/mark-as-draft-on-requesting-changes.yml` (ci)
- `.github/workflows/new-contributor-pr.yml` (ci)
- `.github/workflows/npm-update.yml` (ci)
- `.github/workflows/pr-description-check.yml` (ci)
- `.github/workflows/pr-title.yml` (ci)
- `.github/workflows/prevent-file-change.yml` (ci)
- `.github/workflows/release-nightly.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/stale-bot.yml` (ci)
- `.github/workflows/validate.yml` (ci)
- `compose.yaml` (container)
- `docker/docker-compose-dev.yml` (config)
- `docker/dockerfile` (container)
- `extra/docker-latest-warning/Dockerfile.latest-warning` (container)
- `extra/docker-latest-warning/package.json` (manifest)
- `extra/kuma-pr/package.json` (manifest)
- `extra/push-examples/javascript-fetch/package.json` (manifest)
- `extra/push-examples/typescript-fetch/package.json` (manifest)
- `extra/rdap-dns.json` (config)
- `extra/uptime-kuma-push/Dockerfile` (container)
- `extra/uptime-kuma-push/package.json` (manifest)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `src/lang/ab.json` (config)
- `src/lang/af.json` (config)
- `src/lang/ang.json` (config)
- `src/lang/ar-SY.json` (config)
- `src/lang/ar.json` (config)
- `src/lang/az.json` (config)
- `src/lang/bar.json` (config)
- `src/lang/be.json` (config)
- `src/lang/bg-BG.json` (config)
- `src/lang/bn.json` (config)
- `src/lang/ca.json` (config)
- `src/lang/ca@valencia.json` (config)
- `src/lang/ckb.json` (config)
- `src/lang/cs-CZ.json` (config)
- `src/lang/da-DK.json` (config)
- `src/lang/de-CH.json` (config)
- `src/lang/de-DE.json` (config)
- `src/lang/el-GR.json` (config)
- `src/lang/en.json` (config)
- `src/lang/en_GB.json` (config)
- `src/lang/enm.json` (config)
- `src/lang/es-ES.json` (config)
- `src/lang/et-EE.json` (config)
- `src/lang/eu.json` (config)
- `src/lang/fa.json` (config)
- `src/lang/fi.json` (config)
- `src/lang/fr-FR.json` (config)
- `src/lang/ga.json` (config)
- `src/lang/gl.json` (config)
- `src/lang/he-IL.json` (config)
- `src/lang/he.json` (config)
- `src/lang/hi.json` (config)
- `src/lang/hr-HR.json` (config)
- `src/lang/hu.json` (config)
- `src/lang/id-ID.json` (config)
- `src/lang/it-IT.json` (config)
- `src/lang/ja.json` (config)
- `src/lang/ka.json` (config)
- `src/lang/ko-KR.json` (config)
- `src/lang/lb.json` (config)
- `src/lang/lt.json` (config)
- `src/lang/lv.json` (config)
- `src/lang/lzh.json` (config)
- `src/lang/mk.json` (config)
- `src/lang/ml.json` (config)
- `src/lang/mr.json` (config)
- `src/lang/ms.json` (config)
- `src/lang/my.json` (config)
- `src/lang/nb-NO.json` (config)
- `src/lang/ne.json` (config)
- `src/lang/nl-NL.json` (config)
- `src/lang/pa.json` (config)
- `src/lang/pa_PK.json` (config)
- `src/lang/pl.json` (config)
- `src/lang/pt-BR.json` (config)
- `src/lang/pt-PT.json` (config)
- `src/lang/pt.json` (config)
- `src/lang/ro.json` (config)
- `src/lang/ru-RU.json` (config)
- `src/lang/sk.json` (config)
- `src/lang/sl-SI.json` (config)
- `src/lang/sq.json` (config)
- `src/lang/sr-latn.json` (config)
- `src/lang/sr.json` (config)
- `src/lang/sv-SE.json` (config)
- `src/lang/te.json` (config)
- `src/lang/th-TH.json` (config)
- `src/lang/tr-TR.json` (config)
- `src/lang/ug.json` (config)
- `src/lang/uk-UA.json` (config)
- `src/lang/ur.json` (config)
- `src/lang/uz.json` (config)
- `src/lang/vi-VN.json` (config)
- `src/lang/vls.json` (config)
- `src/lang/xh.json` (config)
- `src/lang/yue.json` (config)
- `src/lang/zh-CN.json` (config)
- `src/lang/zh-HK.json` (config)
- `src/lang/zh-TW.json` (config)
- `src/lang/zu.json` (config)

## Top-level layout

- `src` — 288 analysed file(s)
- `server` — 247 analysed file(s)
- `db` — 122 analysed file(s)
- `extra` — 66 analysed file(s)
- `.github` — 33 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `test` — 14 analysed file(s)
- `docker` — 6 analysed file(s)
- `public` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7e5075d12c85f7282f9c7b7d6821d56aa3acc688` is the revision these paths and observations refer to.
