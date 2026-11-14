# Project structure: Shopify/draggable

**Analysed commit:** `8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d`

**Commit reference:** [8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d](https://github.com/Shopify/draggable/commit/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d)

**Tree at this commit:** [Shopify/draggable@8a1eed57f3ab](https://github.com/Shopify/draggable/tree/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Shopify/draggable |
| Description | The JavaScript Drag & Drop library your grandparents warned you about. |
| Stars | 18456 |
| Forks | 1115 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d` |
| Retrieved at | 2026-11-14T19:11:21.789435+00:00 |
| Files in this snapshot | 347 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (9 files)
  workflows/  (5 files)
    changelog.yml
    ci.yml
    cla.yml
    release.yml
    snapit.yml
  .probots.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yaml
.vscode/  (3 files)
  extensions.json
  launch.json
  settings.json
config/  (1 files)
  typescript/  (1 files)
    rollup-plugin-includepaths.d.ts
doc/  (1 files)
  typescript.md
examples/  (167 files)
  .vscode/  (2 files)
    extensions.json
    settings.json
  src/  (142 files)
    components/  (61 files)
      … 61 files under this directory
    content/  (41 files)
      … 41 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    styles/  (22 files)
      … 22 files under this directory
    views/  (15 files)
      … 15 files under this directory
  tools/  (9 files)
    tasks/  (4 files)
      … 4 files under this directory
    index.js
    server.js
    watch.js
    webpack.config.js
    webpack.plugins.js
  .babelrc
  .browserslistrc
  .editorconfig
  .eslintignore
  .eslintrc.js
  .gitignore
  .nvmrc
  .prettierignore
  .prettierrc
  .stylelintignore
  .stylelintrc
  README.md
  package.json
  postcss.config.js
src/  (127 files)
  Draggable/  (57 files)
    DragEvent/  (4 files)
      … 4 files under this directory
    DraggableEvent/  (3 files)
      … 3 files under this directory
    Emitter/  (3 files)
      … 3 files under this directory
    Plugins/  (19 files)
      … 19 files under this directory
    Sensors/  (24 files)
      … 24 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    Draggable.js
    README.md
    index.js
  Droppable/  (7 files)
    DroppableEvent/  (3 files)
      … 3 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    Droppable.js
    README.md
    index.js
  Plugins/  (24 files)
    Collidable/  (6 files)
      … 6 files under this directory
    ResizeMirror/  (4 files)
      … 4 files under this directory
    Snappable/  (6 files)
      … 6 files under this directory
    SortAnimation/  (3 files)
      … 3 files under this directory
    SwapAnimation/  (3 files)
      … 3 files under this directory
    README.md
    index.js
  Sortable/  (7 files)
    SortableEvent/  (3 files)
      … 3 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    Sortable.js
    index.js
  Swappable/  (7 files)
    SwappableEvent/  (3 files)
      … 3 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    Swappable.js
    index.js
  shared/  (24 files)
    AbstractEvent/  (4 files)
      … 4 files under this directory
    AbstractPlugin/  (3 files)
      … 3 files under this directory
    utils/  (15 files)
      … 15 files under this directory
    README.md
    types.ts
  index.js
test/  (16 files)
  helpers/  (7 files)
    constants.ts
    environment.ts
    event.ts
    index.ts
    module.ts
    plugin.ts
    sensor.ts
  matchers/  (6 files)
    dom-event.ts
    event.ts
    index.ts
    order.ts
    sensor.ts
    utils.ts
  environment.ts
  helper.ts
  setup.ts
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.nvmrc
.prettierignore
.prettierrc
AUTHORS
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
README.md
babel.config.js
esdoc.json
index.d.ts
jest.config.js
package.json
rollup.config.ts
rollup.development.config.ts
tsconfig.json
```

## Entry points

- [examples/tools/index.js](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/examples/tools/index.js)
- [src/Draggable/DragEvent/index.ts](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Draggable/DragEvent/index.ts)
- [src/Draggable/DraggableEvent/index.ts](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Draggable/DraggableEvent/index.ts)
- [src/Draggable/Emitter/index.ts](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Draggable/Emitter/index.ts)
- [src/Draggable/Plugins/index.js](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Draggable/Plugins/index.js)
- [src/Draggable/Sensors/index.js](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Draggable/Sensors/index.js)
- [src/Draggable/index.js](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Draggable/index.js)
- [src/Droppable/DroppableEvent/index.ts](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Droppable/DroppableEvent/index.ts)
- [src/Droppable/index.js](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Droppable/index.js)
- [src/Plugins/Collidable/index.js](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Plugins/Collidable/index.js)
- [src/Plugins/ResizeMirror/index.ts](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Plugins/ResizeMirror/index.ts)
- [src/Plugins/Snappable/index.js](https://github.com/Shopify/draggable/blob/8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d/src/Plugins/Snappable/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Draggable package | library | Observed | Groups 32 file(s) under draggable package (observed from repository paths and static analysis). |
| Droppable package | library | Observed | Groups 4 file(s) under droppable package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Plugins package | library | Observed | Groups 15 file(s) under plugins package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 16 file(s) under shared package (observed from repository paths and static analysis). |
| Sortable package | library | Observed | Groups 4 file(s) under sortable package (observed from repository paths and static analysis). |
| Swappable package | library | Observed | Groups 4 file(s) under swappable package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 31 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/.probots.yml` (config)
- `.github/dependabot.yaml` (config)
- `.github/workflows/changelog.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/cla.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/snapit.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `esdoc.json` (config)
- `examples/.editorconfig` (config)
- `examples/.vscode/extensions.json` (config)
- `examples/.vscode/settings.json` (config)
- `examples/package.json` (manifest)
- `examples/src/views/data-pages.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `examples` — 167 analysed file(s)
- `src` — 127 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `test` — 16 analysed file(s)
- `.github` — 9 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `config` — 1 analysed file(s)
- `doc` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `8a1eed57f3ab2dff9371e8ce60fb39ac85871e8d` is the revision these paths and observations refer to.
