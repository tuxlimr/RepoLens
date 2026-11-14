# Project structure: bilibili/flv.js

**Analysed commit:** `42343088f22619cf014a057b3878fe3d320016a6`

**Commit reference:** [42343088f22619cf014a057b3878fe3d320016a6](https://github.com/bilibili/flv.js/commit/42343088f22619cf014a057b3878fe3d320016a6)

**Tree at this commit:** [bilibili/flv.js@42343088f226](https://github.com/bilibili/flv.js/tree/42343088f22619cf014a057b3878fe3d320016a6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bilibili/flv.js |
| Description | HTML5 FLV Player |
| Stars | 23169 |
| Forks | 3323 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `42343088f22619cf014a057b3878fe3d320016a6` |
| Retrieved at | 2026-11-14T19:11:05.457754+00:00 |
| Files in this snapshot | 61 |

## Directory tree

```text
d.ts/  (1 files)
  flv.d.ts
demo/  (2 files)
  demo.css
  index.html
docs/  (5 files)
  api.md
  cors.md
  design.md
  livestream.md
  multipart.md
src/  (40 files)
  core/  (9 files)
    features.js
    media-info.js
    media-segment-info.js
    mse-controller.js
    mse-events.js
    transmuxer.js
    transmuxing-controller.js
    transmuxing-events.js
    transmuxing-worker.js
  demux/  (5 files)
    amf-parser.js
    demux-errors.js
    exp-golomb.js
    flv-demuxer.js
    sps-parser.js
  io/  (10 files)
    fetch-stream-loader.js
    io-controller.js
    loader.js
    param-seek-handler.js
    range-seek-handler.js
    speed-sampler.js
    websocket-loader.js
    xhr-moz-chunked-loader.js
    xhr-msstream-loader.js
    xhr-range-loader.js
  player/  (4 files)
    flv-player.js
    native-player.js
    player-errors.js
    player-events.js
  remux/  (3 files)
    aac-silent.js
    mp4-generator.js
    mp4-remuxer.js
  utils/  (6 files)
    browser.js
    exception.js
    logger.js
    logging-control.js
    polyfill.js
    utf8-conv.js
  config.js
  flv.js
  index.js
types/  (3 files)
  index.d.ts
  test-flv.ts
  tsconfig.json
.eslintignore
.eslintrc.json
.gitignore
.npmignore
LICENSE
README.md
package.json
tsconfig.json
tslint.json
webpack.config.js
```

## Entry points

- [src/index.js](https://github.com/bilibili/flv.js/blob/42343088f22619cf014a057b3878fe3d320016a6/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| d.ts package | library | Observed | Groups 1 file(s) under d.ts package (observed from repository paths and static analysis). |
| demux package | library | Observed | Groups 5 file(s) under demux package (observed from repository paths and static analysis). |
| flv.js package | library | Observed | Groups 1 file(s) under flv.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| io package | library | Observed | Groups 10 file(s) under io package (observed from repository paths and static analysis). |
| player package | library | Observed | Groups 4 file(s) under player package (observed from repository paths and static analysis). |
| remux package | library | Observed | Groups 3 file(s) under remux package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 9 file(s) under service / domain layer (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 2 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 6 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tslint.json` (config)
- `types/tsconfig.json` (config)

## Top-level layout

- `src` — 40 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `docs` — 5 analysed file(s)
- `types` — 3 analysed file(s)
- `demo` — 2 analysed file(s)
- `d.ts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `42343088f22619cf014a057b3878fe3d320016a6` is the revision these paths and observations refer to.
