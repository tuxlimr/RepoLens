# Project structure: welldone-software/why-did-you-render

**Analysed commit:** `3ec3512d750c49448fe2241e26d05db9e42f0c21`

**Commit reference:** [3ec3512d750c49448fe2241e26d05db9e42f0c21](https://github.com/welldone-software/why-did-you-render/commit/3ec3512d750c49448fe2241e26d05db9e42f0c21)

**Tree at this commit:** [welldone-software/why-did-you-render@3ec3512d750c](https://github.com/welldone-software/why-did-you-render/tree/3ec3512d750c49448fe2241e26d05db9e42f0c21)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | welldone-software/why-did-you-render |
| Description | why-did-you-render by Welldone Software monkey patches React to notify you about potentially avoidable re-renders. (Works with React Native as well.) |
| Stars | 12534 |
| Forks | 224 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `3ec3512d750c49448fe2241e26d05db9e42f0c21` |
| Retrieved at | 2026-11-14T19:13:19.782000+00:00 |
| Files in this snapshot | 128 |

## Directory tree

```text
.github/  (2 files)
  actions/  (1 files)
    setup/  (1 files)
      … 1 files under this directory
  workflows/  (1 files)
    main.yml
.husky/  (2 files)
  .gitignore
  pre-commit
.run/  (1 files)
  Main Jest.run.xml
.vscode/  (3 files)
  extensions.json
  launch.json
  settings.json
cypress/  (27 files)
  e2e/  (20 files)
    big_list.js
    child-of-pure-component.js
    clone-element.js
    create-factory.js
    hooks-use-context.js
    hooks-use-memo-and-callback-child.js
    hooks-use-reducer.js
    hooks-use-state.js
    hot-reload.js
    no-change.js
    owner-reasons.js
    props-and-state-change.js
    props-changes.js
    react-redux.js
    special-changes.js
    ssr.js
    state-changes.js
    strict-mode.js
    styled-component.js
    test_console_assertions.js
  fixtures/  (1 files)
    example.json
  plugins/  (1 files)
    index.js
  support/  (3 files)
    assertions.js
    commands.js
    e2e.js
  .eslintrc
  babel.config.js
demo/  (29 files)
  public/  (1 files)
    index.html
  src/  (26 files)
    bigList/  (1 files)
      … 1 files under this directory
    bothChanges/  (1 files)
      … 1 files under this directory
    childOfPureComponent/  (1 files)
      … 1 files under this directory
    cloneElement/  (1 files)
      … 1 files under this directory
    createFactory/  (1 files)
      … 1 files under this directory
    forwardRef/  (1 files)
      … 1 files under this directory
    hooks/  (4 files)
      … 4 files under this directory
    hotReload/  (1 files)
      … 1 files under this directory
    logOwnerReasons/  (1 files)
      … 1 files under this directory
    noChanges/  (1 files)
      … 1 files under this directory
    propsChanges/  (1 files)
      … 1 files under this directory
    reactRedux/  (1 files)
      … 1 files under this directory
    reactReduxHOC/  (1 files)
      … 1 files under this directory
    specialChanges/  (1 files)
      … 1 files under this directory
    ssr/  (2 files)
      … 2 files under this directory
    stateChanges/  (1 files)
      … 1 files under this directory
    strict/  (1 files)
      … 1 files under this directory
    styledComponents/  (1 files)
      … 1 files under this directory
    App.js
    Menu.js
    createStepLogger.js
    index.js
  nollup.config.js
  serve.js
src/  (19 files)
  patches/  (4 files)
    patchClassComponent.js
    patchForwardRefComponent.js
    patchFunctionalOrStrComponent.js
    patchMemoComponent.js
  calculateDeepEqualDiffs.js
  consts.js
  defaultNotifier.js
  findObjectsDifferences.js
  getDefaultProps.js
  getDisplayName.js
  getUpdateInfo.js
  helpers.js
  index.js
  normalizeOptions.js
  printDiff.js
  shouldTrack.js
  utils.js
  wdyrStore.js
  whyDidYouRender.js
tests/  (27 files)
  hooks/  (6 files)
    childrenUsingHookResults.test.js
    hooks.test.js
    useContext.test.js
    useReducer.test.js
    useState.test.js
    useSyncExternalStore.test.js
  librariesTests/  (3 files)
    react-redux.test.js
    react-router-dom.test.js
    styled-components.test.js
  patches/  (4 files)
    patchClassComponent.test.js
    patchForwardRefComponent.test.js
    patchFunctionalOrStrComponent.test.js
    patchMemoComponent.test.js
  .eslintrc
  babel.config.cjs
  calculateDeepEqualDiffs.test.js
  defaultNotifier.test.js
  findObjectsDifferences.test.js
  getDisplayName.test.js
  getUpdateInfo.test.js
  index.test.js
  logOnDifferentValues.test.js
  logOwnerReasons.test.js
  normalizeOptions.test.js
  shouldTrack.test.js
  strictMode.test.js
  utils.test.js
.gitignore
LICENSE
README.md
babel.config.cjs
cypress.config.ts
eslint.config.js
jest.config.js
jest.polyfills.js
jestSetup.js
jsx-dev-runtime.d.ts
jsx-dev-runtime.js
jsx-runtime.d.ts
jsx-runtime.js
package.json
rollup.config.js
tsconfig.json
tsx-test.tsx
types.d.ts
```

## Entry points

- [cypress/plugins/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/cypress/plugins/index.js)
- [demo/src/App.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/App.js)
- [demo/src/bigList/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/bigList/index.js)
- [demo/src/bothChanges/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/bothChanges/index.js)
- [demo/src/childOfPureComponent/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/childOfPureComponent/index.js)
- [demo/src/cloneElement/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/cloneElement/index.js)
- [demo/src/createFactory/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/createFactory/index.js)
- [demo/src/forwardRef/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/forwardRef/index.js)
- [demo/src/hotReload/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/hotReload/index.js)
- [demo/src/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/index.js)
- [demo/src/logOwnerReasons/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/logOwnerReasons/index.js)
- [demo/src/noChanges/index.js](https://github.com/welldone-software/why-did-you-render/blob/3ec3512d750c49448fe2241e26d05db9e42f0c21/demo/src/noChanges/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| calculateDeepEqualDiffs.js package | library | Observed | Groups 1 file(s) under calculatedeepequaldiffs.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| consts.js package | library | Observed | Groups 1 file(s) under consts.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 13 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 24 file(s) under cypress package (observed from repository paths and static analysis). |
| defaultNotifier.js package | library | Observed | Groups 1 file(s) under defaultnotifier.js package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 28 file(s) under demo package (observed from repository paths and static analysis). |
| findObjectsDifferences.js package | library | Observed | Groups 1 file(s) under findobjectsdifferences.js package (observed from repository paths and static analysis). |
| getDefaultProps.js package | library | Observed | Groups 1 file(s) under getdefaultprops.js package (observed from repository paths and static analysis). |
| getDisplayName.js package | library | Observed | Groups 1 file(s) under getdisplayname.js package (observed from repository paths and static analysis). |
| getUpdateInfo.js package | library | Observed | Groups 1 file(s) under getupdateinfo.js package (observed from repository paths and static analysis). |
| helpers.js package | library | Observed | Groups 1 file(s) under helpers.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| normalizeOptions.js package | library | Observed | Groups 1 file(s) under normalizeoptions.js package (observed from repository paths and static analysis). |
| patches package | library | Observed | Groups 4 file(s) under patches package (observed from repository paths and static analysis). |
| printDiff.js package | library | Observed | Groups 1 file(s) under printdiff.js package (observed from repository paths and static analysis). |
| shouldTrack.js package | library | Observed | Groups 1 file(s) under shouldtrack.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 28 file(s) under tests (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| wdyrStore.js package | library | Observed | Groups 1 file(s) under wdyrstore.js package (observed from repository paths and static analysis). |
| whyDidYouRender.js package | library | Observed | Groups 1 file(s) under whydidyourender.js package (observed from repository paths and static analysis). |

## Important files

- `.github/actions/setup/action.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `cypress/fixtures/example.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `demo` — 29 analysed file(s)
- `cypress` — 27 analysed file(s)
- `tests` — 27 analysed file(s)
- `src` — 19 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.run` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3ec3512d750c49448fe2241e26d05db9e42f0c21` is the revision these paths and observations refer to.
