# Project structure: clauderic/dnd-kit

**Analysed commit:** `ccaf3d583903a5d0b68616310a24aec891ee0d69`

**Commit reference:** [ccaf3d583903a5d0b68616310a24aec891ee0d69](https://github.com/clauderic/dnd-kit/commit/ccaf3d583903a5d0b68616310a24aec891ee0d69)

**Tree at this commit:** [clauderic/dnd-kit@ccaf3d583903](https://github.com/clauderic/dnd-kit/tree/ccaf3d583903a5d0b68616310a24aec891ee0d69)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | clauderic/dnd-kit |
| Description | The modern toolkit for building drag and drop interfaces |
| Stars | 17795 |
| Forks | 933 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `ccaf3d583903a5d0b68616310a24aec891ee0d69` |
| Retrieved at | 2026-11-14T19:13:12.632788+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (7 files)
  assets/  (1 files)
    dnd-kit-hero-banner.svg
  workflows/  (5 files)
    chromatic.yml
    continous-release.yml
    playwright.yml
    release.yml
    tests.yml
  FUNDING.yml
.vscode/  (1 files)
  settings.json
apps/  (546 files)
  docs/  (187 files)
    docs/  (102 files)
      … 102 files under this directory
    public/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    src/  (71 files)
      … 71 files under this directory
    .env.example
    .gitignore
    .prettierignore
    .prettierrc
    astro.config.mjs
    eslint.config.js
    package.json
    tsconfig.json
    wrangler.json
  stories/  (133 files)
    .storybook/  (7 files)
      … 7 files under this directory
    stories/  (104 files)
      … 104 files under this directory
    tests/  (17 files)
      … 17 files under this directory
    .eslintrc.js
    package.json
    playwright.config.ts
    raw.d.ts
    tsconfig.json
  stories-shared/  (27 files)
    assets/  (3 files)
      … 3 files under this directory
    components/  (7 files)
      … 7 files under this directory
    styles/  (2 files)
      … 2 files under this directory
    tests/  (9 files)
      … 9 files under this directory
    utilities/  (3 files)
      … 3 files under this directory
    package.json
    preview-head.html
    register.ts
  stories-solid/  (34 files)
    .storybook/  (6 files)
      … 6 files under this directory
    stories/  (18 files)
      … 18 files under this directory
    tests/  (5 files)
      … 5 files under this directory
    custom-elements.d.ts
    package.json
    playwright.config.ts
    raw.d.ts
    tsconfig.json
  stories-svelte/  (50 files)
    .storybook/  (5 files)
      … 5 files under this directory
    stories/  (34 files)
      … 34 files under this directory
    tests/  (6 files)
      … 6 files under this directory
    package.json
    playwright.config.ts
    raw.d.ts
    svelte.config.js
    vite.config.ts
  stories-vanilla/  (23 files)
    .storybook/  (6 files)
      … 6 files under this directory
    stories/  (15 files)
      … 15 files under this directory
    package.json
    raw.d.ts
  stories-vue/  (36 files)
    .storybook/  (6 files)
      … 6 files under this directory
    stories/  (22 files)
      … 22 files under this directory
    tests/  (5 files)
      … 5 files under this directory
    package.json
    playwright.config.ts
    raw.d.ts
  templates/  (56 files)
    react-draggable/  (7 files)
      … 7 files under this directory
    react-sortable/  (6 files)
      … 6 files under this directory
    solid-draggable/  (7 files)
      … 7 files under this directory
    solid-sortable/  (6 files)
      … 6 files under this directory
    svelte-draggable/  (7 files)
      … 7 files under this directory
    svelte-sortable/  (8 files)
      … 8 files under this directory
    vue-draggable/  (8 files)
      … 8 files under this directory
    vue-sortable/  (7 files)
      … 7 files under this directory
config/  (6 files)
  typescript/  (6 files)
    base.json
    react.json
    solid.json
    svelte.json
    vanilla.json
    vue.json
packages/  (229 files)
  abstract/  (48 files)
    src/  (38 files)
      … 38 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    .eslintrc.js
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsup.config.ts
  collision/  (13 files)
    src/  (9 files)
      … 9 files under this directory
    CHANGELOG.md
    LICENSE
    package.json
    tsconfig.json
  dom/  (151 files)
    src/  (136 files)
      … 136 files under this directory
    tests/  (9 files)
      … 9 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsup.config.ts
  eslint-config/  (2 files)
    README.md
    package.json
  geometry/  (15 files)
    src/  (10 files)
      … 10 files under this directory
    .eslintrc.js
    CHANGELOG.md
    LICENSE
    README.md
    package.json
.browserslistrc
.eslintrc.js
.gitignore
.nvmrc
.prettierrc
CONTRIBUTING.md
LICENSE
README.md
package.json
```

## Entry points

- [apps/stories-shared/components/index.ts](https://github.com/clauderic/dnd-kit/blob/ccaf3d583903a5d0b68616310a24aec891ee0d69/apps/stories-shared/components/index.ts)
- [apps/stories-shared/styles/index.ts](https://github.com/clauderic/dnd-kit/blob/ccaf3d583903a5d0b68616310a24aec891ee0d69/apps/stories-shared/styles/index.ts)
- [apps/stories-shared/utilities/index.ts](https://github.com/clauderic/dnd-kit/blob/ccaf3d583903a5d0b68616310a24aec891ee0d69/apps/stories-shared/utilities/index.ts)
- [apps/stories-solid/.storybook/main.ts](https://github.com/clauderic/dnd-kit/blob/ccaf3d583903a5d0b68616310a24aec891ee0d69/apps/stories-solid/.storybook/main.ts)
- [apps/stories-svelte/.storybook/main.ts](https://github.com/clauderic/dnd-kit/blob/ccaf3d583903a5d0b68616310a24aec891ee0d69/apps/stories-svelte/.storybook/main.ts)
- [apps/stories-vanilla/.storybook/main.ts](https://github.com/clauderic/dnd-kit/blob/ccaf3d583903a5d0b68616310a24aec891ee0d69/apps/stories-vanilla/.storybook/main.ts)
- [apps/stories-vue/.storybook/main.ts](https://github.com/clauderic/dnd-kit/blob/ccaf3d583903a5d0b68616310a24aec891ee0d69/apps/stories-vue/.storybook/main.ts)
- [apps/stories/.storybook/main.ts](https://github.com/clauderic/dnd-kit/blob/ccaf3d583903a5d0b68616310a24aec891ee0d69/apps/stories/.storybook/main.ts)
- [packages/collision/src/index.ts](https://github.com/clauderic/dnd-kit/blob/ccaf3d583903a5d0b68616310a24aec891ee0d69/packages/collision/src/index.ts)
- [packages/geometry/src/index.ts](https://github.com/clauderic/dnd-kit/blob/ccaf3d583903a5d0b68616310a24aec891ee0d69/packages/geometry/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 229 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 36 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 118 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 79 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 54 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/chromatic.yml` (ci)
- `.github/workflows/continous-release.yml` (ci)
- `.github/workflows/playwright.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.vscode/settings.json` (config)
- `apps/docs/.env.example` (config)
- `apps/docs/docs/docs.json` (config)
- `apps/docs/package.json` (manifest)
- `apps/docs/tsconfig.json` (config)
- `apps/docs/wrangler.json` (config)
- `apps/stories-shared/package.json` (manifest)
- `apps/stories-solid/package.json` (manifest)
- `apps/stories-solid/tsconfig.json` (config)
- `apps/stories-svelte/package.json` (manifest)
- `apps/stories-vanilla/package.json` (manifest)
- `apps/stories-vue/package.json` (manifest)
- `apps/stories/package.json` (manifest)
- `apps/stories/tsconfig.json` (config)
- `apps/templates/react-draggable/package.json` (manifest)
- `apps/templates/react-sortable/package.json` (manifest)
- `apps/templates/solid-draggable/package.json` (manifest)
- `apps/templates/solid-sortable/package.json` (manifest)
- `apps/templates/svelte-draggable/package.json` (manifest)
- `apps/templates/svelte-sortable/package.json` (manifest)
- `apps/templates/vue-draggable/package.json` (manifest)
- `apps/templates/vue-sortable/package.json` (manifest)
- `config/typescript/base.json` (config)
- `config/typescript/react.json` (config)
- `config/typescript/solid.json` (config)
- `config/typescript/svelte.json` (config)
- `config/typescript/vanilla.json` (config)
- `config/typescript/vue.json` (config)
- `package.json` (manifest)
- `packages/abstract/package.json` (manifest)
- `packages/abstract/tsconfig.json` (config)
- `packages/collision/package.json` (manifest)
- `packages/collision/tsconfig.json` (config)
- `packages/dom/package.json` (manifest)
- `packages/dom/tsconfig.json` (config)
- `packages/eslint-config/package.json` (manifest)
- `packages/geometry/package.json` (manifest)

## Top-level layout

- `apps` — 546 analysed file(s)
- `packages` — 229 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 7 analysed file(s)
- `config` — 6 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ccaf3d583903a5d0b68616310a24aec891ee0d69` is the revision these paths and observations refer to.
