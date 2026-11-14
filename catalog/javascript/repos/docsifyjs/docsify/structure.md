# Project structure: docsifyjs/docsify

**Analysed commit:** `0e0cd50b326042d37b1f613eb654434c5db0e2df`

**Commit reference:** [0e0cd50b326042d37b1f613eb654434c5db0e2df](https://github.com/docsifyjs/docsify/commit/0e0cd50b326042d37b1f613eb654434c5db0e2df)

**Tree at this commit:** [docsifyjs/docsify@0e0cd50b3260](https://github.com/docsifyjs/docsify/tree/0e0cd50b326042d37b1f613eb654434c5db0e2df)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | docsifyjs/docsify |
| Description | 🃏 A magical documentation site generator. |
| Stars | 31590 |
| Forks | 5780 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `0e0cd50b326042d37b1f613eb654434c5db0e2df` |
| Retrieved at | 2026-11-14T19:10:45.932574+00:00 |
| Files in this snapshot | 198 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  crowdin/  (1 files)
    crowdin-push.yml
  workflows/  (3 files)
    crowdin.yml
    emoji.yml
    test.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.husky/  (2 files)
  install.mjs
  pre-commit
.vscode/  (2 files)
  launch.json
  settings.json
docs/  (35 files)
  _media/  (9 files)
    example-with-yaml.md
    example.html
    example.js
    example.md
    icon.svg
    moon.svg
    powered-by-vercel.svg
    sun.svg
    vercel_logo.svg
  .nojekyll
  CNAME
  README.md
  _coverpage.md
  _navbar.md
  _sidebar.md
  adding-pages.md
  cdn.md
  configuration.md
  cover.md
  custom-navbar.md
  deploy.md
  embed-files.md
  emoji.md
  helpers.md
  index.html
  language-highlight.md
  markdown.md
  plugins.md
  pwa.md
  quickstart.md
  themes.md
  ui-kit.md
  v5-upgrade.md
  … 2 more files
src/  (77 files)
  core/  (44 files)
    event/  (1 files)
      … 1 files under this directory
    fetch/  (1 files)
      … 1 files under this directory
    init/  (1 files)
      … 1 files under this directory
    render/  (20 files)
      … 20 files under this directory
    router/  (5 files)
      … 5 files under this directory
    util/  (6 files)
      … 6 files under this directory
    virtual-routes/  (3 files)
      … 3 files under this directory
    Docsify.js
    config.js
    global-api.js
    globals.ts
    index.js
    module.js
    modules.ts
  plugins/  (16 files)
    front-matter/  (3 files)
      … 3 files under this directory
    search/  (5 files)
      … 5 files under this directory
    disqus.js
    emoji.js
    external-script.js
    ga.js
    gitalk.js
    gtag.js
    matomo.js
    zoom-image.js
  themes/  (17 files)
    addons/  (2 files)
      … 2 files under this directory
    shared/  (14 files)
      … 14 files under this directory
    core.css
test/  (49 files)
  config/  (6 files)
    jest.setup-tests.js
    jest.setup.js
    jest.teardown.js
    playwright.setup.js
    playwright.teardown.js
    server.js
  consume-types/  (8 files)
    README.md
    example.js
    index.html
    package.json
    prism.js
    register-sw.js
    sw.js
    tsconfig.json
  e2e/  (14 files)
    fixtures/  (1 files)
      … 1 files under this directory
    anchor-scroll.test.js
    configuration.test.js
    embed.test.js
    example.test.js
    gtag.test.js
    index-file.test.js
    module.test.js
    plugins.test.js
    search.test.js
    security.test.js
    sidebar.test.js
    virtual-routes.test.js
    vue.test.js
  helpers/  (2 files)
    docsify-init.js
    wait-for.js
  integration/  (11 files)
    __snapshots__/  (2 files)
      … 2 files under this directory
    callouts.test.js
    docs.test.js
    docsify.test.js
    embed.test.js
    emoji.test.js
    example.test.js
    global-apis.test.js
    render.test.js
    sidebar.test.js
  unit/  (7 files)
    ajax.test.js
    core-util.test.js
    embed-cache.test.js
    render-util.test.js
    router-history-base.test.js
    router-util.test.js
    search-markdown-to-txt.test.js
  README.md
.editorconfig
.gitattributes
.gitignore
.gitpod.yml
.npmignore
.prettierignore
.prettierrc.json
CHANGELOG.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
babel.config.json
eslint.config.js
jest.config.js
middleware.js
package.json
playwright.config.js
postcss.config.cjs
rollup.config.js
server.configs.js
server.js
tsconfig.json
vercel.json
```

## Entry points

- [server.js](https://github.com/docsifyjs/docsify/blob/0e0cd50b326042d37b1f613eb654434c5db0e2df/server.js)
- [src/core/event/index.js](https://github.com/docsifyjs/docsify/blob/0e0cd50b326042d37b1f613eb654434c5db0e2df/src/core/event/index.js)
- [src/core/fetch/index.js](https://github.com/docsifyjs/docsify/blob/0e0cd50b326042d37b1f613eb654434c5db0e2df/src/core/fetch/index.js)
- [src/core/index.js](https://github.com/docsifyjs/docsify/blob/0e0cd50b326042d37b1f613eb654434c5db0e2df/src/core/index.js)
- [src/core/render/index.js](https://github.com/docsifyjs/docsify/blob/0e0cd50b326042d37b1f613eb654434c5db0e2df/src/core/render/index.js)
- [src/core/router/index.js](https://github.com/docsifyjs/docsify/blob/0e0cd50b326042d37b1f613eb654434c5db0e2df/src/core/router/index.js)
- [src/core/util/index.js](https://github.com/docsifyjs/docsify/blob/0e0cd50b326042d37b1f613eb654434c5db0e2df/src/core/util/index.js)
- [src/core/virtual-routes/index.js](https://github.com/docsifyjs/docsify/blob/0e0cd50b326042d37b1f613eb654434c5db0e2df/src/core/virtual-routes/index.js)
- [src/plugins/front-matter/index.js](https://github.com/docsifyjs/docsify/blob/0e0cd50b326042d37b1f613eb654434c5db0e2df/src/plugins/front-matter/index.js)
- [src/plugins/search/index.js](https://github.com/docsifyjs/docsify/blob/0e0cd50b326042d37b1f613eb654434c5db0e2df/src/plugins/search/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 15 file(s) under plugins package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 44 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 49 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/crowdin/crowdin-push.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/crowdin.yml` (ci)
- `.github/workflows/emoji.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.gitpod.yml` (config)
- `.prettierrc.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `babel.config.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `src` — 77 analysed file(s)
- `test` — 49 analysed file(s)
- `docs` — 35 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `.github` — 9 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (1 x lockfile excluded; 5 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0e0cd50b326042d37b1f613eb654434c5db0e2df` is the revision these paths and observations refer to.
