# Project structure: bailicangdu/react-pxq

**Analysed commit:** `553e42f41b9ed4ad0d30216aedf7e3fb7c06fc3e`

**Commit reference:** [553e42f41b9ed4ad0d30216aedf7e3fb7c06fc3e](https://github.com/bailicangdu/react-pxq/commit/553e42f41b9ed4ad0d30216aedf7e3fb7c06fc3e)

**Tree at this commit:** [bailicangdu/react-pxq@553e42f41b9e](https://github.com/bailicangdu/react-pxq/tree/553e42f41b9ed4ad0d30216aedf7e3fb7c06fc3e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bailicangdu/react-pxq |
| Description | 一个 react + redux 的完整项目 和 个人总结 |
| Stars | 7494 |
| Forks | 2109 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `553e42f41b9ed4ad0d30216aedf7e3fb7c06fc3e` |
| Retrieved at | 2026-11-14T19:13:49.777750+00:00 |
| Files in this snapshot | 71 |

## Directory tree

```text
bin/  (1 files)
  react-scripts
config/  (9 files)
  jest/  (3 files)
    babelTransform.js
    cssTransform.js
    fileTransform.js
  env.js
  paths.js
  polyfills.js
  webpack.config.dev.js
  webpack.config.prod.js
  webpackDevServer.config.js
public/  (2 files)
  index.html
  manifest.json
pxq/  (10 files)
  static/  (6 files)
    css/  (1 files)
      … 1 files under this directory
    js/  (4 files)
      … 4 files under this directory
    media/  (1 files)
      … 1 files under this directory
  asset-manifest.json
  index.html
  manifest.json
  service-worker.js
scripts/  (6 files)
  utils/  (1 files)
    createJestConfig.js
  build.js
  eject.js
  init.js
  start.js
  test.js
src/  (38 files)
  api/  (2 files)
    api.js
    server.js
  assets/  (2 files)
    iconfonts/  (2 files)
      … 2 files under this directory
  components/  (6 files)
    TouchableOpacity/  (2 files)
      … 2 files under this directory
    alert/  (2 files)
      … 2 files under this directory
    header/  (2 files)
      … 2 files under this directory
  envconfig/  (1 files)
    envconfig.js
  pages/  (12 files)
    balance/  (2 files)
      … 2 files under this directory
    helpcenter/  (2 files)
      … 2 files under this directory
    home/  (2 files)
      … 2 files under this directory
    production/  (2 files)
      … 2 files under this directory
    record/  (4 files)
      … 4 files under this directory
  router/  (1 files)
    index.js
  store/  (7 files)
    home/  (3 files)
      … 3 files under this directory
    production/  (3 files)
      … 3 files under this directory
    store.js
  style/  (2 files)
    base.css
    mixin.less
  utils/  (3 files)
    asyncComponent.jsx
    mixin.js
    setRem.js
  index.js
  registerServiceWorker.js
.babelrc
.gitignore
LICENSE
README.md
package.json
```

## Entry points

- [src/api/server.js](https://github.com/bailicangdu/react-pxq/blob/553e42f41b9ed4ad0d30216aedf7e3fb7c06fc3e/src/api/server.js)
- [src/index.js](https://github.com/bailicangdu/react-pxq/blob/553e42f41b9ed4ad0d30216aedf7e3fb7c06fc3e/src/index.js)
- [src/router/index.js](https://github.com/bailicangdu/react-pxq/blob/553e42f41b9ed4ad0d30216aedf7e3fb7c06fc3e/src/router/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 3 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| envconfig package | library | Observed | Groups 1 file(s) under envconfig package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 6 file(s) under pages package (observed from repository paths and static analysis). |
| pxq package | library | Observed | Groups 5 file(s) under pxq package (observed from repository paths and static analysis). |
| registerServiceWorker.js package | library | Observed | Groups 1 file(s) under registerserviceworker.js package (observed from repository paths and static analysis). |
| router package | library | Observed | Groups 1 file(s) under router package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 7 file(s) under store package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `package.json` (manifest)
- `public/manifest.json` (config)
- `pxq/asset-manifest.json` (config)
- `pxq/manifest.json` (config)

## Top-level layout

- `src` — 38 analysed file(s)
- `pxq` — 10 analysed file(s)
- `config` — 9 analysed file(s)
- `scripts` — 6 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `public` — 2 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `553e42f41b9ed4ad0d30216aedf7e3fb7c06fc3e` is the revision these paths and observations refer to.
