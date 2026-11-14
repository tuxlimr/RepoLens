# Project structure: cmiscm/leonsans

**Analysed commit:** `f8c03c92d80552f9210a9c5a54a1b1ee81252129`

**Commit reference:** [f8c03c92d80552f9210a9c5a54a1b1ee81252129](https://github.com/cmiscm/leonsans/commit/f8c03c92d80552f9210a9c5a54a1b1ee81252129)

**Tree at this commit:** [cmiscm/leonsans@f8c03c92d805](https://github.com/cmiscm/leonsans/tree/f8c03c92d80552f9210a9c5a54a1b1ee81252129)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cmiscm/leonsans |
| Description | Leon Sans is a geometric sans-serif typeface made with code in 2019 by Jongmin Kim. |
| Stars | 10172 |
| Forks | 517 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f8c03c92d80552f9210a9c5a54a1b1ee81252129` |
| Retrieved at | 2026-11-14T19:12:43.888937+00:00 |
| Files in this snapshot | 47 |

## Directory tree

```text
examples/  (15 files)
  js/  (1 files)
    util.js
  all.html
  canvas-basic.html
  color-pattern.html
  colorful.html
  gradient.html
  grid.html
  index.html
  mask-tiling-pixi.html
  metaball-pixi.html
  morphing-pixi.html
  pattern.html
  plants-pixi.html
  wave.html
  webgl-basic-pixi.html
src/  (29 files)
  core/  (10 files)
    align.js
    dispatcher.js
    group.js
    guide.js
    length.js
    model.js
    paths.js
    point.js
    util.js
    vector.js
  draw/  (9 files)
    canvas/  (7 files)
      … 7 files under this directory
    pixi/  (2 files)
      … 2 files under this directory
  font/  (8 files)
    index.js
    latin.js
    latinutil.js
    lower.js
    number.js
    special.js
    upper.js
    util.js
  index.js
  leonsans.js
.gitignore
LICENSE
README.md
```

## Entry points

- [src/font/index.js](https://github.com/cmiscm/leonsans/blob/f8c03c92d80552f9210a9c5a54a1b1ee81252129/src/font/index.js)
- [src/index.js](https://github.com/cmiscm/leonsans/blob/f8c03c92d80552f9210a9c5a54a1b1ee81252129/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| draw package | library | Observed | Groups 9 file(s) under draw package (observed from repository paths and static analysis). |
| font package | library | Observed | Groups 8 file(s) under font package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| leonsans.js package | library | Observed | Groups 1 file(s) under leonsans.js package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 10 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

No manifest, config, CI, or container files were observed in the analysed set.

## Top-level layout

- `src` — 29 analysed file(s)
- `examples` — 15 analysed file(s)
- `(root files)` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f8c03c92d80552f9210a9c5a54a1b1ee81252129` is the revision these paths and observations refer to.
