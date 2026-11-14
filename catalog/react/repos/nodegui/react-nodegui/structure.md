# Project structure: nodegui/react-nodegui

**Analysed commit:** `87c844050c86e0eb548c3e6e8c57bd40d5174546`

**Commit reference:** [87c844050c86e0eb548c3e6e8c57bd40d5174546](https://github.com/nodegui/react-nodegui/commit/87c844050c86e0eb548c3e6e8c57bd40d5174546)

**Tree at this commit:** [nodegui/react-nodegui@87c844050c86](https://github.com/nodegui/react-nodegui/tree/87c844050c86e0eb548c3e6e8c57bd40d5174546)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nodegui/react-nodegui |
| Description | Build performant, native and cross-platform desktop applications with native React + powerful CSS like styling.🚀 |
| Stars | 6178 |
| Forks | 179 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `87c844050c86e0eb548c3e6e8c57bd40d5174546` |
| Retrieved at | 2026-11-14T19:14:09.090792+00:00 |
| Files in this snapshot | 178 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    docs.yml
examples/  (1 files)
  README.md
src/  (87 files)
  components/  (79 files)
    AbstractComponents/  (1 files)
      … 1 files under this directory
    Action/  (2 files)
      … 2 files under this directory
    AnimatedImage/  (2 files)
      … 2 files under this directory
    BoxView/  (2 files)
      … 2 files under this directory
    Button/  (2 files)
      … 2 files under this directory
    Calendar/  (2 files)
      … 2 files under this directory
    CheckBox/  (2 files)
      … 2 files under this directory
    ColorDialog/  (2 files)
      … 2 files under this directory
    ComboBox/  (2 files)
      … 2 files under this directory
    Dial/  (2 files)
      … 2 files under this directory
    Dialog/  (2 files)
      … 2 files under this directory
    ErrorPrompt/  (2 files)
      … 2 files under this directory
    FileDialog/  (2 files)
      … 2 files under this directory
    FontDialog/  (2 files)
      … 2 files under this directory
    GridView/  (7 files)
      … 7 files under this directory
    Image/  (2 files)
      … 2 files under this directory
    InputDialog/  (2 files)
      … 2 files under this directory
    LineEdit/  (2 files)
      … 2 files under this directory
    List/  (2 files)
      … 2 files under this directory
    ListItem/  (2 files)
      … 2 files under this directory
    Menu/  (2 files)
      … 2 files under this directory
    MenuBar/  (2 files)
      … 2 files under this directory
    PlainTextEdit/  (2 files)
      … 2 files under this directory
    ProgressBar/  (2 files)
      … 2 files under this directory
    ProgressDialog/  (2 files)
      … 2 files under this directory
    RadioButton/  (2 files)
      … 2 files under this directory
    ScrollArea/  (2 files)
      … 2 files under this directory
    Slider/  (2 files)
      … 2 files under this directory
    SpinBox/  (2 files)
      … 2 files under this directory
    SystemTrayIcon/  (2 files)
      … 2 files under this directory
    Tab/  (2 files)
      … 2 files under this directory
    TabItem/  (2 files)
      … 2 files under this directory
    Table/  (2 files)
      … 2 files under this directory
    TableItem/  (2 files)
      … 2 files under this directory
    Text/  (2 files)
      … 2 files under this directory
    View/  (2 files)
      … 2 files under this directory
    Window/  (2 files)
      … 2 files under this directory
    config.ts
  development/  (2 files)
    hot-reload.ts
    types.ts
  hooks/  (1 files)
    index.ts
  reconciler/  (1 files)
    index.ts
  renderer/  (1 files)
    index.ts
  utils/  (1 files)
    helpers.ts
  demo.tsx
  index.ts
website/  (80 files)
  blog/  (1 files)
    2019-05-30-welcome.md
  docs/  (52 files)
    api/  (36 files)
      … 36 files under this directory
    guides/  (13 files)
      … 13 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    doc1.md
    mdx.md
  src/  (12 files)
    components/  (9 files)
      … 9 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
  static/  (9 files)
    img/  (8 files)
      … 8 files under this directory
    CNAME
  website/  (1 files)
    sidebars.js
  .gitignore
  README.md
  docusaurus.config.js
  package.json
  sidebars.js
.all-contributorsrc
.gitignore
.npmignore
LICENSE
README.md
package.json
tsconfig.json
```

## Entry points

- [src/components/Action/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/Action/index.ts)
- [src/components/AnimatedImage/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/AnimatedImage/index.ts)
- [src/components/BoxView/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/BoxView/index.ts)
- [src/components/Button/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/Button/index.ts)
- [src/components/Calendar/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/Calendar/index.ts)
- [src/components/CheckBox/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/CheckBox/index.ts)
- [src/components/ColorDialog/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/ColorDialog/index.ts)
- [src/components/ComboBox/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/ComboBox/index.ts)
- [src/components/Dial/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/Dial/index.ts)
- [src/components/Dialog/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/Dialog/index.ts)
- [src/components/ErrorPrompt/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/ErrorPrompt/index.ts)
- [src/components/FileDialog/index.ts](https://github.com/nodegui/react-nodegui/blob/87c844050c86e0eb548c3e6e8c57bd40d5174546/src/components/FileDialog/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 79 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| demo.tsx package | library | Observed | Groups 1 file(s) under demo.tsx package (observed from repository paths and static analysis). |
| development package | library | Observed | Groups 2 file(s) under development package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 1 file(s) under hooks package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| reconciler package | library | Observed | Groups 1 file(s) under reconciler package (observed from repository paths and static analysis). |
| renderer package | library | Observed | Groups 1 file(s) under renderer package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 12 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/docs.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `website/package.json` (manifest)

## Top-level layout

- `src` — 87 analysed file(s)
- `website` — 80 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 3 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `87c844050c86e0eb548c3e6e8c57bd40d5174546` is the revision these paths and observations refer to.
