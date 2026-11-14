# Project structure: fishjar/kiss-translator

**Analysed commit:** `9dba2e86d524a8ec85f56bc08ef645a555707bdc`

**Commit reference:** [9dba2e86d524a8ec85f56bc08ef645a555707bdc](https://github.com/fishjar/kiss-translator/commit/9dba2e86d524a8ec85f56bc08ef645a555707bdc)

**Tree at this commit:** [fishjar/kiss-translator@9dba2e86d524](https://github.com/fishjar/kiss-translator/tree/9dba2e86d524a8ec85f56bc08ef645a555707bdc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fishjar/kiss-translator |
| Description | A simple, open source bilingual translation extension & Greasemonkey script (一个简约、开源的 双语对照翻译扩展 & 油猴脚本) |
| Stars | 13337 |
| Forks | 684 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | dev |
| Analysed commit | `9dba2e86d524a8ec85f56bc08ef645a555707bdc` |
| Retrieved at | 2026-11-14T19:11:57.693772+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.agents/  (2 files)
  skills/  (2 files)
    release-kiss-translator/  (2 files)
      … 2 files under this directory
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    deploy-web.yml
    release.yml
docs/  (2 files)
  README.md
  prompt-template-contract.md
public/  (48 files)
  _locales/  (11 files)
    de/  (1 files)
      … 1 files under this directory
    en/  (1 files)
      … 1 files under this directory
    es/  (1 files)
      … 1 files under this directory
    fr/  (1 files)
      … 1 files under this directory
    ja/  (1 files)
      … 1 files under this directory
    ko/  (1 files)
      … 1 files under this directory
    ru/  (1 files)
      … 1 files under this directory
    tr/  (1 files)
      … 1 files under this directory
    vi/  (1 files)
      … 1 files under this directory
    zh_CN/  (1 files)
      … 1 files under this directory
    zh_TW/  (1 files)
      … 1 files under this directory
  api/  (27 files)
    APIMart.svg
    AliyunBailian.svg
    AzureAI.svg
    Baidu.svg
    BuiltinAI.svg
    Cerebras.svg
    Claude.svg
    CloudflareAI.svg
    DeepL.svg
    DeepSeek.svg
    Gemini.svg
    Google.svg
    GoogleCloud.svg
    Microsoft.svg
    Ollama.svg
    OpenAI.svg
    OpenCodeGo.svg
    OpenRouter.svg
    OrcaRouter.svg
    QwenMT.svg
    Requesty.svg
    SiliconFlow.svg
    Tencent.svg
    Volcengine.svg
    … 3 more files
  .nojekyll
  404.html
  content.html
  file-translate.html
  index.html
  manifest.firefox.json
  manifest.json
  manifest.thunderbird.json
  robots.txt
  sitemap.xml
src/  (724 files)
  apis/  (26 files)
    baidu.js
    deepl.js
    deepl.test.js
    history.js
    history.test.js
    index.batchCancellation.test.js
    index.dictCache.test.js
    index.js
    index.openaiXml.test.js
    index.test.js
    opencode.js
    trans.batchLine.test.js
    trans.deepl.test.js
    trans.dict.test.js
    trans.explicitPrompts.test.js
    trans.js
    trans.localai.test.js
    trans.opencode.test.js
    trans.orcarouter.test.js
    trans.poolCancellation.test.js
    trans.requesty.test.js
    trans.subtitle.test.js
    trans.translate.test.js
    vision.js
    … 2 more files
  builtin-plugins/  (52 files)
    fixtures/  (2 files)
      … 2 files under this directory
    baidu.js
    capabilities.js
    capabilities.test.js
    chat.js
    chat.test.js
    claude.js
    cloudflare.js
    credentials.js
    deepl-free.js
    deepl.js
    definitions.js
    discovery.js
    emptyMessages.test.js
    fields.js
    fields.test.js
    gemini.js
    google.js
    index.js
    languageMappings.js
    local-asr-runtime.js
    local-asr-runtime.test.js
    local.js
    local.test.js
    messages.js
    … 26 more files
  components/  (23 files)
    Logo/  (2 files)
      … 2 files under this directory
    TranslationPanel/  (9 files)
      … 9 files under this directory
    ApiProviderIcon.js
    ApiProviderIcon.test.js
    ExtensionLocalServiceNotice.js
    FloatingButton.js
    FloatingButton.styles.js
    LocalServiceNotice.js
    LocalServiceNotice.test.js
    TerminologySelect.js
    TextareaResizeGrip.js
    TextareaResizeGrip.test.js
    TouchTranslateControl.js
    TouchTranslateControl.test.js
  config/  (47 files)
    locales/  (13 files)
      … 13 files under this directory
    api.js
    api.test.js
    apiConstants.js
    app.js
    client.js
    defaultServices.js
    defaultServices.test.js
    fab.js
    fileTranslationSites.json
    i18n.popup.js
    i18n.ru.js
    i18n.ruleEditor.js
    i18n.test.js
    i18n.touch.js
    index.js
    localModelTasks.json
    localModelTasks.test.js
    msg.js
    prompt.js
    prompt.test.js
    quotes.js
    rules.js
    serviceSelection.js
    serviceSelection.test.js
    … 10 more files
  fileTranslation/  (16 files)
    backend.js
    backend.test.js
    bridgeRecovery.js
    bridgeRecovery.test.js
    client.js
    client.test.js
    imageLayout.js
    imageLayout.test.js
    onlineFile.js
    pipelineCore.js
    pipelineCore.test.js
    pluginTranslation.integration.test.js
    protocol.js
    recognition.js
    recognition.test.js
    resultCache.js
  homepage/  (6 files)
    App.js
    App.test.js
    content.js
    content.test.js
    theme.js
    useHomepageSettings.js
  hooks/  (70 files)
    Alert.js
    Alert.test.js
    Api.js
    Api.test.js
    Audio.js
    ColorMode.js
    Commands.js
    Commands.test.js
    Confirm.js
    CustomStyles.js
    CustomStyles.test.js
    DebouncedCallback.js
    Fab.js
    FavWords.js
    FavWords.reducers.test.js
    Fetch.js
    Fetch.test.js
    I18n.js
    I18n.test.js
    InputRule.js
    Loading.js
    M2Theme.js
    M2Theme.test.js
    M3Theme.js
    … 46 more files
  injectors/  (7 files)
    index.js
    shadowroot.js
    xmlhttp.js
    youtubeAudioBridge.js
    youtubeAudioBridge.test.js
    youtubeBridge.js
    youtubeBridge.test.js
  libs/  (236 files)
    __fixtures__/  (1 files)
      … 1 files under this directory
    diagnostics/  (20 files)
      … 20 files under this directory
    document/  (3 files)
      … 3 files under this directory
    epub/  (7 files)
      … 7 files under this directory
    imageTranslate/  (13 files)
      … 13 files under this directory
    pdf/  (11 files)
      … 11 files under this directory
    stubs/  (3 files)
      … 3 files under this directory
    aiDictionary.js
    aiDictionary.test.js
    aiResponseParser.js
    aiResponseParser.test.js
    apiSelection.js
    apiSelection.test.js
    batchQueue.cancellation.test.js
    batchQueue.js
    batchQueue.test.js
    blacklist.js
    blacklistStartup.js
    blacklistStartup.test.js
    browser.js
    builtinAI.js
    builtinAI.test.js
    cache.js
    cache.test.js
    cacheDigest.js
    cacheDigest.test.js
    client.js
    clipboard.js
    clipboard.test.js
    customElementsContainer.test.js
    detect.js
    … 154 more files
  localAi/  (121 files)
    assets/  (1 files)
      … 1 files under this directory
    core/  (97 files)
      … 97 files under this directory
    runtime/  (7 files)
      … 7 files under this directory
    stubs/  (1 files)
      … 1 files under this directory
    types/  (2 files)
      … 2 files under this directory
    workers/  (8 files)
      … 8 files under this directory
    fileOperations.ts
    offscreen.ts
    paddleBuild.ts
    patchOpencvCsp.ts
    serviceModelOptions.test.ts
  providers/  (104 files)
    sdk/  (22 files)
      … 22 files under this directory
    testSupport/  (1 files)
      … 1 files under this directory
    asrLimits.js
    asrWords.js
    asrWords.test.js
    assetPackets.js
    assetPackets.test.js
    audioAsset.js
    audioAsset.test.js
    audioTransport.test.js
    background.js
    background.test.js
    backgroundInvocation.js
    backgroundInvocation.test.js
    bridge.js
    bridgeInvocation.js
    cache.js
    cache.test.js
    capabilities.js
    capabilityLabels.js
    compatibility.js
    compatibility.test.js
    contracts.ts
    declarative.js
    declarative.test.js
    declarativeIntegration.test.js
    … 57 more files
  background.imageTranslate.test.js
  background.js
  background.options.test.js
  background.separateWindow.test.js
  common.blacklistStartup.test.js
  common.js
  common.test.js
  content.js
  fileBridge.js
  fileBridge.test.js
  fileTranslate.js
  index.js
  injector-shadowroot.js
  injector-subtitle.js
  options.js
  popup.js
.babelrc
.gitattributes
.gitignore
.pnpm-version
.prettierignore
.prettierrc
CHANGELOG.md
LICENSE
README.en.md
README.ja.md
README.ko.md
README.md
VERSION_MANAGEMENT.md
config-overrides.js
custom-api.md
custom-api_v2.md
dev-server-check.log
package.json
pnpm-workspace.yaml
```

## Entry points

- [src/apis/index.js](https://github.com/fishjar/kiss-translator/blob/9dba2e86d524a8ec85f56bc08ef645a555707bdc/src/apis/index.js)
- [src/builtin-plugins/index.js](https://github.com/fishjar/kiss-translator/blob/9dba2e86d524a8ec85f56bc08ef645a555707bdc/src/builtin-plugins/index.js)
- [src/components/Logo/index.js](https://github.com/fishjar/kiss-translator/blob/9dba2e86d524a8ec85f56bc08ef645a555707bdc/src/components/Logo/index.js)
- [src/config/app.js](https://github.com/fishjar/kiss-translator/blob/9dba2e86d524a8ec85f56bc08ef645a555707bdc/src/config/app.js)
- [src/config/index.js](https://github.com/fishjar/kiss-translator/blob/9dba2e86d524a8ec85f56bc08ef645a555707bdc/src/config/index.js)
- [src/homepage/App.js](https://github.com/fishjar/kiss-translator/blob/9dba2e86d524a8ec85f56bc08ef645a555707bdc/src/homepage/App.js)
- [src/index.js](https://github.com/fishjar/kiss-translator/blob/9dba2e86d524a8ec85f56bc08ef645a555707bdc/src/index.js)
- [src/injectors/index.js](https://github.com/fishjar/kiss-translator/blob/9dba2e86d524a8ec85f56bc08ef645a555707bdc/src/injectors/index.js)
- [src/providers/sdk/index.js](https://github.com/fishjar/kiss-translator/blob/9dba2e86d524a8ec85f56bc08ef645a555707bdc/src/providers/sdk/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apis package | library | Observed | Groups 26 file(s) under apis package (observed from repository paths and static analysis). |
| background.imageTranslate.test.js package | library | Observed | Groups 1 file(s) under background.imagetranslate.test.js package (observed from repository paths and static analysis). |
| background.js package | library | Observed | Groups 1 file(s) under background.js package (observed from repository paths and static analysis). |
| background.options.test.js package | library | Observed | Groups 1 file(s) under background.options.test.js package (observed from repository paths and static analysis). |
| background.separateWindow.test.js package | library | Observed | Groups 1 file(s) under background.separatewindow.test.js package (observed from repository paths and static analysis). |
| builtin-plugins package | library | Observed | Groups 50 file(s) under builtin-plugins package (observed from repository paths and static analysis). |
| common.blacklistStartup.test.js package | library | Observed | Groups 1 file(s) under common.blackliststartup.test.js package (observed from repository paths and static analysis). |
| common.js package | library | Observed | Groups 1 file(s) under common.js package (observed from repository paths and static analysis). |
| common.test.js package | library | Observed | Groups 1 file(s) under common.test.js package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 23 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 74 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| content.js package | library | Observed | Groups 1 file(s) under content.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| fileBridge.js package | library | Observed | Groups 1 file(s) under filebridge.js package (observed from repository paths and static analysis). |
| fileBridge.test.js package | library | Observed | Groups 1 file(s) under filebridge.test.js package (observed from repository paths and static analysis). |
| fileTranslate.js package | library | Observed | Groups 1 file(s) under filetranslate.js package (observed from repository paths and static analysis). |
| fileTranslation package | library | Observed | Groups 16 file(s) under filetranslation package (observed from repository paths and static analysis). |
| homepage package | library | Observed | Groups 6 file(s) under homepage package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 70 file(s) under hooks package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| injector-shadowroot.js package | library | Observed | Groups 1 file(s) under injector-shadowroot.js package (observed from repository paths and static analysis). |
| injector-subtitle.js package | library | Observed | Groups 1 file(s) under injector-subtitle.js package (observed from repository paths and static analysis). |
| injectors package | library | Observed | Groups 7 file(s) under injectors package (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 236 file(s) under libs package (observed from repository paths and static analysis). |
| localAi package | library | Observed | Groups 23 file(s) under localai package (observed from repository paths and static analysis). |
| options.js package | library | Observed | Groups 1 file(s) under options.js package (observed from repository paths and static analysis). |
| popup.js package | library | Observed | Groups 1 file(s) under popup.js package (observed from repository paths and static analysis). |
| providers package | library | Observed | Groups 101 file(s) under providers package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 91 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.agents/skills/release-kiss-translator/agents/openai.yaml` (config)
- `.github/workflows/deploy-web.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `public/_locales/de/messages.json` (config)
- `public/_locales/en/messages.json` (config)
- `public/_locales/es/messages.json` (config)
- `public/_locales/fr/messages.json` (config)
- `public/_locales/ja/messages.json` (config)
- `public/_locales/ko/messages.json` (config)
- `public/_locales/ru/messages.json` (config)
- `public/_locales/tr/messages.json` (config)
- `public/_locales/vi/messages.json` (config)
- `public/_locales/zh_CN/messages.json` (config)
- `public/_locales/zh_TW/messages.json` (config)
- `public/manifest.firefox.json` (config)
- `public/manifest.json` (config)
- `public/manifest.thunderbird.json` (config)
- `src/builtin-plugins/fixtures/native-preset-baseline.json` (config)
- `src/builtin-plugins/fixtures/native-response-fixtures.json` (config)
- `src/config/fileTranslationSites.json` (config)
- `src/config/localModelTasks.json` (config)
- `src/localAi/core/__tests__/fixtures/pdfNativeAbsoluteFormulas.json` (config)
- `src/localAi/core/__tests__/fixtures/pdfNativeDisplayFormulas.json` (config)
- `src/localAi/core/__tests__/fixtures/pdfNativeFormulaText.json` (config)
- `src/localAi/core/__tests__/fixtures/pdfNativeParagraph.json` (config)
- `src/localAi/core/__tests__/fixtures/pdfNavierEquationLayout.json` (config)
- `src/localAi/core/__tests__/fixtures/pdfNavierLayout.json` (config)
- `src/providers/sdk/defaultTextTaskPrompts.json` (config)
- `src/providers/sdk/defaultTranslationPrompts.json` (config)
- `src/providers/sdk/translationProtocolPrompts.json` (config)

## Top-level layout

- `src` — 724 analysed file(s)
- `public` — 48 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 4 analysed file(s)
- `.agents` — 2 analysed file(s)
- `docs` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9dba2e86d524a8ec85f56bc08ef645a555707bdc` is the revision these paths and observations refer to.
