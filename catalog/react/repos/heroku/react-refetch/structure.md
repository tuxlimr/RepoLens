# Project structure: heroku/react-refetch

**Analysed commit:** `acdf8d91e8b856183040db5b1f35545f793c4b71`

**Commit reference:** [acdf8d91e8b856183040db5b1f35545f793c4b71](https://github.com/heroku/react-refetch/commit/acdf8d91e8b856183040db5b1f35545f793c4b71)

**Tree at this commit:** [heroku/react-refetch@acdf8d91e8b8](https://github.com/heroku/react-refetch/tree/acdf8d91e8b856183040db5b1f35545f793c4b71)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | heroku/react-refetch |
| Description | A simple, declarative, and composable way to fetch data for React components |
| Stars | 3398 |
| Forks | 137 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `acdf8d91e8b856183040db5b1f35545f793c4b71` |
| Retrieved at | 2026-11-14T19:15:20.466373+00:00 |
| Files in this snapshot | 35 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
docs/  (1 files)
  api.md
examples/  (6 files)
  ts/  (6 files)
    .gitignore
    UserPage.tsx
    UserWidgetComp.tsx
    UserWidgetFunc.tsx
    tsconfig.json
    types.ts
src/  (10 files)
  components/  (1 files)
    connect.js
  utils/  (6 files)
    buildRequest.js
    checkTypes.js
    errors.js
    handleResponse.js
    isPlainObject.js
    shallowEqual.js
  PromiseState.js
  index.d.ts
  index.js
test/  (6 files)
  components/  (1 files)
    connect.spec.js
  utils/  (3 files)
    errors.spec.js
    isPlainObject.spec.js
    shallowEqual.spec.js
  PromiseState.spec.js
  setup.js
.babelrc
.eslintignore
.eslintrc
.gitignore
CHANGELOG.md
CODEOWNERS
CODE_OF_CONDUCT.md
LICENSE.md
README.md
SECURITY.md
package.json
```

## Entry points

- [src/index.js](https://github.com/heroku/react-refetch/blob/acdf8d91e8b856183040db5b1f35545f793c4b71/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 1 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| PromiseState.js package | library | Observed | Groups 1 file(s) under promisestate.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 6 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci.yml` (ci)
- `examples/ts/tsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 11 analysed file(s)
- `src` — 10 analysed file(s)
- `examples` — 6 analysed file(s)
- `test` — 6 analysed file(s)
- `.github` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `acdf8d91e8b856183040db5b1f35545f793c4b71` is the revision these paths and observations refer to.
