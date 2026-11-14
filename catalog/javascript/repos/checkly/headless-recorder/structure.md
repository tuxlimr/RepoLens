# Project structure: checkly/headless-recorder

**Analysed commit:** `4fb93c125f40bceb2dd9aac403e200a3ade5a8d9`

**Commit reference:** [4fb93c125f40bceb2dd9aac403e200a3ade5a8d9](https://github.com/checkly/headless-recorder/commit/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9)

**Tree at this commit:** [checkly/headless-recorder@4fb93c125f40](https://github.com/checkly/headless-recorder/tree/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | checkly/headless-recorder |
| Description | Chrome extension that records your browser interactions and generates a Playwright or Puppeteer script.  |
| Stars | 15309 |
| Forks | 730 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `4fb93c125f40bceb2dd9aac403e200a3ade5a8d9` |
| Retrieved at | 2026-11-14T19:11:39.603729+00:00 |
| Files in this snapshot | 104 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (2 files)
    codeql-analysis.yml
    lint-build-test.yml
  auto_assign.yml
  dependabot.yml
  pull_request_template.md
public/  (16 files)
  _locales/  (1 files)
    en/  (1 files)
      … 1 files under this directory
  icons/  (13 files)
    dark/  (6 files)
      … 6 files under this directory
    light/  (7 files)
      … 7 files under this directory
  images/  (1 files)
    checkly-logo.svg
  browser-extension.html
src/  (65 files)
  __tests__/  (2 files)
    build.spec.js
    helpers.js
  assets/  (6 files)
    icons/  (3 files)
      … 3 files under this directory
    animations.css
    code.css
    tailwind.css
  background/  (1 files)
    index.js
  components/  (10 files)
    __tests__/  (4 files)
      … 4 files under this directory
    Button.vue
    Footer.vue
    Header.vue
    RecordingLabel.vue
    RoundButton.vue
    Toggle.vue
  content-scripts/  (8 files)
    __tests__/  (6 files)
      … 6 files under this directory
    controller.js
    index.js
  modules/  (14 files)
    code-generator/  (8 files)
      … 8 files under this directory
    overlay/  (4 files)
      … 4 files under this directory
    recorder/  (1 files)
      … 1 files under this directory
    shooter/  (1 files)
      … 1 files under this directory
  options/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    OptionsApp.vue
    main.js
  popup/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    PopupApp.vue
    main.js
  services/  (11 files)
    __tests__/  (5 files)
      … 5 files under this directory
    analytics.js
    badge.js
    browser.js
    constants.js
    selector.js
    storage.js
  store/  (1 files)
    index.js
  views/  (3 files)
    Home.vue
    Recording.vue
    Results.vue
  manifest.json
.browserslistrc
.eslintrc.js
.gitignore
.prettierrc.js
CHANGELOG.md
CONTRIBUTING.md
LICENSE
PRIVACY_POLICY.md
README.md
babel.config.js
dependabot.yml
jest.config.js
jest.setup.js
jsconfig.json
package.json
postcss.config.js
tailwind.config.js
vue.config.js
```

## Entry points

- [src/background/index.js](https://github.com/checkly/headless-recorder/blob/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9/src/background/index.js)
- [src/content-scripts/index.js](https://github.com/checkly/headless-recorder/blob/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9/src/content-scripts/index.js)
- [src/modules/code-generator/index.js](https://github.com/checkly/headless-recorder/blob/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9/src/modules/code-generator/index.js)
- [src/modules/overlay/index.js](https://github.com/checkly/headless-recorder/blob/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9/src/modules/overlay/index.js)
- [src/modules/recorder/index.js](https://github.com/checkly/headless-recorder/blob/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9/src/modules/recorder/index.js)
- [src/modules/shooter/index.js](https://github.com/checkly/headless-recorder/blob/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9/src/modules/shooter/index.js)
- [src/options/main.js](https://github.com/checkly/headless-recorder/blob/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9/src/options/main.js)
- [src/popup/main.js](https://github.com/checkly/headless-recorder/blob/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9/src/popup/main.js)
- [src/store/index.js](https://github.com/checkly/headless-recorder/blob/4fb93c125f40bceb2dd9aac403e200a3ade5a8d9/src/store/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| background package | library | Observed | Groups 1 file(s) under background package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 8 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| content-scripts package | library | Observed | Groups 6 file(s) under content-scripts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 14 file(s) under modules package (observed from repository paths and static analysis). |
| options package | library | Observed | Groups 3 file(s) under options package (observed from repository paths and static analysis). |
| popup package | library | Observed | Groups 3 file(s) under popup package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 11 file(s) under service / domain layer (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 1 file(s) under store package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 2 file(s) under __tests__ package (observed from repository paths and static analysis). |

## Important files

- `.github/auto_assign.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/lint-build-test.yml` (ci)
- `dependabot.yml` (config)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `public/_locales/en/messages.json` (config)
- `src/manifest.json` (config)

## Top-level layout

- `src` — 65 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `public` — 16 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `4fb93c125f40bceb2dd9aac403e200a3ade5a8d9` is the revision these paths and observations refer to.
