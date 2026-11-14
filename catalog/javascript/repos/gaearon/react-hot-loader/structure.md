# Project structure: gaearon/react-hot-loader

**Analysed commit:** `07d1f4e080f18dd83273be5bd02863ce1caf892e`

**Commit reference:** [07d1f4e080f18dd83273be5bd02863ce1caf892e](https://github.com/gaearon/react-hot-loader/commit/07d1f4e080f18dd83273be5bd02863ce1caf892e)

**Tree at this commit:** [gaearon/react-hot-loader@07d1f4e080f1](https://github.com/gaearon/react-hot-loader/tree/07d1f4e080f18dd83273be5bd02863ce1caf892e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gaearon/react-hot-loader |
| Description | Tweak React components in real time. (Deprecated: use Fast Refresh instead.) |
| Stars | 12148 |
| Forks | 770 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `07d1f4e080f18dd83273be5bd02863ce1caf892e` |
| Retrieved at | 2026-11-14T19:12:09.554967+00:00 |
| Files in this snapshot | 323 |

## Directory tree

```text
.vscode/  (2 files)
  extensions.json
  settings.json
docs/  (1 files)
  Troubleshooting.md
examples/  (191 files)
  SSR/  (10 files)
    src/  (6 files)
      … 6 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  all-possible-containers/  (31 files)
    src/  (23 files)
      … 23 files under this directory
    .babelrc
    .editorconfig
    .flowconfig
    .gitignore
    LICENSE
    README.md
    package.json
    webpack.config.js
  async-components/  (13 files)
    src/  (9 files)
      … 9 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  async-portals/  (11 files)
    src/  (7 files)
      … 7 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  decorators/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  electron-typescript/  (11 files)
    app/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    main.js
    package.json
    tsconfig.json
    webpack.config.js
  hotCold/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  indeterminateComponent/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  mobx/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  multiple-hocs/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  parcel/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    .babelrc
    .gitignore
    index.html
    package.json
  preact/  (9 files)
    src/  (5 files)
      … 5 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  react-bootstrap/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  react-refetch/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  redux/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    .babelrc
    .gitignore
    index_csp.html
    package.json
    webpack.config.babel.js
  styled-components/  (11 files)
    src/  (6 files)
      … 6 files under this directory
    .babelrc
    .gitignore
    index_csp.html
    package.json
    webpack.config.babel.js
  typescript/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    package.json
    tsconfig.json
    webpack.config.babel.js
  typescript-no-babel/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
    webpack.config.js
  webpack/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
  webpack-modern/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .babelrc
    .gitignore
    package.json
    webpack.config.babel.js
scripts/  (4 files)
  ci.sh
  react-15.ci.sh
  react-16.ci.sh
  react-17.ci.sh
src/  (42 files)
  adapters/  (1 files)
    preact.js
  fresh/  (1 files)
    babel.js
  global/  (2 files)
    generation.js
    modules.js
  internal/  (5 files)
    stack/  (2 files)
      … 2 files under this directory
    constants.js
    getReactStack.js
    reactUtils.js
  proxy/  (6 files)
    constants.js
    createClassProxy.js
    index.js
    inject.js
    transferStaticProps.js
    utils.js
  reconciler/  (8 files)
    componentComparator.js
    fiberUpdater.js
    hotReplacementRender.js
    index.js
    proxies.js
    proxyAdapter.js
    resolver.js
    utils.js
  utils/  (1 files)
    runQueue.js
  webpack/  (4 files)
    index.js
    makeIdentitySourceMap.js
    patch.js
    webpackTagCommonJSExports.js
  AppContainer.dev.js
  AppContainer.prod.js
  babel.dev.js
  babel.prod.js
  configuration.js
  errorReporter.js
  hot.dev.js
  hot.prod.js
  index.dev.js
  index.prod.js
  logger.js
  reactHotLoader.js
  utils.dev.js
  utils.prod.js
test/  (57 files)
  __babel_fixtures__/  (23 files)
    class-properties/  (15 files)
      … 15 files under this directory
    bindings.js
    counter.js
    drop-hot-half.prod.js
    drop-hot.prod.js
    hooks.js
    issue-246.js
    local-hooks.js
    name-clash.js
  __snapshots__/  (1 files)
    babel.test.js.snap
  cases/  (2 files)
    hooks/  (1 files)
      … 1 files under this directory
    memo/  (1 files)
      … 1 files under this directory
  global/  (2 files)
    generation.test.js
    modules.test.js
  hot/  (4 files)
    .gitignore
    createPatchedReact.js
    react-dom.integration.spec.js
    react-dom.no-integration.spec.js
  internal/  (2 files)
    getReactStack.test.js
    reactUtils.test.js
  prod/  (3 files)
    AppContainer.prod.test.js
    hot.prod.test.js
    utils.prod.test.js
  proxy/  (10 files)
    consistency.test.js
    helper.js
    instance-descriptor.test.js
    instance-method.test.js
    instance-property.test.js
    lifecycle-method.test.js
    static-descriptor.test.js
    static-method.test.js
    static-property.test.js
    unmounting.test.js
  reconciler/  (1 files)
    proxyAdapter.test.js
  .eslintrc.js
  AppContainer.dev.test.js
  babel.test.js
  build.test.js
  hot.dev.test.js
  index.dev.test.js
  reactHotLoader.test.js
  reconciler.test.js
  utils.test.js
testConfig/  (2 files)
  babel.js
  setupTests.js
.babelrc
.eslintignore
.eslintrc.js
.gitattributes
.gitignore
.prettierignore
.prettierrc
.travis.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
PATRONS.md
README.md
babel.js
index.d.ts
index.js
package.json
patch.js
rollup.config.js
root.d.ts
root.js
webpack.js
```

## Entry points

- [examples/all-possible-containers/src/index.js](https://github.com/gaearon/react-hot-loader/blob/07d1f4e080f18dd83273be5bd02863ce1caf892e/examples/all-possible-containers/src/index.js)
- [examples/electron-typescript/main.js](https://github.com/gaearon/react-hot-loader/blob/07d1f4e080f18dd83273be5bd02863ce1caf892e/examples/electron-typescript/main.js)
- [index.js](https://github.com/gaearon/react-hot-loader/blob/07d1f4e080f18dd83273be5bd02863ce1caf892e/index.js)
- [src/proxy/index.js](https://github.com/gaearon/react-hot-loader/blob/07d1f4e080f18dd83273be5bd02863ce1caf892e/src/proxy/index.js)
- [src/reconciler/index.js](https://github.com/gaearon/react-hot-loader/blob/07d1f4e080f18dd83273be5bd02863ce1caf892e/src/reconciler/index.js)
- [src/webpack/index.js](https://github.com/gaearon/react-hot-loader/blob/07d1f4e080f18dd83273be5bd02863ce1caf892e/src/webpack/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| AppContainer.dev.js package | library | Observed | Groups 1 file(s) under appcontainer.dev.js package (observed from repository paths and static analysis). |
| AppContainer.prod.js package | library | Observed | Groups 1 file(s) under appcontainer.prod.js package (observed from repository paths and static analysis). |
| babel.dev.js package | library | Observed | Groups 1 file(s) under babel.dev.js package (observed from repository paths and static analysis). |
| babel.prod.js package | library | Observed | Groups 1 file(s) under babel.prod.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| configuration.js package | library | Observed | Groups 1 file(s) under configuration.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| errorReporter.js package | library | Observed | Groups 1 file(s) under errorreporter.js package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| fresh package | library | Observed | Groups 1 file(s) under fresh package (observed from repository paths and static analysis). |
| global package | library | Observed | Groups 2 file(s) under global package (observed from repository paths and static analysis). |
| hot.dev.js package | library | Observed | Groups 1 file(s) under hot.dev.js package (observed from repository paths and static analysis). |
| hot.prod.js package | library | Observed | Groups 1 file(s) under hot.prod.js package (observed from repository paths and static analysis). |
| index.dev.js package | library | Observed | Groups 1 file(s) under index.dev.js package (observed from repository paths and static analysis). |
| index.prod.js package | library | Observed | Groups 1 file(s) under index.prod.js package (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 5 file(s) under internal package (observed from repository paths and static analysis). |
| logger.js package | library | Observed | Groups 1 file(s) under logger.js package (observed from repository paths and static analysis). |
| proxy package | library | Observed | Groups 6 file(s) under proxy package (observed from repository paths and static analysis). |
| reactHotLoader.js package | library | Observed | Groups 1 file(s) under reacthotloader.js package (observed from repository paths and static analysis). |
| reconciler package | library | Observed | Groups 8 file(s) under reconciler package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| testConfig package | library | Observed | Groups 2 file(s) under testconfig package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 57 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |
| utils.dev.js package | library | Observed | Groups 1 file(s) under utils.dev.js package (observed from repository paths and static analysis). |
| utils.prod.js package | library | Observed | Groups 1 file(s) under utils.prod.js package (observed from repository paths and static analysis). |
| webpack package | library | Observed | Groups 4 file(s) under webpack package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `examples/SSR/package.json` (manifest)
- `examples/all-possible-containers/.editorconfig` (config)
- `examples/all-possible-containers/package.json` (manifest)
- `examples/async-components/package.json` (manifest)
- `examples/async-portals/package.json` (manifest)
- `examples/decorators/package.json` (manifest)
- `examples/electron-typescript/package.json` (manifest)
- `examples/electron-typescript/tsconfig.json` (config)
- `examples/hotCold/package.json` (manifest)
- `examples/indeterminateComponent/package.json` (manifest)
- `examples/mobx/package.json` (manifest)
- `examples/multiple-hocs/package.json` (manifest)
- `examples/parcel/package.json` (manifest)
- `examples/preact/package.json` (manifest)
- `examples/react-bootstrap/package.json` (manifest)
- `examples/react-refetch/package.json` (manifest)
- `examples/redux/package.json` (manifest)
- `examples/styled-components/package.json` (manifest)
- `examples/typescript-no-babel/package.json` (manifest)
- `examples/typescript-no-babel/tsconfig.json` (config)
- `examples/typescript/package.json` (manifest)
- `examples/typescript/tsconfig.json` (config)
- `examples/webpack-modern/package.json` (manifest)
- `examples/webpack/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `examples` — 191 analysed file(s)
- `test` — 57 analysed file(s)
- `src` — 42 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `testConfig` — 2 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 12 file(s) were skipped during inventory (12 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `07d1f4e080f18dd83273be5bd02863ce1caf892e` is the revision these paths and observations refer to.
