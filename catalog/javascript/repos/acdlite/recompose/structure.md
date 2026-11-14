# Project structure: acdlite/recompose

**Analysed commit:** `3db12ce7121a050b533476958ff3d66ded1c4bb8`

**Commit reference:** [3db12ce7121a050b533476958ff3d66ded1c4bb8](https://github.com/acdlite/recompose/commit/3db12ce7121a050b533476958ff3d66ded1c4bb8)

**Tree at this commit:** [acdlite/recompose@3db12ce7121a](https://github.com/acdlite/recompose/tree/3db12ce7121a050b533476958ff3d66ded1c4bb8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | acdlite/recompose |
| Description | A React utility belt for function components and higher-order components. |
| Stars | 14751 |
| Forks | 1208 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `3db12ce7121a050b533476958ff3d66ded1c4bb8` |
| Retrieved at | 2026-11-14T19:11:43.213130+00:00 |
| Files in this snapshot | 170 |

## Directory tree

```text
docs/  (3 files)
  API.md
  flow.md
  performance.md
scripts/  (5 files)
  getPackageNames.js
  installNestedPackageDeps.js
  jest.setup.js
  release.js
  rollup.config.js
src/  (131 files)
  packages/  (130 files)
    recompose/  (124 files)
      … 124 files under this directory
    recompose-relay/  (6 files)
      … 6 files under this directory
  basePackage.json
types/  (15 files)
  flow-example/  (14 files)
    flow-typed/  (2 files)
      … 2 files under this directory
    public/  (2 files)
      … 2 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .eslintrc
    .flowconfig
    .gitignore
    README.md
    package.json
  README.md
.codeclimate.yml
.editorconfig
.eslintignore
.eslintrc
.flowconfig
.gitignore
.npmignore
.prettierignore
.prettierrc
.size-snapshot.json
.travis.yml
CHANGELOG.md
LICENSE.md
README.md
babel.config.js
package.json
```

## Entry points

- [src/packages/recompose-relay/index.js](https://github.com/acdlite/recompose/blob/3db12ce7121a050b533476958ff3d66ded1c4bb8/src/packages/recompose-relay/index.js)
- [src/packages/recompose/index.js](https://github.com/acdlite/recompose/blob/3db12ce7121a050b533476958ff3d66ded1c4bb8/src/packages/recompose/index.js)
- [types/flow-example/src/App.js](https://github.com/acdlite/recompose/blob/3db12ce7121a050b533476958ff3d66ded1c4bb8/types/flow-example/src/App.js)
- [types/flow-example/src/index.js](https://github.com/acdlite/recompose/blob/3db12ce7121a050b533476958ff3d66ded1c4bb8/types/flow-example/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 97 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 24 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 7 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.editorconfig` (config)
- `.size-snapshot.json` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)
- `src/basePackage.json` (config)
- `src/packages/recompose-relay/package.json` (manifest)
- `src/packages/recompose/package.json` (manifest)
- `types/flow-example/package.json` (manifest)
- `types/flow-example/public/manifest.json` (config)

## Top-level layout

- `src` — 131 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `types` — 15 analysed file(s)
- `scripts` — 5 analysed file(s)
- `docs` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `3db12ce7121a050b533476958ff3d66ded1c4bb8` is the revision these paths and observations refer to.
