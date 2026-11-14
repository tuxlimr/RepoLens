# Project structure: margox/braft-editor

**Analysed commit:** `099025513256bf74ca48d98698a5f837130f6262`

**Commit reference:** [099025513256bf74ca48d98698a5f837130f6262](https://github.com/margox/braft-editor/commit/099025513256bf74ca48d98698a5f837130f6262)

**Tree at this commit:** [margox/braft-editor@099025513256](https://github.com/margox/braft-editor/tree/099025513256bf74ca48d98698a5f837130f6262)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | margox/braft-editor |
| Description | 美观易用的React富文本编辑器，基于draft-js开发 |
| Stars | 4573 |
| Forks | 577 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `099025513256bf74ca48d98698a5f837130f6262` |
| Retrieved at | 2026-11-14T19:14:42.366808+00:00 |
| Files in this snapshot | 108 |

## Directory tree

```text
.vscode/  (1 files)
  settings.json
playground/  (11 files)
  webpack/  (4 files)
    scss-output.js
    webpack.base.js
    webpack.config.dev.js
    webpack.config.prod.js
  argv.js
  devMiddlewares.js
  index.html
  index.jsx
  logger.js
  port.js
  server.js
src/  (80 files)
  assets/  (7 files)
    icons/  (1 files)
      … 1 files under this directory
    scss/  (6 files)
      … 6 files under this directory
  components/  (31 files)
    business/  (23 files)
      … 23 files under this directory
    common/  (8 files)
      … 8 files under this directory
  configs/  (5 files)
    controls.js
    handlers.js
    keybindings.js
    maps.js
    props.js
  editor/  (1 files)
    index.jsx
  helpers/  (2 files)
    extension.js
    responsive.js
  languages/  (15 files)
    en.js
    fa.js
    fr.js
    index.js
    is.js
    jpn.js
    kr.js
    nl.js
    pl.js
    pt-br.js
    ru.js
    tr.js
    vi-vn.js
    zh-hant.js
    zh.js
  renderers/  (18 files)
    atomics/  (10 files)
      … 10 files under this directory
    block/  (3 files)
      … 3 files under this directory
    decorators/  (2 files)
      … 2 files under this directory
    inline/  (2 files)
      … 2 files under this directory
    index.js
  index.jsx
.babelrc
.editorconfig
.eslintignore
.eslintrc.js
.gitattributes
.gitignore
.npmignore
.prettierignore
.prettierrc
CHANGELOG.md
LICENSE
README.md
index.d.ts
jsconfig.json
package.json
tea.yaml
```

## Entry points

- [playground/index.jsx](https://github.com/margox/braft-editor/blob/099025513256bf74ca48d98698a5f837130f6262/playground/index.jsx)
- [playground/server.js](https://github.com/margox/braft-editor/blob/099025513256bf74ca48d98698a5f837130f6262/playground/server.js)
- [src/editor/index.jsx](https://github.com/margox/braft-editor/blob/099025513256bf74ca48d98698a5f837130f6262/src/editor/index.jsx)
- [src/index.jsx](https://github.com/margox/braft-editor/blob/099025513256bf74ca48d98698a5f837130f6262/src/index.jsx)
- [src/languages/index.js](https://github.com/margox/braft-editor/blob/099025513256bf74ca48d98698a5f837130f6262/src/languages/index.js)
- [src/renderers/decorators/index.js](https://github.com/margox/braft-editor/blob/099025513256bf74ca48d98698a5f837130f6262/src/renderers/decorators/index.js)
- [src/renderers/index.js](https://github.com/margox/braft-editor/blob/099025513256bf74ca48d98698a5f837130f6262/src/renderers/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 4 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| editor package | library | Observed | Groups 1 file(s) under editor package (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 2 file(s) under helpers package (observed from repository paths and static analysis). |
| index.jsx package | library | Observed | Groups 1 file(s) under index.jsx package (observed from repository paths and static analysis). |
| languages package | library | Observed | Groups 15 file(s) under languages package (observed from repository paths and static analysis). |
| playground package | library | Observed | Groups 10 file(s) under playground package (observed from repository paths and static analysis). |
| renderers package | library | Observed | Groups 13 file(s) under renderers package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 13 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.vscode/settings.json` (config)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `src/assets/icons/icons.json` (config)
- `tea.yaml` (config)

## Top-level layout

- `src` — 80 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `playground` — 11 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `099025513256bf74ca48d98698a5f837130f6262` is the revision these paths and observations refer to.
