# Project structure: frontend-collective/react-sortable-tree

**Analysed commit:** `f482bc7f2853c698cad08fc75bb6fd3e36f2f79a`

**Commit reference:** [f482bc7f2853c698cad08fc75bb6fd3e36f2f79a](https://github.com/frontend-collective/react-sortable-tree/commit/f482bc7f2853c698cad08fc75bb6fd3e36f2f79a)

**Tree at this commit:** [frontend-collective/react-sortable-tree@f482bc7f2853](https://github.com/frontend-collective/react-sortable-tree/tree/f482bc7f2853c698cad08fc75bb6fd3e36f2f79a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | frontend-collective/react-sortable-tree |
| Description | Drag-and-drop sortable component for nested data and hierarchies |
| Stars | 4959 |
| Forks | 911 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f482bc7f2853c698cad08fc75bb6fd3e36f2f79a` |
| Retrieved at | 2026-11-14T19:14:33.465171+00:00 |
| Files in this snapshot | 67 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    feature-request.md
  FUNDING.yml
.storybook/  (2 files)
  main.js
  manager.js
__mocks__/  (4 files)
  fileMock.js
  react-dnd-html5-backend.js
  react-dnd-scrollzone.js
  react-virtualized.js
src/  (22 files)
  __snapshots__/  (1 files)
    react-sortable-tree.test.js.snap
  utils/  (9 files)
    classnames.js
    default-handlers.js
    dnd-manager.js
    generic-utils.js
    generic-utils.test.js
    memoized-tree-data-utils.js
    memoized-tree-data-utils.test.js
    tree-data-utils.js
    tree-data-utils.test.js
  index.js
  node-renderer-default.css
  node-renderer-default.js
  placeholder-renderer-default.css
  placeholder-renderer-default.js
  react-sortable-tree.css
  react-sortable-tree.js
  react-sortable-tree.test.js
  tests.js
  tree-node.css
  tree-node.js
  tree-placeholder.js
stories/  (21 files)
  __snapshots__/  (1 files)
    storyshots.test.js.snap
  add-remove.js
  barebones-no-context.js
  barebones.js
  callbacks.js
  can-drop.js
  childless-nodes.js
  drag-out-to-remove.js
  external-node.js
  generate-node-props.js
  generic.css
  index.js
  modify-nodes.js
  only-expand-searched-node.js
  rtl-support.js
  search.js
  storyshots.test.js
  themes.js
  touch-support.js
  tree-data-io.js
  tree-to-tree.js
test-config/  (2 files)
  shim.js
  test-setup.js
.babelrc.js
.eslintrc.js
.gitignore
.nvmrc
.prettierignore
.prettierrc
.travis.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
README.md
package.json
rollup.config.js
```

## Entry points

- [.storybook/main.js](https://github.com/frontend-collective/react-sortable-tree/blob/f482bc7f2853c698cad08fc75bb6fd3e36f2f79a/.storybook/main.js)
- [src/index.js](https://github.com/frontend-collective/react-sortable-tree/blob/f482bc7f2853c698cad08fc75bb6fd3e36f2f79a/src/index.js)
- [stories/index.js](https://github.com/frontend-collective/react-sortable-tree/blob/f482bc7f2853c698cad08fc75bb6fd3e36f2f79a/stories/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 4 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| node-renderer-default.js package | library | Observed | Groups 1 file(s) under node-renderer-default.js package (observed from repository paths and static analysis). |
| placeholder-renderer-default.js package | library | Observed | Groups 1 file(s) under placeholder-renderer-default.js package (observed from repository paths and static analysis). |
| react-sortable-tree.js package | library | Observed | Groups 1 file(s) under react-sortable-tree.js package (observed from repository paths and static analysis). |
| react-sortable-tree.test.js package | library | Observed | Groups 1 file(s) under react-sortable-tree.test.js package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 19 file(s) under stories package (observed from repository paths and static analysis). |
| test-config package | library | Observed | Groups 2 file(s) under test-config package (observed from repository paths and static analysis). |
| tests.js package | library | Observed | Groups 1 file(s) under tests.js package (observed from repository paths and static analysis). |
| tree-node.js package | library | Observed | Groups 1 file(s) under tree-node.js package (observed from repository paths and static analysis). |
| tree-placeholder.js package | library | Observed | Groups 1 file(s) under tree-placeholder.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 9 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 22 analysed file(s)
- `stories` — 21 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `__mocks__` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `.storybook` — 2 analysed file(s)
- `test-config` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f482bc7f2853c698cad08fc75bb6fd3e36f2f79a` is the revision these paths and observations refer to.
