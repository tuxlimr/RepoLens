# Project structure: chvin/react-tetris

**Analysed commit:** `89435b72f127b67f95870c515a130cbff38fd7cf`

**Commit reference:** [89435b72f127b67f95870c515a130cbff38fd7cf](https://github.com/chvin/react-tetris/commit/89435b72f127b67f95870c515a130cbff38fd7cf)

**Tree at this commit:** [chvin/react-tetris@89435b72f127](https://github.com/chvin/react-tetris/tree/89435b72f127b67f95870c515a130cbff38fd7cf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chvin/react-tetris |
| Description | Use React, Redux, Immutable to code Tetris. 🎮 |
| Stars | 8734 |
| Forks | 2288 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `89435b72f127b67f95870c515a130cbff38fd7cf` |
| Retrieved at | 2026-11-14T19:13:39.836728+00:00 |
| Files in this snapshot | 86 |

## Directory tree

```text
docs/  (3 files)
  css-1.0.1.css
  index.html
  loader.css
server/  (2 files)
  index.html
  index.tmpl.html
src/  (71 files)
  actions/  (2 files)
    index.js
    keyboard.js
  components/  (21 files)
    decorate/  (2 files)
      … 2 files under this directory
    guide/  (2 files)
      … 2 files under this directory
    keyboard/  (4 files)
      … 4 files under this directory
    logo/  (2 files)
      … 2 files under this directory
    matrix/  (2 files)
      … 2 files under this directory
    music/  (2 files)
      … 2 files under this directory
    next/  (2 files)
      … 2 files under this directory
    number/  (2 files)
      … 2 files under this directory
    pause/  (2 files)
      … 2 files under this directory
    point/  (1 files)
      … 1 files under this directory
  containers/  (3 files)
    index.js
    index.less
    loader.less
  control/  (11 files)
    todo/  (9 files)
      … 9 files under this directory
    index.js
    states.js
  reducers/  (25 files)
    clearLines/  (1 files)
      … 1 files under this directory
    cur/  (1 files)
      … 1 files under this directory
    drop/  (1 files)
      … 1 files under this directory
    focus/  (1 files)
      … 1 files under this directory
    keyboard/  (9 files)
      … 9 files under this directory
    lock/  (1 files)
      … 1 files under this directory
    matrix/  (1 files)
      … 1 files under this directory
    max/  (1 files)
      … 1 files under this directory
    music/  (1 files)
      … 1 files under this directory
    next/  (1 files)
      … 1 files under this directory
    pause/  (1 files)
      … 1 files under this directory
    points/  (1 files)
      … 1 files under this directory
    reset/  (1 files)
      … 1 files under this directory
    speedRun/  (1 files)
      … 1 files under this directory
    speedStart/  (1 files)
      … 1 files under this directory
    startLines/  (1 files)
      … 1 files under this directory
    index.js
  resource/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  store/  (1 files)
    index.js
  unit/  (6 files)
    block.js
    const.js
    event.js
    index.js
    music.js
    reducerType.js
  index.js
.babelrc
.eslintrc.js
.gitignore
README-EN.md
README.md
i18n.json
package.json
w.config.js
webpack.config.js
webpack.production.config.js
```

## Entry points

- [src/actions/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/actions/index.js)
- [src/components/decorate/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/components/decorate/index.js)
- [src/components/guide/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/components/guide/index.js)
- [src/components/keyboard/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/components/keyboard/index.js)
- [src/components/logo/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/components/logo/index.js)
- [src/components/matrix/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/components/matrix/index.js)
- [src/components/music/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/components/music/index.js)
- [src/components/next/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/components/next/index.js)
- [src/components/number/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/components/number/index.js)
- [src/components/pause/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/components/pause/index.js)
- [src/components/point/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/components/point/index.js)
- [src/containers/index.js](https://github.com/chvin/react-tetris/blob/89435b72f127b67f95870c515a130cbff38fd7cf/src/containers/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| actions package | library | Observed | Groups 2 file(s) under actions package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 11 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| containers package | library | Observed | Groups 1 file(s) under containers package (observed from repository paths and static analysis). |
| control package | library | Observed | Groups 11 file(s) under control package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| reducers package | library | Observed | Groups 25 file(s) under reducers package (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 1 file(s) under store package (observed from repository paths and static analysis). |
| unit package | library | Observed | Groups 6 file(s) under unit package (observed from repository paths and static analysis). |

## Important files

- `i18n.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 71 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `docs` — 3 analysed file(s)
- `server` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `89435b72f127b67f95870c515a130cbff38fd7cf` is the revision these paths and observations refer to.
