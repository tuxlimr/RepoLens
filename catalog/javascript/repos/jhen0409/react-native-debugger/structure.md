# Project structure: jhen0409/react-native-debugger

**Analysed commit:** `bd3435a456a29e1eda017ad37b94451834b4ee3a`

**Commit reference:** [bd3435a456a29e1eda017ad37b94451834b4ee3a](https://github.com/jhen0409/react-native-debugger/commit/bd3435a456a29e1eda017ad37b94451834b4ee3a)

**Tree at this commit:** [jhen0409/react-native-debugger@bd3435a456a2](https://github.com/jhen0409/react-native-debugger/tree/bd3435a456a29e1eda017ad37b94451834b4ee3a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jhen0409/react-native-debugger |
| Description | The standalone app based on official debugger of React Native, and includes React Inspector / Redux DevTools |
| Stars | 10437 |
| Forks | 807 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `bd3435a456a29e1eda017ad37b94451834b4ee3a` |
| Retrieved at | 2026-11-14T19:12:39.984094+00:00 |
| Files in this snapshot | 137 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (2 files)
    main.yml
    release.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  settings.yml
__e2e__/  (10 files)
  fixture/  (7 files)
    apollo.js
    app.js
    mobx.js
    redux.js
    remotedev.js
    setup.js
    xhr-test.js
  app.spec.js
  buildTestBundle.js
  mockRNServer.js
app/  (34 files)
  actions/  (2 files)
    debugger.js
    setting.js
  components/  (2 files)
    Draggable.js
    FormInput.js
  containers/  (5 files)
    redux/  (3 files)
      … 3 files under this directory
    App.js
    ReactInspector.js
  middlewares/  (2 files)
    debuggerAPI.js
    reduxAPI.js
  reducers/  (3 files)
    debugger.js
    index.js
    setting.js
  store/  (1 files)
    configureStore.js
  utils/  (4 files)
    adb.js
    config.js
    devMenu.js
    devtools.js
  worker/  (12 files)
    polyfills/  (1 files)
      … 1 files under this directory
    .eslintrc
    apollo.js
    asyncStorage.js
    devMenu.js
    index.js
    networkInspect.js
    reactDevTools.js
    reduxAPI.js
    remotedev.js
    setup.js
    utils.js
  globalStyles.js
  index.js
  setup.js
docs/  (12 files)
  README.md
  apollo-client-devtools-integration.md
  config-file-in-home-directory.md
  contributing.md
  debugger-integration.md
  enable-open-in-editor-in-console.md
  getting-started.md
  network-inspect-of-chrome-devtools.md
  react-devtools-integration.md
  redux-devtools-integration.md
  shortcut-references.md
  troubleshooting.md
electron/  (21 files)
  config/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.js
    template.js
  menu/  (5 files)
    common.js
    darwin.js
    dialog.js
    index.js
    linux+win.js
  url-handle/  (3 files)
    handleURL.js
    index.js
    port.js
  app.html
  context-menu.js
  debug.js
  devtools.js
  extensions.js
  main.js
  sync-state.js
  update.js
  window.js
examples/  (14 files)
  test-old-bridge/  (13 files)
    examples/  (7 files)
      … 7 files under this directory
    .gitignore
    App.js
    README.md
    app.json
    babel.config.js
    package.json
  .eslintrc
npm-package/  (12 files)
  bin/  (1 files)
    rndebugger-open.js
  lib/  (1 files)
    injectDevToolsMiddleware.tmpl.js
  src/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    injectDevToolsMiddleware.js
    main.js
    open.js
  .eslintrc
  .gitignore
  README.md
  babel.config.js
  package.json
patches/  (5 files)
  @redux-devtools+inspector-monitor-trace-tab+1.0.0.patch
  @redux-devtools+ui+1.3.0.patch
  apollo-client-devtools+4.1.4.patch
  electron-gh-releases+2.0.4.patch
  react-dev-utils+4.2.3.patch
scripts/  (9 files)
  mac/  (3 files)
    createDMG.js
    createUniversalApp.js
    entitlements.plist
  config.json
  package-linux.sh
  package-macos.sh
  package-windows.sh
  patch-modules.js
  postinstall.js
webpack/  (5 files)
  .eslintrc
  base.js
  main.prod.js
  renderer.dev.js
  renderer.prod.js
.eslintignore
.eslintrc
.gitignore
.prettierrc
LICENSE.md
README.md
auto_update.json
auto_updater.json
babel.config.js
package.json
```

## Entry points

- [npm-package/bin/rndebugger-open.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/npm-package/bin/rndebugger-open.js)
- [electron/main.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/electron/main.js)
- [__e2e__/fixture/app.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/__e2e__/fixture/app.js)
- [app/containers/App.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/app/containers/App.js)
- [app/index.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/app/index.js)
- [app/reducers/index.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/app/reducers/index.js)
- [app/worker/index.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/app/worker/index.js)
- [electron/config/index.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/electron/config/index.js)
- [electron/menu/index.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/electron/menu/index.js)
- [electron/url-handle/index.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/electron/url-handle/index.js)
- [npm-package/src/main.js](https://github.com/jhen0409/react-native-debugger/blob/bd3435a456a29e1eda017ad37b94451834b4ee3a/npm-package/src/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 33 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| __e2e__ package | library | Observed | Groups 10 file(s) under __e2e__ package (observed from repository paths and static analysis). |
| electron package | library | Observed | Groups 16 file(s) under electron package (observed from repository paths and static analysis). |
| npm-package package | library | Observed | Groups 7 file(s) under npm-package package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). |
| webpack package | library | Observed | Groups 4 file(s) under webpack package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/settings.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `auto_update.json` (config)
- `auto_updater.json` (config)
- `examples/test-old-bridge/app.json` (config)
- `examples/test-old-bridge/package.json` (manifest)
- `npm-package/package.json` (manifest)
- `package.json` (manifest)
- `scripts/config.json` (config)

## Top-level layout

- `app` — 34 analysed file(s)
- `electron` — 21 analysed file(s)
- `examples` — 14 analysed file(s)
- `docs` — 12 analysed file(s)
- `npm-package` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `__e2e__` — 10 analysed file(s)
- `scripts` — 9 analysed file(s)
- `.github` — 5 analysed file(s)
- `patches` — 5 analysed file(s)
- `webpack` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (1 x lockfile excluded; 8 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bd3435a456a29e1eda017ad37b94451834b4ee3a` is the revision these paths and observations refer to.
