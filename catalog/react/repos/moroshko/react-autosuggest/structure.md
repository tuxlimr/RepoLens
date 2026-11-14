# Project structure: moroshko/react-autosuggest

**Analysed commit:** `e2c84d906afc7b6723d29d1c2283c3f322ee2552`

**Commit reference:** [e2c84d906afc7b6723d29d1c2283c3f322ee2552](https://github.com/moroshko/react-autosuggest/commit/e2c84d906afc7b6723d29d1c2283c3f322ee2552)

**Tree at this commit:** [moroshko/react-autosuggest@e2c84d906afc](https://github.com/moroshko/react-autosuggest/tree/e2c84d906afc7b6723d29d1c2283c3f322ee2552)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | moroshko/react-autosuggest |
| Description | WAI-ARIA compliant React autosuggest component |
| Stars | 5932 |
| Forks | 565 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e2c84d906afc7b6723d29d1c2283c3f322ee2552` |
| Retrieved at | 2026-11-14T19:14:12.200947+00:00 |
| Files in this snapshot | 116 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (1 files)
    build-and-test.yml
  CONTRIBUTING.md
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
demo/  (44 files)
  src/  (40 files)
    components/  (37 files)
      … 37 files under this directory
    index.html
    index.js
    variables.less
  standalone/  (4 files)
    app.css
    app.js
    compiled.app.js
    index.html
scripts/  (1 files)
  deploy-to-gh-pages.sh
src/  (8 files)
  Autosuggest.js
  Autowhatever.js
  Item.js
  ItemList.js
  SectionTitle.js
  compareObjects.js
  index.js
  theme.js
test/  (44 files)
  always-render-suggestions/  (2 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
  async-suggestions/  (2 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
  autowhatever/  (17 files)
    default-props/  (3 files)
      … 3 files under this directory
    function-ref/  (3 files)
      … 3 files under this directory
    multi-section/  (3 files)
      … 3 files under this directory
    plain-list/  (3 files)
      … 3 files under this directory
    render-items-container/  (3 files)
      … 3 files under this directory
    autowhatever-helpers.js
    compareObjects.test.js
  do-not-focus-input-on-suggestion-click/  (2 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
  focus-first-suggestion/  (2 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
  focus-first-suggestion-clear-on-enter/  (2 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
  keep-suggestions-on-select/  (2 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
  multi-section/  (3 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
    languages.js
  plain-list/  (3 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
    languages.js
  render-input-component/  (2 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
  render-suggestions-container/  (2 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
  textarea/  (3 files)
    AutosuggestApp.js
    AutosuggestApp.test.js
    languages.js
  helpers.js
  setup.js
.babelrc
.editorconfig
.eslintrc.js
.gitignore
.mocharc.yaml
FAQ.md
LICENSE
README.md
nyc.config.js
package.json
server.js
webpack.dev.config.js
webpack.gh-pages.config.js
webpack.standalone-demo.config.js
webpack.standalone.config.js
```

## Entry points

- [demo/src/index.js](https://github.com/moroshko/react-autosuggest/blob/e2c84d906afc7b6723d29d1c2283c3f322ee2552/demo/src/index.js)
- [demo/standalone/app.js](https://github.com/moroshko/react-autosuggest/blob/e2c84d906afc7b6723d29d1c2283c3f322ee2552/demo/standalone/app.js)
- [server.js](https://github.com/moroshko/react-autosuggest/blob/e2c84d906afc7b6723d29d1c2283c3f322ee2552/server.js)
- [src/index.js](https://github.com/moroshko/react-autosuggest/blob/e2c84d906afc7b6723d29d1c2283c3f322ee2552/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Autosuggest.js package | library | Observed | Groups 1 file(s) under autosuggest.js package (observed from repository paths and static analysis). |
| Autowhatever.js package | library | Observed | Groups 1 file(s) under autowhatever.js package (observed from repository paths and static analysis). |
| compareObjects.js package | library | Observed | Groups 1 file(s) under compareobjects.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 19 file(s) under demo package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Item.js package | library | Observed | Groups 1 file(s) under item.js package (observed from repository paths and static analysis). |
| ItemList.js package | library | Observed | Groups 1 file(s) under itemlist.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| SectionTitle.js package | library | Observed | Groups 1 file(s) under sectiontitle.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 44 file(s) under tests (observed from repository paths and static analysis). |
| theme.js package | library | Observed | Groups 1 file(s) under theme.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/build-and-test.yml` (ci)
- `.mocharc.yaml` (config)
- `package.json` (manifest)

## Top-level layout

- `demo` — 44 analysed file(s)
- `test` — 44 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `src` — 8 analysed file(s)
- `.github` — 4 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e2c84d906afc7b6723d29d1c2283c3f322ee2552` is the revision these paths and observations refer to.
