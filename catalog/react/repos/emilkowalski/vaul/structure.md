# Project structure: emilkowalski/vaul

**Analysed commit:** `3e97aac6a38e4481bade71d7233ed6002e80f9b0`

**Commit reference:** [3e97aac6a38e4481bade71d7233ed6002e80f9b0](https://github.com/emilkowalski/vaul/commit/3e97aac6a38e4481bade71d7233ed6002e80f9b0)

**Tree at this commit:** [emilkowalski/vaul@3e97aac6a38e](https://github.com/emilkowalski/vaul/tree/3e97aac6a38e4481bade71d7233ed6002e80f9b0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | emilkowalski/vaul |
| Description | A drawer component for React. |
| Stars | 8737 |
| Forks | 371 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `3e97aac6a38e4481bade71d7233ed6002e80f9b0` |
| Retrieved at | 2026-11-14T19:13:39.107700+00:00 |
| Files in this snapshot | 67 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    playwright.yml
.vscode/  (1 files)
  settings.json
src/  (13 files)
  browser.ts
  constants.ts
  context.ts
  helpers.ts
  index.tsx
  style.css
  types.ts
  use-composed-refs.ts
  use-controllable-state.ts
  use-position-fixed.ts
  use-prevent-scroll.ts
  use-scale-background.ts
  use-snap-points.ts
test/  (41 files)
  public/  (2 files)
    next.svg
    vercel.svg
  src/  (20 files)
    app/  (20 files)
      … 20 files under this directory
  tests/  (11 files)
    base.spec.ts
    constants.ts
    controlled.spec.ts
    helpers.ts
    initial-snap.spec.ts
    nested.spec.ts
    non-dismissible.spec.ts
    with-handle.spec.ts
    with-redirect.spec.ts
    with-scaled-background.spec.ts
    without-scaled-background.spec.ts
  .eslintrc.json
  .gitignore
  README.md
  next.config.js
  package.json
  postcss.config.js
  tailwind.config.ts
  tsconfig.json
.eslintrc.js
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

- [src/index.tsx](https://github.com/emilkowalski/vaul/blob/3e97aac6a38e4481bade71d7233ed6002e80f9b0/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| browser.ts package | library | Observed | Groups 1 file(s) under browser.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.ts package | library | Observed | Groups 1 file(s) under constants.ts package (observed from repository paths and static analysis). |
| context.ts package | library | Observed | Groups 1 file(s) under context.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| helpers.ts package | library | Observed | Groups 1 file(s) under helpers.ts package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 41 file(s) under tests (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| use-composed-refs.ts package | library | Observed | Groups 1 file(s) under use-composed-refs.ts package (observed from repository paths and static analysis). |
| use-controllable-state.ts package | library | Observed | Groups 1 file(s) under use-controllable-state.ts package (observed from repository paths and static analysis). |
| use-position-fixed.ts package | library | Observed | Groups 1 file(s) under use-position-fixed.ts package (observed from repository paths and static analysis). |
| use-prevent-scroll.ts package | library | Observed | Groups 1 file(s) under use-prevent-scroll.ts package (observed from repository paths and static analysis). |
| use-scale-background.ts package | library | Observed | Groups 1 file(s) under use-scale-background.ts package (observed from repository paths and static analysis). |
| use-snap-points.ts package | library | Observed | Groups 1 file(s) under use-snap-points.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/playwright.yml` (ci)
- `.vscode/settings.json` (config)
- `FUNDING.yml` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)

## Top-level layout

- `test` — 41 analysed file(s)
- `src` — 13 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3e97aac6a38e4481bade71d7233ed6002e80f9b0` is the revision these paths and observations refer to.
