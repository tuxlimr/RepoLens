# Project structure: puckeditor/puck

**Analysed commit:** `ab5624ddcb0435cc9575b5154433be7aadf84809`

**Commit reference:** [ab5624ddcb0435cc9575b5154433be7aadf84809](https://github.com/puckeditor/puck/commit/ab5624ddcb0435cc9575b5154433be7aadf84809)

**Tree at this commit:** [puckeditor/puck@ab5624ddcb04](https://github.com/puckeditor/puck/tree/ab5624ddcb0435cc9575b5154433be7aadf84809)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | puckeditor/puck |
| Description | The visual editor for React. |
| Stars | 13708 |
| Forks | 1054 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `ab5624ddcb0435cc9575b5154433be7aadf84809` |
| Retrieved at | 2026-11-14T19:13:18.006789+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    config.yml
    feature_request.md
  workflows/  (3 files)
    ci.yml
    publish-canary.yml
    publish.yml
  dependabot.yml
  pull_request_template.md
apps/  (262 files)
  demo/  (95 files)
    app/  (12 files)
      … 12 files under this directory
    components/  (2 files)
      … 2 files under this directory
    config/  (68 files)
      … 68 files under this directory
    lib/  (3 files)
      … 3 files under this directory
    tsconfig/  (2 files)
      … 2 files under this directory
    .env.example
    .gitignore
    README.md
    eslint.config.mjs
    instrumentation-client.ts
    next.config.js
    package.json
    tsconfig.json
  docs/  (167 files)
    components/  (15 files)
      … 15 files under this directory
    pages/  (137 files)
      … 137 files under this directory
    public/  (3 files)
      … 3 files under this directory
    tsconfig/  (2 files)
      … 2 files under this directory
    .gitignore
    eslint.config.mjs
    middleware.ts
    next-sitemap.config.js
    next.config.mjs
    package.json
    releases.json
    styles.css
    theme.config.tsx
    tsconfig.json
packages/  (484 files)
  core/  (443 files)
    __tests__/  (1 files)
      … 1 files under this directory
    bundle/  (9 files)
      … 9 files under this directory
    components/  (200 files)
      … 200 files under this directory
    lib/  (168 files)
      … 168 files under this directory
    plugins/  (7 files)
      … 7 files under this directory
    reducer/  (23 files)
      … 23 files under this directory
    store/  (10 files)
      … 10 files under this directory
    styles/  (3 files)
      … 3 files under this directory
    types/  (14 files)
      … 14 files under this directory
    .gitignore
    globals.d.ts
    index.ts
    jest.config.ts
    package.json
    styles.css
    tsconfig.json
    tsup.config.ts
  create-puck-app/  (11 files)
    scripts/  (1 files)
      … 1 files under this directory
    templates/  (7 files)
      … 7 files under this directory
    README.md
    index.js
    package.json
  eslint-config-custom/  (2 files)
    index.mjs
    package.json
  field-contentful/  (5 files)
    README.md
    index.ts
    package.json
    tsconfig.json
    tsup.config.ts
  plugin-emotion-cache/  (5 files)
    README.md
    index.tsx
    package.json
    tsconfig.json
    tsup.config.ts
  plugin-heading-analyzer/  (10 files)
    src/  (3 files)
      … 3 files under this directory
    README.md
    globals.d.ts
    index.ts
    jest.config.ts
    package.json
    tsconfig.json
    tsup.config.ts
  tsconfig/  (4 files)
    base.json
    nextjs.json
    package.json
    react-library.json
  tsup-config/  (4 files)
    css-module-plugin.ts
    index.ts
    package.json
    react-import.js
recipes/  (31 files)
  next/  (8 files)
    app/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
  next-ai/  (23 files)
    app/  (10 files)
      … 10 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    tsconfig/  (2 files)
      … 2 files under this directory
    .env.example
    .gitignore
    README.md
    database.json
    eslint.config.mjs
    next.config.js
    package.json
    proxy.ts
    puck.config.tsx
    tsconfig.json
.eslintrc.js
.gitignore
.nvmrc
.prettierignore
.prettierrc.json
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
eslint.config.mjs
lerna.json
package.json
pnpm-workspace.yaml
```

## Entry points

- [packages/create-puck-app/index.js](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/packages/create-puck-app/index.js)
- [packages/eslint-config-custom/index.mjs](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/packages/eslint-config-custom/index.mjs)
- [apps/demo/app/page.tsx](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/apps/demo/app/page.tsx)
- [apps/demo/config/index.tsx](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/apps/demo/config/index.tsx)
- [packages/core/bundle/index.ts](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/packages/core/bundle/index.ts)
- [packages/core/index.ts](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/packages/core/index.ts)
- [packages/core/lib/index.ts](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/packages/core/lib/index.ts)
- [packages/core/reducer/index.ts](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/packages/core/reducer/index.ts)
- [packages/core/store/index.ts](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/packages/core/store/index.ts)
- [packages/core/types/index.ts](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/packages/core/types/index.ts)
- [packages/field-contentful/index.ts](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/packages/field-contentful/index.ts)
- [packages/plugin-emotion-cache/index.tsx](https://github.com/puckeditor/puck/blob/ab5624ddcb0435cc9575b5154433be7aadf84809/packages/plugin-emotion-cache/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 16 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 78 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 41 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 16 file(s) under packages package (observed from repository paths and static analysis). |
| recipes package | library | Observed | Groups 18 file(s) under recipes package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 335 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/publish-canary.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.prettierrc.json` (config)
- `apps/demo/.env.example` (config)
- `apps/demo/package.json` (manifest)
- `apps/demo/tsconfig.json` (config)
- `apps/demo/tsconfig/base.json` (config)
- `apps/demo/tsconfig/nextjs.json` (config)
- `apps/docs/package.json` (manifest)
- `apps/docs/releases.json` (config)
- `apps/docs/tsconfig.json` (config)
- `apps/docs/tsconfig/base.json` (config)
- `apps/docs/tsconfig/nextjs.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/create-puck-app/package.json` (manifest)
- `packages/eslint-config-custom/package.json` (manifest)
- `packages/field-contentful/package.json` (manifest)
- `packages/field-contentful/tsconfig.json` (config)
- `packages/plugin-emotion-cache/package.json` (manifest)
- `packages/plugin-emotion-cache/tsconfig.json` (config)
- `packages/plugin-heading-analyzer/package.json` (manifest)
- `packages/plugin-heading-analyzer/tsconfig.json` (config)
- `packages/tsconfig/base.json` (config)
- `packages/tsconfig/nextjs.json` (config)
- `packages/tsconfig/package.json` (manifest)
- `packages/tsconfig/react-library.json` (config)
- `packages/tsup-config/package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `recipes/next-ai/.env.example` (config)
- `recipes/next-ai/database.json` (config)
- `recipes/next-ai/package.json` (manifest)
- `recipes/next-ai/tsconfig.json` (config)
- `recipes/next-ai/tsconfig/base.json` (config)
- `recipes/next-ai/tsconfig/nextjs.json` (config)

## Top-level layout

- `packages` — 484 analysed file(s)
- `apps` — 262 analysed file(s)
- `recipes` — 31 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ab5624ddcb0435cc9575b5154433be7aadf84809` is the revision these paths and observations refer to.
