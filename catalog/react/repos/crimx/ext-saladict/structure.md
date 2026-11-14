# Project structure: crimx/ext-saladict

**Analysed commit:** `1673df15690842847f4c5369f8113f26d4aa2604`

**Commit reference:** [1673df15690842847f4c5369f8113f26d4aa2604](https://github.com/crimx/ext-saladict/commit/1673df15690842847f4c5369f8113f26d4aa2604)

**Tree at this commit:** [crimx/ext-saladict@1673df156908](https://github.com/crimx/ext-saladict/tree/1673df15690842847f4c5369f8113f26d4aa2604)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | crimx/ext-saladict |
| Description | 🥗 All-in-one professional pop-up dictionary and page translator which supports multiple search modes, page translations, new word notebook and PDF selection searching. |
| Stars | 13436 |
| Forks | 858 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | dev |
| Analysed commit | `1673df15690842847f4c5369f8113f26d4aa2604` |
| Retrieved at | 2026-11-14T19:13:18.886818+00:00 |
| Files in this snapshot | 766 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (6 files)
    _bug_report_chs.md
    _feature_request_chs.md
    _new_dict_chs.md
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (2 files)
    build.yml
    pr.yml
  FUNDING.yml
  config.yml
  no-response.yml
.storybook/  (7 files)
  configs/  (1 files)
    contexts.tsx
  addons.ts
  config.ts
  manager-head.html
  preview-head.html
  style.css
  webpack.config.js
.vscode/  (2 files)
  locales.schema.json
  settings.json
assets/  (3 files)
  content.css
  inject-dict-panel.js
  pdf-viewer-bridge.js
config/  (4 files)
  jest/  (4 files)
    cssTransform.js
    fileTransform.js
    rawTextTransform.js
    setupTests.js
docs/  (2 files)
  superpowers/  (2 files)
    plans/  (1 files)
      … 1 files under this directory
    specs/  (1 files)
      … 1 files under this directory
mac-app/  (15 files)
  Saladict - Pop-up Dictionary and Page Translator/  (15 files)
    Saladict - Pop-up Dictionary and Page Translator/  (8 files)
      … 8 files under this directory
    Saladict - Pop-up Dictionary and Page Translator Extension/  (3 files)
      … 3 files under this directory
    Saladict - Pop-up Dictionary and Page Translator.xcodeproj/  (4 files)
      … 4 files under this directory
scripts/  (13 files)
  build.js
  clean-output-plugin.js
  create-neutrino-config.js
  firefox-fix.js
  fixtures.js
  pdf.js
  setup-env.js
  start.js
  style-extractor.js
  targeted-webext-manifest-plugin.js
  test.js
  webext-targets.js
  zip.js
src/  (579 files)
  _helpers/  (35 files)
    __mocks__/  (3 files)
      … 3 files under this directory
    analytics/  (2 files)
      … 2 files under this directory
    axios-worker-adapter.ts
    basic-auth.ts
    browser-api.ts
    check-update.ts
    chs-to-chz.ts
    config-manager.ts
    dark-mode.ts
    dom.ts
    fetch-dom.ts
    getSuggests.ts
    hooks.ts
    i18n.ts
    injectSaladictInternal.ts
    integrity.ts
    lang-check.ts
    matchPatternToRegExpStr.ts
    message-tab.ts
    observables.ts
    permission-manager.ts
    profile-manager.ts
    promise-more.ts
    record-manager.ts
    saladict.ts
    scripting.ts
    … 6 more files
  _locales/  (54 files)
    en/  (8 files)
      … 8 files under this directory
    es/  (8 files)
      … 8 files under this directory
    ko/  (8 files)
      … 8 files under this directory
    manifest/  (5 files)
      … 5 files under this directory
    ne/  (8 files)
      … 8 files under this directory
    zh-CN/  (9 files)
      … 9 files under this directory
    zh-TW/  (8 files)
      … 8 files under this directory
  _sass_shared/  (8 files)
    _global/  (4 files)
      … 4 files under this directory
    _fancy-scrollbar.scss
    _namespace.scss
    _reset.scss
    _theme.scss
  app-config/  (7 files)
    auth.ts
    context-menus.ts
    dicts.ts
    index.ts
    merge-config.ts
    merge-profile.ts
    profiles.ts
  assets/  (7 files)
    Speaker.svg
    bowl.svg
    leaf.svg
    orange.svg
    saladict.svg
    symbol-defs.svg
    tomato.svg
  audio-control/  (2 files)
    audio-control.scss
    index.tsx
  background/  (59 files)
    __fake__/  (1 files)
      … 1 files under this directory
    __mocks__/  (1 files)
      … 1 files under this directory
    database/  (5 files)
      … 5 files under this directory
    sync-manager/  (31 files)
      … 31 files under this directory
    audio-manager.ts
    badge.ts
    clipboard-manager.ts
    context-menus.ts
    dom-task-bridge.ts
    env.ts
    i18n-loader.ts
    i18n-manager.ts
    index.ts
    initialization.ts
    offscreen-dict-bridge.ts
    offscreen-document.ts
    pdf-pending-store.ts
    pdf-sniffer-mv3.ts
    pdf-sniffer-shared.ts
    pdf-sniffer.ts
    server.ts
    state.ts
    static-locales.ts
    types.ts
    windows-manager.ts
  components/  (223 files)
    AntdRoot/  (3 files)
      … 3 files under this directory
    EntryBox/  (3 files)
      … 3 files under this directory
    FloatBox/  (3 files)
      … 3 files under this directory
    HoverBox/  (2 files)
      … 2 files under this directory
    MachineTrans/  (4 files)
      … 4 files under this directory
    ShadowPortal/  (2 files)
      … 2 files under this directory
    Speaker/  (3 files)
      … 3 files under this directory
    StarRates/  (1 files)
      … 1 files under this directory
    StrElm/  (1 files)
      … 1 files under this directory
    Waveform/  (3 files)
      … 3 files under this directory
    WordPage/  (7 files)
      … 7 files under this directory
    dictionaries/  (189 files)
      … 189 files under this directory
    DocumentTitle.tsx
    ErrorBoundary.tsx
  content/  (85 files)
    __fake__/  (3 files)
      … 3 files under this directory
    components/  (67 files)
      … 67 files under this directory
    redux/  (13 files)
      … 13 files under this directory
    _style.scss
    index.tsx
  history/  (2 files)
    env.ts
    index.tsx
  manifest/  (5 files)
    chrome.manifest.json
    common.manifest.js
    edge.manifest.json
    firefox.manifest.json
    safari.manifest.json
  notebook/  (2 files)
    env.ts
    index.tsx
  offscreen/  (1 files)
    index.ts
  options/  (66 files)
    __fake__/  (1 files)
      … 1 files under this directory
    components/  (55 files)
      … 55 files under this directory
    helpers/  (6 files)
      … 6 files under this directory
    _style.scss
    acknowledgement.ts
    env.ts
    index.tsx
  popup/  (7 files)
    __fake__/  (2 files)
      … 2 files under this directory
    Notebook.tsx
    Popup.tsx
    _style.scss
    env.ts
    index.tsx
  quick-search/  (3 files)
    env.ts
    index.tsx
    quick-search.scss
  selection/  (6 files)
    helper.ts
    index.ts
    instant-capture.ts
    message.ts
    quick-search.ts
    select-text.ts
  typings/  (4 files)
    css.d.ts
    global.d.ts
    helpers.ts
    message.ts
  word-editor/  (3 files)
    env.ts
    index.tsx
    word-editor.scss
test/  (105 files)
  specs/  (104 files)
    _helpers/  (9 files)
      … 9 files under this directory
    app-config/  (2 files)
      … 2 files under this directory
    background/  (10 files)
      … 10 files under this directory
    components/  (80 files)
      … 80 files under this directory
    content/  (2 files)
      … 2 files under this directory
    options/  (1 files)
      … 1 files under this directory
  helper.ts
.browserslistrc
.editorconfig
.env.example
.eslintrc.js
.gitattributes
.gitignore
.neutrinorc.js
.neutrinorc.mv3.js
.nvmrc
.prettierrc
CHANGELOG.md
CONTRIBUTING-zh.md
CONTRIBUTING.md
LICENSE
README-zh.md
README.md
TRADEMARKS.md
commitlint.config.js
jest.config.js
jsconfig.json
package.json
postcss.config.js
tsconfig.json
webpack.config.js
… 1 more files
```

## Entry points

- [src/_helpers/analytics/index.ts](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/_helpers/analytics/index.ts)
- [src/app-config/index.ts](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/app-config/index.ts)
- [src/audio-control/index.tsx](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/audio-control/index.tsx)
- [src/background/database/index.ts](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/background/database/index.ts)
- [src/background/index.ts](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/background/index.ts)
- [src/background/server.ts](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/background/server.ts)
- [src/background/sync-manager/index.ts](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/background/sync-manager/index.ts)
- [src/components/AntdRoot/index.tsx](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/components/AntdRoot/index.tsx)
- [src/components/EntryBox/index.tsx](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/components/EntryBox/index.tsx)
- [src/components/FloatBox/index.tsx](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/components/FloatBox/index.tsx)
- [src/components/HoverBox/index.tsx](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/components/HoverBox/index.tsx)
- [src/components/ShadowPortal/index.tsx](https://github.com/crimx/ext-saladict/blob/1673df15690842847f4c5369f8113f26d4aa2604/src/components/ShadowPortal/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app-config package | library | Observed | Groups 7 file(s) under app-config package (observed from repository paths and static analysis). |
| assets package | library | Observed | Groups 2 file(s) under assets package (observed from repository paths and static analysis). |
| audio-control package | library | Observed | Groups 1 file(s) under audio-control package (observed from repository paths and static analysis). |
| background package | library | Observed | Groups 27 file(s) under background package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 157 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 43 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| content package | library | Observed | Groups 63 file(s) under content package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| _helpers package | library | Observed | Groups 35 file(s) under _helpers package (observed from repository paths and static analysis). |
| history package | library | Observed | Groups 2 file(s) under history package (observed from repository paths and static analysis). |
| _locales package | library | Observed | Groups 48 file(s) under _locales package (observed from repository paths and static analysis). |
| manifest package | library | Observed | Groups 1 file(s) under manifest package (observed from repository paths and static analysis). |
| notebook package | library | Observed | Groups 2 file(s) under notebook package (observed from repository paths and static analysis). |
| offscreen package | library | Observed | Groups 1 file(s) under offscreen package (observed from repository paths and static analysis). |
| options package | library | Observed | Groups 57 file(s) under options package (observed from repository paths and static analysis). |
| popup package | library | Observed | Groups 5 file(s) under popup package (observed from repository paths and static analysis). |
| quick-search package | library | Observed | Groups 2 file(s) under quick-search package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 13 file(s) under scripts package (observed from repository paths and static analysis). |
| selection package | library | Observed | Groups 6 file(s) under selection package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 27 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 105 file(s) under tests (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 4 file(s) under typings package (observed from repository paths and static analysis). |
| word-editor package | library | Observed | Groups 2 file(s) under word-editor package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/config.yml` (config)
- `.github/no-response.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/pr.yml` (ci)
- `.vscode/locales.schema.json` (config)
- `.vscode/settings.json` (config)
- `jsconfig.json` (config)
- `mac-app/Saladict - Pop-up Dictionary and Page Translator/Saladict - Pop-up Dictionary and Page Translator/Assets.xcassets/AccentColor.colorset/Contents.json` (config)
- `mac-app/Saladict - Pop-up Dictionary and Page Translator/Saladict - Pop-up Dictionary and Page Translator/Assets.xcassets/AppIcon.appiconset/Contents.json` (config)
- `mac-app/Saladict - Pop-up Dictionary and Page Translator/Saladict - Pop-up Dictionary and Page Translator/Assets.xcassets/Contents.json` (config)
- `package.json` (manifest)
- `src/_locales/manifest/en/messages.json` (config)
- `src/_locales/manifest/ko/messages.json` (config)
- `src/_locales/manifest/np/messages.json` (config)
- `src/_locales/manifest/zh_CN/messages.json` (config)
- `src/_locales/manifest/zh_TW/messages.json` (config)
- `src/_locales/zh-CN/tsconfig.json` (config)
- `src/components/dictionaries/ahdict/_locales.json` (config)
- `src/components/dictionaries/bing/_locales.json` (config)
- `src/components/dictionaries/cambridge/_locales.json` (config)
- `src/components/dictionaries/cobuild/_locales.json` (config)
- `src/components/dictionaries/etymonline/_locales.json` (config)
- `src/components/dictionaries/eudic/_locales.json` (config)
- `src/components/dictionaries/guoyu/_locales.json` (config)
- `src/components/dictionaries/hjdict/_locales.json` (config)
- `src/components/dictionaries/liangan/_locales.json` (config)
- `src/components/dictionaries/longman/_locales.json` (config)
- `src/components/dictionaries/merriamwebster/_locales.json` (config)
- `src/components/dictionaries/mojidict/_locales.json` (config)
- `src/components/dictionaries/naver/_locales.json` (config)
- `src/components/dictionaries/oaldict/_locales.json` (config)
- `src/components/dictionaries/renren/_locales.json` (config)
- `src/components/dictionaries/shanbay/_locales.json` (config)
- `src/components/dictionaries/urban/_locales.json` (config)
- `src/components/dictionaries/vocabulary/_locales.json` (config)
- `src/components/dictionaries/weblio/_locales.json` (config)
- `src/components/dictionaries/weblioejje/_locales.json` (config)
- `src/components/dictionaries/wikipedia/_locales.json` (config)
- `src/components/dictionaries/youdao/_locales.json` (config)
- `src/components/dictionaries/zdic/_locales.json` (config)
- `src/manifest/chrome.manifest.json` (config)
- `src/manifest/edge.manifest.json` (config)
- `src/manifest/firefox.manifest.json` (config)
- `src/manifest/safari.manifest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 579 analysed file(s)
- `test` — 105 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `mac-app` — 15 analysed file(s)
- `scripts` — 13 analysed file(s)
- `.github` — 11 analysed file(s)
- `.storybook` — 7 analysed file(s)
- `config` — 4 analysed file(s)
- `assets` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `docs` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1673df15690842847f4c5369f8113f26d4aa2604` is the revision these paths and observations refer to.
