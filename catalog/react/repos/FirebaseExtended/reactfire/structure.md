# Project structure: FirebaseExtended/reactfire

**Analysed commit:** `9b2bb79824d69ffc6368658a9569643c7013b4a1`

**Commit reference:** [9b2bb79824d69ffc6368658a9569643c7013b4a1](https://github.com/FirebaseExtended/reactfire/commit/9b2bb79824d69ffc6368658a9569643c7013b4a1)

**Tree at this commit:** [FirebaseExtended/reactfire@9b2bb79824d6](https://github.com/FirebaseExtended/reactfire/tree/9b2bb79824d69ffc6368658a9569643c7013b4a1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FirebaseExtended/reactfire |
| Description | Hooks, Context Providers, and Components that make it easy to interact with Firebase. |
| Stars | 3567 |
| Forks | 402 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `9b2bb79824d69ffc6368658a9569643c7013b4a1` |
| Retrieved at | 2026-11-14T19:15:13.821116+00:00 |
| Files in this snapshot | 174 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (2 files)
    docs.yaml
    test.yaml
  CONTRIBUTING.md
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
docs/  (92 files)
  reference/  (89 files)
    classes/  (1 files)
      … 1 files under this directory
    functions/  (45 files)
      … 45 files under this directory
    interfaces/  (11 files)
      … 11 files under this directory
    type-aliases/  (3 files)
      … 3 files under this directory
    variables/  (28 files)
      … 28 files under this directory
    README.md
  quickstart.md
  upgrade-guide.md
  use.md
example/  (27 files)
  display/  (3 files)
    Button.tsx
    Card.tsx
    LoadingSpinner.tsx
  withSuspense/  (6 files)
    App.tsx
    Auth.tsx
    Firestore.tsx
    RealtimeDatabase.tsx
    RemoteConfig.tsx
    Storage.tsx
  withoutSuspense/  (8 files)
    Analytics.tsx
    App.tsx
    Auth.tsx
    Firestore.tsx
    Functions.tsx
    RealtimeDatabase.tsx
    RemoteConfig.tsx
    Storage.tsx
  .npmignore
  index.css
  index.html
  index.tsx
  package.json
  postcss.config.cjs
  tailwind.config.cjs
  tsconfig.json
  tsconfig.node.json
  vite.config.js
functions/  (3 files)
  .gitignore
  index.js
  package.json
src/  (14 files)
  SuspenseSubject.ts
  auth.tsx
  database.tsx
  firebaseApp.tsx
  firestore.tsx
  functions.tsx
  index.ts
  performance.tsx
  remote-config.tsx
  sdk.tsx
  storage.tsx
  telemetry.ts
  useObservable.ts
  utils.ts
test/  (16 files)
  appConfig.ts
  auth.test.tsx
  database.test.tsx
  firebaseApp.test.tsx
  firestore.test.tsx
  functions.test.tsx
  performance.test.tsx
  preload-suspense-policy.test.tsx
  sdk-init-cache.test.tsx
  sdk.test.tsx
  setupTests.ts
  storage.test.tsx
  suspenseSubject-error-branch.test.tsx
  test-utils.ts
  tsconfig.json
  useObservable.test.tsx
.gitattributes
.gitignore
.nvmrc
.oxlintrc.json
LICENSE
README.md
build.sh
database.rules.json
firebase.json
firestore.indexes.json
firestore.rules
package.json
storage.rules
tsconfig.json
tsconfig.test.json
typedoc.json
vite.config.ts
```

## Entry points

- [functions/index.js](https://github.com/FirebaseExtended/reactfire/blob/9b2bb79824d69ffc6368658a9569643c7013b4a1/functions/index.js)
- [src/index.ts](https://github.com/FirebaseExtended/reactfire/blob/9b2bb79824d69ffc6368658a9569643c7013b4a1/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| auth.tsx package | library | Observed | Groups 1 file(s) under auth.tsx package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| database.tsx package | library | Observed | Groups 1 file(s) under database.tsx package (observed from repository paths and static analysis). |
| firebaseApp.tsx package | library | Observed | Groups 1 file(s) under firebaseapp.tsx package (observed from repository paths and static analysis). |
| firestore.tsx package | library | Observed | Groups 1 file(s) under firestore.tsx package (observed from repository paths and static analysis). |
| functions package | library | Observed | Groups 1 file(s) under functions package (observed from repository paths and static analysis). |
| functions.tsx package | library | Observed | Groups 1 file(s) under functions.tsx package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| performance.tsx package | library | Observed | Groups 1 file(s) under performance.tsx package (observed from repository paths and static analysis). |
| remote-config.tsx package | library | Observed | Groups 1 file(s) under remote-config.tsx package (observed from repository paths and static analysis). |
| sdk.tsx package | library | Observed | Groups 1 file(s) under sdk.tsx package (observed from repository paths and static analysis). |
| storage.tsx package | library | Observed | Groups 1 file(s) under storage.tsx package (observed from repository paths and static analysis). |
| SuspenseSubject.ts package | library | Observed | Groups 1 file(s) under suspensesubject.ts package (observed from repository paths and static analysis). |
| telemetry.ts package | library | Observed | Groups 1 file(s) under telemetry.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). |
| useObservable.ts package | library | Observed | Groups 1 file(s) under useobservable.ts package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/docs.yaml` (ci)
- `.github/workflows/test.yaml` (ci)
- `.oxlintrc.json` (config)
- `database.rules.json` (config)
- `example/package.json` (manifest)
- `example/tsconfig.json` (config)
- `example/tsconfig.node.json` (config)
- `firebase.json` (config)
- `firestore.indexes.json` (config)
- `functions/package.json` (manifest)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tsconfig.test.json` (config)
- `typedoc.json` (config)

## Top-level layout

- `docs` — 92 analysed file(s)
- `example` — 27 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `test` — 16 analysed file(s)
- `src` — 14 analysed file(s)
- `.github` — 5 analysed file(s)
- `functions` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9b2bb79824d69ffc6368658a9569643c7013b4a1` is the revision these paths and observations refer to.
