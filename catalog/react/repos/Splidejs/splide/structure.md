# Project structure: Splidejs/splide

**Analysed commit:** `d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6`

**Commit reference:** [d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6](https://github.com/Splidejs/splide/commit/d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6)

**Tree at this commit:** [Splidejs/splide@d7e1f08e6b4f](https://github.com/Splidejs/splide/tree/d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Splidejs/splide |
| Description | Splide is a lightweight, flexible and accessible slider/carousel written in TypeScript. No dependencies, no Lighthouse errors. |
| Stars | 5367 |
| Forks | 445 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6` |
| Retrieved at | 2026-11-14T19:14:21.531989+00:00 |
| Files in this snapshot | 327 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    BUG_REPORT.yml
    config.yml
  FUNDING.yml
  pull_request_template.md
images/  (6 files)
  javascript-logo.svg
  logo.svg
  react-logo.svg
  svelte-logo.svg
  typescript-logo.svg
  vue-logo.svg
scripts/  (9 files)
  constants/  (1 files)
    banner.js
  plugins/  (1 files)
    minify.js
  build-css.js
  build-module.js
  build-script.js
  build-types.js
  build-utils.js
  develop.js
  serve.js
src/  (299 files)
  css/  (37 files)
    core/  (18 files)
      … 18 files under this directory
    template/  (13 files)
      … 13 files under this directory
    themes/  (6 files)
      … 6 files under this directory
  js/  (262 files)
    components/  (74 files)
      … 74 files under this directory
    constants/  (12 files)
      … 12 files under this directory
    constructors/  (13 files)
      … 13 files under this directory
    core/  (2 files)
      … 2 files under this directory
    renderer/  (5 files)
      … 5 files under this directory
    test/  (35 files)
      … 35 files under this directory
    transitions/  (3 files)
      … 3 files under this directory
    types/  (6 files)
      … 6 files under this directory
    utils/  (111 files)
      … 111 files under this directory
    index.ts
.babelrc
.eslintrc
.gitignore
.stylelintrc
LICENSE
README.md
jest.config.js
package.json
tsconfig.json
```

## Entry points

- [src/js/components/index.ts](https://github.com/Splidejs/splide/blob/d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6/src/js/components/index.ts)
- [src/js/constructors/index.ts](https://github.com/Splidejs/splide/blob/d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6/src/js/constructors/index.ts)
- [src/js/index.ts](https://github.com/Splidejs/splide/blob/d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6/src/js/index.ts)
- [src/js/transitions/index.ts](https://github.com/Splidejs/splide/blob/d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6/src/js/transitions/index.ts)
- [src/js/types/index.ts](https://github.com/Splidejs/splide/blob/d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6/src/js/types/index.ts)
- [src/js/utils/index.ts](https://github.com/Splidejs/splide/blob/d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6/src/js/utils/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 171 file(s) under js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 9 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 90 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/BUG_REPORT.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 299 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `scripts` — 9 analysed file(s)
- `images` — 6 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 13 file(s) were skipped during inventory (13 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d7e1f08e6b4f4b02a7c6ccbfbeb2d569d85715e6` is the revision these paths and observations refer to.
