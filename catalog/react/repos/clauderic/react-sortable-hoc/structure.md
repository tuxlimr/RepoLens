# Project structure: clauderic/react-sortable-hoc

**Analysed commit:** `caf3c4f5bfb30894639391ae75c1bfc2b707a127`

**Commit reference:** [caf3c4f5bfb30894639391ae75c1bfc2b707a127](https://github.com/clauderic/react-sortable-hoc/commit/caf3c4f5bfb30894639391ae75c1bfc2b707a127)

**Tree at this commit:** [clauderic/react-sortable-hoc@caf3c4f5bfb3](https://github.com/clauderic/react-sortable-hoc/tree/caf3c4f5bfb30894639391ae75c1bfc2b707a127)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | clauderic/react-sortable-hoc |
| Description | A set of higher-order components to turn any list into an animated, accessible and touch-friendly sortable list✌️ |
| Stars | 10879 |
| Forks | 953 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `caf3c4f5bfb30894639391ae75c1bfc2b707a127` |
| Retrieved at | 2026-11-14T19:13:28.717742+00:00 |
| Files in this snapshot | 50 |

## Directory tree

```text
.codesandbox/  (1 files)
  ci.json
.github/  (1 files)
  assets/  (1 files)
    dnd-kit-banner.svg
.storybook/  (4 files)
  config.js
  manager-head.html
  theme.js
  webpack.config.js
examples/  (7 files)
  .eslintrc.json
  basic.js
  collections.js
  drag-handle.js
  react-infinite.js
  react-virtualized-table-columns.js
  react-virtualized.js
src/  (25 files)
  .stories/  (15 files)
    grouping-items/  (8 files)
      … 8 files under this directory
    interactive-elements-stress-test/  (5 files)
      … 5 files under this directory
    Storybook.scss
    index.js
  AutoScroller/  (1 files)
    index.js
  Manager/  (1 files)
    index.js
  SortableContainer/  (4 files)
    defaultGetHelperDimensions.js
    defaultShouldCancelStart.js
    index.js
    props.js
  SortableElement/  (1 files)
    index.js
  SortableHandle/  (1 files)
    index.js
  index.js
  utils.js
types/  (1 files)
  index.d.ts
.editorconfig
.eslintrc.json
.gitignore
.npmignore
.prettierrc
.travis.yml
CHANGELOG.md
LICENSE
README.md
package.json
rollup.config.js
```

## Entry points

- [src/.stories/grouping-items/index.js](https://github.com/clauderic/react-sortable-hoc/blob/caf3c4f5bfb30894639391ae75c1bfc2b707a127/src/.stories/grouping-items/index.js)
- [src/.stories/index.js](https://github.com/clauderic/react-sortable-hoc/blob/caf3c4f5bfb30894639391ae75c1bfc2b707a127/src/.stories/index.js)
- [src/.stories/interactive-elements-stress-test/index.js](https://github.com/clauderic/react-sortable-hoc/blob/caf3c4f5bfb30894639391ae75c1bfc2b707a127/src/.stories/interactive-elements-stress-test/index.js)
- [src/AutoScroller/index.js](https://github.com/clauderic/react-sortable-hoc/blob/caf3c4f5bfb30894639391ae75c1bfc2b707a127/src/AutoScroller/index.js)
- [src/Manager/index.js](https://github.com/clauderic/react-sortable-hoc/blob/caf3c4f5bfb30894639391ae75c1bfc2b707a127/src/Manager/index.js)
- [src/SortableContainer/index.js](https://github.com/clauderic/react-sortable-hoc/blob/caf3c4f5bfb30894639391ae75c1bfc2b707a127/src/SortableContainer/index.js)
- [src/SortableElement/index.js](https://github.com/clauderic/react-sortable-hoc/blob/caf3c4f5bfb30894639391ae75c1bfc2b707a127/src/SortableElement/index.js)
- [src/SortableHandle/index.js](https://github.com/clauderic/react-sortable-hoc/blob/caf3c4f5bfb30894639391ae75c1bfc2b707a127/src/SortableHandle/index.js)
- [src/index.js](https://github.com/clauderic/react-sortable-hoc/blob/caf3c4f5bfb30894639391ae75c1bfc2b707a127/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| AutoScroller package | library | Observed | Groups 1 file(s) under autoscroller package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Manager package | library | Observed | Groups 1 file(s) under manager package (observed from repository paths and static analysis). |
| SortableContainer package | library | Observed | Groups 4 file(s) under sortablecontainer package (observed from repository paths and static analysis). |
| SortableElement package | library | Observed | Groups 1 file(s) under sortableelement package (observed from repository paths and static analysis). |
| SortableHandle package | library | Observed | Groups 1 file(s) under sortablehandle package (observed from repository paths and static analysis). |
| .stories package | library | Observed | Groups 11 file(s) under .stories package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |

## Important files

- `.codesandbox/ci.json` (config)
- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.travis.yml` (ci)
- `examples/.eslintrc.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 25 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `examples` — 7 analysed file(s)
- `.storybook` — 4 analysed file(s)
- `.codesandbox` — 1 analysed file(s)
- `.github` — 1 analysed file(s)
- `types` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `caf3c4f5bfb30894639391ae75c1bfc2b707a127` is the revision these paths and observations refer to.
