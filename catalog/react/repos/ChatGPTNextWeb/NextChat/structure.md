# Project structure: ChatGPTNextWeb/NextChat

**Analysed commit:** `1d3dc331512929a4b1d3e82354e72acce33b5c7a`

**Commit reference:** [1d3dc331512929a4b1d3e82354e72acce33b5c7a](https://github.com/ChatGPTNextWeb/NextChat/commit/1d3dc331512929a4b1d3e82354e72acce33b5c7a)

**Tree at this commit:** [ChatGPTNextWeb/NextChat@1d3dc3315129](https://github.com/ChatGPTNextWeb/NextChat/tree/1d3dc331512929a4b1d3e82354e72acce33b5c7a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ChatGPTNextWeb/NextChat |
| Description | ✨ Zero-config AI chat assistant. No API key needed — sign up and instantly chat with GPT-5, Claude 4, Gemini 2.5, DeepSeek & 100+ top models. Pay-as-you-go saves you more. Available on Web, iOS, macOS, Android, Linux, Windows. |
| Stars | 88962 |
| Forks | 58526 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `1d3dc331512929a4b1d3e82354e72acce33b5c7a` |
| Retrieved at | 2026-11-14T19:12:57.063275+00:00 |
| Files in this snapshot | 370 |

## Directory tree

```text
.github/  (13 files)
  ISSUE_TEMPLATE/  (4 files)
    1_bug_report.yml
    1_bug_report_cn.yml
    2_feature_request.yml
    2_feature_request_cn.yml
  workflows/  (7 files)
    app.yml
    deploy_preview.yml
    docker.yml
    issue-translator.yml
    remove_deploy_preview.yml
    sync.yml
    test.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.husky/  (1 files)
  pre-commit
app/  (256 files)
  api/  (24 files)
    [provider]/  (1 files)
      … 1 files under this directory
    artifacts/  (1 files)
      … 1 files under this directory
    config/  (1 files)
      … 1 files under this directory
    tencent/  (1 files)
      … 1 files under this directory
    upstash/  (1 files)
      … 1 files under this directory
    webdav/  (1 files)
      … 1 files under this directory
    302ai.ts
    alibaba.ts
    anthropic.ts
    auth.ts
    azure.ts
    baidu.ts
    bytedance.ts
    common.ts
    deepseek.ts
    glm.ts
    google.ts
    iflytek.ts
    moonshot.ts
    openai.ts
    proxy.ts
    siliconflow.ts
    stability.ts
    xai.ts
  client/  (16 files)
    platforms/  (14 files)
      … 14 files under this directory
    api.ts
    controller.ts
  components/  (51 files)
    realtime-chat/  (4 files)
      … 4 files under this directory
    sd/  (6 files)
      … 6 files under this directory
    voice-print/  (3 files)
      … 3 files under this directory
    artifacts.module.scss
    artifacts.tsx
    auth.module.scss
    auth.tsx
    button.module.scss
    button.tsx
    chat-list.tsx
    chat.module.scss
    chat.tsx
    emoji.tsx
    error.tsx
    exporter.module.scss
    exporter.tsx
    home.module.scss
    home.tsx
    input-range.module.scss
    input-range.tsx
    markdown.tsx
    mask.module.scss
    mask.tsx
    mcp-market.module.scss
    mcp-market.tsx
    message-selector.module.scss
    message-selector.tsx
    … 14 more files
  config/  (3 files)
    build.ts
    client.ts
    server.ts
  icons/  (83 files)
    llm-icons/  (13 files)
      … 13 files under this directory
    add.svg
    arrow.svg
    auto.svg
    bottom.svg
    brain.svg
    break.svg
    cancel.svg
    chat-settings.svg
    chat.svg
    clear.svg
    close.svg
    cloud-fail.svg
    cloud-success.svg
    config.svg
    confirm.svg
    connection.svg
    copy.svg
    dark.svg
    delete.svg
    discovery.svg
    down.svg
    download.svg
    drag.svg
    edit.svg
    … 46 more files
  lib/  (1 files)
    audio.ts
  locales/  (21 files)
    ar.ts
    bn.ts
    cn.ts
    cs.ts
    da.ts
    de.ts
    en.ts
    es.ts
    fr.ts
    id.ts
    index.ts
    it.ts
    jp.ts
    ko.ts
    no.ts
    pt.ts
    ru.ts
    sk.ts
    tr.ts
    tw.ts
    vi.ts
  masks/  (6 files)
    build.ts
    cn.ts
    en.ts
    index.ts
    tw.ts
    typing.ts
  mcp/  (6 files)
    actions.ts
    client.ts
    logger.ts
    mcp_config.default.json
    types.ts
    utils.ts
  store/  (10 files)
    access.ts
    chat.ts
    config.ts
    index.ts
    mask.ts
    plugin.ts
    prompt.ts
    sd.ts
    sync.ts
    update.ts
  styles/  (5 files)
    animation.scss
    globals.scss
    highlight.scss
    markdown.scss
    window.scss
  utils/  (22 files)
    cloud/  (3 files)
      … 3 files under this directory
    audio.ts
    auth-settings-events.ts
    baidu.ts
    chat.ts
    clone.ts
    cloudflare.ts
    format.ts
    hmac.ts
    hooks.ts
    indexedDB-storage.ts
    merge.ts
    model.ts
    ms_edge_tts.ts
    object.ts
    store.ts
    stream.ts
    sync.ts
    tencent.ts
    token.ts
  command.ts
  constant.ts
  global.d.ts
  layout.tsx
  page.tsx
  polyfill.ts
  typing.ts
  utils.ts
docs/  (23 files)
  images/  (1 files)
    icon.svg
  bt-cn.md
  cloudflare-pages-cn.md
  cloudflare-pages-en.md
  cloudflare-pages-es.md
  cloudflare-pages-ja.md
  cloudflare-pages-ko.md
  faq-cn.md
  faq-en.md
  faq-es.md
  faq-ja.md
  faq-ko.md
  synchronise-chat-logs-cn.md
  synchronise-chat-logs-en.md
  synchronise-chat-logs-es.md
  synchronise-chat-logs-ja.md
  synchronise-chat-logs-ko.md
  translation.md
  user-manual-cn.md
  vercel-cn.md
  vercel-es.md
  vercel-ja.md
  vercel-ko.md
public/  (6 files)
  audio-processor.js
  plugins.json
  robots.txt
  serviceWorker.js
  serviceWorkerRegister.js
  site.webmanifest
scripts/  (6 files)
  .gitignore
  delete-deployment-preview.sh
  fetch-prompts.mjs
  init-proxy.sh
  proxychains.template.conf
  setup.sh
src-tauri/  (6 files)
  src/  (2 files)
    main.rs
    stream.rs
  .gitignore
  Cargo.toml
  build.rs
  tauri.conf.json
test/  (36 files)
  adapter.test.ts
  chat-command-prefix.test.ts
  cloudflare.test.ts
  collect-model-table.test.ts
  collect-model-with-default.test.ts
  create-message.test.ts
  estimate-token-length.test.ts
  extract-mcp-json.test.ts
  format-chunks.test.ts
  format.test.ts
  get-bearer-token.test.ts
  get-client-config.test.ts
  get-operation-id.test.ts
  hmac-hash.test.ts
  hmac-hex.test.ts
  hmac-sign.test.ts
  is-gpt4-model.test.ts
  is-mcp-json.test.ts
  limit-number.test.ts
  mcp-actions-require-enabled.test.ts
  mcp-client-environment.test.ts
  merge.test.ts
  modal-config-validator.test.ts
  model-available-in-server.test.ts
  … 12 more files
.babelrc
.dockerignore
.env.template
.eslintignore
.eslintrc.json
.gitignore
.gitpod.yml
.lintstagedrc.json
.prettierrc.js
CODE_OF_CONDUCT.md
Dockerfile
LICENSE
README.md
README_CN.md
README_JA.md
README_KO.md
docker-compose.yml
jest.config.ts
jest.setup.ts
next.config.mjs
package.json
tsconfig.json
vercel.json
```

## Entry points

- [app/components/realtime-chat/index.ts](https://github.com/ChatGPTNextWeb/NextChat/blob/1d3dc331512929a4b1d3e82354e72acce33b5c7a/app/components/realtime-chat/index.ts)
- [app/components/sd/index.tsx](https://github.com/ChatGPTNextWeb/NextChat/blob/1d3dc331512929a4b1d3e82354e72acce33b5c7a/app/components/sd/index.tsx)
- [app/components/voice-print/index.ts](https://github.com/ChatGPTNextWeb/NextChat/blob/1d3dc331512929a4b1d3e82354e72acce33b5c7a/app/components/voice-print/index.ts)
- [app/config/server.ts](https://github.com/ChatGPTNextWeb/NextChat/blob/1d3dc331512929a4b1d3e82354e72acce33b5c7a/app/config/server.ts)
- [app/locales/index.ts](https://github.com/ChatGPTNextWeb/NextChat/blob/1d3dc331512929a4b1d3e82354e72acce33b5c7a/app/locales/index.ts)
- [app/masks/index.ts](https://github.com/ChatGPTNextWeb/NextChat/blob/1d3dc331512929a4b1d3e82354e72acce33b5c7a/app/masks/index.ts)
- [app/page.tsx](https://github.com/ChatGPTNextWeb/NextChat/blob/1d3dc331512929a4b1d3e82354e72acce33b5c7a/app/page.tsx)
- [app/store/index.ts](https://github.com/ChatGPTNextWeb/NextChat/blob/1d3dc331512929a4b1d3e82354e72acce33b5c7a/app/store/index.ts)
- [app/utils/cloud/index.ts](https://github.com/ChatGPTNextWeb/NextChat/blob/1d3dc331512929a4b1d3e82354e72acce33b5c7a/app/utils/cloud/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 24 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 104 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 16 file(s) under external integrations (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 3 file(s) under public package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| src-tauri package | library | Observed | Groups 3 file(s) under src-tauri package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 36 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.template` (config)
- `.eslintrc.json` (config)
- `.github/ISSUE_TEMPLATE/1_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/1_bug_report_cn.yml` (config)
- `.github/ISSUE_TEMPLATE/2_feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/2_feature_request_cn.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/app.yml` (ci)
- `.github/workflows/deploy_preview.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/issue-translator.yml` (ci)
- `.github/workflows/remove_deploy_preview.yml` (ci)
- `.github/workflows/sync.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.gitpod.yml` (config)
- `.lintstagedrc.json` (config)
- `Dockerfile` (container)
- `app/mcp/mcp_config.default.json` (config)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `public/plugins.json` (config)
- `src-tauri/Cargo.toml` (manifest)
- `src-tauri/tauri.conf.json` (config)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `app` — 256 analysed file(s)
- `test` — 36 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `docs` — 23 analysed file(s)
- `.github` — 13 analysed file(s)
- `public` — 6 analysed file(s)
- `scripts` — 6 analysed file(s)
- `src-tauri` — 6 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1d3dc331512929a4b1d3e82354e72acce33b5c7a` is the revision these paths and observations refer to.
