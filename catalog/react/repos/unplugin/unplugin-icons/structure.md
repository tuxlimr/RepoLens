# Project structure: unplugin/unplugin-icons

**Analysed commit:** `9a0ca853f0c68a43fe6f1aae4c6fa156ab0eea4b`

**Commit reference:** [9a0ca853f0c68a43fe6f1aae4c6fa156ab0eea4b](https://github.com/unplugin/unplugin-icons/commit/9a0ca853f0c68a43fe6f1aae4c6fa156ab0eea4b)

**Tree at this commit:** [unplugin/unplugin-icons@9a0ca853f0c6](https://github.com/unplugin/unplugin-icons/tree/9a0ca853f0c68a43fe6f1aae4c6fa156ab0eea4b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | unplugin/unplugin-icons |
| Description | 🤹 Access thousands of icons as components on-demand universally. |
| Stars | 4962 |
| Forks | 164 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `9a0ca853f0c68a43fe6f1aae4c6fa156ab0eea4b` |
| Retrieved at | 2026-11-14T19:14:34.358418+00:00 |
| Files in this snapshot | 243 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    release.yml
    relese-commit.yml
  FUNDING.yml
.vscode/  (1 files)
  settings.json
examples/  (180 files)
  astro/  (9 files)
    custom-a/  (1 files)
      … 1 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .stackblitz.js
    astro.config.mjs
    package.json
    tsconfig.json
  astro-vue/  (10 files)
    custom-a/  (1 files)
      … 1 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .stackblitz.js
    astro.config.mjs
    package.json
    tsconfig.json
  next/  (11 files)
    custom-a/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    styles/  (2 files)
      … 2 files under this directory
    .gitignore
    .stackblitz.js
    next-env.d.ts
    next.config.js
    package.json
    tsconfig.json
  nuxt4/  (12 files)
    app/  (5 files)
      … 5 files under this directory
    .gitignore
    .stackblitz.js
    README.md
    nuxt.config.ts
    package.json
    pnpm-workspace.yaml
    tsconfig.json
  rspack-vue3/  (13 files)
    custom-a/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    .stackblitz.js
    README.md
    index.html
    package.json
    rspack.config.mjs
  sveltekit/  (9 files)
    custom-a/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .stackblitz.js
    package.json
    svelte.config.js
    tsconfig.json
    vite.config.ts
  vite-ember/  (9 files)
    app/  (3 files)
      … 3 files under this directory
    custom-a/  (1 files)
      … 1 files under this directory
    babel.config.cjs
    index.html
    package.json
    tsconfig.json
    vite.config.mjs
  vite-preact/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    .stackblitz.js
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  vite-qwik/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    .stackblitz.js
    package.json
    tsconfig.json
    vite.config.ts
  vite-react/  (10 files)
    src/  (5 files)
      … 5 files under this directory
    .stackblitz.js
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  vite-solid/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    .stackblitz.js
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  vite-svelte/  (10 files)
    src/  (4 files)
      … 4 files under this directory
    .stackblitz.js
    index.html
    package.json
    svelte.config.js
    tsconfig.json
    vite.config.js
  vite-vanilla/  (5 files)
    .stackblitz.js
    index.html
    main.ts
    package.json
    vite.config.ts
  vite-vue3/  (19 files)
    @test-scope/  (4 files)
      … 4 files under this directory
    assets/  (3 files)
      … 3 files under this directory
    plain-color-icons/  (4 files)
      … 4 files under this directory
    .stackblitz.js
    App.vue
    components.d.ts
    getConfig.ts
    index.html
    main.ts
    package.json
    vite.config.ts
  vite-vue3-legacy/  (10 files)
    assets/  (3 files)
      … 3 files under this directory
    .stackblitz.js
    App.vue
    components.d.ts
    index.html
    main.ts
    package.json
    vite.config.ts
  vite-web-components/  (4 files)
    .stackblitz.js
    index.html
    package.json
    vite.config.ts
  webpack/  (4 files)
    custom-a/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    package.json
    webpack.config.js
  webpack-ember/  (13 files)
    app/  (6 files)
      … 6 files under this directory
    config/  (4 files)
      … 4 files under this directory
    .ember-cli
    ember-cli-build.js
    package.json
  README.md
scripts/  (1 files)
  prebuild.ts
src/  (30 files)
  core/  (19 files)
    compilers/  (14 files)
      … 14 files under this directory
    collections.ts
    icon-sets.json
    loader.ts
    options.ts
    svgId.ts
  esbuild.ts
  index.ts
  loaders.ts
  nuxt.ts
  resolver.ts
  rolldown.ts
  rollup.ts
  rspack.ts
  types.ts
  vite.ts
  webpack.ts
test/  (3 files)
  __snapshots__/  (1 files)
    idSvg.test.ts.snap
  idSvg.test.ts
  vueVapor.test.ts
types/  (15 files)
  astro.d.ts
  ember.d.ts
  index.d.ts
  preact.d.ts
  qwik.d.ts
  raw.d.ts
  react.d.ts
  solid.d.ts
  svelte.d.ts
  svelte3.d.ts
  svelte4.d.ts
  svelte5.d.ts
  vue.d.ts
  vue3.d.ts
  web-components.d.ts
.gitattributes
.gitignore
CONTRIBUTING.md
LICENSE
README.md
eslint.config.js
package.json
pnpm-workspace.yaml
tsconfig.json
tsdown.config.ts
```

## Entry points

- [examples/vite-vue3/@test-scope/test-color-icons/index.js](https://github.com/unplugin/unplugin-icons/blob/9a0ca853f0c68a43fe6f1aae4c6fa156ab0eea4b/examples/vite-vue3/%40test-scope/test-color-icons/index.js)
- [examples/vite-vue3/plain-color-icons/index.js](https://github.com/unplugin/unplugin-icons/blob/9a0ca853f0c68a43fe6f1aae4c6fa156ab0eea4b/examples/vite-vue3/plain-color-icons/index.js)
- [src/core/compilers/index.ts](https://github.com/unplugin/unplugin-icons/blob/9a0ca853f0c68a43fe6f1aae4c6fa156ab0eea4b/src/core/compilers/index.ts)
- [src/index.ts](https://github.com/unplugin/unplugin-icons/blob/9a0ca853f0c68a43fe6f1aae4c6fa156ab0eea4b/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| esbuild.ts package | library | Observed | Groups 1 file(s) under esbuild.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| loaders.ts package | library | Observed | Groups 1 file(s) under loaders.ts package (observed from repository paths and static analysis). |
| nuxt.ts package | library | Observed | Groups 1 file(s) under nuxt.ts package (observed from repository paths and static analysis). |
| resolver.ts package | library | Observed | Groups 1 file(s) under resolver.ts package (observed from repository paths and static analysis). |
| rolldown.ts package | library | Observed | Groups 1 file(s) under rolldown.ts package (observed from repository paths and static analysis). |
| rollup.ts package | library | Observed | Groups 1 file(s) under rollup.ts package (observed from repository paths and static analysis). |
| rspack.ts package | library | Observed | Groups 1 file(s) under rspack.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 18 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 15 file(s) under types package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| vite.ts package | library | Observed | Groups 1 file(s) under vite.ts package (observed from repository paths and static analysis). |
| webpack.ts package | library | Observed | Groups 1 file(s) under webpack.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/relese-commit.yml` (ci)
- `.vscode/settings.json` (config)
- `examples/astro-vue/package.json` (manifest)
- `examples/astro-vue/tsconfig.json` (config)
- `examples/astro/package.json` (manifest)
- `examples/astro/tsconfig.json` (config)
- `examples/next/package.json` (manifest)
- `examples/next/tsconfig.json` (config)
- `examples/nuxt4/package.json` (manifest)
- `examples/nuxt4/pnpm-workspace.yaml` (config)
- `examples/nuxt4/tsconfig.json` (config)
- `examples/rspack-vue3/package.json` (manifest)
- `examples/sveltekit/package.json` (manifest)
- `examples/sveltekit/tsconfig.json` (config)
- `examples/vite-ember/package.json` (manifest)
- `examples/vite-ember/tsconfig.json` (config)
- `examples/vite-preact/package.json` (manifest)
- `examples/vite-preact/tsconfig.json` (config)
- `examples/vite-qwik/package.json` (manifest)
- `examples/vite-qwik/tsconfig.json` (config)
- `examples/vite-react/package.json` (manifest)
- `examples/vite-react/tsconfig.json` (config)
- `examples/vite-solid/package.json` (manifest)
- `examples/vite-solid/tsconfig.json` (config)
- `examples/vite-svelte/package.json` (manifest)
- `examples/vite-svelte/tsconfig.json` (config)
- `examples/vite-vanilla/package.json` (manifest)
- `examples/vite-vue3-legacy/package.json` (manifest)
- `examples/vite-vue3/@test-scope/test-color-icons/package.json` (manifest)
- `examples/vite-vue3/package.json` (manifest)
- `examples/vite-vue3/plain-color-icons/package.json` (manifest)
- `examples/vite-web-components/package.json` (manifest)
- `examples/webpack-ember/config/ember-cli-update.json` (config)
- `examples/webpack-ember/config/optional-features.json` (config)
- `examples/webpack-ember/package.json` (manifest)
- `examples/webpack/package.json` (manifest)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `src/core/icon-sets.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `examples` — 180 analysed file(s)
- `src` — 30 analysed file(s)
- `types` — 15 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 3 analysed file(s)
- `test` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9a0ca853f0c68a43fe6f1aae4c6fa156ab0eea4b` is the revision these paths and observations refer to.
