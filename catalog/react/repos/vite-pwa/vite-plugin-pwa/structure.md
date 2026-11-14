# Project structure: vite-pwa/vite-plugin-pwa

**Analysed commit:** `355cf3dd283ca50da3ac4759501e9c3312a3da91`

**Commit reference:** [355cf3dd283ca50da3ac4759501e9c3312a3da91](https://github.com/vite-pwa/vite-plugin-pwa/commit/355cf3dd283ca50da3ac4759501e9c3312a3da91)

**Tree at this commit:** [vite-pwa/vite-plugin-pwa@355cf3dd283c](https://github.com/vite-pwa/vite-plugin-pwa/tree/355cf3dd283ca50da3ac4759501e9c3312a3da91)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vite-pwa/vite-plugin-pwa |
| Description | Zero-config PWA for Vite |
| Stars | 4313 |
| Forks | 261 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `355cf3dd283ca50da3ac4759501e9c3312a3da91` |
| Retrieved at | 2026-11-14T19:14:49.471343+00:00 |
| Files in this snapshot | 341 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (3 files)
    cr-comment.yml
    cr.yml
    release.yml
  pull_request_template.md
.vscode/  (1 files)
  settings.json
docs/  (81 files)
  .vitepress/  (20 files)
    theme/  (17 files)
      … 17 files under this directory
    components.d.ts
    config.ts
    contributors.ts
  deployment/  (6 files)
    apache.md
    aws.md
    index.md
    netlify.md
    nginx.md
    vercel.md
  examples/  (10 files)
    astro.md
    iles.md
    index.md
    preact.md
    react.md
    solidjs.md
    svelte.md
    sveltekit.md
    vitepress.md
    vue.md
  frameworks/  (10 files)
    astro.md
    iles.md
    index.md
    preact.md
    react.md
    solidjs.md
    svelte.md
    sveltekit.md
    vitepress.md
    vue.md
  guide/  (13 files)
    auto-update.md
    development.md
    faq.md
    index.md
    inject-manifest.md
    periodic-sw-updates.md
    prompt-for-update.md
    pwa-minimal-requirements.md
    register-service-worker.md
    service-worker-precache.md
    service-worker-strategies-and-behaviors.md
    static-assets.md
    unregister-service-worker.md
  plugins/  (1 files)
    navbar.ts
  public/  (10 files)
    _headers
    banner_dark.svg
    banner_light.svg
    favicon.svg
    icon_dark.svg
    icon_gray.svg
    icon_light.svg
    netlify.svg
    robots.txt
    safari-pinned-tab.svg
  scripts/  (3 files)
    assets.ts
    build.ts
    pwa.ts
  workbox/  (3 files)
    generate-sw.md
    index.md
    inject-manifest.md
  index.md
  netlify.toml
  package.json
  tsconfig.json
  vite.config.ts
examples/  (196 files)
  assets-generator/  (9 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    index.html
    package.json
    pwa-assets.config.ts
    tsconfig.json
    vite.config.ts
  preact-router/  (25 files)
    client-test/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (14 files)
      … 14 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.html
    package.json
    playwright.config.ts
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
    vitest.config.mts
  react-router/  (25 files)
    client-test/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (13 files)
      … 13 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    playwright.config.ts
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
    vitest.config.mts
  solid-router/  (27 files)
    client-test/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (15 files)
      … 15 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    playwright.config.ts
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
    vitest.config.mts
  svelte-routify/  (27 files)
    client-test/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (13 files)
      … 13 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    playwright.config.ts
    svelte.config.js
    tsconfig.json
    tsconfig.node.json
    vite-env.d.ts
    vite.config.js
    vitest.config.mts
  sveltekit-pwa/  (20 files)
    src/  (11 files)
      … 11 files under this directory
    static/  (1 files)
      … 1 files under this directory
    .eslintrc.cjs
    .gitignore
    README.md
    package.json
    pwa-configuration.js
    pwa.js
    svelte.config.js
    tsconfig.json
  vanilla-js-custom-sw/  (6 files)
    public/  (1 files)
      … 1 files under this directory
    service-worker/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    index.html
    package.json
    vite.config.js
  vanilla-ts-dev-options/  (8 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  vanilla-ts-no-ip/  (13 files)
    client-test/  (1 files)
      … 1 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    playwright.config.ts
    tsconfig.json
    vite.config.ts
    vitest.config.mts
  vue-basic-cdn/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  vue-router/  (25 files)
    client-test/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    src/  (13 files)
      … 13 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    playwright.config.ts
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
    vitest.config.mts
scripts/  (4 files)
  build.ts
  commands.ts
  dev.ts
  run-examples.ts
src/  (34 files)
  client/  (7 files)
    dev/  (6 files)
      … 6 files under this directory
    type.d.ts
  plugins/  (5 files)
    build.ts
    dev.ts
    info.ts
    main.ts
    pwa-assets.ts
  pwa-assets/  (9 files)
    build.ts
    config.ts
    dev.ts
    generator.ts
    html.ts
    manifest.ts
    options.ts
    types.ts
    utils.ts
  api.ts
  assets.ts
  cache.ts
  constants.ts
  context.ts
  html.ts
  index.ts
  log.ts
  modules.ts
  options.ts
  types.ts
  utils.ts
  vite-build.ts
types/  (2 files)
  index.d.ts
  package.json
.gitignore
CONTRIBUTING.md
LICENSE
README.md
client.d.ts
eslint.config.js
index.d.ts
info.d.ts
netlify.toml
package.json
pnpm-workspace.yaml
preact.d.ts
pwa-assets.d.ts
react.d.ts
solid.d.ts
svelte.d.ts
tsconfig.json
vanillajs.d.ts
vue.d.ts
```

## Entry points

- [src/index.ts](https://github.com/vite-pwa/vite-plugin-pwa/blob/355cf3dd283ca50da3ac4759501e9c3312a3da91/src/index.ts)
- [src/plugins/main.ts](https://github.com/vite-pwa/vite-plugin-pwa/blob/355cf3dd283ca50da3ac4759501e9c3312a3da91/src/plugins/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| api.ts package | library | Observed | Groups 1 file(s) under api.ts package (observed from repository paths and static analysis). |
| assets.ts package | library | Observed | Groups 1 file(s) under assets.ts package (observed from repository paths and static analysis). |
| cache.ts package | library | Observed | Groups 1 file(s) under cache.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.ts package | library | Observed | Groups 1 file(s) under constants.ts package (observed from repository paths and static analysis). |
| context.ts package | library | Observed | Groups 1 file(s) under context.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 11 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 7 file(s) under external integrations (observed from repository paths and static analysis). |
| html.ts package | library | Observed | Groups 1 file(s) under html.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| log.ts package | library | Observed | Groups 1 file(s) under log.ts package (observed from repository paths and static analysis). |
| modules.ts package | library | Observed | Groups 1 file(s) under modules.ts package (observed from repository paths and static analysis). |
| options.ts package | library | Observed | Groups 1 file(s) under options.ts package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 5 file(s) under plugins package (observed from repository paths and static analysis). |
| pwa-assets package | library | Observed | Groups 9 file(s) under pwa-assets package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |
| vite-build.ts package | library | Observed | Groups 1 file(s) under vite-build.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/cr-comment.yml` (ci)
- `.github/workflows/cr.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.vscode/settings.json` (config)
- `docs/netlify.toml` (config)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `examples/assets-generator/package.json` (manifest)
- `examples/assets-generator/tsconfig.json` (config)
- `examples/preact-router/package.json` (manifest)
- `examples/preact-router/tsconfig.json` (config)
- `examples/preact-router/tsconfig.node.json` (config)
- `examples/react-router/package.json` (manifest)
- `examples/react-router/tsconfig.json` (config)
- `examples/react-router/tsconfig.node.json` (config)
- `examples/solid-router/package.json` (manifest)
- `examples/solid-router/tsconfig.json` (config)
- `examples/solid-router/tsconfig.node.json` (config)
- `examples/svelte-routify/package.json` (manifest)
- `examples/svelte-routify/tsconfig.json` (config)
- `examples/svelte-routify/tsconfig.node.json` (config)
- `examples/sveltekit-pwa/package.json` (manifest)
- `examples/sveltekit-pwa/tsconfig.json` (config)
- `examples/vanilla-js-custom-sw/package.json` (manifest)
- `examples/vanilla-ts-dev-options/package.json` (manifest)
- `examples/vanilla-ts-dev-options/tsconfig.json` (config)
- `examples/vanilla-ts-no-ip/package.json` (manifest)
- `examples/vanilla-ts-no-ip/tsconfig.json` (config)
- `examples/vue-basic-cdn/package.json` (manifest)
- `examples/vue-basic-cdn/tsconfig.json` (config)
- `examples/vue-basic-cdn/tsconfig.node.json` (config)
- `examples/vue-router/package.json` (manifest)
- `examples/vue-router/tsconfig.json` (config)
- `examples/vue-router/tsconfig.node.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `types/package.json` (manifest)

## Top-level layout

- `examples` — 196 analysed file(s)
- `docs` — 81 analysed file(s)
- `src` — 34 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `types` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (1 x likely secret file excluded; 6 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `355cf3dd283ca50da3ac4759501e9c3312a3da91` is the revision these paths and observations refer to.
