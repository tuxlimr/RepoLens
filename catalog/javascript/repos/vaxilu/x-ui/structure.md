# Project structure: vaxilu/x-ui

**Analysed commit:** `9c1be8c57a53953b47ee7c09a93554e73816f907`

**Commit reference:** [9c1be8c57a53953b47ee7c09a93554e73816f907](https://github.com/vaxilu/x-ui/commit/9c1be8c57a53953b47ee7c09a93554e73816f907)

**Tree at this commit:** [vaxilu/x-ui@9c1be8c57a53](https://github.com/vaxilu/x-ui/tree/9c1be8c57a53953b47ee7c09a93554e73816f907)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vaxilu/x-ui |
| Description | 支持多协议多用户的 xray 面板 |
| Stars | 19078 |
| Forks | 7168 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `9c1be8c57a53953b47ee7c09a93554e73816f907` |
| Retrieved at | 2026-11-14T19:11:21.457643+00:00 |
| Files in this snapshot | 108 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (1 files)
    ------.md
  workflows/  (1 files)
    release.yml
config/  (3 files)
  config.go
  name
  version
database/  (2 files)
  model/  (1 files)
    model.go
  db.go
logger/  (1 files)
  logger.go
util/  (12 files)
  common/  (4 files)
    err.go
    format.go
    multi_error.go
    stringUtil.go
  json_util/  (1 files)
    json.go
  random/  (1 files)
    random.go
  reflect_util/  (1 files)
    reflect.go
  sys/  (4 files)
    a.s
    psutil.go
    sys_darwin.go
    sys_linux.go
  context.go
v2ui/  (3 files)
  db.go
  models.go
  v2ui.go
web/  (71 files)
  assets/  (13 files)
    ant-design-vue@1.7.2/  (1 files)
      … 1 files under this directory
    css/  (1 files)
      … 1 files under this directory
    element-ui@2.15.0/  (1 files)
      … 1 files under this directory
    js/  (6 files)
      … 6 files under this directory
    vue@2.6.12/  (4 files)
      … 4 files under this directory
  controller/  (7 files)
    base.go
    inbound.go
    index.go
    server.go
    setting.go
    util.go
    xui.go
  entity/  (1 files)
    entity.go
  global/  (1 files)
    global.go
  html/  (31 files)
    common/  (5 files)
      … 5 files under this directory
    xui/  (25 files)
      … 25 files under this directory
    login.html
  job/  (4 files)
    check_inbound_job.go
    check_xray_running_job.go
    stats_notify_job.go
    xray_traffic_job.go
  network/  (2 files)
    auto_https_listener.go
    autp_https_conn.go
  service/  (7 files)
    config.json
    inbound.go
    panel.go
    server.go
    setting.go
    user.go
    xray.go
  session/  (1 files)
    session.go
  translation/  (3 files)
    translate.en_US.toml
    translate.zh_Hans.toml
    translate.zh_Hant.toml
  web.go
xray/  (4 files)
  config.go
  inbound.go
  process.go
  traffic.go
.gitignore
Dockerfile
LICENSE
README.md
go.mod
go.sum
install.sh
main.go
x-ui.service
x-ui.sh
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| logger package | library | Observed | Groups 1 file(s) under logger package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 11 file(s) under util package (observed from repository paths and static analysis). |
| v2ui package | library | Observed | Groups 3 file(s) under v2ui package (observed from repository paths and static analysis). |
| web package | library | Observed | Groups 27 file(s) under web package (observed from repository paths and static analysis). |
| xray package | library | Observed | Groups 4 file(s) under xray package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/release.yml` (ci)
- `Dockerfile` (container)
- `go.mod` (manifest)
- `web/service/config.json` (config)
- `web/translation/translate.en_US.toml` (config)
- `web/translation/translate.zh_Hans.toml` (config)
- `web/translation/translate.zh_Hant.toml` (config)

## Top-level layout

- `web` — 71 analysed file(s)
- `util` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `xray` — 4 analysed file(s)
- `config` — 3 analysed file(s)
- `v2ui` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `database` — 2 analysed file(s)
- `logger` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9c1be8c57a53953b47ee7c09a93554e73816f907` is the revision these paths and observations refer to.
