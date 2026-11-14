# Project structure: kusti8/proton-native

**Analysed commit:** `ab482b120542951628292211b989e504fa4a3985`

**Commit reference:** [ab482b120542951628292211b989e504fa4a3985](https://github.com/kusti8/proton-native/commit/ab482b120542951628292211b989e504fa4a3985)

**Tree at this commit:** [kusti8/proton-native@ab482b120542](https://github.com/kusti8/proton-native/tree/ab482b120542951628292211b989e504fa4a3985)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | kusti8/proton-native |
| Description | A React environment for cross platform desktop apps |
| Stars | 10866 |
| Forks | 348 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `ab482b120542951628292211b989e504fa4a3985` |
| Retrieved at | 2026-11-14T19:13:29.320642+00:00 |
| Files in this snapshot | 103 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    documentation-issue.md
    feature_request.md
  FUNDING.yml
.vscode/  (1 files)
  launch.json
__mocks__/  (1 files)
  node-qt.js
docs/  (26 files)
  SVG/  (1 files)
    Artboard 1.svg
  components/  (2 files)
    View.md
    Window.md
  images/  (5 files)
    app_icon.svg
    icon_black.svg
    icon_white.svg
    logo_black.svg
    logo_white.svg
  .nojekyll
  CNAME
  README.md
  _coverpage.md
  _sidebar.md
  about.md
  components.md
  debugging.md
  external_functionality.md
  hot_reloading.md
  index.html
  js_example.js
  main.js
  packaging.md
  python_example.py
  quickstart.md
  v2_changes.md
  wx_backend.md
examples/  (17 files)
  Calculator/  (5 files)
    .babelrc
    app.js
    index.js
    package.json
    webpack.config.js
  CatApi/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    .babelrc
    app.js
    index.js
    package.json
    webpack.config.js
  Notepad/  (3 files)
    .babelrc
    index.js
    package.json
src/  (41 files)
  backends/  (3 files)
    index.ts
    qt.ts
    wx.ts
  components/  (15 files)
    App.ts
    Base.ts
    Button.ts
    Container.ts
    Image.ts
    PickerInternal.ts
    Root.ts
    RootText.ts
    TextFuncs.ts
    TextInput.ts
    View.ts
    VirtualText.ts
    Window.ts
    YogaComponent.ts
    index.ts
  misc/  (7 files)
    hot.ts
    index.ts
    node-qt-napi.d.ts
    node-wx-napi.ts
    react-proxy.d.ts
    styleSheet.ts
    yoga-layout-prebuilt.d.ts
  react-components/  (6 files)
    Picker.tsx
    Text.tsx
    TouchableHighlight.tsx
    TouchableOpacity.tsx
    TouchableWithoutFeedback.tsx
    index.ts
  reconciler/  (1 files)
    index.ts
  render/  (1 files)
    index.ts
  utils/  (6 files)
    convertStyleSheet.ts
    createElement.ts
    propChecker.ts
    propsUpdater.ts
    requireImpl.ts
    yogaHelper.ts
  devtools.ts
  index.ts
test/  (2 files)
  components/  (1 files)
    Window.test.js
  index.js
.babelrc
.editorconfig
.gitignore
.travis.yml
CONTRIBUTING.md
LICENSE
README.md
package.json
testprog.js
testyoga.js
tsconfig.json
```

## Entry points

- [examples/Calculator/index.js](https://github.com/kusti8/proton-native/blob/ab482b120542951628292211b989e504fa4a3985/examples/Calculator/index.js)
- [examples/Notepad/index.js](https://github.com/kusti8/proton-native/blob/ab482b120542951628292211b989e504fa4a3985/examples/Notepad/index.js)
- [src/backends/index.ts](https://github.com/kusti8/proton-native/blob/ab482b120542951628292211b989e504fa4a3985/src/backends/index.ts)
- [src/components/App.ts](https://github.com/kusti8/proton-native/blob/ab482b120542951628292211b989e504fa4a3985/src/components/App.ts)
- [src/components/index.ts](https://github.com/kusti8/proton-native/blob/ab482b120542951628292211b989e504fa4a3985/src/components/index.ts)
- [src/index.ts](https://github.com/kusti8/proton-native/blob/ab482b120542951628292211b989e504fa4a3985/src/index.ts)
- [src/misc/index.ts](https://github.com/kusti8/proton-native/blob/ab482b120542951628292211b989e504fa4a3985/src/misc/index.ts)
- [src/react-components/index.ts](https://github.com/kusti8/proton-native/blob/ab482b120542951628292211b989e504fa4a3985/src/react-components/index.ts)
- [src/reconciler/index.ts](https://github.com/kusti8/proton-native/blob/ab482b120542951628292211b989e504fa4a3985/src/reconciler/index.ts)
- [src/render/index.ts](https://github.com/kusti8/proton-native/blob/ab482b120542951628292211b989e504fa4a3985/src/render/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| backends package | library | Observed | Groups 3 file(s) under backends package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 15 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| devtools.ts package | library | Observed | Groups 1 file(s) under devtools.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| misc package | library | Observed | Groups 7 file(s) under misc package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| react-components package | library | Observed | Groups 6 file(s) under react-components package (observed from repository paths and static analysis). |
| reconciler package | library | Observed | Groups 1 file(s) under reconciler package (observed from repository paths and static analysis). |
| render package | library | Observed | Groups 1 file(s) under render package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 6 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `.vscode/launch.json` (config)
- `examples/Calculator/package.json` (manifest)
- `examples/CatApi/package.json` (manifest)
- `examples/Notepad/package.json` (manifest)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 41 analysed file(s)
- `docs` — 26 analysed file(s)
- `examples` — 17 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 4 analysed file(s)
- `test` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `__mocks__` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ab482b120542951628292211b989e504fa4a3985` is the revision these paths and observations refer to.
