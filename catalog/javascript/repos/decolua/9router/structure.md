# Project structure: decolua/9router

**Analysed commit:** `1855aa44473e88feac9d3f131b9c0c5fc9706b68`

**Commit reference:** [1855aa44473e88feac9d3f131b9c0c5fc9706b68](https://github.com/decolua/9router/commit/1855aa44473e88feac9d3f131b9c0c5fc9706b68)

**Tree at this commit:** [decolua/9router@1855aa44473e](https://github.com/decolua/9router/tree/1855aa44473e88feac9d3f131b9c0c5fc9706b68)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | decolua/9router |
| Description | Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini via 40+ providers. Auto-fallback, RTK -40% tokens, never hit limits. |
| Stars | 32433 |
| Forks | 6350 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `1855aa44473e88feac9d3f131b9c0c5fc9706b68` |
| Retrieved at | 2026-11-14T19:10:45.581515+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (3 files)
    docker-publish.yml
    gitbook-pages.yml
    tray-binaries.yml
  dependabot.yml
.vscode/  (1 files)
  settings.json
cli/  (36 files)
  hooks/  (3 files)
    postinstall.js
    sqliteRuntime.js
    trayRuntime.js
  scripts/  (3 files)
    build-cli.js
    buildMitm.js
    buildTrayArm64.js
  src/  (24 files)
    cli/  (24 files)
      … 24 files under this directory
  .gitignore
  .npmignore
  LICENSE
  README.md
  cli.js
  package.json
docs/  (6 files)
  superpowers/  (4 files)
    plans/  (2 files)
      … 2 files under this directory
    specs/  (2 files)
      … 2 files under this directory
  ARCHITECTURE.md
  CODEX_STT.md
gitbook/  (120 files)
  app/  (5 files)
    [lang]/  (2 files)
      … 2 files under this directory
    globals.css
    layout.js
    page.js
  components/  (6 files)
    DocsContent.js
    DocsHeader.js
    DocsLayout.js
    DocsSidebar.js
    DocsToc.js
    LanguageSwitcher.js
  constants/  (2 files)
    docsConfig.js
    languages.js
  content/  (100 files)
    en/  (20 files)
      … 20 files under this directory
    es/  (20 files)
      … 20 files under this directory
    ja/  (20 files)
      … 20 files under this directory
    vi/  (20 files)
      … 20 files under this directory
    zh-CN/  (20 files)
      … 20 files under this directory
  lib/  (1 files)
    content.js
  utils/  (1 files)
    markdown.js
  .gitignore
  jsconfig.json
  next.config.mjs
  package.json
  postcss.config.mjs
i18n/  (10 files)
  README.es.md
  README.fa_IR.md
  README.fr.md
  README.id-ID.md
  README.ja-JP.md
  README.pt-BR.md
  README.ru.md
  README.th.md
  README.vi.md
  README.zh-CN.md
open-sse/  (501 files)
  config/  (16 files)
    appConstants.js
    awsConstants.js
    codexInstructions.js
    constants.js
    defaultThinkingSignature.js
    errorConfig.js
    googleTtsLanguages.js
    grokCli.js
    kiroConstants.js
    mediaConfig.js
    models.js
    ollamaModels.js
    providerModels.js
    providers.js
    runtimeConfig.js
    ttsModels.js
  executors/  (63 files)
    chatgpt-web/  (10 files)
      … 10 files under this directory
    deepseek-web/  (2 files)
      … 2 files under this directory
    gemini-web/  (5 files)
      … 5 files under this directory
    muse-web/  (3 files)
      … 3 files under this directory
    antigravity.js
    azure.js
    base.js
    bedrock.js
    browserExecutableCheck.js
    chatgpt-web.js
    chatgptWebTools.js
    codebuddy-cn.js
    codebuddy-intl.js
    codex.js
    commandcode.js
    cursor.js
    deepseek-web-done-terminator.js
    deepseek-web.js
    default.js
    devin-cli.js
    gemini-cli.js
    gemini-web.js
    github.js
    grok-cli.js
    grok-web-tools.js
    grok-web.js
    iflow.js
    index.js
    … 19 more files
  handlers/  (66 files)
    chatCore/  (4 files)
      … 4 files under this directory
    embeddingProviders/  (8 files)
      … 8 files under this directory
    fetch/  (1 files)
      … 1 files under this directory
    imageProviders/  (21 files)
      … 21 files under this directory
    search/  (4 files)
      … 4 files under this directory
    ttsProviders/  (14 files)
      … 14 files under this directory
    videoProviders/  (3 files)
      … 3 files under this directory
    chatCore.js
    codexStt.js
    codexSttAudio.js
    embeddingsCore.js
    geminiLiveStt.js
    imageGenerationCore.js
    responsesHandler.js
    sttCore.js
    systemoneCore.js
    ttsCore.js
    videoCore.js
  lib/  (3 files)
    deepseek-pow-hash.js
    deepseek-pow-worker.mjs
    deepseek-pow.js
  providers/  (161 files)
    models/  (3 files)
      … 3 files under this directory
    registry/  (149 files)
      … 149 files under this directory
    REGISTRY_TEMPLATE.js
    capabilities.js
    catalogOverride.js
    index.js
    pricing.js
    schema.js
    shared.js
    thinkingLevels.js
    visionPatterns.js
  rtk/  (25 files)
    filters/  (12 files)
      … 12 files under this directory
    applyFilter.js
    autodetect.js
    caveman.js
    cavemanPrompts.js
    constants.js
    customPrompt.js
    headroom.js
    index.js
    ponytail.js
    ponytailPrompt.js
    pxpipe.js
    registry.js
    systemInject.js
  services/  (60 files)
    tokenRefresh/  (2 files)
      … 2 files under this directory
    usage/  (24 files)
      … 24 files under this directory
    accountFallback.js
    browserPool.js
    browserProfileCache.js
    capacityAdapter.js
    clinepassModels.js
    combo.js
    commandcodeModels.js
    compact.js
    copilotModels.js
    cursorModels.js
    emptyFailover.js
    grokCliModels.js
    grokTlsClient.js
    kimchiModels.js
    kiroModels.js
    lazyRuntime.js
    minimaxCodeLease.js
    minimaxCodeUsage.js
    model.js
    nous.js
    oauthCredentialManager.js
    obscura.js
    opencodeTlsClient.js
    projectId.js
    … 10 more files
  shared/  (14 files)
    qoder/  (7 files)
      … 7 files under this directory
    awsCredentials.js
    clineAuth.js
    clineEnvelope.js
    commandCodeHeaders.js
    machineId.js
    mimoAccount.js
    zedAuth.js
  transformer/  (2 files)
    responsesTransformer.js
    streamToJsonConverter.js
  translator/  (53 files)
    concerns/  (15 files)
      … 15 files under this directory
    formats/  (5 files)
      … 5 files under this directory
    request/  (12 files)
      … 12 files under this directory
    response/  (10 files)
      … 10 files under this directory
    schema/  (6 files)
      … 6 files under this directory
    deepseekWebToolBinding.js
    deepseekWebTools.js
    formats.js
    index.js
    webTools.js
  utils/  (35 files)
    awsEventStream.js
    awsSigv4.js
    bypassHandler.js
    claudeCliVersion.js
    claudeCloaking.js
    claudeSignature.js
    claudeToolTypeSelfCheck.mjs
    clientDetector.js
    codexToolSchema.js
    cursorChecksum.js
    cursorProtobuf.js
    debugLog.js
    error.js
    geminiCookies.js
    kiroSessionReplay.js
    modelMarkers.js
    ollamaTransform.js
    opencodeFingerprint.js
    proxyFetch.js
    reasoningContentInjector.js
    requestLogger.js
    responsesStreamHelpers.js
    sessionManager.js
    sse.js
    … 11 more files
  .npmignore
  AGENTS.md
  index.js
public/  (47 files)
  i18n/  (34 files)
    literals/  (34 files)
      … 34 files under this directory
  icons/  (2 files)
    icon-192.svg
    icon-512.svg
  providers/  (4 files)
    codewhale.svg
    kimchi.svg
    pi.svg
    smelt.svg
  favicon.svg
  file.svg
  globe.svg
  next.svg
  sw.js
  vercel.svg
  window.svg
scripts/  (5 files)
  copy-standalone-assets.mjs
  injectDisplayToRegistry.mjs
  migrate-registry.mjs
  test-combo-autoswitch.mjs
  translate-readme.js
skills/  (10 files)
  9router/  (1 files)
    SKILL.md
  9router-chat/  (1 files)
    SKILL.md
  9router-embeddings/  (1 files)
    SKILL.md
  9router-image/  (1 files)
    SKILL.md
  9router-stt/  (1 files)
    SKILL.md
  9router-tts/  (1 files)
    SKILL.md
  9router-video/  (1 files)
    SKILL.md
  9router-web-fetch/  (1 files)
    SKILL.md
  9router-web-search/  (1 files)
    SKILL.md
  README.md
src/  (40 files)
  app/  (40 files)
    (dashboard)/  (40 files)
      … 40 files under this directory
.dockerignore
.env.example
.gitignore
.npmignore
.nvmrc
CHANGELOG.md
CLAUDE.md
DOCKER.md
Dockerfile
LICENSE
README.md
README.zh-CN.md
captain-definition
custom-server.js
docker-compose.yml
eslint.config.mjs
jsconfig.json
next.config.mjs
package.json
postcss.config.mjs
```

## Entry points

- [cli/cli.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/cli/cli.js)
- [gitbook/app/[lang]/page.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/gitbook/app/%5Blang%5D/page.js)
- [gitbook/app/page.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/gitbook/app/page.js)
- [open-sse/executors/index.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/open-sse/executors/index.js)
- [open-sse/handlers/embeddingProviders/index.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/open-sse/handlers/embeddingProviders/index.js)
- [open-sse/handlers/fetch/index.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/open-sse/handlers/fetch/index.js)
- [open-sse/handlers/imageProviders/index.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/open-sse/handlers/imageProviders/index.js)
- [open-sse/handlers/search/index.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/open-sse/handlers/search/index.js)
- [open-sse/handlers/ttsProviders/index.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/open-sse/handlers/ttsProviders/index.js)
- [open-sse/handlers/videoProviders/index.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/open-sse/handlers/videoProviders/index.js)
- [open-sse/index.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/open-sse/index.js)
- [open-sse/providers/index.js](https://github.com/decolua/9router/blob/1855aa44473e88feac9d3f131b9c0c5fc9706b68/open-sse/providers/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 67 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 40 file(s) under app package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 29 file(s) under cli package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 57 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| gitbook package | library | Observed | Groups 16 file(s) under gitbook package (observed from repository paths and static analysis). |
| open-sse package | library | Observed | Groups 354 file(s) under open-sse package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 60 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/docker-publish.yml` (ci)
- `.github/workflows/gitbook-pages.yml` (ci)
- `.github/workflows/tray-binaries.yml` (ci)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `cli/package.json` (manifest)
- `docker-compose.yml` (container)
- `gitbook/jsconfig.json` (config)
- `gitbook/package.json` (manifest)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `public/i18n/literals/ar.json` (config)
- `public/i18n/literals/bn.json` (config)
- `public/i18n/literals/cs.json` (config)
- `public/i18n/literals/da.json` (config)
- `public/i18n/literals/de.json` (config)
- `public/i18n/literals/el.json` (config)
- `public/i18n/literals/es.json` (config)
- `public/i18n/literals/fa.json` (config)
- `public/i18n/literals/fi.json` (config)
- `public/i18n/literals/fr.json` (config)
- `public/i18n/literals/he.json` (config)
- `public/i18n/literals/hi.json` (config)
- `public/i18n/literals/hu.json` (config)
- `public/i18n/literals/id.json` (config)
- `public/i18n/literals/it.json` (config)
- `public/i18n/literals/ja.json` (config)
- `public/i18n/literals/km.json` (config)
- `public/i18n/literals/ko.json` (config)
- `public/i18n/literals/nl.json` (config)
- `public/i18n/literals/no.json` (config)
- `public/i18n/literals/pl.json` (config)
- `public/i18n/literals/pt-BR.json` (config)
- `public/i18n/literals/pt-PT.json` (config)
- `public/i18n/literals/ro.json` (config)
- `public/i18n/literals/ru.json` (config)
- `public/i18n/literals/sv.json` (config)
- `public/i18n/literals/th.json` (config)
- `public/i18n/literals/tl.json` (config)
- `public/i18n/literals/tr.json` (config)
- `public/i18n/literals/uk.json` (config)
- `public/i18n/literals/ur.json` (config)
- `public/i18n/literals/vi.json` (config)
- `public/i18n/literals/zh-CN.json` (config)
- `public/i18n/literals/zh-TW.json` (config)

## Top-level layout

- `open-sse` — 501 analysed file(s)
- `gitbook` — 120 analysed file(s)
- `public` — 47 analysed file(s)
- `src` — 40 analysed file(s)
- `cli` — 36 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `i18n` — 10 analysed file(s)
- `skills` — 10 analysed file(s)
- `docs` — 6 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1855aa44473e88feac9d3f131b9c0c5fc9706b68` is the revision these paths and observations refer to.
