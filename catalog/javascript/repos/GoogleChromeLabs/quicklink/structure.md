# Project structure: GoogleChromeLabs/quicklink

**Analysed commit:** `e2f081b78f518a108a47b9046428a36f96f74f1e`

**Commit reference:** [e2f081b78f518a108a47b9046428a36f96f74f1e](https://github.com/GoogleChromeLabs/quicklink/commit/e2f081b78f518a108a47b9046428a36f96f74f1e)

**Tree at this commit:** [GoogleChromeLabs/quicklink@e2f081b78f51](https://github.com/GoogleChromeLabs/quicklink/tree/e2f081b78f518a108a47b9046428a36f96f74f1e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | GoogleChromeLabs/quicklink |
| Description | ⚡️Faster subsequent page-loads by prefetching in-viewport links during idle time |
| Stars | 11306 |
| Forks | 428 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `e2f081b78f518a108a47b9046428a36f96f74f1e` |
| Retrieved at | 2026-11-14T19:12:19.961599+00:00 |
| Files in this snapshot | 161 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (5 files)
    ci.yml
    codeql.yml
    lint.yml
    site.yml
    size-limit.yml
  dependabot.yml
assets/  (1 files)
  images/  (1 files)
    logos/  (1 files)
      … 1 files under this directory
demos/  (10 files)
  hrefFn/  (3 files)
    2.html
    2.json
    hrefFn_demo.html
  news/  (1 files)
    README.md
  news-workbox/  (1 files)
    README.md
  spa/  (1 files)
    README.md
  basic.html
  network-idle.html
  network-idle.js
  sw.js
site/  (91 files)
  .config/  (2 files)
    configstore/  (1 files)
      … 1 files under this directory
    glitch-package-manager
  src/  (76 files)
    _data/  (1 files)
      … 1 files under this directory
    _includes/  (24 files)
      … 24 files under this directory
    assets/  (16 files)
      … 16 files under this directory
    demos/  (27 files)
      … 27 files under this directory
    api.njk
    approach.njk
    demo.njk
    index.njk
    measure.njk
    robots.njk
    site.webmanifest
    sitemap.njk
  .browserslistrc
  .eleventy.js
  .eleventyignore
  .firebaserc
  .gitignore
  .stylelintignore
  .stylelintrc.json
  LICENSE
  README.md
  firebase.json
  index.njk
  package.json
  watch.json
src/  (6 files)
  chunks.mjs
  index.mjs
  prefetch.mjs
  prerender.mjs
  react-chunks.js
  request-idle-callback.mjs
test/  (32 files)
  fixtures/  (31 files)
    1.html
    2.html
    3.html
    4.html
    index.html
    main.css
    rmanifest.json
    test-allow-origin-all.html
    test-allow-origin.html
    test-basic-usage.html
    test-custom-dom-source.html
    test-custom-href-function.html
    test-delay.html
    test-es-modules.html
    test-ignore-basic.html
    test-ignore-download.html
    test-ignore-multiple.html
    test-limit.html
    test-node-list.html
    test-prefetch-chunks.html
    test-prefetch-duplicate-shared.html
    test-prefetch-duplicate.html
    test-prefetch-multiple.html
    test-prefetch-single.html
    … 7 more files
  quicklink.spec.js
translations/  (1 files)
  zh-cn/  (1 files)
    README.md
.browserslistrc
.editorconfig
.gitattributes
.gitignore
.size-limit.json
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
eslint.config.js
package.json
rollup.config.mjs
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| chunks.mjs package | library | Observed | Groups 1 file(s) under chunks.mjs package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 2 file(s) under demos package (observed from repository paths and static analysis). |
| index.mjs package | library | Observed | Groups 1 file(s) under index.mjs package (observed from repository paths and static analysis). |
| prefetch.mjs package | library | Observed | Groups 1 file(s) under prefetch.mjs package (observed from repository paths and static analysis). |
| prerender.mjs package | library | Observed | Groups 1 file(s) under prerender.mjs package (observed from repository paths and static analysis). |
| react-chunks.js package | library | Observed | Groups 1 file(s) under react-chunks.js package (observed from repository paths and static analysis). |
| request-idle-callback.mjs package | library | Observed | Groups 1 file(s) under request-idle-callback.mjs package (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 4 file(s) under site package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 32 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/site.yml` (ci)
- `.github/workflows/size-limit.yml` (ci)
- `.size-limit.json` (config)
- `demos/hrefFn/2.json` (config)
- `package.json` (manifest)
- `site/.config/configstore/update-notifier-pnpm.json` (config)
- `site/.stylelintrc.json` (config)
- `site/firebase.json` (config)
- `site/package.json` (manifest)
- `site/watch.json` (config)

## Top-level layout

- `site` — 91 analysed file(s)
- `test` — 32 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `demos` — 10 analysed file(s)
- `.github` — 8 analysed file(s)
- `src` — 6 analysed file(s)
- `assets` — 1 analysed file(s)
- `translations` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (1 x lockfile excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e2f081b78f518a108a47b9046428a36f96f74f1e` is the revision these paths and observations refer to.
