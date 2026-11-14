# Project structure: TanStack/virtual

**Analysed commit:** `54a3f7d3cc32b373187b3802d81cb4b24ae08b0b`

**Commit reference:** [54a3f7d3cc32b373187b3802d81cb4b24ae08b0b](https://github.com/TanStack/virtual/commit/54a3f7d3cc32b373187b3802d81cb4b24ae08b0b)

**Tree at this commit:** [TanStack/virtual@54a3f7d3cc32](https://github.com/TanStack/virtual/tree/54a3f7d3cc32b373187b3802d81cb4b24ae08b0b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | TanStack/virtual |
| Description | 🤖 Headless UI for Virtualizing Large Element Lists in JS/TS, React, Solid, Vue and Svelte |
| Stars | 7198 |
| Forks | 495 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `54a3f7d3cc32b373187b3802d81cb4b24ae08b0b` |
| Retrieved at | 2026-11-14T19:13:58.811761+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.changeset/  (2 files)
  config.json
  shared-scroller-offscreen-range.md
.claude/  (1 files)
  scheduled_tasks.lock
.github/  (10 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    config.yml
  workflows/  (4 files)
    autofix.yml
    pr.yml
    release.yml
    zizmor.yml
  CODEOWNERS
  FUNDING.yml
  pull_request_template.md
  renovate.json
benchmarks/  (25 files)
  results/  (2 files)
    .gitkeep
    SAMPLE.json
  runner/  (1 files)
    run.mjs
  src/  (15 files)
    lib/  (4 files)
      … 4 files under this directory
    pages/  (7 files)
      … 7 files under this directory
    scenarios/  (3 files)
      … 3 files under this directory
    main.tsx
  .gitignore
  CHANGELOG.md
  README.md
  index.html
  package.json
  tsconfig.json
  vite.config.ts
docs/  (14 files)
  api/  (2 files)
    virtual-item.md
    virtualizer.md
  framework/  (7 files)
    angular/  (1 files)
      … 1 files under this directory
    lit/  (1 files)
      … 1 files under this directory
    marko/  (1 files)
      … 1 files under this directory
    react/  (1 files)
      … 1 files under this directory
    solid/  (1 files)
      … 1 files under this directory
    svelte/  (1 files)
      … 1 files under this directory
    vue/  (1 files)
      … 1 files under this directory
  chat.md
  config.json
  installation.md
  introduction.md
  pretext.md
examples/  (548 files)
  angular/  (125 files)
    chat/  (9 files)
      … 9 files under this directory
    dynamic/  (18 files)
      … 18 files under this directory
    fixed/  (14 files)
      … 14 files under this directory
    infinite-scroll/  (11 files)
      … 11 files under this directory
    padding/  (14 files)
      … 14 files under this directory
    smooth-scroll/  (11 files)
      … 11 files under this directory
    sticky/  (11 files)
      … 11 files under this directory
    table/  (12 files)
      … 12 files under this directory
    variable/  (14 files)
      … 14 files under this directory
    window/  (11 files)
      … 11 files under this directory
  lit/  (16 files)
    dynamic/  (8 files)
      … 8 files under this directory
    fixed/  (8 files)
      … 8 files under this directory
  marko/  (103 files)
    chat/  (6 files)
      … 6 files under this directory
    chat-pretext/  (6 files)
      … 6 files under this directory
    dynamic/  (5 files)
      … 5 files under this directory
    fixed/  (5 files)
      … 5 files under this directory
    grid/  (5 files)
      … 5 files under this directory
    infinite-scroll/  (5 files)
      … 5 files under this directory
    padding/  (6 files)
      … 6 files under this directory
    pretext/  (5 files)
      … 5 files under this directory
    scroll-padding/  (5 files)
      … 5 files under this directory
    smooth-scroll/  (5 files)
      … 5 files under this directory
    ssr/  (5 files)
      … 5 files under this directory
    ssr-fetch/  (6 files)
      … 6 files under this directory
    ssr-restore/  (6 files)
      … 6 files under this directory
    ssr-slice/  (6 files)
      … 6 files under this directory
    sticky/  (5 files)
      … 5 files under this directory
    table/  (6 files)
      … 6 files under this directory
    variable/  (5 files)
      … 5 files under this directory
    window/  (5 files)
      … 5 files under this directory
    window-ssr-slice/  (6 files)
      … 6 files under this directory
  react/  (98 files)
    chat/  (10 files)
      … 10 files under this directory
    dynamic/  (8 files)
      … 8 files under this directory
    fixed/  (8 files)
      … 8 files under this directory
    infinite-scroll/  (8 files)
      … 8 files under this directory
    padding/  (8 files)
      … 8 files under this directory
    pretext/  (7 files)
      … 7 files under this directory
    scroll-padding/  (8 files)
      … 8 files under this directory
    smooth-scroll/  (8 files)
      … 8 files under this directory
    sticky/  (8 files)
      … 8 files under this directory
    table/  (9 files)
      … 9 files under this directory
    variable/  (8 files)
      … 8 files under this directory
    window/  (8 files)
      … 8 files under this directory
  svelte/  (81 files)
    dynamic/  (16 files)
      … 16 files under this directory
    fixed/  (15 files)
      … 15 files under this directory
    infinite-scroll/  (13 files)
      … 13 files under this directory
    smooth-scroll/  (12 files)
      … 12 files under this directory
    sticky/  (12 files)
      … 12 files under this directory
    table/  (13 files)
      … 13 files under this directory
  vue/  (125 files)
    dynamic/  (17 files)
      … 17 files under this directory
    fixed/  (15 files)
      … 15 files under this directory
    infinite-scroll/  (12 files)
      … 12 files under this directory
    padding/  (15 files)
      … 15 files under this directory
    scroll-padding/  (12 files)
      … 12 files under this directory
    smooth-scroll/  (12 files)
      … 12 files under this directory
    sticky/  (12 files)
      … 12 files under this directory
    table/  (13 files)
      … 13 files under this directory
    variable/  (17 files)
      … 17 files under this directory
media/  (1 files)
  partner_logo.svg
packages/  (187 files)
  angular-virtual/  (29 files)
    e2e/  (18 files)
      … 18 files under this directory
    src/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    README.md
    angular.json
    eslint.config.js
    package.json
    playwright.config.ts
    tsconfig.json
    vite.config.ts
  lit-virtual/  (10 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    README.md
    eslint.config.js
    package.json
    tsconfig.json
    vite.config.ts
  marko-virtual/  (84 files)
    e2e/  (58 files)
      … 58 files under this directory
    src/  (5 files)
      … 5 files under this directory
    tests/  (11 files)
      … 11 files under this directory
    CHANGELOG.md
    README.md
    eslint.config.js
    marko.json
    package.json
    tsconfig.json
    tsconfig.tags.json
    tsconfig.typecheck.json
    vite.config.ts
    vitest.config.ts
  react-virtual/  (56 files)
    e2e/  (47 files)
      … 47 files under this directory
    src/  (1 files)
      … 1 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    eslint.config.js
    package.json
    playwright.config.ts
    tsconfig.json
    vite.config.ts
  solid-virtual/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    eslint.config.js
    package.json
    tsconfig.json
    vite.config.ts
  svelte-virtual/  (1 files)
    CHANGELOG.md
.gitattributes
.gitignore
.nvmrc
.prettierignore
CONTRIBUTING.md
LICENSE
README.md
eslint.config.js
knip.json
nx.json
package.json
```

## Entry points

- [benchmarks/src/main.tsx](https://github.com/TanStack/virtual/blob/54a3f7d3cc32b373187b3802d81cb4b24ae08b0b/benchmarks/src/main.tsx)
- [packages/angular-virtual/src/index.ts](https://github.com/TanStack/virtual/blob/54a3f7d3cc32b373187b3802d81cb4b24ae08b0b/packages/angular-virtual/src/index.ts)
- [packages/lit-virtual/src/index.ts](https://github.com/TanStack/virtual/blob/54a3f7d3cc32b373187b3802d81cb4b24ae08b0b/packages/lit-virtual/src/index.ts)
- [packages/marko-virtual/src/index.ts](https://github.com/TanStack/virtual/blob/54a3f7d3cc32b373187b3802d81cb4b24ae08b0b/packages/marko-virtual/src/index.ts)
- [packages/react-virtual/src/index.tsx](https://github.com/TanStack/virtual/blob/54a3f7d3cc32b373187b3802d81cb4b24ae08b0b/packages/react-virtual/src/index.tsx)
- [packages/solid-virtual/src/index.tsx](https://github.com/TanStack/virtual/blob/54a3f7d3cc32b373187b3802d81cb4b24ae08b0b/packages/solid-virtual/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| benchmarks package | library | Observed | Groups 16 file(s) under benchmarks package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 27 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 69 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 36 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/renovate.json` (config)
- `.github/workflows/autofix.yml` (ci)
- `.github/workflows/pr.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `benchmarks/package.json` (manifest)
- `benchmarks/results/SAMPLE.json` (config)
- `benchmarks/tsconfig.json` (config)
- `docs/config.json` (config)
- `examples/angular/chat/angular.json` (config)
- `examples/angular/chat/package.json` (manifest)
- `examples/angular/chat/tsconfig.app.json` (config)
- `examples/angular/chat/tsconfig.json` (config)
- `examples/angular/dynamic/.devcontainer/devcontainer.json` (config)
- `examples/angular/dynamic/angular.json` (config)
- `examples/angular/dynamic/package.json` (manifest)
- `examples/angular/dynamic/tsconfig.app.json` (config)
- `examples/angular/dynamic/tsconfig.json` (config)
- `examples/angular/fixed/.devcontainer/devcontainer.json` (config)
- `examples/angular/fixed/angular.json` (config)
- `examples/angular/fixed/package.json` (manifest)
- `examples/angular/fixed/tsconfig.app.json` (config)
- `examples/angular/fixed/tsconfig.json` (config)
- `examples/angular/infinite-scroll/.devcontainer/devcontainer.json` (config)
- `examples/angular/infinite-scroll/angular.json` (config)
- `examples/angular/infinite-scroll/package.json` (manifest)
- `examples/angular/infinite-scroll/tsconfig.app.json` (config)
- `examples/angular/infinite-scroll/tsconfig.json` (config)
- `examples/angular/padding/.devcontainer/devcontainer.json` (config)
- `examples/angular/padding/angular.json` (config)
- `examples/angular/padding/package.json` (manifest)
- `examples/angular/padding/tsconfig.app.json` (config)
- `examples/angular/padding/tsconfig.json` (config)
- `examples/angular/smooth-scroll/.devcontainer/devcontainer.json` (config)
- `examples/angular/smooth-scroll/angular.json` (config)
- `examples/angular/smooth-scroll/package.json` (manifest)
- `examples/angular/smooth-scroll/tsconfig.app.json` (config)
- `examples/angular/smooth-scroll/tsconfig.json` (config)
- `examples/angular/sticky/.devcontainer/devcontainer.json` (config)
- `examples/angular/sticky/angular.json` (config)
- `examples/angular/sticky/package.json` (manifest)
- `examples/angular/sticky/tsconfig.app.json` (config)
- `examples/angular/sticky/tsconfig.json` (config)
- `examples/angular/table/.devcontainer/devcontainer.json` (config)
- `examples/angular/table/angular.json` (config)
- `examples/angular/table/package.json` (manifest)
- `examples/angular/table/tsconfig.app.json` (config)
- `examples/angular/table/tsconfig.json` (config)
- `examples/angular/variable/.devcontainer/devcontainer.json` (config)
- `examples/angular/variable/angular.json` (config)
- `examples/angular/variable/package.json` (manifest)
- `examples/angular/variable/tsconfig.app.json` (config)
- `examples/angular/variable/tsconfig.json` (config)
- `examples/angular/window/.devcontainer/devcontainer.json` (config)
- `examples/angular/window/angular.json` (config)
- `examples/angular/window/package.json` (manifest)
- `examples/angular/window/tsconfig.app.json` (config)
- `examples/angular/window/tsconfig.json` (config)
- `examples/lit/dynamic/package.json` (manifest)
- `examples/lit/dynamic/tsconfig.json` (config)
- `examples/lit/fixed/package.json` (manifest)
- `examples/lit/fixed/tsconfig.json` (config)
- `examples/marko/chat-pretext/marko.json` (config)
- `examples/marko/chat-pretext/package.json` (manifest)
- `examples/marko/chat-pretext/tsconfig.json` (config)
- `examples/marko/chat/marko.json` (config)
- `examples/marko/chat/package.json` (manifest)
- `examples/marko/chat/tsconfig.json` (config)
- `examples/marko/dynamic/marko.json` (config)
- `examples/marko/dynamic/package.json` (manifest)
- `examples/marko/dynamic/tsconfig.json` (config)
- `examples/marko/fixed/marko.json` (config)
- `examples/marko/fixed/package.json` (manifest)
- `examples/marko/fixed/tsconfig.json` (config)
- `examples/marko/grid/marko.json` (config)
- `examples/marko/grid/package.json` (manifest)
- `examples/marko/grid/tsconfig.json` (config)
- `examples/marko/infinite-scroll/marko.json` (config)
- `examples/marko/infinite-scroll/package.json` (manifest)
- `examples/marko/infinite-scroll/tsconfig.json` (config)
- `examples/marko/padding/marko.json` (config)
- `examples/marko/padding/package.json` (manifest)
- `examples/marko/padding/tsconfig.json` (config)
- `examples/marko/pretext/marko.json` (config)
- `examples/marko/pretext/package.json` (manifest)
- `examples/marko/pretext/tsconfig.json` (config)
- `examples/marko/scroll-padding/marko.json` (config)
- `examples/marko/scroll-padding/package.json` (manifest)
- `examples/marko/scroll-padding/tsconfig.json` (config)
- `examples/marko/smooth-scroll/marko.json` (config)
- `examples/marko/smooth-scroll/package.json` (manifest)
- `examples/marko/smooth-scroll/tsconfig.json` (config)
- `examples/marko/ssr-fetch/marko.json` (config)
- `examples/marko/ssr-fetch/package.json` (manifest)
- `examples/marko/ssr-fetch/tsconfig.json` (config)
- `examples/marko/ssr-restore/marko.json` (config)
- `examples/marko/ssr-restore/package.json` (manifest)
- `examples/marko/ssr-restore/tsconfig.json` (config)
- `examples/marko/ssr-slice/marko.json` (config)
- `examples/marko/ssr-slice/package.json` (manifest)
- `examples/marko/ssr-slice/tsconfig.json` (config)
- `examples/marko/ssr/marko.json` (config)
- `examples/marko/ssr/package.json` (manifest)
- `examples/marko/ssr/tsconfig.json` (config)
- `examples/marko/sticky/marko.json` (config)
- `examples/marko/sticky/package.json` (manifest)
- `examples/marko/sticky/tsconfig.json` (config)
- `examples/marko/table/marko.json` (config)
- `examples/marko/table/package.json` (manifest)
- `examples/marko/table/tsconfig.json` (config)
- `examples/marko/variable/marko.json` (config)
- `examples/marko/variable/package.json` (manifest)
- `examples/marko/variable/tsconfig.json` (config)
- `examples/marko/window-ssr-slice/marko.json` (config)
- `examples/marko/window-ssr-slice/package.json` (manifest)
- `examples/marko/window-ssr-slice/tsconfig.json` (config)
- `examples/marko/window/marko.json` (config)
- `examples/marko/window/package.json` (manifest)
- `examples/marko/window/tsconfig.json` (config)
- `examples/react/chat/package.json` (manifest)
- `examples/react/chat/tsconfig.json` (config)
- `examples/react/dynamic/package.json` (manifest)
- `examples/react/dynamic/tsconfig.json` (config)
- `examples/react/fixed/package.json` (manifest)
- `examples/react/fixed/tsconfig.json` (config)
- `examples/react/infinite-scroll/package.json` (manifest)
- `examples/react/infinite-scroll/tsconfig.json` (config)
- `examples/react/padding/package.json` (manifest)
- `examples/react/padding/tsconfig.json` (config)
- `examples/react/pretext/package.json` (manifest)
- `examples/react/pretext/tsconfig.json` (config)
- `examples/react/scroll-padding/package.json` (manifest)
- `examples/react/scroll-padding/tsconfig.json` (config)
- `examples/react/smooth-scroll/package.json` (manifest)
- `examples/react/smooth-scroll/tsconfig.json` (config)
- `examples/react/sticky/package.json` (manifest)
- `examples/react/sticky/tsconfig.json` (config)
- `examples/react/table/package.json` (manifest)
- `examples/react/table/tsconfig.json` (config)
- `examples/react/variable/package.json` (manifest)
- `examples/react/variable/tsconfig.json` (config)
- `examples/react/window/package.json` (manifest)
- `examples/react/window/tsconfig.json` (config)
- `examples/svelte/dynamic/package.json` (manifest)
- `examples/svelte/dynamic/tsconfig.json` (config)
- `examples/svelte/dynamic/tsconfig.node.json` (config)
- `examples/svelte/fixed/package.json` (manifest)
- `examples/svelte/fixed/tsconfig.json` (config)
- `examples/svelte/fixed/tsconfig.node.json` (config)
- `examples/svelte/infinite-scroll/package.json` (manifest)
- `examples/svelte/infinite-scroll/tsconfig.json` (config)
- `examples/svelte/infinite-scroll/tsconfig.node.json` (config)
- `examples/svelte/smooth-scroll/package.json` (manifest)
- `examples/svelte/smooth-scroll/tsconfig.json` (config)
- `examples/svelte/smooth-scroll/tsconfig.node.json` (config)
- `examples/svelte/sticky/package.json` (manifest)
- `examples/svelte/sticky/tsconfig.json` (config)
- `examples/svelte/sticky/tsconfig.node.json` (config)
- `examples/svelte/table/package.json` (manifest)
- `examples/svelte/table/tsconfig.json` (config)
- `examples/svelte/table/tsconfig.node.json` (config)
- `examples/vue/dynamic/package.json` (manifest)
- `examples/vue/dynamic/tsconfig.json` (config)
- `examples/vue/dynamic/tsconfig.node.json` (config)
- `examples/vue/fixed/package.json` (manifest)
- `examples/vue/fixed/tsconfig.json` (config)
- `examples/vue/fixed/tsconfig.node.json` (config)
- `examples/vue/infinite-scroll/package.json` (manifest)
- `examples/vue/infinite-scroll/tsconfig.json` (config)
- `examples/vue/infinite-scroll/tsconfig.node.json` (config)
- `examples/vue/padding/package.json` (manifest)
- `examples/vue/padding/tsconfig.json` (config)
- `examples/vue/padding/tsconfig.node.json` (config)
- `examples/vue/scroll-padding/package.json` (manifest)
- `examples/vue/scroll-padding/tsconfig.json` (config)
- `examples/vue/scroll-padding/tsconfig.node.json` (config)
- `examples/vue/smooth-scroll/package.json` (manifest)
- `examples/vue/smooth-scroll/tsconfig.json` (config)
- `examples/vue/smooth-scroll/tsconfig.node.json` (config)
- `examples/vue/sticky/package.json` (manifest)
- `examples/vue/sticky/tsconfig.json` (config)
- `examples/vue/sticky/tsconfig.node.json` (config)
- `examples/vue/table/package.json` (manifest)
- `examples/vue/table/tsconfig.json` (config)
- `examples/vue/table/tsconfig.node.json` (config)
- `examples/vue/variable/package.json` (manifest)
- `examples/vue/variable/tsconfig.json` (config)
- `examples/vue/variable/tsconfig.node.json` (config)
- `knip.json` (config)
- `nx.json` (config)
- `package.json` (manifest)
- `packages/angular-virtual/angular.json` (config)
- `packages/angular-virtual/e2e/app/angular.json` (config)
- `packages/angular-virtual/e2e/app/tsconfig.app.json` (config)
- `packages/angular-virtual/e2e/app/tsconfig.json` (config)
- `packages/angular-virtual/package.json` (manifest)
- `packages/angular-virtual/tsconfig.json` (config)
- `packages/lit-virtual/package.json` (manifest)
- `packages/lit-virtual/tsconfig.json` (config)
- `packages/marko-virtual/e2e/app/marko.json` (config)
- `packages/marko-virtual/e2e/app/package.json` (manifest)
- `packages/marko-virtual/e2e/app/tsconfig.json` (config)
- `packages/marko-virtual/marko.json` (config)
- `packages/marko-virtual/package.json` (manifest)
- `packages/marko-virtual/tsconfig.json` (config)
- `packages/marko-virtual/tsconfig.tags.json` (config)
- `packages/marko-virtual/tsconfig.typecheck.json` (config)
- `packages/react-virtual/e2e/app/tsconfig.json` (config)
- `packages/react-virtual/package.json` (manifest)
- `packages/react-virtual/tsconfig.json` (config)
- `packages/solid-virtual/package.json` (manifest)
- `packages/solid-virtual/tsconfig.json` (config)

## Top-level layout

- `examples` — 548 analysed file(s)
- `packages` — 187 analysed file(s)
- `benchmarks` — 25 analysed file(s)
- `docs` — 14 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 10 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.claude` — 1 analysed file(s)
- `media` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `54a3f7d3cc32b373187b3802d81cb4b24ae08b0b` is the revision these paths and observations refer to.
