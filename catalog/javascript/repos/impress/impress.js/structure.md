# Project structure: impress/impress.js

**Analysed commit:** `b44b9694b41fd2c076c3d1ad7a0c3e0cea9eb262`

**Commit reference:** [b44b9694b41fd2c076c3d1ad7a0c3e0cea9eb262](https://github.com/impress/impress.js/commit/b44b9694b41fd2c076c3d1ad7a0c3e0cea9eb262)

**Tree at this commit:** [impress/impress.js@b44b9694b41f](https://github.com/impress/impress.js/tree/b44b9694b41fd2c076c3d1ad7a0c3e0cea9eb262)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | impress/impress.js |
| Description | It's a presentation framework based on the power of CSS3 transforms and transitions in modern browsers and inspired by the idea behind prezi.com. |
| Stars | 38155 |
| Forks | 6555 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b44b9694b41fd2c076c3d1ad7a0c3e0cea9eb262` |
| Retrieved at | 2026-11-14T19:10:41.194405+00:00 |
| Files in this snapshot | 108 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (1 files)
  workflows/  (1 files)
    pipeline.yaml
css/  (2 files)
  impress-common.css
  impress-demo.css
examples/  (21 files)
  2D-navigation/  (3 files)
    css/  (2 files)
      … 2 files under this directory
    index.html
  3D-positions/  (1 files)
    index.html
  3D-rotations/  (3 files)
    css/  (2 files)
      … 2 files under this directory
    index.html
  classic-slides/  (5 files)
    css/  (2 files)
      … 2 files under this directory
    images/  (2 files)
      … 2 files under this directory
    index.html
  cube/  (3 files)
    css/  (2 files)
      … 2 files under this directory
    index.html
  markdown/  (5 files)
    css/  (4 files)
      … 4 files under this directory
    index.html
  index.html
js/  (1 files)
  impress.js
src/  (51 files)
  lib/  (4 files)
    README.md
    gc.js
    rotation.js
    util.js
  plugins/  (46 files)
    autoplay/  (2 files)
      … 2 files under this directory
    blackout/  (2 files)
      … 2 files under this directory
    bookmark/  (2 files)
      … 2 files under this directory
    extras/  (2 files)
      … 2 files under this directory
    form/  (2 files)
      … 2 files under this directory
    fullscreen/  (2 files)
      … 2 files under this directory
    goto/  (2 files)
      … 2 files under this directory
    help/  (2 files)
      … 2 files under this directory
    impressConsole/  (2 files)
      … 2 files under this directory
    media/  (2 files)
      … 2 files under this directory
    mobile/  (2 files)
      … 2 files under this directory
    mouse-timeout/  (2 files)
      … 2 files under this directory
    navigation/  (3 files)
      … 3 files under this directory
    navigation-ui/  (2 files)
      … 2 files under this directory
    progress/  (2 files)
      … 2 files under this directory
    rel/  (2 files)
      … 2 files under this directory
    resize/  (2 files)
      … 2 files under this directory
    skip/  (2 files)
      … 2 files under this directory
    stop/  (2 files)
      … 2 files under this directory
    substep/  (2 files)
      … 2 files under this directory
    toolbar/  (2 files)
      … 2 files under this directory
    touch/  (2 files)
      … 2 files under this directory
    README.md
  impress.js
test/  (14 files)
  plugins/  (8 files)
    rel/  (8 files)
      … 8 files under this directory
  HOWTO.md
  core_tests.js
  core_tests_presentation.html
  helpers.js
  non_default.html
  non_default.js
.eslintrc.js
.gitattributes
.gitignore
.gitmodules
.jscsrc
.jshintrc
.npmignore
DOCUMENTATION.md
GettingStarted.md
LICENSE
README.md
build.js
index.html
karma.conf.js
npm-readme.md
package.json
qunit_test_runner.html
```

## Entry points

- [js/impress.js](https://github.com/impress/impress.js/blob/b44b9694b41fd2c076c3d1ad7a0c3e0cea9eb262/js/impress.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| impress.js package | library | Observed | Groups 1 file(s) under impress.js package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 1 file(s) under js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 3 file(s) under lib package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 23 file(s) under plugins package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.github/workflows/pipeline.yaml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 51 analysed file(s)
- `examples` — 21 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `test` — 14 analysed file(s)
- `css` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `.github` — 1 analysed file(s)
- `js` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b44b9694b41fd2c076c3d1ad7a0c3e0cea9eb262` is the revision these paths and observations refer to.
