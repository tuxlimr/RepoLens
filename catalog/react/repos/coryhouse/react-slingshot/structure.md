# Project structure: coryhouse/react-slingshot

**Analysed commit:** `a7b0c6111cceaf88ffa4c24df3b38401f045a3d1`

**Commit reference:** [a7b0c6111cceaf88ffa4c24df3b38401f045a3d1](https://github.com/coryhouse/react-slingshot/commit/a7b0c6111cceaf88ffa4c24df3b38401f045a3d1)

**Tree at this commit:** [coryhouse/react-slingshot@a7b0c6111cce](https://github.com/coryhouse/react-slingshot/tree/a7b0c6111cceaf88ffa4c24df3b38401f045a3d1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | coryhouse/react-slingshot |
| Description | React + Redux starter kit / boilerplate with Babel, hot reloading, testing, linting and a working example app built in |
| Stars | 9621 |
| Forks | 2851 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `a7b0c6111cceaf88ffa4c24df3b38401f045a3d1` |
| Retrieved at | 2026-11-14T19:13:33.399057+00:00 |
| Files in this snapshot | 73 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    Bug_report.md
    Feature_request.md
  ISSUE_TEMPLATE.md
docs/  (1 files)
  FAQ.md
src/  (39 files)
  actions/  (2 files)
    fuelSavingsActions.js
    fuelSavingsActions.spec.js
  components/  (15 files)
    containers/  (3 files)
      … 3 files under this directory
    AboutPage.js
    AboutPage.spec.js
    App.js
    FuelSavingsForm.js
    FuelSavingsForm.spec.js
    FuelSavingsResults.js
    FuelSavingsResults.spec.js
    FuelSavingsTextInput.js
    FuelSavingsTextInput.spec.js
    HomePage.js
    NotFoundPage.js
    Root.js
  constants/  (1 files)
    actionTypes.js
  reducers/  (4 files)
    fuelSavingsReducer.js
    fuelSavingsReducer.spec.js
    index.js
    initialState.js
  store/  (3 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    configureStore.js
    store.spec.js
  styles/  (2 files)
    about-page.css
    styles.scss
  types/  (1 files)
    index.js
  utils/  (8 files)
    dates.js
    dates.spec.js
    fuelSavings.js
    fuelSavings.spec.js
    math.js
    math.spec.js
    numberFormat.js
    numberFormat.spec.js
  index.ejs
  index.js
  webpack-public-path.js
tools/  (15 files)
  setup/  (3 files)
    setup.js
    setupMessage.js
    setupPrompts.js
  .yarnclean
  analyzeBundle.js
  assetsTransformer.js
  build.js
  chalkConfig.js
  distServer.js
  enzymeTestAdapterSetup.js
  fileMock.js
  nodeVersionCheck.js
  removeDemo.js
  srcServer.js
  startMessage.js
.browserslistrc
.editorconfig
.gitignore
.istanbul.yml
.travis.yml
.watchmanconfig
CONTRIBUTING.md
CONTRIBUTORS.md
LICENSE
PULL_REQUEST_TEMPLATE.md
README.md
appveyor.yml
package.json
webpack.config.dev.js
webpack.config.prod.js
```

## Entry points

- [src/components/App.js](https://github.com/coryhouse/react-slingshot/blob/a7b0c6111cceaf88ffa4c24df3b38401f045a3d1/src/components/App.js)
- [src/index.js](https://github.com/coryhouse/react-slingshot/blob/a7b0c6111cceaf88ffa4c24df3b38401f045a3d1/src/index.js)
- [src/reducers/index.js](https://github.com/coryhouse/react-slingshot/blob/a7b0c6111cceaf88ffa4c24df3b38401f045a3d1/src/reducers/index.js)
- [src/types/index.js](https://github.com/coryhouse/react-slingshot/blob/a7b0c6111cceaf88ffa4c24df3b38401f045a3d1/src/types/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| actions package | library | Observed | Groups 2 file(s) under actions package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 14 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants package | library | Observed | Groups 1 file(s) under constants package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| reducers package | library | Observed | Groups 4 file(s) under reducers package (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 2 file(s) under store package (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 14 file(s) under tools package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 8 file(s) under utils package (observed from repository paths and static analysis). |
| webpack-public-path.js package | library | Observed | Groups 1 file(s) under webpack-public-path.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.istanbul.yml` (config)
- `.travis.yml` (ci)
- `appveyor.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 39 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `tools` — 15 analysed file(s)
- `.github` — 3 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a7b0c6111cceaf88ffa4c24df3b38401f045a3d1` is the revision these paths and observations refer to.
