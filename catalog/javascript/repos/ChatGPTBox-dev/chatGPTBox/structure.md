# Project structure: ChatGPTBox-dev/chatGPTBox

**Analysed commit:** `f0717a154e756a147f12c985021676c6134c34b5`

**Commit reference:** [f0717a154e756a147f12c985021676c6134c34b5](https://github.com/ChatGPTBox-dev/chatGPTBox/commit/f0717a154e756a147f12c985021676c6134c34b5)

**Tree at this commit:** [ChatGPTBox-dev/chatGPTBox@f0717a154e75](https://github.com/ChatGPTBox-dev/chatGPTBox/tree/f0717a154e756a147f12c985021676c6134c34b5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ChatGPTBox-dev/chatGPTBox |
| Description | Integrating ChatGPT into your browser deeply, everything you need is here |
| Stars | 10774 |
| Forks | 880 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f0717a154e756a147f12c985021676c6134c34b5` |
| Retrieved at | 2026-11-14T19:12:31.388623+00:00 |
| Files in this snapshot | 271 |

## Directory tree

```text
.github/  (14 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report---问题报告.md
    feature-request---新功能请求.md
  workflows/  (10 files)
    scripts/  (2 files)
      … 2 files under this directory
    edge-api-key-expiry.yml
    firefox-metadata.yml
    format-lint.yml
    pr-tests.yml
    pre-release-build.yml
    pullfrog.yml
    tagged-release.yml
    verify-configs.yml
  CONTRIBUTING.md
  dependabot.yml
badges/  (1 files)
  coverage.json
safari/  (3 files)
  appdmg.json
  build.sh
  export-options.plist
scripts/  (4 files)
  check-edge-api-key-expiry.mjs
  create-firefox-sources-zip.mjs
  submit-stores.mjs
  update-firefox-metadata.mjs
src/  (150 files)
  _locales/  (16 files)
    de/  (1 files)
      … 1 files under this directory
    en/  (1 files)
      … 1 files under this directory
    es/  (1 files)
      … 1 files under this directory
    fr/  (1 files)
      … 1 files under this directory
    id/  (1 files)
      … 1 files under this directory
    it/  (1 files)
      … 1 files under this directory
    ja/  (1 files)
      … 1 files under this directory
    ko/  (1 files)
      … 1 files under this directory
    pt/  (1 files)
      … 1 files under this directory
    ru/  (1 files)
      … 1 files under this directory
    tr/  (1 files)
      … 1 files under this directory
    zh-hans/  (1 files)
      … 1 files under this directory
    zh-hant/  (1 files)
      … 1 files under this directory
    i18n-react.mjs
    i18n.mjs
    resources.mjs
  background/  (5 files)
    commands.mjs
    index.mjs
    menus.mjs
    proxy-generation-state.mjs
    redact.mjs
  components/  (20 files)
    ConfirmButton/  (1 files)
      … 1 files under this directory
    ConversationCard/  (2 files)
      … 2 files under this directory
    ConversationItem/  (1 files)
      … 1 files under this directory
    CopyButton/  (1 files)
      … 1 files under this directory
    DecisionCard/  (1 files)
      … 1 files under this directory
    DeleteButton/  (1 files)
      … 1 files under this directory
    FeedbackForChatGPTWeb/  (1 files)
      … 1 files under this directory
    FloatingToolbar/  (1 files)
      … 1 files under this directory
    InputBox/  (3 files)
      … 3 files under this directory
    MarkdownRender/  (4 files)
      … 4 files under this directory
    ReadButton/  (2 files)
      … 2 files under this directory
    WebJumpBackNotification/  (1 files)
      … 1 files under this directory
    index.mjs
  config/  (5 files)
    index.mjs
    language-data.mjs
    language.mjs
    model-key-migrations.mjs
    openai-provider-mappings.mjs
  content-script/  (22 files)
    menu-tools/  (1 files)
      … 1 files under this directory
    selection-tools/  (1 files)
      … 1 files under this directory
    site-adapters/  (17 files)
      … 17 files under this directory
    index.jsx
    port-error.mjs
    styles.scss
  fonts/  (1 files)
    styles.css
  hooks/  (6 files)
    config-storage-listener.mjs
    use-clamp-window-size.mjs
    use-config.mjs
    use-theme.mjs
    use-window-size.mjs
    use-window-theme.mjs
  pages/  (5 files)
    IndependentPanel/  (4 files)
      … 4 files under this directory
    styles.scss
  popup/  (17 files)
    sections/  (11 files)
      … 11 files under this directory
    Popup.jsx
    api-mode-config-utils.mjs
    index.html
    index.jsx
    popup-config-utils.mjs
    styles.scss
  services/  (22 files)
    apis/  (15 files)
      … 15 files under this directory
    clients/  (4 files)
      … 4 files under this directory
    init-session.mjs
    local-session.mjs
    wrappers.mjs
  utils/  (28 files)
    abort-error.mjs
    change-children-font-size.mjs
    create-element-at-position.mjs
    crop-text.mjs
    ends-with-question-mark.mjs
    error-text.mjs
    eventsource-parser.mjs
    fetch-bg.mjs
    fetch-sse.mjs
    get-client-position.mjs
    get-conversation-pairs.mjs
    get-core-content-text.mjs
    get-possible-element-by-query-selector.mjs
    hs256-jwt.mjs
    index.mjs
    is-edge.mjs
    is-firefox.mjs
    is-mobile.mjs
    is-safari.mjs
    jwt-token-generator.mjs
    limited-fetch.mjs
    model-name-convert.mjs
    open-url.mjs
    parse-float-with-clamp.mjs
    … 4 more files
  manifest.json
  manifest.v2.json
  rules.json
tests/  (82 files)
  setup/  (7 files)
    bing-web-lifecycle-loader-hooks.mjs
    browser-shim.mjs
    content-script-selection-toolbar-loader-hooks.mjs
    conversation-card-lifecycle-loader-hooks.mjs
    floating-toolbar-subscriptions-loader-hooks.mjs
    jsx-loader-hooks.mjs
    use-config-loader-hooks.mjs
  unit/  (75 files)
    background/  (3 files)
      … 3 files under this directory
    components/  (7 files)
      … 7 files under this directory
    config/  (5 files)
      … 5 files under this directory
    content-script/  (5 files)
      … 5 files under this directory
    helpers/  (2 files)
      … 2 files under this directory
    hooks/  (3 files)
      … 3 files under this directory
    popup/  (7 files)
      … 7 files under this directory
    release/  (4 files)
      … 4 files under this directory
    services/  (21 files)
      … 21 files under this directory
    setup/  (1 files)
      … 1 files under this directory
    utils/  (17 files)
      … 17 files under this directory
.eslintrc.json
.gitattributes
.gitignore
.nvmrc
.prettierignore
.prettierrc
AGENTS.md
CURRENT_CHANGE.md
LICENSE
README.md
README_IN.md
README_JA.md
README_TR.md
README_ZH.md
SOURCE_CODE_REVIEW.md
build.mjs
package.json
```

## Entry points

- [src/components/ConfirmButton/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/ConfirmButton/index.jsx)
- [src/components/ConversationCard/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/ConversationCard/index.jsx)
- [src/components/ConversationItem/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/ConversationItem/index.jsx)
- [src/components/CopyButton/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/CopyButton/index.jsx)
- [src/components/DecisionCard/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/DecisionCard/index.jsx)
- [src/components/DeleteButton/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/DeleteButton/index.jsx)
- [src/components/FeedbackForChatGPTWeb/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/FeedbackForChatGPTWeb/index.jsx)
- [src/components/FloatingToolbar/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/FloatingToolbar/index.jsx)
- [src/components/InputBox/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/InputBox/index.jsx)
- [src/components/ReadButton/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/ReadButton/index.jsx)
- [src/components/WebJumpBackNotification/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/components/WebJumpBackNotification/index.jsx)
- [src/content-script/index.jsx](https://github.com/ChatGPTBox-dev/chatGPTBox/blob/f0717a154e756a147f12c985021676c6134c34b5/src/content-script/index.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| background package | library | Observed | Groups 5 file(s) under background package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 20 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 24 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| content-script package | library | Observed | Groups 21 file(s) under content-script package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 4 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 6 file(s) under hooks package (observed from repository paths and static analysis). |
| _locales package | library | Observed | Groups 3 file(s) under _locales package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 2 file(s) under pages package (observed from repository paths and static analysis). |
| popup package | library | Observed | Groups 15 file(s) under popup package (observed from repository paths and static analysis). |
| safari package | library | Observed | Groups 1 file(s) under safari package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 18 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 82 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 28 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/edge-api-key-expiry.yml` (ci)
- `.github/workflows/firefox-metadata.yml` (ci)
- `.github/workflows/format-lint.yml` (ci)
- `.github/workflows/pr-tests.yml` (ci)
- `.github/workflows/pre-release-build.yml` (ci)
- `.github/workflows/pullfrog.yml` (ci)
- `.github/workflows/scripts/update-coverage-badge.mjs` (ci)
- `.github/workflows/scripts/verify-search-engine-configs.mjs` (ci)
- `.github/workflows/tagged-release.yml` (ci)
- `.github/workflows/verify-configs.yml` (ci)
- `badges/coverage.json` (config)
- `package.json` (manifest)
- `safari/appdmg.json` (config)
- `src/_locales/de/main.json` (config)
- `src/_locales/en/main.json` (config)
- `src/_locales/es/main.json` (config)
- `src/_locales/fr/main.json` (config)
- `src/_locales/id/main.json` (config)
- `src/_locales/it/main.json` (config)
- `src/_locales/ja/main.json` (config)
- `src/_locales/ko/main.json` (config)
- `src/_locales/pt/main.json` (config)
- `src/_locales/ru/main.json` (config)
- `src/_locales/tr/main.json` (config)
- `src/_locales/zh-hans/main.json` (config)
- `src/_locales/zh-hant/main.json` (config)
- `src/manifest.json` (config)
- `src/manifest.v2.json` (config)
- `src/rules.json` (config)

## Top-level layout

- `src` — 150 analysed file(s)
- `tests` — 82 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 14 analysed file(s)
- `scripts` — 4 analysed file(s)
- `safari` — 3 analysed file(s)
- `badges` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x generated/minified file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f0717a154e756a147f12c985021676c6134c34b5` is the revision these paths and observations refer to.
