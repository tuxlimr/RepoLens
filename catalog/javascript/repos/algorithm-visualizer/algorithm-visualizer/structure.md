# Project structure: algorithm-visualizer/algorithm-visualizer

**Analysed commit:** `18de2edf6b629e843ee4bcedfa2208d22b253f0f`

**Commit reference:** [18de2edf6b629e843ee4bcedfa2208d22b253f0f](https://github.com/algorithm-visualizer/algorithm-visualizer/commit/18de2edf6b629e843ee4bcedfa2208d22b253f0f)

**Tree at this commit:** [algorithm-visualizer/algorithm-visualizer@18de2edf6b62](https://github.com/algorithm-visualizer/algorithm-visualizer/tree/18de2edf6b629e843ee4bcedfa2208d22b253f0f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | algorithm-visualizer/algorithm-visualizer |
| Description | :fireworks:Interactive Online Platform that Visualizes Algorithms from Code |
| Stars | 49507 |
| Forks | 7663 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `18de2edf6b629e843ee4bcedfa2208d22b253f0f` |
| Retrieved at | 2026-11-14T19:10:37.515565+00:00 |
| Files in this snapshot | 95 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
public/  (3 files)
  index.html
  manifest.json
  robots.txt
src/  (83 files)
  apis/  (1 files)
    index.js
  common/  (6 files)
    stylesheet/  (4 files)
      … 4 files under this directory
    config.js
    util.js
  components/  (33 files)
    App/  (2 files)
      … 2 files under this directory
    BaseComponent/  (1 files)
      … 1 files under this directory
    Button/  (2 files)
      … 2 files under this directory
    CodeEditor/  (2 files)
      … 2 files under this directory
    Divider/  (2 files)
      … 2 files under this directory
    Ellipsis/  (2 files)
      … 2 files under this directory
    ExpandableListItem/  (2 files)
      … 2 files under this directory
    FoldableAceEditor/  (1 files)
      … 1 files under this directory
    Header/  (2 files)
      … 2 files under this directory
    ListItem/  (2 files)
      … 2 files under this directory
    Navigator/  (2 files)
      … 2 files under this directory
    Player/  (2 files)
      … 2 files under this directory
    ProgressBar/  (2 files)
      … 2 files under this directory
    ResizableContainer/  (2 files)
      … 2 files under this directory
    TabContainer/  (2 files)
      … 2 files under this directory
    ToastContainer/  (2 files)
      … 2 files under this directory
    VisualizationViewer/  (2 files)
      … 2 files under this directory
    index.js
  core/  (30 files)
    layouts/  (4 files)
      … 4 files under this directory
    renderers/  (17 files)
      … 17 files under this directory
    tracers/  (9 files)
      … 9 files under this directory
  files/  (5 files)
    scratch-paper/  (1 files)
      … 1 files under this directory
    skeletons/  (3 files)
      … 3 files under this directory
    index.js
  reducers/  (6 files)
    current.js
    directory.js
    env.js
    index.js
    player.js
    toast.js
  index.js
  stylesheet.scss
.gitignore
.gitpod.yml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
jsconfig.json
package.json
```

## Entry points

- [src/apis/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/apis/index.js)
- [src/components/App/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/App/index.js)
- [src/components/BaseComponent/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/BaseComponent/index.js)
- [src/components/Button/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/Button/index.js)
- [src/components/CodeEditor/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/CodeEditor/index.js)
- [src/components/Divider/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/Divider/index.js)
- [src/components/Ellipsis/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/Ellipsis/index.js)
- [src/components/ExpandableListItem/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/ExpandableListItem/index.js)
- [src/components/FoldableAceEditor/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/FoldableAceEditor/index.js)
- [src/components/Header/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/Header/index.js)
- [src/components/ListItem/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/ListItem/index.js)
- [src/components/Navigator/index.js](https://github.com/algorithm-visualizer/algorithm-visualizer/blob/18de2edf6b629e843ee4bcedfa2208d22b253f0f/src/components/Navigator/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apis package | library | Observed | Groups 1 file(s) under apis package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 2 file(s) under common package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 18 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| files package | library | Observed | Groups 4 file(s) under files package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| reducers package | library | Observed | Groups 6 file(s) under reducers package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 22 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.gitpod.yml` (config)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `public/manifest.json` (config)

## Top-level layout

- `src` — 83 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `public` — 3 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `18de2edf6b629e843ee4bcedfa2208d22b253f0f` is the revision these paths and observations refer to.
