# Project structure: webpack/webpack-bundle-analyzer

**Analysed commit:** `f65668c9ab4ffe4b1989e5badbba3e0e871e1a24`

**Commit reference:** [f65668c9ab4ffe4b1989e5badbba3e0e871e1a24](https://github.com/webpack/webpack-bundle-analyzer/commit/f65668c9ab4ffe4b1989e5badbba3e0e871e1a24)

**Tree at this commit:** [webpack/webpack-bundle-analyzer@f65668c9ab4f](https://github.com/webpack/webpack-bundle-analyzer/tree/f65668c9ab4ffe4b1989e5badbba3e0e871e1a24)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | webpack/webpack-bundle-analyzer |
| Description | Webpack plugin and CLI utility that represents bundle content as convenient interactive zoomable treemap |
| Stars | 12655 |
| Forks | 519 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `f65668c9ab4ffe4b1989e5badbba3e0e871e1a24` |
| Retrieved at | 2026-11-14T19:12:04.053105+00:00 |
| Files in this snapshot | 224 |

## Directory tree

```text
.changeset/  (6 files)
  README.md
  changelog-generator.mjs
  cli-default-sizes-compressed.md
  config.json
  flatten-large-module-lists.md
  module-parsed-size-utf8.md
.github/  (2 files)
  workflows/  (2 files)
    main.yml
    release.yml
bin/  (1 files)
  install-test-webpack-versions.sh
client/  (49 files)
  assets/  (8 files)
    icon-arrow-right.svg
    icon-chunk.svg
    icon-folder.svg
    icon-invisible.svg
    icon-module.svg
    icon-moon.svg
    icon-pin.svg
    icon-sun.svg
  components/  (34 files)
    Button.css
    Button.jsx
    Checkbox.css
    Checkbox.jsx
    CheckboxList.css
    CheckboxList.jsx
    CheckboxListItem.jsx
    ContextMenu.css
    ContextMenu.jsx
    ContextMenuItem.css
    ContextMenuItem.jsx
    Dropdown.css
    Dropdown.jsx
    Icon.css
    Icon.jsx
    ModuleItem.css
    ModuleItem.jsx
    ModulesList.css
    ModulesList.jsx
    ModulesTreemap.css
    ModulesTreemap.jsx
    Search.css
    Search.jsx
    Sidebar.css
    … 10 more files
  lib/  (1 files)
    PureComponent.jsx
  .eslintrc.json
  localStorage.js
  store.js
  utils.js
  viewer.css
  viewer.jsx
src/  (19 files)
  bin/  (1 files)
    analyzer.js
  tree/  (8 files)
    BaseFolder.js
    ConcatenatedModule.js
    ContentFolder.js
    ContentModule.js
    Folder.js
    Module.js
    Node.js
    utils.js
  BundleAnalyzerPlugin.js
  Logger.js
  analyzer.js
  index.js
  parseUtils.js
  sizeUtils.js
  statsUtils.js
  template.js
  utils.js
  viewer.js
test/  (130 files)
  bundles/  (52 files)
    invalidBundle.js
    validBundleWithArrowFunction.js
    validBundleWithArrowFunction.modules.json
    validBundleWithEsNextFeatures.js
    validBundleWithEsNextFeatures.modules.json
    validBundleWithIIFE.js
    validBundleWithIIFE.modules.json
    validCommonBundleWithDedupePlugin.js
    validCommonBundleWithDedupePlugin.modules.json
    validCommonBundleWithModulesAsArray.js
    validCommonBundleWithModulesAsArray.modules.json
    validCommonBundleWithModulesAsObject.js
    validCommonBundleWithModulesAsObject.modules.json
    validExtraBundleWithModulesAsArray.js
    validExtraBundleWithModulesAsArray.modules.json
    validExtraBundleWithModulesInsideArrayConcat.js
    validExtraBundleWithModulesInsideArrayConcat.modules.json
    validExtraBundleWithNamedChunk.js
    validExtraBundleWithNamedChunk.modules.json
    validJsonpWithArrayConcatAndEntryPoint.js
    validJsonpWithArrayConcatAndEntryPoint.modules.json
    validNodeBundle.js
    validNodeBundle.modules.json
    validUmdLibraryBundleWithModulesAsArray.js
    … 28 more files
  dev-server/  (3 files)
    .gitignore
    src.js
    webpack.config.js
  src/  (4 files)
    a-clone.js
    a.js
    b.js
    index.js
  stats/  (57 files)
    extremely-optimized-webpack-5-bundle/  (3 files)
      … 3 files under this directory
    minimal-stats/  (1 files)
      … 1 files under this directory
    webpack-5-bundle-with-concatenated-entry-module/  (3 files)
      … 3 files under this directory
    webpack-5-bundle-with-multiple-entries/  (3 files)
      … 3 files under this directory
    webpack-5-bundle-with-single-entry/  (3 files)
      … 3 files under this directory
    with-array-config/  (3 files)
      … 3 files under this directory
    with-invalid-chunk/  (3 files)
      … 3 files under this directory
    with-missing-chunk/  (2 files)
      … 2 files under this directory
    with-missing-module-chunks/  (2 files)
      … 2 files under this directory
    with-missing-parsed-module/  (2 files)
      … 2 files under this directory
    with-module-concatenation-info/  (3 files)
      … 3 files under this directory
    with-module-in-multiple-assets/  (8 files)
      … 8 files under this directory
    with-modules-in-chunks/  (2 files)
      … 2 files under this directory
    with-multiple-entrypoints/  (2 files)
      … 2 files under this directory
    with-no-entrypoints/  (1 files)
      … 1 files under this directory
    with-non-asset-asset/  (2 files)
      … 2 files under this directory
    with-special-chars/  (3 files)
      … 3 files under this directory
    with-worker-loader/  (2 files)
      … 2 files under this directory
    with-worker-loader-dynamic-import/  (5 files)
      … 5 files under this directory
    with-children-array.json
    with-cjs-chunk.json
    with-invalid-dynamic-require.json
    with-modules-chunk.json
  .eslintrc.json
  .gitignore
  Logger.js
  analyzer.js
  analyzerUtils.js
  dev-server.js
  helpers.js
  parseUtils.js
  plugin.js
  statsUtils.js
  store.js
  tree.js
  utils.js
  viewer.js
.babelrc
.browserslistrc
.editorconfig
.gitignore
.npm-upgrade.json
.nvmrc
.prettierignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
eslint.config.mjs
jest.config.js
package.json
prettier.config.mjs
tsconfig.json
webpack.config.js
```

## Entry points

- [src/index.js](https://github.com/webpack/webpack-bundle-analyzer/blob/f65668c9ab4ffe4b1989e5badbba3e0e871e1a24/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| analyzer.js package | library | Observed | Groups 1 file(s) under analyzer.js package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| BundleAnalyzerPlugin.js package | library | Observed | Groups 1 file(s) under bundleanalyzerplugin.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 24 file(s) under external integrations (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Logger.js package | library | Observed | Groups 1 file(s) under logger.js package (observed from repository paths and static analysis). |
| parseUtils.js package | library | Observed | Groups 1 file(s) under parseutils.js package (observed from repository paths and static analysis). |
| sizeUtils.js package | library | Observed | Groups 1 file(s) under sizeutils.js package (observed from repository paths and static analysis). |
| statsUtils.js package | library | Observed | Groups 1 file(s) under statsutils.js package (observed from repository paths and static analysis). |
| template.js package | library | Observed | Groups 1 file(s) under template.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 130 file(s) under tests (observed from repository paths and static analysis). |
| tree package | library | Observed | Groups 8 file(s) under tree package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| viewer.js package | library | Observed | Groups 1 file(s) under viewer.js package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.npm-upgrade.json` (config)
- `client/.eslintrc.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 130 analysed file(s)
- `client` — 49 analysed file(s)
- `src` — 19 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.changeset` — 6 analysed file(s)
- `.github` — 2 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f65668c9ab4ffe4b1989e5badbba3e0e871e1a24` is the revision these paths and observations refer to.
