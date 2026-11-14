# Project structure: svg/svgo

**Analysed commit:** `31194fb4b3b592d7a65956f8f3b343b9fd6b80a6`

**Commit reference:** [31194fb4b3b592d7a65956f8f3b343b9fd6b80a6](https://github.com/svg/svgo/commit/31194fb4b3b592d7a65956f8f3b343b9fd6b80a6)

**Tree at this commit:** [svg/svgo@31194fb4b3b5](https://github.com/svg/svgo/tree/31194fb4b3b592d7a65956f8f3b343b9fd6b80a6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | svg/svgo |
| Description | SVG Optimizer for Node.js and CLI. ⚙️ |
| Stars | 22817 |
| Forks | 1491 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `31194fb4b3b592d7a65956f8f3b343b9fd6b80a6` |
| Retrieved at | 2026-11-14T19:11:07.285695+00:00 |
| Files in this snapshot | 616 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    config.yml
    feature_request.md
    plugin_request.md
  workflows/  (4 files)
    ci.yml
    codeql.yml
    publish.yml
    regression.yml
  dependabot.yml
bin/  (1 files)
  svgo.js
docs/  (63 files)
  02-usage/  (3 files)
    01-node.mdx
    02-browser.mdx
    index.mdx
  04-plugins/  (54 files)
    addAttributesToSVGElement.mdx
    addClassesToSVGElement.mdx
    cleanupAttrs.mdx
    cleanupEnableBackground.mdx
    cleanupIds.mdx
    cleanupListOfValues.mdx
    cleanupNumericValues.mdx
    collapseGroups.mdx
    convertColors.mdx
    convertEllipseToCircle.mdx
    convertOneStopGradients.mdx
    convertPathData.mdx
    convertShapeToPath.mdx
    convertStyleToAttrs.mdx
    convertTransform.mdx
    index.mdx
    inlineStyles.mdx
    mergePaths.mdx
    mergeStyles.mdx
    minifyStyles.mdx
    moveElemsAttrsToGroup.mdx
    moveGroupAttrsToElems.mdx
    prefixIds.mdx
    removeAttributesBySelector.mdx
    … 30 more files
  06-migrations/  (3 files)
    01-migration-from-v3-to-v4.mdx
    02-migration-from-v2-to-v3.mdx
    _category_.json
  01-index.mdx
  03-preset-default.mdx
  05-plugins-api.mdx
lib/  (23 files)
  svgo/  (4 files)
    coa.js
    css-select-adapter.js
    plugins.js
    tools.js
  util/  (2 files)
    map-nodes-to-parents.js
    visit.js
  builtin.js
  parser.js
  parser.test.js
  path.js
  path.test.js
  stringifier.js
  style.js
  style.test.js
  svgo-node.js
  svgo-node.test.js
  svgo.js
  svgo.test.js
  types.js
  types.ts
  version.js
  xast.js
  xast.test.js
logo/  (5 files)
  isotype-white.svg
  isotype.svg
  logo-web.svg
  logo-white.svg
  logo.svg
patches/  (1 files)
  sax@1.6.1.patch
plugins/  (58 files)
  _collections.js
  _path.js
  _transforms.js
  addAttributesToSVGElement.js
  addClassesToSVGElement.js
  applyTransforms.js
  cleanupAttrs.js
  cleanupEnableBackground.js
  cleanupIds.js
  cleanupListOfValues.js
  cleanupNumericValues.js
  collapseGroups.js
  convertColors.js
  convertEllipseToCircle.js
  convertOneStopGradients.js
  convertPathData.js
  convertShapeToPath.js
  convertStyleToAttrs.js
  convertTransform.js
  inlineStyles.js
  mergePaths.js
  mergeStyles.js
  minifyStyles.js
  moveElemsAttrsToGroup.js
  … 34 more files
scripts/  (1 files)
  sync-version.js
test/  (440 files)
  cli/  (3 files)
    cli.test.js
    invalid.svg
    single.svg
  coa/  (9 files)
    testFolderWithNoSvg/  (1 files)
      … 1 files under this directory
    testSvg/  (2 files)
      … 2 files under this directory
    testSvgDatauri/  (1 files)
      … 1 files under this directory
    testSvgRecursively/  (4 files)
      … 4 files under this directory
    _index.test.js
  fixtures/  (10 files)
    config-loader/  (10 files)
      … 10 files under this directory
  plugins/  (386 files)
    _collections.test.js
    _index.test.js
    _transforms.test.js
    addAttributesToSVGElement.01.svg.txt
    addAttributesToSVGElement.02.svg.txt
    addAttributesToSVGElement.03.svg.txt
    addAttributesToSVGElement.04.svg.txt
    addClassesToSVGElement.01.svg.txt
    addClassesToSVGElement.02.svg.txt
    addClassesToSVGElement.03.svg.txt
    addClassesToSVGElement.test.js
    cleanupAttrs.01.svg.txt
    cleanupAttrs.02.svg.txt
    cleanupEnableBackground.01.svg.txt
    cleanupEnableBackground.02.svg.txt
    cleanupEnableBackground.03.svg.txt
    cleanupEnableBackground.04.svg.txt
    cleanupEnableBackground.05.svg.txt
    cleanupIds.01.svg.txt
    cleanupIds.02.svg.txt
    cleanupIds.03.svg.txt
    cleanupIds.04.svg.txt
    cleanupIds.05.svg.txt
    cleanupIds.06.svg.txt
    … 362 more files
  regression/  (14 files)
    lists/  (3 files)
      … 3 files under this directory
    compare-worker.js
    compare-worker.test.js
    compare.js
    compare.test.js
    delta.js
    extract.js
    file-lists.js
    lib.js
    optimize-worker.js
    optimize.js
    regression-io.js
  svg2js/  (2 files)
    _index.test.js
    test.svg
  svgo/  (13 files)
    _index.test.js
    billion-laughs-flat.svg
    billion-laughs.svg
    billion-laughs.test.js
    entities.svg.txt
    invalid.svg
    keyframe-selectors.svg.txt
    plugins-order.svg.txt
    pre-element-pretty.svg.txt
    pre-element.svg.txt
    style-specificity.svg.txt
    test.svg.txt
    whitespaces.svg.txt
  types/  (1 files)
    lib/  (1 files)
      … 1 files under this directory
  browser.js
  svgo.cjs
.gitattributes
.gitignore
.prettierignore
.prettierrc
CONTRIBUTING.md
LICENSE
README.md
cspell.jsonc
eslint.config.mjs
package.json
pnpm-workspace.yaml
rollup.config.js
tsconfig.build.json
tsconfig.json
vitest.config.js
```

## Entry points

- [bin/svgo.js](https://github.com/svg/svgo/blob/31194fb4b3b592d7a65956f8f3b343b9fd6b80a6/bin/svgo.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 23 file(s) under lib package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 58 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 440 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/regression.yml` (ci)
- `docs/06-migrations/_category_.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 440 analysed file(s)
- `docs` — 63 analysed file(s)
- `plugins` — 58 analysed file(s)
- `lib` — 23 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 9 analysed file(s)
- `logo` — 5 analysed file(s)
- `bin` — 1 analysed file(s)
- `patches` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `31194fb4b3b592d7a65956f8f3b343b9fd6b80a6` is the revision these paths and observations refer to.
