# Project structure: mobxjs/mobx-react

**Analysed commit:** `baa737e4faf458e3f4c89edebacfb8774b64353d`

**Commit reference:** [baa737e4faf458e3f4c89edebacfb8774b64353d](https://github.com/mobxjs/mobx-react/commit/baa737e4faf458e3f4c89edebacfb8774b64353d)

**Tree at this commit:** [mobxjs/mobx-react@baa737e4faf4](https://github.com/mobxjs/mobx-react/tree/baa737e4faf458e3f4c89edebacfb8774b64353d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mobxjs/mobx-react |
| Description | React bindings for MobX |
| Stars | 4813 |
| Forks | 339 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `baa737e4faf458e3f4c89edebacfb8774b64353d` |
| Retrieved at | 2026-11-14T19:14:34.945216+00:00 |
| Files in this snapshot | 67 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.circleci/  (1 files)
  config.yml
.github/  (6 files)
  ISSUE_TEMPLATE/  (1 files)
    config.yml
  workflows/  (1 files)
    release.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  lock.yml
  stale.yml
.vscode/  (2 files)
  launch.json
  settings.json
__mocks__/  (1 files)
  react-native.js
src/  (13 files)
  types/  (4 files)
    IReactComponent.ts
    IStoresToProps.ts
    IValueMap.ts
    IWrappedComponent.ts
  utils/  (1 files)
    utils.ts
  Provider.tsx
  disposeOnUnmount.ts
  globals.d.ts
  index.ts
  inject.ts
  observer.tsx
  observerClass.ts
  propTypes.ts
test/  (20 files)
  __snapshots__/  (2 files)
    observer.test.tsx.snap
    stateless.test.tsx.snap
  utils/  (1 files)
    withConsole.ts
  .eslintrc.yaml
  ErrorCatcher.tsx
  Provider.test.tsx
  compile-ts.tsx
  context.test.tsx
  disposeOnUnmount.test.tsx
  hooks.test.tsx
  inject.test.tsx
  issue21.test.tsx
  issue806.test.tsx
  misc.test.tsx
  observer.test.tsx
  propTypes.test.ts
  stateless.test.tsx
  symbol.test.tsx
  transactions.test.tsx
  tsconfig.json
.babelrc
.browserlistrc
.eslintignore
.eslintrc.js
.gitignore
.prettierignore
.prettierrc
.size-limit.json
.watchmanconfig
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
README_v5.md
batchingForReactDom.js
batchingForReactNative.js
batchingOptOut.js
jest.setup.ts
package.json
tsconfig.json
tsconfig.test.json
tsdx.config.js
```

## Entry points

- [src/index.ts](https://github.com/mobxjs/mobx-react/blob/baa737e4faf458e3f4c89edebacfb8774b64353d/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| disposeOnUnmount.ts package | library | Observed | Groups 1 file(s) under disposeonunmount.ts package (observed from repository paths and static analysis). |
| globals.d.ts package | library | Observed | Groups 1 file(s) under globals.d.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| inject.ts package | library | Observed | Groups 1 file(s) under inject.ts package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| observer.tsx package | library | Observed | Groups 1 file(s) under observer.tsx package (observed from repository paths and static analysis). |
| observerClass.ts package | library | Observed | Groups 1 file(s) under observerclass.ts package (observed from repository paths and static analysis). |
| propTypes.ts package | library | Observed | Groups 1 file(s) under proptypes.ts package (observed from repository paths and static analysis). |
| Provider.tsx package | library | Observed | Groups 1 file(s) under provider.tsx package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 20 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 4 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.circleci/config.yml` (ci)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/lock.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.size-limit.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tsconfig.test.json` (config)

## Top-level layout

- `(root files)` — 22 analysed file(s)
- `test` — 20 analysed file(s)
- `src` — 13 analysed file(s)
- `.github` — 6 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `__mocks__` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `baa737e4faf458e3f4c89edebacfb8774b64353d` is the revision these paths and observations refer to.
