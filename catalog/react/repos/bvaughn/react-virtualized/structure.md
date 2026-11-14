# Project structure: bvaughn/react-virtualized

**Analysed commit:** `d54281d5d4f0e93746009a5513ce350ced8ef4bf`

**Commit reference:** [d54281d5d4f0e93746009a5513ce350ced8ef4bf](https://github.com/bvaughn/react-virtualized/commit/d54281d5d4f0e93746009a5513ce350ced8ef4bf)

**Tree at this commit:** [bvaughn/react-virtualized@d54281d5d4f0](https://github.com/bvaughn/react-virtualized/tree/d54281d5d4f0e93746009a5513ce350ced8ef4bf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bvaughn/react-virtualized |
| Description | React components for efficiently rendering large lists and tabular data |
| Stars | 27067 |
| Forks | 3009 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `d54281d5d4f0e93746009a5513ce350ced8ef4bf` |
| Retrieved at | 2026-11-14T19:13:04.696652+00:00 |
| Files in this snapshot | 404 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    feature-request.md
    question.md
  workflows/  (6 files)
    eslint.yml
    playwright.yml
    prettier.yml
    stale.yml
    typescript.yml
    vitest.yml
  PULL_REQUEST_TEMPLATE.md
codemods/  (2 files)
  6-to-7/  (1 files)
    rename-properties.js
  7-to-8/  (1 files)
    rename-components.js
integrations/  (25 files)
  tests/  (10 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (7 files)
      … 7 files under this directory
    package.json
    playwright.config.ts
  vite/  (15 files)
    src/  (10 files)
      … 10 files under this directory
    index.html
    package.json
    tsconfig.json
    tsconfig.tsbuildinfo
    vite.config.ts
lib/  (103 files)
  components/  (77 files)
    ArrowKeyStepper/  (4 files)
      … 4 files under this directory
    CellMeasurer/  (6 files)
      … 6 files under this directory
    ColumnSizer/  (3 files)
      … 3 files under this directory
    Grid/  (21 files)
      … 21 files under this directory
    InfiniteLoader/  (5 files)
      … 5 files under this directory
    List/  (4 files)
      … 4 files under this directory
    Masonry/  (9 files)
      … 9 files under this directory
    MultiGrid/  (6 files)
      … 6 files under this directory
    ScrollSync/  (3 files)
      … 3 files under this directory
    Table/  (16 files)
      … 16 files under this directory
  utils/  (24 files)
    scrollElement/  (10 files)
      … 10 files under this directory
    test/  (3 files)
      … 3 files under this directory
    TestHelper.ts
    animationFrame.ts
    createCallbackMemoizer.test.ts
    createCallbackMemoizer.ts
    createInnerGridRef.test.ts
    createInnerGridRef.ts
    getUpdatedOffsetForIndex.test.ts
    getUpdatedOffsetForIndex.ts
    initCellMetadata.ts
    requestAnimationTimeout.ts
    useIsomorphicLayoutEffect.ts
  index.ts
  styles.css
public/  (100 files)
  generated/  (97 files)
    docs/  (20 files)
      … 20 files under this directory
    examples/  (77 files)
      … 77 files under this directory
  favicon.svg
  og.svg
  robots.txt
scripts/  (5 files)
  docs-stubs/  (1 files)
    CellMeasurerCacheOptions.tsx
  compile-docs.ts
  compile-examples.ts
  compile-search-index.ts
  compress-og-image.ts
src/  (139 files)
  components/  (2 files)
    Link.tsx
    Methods.tsx
  routes/  (132 files)
    cell-measurer/  (15 files)
      … 15 files under this directory
    grid/  (20 files)
      … 20 files under this directory
    guides/  (29 files)
      … 29 files under this directory
    hoc/  (12 files)
      … 12 files under this directory
    list/  (15 files)
      … 15 files under this directory
    masonry/  (11 files)
      … 11 files under this directory
    table/  (16 files)
      … 16 files under this directory
    window-scrolling/  (13 files)
      … 13 files under this directory
    types.ts
  utils/  (1 files)
    data.ts
  App.tsx
  constants.ts
  routes.ts
  vite-env.d.ts
.gitignore
.prettierignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
eslint.config.js
index.css
index.html
index.tsx
package.json
pnpm-workspace.yaml
postcss.config.js
prettier.config.js
tsconfig.json
vercel.json
vite.config.ts
vitest.config.ts
vitest.setup.ts
```

## Entry points

- [integrations/tests/src/index.ts](https://github.com/bvaughn/react-virtualized/blob/d54281d5d4f0e93746009a5513ce350ced8ef4bf/integrations/tests/src/index.ts)
- [index.tsx](https://github.com/bvaughn/react-virtualized/blob/d54281d5d4f0e93746009a5513ce350ced8ef4bf/index.tsx)
- [integrations/vite/src/main.tsx](https://github.com/bvaughn/react-virtualized/blob/d54281d5d4f0e93746009a5513ce350ced8ef4bf/integrations/vite/src/main.tsx)
- [lib/index.ts](https://github.com/bvaughn/react-virtualized/blob/d54281d5d4f0e93746009a5513ce350ced8ef4bf/lib/index.ts)
- [src/App.tsx](https://github.com/bvaughn/react-virtualized/blob/d54281d5d4f0e93746009a5513ce350ced8ef4bf/src/App.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 135 file(s) under api layer (observed from repository paths and static analysis). |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| codemods package | library | Observed | Groups 2 file(s) under codemods package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 2 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 103 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.ts package | library | Observed | Groups 1 file(s) under constants.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 6 file(s) under external integrations (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 99 file(s) under lib package (observed from repository paths and static analysis). |
| routes.ts package | library | Observed | Groups 1 file(s) under routes.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 13 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |
| vite-env.d.ts package | library | Observed | Groups 1 file(s) under vite-env.d.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/eslint.yml` (ci)
- `.github/workflows/playwright.yml` (ci)
- `.github/workflows/prettier.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/typescript.yml` (ci)
- `.github/workflows/vitest.yml` (ci)
- `integrations/vite/package.json` (manifest)
- `integrations/vite/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `public/generated/docs/ArrowKeyStepper.json` (config)
- `public/generated/docs/ArrowKeyStepperImperativeAPI.json` (config)
- `public/generated/docs/CellMeasurer.json` (config)
- `public/generated/docs/CellMeasurerCacheAPI.json` (config)
- `public/generated/docs/CellMeasurerCacheOptions.json` (config)
- `public/generated/docs/Column.json` (config)
- `public/generated/docs/ColumnSizer.json` (config)
- `public/generated/docs/Grid.json` (config)
- `public/generated/docs/GridImperativeAPI.json` (config)
- `public/generated/docs/InfiniteLoader.json` (config)
- `public/generated/docs/InfiniteLoaderImperativeAPI.json` (config)
- `public/generated/docs/List.json` (config)
- `public/generated/docs/ListImperativeAPI.json` (config)
- `public/generated/docs/Masonry.json` (config)
- `public/generated/docs/MasonryImperativeAPI.json` (config)
- `public/generated/docs/MultiGrid.json` (config)
- `public/generated/docs/MultiGridImperativeAPI.json` (config)
- `public/generated/docs/ScrollSync.json` (config)
- `public/generated/docs/Table.json` (config)
- `public/generated/docs/TableImperativeAPI.json` (config)
- `public/generated/examples/ArrowKeyStepperControlled.json` (config)
- `public/generated/examples/ArrowKeyStepperGrid.json` (config)
- `public/generated/examples/AutoSizerGrid.json` (config)
- `public/generated/examples/AutoSizerList.json` (config)
- `public/generated/examples/AutoSizerTable.json` (config)
- `public/generated/examples/CellMeasurerCacheClear.json` (config)
- `public/generated/examples/CellMeasurerDynamicHeightGrid.json` (config)
- `public/generated/examples/CellMeasurerDynamicHeightList.json` (config)
- `public/generated/examples/CellMeasurerDynamicHeightTableColumn.json` (config)
- `public/generated/examples/CellMeasurerDynamicWidthGrid.json` (config)
- `public/generated/examples/CellMeasurerDynamicWidthMultiGrid.json` (config)
- `public/generated/examples/CellMeasurerFunctionComponent.json` (config)
- `public/generated/examples/CellMeasurerImages.json` (config)
- `public/generated/examples/CellMeasurerKeyMapper.json` (config)
- `public/generated/examples/ColumnSizerGrid.json` (config)
- `public/generated/examples/CustomizingStylesClassNames.json` (config)
- `public/generated/examples/CustomizingStylesCssModules.json` (config)
- `public/generated/examples/CustomizingStylesCssModules.module.json` (config)
- `public/generated/examples/CustomizingStylesGlobal.json` (config)
- `public/generated/examples/CustomizingStylesImport.json` (config)
- `public/generated/examples/CustomizingStylesInlineStyles.json` (config)
- `public/generated/examples/GridBasic.json` (config)
- `public/generated/examples/GridCellRangeRenderer.json` (config)
- `public/generated/examples/GridCellRenderer.json` (config)
- `public/generated/examples/GridMethodsRef.json` (config)
- `public/generated/examples/GridOverscanIndicesGetter.json` (config)
- `public/generated/examples/GridScrollToCell.json` (config)
- `public/generated/examples/GridVariableSizes.json` (config)
- `public/generated/examples/InfiniteLoaderBasic.json` (config)
- `public/generated/examples/InfiniteLoaderGrid.json` (config)
- `public/generated/examples/InfiniteLoaderList.json` (config)
- `public/generated/examples/InfiniteLoaderResetCache.json` (config)
- `public/generated/examples/InfiniteLoadingList.json` (config)
- `public/generated/examples/InfiniteLoadingListDemo.json` (config)
- `public/generated/examples/ListBasic.json` (config)
- `public/generated/examples/ListMethods.json` (config)
- `public/generated/examples/ListNoRows.json` (config)
- `public/generated/examples/ListRecomputeRowHeights.json` (config)
- `public/generated/examples/ListRowRenderer.json` (config)
- `public/generated/examples/ListScrollToRow.json` (config)
- `public/generated/examples/ListScrollingPlaceholder.json` (config)
- `public/generated/examples/ListVariableRowHeights.json` (config)
- `public/generated/examples/MasonryCellPositioner.json` (config)
- `public/generated/examples/MasonryCellPositionerReset.json` (config)
- `public/generated/examples/MasonryCustomPositioner.json` (config)
- `public/generated/examples/MasonryExample.json` (config)
- `public/generated/examples/MultiColumnSortTable.json` (config)
- `public/generated/examples/MultiColumnSortTableCallback.json` (config)
- `public/generated/examples/MultiColumnSortTableDefaults.json` (config)
- `public/generated/examples/MultiGridFixedRowsAndColumns.json` (config)
- `public/generated/examples/NaturalSortTable.json` (config)
- `public/generated/examples/OverscanDemo.json` (config)
- `public/generated/examples/ReverseList.json` (config)
- `public/generated/examples/ScrollSyncSpreadsheet.json` (config)
- `public/generated/examples/ServerRenderingInitialScroll.json` (config)
- `public/generated/examples/ServerRenderingSizes.json` (config)
- `public/generated/examples/SortIndicatorHeader.json` (config)
- `public/generated/examples/SortTableBasic.json` (config)
- `public/generated/examples/TableBasic.json` (config)
- `public/generated/examples/TableColumnRenderers.json` (config)
- `public/generated/examples/TableFullFeatured.json` (config)
- `public/generated/examples/TableImperativeMethods.json` (config)
- `public/generated/examples/TableRowRenderer.json` (config)
- `public/generated/examples/UsingAutoSizerChildComponent.json` (config)
- `public/generated/examples/UsingAutoSizerFlexContainer.json` (config)
- `public/generated/examples/UsingAutoSizerInfiniteLoader.json` (config)
- `public/generated/examples/UsingAutoSizerWidthOnly.json` (config)
- `public/generated/examples/WindowScrollingContentAbove.json` (config)
- `public/generated/examples/WindowScrollingGrid.json` (config)
- `public/generated/examples/WindowScrollingList.json` (config)
- `public/generated/examples/WindowScrollingMasonry.json` (config)
- `public/generated/examples/WindowScrollingMigrationAfter.json` (config)
- `public/generated/examples/WindowScrollingMigrationBefore.json` (config)
- `public/generated/examples/WindowScrollingScrollElement.json` (config)
- `public/generated/examples/WindowScrollingScrollToRow.json` (config)
- `public/generated/examples/WindowScrollingSmoothScroll.json` (config)
- `public/generated/examples/WindowScrollingTable.json` (config)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `src` — 139 analysed file(s)
- `lib` — 103 analysed file(s)
- `public` — 100 analysed file(s)
- `integrations` — 25 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 10 analysed file(s)
- `scripts` — 5 analysed file(s)
- `codemods` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (1 x lockfile excluded; 3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d54281d5d4f0e93746009a5513ce350ced8ef4bf` is the revision these paths and observations refer to.
