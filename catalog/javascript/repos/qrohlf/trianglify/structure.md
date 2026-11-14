# Project structure: qrohlf/trianglify

**Analysed commit:** `b959ccd656ca7294ebe363ee0c1dfbe72929a16e`

**Commit reference:** [b959ccd656ca7294ebe363ee0c1dfbe72929a16e](https://github.com/qrohlf/trianglify/commit/b959ccd656ca7294ebe363ee0c1dfbe72929a16e)

**Tree at this commit:** [qrohlf/trianglify@b959ccd656ca](https://github.com/qrohlf/trianglify/tree/b959ccd656ca7294ebe363ee0c1dfbe72929a16e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | qrohlf/trianglify |
| Description | Algorithmically generated triangle art |
| Stars | 10089 |
| Forks | 652 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b959ccd656ca7294ebe363ee0c1dfbe72929a16e` |
| Retrieved at | 2026-11-14T19:12:44.996441+00:00 |
| Files in this snapshot | 30 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    build.yml
examples/  (7 files)
  basic-web-example.html
  color-function-example.html
  custom-points-example.html
  destsvg-example.html
  save-as-png.js
  save-as-svg.js
  transparency-example.html
src/  (12 files)
  __snapshots__/  (2 files)
    trianglify.browser.test.js.snap
    trianglify.node.test.js.snap
  utils/  (6 files)
    colorFunctions.js
    colorbrewer.js
    debugRender.js
    geom.js
    getScalingRatio.js
    mulberry32.js
  pattern.js
  trianglify.browser.test.js
  trianglify.js
  trianglify.node.test.js
.babelrc
.browserslistrc
.gitignore
.nvmrc
CONTRIBUTING.md
LICENSE
Readme.md
changelog.txt
package.json
rollup.config.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| pattern.js package | library | Observed | Groups 1 file(s) under pattern.js package (observed from repository paths and static analysis). |
| trianglify.browser.test.js package | library | Observed | Groups 1 file(s) under trianglify.browser.test.js package (observed from repository paths and static analysis). |
| trianglify.js package | library | Observed | Groups 1 file(s) under trianglify.js package (observed from repository paths and static analysis). |
| trianglify.node.test.js package | library | Observed | Groups 1 file(s) under trianglify.node.test.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 6 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/build.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `examples` — 7 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b959ccd656ca7294ebe363ee0c1dfbe72929a16e` is the revision these paths and observations refer to.
