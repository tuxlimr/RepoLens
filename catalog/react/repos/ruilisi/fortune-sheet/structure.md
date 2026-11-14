# Project structure: ruilisi/fortune-sheet

**Analysed commit:** `94346608877db4747406707a177c4b8f3bacdbf9`

**Commit reference:** [94346608877db4747406707a177c4b8f3bacdbf9](https://github.com/ruilisi/fortune-sheet/commit/94346608877db4747406707a177c4b8f3bacdbf9)

**Tree at this commit:** [ruilisi/fortune-sheet@94346608877d](https://github.com/ruilisi/fortune-sheet/tree/94346608877db4747406707a177c4b8f3bacdbf9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ruilisi/fortune-sheet |
| Description | A drop-in javascript spreadsheet library that provides rich features like Excel and Google Sheets |
| Stars | 3751 |
| Forks | 324 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `94346608877db4747406707a177c4b8f3bacdbf9` |
| Retrieved at | 2026-11-14T19:15:05.378962+00:00 |
| Files in this snapshot | 325 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    ci.yml
    deprecate.yml
    release.yml
  FUNDING.yml
  dependabot.yml
.storybook/  (4 files)
  main.js
  preview-head.html
  preview.js
  webpack.config.js
backend-demo/  (2 files)
  index.js
  op.js
docs/  (20 files)
  .vuepress/  (1 files)
    config.js
  guide/  (8 files)
    FAQ.md
    README.md
    api.md
    cell.md
    config.md
    contribute.md
    op.md
    sheet.md
  zh/  (9 files)
    guide/  (8 files)
      … 8 files under this directory
    README.md
  README.md
  package.json
packages/  (263 files)
  core/  (89 files)
    src/  (60 files)
      … 60 files under this directory
    test/  (27 files)
      … 27 files under this directory
    README.md
    package.json
  formula-parser/  (84 files)
    .config/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (23 files)
      … 23 files under this directory
    test/  (40 files)
      … 40 files under this directory
    .babelrc
    .codeclimate.yml
    .editorconfig
    .eslintignore
    .eslintrc
    .fatherrc.js
    .gitattributes
    .gitignore
    .npmignore
    .nvmrc
    .release.json
    .travis.yml
    CHANGELOG.md
    CONTRIBUTING.md
    LICENSE
    README.md
    bower.json
    package.json
    webpack.config.js
  react/  (90 files)
    src/  (86 files)
      … 86 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .fatherrc.js
    README.md
    package.json
scripts/  (1 files)
  build.js
stories/  (10 files)
  data/  (6 files)
    cell.ts
    dataVerification.ts
    empty.ts
    formula.ts
    freeze.ts
    protected.ts
  API.stories.tsx
  Collabration.stories.tsx
  Features.stories.tsx
  utils.ts
tests/  (2 files)
  setup.js
  transformer.js
.drone.yml
.eslintignore
.eslintrc.js
.fatherrc.js
.gitignore
.prettierignore
CHANGELOG.md
LICENSE
README-zh.md
README.md
babel.config.json
jest.config.js
lerna.json
lint-staged.config.js
package.json
tsconfig.json
```

## Entry points

- [.storybook/main.js](https://github.com/ruilisi/fortune-sheet/blob/94346608877db4747406707a177c4b8f3bacdbf9/.storybook/main.js)
- [backend-demo/index.js](https://github.com/ruilisi/fortune-sheet/blob/94346608877db4747406707a177c4b8f3bacdbf9/backend-demo/index.js)
- [packages/core/src/index.ts](https://github.com/ruilisi/fortune-sheet/blob/94346608877db4747406707a177c4b8f3bacdbf9/packages/core/src/index.ts)
- [packages/formula-parser/src/index.js](https://github.com/ruilisi/fortune-sheet/blob/94346608877db4747406707a177c4b8f3bacdbf9/packages/formula-parser/src/index.js)
- [packages/react/src/index.ts](https://github.com/ruilisi/fortune-sheet/blob/94346608877db4747406707a177c4b8f3bacdbf9/packages/react/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). |
| backend-demo package | library | Observed | Groups 2 file(s) under backend-demo package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 6 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 90 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 51 file(s) under service / domain layer (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 4 file(s) under stories package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 70 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.drone.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deprecate.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `babel.config.json` (config)
- `docs/package.json` (manifest)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/formula-parser/.codeclimate.yml` (config)
- `packages/formula-parser/.editorconfig` (config)
- `packages/formula-parser/.release.json` (config)
- `packages/formula-parser/.travis.yml` (ci)
- `packages/formula-parser/bower.json` (config)
- `packages/formula-parser/package.json` (manifest)
- `packages/react/package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 263 analysed file(s)
- `docs` — 20 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `stories` — 10 analysed file(s)
- `.github` — 7 analysed file(s)
- `.storybook` — 4 analysed file(s)
- `backend-demo` — 2 analysed file(s)
- `tests` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `94346608877db4747406707a177c4b8f3bacdbf9` is the revision these paths and observations refer to.
