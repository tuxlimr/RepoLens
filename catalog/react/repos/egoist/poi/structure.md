# Project structure: egoist/poi

**Analysed commit:** `25f782797c4bf4e85ab3a23c0a6a040f7843c5db`

**Commit reference:** [25f782797c4bf4e85ab3a23c0a6a040f7843c5db](https://github.com/egoist/poi/commit/25f782797c4bf4e85ab3a23c0a6a040f7843c5db)

**Tree at this commit:** [egoist/poi@25f782797c4b](https://github.com/egoist/poi/tree/25f782797c4bf4e85ab3a23c0a6a040f7843c5db)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | egoist/poi |
| Description | ⚡A zero-config bundler for JavaScript applications. |
| Stars | 5155 |
| Forks | 252 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `25f782797c4bf4e85ab3a23c0a6a040f7843c5db` |
| Retrieved at | 2026-11-14T19:14:26.643400+00:00 |
| Files in this snapshot | 213 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
core/  (70 files)
  dev-utils/  (18 files)
    CHANGELOG.md
    InlineChunkHtmlPlugin.js
    WatchMissingNodeModulesPlugin.js
    clearConsole.js
    colors.js
    formatWebpackMessages.js
    hotDevClient.js
    launchEditorEndpoint.js
    open.js
    openBrowser.js
    openChrome.applescript
    package.json
    prepareProxy.js
    prettyBytes.js
    printServeMessage.js
    refreshOverlayInterop.js
    runCompiler.js
    skipServiceWorker.js
  logger/  (2 files)
    index.js
    package.json
  poi/  (47 files)
    __test__/  (2 files)
      … 2 files under this directory
    bin/  (1 files)
      … 1 files under this directory
    lib/  (39 files)
      … 39 files under this directory
    CHANGELOG.md
    README.md
    babel.js
    package.json
    webpack.config.js
  test-utils/  (3 files)
    CHANGELOG.md
    createProject.js
    package.json
create-poi-app/  (21 files)
  bin/  (1 files)
    cli.js
  generator/  (17 files)
    __test__/  (1 files)
      … 1 files under this directory
    templates/  (15 files)
      … 15 files under this directory
    saofile.js
  CHANGELOG.md
  README.md
  package.json
other-packages/  (9 files)
  babel-plugin-assets-named-imports/  (4 files)
    __test__/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    index.js
    package.json
  pnp-webpack-plugin/  (3 files)
    CHANGELOG.md
    index.js
    package.json
  pwa-html-webpack-plugin/  (2 files)
    index.js
    package.json
plugins/  (62 files)
  astroturf/  (5 files)
    CHANGELOG.md
    README.md
    index.js
    index.test.js
    package.json
  bundle-report/  (4 files)
    CHANGELOG.md
    README.md
    index.js
    package.json
  eslint/  (4 files)
    CHANGELOG.md
    README.md
    index.js
    package.json
  html-entry/  (11 files)
    example/  (4 files)
      … 4 files under this directory
    lib/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    README.md
    package.json
  karma/  (6 files)
    example/  (1 files)
      … 1 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    package.json
  puppet/  (12 files)
    example/  (2 files)
      … 2 files under this directory
    lib/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    README.md
    package.json
  pwa/  (4 files)
    CHANGELOG.md
    README.md
    index.js
    package.json
  typescript/  (4 files)
    CHANGELOG.md
    README.md
    index.js
    package.json
  vue-static/  (12 files)
    example/  (4 files)
      … 4 files under this directory
    lib/  (5 files)
      … 5 files under this directory
    CHANGELOG.md
    README.md
    package.json
tasks/  (1 files)
  test.sh
test/  (39 files)
  kitchensink/  (39 files)
    src/  (37 files)
      … 37 files under this directory
    .poirc
    package.json
.editorconfig
.gitattributes
.gitignore
.prettierrc
BACKERS.md
LICENSE
README.md
circle.yml
lerna.json
package.json
```

## Entry points

- [core/logger/index.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/core/logger/index.js)
- [core/poi/lib/index.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/core/poi/lib/index.js)
- [core/poi/bin/cli.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/core/poi/bin/cli.js)
- [create-poi-app/bin/cli.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/create-poi-app/bin/cli.js)
- [other-packages/babel-plugin-assets-named-imports/index.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/other-packages/babel-plugin-assets-named-imports/index.js)
- [other-packages/pnp-webpack-plugin/index.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/other-packages/pnp-webpack-plugin/index.js)
- [other-packages/pwa-html-webpack-plugin/index.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/other-packages/pwa-html-webpack-plugin/index.js)
- [plugins/astroturf/index.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/plugins/astroturf/index.js)
- [plugins/bundle-report/index.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/plugins/bundle-report/index.js)
- [plugins/eslint/index.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/plugins/eslint/index.js)
- [plugins/html-entry/lib/index.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/plugins/html-entry/lib/index.js)
- [plugins/karma/lib/index.js](https://github.com/egoist/poi/blob/25f782797c4bf4e85ab3a23c0a6a040f7843c5db/plugins/karma/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 24 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| create-poi-app package | library | Observed | Groups 10 file(s) under create-poi-app package (observed from repository paths and static analysis). |
| other-packages package | library | Observed | Groups 4 file(s) under other-packages package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 31 file(s) under plugins package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 59 file(s) under service / domain layer (observed from repository paths and static analysis). |
| tasks package | library | Observed | Groups 1 file(s) under tasks package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 39 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `circle.yml` (config)
- `core/dev-utils/package.json` (manifest)
- `core/logger/package.json` (manifest)
- `core/poi/package.json` (manifest)
- `core/test-utils/package.json` (manifest)
- `create-poi-app/generator/templates/linter-tslint/tslint.json` (config)
- `create-poi-app/generator/templates/main/package.json` (manifest)
- `create-poi-app/generator/templates/pwa/public/manifest.json` (config)
- `create-poi-app/generator/templates/ts/tsconfig.json` (config)
- `create-poi-app/package.json` (manifest)
- `lerna.json` (config)
- `other-packages/babel-plugin-assets-named-imports/package.json` (manifest)
- `other-packages/pnp-webpack-plugin/package.json` (manifest)
- `other-packages/pwa-html-webpack-plugin/package.json` (manifest)
- `package.json` (manifest)
- `plugins/astroturf/package.json` (manifest)
- `plugins/bundle-report/package.json` (manifest)
- `plugins/eslint/package.json` (manifest)
- `plugins/html-entry/package.json` (manifest)
- `plugins/karma/package.json` (manifest)
- `plugins/puppet/package.json` (manifest)
- `plugins/pwa/package.json` (manifest)
- `plugins/typescript/package.json` (manifest)
- `plugins/vue-static/package.json` (manifest)

## Top-level layout

- `core` — 70 analysed file(s)
- `plugins` — 62 analysed file(s)
- `test` — 39 analysed file(s)
- `create-poi-app` — 21 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `other-packages` — 9 analysed file(s)
- `.github` — 1 analysed file(s)
- `tasks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `25f782797c4bf4e85ab3a23c0a6a040f7843c5db` is the revision these paths and observations refer to.
