# Project structure: bernaferrari/FigmaToCode

**Analysed commit:** `f5c4831d5de6cffc19a73fe2823c56b4bb551281`

**Commit reference:** [f5c4831d5de6cffc19a73fe2823c56b4bb551281](https://github.com/bernaferrari/FigmaToCode/commit/f5c4831d5de6cffc19a73fe2823c56b4bb551281)

**Tree at this commit:** [bernaferrari/FigmaToCode@f5c4831d5de6](https://github.com/bernaferrari/FigmaToCode/tree/f5c4831d5de6cffc19a73fe2823c56b4bb551281)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bernaferrari/FigmaToCode |
| Description | Generate responsive pages and apps on HTML, Tailwind, Flutter and SwiftUI. |
| Stars | 5269 |
| Forks | 508 |
| Licence | GPL-3.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `f5c4831d5de6cffc19a73fe2823c56b4bb551281` |
| Retrieved at | 2026-11-14T19:14:22.961949+00:00 |
| Files in this snapshot | 188 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.yaml
  workflows/  (1 files)
    test.yml
apps/  (42 files)
  plugin/  (14 files)
    plugin-src/  (2 files)
      … 2 files under this directory
    ui-src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    package.json
    postcss.config.mjs
    tsconfig.json
    vite-env.d.ts
    vite.config.ts
  web/  (28 files)
    app/  (16 files)
      … 16 files under this directory
    components/  (1 files)
      … 1 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    .env.example
    .gitignore
    README.md
    components.json
    next-env.d.ts
    next.config.mjs
    package.json
    postcss.config.js
    tsconfig.json
packages/  (131 files)
  backend/  (92 files)
    src/  (90 files)
      … 90 files under this directory
    package.json
    tsconfig.json
  plugin-ui/  (30 files)
    src/  (28 files)
      … 28 files under this directory
    package.json
    tsconfig.json
  tsconfig/  (5 files)
    backend.json
    base.json
    nextjs.json
    package.json
    react-library.json
  types/  (4 files)
    src/  (2 files)
      … 2 files under this directory
    package.json
    tsconfig.json
.eslintrc.js
.gitignore
.node-version
.oxfmtrc.json
.oxlintrc.json
.vercelignore
LICENSE
README.md
manifest.json
package.json
pnpm-workspace.yaml
tsconfig.json
turbo.json
```

## Entry points

- [packages/backend/src/index.ts](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/packages/backend/src/index.ts)
- [packages/plugin-ui/src/index.tsx](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/packages/plugin-ui/src/index.tsx)
- [packages/types/src/index.ts](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/packages/types/src/index.ts)
- [apps/plugin/ui-src/App.tsx](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/apps/plugin/ui-src/App.tsx)
- [apps/plugin/ui-src/main.tsx](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/apps/plugin/ui-src/main.tsx)
- [apps/web/app/page.tsx](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/apps/web/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 28 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 120 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/workflows/test.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `apps/plugin/package.json` (manifest)
- `apps/plugin/plugin-src/tsconfig.json` (config)
- `apps/plugin/tsconfig.json` (config)
- `apps/web/.env.example` (config)
- `apps/web/components.json` (config)
- `apps/web/package.json` (manifest)
- `apps/web/tsconfig.json` (config)
- `manifest.json` (config)
- `package.json` (manifest)
- `packages/backend/package.json` (manifest)
- `packages/backend/tsconfig.json` (config)
- `packages/plugin-ui/package.json` (manifest)
- `packages/plugin-ui/tsconfig.json` (config)
- `packages/tsconfig/backend.json` (config)
- `packages/tsconfig/base.json` (config)
- `packages/tsconfig/nextjs.json` (config)
- `packages/tsconfig/package.json` (manifest)
- `packages/tsconfig/react-library.json` (config)
- `packages/types/package.json` (manifest)
- `packages/types/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 131 analysed file(s)
- `apps` — 42 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f5c4831d5de6cffc19a73fe2823c56b4bb551281` is the revision these paths and observations refer to.
