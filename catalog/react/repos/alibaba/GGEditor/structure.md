# Project structure: alibaba/GGEditor

**Analysed commit:** `68e4cb609a15428d93467564a31ea443e4da35c7`

**Commit reference:** [68e4cb609a15428d93467564a31ea443e4da35c7](https://github.com/alibaba/GGEditor/commit/68e4cb609a15428d93467564a31ea443e4da35c7)

**Tree at this commit:** [alibaba/GGEditor@68e4cb609a15](https://github.com/alibaba/GGEditor/tree/68e4cb609a15428d93467564a31ea443e4da35c7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alibaba/GGEditor |
| Description | A visual graph editor based on G6 and React |
| Stars | 3402 |
| Forks | 561 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `68e4cb609a15428d93467564a31ea443e4da35c7` |
| Retrieved at | 2026-11-14T19:15:19.967816+00:00 |
| Files in this snapshot | 130 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug.md
    feature.md
  workflows/  (1 files)
    gh-pages.yml
.vscode/  (1 files)
  settings.json
docs/  (26 files)
  examples/  (22 files)
    component/  (6 files)
      … 6 files under this directory
    editor/  (2 files)
      … 2 files under this directory
    graph/  (4 files)
      … 4 files under this directory
    plugin/  (6 files)
      … 6 files under this directory
    register/  (4 files)
      … 4 files under this directory
  guide/  (2 files)
    getting-started.md
    getting-started.zh-CN.md
  index.md
  index.zh-CN.md
examples/  (27 files)
  component/  (7 files)
    command/  (2 files)
      … 2 files under this directory
    detail-panel/  (3 files)
      … 3 files under this directory
    item-panel/  (2 files)
      … 2 files under this directory
  editor/  (4 files)
    context/  (4 files)
      … 4 files under this directory
  graph/  (4 files)
    flow/  (2 files)
      … 2 files under this directory
    mind/  (2 files)
      … 2 files under this directory
  plugin/  (6 files)
    context-menu/  (2 files)
      … 2 files under this directory
    editable-label/  (2 files)
      … 2 files under this directory
    item-popover/  (2 files)
      … 2 files under this directory
  register/  (4 files)
    dom-node/  (2 files)
      … 2 files under this directory
    node/  (2 files)
      … 2 files under this directory
  index.d.ts
  tsconfig.json
public/  (1 files)
  CNAME
scripts/  (1 files)
  build.js
src/  (56 files)
  common/  (7 files)
    CommandManager/  (1 files)
      … 1 files under this directory
    behaviorManager/  (1 files)
      … 1 files under this directory
    commandManager/  (1 files)
      … 1 files under this directory
    constants/  (1 files)
      … 1 files under this directory
    global/  (1 files)
      … 1 files under this directory
    interfaces/  (1 files)
      … 1 files under this directory
    withContext/  (1 files)
      … 1 files under this directory
  components/  (35 files)
    Command/  (1 files)
      … 1 files under this directory
    DetailPanel/  (1 files)
      … 1 files under this directory
    Editor/  (1 files)
      … 1 files under this directory
    EditorContext/  (1 files)
      … 1 files under this directory
    Flow/  (4 files)
      … 4 files under this directory
    Graph/  (18 files)
      … 18 files under this directory
    ItemPanel/  (2 files)
      … 2 files under this directory
    Mind/  (6 files)
      … 6 files under this directory
    Register/  (1 files)
      … 1 files under this directory
  helpers/  (1 files)
    index.ts
  plugins/  (3 files)
    ContextMenu/  (1 files)
      … 1 files under this directory
    EditableLabel/  (1 files)
      … 1 files under this directory
    ItemPopover/  (1 files)
      … 1 files under this directory
  shape/  (8 files)
    common/  (1 files)
      … 1 files under this directory
    edges/  (2 files)
      … 2 files under this directory
    nodes/  (3 files)
      … 3 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    index.ts
  utils/  (1 files)
    index.ts
  index.tsx
.eslintignore
.eslintrc.js
.gitignore
.prettierignore
.prettierrc.js
.travis.yml
.umirc.ts
CHANGELOG.md
LICENSE
README.en-US.md
README.md
babel.config.js
package.json
tsconfig.cjs.json
tsconfig.json
```

## Entry points

- [src/common/CommandManager/index.ts](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/common/CommandManager/index.ts)
- [src/common/behaviorManager/index.ts](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/common/behaviorManager/index.ts)
- [src/common/commandManager/index.ts](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/common/commandManager/index.ts)
- [src/common/constants/index.ts](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/common/constants/index.ts)
- [src/common/global/index.ts](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/common/global/index.ts)
- [src/common/interfaces/index.ts](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/common/interfaces/index.ts)
- [src/common/withContext/index.tsx](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/common/withContext/index.tsx)
- [src/components/Command/index.tsx](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/components/Command/index.tsx)
- [src/components/DetailPanel/index.tsx](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/components/DetailPanel/index.tsx)
- [src/components/Editor/index.tsx](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/components/Editor/index.tsx)
- [src/components/EditorContext/index.tsx](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/components/EditorContext/index.tsx)
- [src/components/Flow/index.tsx](https://github.com/alibaba/GGEditor/blob/68e4cb609a15428d93467564a31ea443e4da35c7/src/components/Flow/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| common package | library | Observed | Groups 7 file(s) under common package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 35 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 1 file(s) under helpers package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 3 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| shape package | library | Observed | Groups 8 file(s) under shape package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/gh-pages.yml` (ci)
- `.travis.yml` (ci)
- `.vscode/settings.json` (config)
- `examples/tsconfig.json` (config)
- `package.json` (manifest)
- `tsconfig.cjs.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 56 analysed file(s)
- `examples` — 27 analysed file(s)
- `docs` — 26 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `public` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `68e4cb609a15428d93467564a31ea443e4da35c7` is the revision these paths and observations refer to.
