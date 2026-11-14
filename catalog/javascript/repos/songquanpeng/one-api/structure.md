# Project structure: songquanpeng/one-api

**Analysed commit:** `8df4a2670b98266bd287c698243fff327d9748cf`

**Commit reference:** [8df4a2670b98266bd287c698243fff327d9748cf](https://github.com/songquanpeng/one-api/commit/8df4a2670b98266bd287c698243fff327d9748cf)

**Tree at this commit:** [songquanpeng/one-api@8df4a2670b98](https://github.com/songquanpeng/one-api/tree/8df4a2670b98266bd287c698243fff327d9748cf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | songquanpeng/one-api |
| Description | LLM API 管理 & 分发系统，支持 OpenAI、Azure、Anthropic Claude、Google Gemini、DeepSeek、字节豆包、ChatGLM、文心一言、讯飞星火、通义千问、360 智脑、腾讯混元等主流模型，统一 API 适配，可用于 key 管理与二次分发。单可执行文件，提供 Docker 镜像，一键部署，开箱即用。LLM API management & key redistribution system, unifying multiple providers under a single API. Single binary, Docker-ready,… |
| Stars | 37434 |
| Forks | 6889 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `8df4a2670b98266bd287c698243fff327d9748cf` |
| Retrieved at | 2026-11-14T19:10:41.792159+00:00 |
| Files in this snapshot | 552 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (5 files)
    ci.yml
    docker-image.yml
    linux-release.yml
    macos-release.yml
    windows-release.yml
  FUNDING.yml
bin/  (3 files)
  migration_v0.2-v0.3.sql
  migration_v0.3-v0.4.sql
  time_test.sh
common/  (37 files)
  blacklist/  (1 files)
    main.go
  client/  (1 files)
    init.go
  config/  (1 files)
    config.go
  conv/  (1 files)
    any.go
  ctxkey/  (1 files)
    key.go
  env/  (1 files)
    helper.go
  helper/  (3 files)
    helper.go
    key.go
    time.go
  i18n/  (3 files)
    locales/  (2 files)
      … 2 files under this directory
    i18n.go
  image/  (2 files)
    image.go
    image_test.go
  logger/  (2 files)
    constants.go
    logger.go
  message/  (4 files)
    email.go
    main.go
    message-pusher.go
    template.go
  network/  (2 files)
    ip.go
    ip_test.go
  random/  (1 files)
    main.go
  render/  (1 files)
    render.go
  utils/  (1 files)
    array.go
  constants.go
  crypto.go
  custom-event.go
  database.go
  embed-file-system.go
  gin.go
  init.go
  rate-limit.go
  redis.go
  utils.go
  validate.go
  verification.go
controller/  (17 files)
  auth/  (4 files)
    github.go
    lark.go
    oidc.go
    wechat.go
  billing.go
  channel-billing.go
  channel-test.go
  channel.go
  group.go
  log.go
  misc.go
  model.go
  option.go
  redemption.go
  relay.go
  token.go
  user.go
docs/  (1 files)
  API.md
middleware/  (12 files)
  auth.go
  cache.go
  cors.go
  distributor.go
  gzip.go
  language.go
  logger.go
  rate-limit.go
  recover.go
  request-id.go
  turnstile-check.go
  utils.go
model/  (10 files)
  ability.go
  cache.go
  channel.go
  log.go
  main.go
  option.go
  redemption.go
  token.go
  user.go
  utils.go
monitor/  (3 files)
  channel.go
  manage.go
  metric.go
relay/  (152 files)
  adaptor/  (122 files)
    ai360/  (1 files)
      … 1 files under this directory
    aiproxy/  (4 files)
      … 4 files under this directory
    ali/  (5 files)
      … 5 files under this directory
    alibailian/  (2 files)
      … 2 files under this directory
    anthropic/  (4 files)
      … 4 files under this directory
    aws/  (11 files)
      … 11 files under this directory
    baichuan/  (1 files)
      … 1 files under this directory
    baidu/  (4 files)
      … 4 files under this directory
    baiduv2/  (2 files)
      … 2 files under this directory
    cloudflare/  (4 files)
      … 4 files under this directory
    cohere/  (4 files)
      … 4 files under this directory
    coze/  (8 files)
      … 8 files under this directory
    deepl/  (5 files)
      … 5 files under this directory
    deepseek/  (1 files)
      … 1 files under this directory
    doubao/  (2 files)
      … 2 files under this directory
    gemini/  (4 files)
      … 4 files under this directory
    geminiv2/  (2 files)
      … 2 files under this directory
    groq/  (1 files)
      … 1 files under this directory
    lingyiwanwu/  (1 files)
      … 1 files under this directory
    minimax/  (2 files)
      … 2 files under this directory
    mistral/  (1 files)
      … 1 files under this directory
    moonshot/  (1 files)
      … 1 files under this directory
    novita/  (2 files)
      … 2 files under this directory
    ollama/  (4 files)
      … 4 files under this directory
    openai/  (9 files)
      … 9 files under this directory
    openrouter/  (1 files)
      … 1 files under this directory
    palm/  (4 files)
      … 4 files under this directory
    proxy/  (1 files)
      … 1 files under this directory
    replicate/  (5 files)
      … 5 files under this directory
    siliconflow/  (1 files)
      … 1 files under this directory
    stepfun/  (1 files)
      … 1 files under this directory
    tencent/  (4 files)
      … 4 files under this directory
    togetherai/  (1 files)
      … 1 files under this directory
    vertexai/  (6 files)
      … 6 files under this directory
    xai/  (1 files)
      … 1 files under this directory
    xunfei/  (5 files)
      … 5 files under this directory
    xunfeiv2/  (1 files)
      … 1 files under this directory
    zhipu/  (4 files)
      … 4 files under this directory
    common.go
    interface.go
  apitype/  (1 files)
    define.go
  billing/  (4 files)
    ratio/  (3 files)
      … 3 files under this directory
    billing.go
  channeltype/  (4 files)
    define.go
    helper.go
    url.go
    url_test.go
  constant/  (3 files)
    finishreason/  (1 files)
      … 1 files under this directory
    role/  (1 files)
      … 1 files under this directory
    common.go
  controller/  (7 files)
    validator/  (1 files)
      … 1 files under this directory
    audio.go
    error.go
    helper.go
    image.go
    proxy.go
    text.go
  meta/  (1 files)
    relay_meta.go
  model/  (6 files)
    constant.go
    general.go
    image.go
    message.go
    misc.go
    tool.go
  relaymode/  (2 files)
    define.go
    helper.go
  adaptor.go
  adaptor_test.go
router/  (5 files)
  api.go
  dashboard.go
  main.go
  relay.go
  web.go
web/  (289 files)
  air/  (64 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (58 files)
      … 58 files under this directory
    .gitignore
    README.md
    package.json
    vercel.json
  berry/  (155 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (149 files)
      … 149 files under this directory
    .gitignore
    .prettierrc
    README.md
    jsconfig.json
    package.json
  default/  (67 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (61 files)
      … 61 files under this directory
    .gitignore
    README.md
    package.json
    vercel.json
  README.md
  THEMES
  build.sh
.env.example
.gitignore
Dockerfile
LICENSE
README.en.md
README.ja.md
README.md
VERSION
docker-compose.yml
go.mod
go.sum
main.go
one-api.service
pull_request_template.md
```

## Entry points

- [web/air/src/App.js](https://github.com/songquanpeng/one-api/blob/8df4a2670b98266bd287c698243fff327d9748cf/web/air/src/App.js)
- [web/air/src/index.js](https://github.com/songquanpeng/one-api/blob/8df4a2670b98266bd287c698243fff327d9748cf/web/air/src/index.js)
- [web/berry/src/App.js](https://github.com/songquanpeng/one-api/blob/8df4a2670b98266bd287c698243fff327d9748cf/web/berry/src/App.js)
- [web/berry/src/index.js](https://github.com/songquanpeng/one-api/blob/8df4a2670b98266bd287c698243fff327d9748cf/web/berry/src/index.js)
- [web/default/src/App.js](https://github.com/songquanpeng/one-api/blob/8df4a2670b98266bd287c698243fff327d9748cf/web/default/src/App.js)
- [web/default/src/index.js](https://github.com/songquanpeng/one-api/blob/8df4a2670b98266bd287c698243fff327d9748cf/web/default/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 59 file(s) under api layer (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 33 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| controller package | library | Observed | Groups 17 file(s) under controller package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| middleware package | library | Observed | Groups 12 file(s) under middleware package (observed from repository paths and static analysis). |
| model package | library | Observed | Groups 10 file(s) under model package (observed from repository paths and static analysis). |
| monitor package | library | Observed | Groups 3 file(s) under monitor package (observed from repository paths and static analysis). |
| relay package | library | Observed | Groups 152 file(s) under relay package (observed from repository paths and static analysis). |
| router package | library | Observed | Groups 5 file(s) under router package (observed from repository paths and static analysis). |
| web package | library | Observed | Groups 184 file(s) under web package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docker-image.yml` (ci)
- `.github/workflows/linux-release.yml` (ci)
- `.github/workflows/macos-release.yml` (ci)
- `.github/workflows/windows-release.yml` (ci)
- `Dockerfile` (container)
- `common/i18n/locales/en.json` (config)
- `common/i18n/locales/zh-CN.json` (config)
- `docker-compose.yml` (container)
- `go.mod` (manifest)
- `web/air/package.json` (manifest)
- `web/air/vercel.json` (config)
- `web/berry/jsconfig.json` (config)
- `web/berry/package.json` (manifest)
- `web/default/package.json` (manifest)
- `web/default/src/locales/en/translation.json` (config)
- `web/default/src/locales/zh/translation.json` (config)
- `web/default/vercel.json` (config)

## Top-level layout

- `web` — 289 analysed file(s)
- `relay` — 152 analysed file(s)
- `common` — 37 analysed file(s)
- `controller` — 17 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `middleware` — 12 analysed file(s)
- `model` — 10 analysed file(s)
- `.github` — 9 analysed file(s)
- `router` — 5 analysed file(s)
- `bin` — 3 analysed file(s)
- `monitor` — 3 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8df4a2670b98266bd287c698243fff327d9748cf` is the revision these paths and observations refer to.
