# Project structure: francoischalifour/medium-zoom

**Analysed commit:** `6ed91069df0236c4bf971e9213bc31b39059bf00`

**Commit reference:** [6ed91069df0236c4bf971e9213bc31b39059bf00](https://github.com/francoischalifour/medium-zoom/commit/6ed91069df0236c4bf971e9213bc31b39059bf00)

**Tree at this commit:** [francoischalifour/medium-zoom@6ed91069df02](https://github.com/francoischalifour/medium-zoom/tree/6ed91069df0236c4bf971e9213bc31b39059bf00)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | francoischalifour/medium-zoom |
| Description | 🔎🖼️ Lightweight image zoom for the web. Zero dependencies, any framework, React via shadcn. |
| Stars | 3944 |
| Forks | 168 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `6ed91069df0236c4bf971e9213bc31b39059bf00` |
| Retrieved at | 2026-11-14T19:14:58.725970+00:00 |
| Files in this snapshot | 408 |

## Directory tree

```text
.codex/  (1 files)
  environments/  (1 files)
    environment.toml
.github/  (16 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    feature_request.yml
  release-please/  (5 files)
    .gitignore
    manifest.mjs
    manifest.test.mjs
    package.json
    run.mjs
  workflows/  (5 files)
    checks.yml
    ci.yml
    deploy-preview.yml
    preview.yml
    release.yml
  .release-please-manifest.json
  dependabot.yml
  pull_request_template.md
  release-please-config.json
assets/  (1 files)
  images/  (1 files)
    CREDITS.md
config/  (12 files)
  playwright.analytics.config.mts
  playwright.config.mts
  playwright.rsc.config.mts
  size.config.mts
  test-ports.mts
  tsconfig.worker.json
  tsdown.config.mts
  vite.examples.config.mts
  vite.shared.config.mts
  vite.stories.config.mts
  vite.website.config.mts
  wrangler.jsonc
docs/  (5 files)
  assets/  (1 files)
    logo.svg
  container.md
  inline-svg.md
  template.md
  video.md
examples/  (157 files)
  angular/  (15 files)
    .codesandbox/  (1 files)
      … 1 files under this directory
    .devcontainer/  (1 files)
      … 1 files under this directory
    src/  (7 files)
      … 7 files under this directory
    .gitignore
    README.md
    angular.json
    package.json
    tsconfig.app.json
    tsconfig.json
  astro/  (11 files)
    .codesandbox/  (1 files)
      … 1 files under this directory
    .devcontainer/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    astro.config.mjs
    package.json
    tsconfig.json
  dropbox-paper-template/  (10 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    sandbox.config.json
    tsconfig.json
    vite.config.ts
  facebook-template/  (10 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    sandbox.config.json
    tsconfig.json
    vite.config.ts
  react/  (13 files)
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    sandbox.config.json
    tsconfig.json
    vite.config.ts
  react-markdown/  (13 files)
    .codesandbox/  (1 files)
      … 1 files under this directory
    .devcontainer/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  shadcn/  (16 files)
    src/  (3 files)
      … 3 files under this directory
    tests/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    gallery-assets.ts
    index.html
    package.json
    playground.html
    tsconfig.json
    vite.config.ts
  svelte/  (16 files)
    .codesandbox/  (1 files)
      … 1 files under this directory
    .devcontainer/  (1 files)
      … 1 files under this directory
    src/  (7 files)
      … 7 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    svelte.config.js
    tsconfig.json
    vite.config.ts
  svg-data-url/  (9 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  vanilla/  (10 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    sandbox.config.json
    tsconfig.json
    vite.config.ts
  video/  (9 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  vitepress/  (11 files)
    .codesandbox/  (1 files)
      … 1 files under this directory
    .devcontainer/  (1 files)
      … 1 files under this directory
    docs/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  vue/  (14 files)
    .codesandbox/  (1 files)
      … 1 files under this directory
    .devcontainer/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
scripts/  (20 files)
  build-analytics-fixture.ts
  build-examples.ts
  build-registry.ts
  check-docs.ts
  check-examples.ts
  check-package-analyzers.ts
  check-package-consumers.ts
  check-package.ts
  check-preview.sh
  check-size.ts
  ci-scope.sh
  clean.ts
  deploy-preview.sh
  dev-example.ts
  example-names.ts
  generate-og.ts
  pack.ts
  playwright-image.ts
  prerender-website.ts
  update-npm-downloads.ts
src/  (5 files)
  index.js
  medium-zoom.css
  medium-zoom.d.ts
  medium-zoom.js
  utils.js
stories/  (22 files)
  catalogue/  (5 files)
    frame.css
    frame.ts
    index.ts
    registry.ts
    stories.ts
  images/  (1 files)
    crab.svg
  attach.stories.js
  attributes.stories.js
  clone.stories.js
  close.stories.js
  detach.stories.js
  frame.html
  getImages.stories.js
  getOptions.stories.js
  getZoomedImage.stories.js
  index.html
  off.stories.js
  on.stories.js
  open.stories.js
  options.stories.js
  toggle.stories.js
  update.stories.js
tests/  (48 files)
  analytics/  (1 files)
    website.spec.ts
  browser/  (30 files)
    api.spec.ts
    dev.spec.ts
    helpers.ts
    loading.spec.ts
    mobile.spec.ts
    motion.spec.ts
    package.spec.ts
    shadcn-composition.spec.ts
    shadcn.spec.ts
    stories.helpers.ts
    stories.spec.ts
    video.spec.ts
    website-accessibility.spec.ts
    website-command-palette.spec.ts
    website-delivery.spec.ts
    website-dev.spec.ts
    website-docs.spec.ts
    website-downloads.spec.ts
    website-examples.spec.ts
    website-fixture.ts
    website-footer.spec.ts
    website-hero.spec.ts
    website-hierarchy.spec.ts
    website-markdown.spec.ts
    … 6 more files
  fixtures/  (7 files)
    next/  (7 files)
      … 7 files under this directory
  rsc/  (1 files)
    image-zoom.spec.ts
  types/  (5 files)
    bundler.mjs
    commonjs.cts
    consumer.ts
    node-esm.mts
    runtime.mjs
  globals.d.ts
  registry-downloads.test.mts
  server-urls.ts
  server.ts
website/  (104 files)
  public/  (6 files)
    brand/  (4 files)
      … 4 files under this directory
    _redirects
    favicon.svg
  src/  (89 files)
    docs/  (46 files)
      … 46 files under this directory
    App.tsx
    JavaScriptPage.tsx
    NotFoundPage.tsx
    ReactPage.tsx
    chat-links.ts
    closing-install.tsx
    code-font.ts
    command-items.ts
    command-palette.css
    command-palette.tsx
    docs-search-index.ts
    docs-search.ts
    example-rail.tsx
    gallery.ts
    hero.tsx
    hydrate.tsx
    install-command.tsx
    install-commands.ts
    javascript.css
    main.tsx
    monthly-downloads.tsx
    not-found.css
    npm-downloads.json
    npm-downloads.ts
    … 19 more files
  .gitignore
  404.html
  LICENSE
  README.md
  index.html
  package.json
  react.html
  tsconfig.json
  worker.ts
.bun-version
.editorconfig
.env.example
.gitignore
.node-version
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
bunfig.toml
oxfmt.config.mts
oxlint.config.mts
package.json
registry.json
tsconfig.json
```

## Entry points

- [examples/dropbox-paper-template/index.html](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/examples/dropbox-paper-template/index.html)
- [examples/facebook-template/index.html](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/examples/facebook-template/index.html)
- [examples/react-markdown/src/main.tsx](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/examples/react-markdown/src/main.tsx)
- [examples/react/src/main.tsx](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/examples/react/src/main.tsx)
- [examples/svelte/src/main.js](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/examples/svelte/src/main.js)
- [examples/svg-data-url/index.html](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/examples/svg-data-url/index.html)
- [examples/vanilla/index.html](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/examples/vanilla/index.html)
- [examples/video/index.html](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/examples/video/index.html)
- [examples/vue/src/main.ts](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/examples/vue/src/main.ts)
- [website/index.html](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/website/index.html)
- [src/index.js](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/src/index.js)
- [stories/catalogue/index.ts](https://github.com/francoischalifour/medium-zoom/blob/6ed91069df0236c4bf971e9213bc31b39059bf00/stories/catalogue/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| medium-zoom.d.ts package | library | Observed | Groups 1 file(s) under medium-zoom.d.ts package (observed from repository paths and static analysis). |
| medium-zoom.js package | library | Observed | Groups 1 file(s) under medium-zoom.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 20 file(s) under scripts package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 18 file(s) under stories package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 53 file(s) under tests (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 38 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.codex/environments/environment.toml` (config)
- `.editorconfig` (config)
- `.env.example` (config)
- `.github/.release-please-manifest.json` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/release-please-config.json` (config)
- `.github/release-please/package.json` (manifest)
- `.github/workflows/checks.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-preview.yml` (ci)
- `.github/workflows/preview.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `bunfig.toml` (config)
- `config/tsconfig.worker.json` (config)
- `examples/angular/.codesandbox/tasks.json` (config)
- `examples/angular/.devcontainer/devcontainer.json` (config)
- `examples/angular/angular.json` (config)
- `examples/angular/package.json` (manifest)
- `examples/angular/tsconfig.app.json` (config)
- `examples/angular/tsconfig.json` (config)
- `examples/astro/.codesandbox/tasks.json` (config)
- `examples/astro/.devcontainer/devcontainer.json` (config)
- `examples/astro/package.json` (manifest)
- `examples/astro/tsconfig.json` (config)
- `examples/dropbox-paper-template/package.json` (manifest)
- `examples/dropbox-paper-template/sandbox.config.json` (config)
- `examples/dropbox-paper-template/tsconfig.json` (config)
- `examples/facebook-template/package.json` (manifest)
- `examples/facebook-template/sandbox.config.json` (config)
- `examples/facebook-template/tsconfig.json` (config)
- `examples/react-markdown/.codesandbox/tasks.json` (config)
- `examples/react-markdown/.devcontainer/devcontainer.json` (config)
- `examples/react-markdown/package.json` (manifest)
- `examples/react-markdown/tsconfig.json` (config)
- `examples/react/package.json` (manifest)
- `examples/react/sandbox.config.json` (config)
- `examples/react/tsconfig.json` (config)
- `examples/shadcn/package.json` (manifest)
- `examples/shadcn/tsconfig.json` (config)
- `examples/svelte/.codesandbox/tasks.json` (config)
- `examples/svelte/.devcontainer/devcontainer.json` (config)
- `examples/svelte/package.json` (manifest)
- `examples/svelte/tsconfig.json` (config)
- `examples/svg-data-url/package.json` (manifest)
- `examples/svg-data-url/tsconfig.json` (config)
- `examples/vanilla/package.json` (manifest)
- `examples/vanilla/sandbox.config.json` (config)
- `examples/vanilla/tsconfig.json` (config)
- `examples/video/package.json` (manifest)
- `examples/video/tsconfig.json` (config)
- `examples/vitepress/.codesandbox/tasks.json` (config)
- `examples/vitepress/.devcontainer/devcontainer.json` (config)
- `examples/vitepress/package.json` (manifest)
- `examples/vitepress/tsconfig.json` (config)
- `examples/vue/.codesandbox/tasks.json` (config)
- `examples/vue/.devcontainer/devcontainer.json` (config)
- `examples/vue/package.json` (manifest)
- `examples/vue/tsconfig.json` (config)
- `package.json` (manifest)
- `registry.json` (config)
- `tsconfig.json` (config)
- `website/package.json` (manifest)
- `website/src/npm-downloads.json` (config)
- `website/tsconfig.json` (config)

## Top-level layout

- `examples` — 157 analysed file(s)
- `website` — 104 analysed file(s)
- `tests` — 48 analysed file(s)
- `stories` — 22 analysed file(s)
- `scripts` — 20 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 16 analysed file(s)
- `config` — 12 analysed file(s)
- `docs` — 5 analysed file(s)
- `src` — 5 analysed file(s)
- `.codex` — 1 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 17 file(s) were skipped during inventory (1 x lockfile excluded; 16 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6ed91069df0236c4bf971e9213bc31b39059bf00` is the revision these paths and observations refer to.
