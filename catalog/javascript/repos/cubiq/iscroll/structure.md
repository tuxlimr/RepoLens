# Project structure: cubiq/iscroll

**Analysed commit:** `60ed6f8029b2e097a87399a2b3c688afd596980f`

**Commit reference:** [60ed6f8029b2e097a87399a2b3c688afd596980f](https://github.com/cubiq/iscroll/commit/60ed6f8029b2e097a87399a2b3c688afd596980f)

**Tree at this commit:** [cubiq/iscroll@60ed6f8029b2](https://github.com/cubiq/iscroll/tree/60ed6f8029b2e097a87399a2b3c688afd596980f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cubiq/iscroll |
| Description | Smooth scrolling for the web |
| Stars | 12779 |
| Forks | 3702 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `60ed6f8029b2e097a87399a2b3c688afd596980f` |
| Retrieved at | 2026-11-14T19:12:03.399860+00:00 |
| Files in this snapshot | 64 |

## Directory tree

```text
demos/  (23 files)
  2d-scroll/  (1 files)
    index.html
  barebone/  (1 files)
    index.html
  bounce-easing/  (1 files)
    index.html
  carousel/  (1 files)
    index.html
  click/  (1 files)
    index.html
  event-passthrough/  (1 files)
    index.html
  forms/  (1 files)
    index.html
  horizontal/  (1 files)
    index.html
  infinite/  (2 files)
    dataset.php
    index.html
  key-bindings/  (1 files)
    index.html
  minimap/  (1 files)
    index.html
  no-transition/  (1 files)
    index.html
  parallax/  (1 files)
    index.html
  probe/  (1 files)
    index.html
  scroll-to-element/  (1 files)
    index.html
  scrollbars/  (1 files)
    index.html
  simple/  (1 files)
    index.html
  snap/  (1 files)
    index.html
  styled-scrollbars/  (1 files)
    index.html
  tap/  (1 files)
    index.html
  zoom/  (1 files)
    index.html
  demoUtils.js
src/  (32 files)
  default/  (2 files)
    _animate.js
    handleEvent.js
  indicator/  (6 files)
    _initIndicators.js
    _transitionTime.js
    _transitionTimingFunction.js
    _translate.js
    build.json
    indicator.js
  infinite/  (3 files)
    build.json
    infinite.js
    refresh.js
  keys/  (2 files)
    build.json
    keys.js
  probe/  (5 files)
    _animate.js
    _move.js
    build.json
    indicator._move.js
    probe.js
  snap/  (4 files)
    _end.js
    build.json
    refresh.js
    snap.js
  wheel/  (2 files)
    build.json
    wheel.js
  zoom/  (4 files)
    build.json
    handleEvent.js
    refresh.js
    zoom.js
  close.js
  core.js
  open.js
  utils.js
.gitignore
.nodemonignore
CONTRIBUTING.md
LICENSE
README.md
RELEASENOTES.md
bower.json
build.js
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| close.js package | library | Observed | Groups 1 file(s) under close.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| core.js package | library | Observed | Groups 1 file(s) under core.js package (observed from repository paths and static analysis). |
| default package | library | Observed | Groups 2 file(s) under default package (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 2 file(s) under demos package (observed from repository paths and static analysis). |
| indicator package | library | Observed | Groups 5 file(s) under indicator package (observed from repository paths and static analysis). |
| infinite package | library | Observed | Groups 2 file(s) under infinite package (observed from repository paths and static analysis). |
| keys package | library | Observed | Groups 1 file(s) under keys package (observed from repository paths and static analysis). |
| open.js package | library | Observed | Groups 1 file(s) under open.js package (observed from repository paths and static analysis). |
| probe package | library | Observed | Groups 4 file(s) under probe package (observed from repository paths and static analysis). |
| snap package | library | Observed | Groups 3 file(s) under snap package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| wheel package | library | Observed | Groups 1 file(s) under wheel package (observed from repository paths and static analysis). |
| zoom package | library | Observed | Groups 3 file(s) under zoom package (observed from repository paths and static analysis). |

## Important files

- `bower.json` (config)
- `package.json` (manifest)
- `src/indicator/build.json` (config)
- `src/infinite/build.json` (config)
- `src/keys/build.json` (config)
- `src/probe/build.json` (config)
- `src/snap/build.json` (config)
- `src/wheel/build.json` (config)
- `src/zoom/build.json` (config)

## Top-level layout

- `src` — 32 analysed file(s)
- `demos` — 23 analysed file(s)
- `(root files)` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (5 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `60ed6f8029b2e097a87399a2b3c688afd596980f` is the revision these paths and observations refer to.
