# Project structure: sweetalert2/sweetalert2

**Analysed commit:** `5a57eebd3a42c8f9d5f1a66918d283dae7b0df2a`

**Commit reference:** [5a57eebd3a42c8f9d5f1a66918d283dae7b0df2a](https://github.com/sweetalert2/sweetalert2/commit/5a57eebd3a42c8f9d5f1a66918d283dae7b0df2a)

**Tree at this commit:** [sweetalert2/sweetalert2@5a57eebd3a42](https://github.com/sweetalert2/sweetalert2/tree/5a57eebd3a42c8f9d5f1a66918d283dae7b0df2a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sweetalert2/sweetalert2 |
| Description | ✨ A beautiful, responsive, highly customizable and accessible (WAI-ARIA) replacement for JavaScript's popup boxes. Zero dependencies. 🇺🇦🇪🇺 |
| Stars | 18102 |
| Forks | 1615 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `5a57eebd3a42c8f9d5f1a66918d283dae7b0df2a` |
| Retrieved at | 2026-11-14T19:11:22.897507+00:00 |
| Files in this snapshot | 114 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    01_bug_report.yml
    02_feature_request.yml
    03_question.md
  workflows/  (4 files)
    chrome.yml
    copilot-setup-steps.yml
    firefox.yml
    webkit.yml
  CODE_OF_CONDUCT.md
  FUNDING.yml
  copilot-instructions.md
.vscode/  (2 files)
  extensions.json
  settings.json
cypress/  (5 files)
  e2e/  (1 files)
    tests.cy.js
  support/  (2 files)
    commands.js
    index.js
  styles.css
  utils.js
src/  (61 files)
  instanceMethods/  (7 files)
    _destroy.js
    close.js
    enable-disable-elements.js
    getInput.js
    hideLoading.js
    update.js
    validation-message.js
  staticMethods/  (8 files)
    argsToParams.js
    bindClickHandler.js
    dom.js
    eventHandlers.js
    fire.js
    mixin.js
    showLoading.js
    timer.js
  utils/  (33 files)
    dom/  (18 files)
      … 18 files under this directory
    DismissReason.js
    EventEmitter.js
    Timer.js
    aria.js
    classes.js
    defaultInputValidators.js
    draggable.js
    getTemplateParams.js
    iosFix.js
    isNodeEnv.js
    openPopup.js
    params.js
    scrollbar.js
    setParameters.js
    utils.js
  SweetAlert.js
  buttons-handlers.js
  constants.js
  globalState.js
  instanceMethods.js
  keydown-handler.js
  popup-click-handler.js
  privateMethods.js
  privateProps.js
  staticMethods.js
  sweetalert2.js
  sweetalert2.scss
  types.js
test/  (8 files)
  sandbox/  (1 files)
    index.html
  ts/  (4 files)
    dist-sweetalert2.ts
    inputValidator.ts
    simple-usage.ts
    src-sweetalert2.ts
  webpack/  (2 files)
    index.js
    webpack.config.js
  require-in-commonjs.cjs
themes/  (7 files)
  bootstrap-4.css
  bootstrap-5.css
  borderless.css
  bulma.css
  embed-iframe.css
  material-ui.css
  minimal.css
tools/  (3 files)
  build-dist.mjs
  build.mjs
  purge-jsdelivr.mjs
.editorconfig
.gitignore
.oxfmtrc.json
.oxlintrc.json
.stylelintrc.json
CHANGELOG.md
LICENSE
README.md
SECURITY.md
SPONSORS.md
bun.lock
bunfig.toml
cypress.config.mjs
jsconfig.json
package.json
release.config.js
rollup.config.js
sweetalert2.d.ts
```

## Entry points

- [cypress/support/index.js](https://github.com/sweetalert2/sweetalert2/blob/5a57eebd3a42c8f9d5f1a66918d283dae7b0df2a/cypress/support/index.js)
- [src/utils/dom/index.js](https://github.com/sweetalert2/sweetalert2/blob/5a57eebd3a42c8f9d5f1a66918d283dae7b0df2a/src/utils/dom/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| buttons-handlers.js package | library | Observed | Groups 1 file(s) under buttons-handlers.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 4 file(s) under cypress package (observed from repository paths and static analysis). |
| globalState.js package | library | Observed | Groups 1 file(s) under globalstate.js package (observed from repository paths and static analysis). |
| instanceMethods package | library | Observed | Groups 7 file(s) under instancemethods package (observed from repository paths and static analysis). |
| instanceMethods.js package | library | Observed | Groups 1 file(s) under instancemethods.js package (observed from repository paths and static analysis). |
| keydown-handler.js package | library | Observed | Groups 1 file(s) under keydown-handler.js package (observed from repository paths and static analysis). |
| popup-click-handler.js package | library | Observed | Groups 1 file(s) under popup-click-handler.js package (observed from repository paths and static analysis). |
| privateMethods.js package | library | Observed | Groups 1 file(s) under privatemethods.js package (observed from repository paths and static analysis). |
| privateProps.js package | library | Observed | Groups 1 file(s) under privateprops.js package (observed from repository paths and static analysis). |
| staticMethods package | library | Observed | Groups 8 file(s) under staticmethods package (observed from repository paths and static analysis). |
| staticMethods.js package | library | Observed | Groups 1 file(s) under staticmethods.js package (observed from repository paths and static analysis). |
| sweetalert2.js package | library | Observed | Groups 1 file(s) under sweetalert2.js package (observed from repository paths and static analysis). |
| SweetAlert.js package | library | Observed | Groups 1 file(s) under sweetalert.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 3 file(s) under tools package (observed from repository paths and static analysis). |
| types.js package | library | Observed | Groups 1 file(s) under types.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 33 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/01_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/02_feature_request.yml` (config)
- `.github/workflows/chrome.yml` (ci)
- `.github/workflows/copilot-setup-steps.yml` (ci)
- `.github/workflows/firefox.yml` (ci)
- `.github/workflows/webkit.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `.stylelintrc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `bunfig.toml` (config)
- `jsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 61 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 10 analysed file(s)
- `test` — 8 analysed file(s)
- `themes` — 7 analysed file(s)
- `cypress` — 5 analysed file(s)
- `tools` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5a57eebd3a42c8f9d5f1a66918d283dae7b0df2a` is the revision these paths and observations refer to.
