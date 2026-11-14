# Project structure: rcbyr/keen-slider

**Analysed commit:** `520c757a80aa10ff224e9c89b0917edfa811adcf`

**Commit reference:** [520c757a80aa10ff224e9c89b0917edfa811adcf](https://github.com/rcbyr/keen-slider/commit/520c757a80aa10ff224e9c89b0917edfa811adcf)

**Tree at this commit:** [rcbyr/keen-slider@520c757a80aa](https://github.com/rcbyr/keen-slider/tree/520c757a80aa10ff224e9c89b0917edfa811adcf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | rcbyr/keen-slider |
| Description | The HTML touch slider carousel with the most native feeling you will get. |
| Stars | 5017 |
| Forks | 218 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `520c757a80aa10ff224e9c89b0917edfa811adcf` |
| Retrieved at | 2026-11-14T19:14:29.635980+00:00 |
| Files in this snapshot | 42 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    main.yml
  FUNDING.yml
docs/  (2 files)
  react-native.md
  web.md
src/  (20 files)
  core/  (5 files)
    animator.ts
    slider.ts
    track.ts
    types.ts
    utils.ts
  plugins/  (10 files)
    native/  (4 files)
      … 4 files under this directory
    web/  (4 files)
      … 4 files under this directory
    modes.ts
    types.ts
  keen-slider.scss
  keen-slider.ts
  react-native.ts
  react.ts
  vue.ts
.eslintignore
.eslintrc
.gitignore
.npmignore
.nvmrc
.prettierrc
LICENSE
README.md
api-extractor.json
api-extractor.react-native.json
api-extractor.react.json
api-extractor.vue.json
babel.config.js
jest.config.js
jest.setup.ts
package.json
rollup.config.js
tsconfig.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| keen-slider.ts package | library | Observed | Groups 1 file(s) under keen-slider.ts package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 10 file(s) under plugins package (observed from repository paths and static analysis). |
| react-native.ts package | library | Observed | Groups 1 file(s) under react-native.ts package (observed from repository paths and static analysis). |
| react.ts package | library | Observed | Groups 1 file(s) under react.ts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| vue.ts package | library | Observed | Groups 1 file(s) under vue.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/main.yml` (ci)
- `api-extractor.json` (config)
- `api-extractor.react-native.json` (config)
- `api-extractor.react.json` (config)
- `api-extractor.vue.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 20 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 2 analysed file(s)
- `docs` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `520c757a80aa10ff224e9c89b0917edfa811adcf` is the revision these paths and observations refer to.
