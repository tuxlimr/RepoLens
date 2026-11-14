# Project structure: coaidev/coai

**Analysed commit:** `3048a493eedcfe75de4d59afd5139847ad3195ed`

**Commit reference:** [3048a493eedcfe75de4d59afd5139847ad3195ed](https://github.com/coaidev/coai/commit/3048a493eedcfe75de4d59afd5139847ad3195ed)

**Tree at this commit:** [coaidev/coai@3048a493eedc](https://github.com/coaidev/coai/tree/3048a493eedcfe75de4d59afd5139847ad3195ed)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | coaidev/coai |
| Description | 🚀 Next Gen Multi-tenant AI One-Stop Solution. Builtin Admin & Billing System. Enterprise-Grade Unified LLM Gateway Support for 200+ Models And 35+ Providers, Load Balacing w/ Priority-base Routing, Cost Management, Chat Share, Cloud Sync, Credit/Subscription Billing, All File Parsing, Web Search, B… |
| Stars | 9347 |
| Forks | 1224 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `3048a493eedcfe75de4d59afd5139847ad3195ed` |
| Retrieved at | 2026-11-14T19:13:34.771058+00:00 |
| Files in this snapshot | 533 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    channel_update.md
    config.yml
    feature_request.md
  workflows/  (5 files)
    app.yaml
    build.yaml
    docker-cd.yaml
    docker-ci.yaml
    issue-translator.yaml
adapter/  (68 files)
  azure/  (5 files)
    chat.go
    image.go
    processor.go
    struct.go
    types.go
  baichuan/  (4 files)
    chat.go
    processor.go
    struct.go
    types.go
  bing/  (3 files)
    chat.go
    struct.go
    types.go
  claude/  (3 files)
    chat.go
    struct.go
    types.go
  common/  (2 files)
    interface.go
    types.go
  coze/  (3 files)
    chat.go
    processor.go
    struct.go
  dashscope/  (3 files)
    chat.go
    struct.go
    types.go
  deepseek/  (2 files)
    chat.go
    struct.go
  dify/  (3 files)
    chat.go
    processor.go
    struct.go
  hunyuan/  (3 files)
    chat.go
    sdk.go
    struct.go
  midjourney/  (7 files)
    api.go
    chat.go
    expose.go
    handler.go
    storage.go
    struct.go
    types.go
  openai/  (6 files)
    chat.go
    image.go
    processor.go
    struct.go
    types.go
    videos.go
  palm2/  (5 files)
    chat.go
    formatter.go
    image.go
    struct.go
    types.go
  skylark/  (3 files)
    chat.go
    formatter.go
    struct.go
  slack/  (2 files)
    chat.go
    struct.go
  sparkdesk/  (3 files)
    chat.go
    struct.go
    types.go
  zhinao/  (4 files)
    chat.go
    processor.go
    struct.go
    types.go
  zhipuai/  (4 files)
    chat.go
    processor.go
    struct.go
    types.go
  adapter.go
  request.go
  router.go
addition/  (17 files)
  article/  (4 files)
    data/  (1 files)
      … 1 files under this directory
    api.go
    generate.go
    utils.go
  card/  (5 files)
    .gitignore
    card.go
    card.php
    error.php
    utils.php
  generation/  (5 files)
    data/  (1 files)
      … 1 files under this directory
    api.go
    build.go
    generate.go
    prompt.go
  web/  (2 files)
    call.go
    search.go
  router.go
admin/  (16 files)
  analysis/  (5 files)
    analysis.go
    format.go
    reflect.go
    statistic.go
    types.go
  controller.go
  format.go
  instance.go
  invitation.go
  logger.go
  market.go
  redeem.go
  router.go
  statistic.go
  types.go
  user.go
app/  (312 files)
  public/  (5 files)
    manifest.json
    robots.txt
    service.js
    site.webmanifest
    workbox.js
  src/  (290 files)
    admin/  (15 files)
      … 15 files under this directory
    api/  (16 files)
      … 16 files under this directory
    assets/  (42 files)
      … 42 files under this directory
    components/  (120 files)
      … 120 files under this directory
    conf/  (8 files)
      … 8 files under this directory
    dialogs/  (2 files)
      … 2 files under this directory
    events/  (6 files)
      … 6 files under this directory
    masks/  (2 files)
      … 2 files under this directory
    payment/  (3 files)
      … 3 files under this directory
    plugin/  (1 files)
      … 1 files under this directory
    resources/  (5 files)
      … 5 files under this directory
    routes/  (27 files)
      … 27 files under this directory
    store/  (15 files)
      … 15 files under this directory
    translator/  (4 files)
      … 4 files under this directory
    types/  (3 files)
      … 3 files under this directory
    utils/  (15 files)
      … 15 files under this directory
    App.tsx
    i18n.ts
    main.tsx
    router.tsx
    spinner.tsx
    vite-env.d.ts
  src-tauri/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    Cargo.toml
    build.rs
    tauri.conf.json
  .eslintrc.cjs
  .gitignore
  .prettierrc.json
  components.json
  index.html
  package.json
  postcss.config.js
  qodana.yaml
  tailwind.config.js
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
auth/  (17 files)
  analysis.go
  apikey.go
  auth.go
  call.go
  cert.go
  controller.go
  invitation.go
  package.go
  payment.go
  quota.go
  redeem.go
  router.go
  rule.go
  struct.go
  subscription.go
  usage.go
  validators.go
channel/  (11 files)
  channel.go
  charge.go
  controller.go
  manager.go
  plan.go
  router.go
  sequence.go
  system.go
  ticker.go
  types.go
  worker.go
cli/  (6 files)
  admin.go
  exec.go
  help.go
  invite.go
  parser.go
  token.go
connection/  (4 files)
  cache.go
  database.go
  db_migration.go
  worker.go
globals/  (10 files)
  constant.go
  interface.go
  logger.go
  method.go
  params.go
  sql.go
  tools.go
  types.go
  usage.go
  variables.go
manager/  (22 files)
  broadcast/  (5 files)
    controller.go
    manage.go
    router.go
    types.go
    view.go
  conversation/  (6 files)
    api.go
    conversation.go
    mask.go
    router.go
    shared.go
    storage.go
  chat.go
  chat_completions.go
  completions.go
  connection.go
  images.go
  manager.go
  relay.go
  router.go
  types.go
  usage.go
  videos.go
middleware/  (5 files)
  auth.go
  builtins.go
  cors.go
  middleware.go
  throttle.go
migration/  (2 files)
  3.6.sql
  3.8.sql
utils/  (18 files)
  templates/  (1 files)
    code.html
  base.go
  bootstrap.go
  buffer.go
  cache.go
  char.go
  compress.go
  config.go
  ctx.go
  encrypt.go
  fs.go
  image.go
  net.go
  scanner.go
  smtp.go
  sse.go
  tokenizer.go
  websocket.go
.dockerignore
.gitignore
Dockerfile
LICENSE
README.md
README_ja-JP.md
README_zh-CN.md
config.example.yaml
docker-compose.stable.yaml
docker-compose.watch.yaml
docker-compose.yaml
go.mod
go.sum
main.go
nginx.conf
zeabur.yaml
```

## Entry points

- [app/src/App.tsx](https://github.com/coaidev/coai/blob/3048a493eedcfe75de4d59afd5139847ad3195ed/app/src/App.tsx)
- [app/src/dialogs/index.tsx](https://github.com/coaidev/coai/blob/3048a493eedcfe75de4d59afd5139847ad3195ed/app/src/dialogs/index.tsx)
- [app/src/main.tsx](https://github.com/coaidev/coai/blob/3048a493eedcfe75de4d59afd5139847ad3195ed/app/src/main.tsx)
- [app/src/routes/Index.tsx](https://github.com/coaidev/coai/blob/3048a493eedcfe75de4d59afd5139847ad3195ed/app/src/routes/Index.tsx)
- [app/src/store/index.ts](https://github.com/coaidev/coai/blob/3048a493eedcfe75de4d59afd5139847ad3195ed/app/src/store/index.ts)
- [app/src/translator/index.ts](https://github.com/coaidev/coai/blob/3048a493eedcfe75de4d59afd5139847ad3195ed/app/src/translator/index.ts)
- [app/src/utils/app.ts](https://github.com/coaidev/coai/blob/3048a493eedcfe75de4d59afd5139847ad3195ed/app/src/utils/app.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| adapter package | library | Observed | Groups 68 file(s) under adapter package (observed from repository paths and static analysis). |
| addition package | library | Observed | Groups 14 file(s) under addition package (observed from repository paths and static analysis). |
| admin package | library | Observed | Groups 16 file(s) under admin package (observed from repository paths and static analysis). |
| API layer | api | Observed | Groups 51 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 192 file(s) under app package (observed from repository paths and static analysis). |
| auth package | library | Observed | Groups 17 file(s) under auth package (observed from repository paths and static analysis). |
| channel package | library | Observed | Groups 11 file(s) under channel package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 6 file(s) under cli package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 29 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| connection package | library | Observed | Groups 4 file(s) under connection package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| globals package | library | Observed | Groups 10 file(s) under globals package (observed from repository paths and static analysis). |
| manager package | library | Observed | Groups 22 file(s) under manager package (observed from repository paths and static analysis). |
| middleware package | library | Observed | Groups 5 file(s) under middleware package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 17 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/app.yaml` (ci)
- `.github/workflows/build.yaml` (ci)
- `.github/workflows/docker-cd.yaml` (ci)
- `.github/workflows/docker-ci.yaml` (ci)
- `.github/workflows/issue-translator.yaml` (ci)
- `Dockerfile` (container)
- `app/.prettierrc.json` (config)
- `app/components.json` (config)
- `app/package.json` (manifest)
- `app/public/manifest.json` (config)
- `app/qodana.yaml` (config)
- `app/src-tauri/Cargo.toml` (manifest)
- `app/src-tauri/tauri.conf.json` (config)
- `app/src/conf/version.json` (config)
- `app/src/resources/i18n/cn.json` (config)
- `app/src/resources/i18n/en.json` (config)
- `app/src/resources/i18n/ja.json` (config)
- `app/src/resources/i18n/ru.json` (config)
- `app/src/resources/i18n/tw.json` (config)
- `app/tsconfig.json` (config)
- `app/tsconfig.node.json` (config)
- `config.example.yaml` (config)
- `docker-compose.stable.yaml` (config)
- `docker-compose.watch.yaml` (config)
- `docker-compose.yaml` (container)
- `go.mod` (manifest)
- `zeabur.yaml` (config)

## Top-level layout

- `app` — 312 analysed file(s)
- `adapter` — 68 analysed file(s)
- `manager` — 22 analysed file(s)
- `utils` — 18 analysed file(s)
- `addition` — 17 analysed file(s)
- `auth` — 17 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `admin` — 16 analysed file(s)
- `channel` — 11 analysed file(s)
- `globals` — 10 analysed file(s)
- `.github` — 9 analysed file(s)
- `cli` — 6 analysed file(s)
- `middleware` — 5 analysed file(s)
- `connection` — 4 analysed file(s)
- `migration` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3048a493eedcfe75de4d59afd5139847ad3195ed` is the revision these paths and observations refer to.
