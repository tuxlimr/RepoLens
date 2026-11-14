# Project structure: emilkowalski/sonner

**Analysed commit:** `8e4662b39255120b62138312058f5d77c0139a5e`

**Commit reference:** [8e4662b39255120b62138312058f5d77c0139a5e](https://github.com/emilkowalski/sonner/commit/8e4662b39255120b62138312058f5d77c0139a5e)

**Tree at this commit:** [emilkowalski/sonner@8e4662b39255](https://github.com/emilkowalski/sonner/tree/8e4662b39255120b62138312058f5d77c0139a5e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | emilkowalski/sonner |
| Description | An opinionated toast component for React. |
| Stars | 13217 |
| Forks | 472 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `8e4662b39255120b62138312058f5d77c0139a5e` |
| Retrieved at | 2026-11-14T19:13:19.368668+00:00 |
| Files in this snapshot | 28 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    playwright.yml
src/  (6 files)
  assets.tsx
  hooks.tsx
  index.tsx
  state.ts
  styles.css
  types.ts
test/  (11 files)
  .vscode/  (1 files)
    settings.json
  src/  (3 files)
    app/  (3 files)
      … 3 files under this directory
  tests/  (1 files)
    basic.spec.ts
  .eslintrc.json
  .gitignore
  README.md
  next.config.js
  package.json
  tsconfig.json
.gitignore
.prettierrc.js
FUNDING.yml
LICENSE.md
README.md
package.json
playwright.config.ts
pnpm-workspace.yaml
tsconfig.json
turbo.json
```

## Entry points

- [src/index.tsx](https://github.com/emilkowalski/sonner/blob/8e4662b39255120b62138312058f5d77c0139a5e/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets.tsx package | library | Observed | Groups 1 file(s) under assets.tsx package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| hooks.tsx package | library | Observed | Groups 1 file(s) under hooks.tsx package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| state.ts package | library | Observed | Groups 1 file(s) under state.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/playwright.yml` (ci)
- `FUNDING.yml` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)

## Top-level layout

- `test` — 11 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `src` — 6 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8e4662b39255120b62138312058f5d77c0139a5e` is the revision these paths and observations refer to.
