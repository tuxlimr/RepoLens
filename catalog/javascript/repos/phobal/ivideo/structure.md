# Project structure: phobal/ivideo

**Analysed commit:** `e9a26b66177a643f53bbadeb89da45dfee821abc`

**Commit reference:** [e9a26b66177a643f53bbadeb89da45dfee821abc](https://github.com/phobal/ivideo/commit/e9a26b66177a643f53bbadeb89da45dfee821abc)

**Tree at this commit:** [phobal/ivideo@e9a26b66177a](https://github.com/phobal/ivideo/tree/e9a26b66177a643f53bbadeb89da45dfee821abc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | phobal/ivideo |
| Description | 一个可以观看国内主流视频平台所有视频的客户端（Mac、Windows、Linux） A client that can watch video of domestic(China) mainstream video platform |
| Stars | 11816 |
| Forks | 3132 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e9a26b66177a643f53bbadeb89da45dfee821abc` |
| Retrieved at | 2026-11-14T19:12:14.431291+00:00 |
| Files in this snapshot | 66 |

## Directory tree

```text
.vscode/  (1 files)
  settings.json
app/  (23 files)
  actions/  (1 files)
    source.js
  components/  (1 files)
    .githook
  containers/  (6 files)
    App.js
    Channel.js
    Frame.js
    Root.js
    ToolBar.js
    Video.js
  reducers/  (2 files)
    index.js
    source.js
  store/  (3 files)
    configureStore.dev.js
    configureStore.js
    configureStore.prod.js
  utils/  (2 files)
    .gitkeep
    fetch.js
  .eslintrc
  app.global.css
  app.html
  index.js
  main.dev.js
  menu.js
  package.json
  routes.js
flow-typed/  (1 files)
  module_vx.x.x.js
internals/  (9 files)
  flow/  (2 files)
    CSSModule.js.flow
    WebpackAsset.js.flow
  mocks/  (1 files)
    fileMock.js
  scripts/  (6 files)
    CheckBuiltsExist.js
    CheckNativeDep.js
    CheckNodeEnv.js
    CheckPortInUse.js
    ElectronRebuild.js
    RunTests.js
resources/  (1 files)
  viplist.json
test/  (10 files)
  actions/  (2 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    counter.spec.js
  components/  (2 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    Counter.spec.js
  containers/  (1 files)
    CounterPage.spec.js
  e2e/  (1 files)
    e2e.spec.js
  reducers/  (2 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    counter.spec.js
  .eslintrc
  example.js
.babelrc
.dockerignore
.editorconfig
.eslintignore
.eslintrc
.flowconfig
.gitattributes
.gitignore
.stylelintrc
.travis.yml
CHANGELOG.md
LICENSE
README.md
appveyor.yml
package.json
webpack.config.base.js
webpack.config.eslint.js
webpack.config.main.prod.js
webpack.config.renderer.dev.dll.js
webpack.config.renderer.dev.js
webpack.config.renderer.prod.js
```

## Entry points

- [app/containers/App.js](https://github.com/phobal/ivideo/blob/e9a26b66177a643f53bbadeb89da45dfee821abc/app/containers/App.js)
- [app/index.js](https://github.com/phobal/ivideo/blob/e9a26b66177a643f53bbadeb89da45dfee821abc/app/index.js)
- [app/reducers/index.js](https://github.com/phobal/ivideo/blob/e9a26b66177a643f53bbadeb89da45dfee821abc/app/reducers/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 17 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 1 file(s) under flow-typed package (observed from repository paths and static analysis). |
| internals package | library | Observed | Groups 7 file(s) under internals package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.travis.yml` (ci)
- `.vscode/settings.json` (config)
- `app/package.json` (manifest)
- `appveyor.yml` (config)
- `package.json` (manifest)
- `resources/viplist.json` (config)

## Top-level layout

- `app` — 23 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `test` — 10 analysed file(s)
- `internals` — 9 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `flow-typed` — 1 analysed file(s)
- `resources` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `e9a26b66177a643f53bbadeb89da45dfee821abc` is the revision these paths and observations refer to.
