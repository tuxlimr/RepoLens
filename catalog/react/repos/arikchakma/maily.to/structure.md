# Project structure: arikchakma/maily.to

**Analysed commit:** `042d13169b39e0ae8c692a25693bebdbb9b894c0`

**Commit reference:** [042d13169b39e0ae8c692a25693bebdbb9b894c0](https://github.com/arikchakma/maily.to/commit/042d13169b39e0ae8c692a25693bebdbb9b894c0)

**Tree at this commit:** [arikchakma/maily.to@042d13169b39](https://github.com/arikchakma/maily.to/tree/042d13169b39e0ae8c692a25693bebdbb9b894c0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | arikchakma/maily.to |
| Description | Craft beautiful emails effortlessly with Maily, the powerful email editor that ensures impeccable communication across all major clients. |
| Stars | 4000 |
| Forks | 253 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `042d13169b39e0ae8c692a25693bebdbb9b894c0` |
| Retrieved at | 2026-11-14T19:14:56.302176+00:00 |
| Files in this snapshot | 247 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
.vscode/  (1 files)
  settings.json
apps/  (76 files)
  web/  (76 files)
    app/  (60 files)
      … 60 files under this directory
    public/  (8 files)
      … 8 files under this directory
    .env.example
    .gitignore
    package.json
    react-router.config.ts
    readme.md
    tsconfig.json
    vite-env.d.ts
    vite.config.ts
packages/  (159 files)
  core/  (134 files)
    src/  (128 files)
      … 128 files under this directory
    .prettierrc.cjs
    package.json
    postcss.config.cjs
    readme.md
    tsconfig.json
    tsup.config.ts
  render/  (12 files)
    src/  (7 files)
      … 7 files under this directory
    .babelrc
    package.json
    readme.md
    tsconfig.json
    tsdown.config.ts
  shared/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    package.json
    readme.md
    tsconfig.json
    tsdown.config.ts
  tsconfig/  (5 files)
    base.json
    library.json
    nextjs.json
    package.json
    react-library.json
.gitignore
.prettierignore
.prettierrc.cjs
license
package.json
pnpm-workspace.yaml
readme.md
tsconfig.json
turbo.json
vitest.config.ts
```

## Entry points

- [packages/core/src/index.ts](https://github.com/arikchakma/maily.to/blob/042d13169b39e0ae8c692a25693bebdbb9b894c0/packages/core/src/index.ts)
- [packages/render/src/index.ts](https://github.com/arikchakma/maily.to/blob/042d13169b39e0ae8c692a25693bebdbb9b894c0/packages/render/src/index.ts)
- [packages/shared/src/index.ts](https://github.com/arikchakma/maily.to/blob/042d13169b39e0ae8c692a25693bebdbb9b894c0/packages/shared/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 16 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 45 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 13 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 129 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.vscode/settings.json` (config)
- `apps/web/.env.example` (config)
- `apps/web/app/lib/default-editor-json.json` (config)
- `apps/web/package.json` (manifest)
- `apps/web/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/render/package.json` (manifest)
- `packages/render/tsconfig.json` (config)
- `packages/shared/package.json` (manifest)
- `packages/shared/tsconfig.json` (config)
- `packages/tsconfig/base.json` (config)
- `packages/tsconfig/library.json` (config)
- `packages/tsconfig/nextjs.json` (config)
- `packages/tsconfig/package.json` (manifest)
- `packages/tsconfig/react-library.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 159 analysed file(s)
- `apps` — 76 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `042d13169b39e0ae8c692a25693bebdbb9b894c0` is the revision these paths and observations refer to.
