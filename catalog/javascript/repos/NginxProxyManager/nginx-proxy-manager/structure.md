# Project structure: NginxProxyManager/nginx-proxy-manager

**Analysed commit:** `66ab4b24d1a07587ec0d481740ce57abefbebfaa`

**Commit reference:** [66ab4b24d1a07587ec0d481740ce57abefbebfaa](https://github.com/NginxProxyManager/nginx-proxy-manager/commit/66ab4b24d1a07587ec0d481740ce57abefbebfaa)

**Tree at this commit:** [NginxProxyManager/nginx-proxy-manager@66ab4b24d1a0](https://github.com/NginxProxyManager/nginx-proxy-manager/tree/66ab4b24d1a07587ec0d481740ce57abefbebfaa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | NginxProxyManager/nginx-proxy-manager |
| Description | Docker container for managing Nginx proxy hosts with a simple, powerful interface |
| Stars | 34712 |
| Forks | 3973 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `66ab4b24d1a07587ec0d481740ce57abefbebfaa` |
| Retrieved at | 2026-11-14T19:10:43.701952+00:00 |
| Files in this snapshot | 798 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    dns_challenge_request.md
    feature_request.md
  workflows/  (1 files)
    stale.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
backend/  (270 files)
  certbot/  (2 files)
    README.md
    dns-plugins.json
  config/  (3 files)
    README.md
    default.json
    sqlite-test-db.json
  internal/  (17 files)
    2fa.js
    access-list.js
    audit-log.js
    certificate.js
    dead-host.js
    host.js
    ip_ranges.js
    log-viewer.js
    nginx.js
    proxy-host.js
    redirection-host.js
    remote-version.js
    report.js
    setting.js
    stream.js
    token.js
    user.js
  lib/  (63 files)
    access/  (46 files)
      … 46 files under this directory
    express/  (7 files)
      … 7 files under this directory
    validator/  (2 files)
      … 2 files under this directory
    access.js
    certbot.js
    config.js
    error.js
    helpers.js
    migrate_template.js
    nginx-values.js
    utils.js
  migrations/  (20 files)
    20180618015850_initial.js
    20180929054513_websockets.js
    20181019052346_forward_host.js
    20181113041458_http2_support.js
    20181213013211_forward_scheme.js
    20190104035154_disabled.js
    20190215115310_customlocations.js
    20190218060101_hsts.js
    20190227065017_settings.js
    20200410143839_access_list_client.js
    20200410143840_access_list_client_fix.js
    20201014143841_pass_auth.js
    20210210154702_redirection_scheme.js
    20210210154703_redirection_status_code.js
    20210423103500_stream_domain.js
    20211108145214_regenerate_default_host.js
    20240427161436_stream_ssl.js
    20251111090000_redirect_auto_scheme.js
    20260131163528_trust_forwarded_proto.js
    20260906220000_user_permission_meta.js
  models/  (15 files)
    access_list.js
    access_list_auth.js
    access_list_client.js
    audit-log.js
    auth.js
    certificate.js
    dead_host.js
    now_helper.js
    proxy_host.js
    redirection_host.js
    setting.js
    stream.js
    token.js
    user.js
    user_permission.js
  routes/  (16 files)
    nginx/  (6 files)
      … 6 files under this directory
    audit-log.js
    ci.js
    logs.js
    main.js
    reports.js
    schema.js
    settings.js
    tokens.js
    users.js
    version.js
  schema/  (101 files)
    components/  (28 files)
      … 28 files under this directory
    paths/  (70 files)
      … 70 files under this directory
    common.json
    index.js
    swagger.json
  scripts/  (2 files)
    install-certbot-plugins
    regenerate-config
  templates/  (18 files)
    _access.conf
    _assets.conf
    _certificates.conf
    _certificates_stream.conf
    _exploits.conf
    _forced_ssl.conf
    _header_comment.conf
    _hsts.conf
    _hsts_map.conf
    _listen.conf
    _location.conf
    dead_host.conf
    default.conf
    ip_ranges.conf
    letsencrypt-request.conf
    proxy_host.conf
    redirection_host.conf
    stream.conf
  test/  (1 files)
    nginx-values.test.js
  .gitignore
  app.js
  biome.json
  db.js
  index.js
  knexfile.js
  logger.js
  migrate.js
  nodemon.json
  package.json
  setup.js
  validate-schema.js
docker/  (63 files)
  dev/  (5 files)
    Dockerfile
    dnsrouter-config.json
    letsencrypt.ini
    pdns-db.sql
    squid.conf
  rootfs/  (48 files)
    etc/  (44 files)
      … 44 files under this directory
    root/  (1 files)
      … 1 files under this directory
    usr/  (2 files)
      … 2 files under this directory
    var/  (1 files)
      … 1 files under this directory
  scripts/  (1 files)
    install-s6
  .dive-ci
  Dockerfile
  ci.env
  docker-compose.ci.isolated.yml
  docker-compose.ci.mysql.yml
  docker-compose.ci.postgres.yml
  docker-compose.ci.sqlite.yml
  docker-compose.ci.yml
  docker-compose.dev.yml
docs/  (18 files)
  .vitepress/  (3 files)
    theme/  (2 files)
      … 2 files under this directory
    config.mts
  scripts/  (1 files)
    set-version.sh
  src/  (12 files)
    advanced-config/  (1 files)
      … 1 files under this directory
    certbot/  (1 files)
      … 1 files under this directory
    faq/  (1 files)
      … 1 files under this directory
    guide/  (1 files)
      … 1 files under this directory
    public/  (2 files)
      … 2 files under this directory
    screenshots/  (1 files)
      … 1 files under this directory
    setup/  (1 files)
      … 1 files under this directory
    third-party/  (2 files)
      … 2 files under this directory
    upgrading/  (1 files)
      … 1 files under this directory
    index.md
  .gitignore
  package.json
frontend/  (435 files)
  public/  (6 files)
    images/  (6 files)
      … 6 files under this directory
  src/  (424 files)
    api/  (69 files)
      … 69 files under this directory
    components/  (56 files)
      … 56 files under this directory
    context/  (4 files)
      … 4 files under this directory
    hooks/  (26 files)
      … 26 files under this directory
    locale/  (219 files)
      … 219 files under this directory
    modals/  (22 files)
      … 22 files under this directory
    modules/  (3 files)
      … 3 files under this directory
    notifications/  (4 files)
      … 4 files under this directory
    pages/  (15 files)
      … 15 files under this directory
    App.css
    App.tsx
    Router.test.tsx
    Router.tsx
    declarations.d.ts
    main.tsx
  .gitignore
  biome.json
  check-locales.cjs
  index.html
  package.json
.gitattributes
.gitignore
.version
LICENSE
README.md
SECURITY.md
```

## Entry points

- [backend/index.js](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/backend/index.js)
- [backend/app.js](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/backend/app.js)
- [backend/lib/validator/index.js](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/backend/lib/validator/index.js)
- [backend/routes/main.js](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/backend/routes/main.js)
- [backend/schema/index.js](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/backend/schema/index.js)
- [frontend/src/App.tsx](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/frontend/src/App.tsx)
- [frontend/src/components/Page.tsx](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/frontend/src/components/Page.tsx)
- [frontend/src/components/index.ts](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/frontend/src/components/index.ts)
- [frontend/src/context/index.ts](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/frontend/src/context/index.ts)
- [frontend/src/hooks/index.ts](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/frontend/src/hooks/index.ts)
- [frontend/src/locale/index.ts](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/frontend/src/locale/index.ts)
- [frontend/src/main.tsx](https://github.com/NginxProxyManager/nginx-proxy-manager/blob/66ab4b24d1a07587ec0d481740ce57abefbebfaa/frontend/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 85 file(s) under api layer (observed from repository paths and static analysis). |
| backend package | library | Observed | Groups 63 file(s) under backend package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 192 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 15 file(s) under data layer (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 10 file(s) under docker package (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 159 file(s) under frontend package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/stale.yml` (ci)
- `backend/biome.json` (config)
- `backend/certbot/dns-plugins.json` (config)
- `backend/config/default.json` (config)
- `backend/config/sqlite-test-db.json` (config)
- `backend/lib/access/access_lists-create.json` (config)
- `backend/lib/access/access_lists-delete.json` (config)
- `backend/lib/access/access_lists-get.json` (config)
- `backend/lib/access/access_lists-list.json` (config)
- `backend/lib/access/access_lists-update.json` (config)
- `backend/lib/access/auditlog-list.json` (config)
- `backend/lib/access/certificates-create.json` (config)
- `backend/lib/access/certificates-delete.json` (config)
- `backend/lib/access/certificates-get.json` (config)
- `backend/lib/access/certificates-list.json` (config)
- `backend/lib/access/certificates-update.json` (config)
- `backend/lib/access/dead_hosts-create.json` (config)
- `backend/lib/access/dead_hosts-delete.json` (config)
- `backend/lib/access/dead_hosts-get.json` (config)
- `backend/lib/access/dead_hosts-list.json` (config)
- `backend/lib/access/dead_hosts-update.json` (config)
- `backend/lib/access/logs-list.json` (config)
- `backend/lib/access/permissions.json` (config)
- `backend/lib/access/proxy_hosts-create.json` (config)
- `backend/lib/access/proxy_hosts-delete.json` (config)
- `backend/lib/access/proxy_hosts-get.json` (config)
- `backend/lib/access/proxy_hosts-list.json` (config)
- `backend/lib/access/proxy_hosts-update.json` (config)
- `backend/lib/access/redirection_hosts-create.json` (config)
- `backend/lib/access/redirection_hosts-delete.json` (config)
- `backend/lib/access/redirection_hosts-get.json` (config)
- `backend/lib/access/redirection_hosts-list.json` (config)
- `backend/lib/access/redirection_hosts-update.json` (config)
- `backend/lib/access/reports-hosts.json` (config)
- `backend/lib/access/roles.json` (config)
- `backend/lib/access/settings-get.json` (config)
- `backend/lib/access/settings-list.json` (config)
- `backend/lib/access/settings-update.json` (config)
- `backend/lib/access/streams-create.json` (config)
- `backend/lib/access/streams-delete.json` (config)
- `backend/lib/access/streams-get.json` (config)
- `backend/lib/access/streams-list.json` (config)
- `backend/lib/access/streams-update.json` (config)
- `backend/lib/access/users-create.json` (config)
- `backend/lib/access/users-delete.json` (config)
- `backend/lib/access/users-get.json` (config)
- `backend/lib/access/users-list.json` (config)
- `backend/lib/access/users-loginas.json` (config)
- `backend/lib/access/users-password.json` (config)
- `backend/lib/access/users-permissions.json` (config)
- `backend/lib/access/users-update.json` (config)
- `backend/nodemon.json` (config)
- `backend/package.json` (manifest)
- `backend/schema/common.json` (config)
- `backend/schema/components/access-list-object.json` (config)
- `backend/schema/components/audit-log-list.json` (config)
- `backend/schema/components/audit-log-object.json` (config)
- `backend/schema/components/certificate-list.json` (config)
- `backend/schema/components/certificate-object.json` (config)
- `backend/schema/components/check-version-object.json` (config)
- `backend/schema/components/dead-host-list.json` (config)
- `backend/schema/components/dead-host-object.json` (config)
- `backend/schema/components/dns-providers-list.json` (config)
- `backend/schema/components/error-object.json` (config)
- `backend/schema/components/error.json` (config)
- `backend/schema/components/health-object.json` (config)
- `backend/schema/components/log-sources-object.json` (config)
- `backend/schema/components/log-tail-object.json` (config)
- `backend/schema/components/permission-object.json` (config)
- `backend/schema/components/proxy-host-list.json` (config)
- `backend/schema/components/proxy-host-object.json` (config)
- `backend/schema/components/redirection-host-list.json` (config)
- `backend/schema/components/redirection-host-object.json` (config)
- `backend/schema/components/security-schemes.json` (config)
- `backend/schema/components/setting-list.json` (config)
- `backend/schema/components/setting-object.json` (config)
- `backend/schema/components/stream-list.json` (config)
- `backend/schema/components/stream-object.json` (config)
- `backend/schema/components/token-challenge.json` (config)
- `backend/schema/components/token-object.json` (config)
- `backend/schema/components/user-list.json` (config)
- `backend/schema/components/user-object.json` (config)
- `backend/schema/paths/audit-log/get.json` (config)
- `backend/schema/paths/audit-log/id/get.json` (config)
- `backend/schema/paths/get.json` (config)
- `backend/schema/paths/logs/sources/get.json` (config)
- `backend/schema/paths/logs/tail/get.json` (config)
- `backend/schema/paths/nginx/access-lists/get.json` (config)
- `backend/schema/paths/nginx/access-lists/listID/delete.json` (config)
- `backend/schema/paths/nginx/access-lists/listID/get.json` (config)
- `backend/schema/paths/nginx/access-lists/listID/put.json` (config)
- `backend/schema/paths/nginx/access-lists/post.json` (config)
- `backend/schema/paths/nginx/certificates/certID/delete.json` (config)
- `backend/schema/paths/nginx/certificates/certID/download/get.json` (config)
- `backend/schema/paths/nginx/certificates/certID/get.json` (config)
- `backend/schema/paths/nginx/certificates/certID/renew/post.json` (config)
- `backend/schema/paths/nginx/certificates/certID/upload/post.json` (config)
- `backend/schema/paths/nginx/certificates/dns-providers/get.json` (config)
- `backend/schema/paths/nginx/certificates/get.json` (config)
- `backend/schema/paths/nginx/certificates/post.json` (config)
- `backend/schema/paths/nginx/certificates/test-http/post.json` (config)
- `backend/schema/paths/nginx/certificates/validate/post.json` (config)
- `backend/schema/paths/nginx/dead-hosts/get.json` (config)
- `backend/schema/paths/nginx/dead-hosts/hostID/delete.json` (config)
- `backend/schema/paths/nginx/dead-hosts/hostID/disable/post.json` (config)
- `backend/schema/paths/nginx/dead-hosts/hostID/enable/post.json` (config)
- `backend/schema/paths/nginx/dead-hosts/hostID/get.json` (config)
- `backend/schema/paths/nginx/dead-hosts/hostID/put.json` (config)
- `backend/schema/paths/nginx/dead-hosts/post.json` (config)
- `backend/schema/paths/nginx/proxy-hosts/get.json` (config)
- `backend/schema/paths/nginx/proxy-hosts/hostID/delete.json` (config)
- `backend/schema/paths/nginx/proxy-hosts/hostID/disable/post.json` (config)
- `backend/schema/paths/nginx/proxy-hosts/hostID/enable/post.json` (config)
- `backend/schema/paths/nginx/proxy-hosts/hostID/get.json` (config)
- `backend/schema/paths/nginx/proxy-hosts/hostID/put.json` (config)
- `backend/schema/paths/nginx/proxy-hosts/post.json` (config)
- `backend/schema/paths/nginx/redirection-hosts/get.json` (config)
- `backend/schema/paths/nginx/redirection-hosts/hostID/delete.json` (config)
- `backend/schema/paths/nginx/redirection-hosts/hostID/disable/post.json` (config)
- `backend/schema/paths/nginx/redirection-hosts/hostID/enable/post.json` (config)
- `backend/schema/paths/nginx/redirection-hosts/hostID/get.json` (config)
- `backend/schema/paths/nginx/redirection-hosts/hostID/put.json` (config)
- `backend/schema/paths/nginx/redirection-hosts/post.json` (config)
- `backend/schema/paths/nginx/streams/get.json` (config)
- `backend/schema/paths/nginx/streams/post.json` (config)
- `backend/schema/paths/nginx/streams/streamID/delete.json` (config)
- `backend/schema/paths/nginx/streams/streamID/disable/post.json` (config)
- `backend/schema/paths/nginx/streams/streamID/enable/post.json` (config)
- `backend/schema/paths/nginx/streams/streamID/get.json` (config)
- `backend/schema/paths/nginx/streams/streamID/put.json` (config)
- `backend/schema/paths/reports/hosts/get.json` (config)
- `backend/schema/paths/schema/get.json` (config)
- `backend/schema/paths/settings/get.json` (config)
- `backend/schema/paths/settings/settingID/get.json` (config)
- `backend/schema/paths/settings/settingID/put.json` (config)
- `backend/schema/paths/tokens/2fa/post.json` (config)
- `backend/schema/paths/tokens/get.json` (config)
- `backend/schema/paths/tokens/post.json` (config)
- `backend/schema/paths/users/get.json` (config)
- `backend/schema/paths/users/post.json` (config)
- `backend/schema/paths/users/userID/2fa/backup-codes/post.json` (config)
- `backend/schema/paths/users/userID/2fa/delete.json` (config)
- `backend/schema/paths/users/userID/2fa/enable/post.json` (config)
- `backend/schema/paths/users/userID/2fa/get.json` (config)
- `backend/schema/paths/users/userID/2fa/post.json` (config)
- `backend/schema/paths/users/userID/auth/put.json` (config)
- `backend/schema/paths/users/userID/delete.json` (config)
- `backend/schema/paths/users/userID/get.json` (config)
- `backend/schema/paths/users/userID/login/post.json` (config)
- `backend/schema/paths/users/userID/permissions/put.json` (config)
- `backend/schema/paths/users/userID/put.json` (config)
- `backend/schema/paths/version/check/get.json` (config)
- `backend/schema/swagger.json` (config)
- `docker/Dockerfile` (container)
- `docker/dev/Dockerfile` (container)
- `docker/dev/dnsrouter-config.json` (config)
- `docker/dev/letsencrypt.ini` (config)
- `docker/docker-compose.ci.isolated.yml` (config)
- `docker/docker-compose.ci.mysql.yml` (config)
- `docker/docker-compose.ci.postgres.yml` (config)
- `docker/docker-compose.ci.sqlite.yml` (config)
- `docker/docker-compose.ci.yml` (config)
- `docker/docker-compose.dev.yml` (config)
- `docker/rootfs/etc/letsencrypt.ini` (config)
- `docs/package.json` (manifest)
- `frontend/biome.json` (config)
- `frontend/package.json` (manifest)
- `frontend/src/locale/src/az.json` (config)
- `frontend/src/locale/src/bg.json` (config)
- `frontend/src/locale/src/cs.json` (config)
- `frontend/src/locale/src/de.json` (config)
- `frontend/src/locale/src/en.json` (config)
- `frontend/src/locale/src/es.json` (config)
- `frontend/src/locale/src/et.json` (config)
- `frontend/src/locale/src/fa.json` (config)
- `frontend/src/locale/src/fr.json` (config)
- `frontend/src/locale/src/ga.json` (config)
- `frontend/src/locale/src/hu.json` (config)
- `frontend/src/locale/src/id.json` (config)
- `frontend/src/locale/src/it.json` (config)
- `frontend/src/locale/src/ja.json` (config)
- `frontend/src/locale/src/ko.json` (config)
- `frontend/src/locale/src/lang-list.json` (config)
- `frontend/src/locale/src/nl.json` (config)
- `frontend/src/locale/src/no.json` (config)
- `frontend/src/locale/src/pl.json` (config)
- `frontend/src/locale/src/pt.json` (config)
- `frontend/src/locale/src/ru.json` (config)
- `frontend/src/locale/src/sk.json` (config)
- `frontend/src/locale/src/tr.json` (config)
- `frontend/src/locale/src/uk.json` (config)
- `frontend/src/locale/src/vi.json` (config)
- `frontend/src/locale/src/zh-tw.json` (config)
- `frontend/src/locale/src/zh.json` (config)

## Top-level layout

- `frontend` — 435 analysed file(s)
- `backend` — 270 analysed file(s)
- `docker` — 63 analysed file(s)
- `docs` — 18 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `66ab4b24d1a07587ec0d481740ce57abefbebfaa` is the revision these paths and observations refer to.
