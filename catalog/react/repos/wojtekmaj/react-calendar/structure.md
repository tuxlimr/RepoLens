# Project structure: wojtekmaj/react-calendar

**Analysed commit:** `80319ee35958e755fbee08e995f7d923e7f1255e`

**Commit reference:** [80319ee35958e755fbee08e995f7d923e7f1255e](https://github.com/wojtekmaj/react-calendar/commit/80319ee35958e755fbee08e995f7d923e7f1255e)

**Tree at this commit:** [wojtekmaj/react-calendar@80319ee35958](https://github.com/wojtekmaj/react-calendar/tree/80319ee35958e755fbee08e995f7d923e7f1255e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wojtekmaj/react-calendar |
| Description | Ultimate calendar for your React app. |
| Stars | 3789 |
| Forks | 530 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `80319ee35958e755fbee08e995f7d923e7f1255e` |
| Retrieved at | 2026-11-14T19:15:05.194559+00:00 |
| Files in this snapshot | 92 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    Bug_report.yml
    Feature_request.yml
    config.yml
  workflows/  (3 files)
    ci.yml
    close-stale-issues.yml
    publish.yml
  FUNDING.yml
.husky/  (1 files)
  pre-commit
.vscode/  (2 files)
  extensions.json
  settings.json
packages/  (51 files)
  react-calendar/  (51 files)
    src/  (45 files)
      … 45 files under this directory
    LICENSE
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vitest.config.ts
sample/  (8 files)
  .gitignore
  Sample.css
  Sample.tsx
  index.html
  index.tsx
  package.json
  tsconfig.json
  vite.config.ts
test/  (17 files)
  shared/  (2 files)
    dateFormatter.ts
    types.ts
  .gitignore
  DateBoundariesOptions.tsx
  LocaleOptions.tsx
  MaxDetailOptions.tsx
  MinDetailOptions.tsx
  Test.css
  Test.tsx
  ValueOptions.tsx
  ViewOptions.tsx
  global.d.ts
  index.html
  index.tsx
  package.json
  tsconfig.json
  vite.config.ts
.gitattributes
.gitignore
.yarnrc.yml
LICENSE
biome.json
package.json
```

## Entry points

- [packages/react-calendar/src/index.ts](https://github.com/wojtekmaj/react-calendar/blob/80319ee35958e755fbee08e995f7d923e7f1255e/packages/react-calendar/src/index.ts)
- [sample/index.tsx](https://github.com/wojtekmaj/react-calendar/blob/80319ee35958e755fbee08e995f7d923e7f1255e/sample/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 45 file(s) under packages package (observed from repository paths and static analysis). |
| sample package | library | Observed | Groups 3 file(s) under sample package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/Bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/Feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/close-stale-issues.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `.yarnrc.yml` (config)
- `biome.json` (config)
- `package.json` (manifest)
- `packages/react-calendar/package.json` (manifest)
- `packages/react-calendar/tsconfig.build.json` (config)
- `packages/react-calendar/tsconfig.json` (config)
- `sample/package.json` (manifest)
- `sample/tsconfig.json` (config)

## Top-level layout

- `packages` — 51 analysed file(s)
- `test` — 17 analysed file(s)
- `sample` — 8 analysed file(s)
- `.github` — 7 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `80319ee35958e755fbee08e995f7d923e7f1255e` is the revision these paths and observations refer to.
