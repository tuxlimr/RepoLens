# Project structure: piotrwitek/react-redux-typescript-guide

**Analysed commit:** `43a22a97c407ab742f24368af4686582df6a60f0`

**Commit reference:** [43a22a97c407ab742f24368af4686582df6a60f0](https://github.com/piotrwitek/react-redux-typescript-guide/commit/43a22a97c407ab742f24368af4686582df6a60f0)

**Tree at this commit:** [piotrwitek/react-redux-typescript-guide@43a22a97c407](https://github.com/piotrwitek/react-redux-typescript-guide/tree/43a22a97c407ab742f24368af4686582df6a60f0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | piotrwitek/react-redux-typescript-guide |
| Description | The complete guide to static typing in "React & Redux" apps using TypeScript |
| Stars | 13254 |
| Forks | 1094 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `43a22a97c407ab742f24368af4686582df6a60f0` |
| Retrieved at | 2026-11-14T19:13:19.255708+00:00 |
| Files in this snapshot | 173 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    custom.md
    feature_request.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
.vscode/  (1 files)
  launch.json
configs/  (2 files)
  jest.config.json
  jest.stubs.js
docs/  (1 files)
  index.html
playground/  (151 files)
  .storybook/  (3 files)
    addons.js
    config.js
    webpack.config.js
  .vscode/  (1 files)
    settings.json
  public/  (2 files)
    index.html
    manifest.json
  src/  (120 files)
    api/  (6 files)
      … 6 files under this directory
    components/  (40 files)
      … 40 files under this directory
    connected/  (8 files)
      … 8 files under this directory
    context/  (4 files)
      … 4 files under this directory
    features/  (23 files)
      … 23 files under this directory
    hoc/  (7 files)
      … 7 files under this directory
    hooks/  (4 files)
      … 4 files under this directory
    layout/  (3 files)
      … 3 files under this directory
    models/  (3 files)
      … 3 files under this directory
    routes/  (2 files)
      … 2 files under this directory
    services/  (4 files)
      … 4 files under this directory
    store/  (9 files)
      … 9 files under this directory
    app.test.tsx
    app.tsx
    index.css
    index.tsx
    react-app-env.d.ts
    serviceWorker.ts
    storyshots.disabled-test.ts
  src-old/  (9 files)
    App.css
    App.test.tsx
    App.tsx
    index.css
    index.tsx
    logo.svg
    react-app-env.d.ts
    reportWebVitals.ts
    setupTests.ts
  styleguide/  (3 files)
    docs/  (1 files)
      … 1 files under this directory
    package.json
    styleguide.config.js
  typings/  (5 files)
    redux/  (1 files)
      … 1 files under this directory
    redux-thunk/  (1 files)
      … 1 files under this directory
    augmentations.d.ts
    globals.d.ts
    modules.d.ts
  .eslintrc.js
  .gitignore
  .prettierrc
  README.md
  index.html
  package.json
  tsconfig.json
  tsconfig.test.json
.all-contributorsrc
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTORS.md
LICENSE
README.md
README_SOURCE.md
generate-readme.js
generate-readme.sh
generate-styleguide.sh
is-git-status-clean.sh
package.json
```

## Entry points

- [playground/src/index.tsx](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src/index.tsx)
- [playground/src-old/App.tsx](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src-old/App.tsx)
- [playground/src-old/index.tsx](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src-old/index.tsx)
- [playground/src/api/index.ts](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src/api/index.ts)
- [playground/src/app.tsx](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src/app.tsx)
- [playground/src/components/index.ts](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src/components/index.ts)
- [playground/src/connected/index.ts](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src/connected/index.ts)
- [playground/src/hoc/index.ts](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src/hoc/index.ts)
- [playground/src/models/index.ts](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src/models/index.ts)
- [playground/src/services/index.ts](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src/services/index.ts)
- [playground/src/store/index.ts](https://github.com/piotrwitek/react-redux-typescript-guide/blob/43a22a97c407ab742f24368af4686582df6a60f0/playground/src/store/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 7 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| playground package | library | Observed | Groups 104 file(s) under playground package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.vscode/launch.json` (config)
- `configs/jest.config.json` (config)
- `package.json` (manifest)
- `playground/.vscode/settings.json` (config)
- `playground/package.json` (manifest)
- `playground/public/manifest.json` (config)
- `playground/src/api/fixtures/todos.json` (config)
- `playground/styleguide/package.json` (manifest)
- `playground/tsconfig.json` (config)
- `playground/tsconfig.test.json` (config)

## Top-level layout

- `playground` — 151 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 5 analysed file(s)
- `configs` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `43a22a97c407ab742f24368af4686582df6a60f0` is the revision these paths and observations refer to.
