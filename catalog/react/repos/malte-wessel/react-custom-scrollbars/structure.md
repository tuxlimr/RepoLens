# Project structure: malte-wessel/react-custom-scrollbars

**Analysed commit:** `b353cc4956d6154d6a100f34c3a6202c75434186`

**Commit reference:** [b353cc4956d6154d6a100f34c3a6202c75434186](https://github.com/malte-wessel/react-custom-scrollbars/commit/b353cc4956d6154d6a100f34c3a6202c75434186)

**Tree at this commit:** [malte-wessel/react-custom-scrollbars@b353cc4956d6](https://github.com/malte-wessel/react-custom-scrollbars/tree/b353cc4956d6154d6a100f34c3a6202c75434186)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | malte-wessel/react-custom-scrollbars |
| Description | React scrollbars component |
| Stars | 3212 |
| Forks | 556 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b353cc4956d6154d6a100f34c3a6202c75434186` |
| Retrieved at | 2026-11-14T19:15:27.956913+00:00 |
| Files in this snapshot | 64 |

## Directory tree

```text
docs/  (6 files)
  API.md
  README.md
  customization.md
  upgrade-guide-v2-v3.md
  usage.md
  v2-documentation.md
examples/  (16 files)
  simple/  (16 files)
    components/  (7 files)
      … 7 files under this directory
    sass/  (4 files)
      … 4 files under this directory
    index.html
    index.js
    package.json
    server.js
    webpack.config.js
src/  (9 files)
  Scrollbars/  (3 files)
    defaultRenderElements.js
    index.js
    styles.js
  utils/  (5 files)
    getInnerHeight.js
    getInnerWidth.js
    getScrollbarWidth.js
    isString.js
    returnFalse.js
  index.js
test/  (17 files)
  Scrollbars/  (13 files)
    autoHeight.js
    autoHide.js
    clickTrack.js
    dragThumb.js
    flexbox.js
    gettersSetters.js
    hideTracks.js
    index.js
    onUpdate.js
    rendering.js
    resizing.js
    scrolling.js
    universal.js
  .eslintrc
  browser.spec.js
  mobile.spec.js
  utils.spec.js
.babelrc
.eslintignore
.eslintrc
.gitignore
.npmignore
.nvmrc
.travis.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE.md
README.md
karma.conf.js
package.json
prepublish.js
test.js
webpack.config.js
```

## Entry points

- [examples/simple/server.js](https://github.com/malte-wessel/react-custom-scrollbars/blob/b353cc4956d6154d6a100f34c3a6202c75434186/examples/simple/server.js)
- [src/Scrollbars/index.js](https://github.com/malte-wessel/react-custom-scrollbars/blob/b353cc4956d6154d6a100f34c3a6202c75434186/src/Scrollbars/index.js)
- [src/index.js](https://github.com/malte-wessel/react-custom-scrollbars/blob/b353cc4956d6154d6a100f34c3a6202c75434186/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Scrollbars package | library | Observed | Groups 3 file(s) under scrollbars package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `examples/simple/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `test` — 17 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `examples` — 16 analysed file(s)
- `src` — 9 analysed file(s)
- `docs` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b353cc4956d6154d6a100f34c3a6202c75434186` is the revision these paths and observations refer to.
