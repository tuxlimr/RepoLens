# Project structure: aidenybai/react-scan

**Analysed commit:** `0fb31862b697ef3ed2d8ed6990878a35a4ca8a75`

**Commit reference:** [0fb31862b697ef3ed2d8ed6990878a35a4ca8a75](https://github.com/aidenybai/react-scan/commit/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75)

**Tree at this commit:** [aidenybai/react-scan@0fb31862b697](https://github.com/aidenybai/react-scan/tree/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | aidenybai/react-scan |
| Description | Scan and fix React performance issues |
| Stars | 21884 |
| Forks | 393 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `0fb31862b697ef3ed2d8ed6990878a35a4ca8a75` |
| Retrieved at | 2026-11-14T19:13:09.335597+00:00 |
| Files in this snapshot | 245 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.cursor/  (2 files)
  commands/  (1 files)
    deslop.md
  skills/  (1 files)
    animation-best-practices/  (1 files)
      … 1 files under this directory
.github/  (7 files)
  assets/  (2 files)
    faire-logo.svg
    logo.svg
  workflows/  (2 files)
    build-extension.yml
    pkg-pr-new.yaml
  CODEOWNERS
  CODE_OF_CONDUCT.md
  dependabot.yml
.vscode/  (1 files)
  settings.json
docs/  (11 files)
  installation/  (11 files)
    astro.md
    cdn.md
    create-react-app.md
    next-js-app-router.md
    next-js-page-router.md
    parcel.md
    react-router.md
    remix.md
    rsbuild.md
    tanstack-start.md
    vite.md
e2e/  (9 files)
  helpers.ts
  inspector.spec.ts
  notifications.spec.ts
  outlines.spec.ts
  overlay-inspector.spec.ts
  overlay-notifications.spec.ts
  overlay-toolbar.spec.ts
  overlay-widget.spec.ts
  toolbar.spec.ts
kitchen-sink/  (15 files)
  src/  (9 files)
    examples/  (5 files)
      … 5 files under this directory
    index.css
    index.tsx
    main.css
    main.tsx
  index.html
  package.json
  postcss.config.mjs
  tailwind.config.mjs
  tsconfig.json
  vite.config.ts
packages/  (187 files)
  extension/  (22 files)
    src/  (14 files)
      … 14 files under this directory
    .env.example
    .gitignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  scan/  (134 files)
    bin/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (119 files)
      … 119 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    auto.d.ts
    global.d.ts
    package.json
    postcss.config.mjs
    postcss.rem2px.mjs
    tailwind.config.mjs
    tsconfig.json
    tsup.config.ts
    vite.config.mts
    worker-plugin.ts
  vite-plugin-react-scan/  (9 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    vite.config.ts
  website/  (22 files)
    app/  (5 files)
      … 5 files under this directory
    components/  (6 files)
      … 6 files under this directory
    public/  (3 files)
      … 3 files under this directory
    .gitignore
    AGENTS.md
    README.md
    next.config.ts
    package.json
    postcss.config.mjs
    tailwind.config.ts
    tsconfig.json
.gitignore
AGENTS.md
CONTRIBUTING.md
LICENSE
README.md
package.json
playwright.config.ts
pnpm-workspace.yaml
tsconfig.json
turbo.json
vite.config.ts
```

## Entry points

- [packages/scan/bin/cli.js](https://github.com/aidenybai/react-scan/blob/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75/packages/scan/bin/cli.js)
- [kitchen-sink/src/index.tsx](https://github.com/aidenybai/react-scan/blob/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75/kitchen-sink/src/index.tsx)
- [kitchen-sink/src/main.tsx](https://github.com/aidenybai/react-scan/blob/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75/kitchen-sink/src/main.tsx)
- [packages/scan/src/index.ts](https://github.com/aidenybai/react-scan/blob/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75/packages/scan/src/index.ts)
- [packages/vite-plugin-react-scan/src/index.ts](https://github.com/aidenybai/react-scan/blob/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75/packages/vite-plugin-react-scan/src/index.ts)
- [packages/website/app/page.tsx](https://github.com/aidenybai/react-scan/blob/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75/packages/website/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 28 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 9 file(s) under e2e package (observed from repository paths and static analysis). |
| kitchen-sink package | library | Observed | Groups 8 file(s) under kitchen-sink package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 109 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build-extension.yml` (ci)
- `.github/workflows/pkg-pr-new.yaml` (ci)
- `.vscode/settings.json` (config)
- `kitchen-sink/package.json` (manifest)
- `kitchen-sink/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/extension/.env.example` (config)
- `packages/extension/package.json` (manifest)
- `packages/extension/src/manifest.chrome.json` (config)
- `packages/extension/src/manifest.firefox.json` (config)
- `packages/extension/tsconfig.json` (config)
- `packages/extension/tsconfig.node.json` (config)
- `packages/scan/package.json` (manifest)
- `packages/scan/src/react-component-name/tsconfig.json` (config)
- `packages/scan/tsconfig.json` (config)
- `packages/vite-plugin-react-scan/package.json` (manifest)
- `packages/vite-plugin-react-scan/tsconfig.json` (config)
- `packages/website/package.json` (manifest)
- `packages/website/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 187 analysed file(s)
- `kitchen-sink` — 15 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `docs` — 11 analysed file(s)
- `e2e` — 9 analysed file(s)
- `.github` — 7 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.cursor` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0fb31862b697ef3ed2d8ed6990878a35a4ca8a75` is the revision these paths and observations refer to.
