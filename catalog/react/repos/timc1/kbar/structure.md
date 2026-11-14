# Project structure: timc1/kbar

**Analysed commit:** `26ec0f49f92ab34fa6ab59392782d56020f28098`

**Commit reference:** [26ec0f49f92ab34fa6ab59392782d56020f28098](https://github.com/timc1/kbar/commit/26ec0f49f92ab34fa6ab59392782d56020f28098)

**Tree at this commit:** [timc1/kbar@26ec0f49f92a](https://github.com/timc1/kbar/tree/26ec0f49f92ab34fa6ab59392782d56020f28098)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | timc1/kbar |
| Description | fast, portable, and extensible cmd+k interface for your site |
| Stars | 5264 |
| Forks | 204 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `26ec0f49f92ab34fa6ab59392782d56020f28098` |
| Retrieved at | 2026-11-14T19:14:22.997701+00:00 |
| Files in this snapshot | 63 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
  stale.yml
example/  (26 files)
  src/  (24 files)
    Docs/  (11 files)
      … 11 files under this directory
    hooks/  (2 files)
      … 2 files under this directory
    App.tsx
    Blog.tsx
    Code.module.scss
    Code.tsx
    Home.tsx
    Layout.module.scss
    Layout.tsx
    Logo.tsx
    index.scss
    index.tsx
    utils.tsx
  webpack.config.cjs
  webpack.prod.cjs
src/  (24 files)
  __tests__/  (4 files)
    ActionImpl.test.ts
    ActionInterface.test.ts
    Command.test.ts
    useMatches.test.tsx
  action/  (5 files)
    ActionImpl.ts
    ActionInterface.ts
    Command.ts
    HistoryImpl.ts
    index.tsx
  InternalEvents.tsx
  KBarAnimator.tsx
  KBarContextProvider.tsx
  KBarPortal.tsx
  KBarPositioner.tsx
  KBarResults.tsx
  KBarSearch.tsx
  index.tsx
  tinykeys.ts
  types.ts
  useKBar.tsx
  useMatches.tsx
  useRegisterActions.tsx
  useStore.tsx
  utils.ts
.eslintignore
.eslintrc.json
.gitignore
.prettierrc
LICENSE
README.md
jest.config.js
package.json
tsconfig.json
vercel.json
```

## Entry points

- [src/action/index.tsx](https://github.com/timc1/kbar/blob/26ec0f49f92ab34fa6ab59392782d56020f28098/src/action/index.tsx)
- [src/index.tsx](https://github.com/timc1/kbar/blob/26ec0f49f92ab34fa6ab59392782d56020f28098/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| action package | library | Observed | Groups 5 file(s) under action package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| InternalEvents.tsx package | library | Observed | Groups 1 file(s) under internalevents.tsx package (observed from repository paths and static analysis). |
| KBarAnimator.tsx package | library | Observed | Groups 1 file(s) under kbaranimator.tsx package (observed from repository paths and static analysis). |
| KBarContextProvider.tsx package | library | Observed | Groups 1 file(s) under kbarcontextprovider.tsx package (observed from repository paths and static analysis). |
| KBarPortal.tsx package | library | Observed | Groups 1 file(s) under kbarportal.tsx package (observed from repository paths and static analysis). |
| KBarPositioner.tsx package | library | Observed | Groups 1 file(s) under kbarpositioner.tsx package (observed from repository paths and static analysis). |
| KBarResults.tsx package | library | Observed | Groups 1 file(s) under kbarresults.tsx package (observed from repository paths and static analysis). |
| KBarSearch.tsx package | library | Observed | Groups 1 file(s) under kbarsearch.tsx package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 4 file(s) under __tests__ package (observed from repository paths and static analysis). |
| tinykeys.ts package | library | Observed | Groups 1 file(s) under tinykeys.ts package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| useKBar.tsx package | library | Observed | Groups 1 file(s) under usekbar.tsx package (observed from repository paths and static analysis). |
| useMatches.tsx package | library | Observed | Groups 1 file(s) under usematches.tsx package (observed from repository paths and static analysis). |
| useRegisterActions.tsx package | library | Observed | Groups 1 file(s) under useregisteractions.tsx package (observed from repository paths and static analysis). |
| useStore.tsx package | library | Observed | Groups 1 file(s) under usestore.tsx package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `example` — 26 analysed file(s)
- `src` — 24 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `26ec0f49f92ab34fa6ab59392782d56020f28098` is the revision these paths and observations refer to.
