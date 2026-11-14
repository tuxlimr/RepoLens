# Project structure: GoogleChrome/workbox

**Analysed commit:** `4ea3138a120fd2c87389b54130e25f47e0fd7089`

**Commit reference:** [4ea3138a120fd2c87389b54130e25f47e0fd7089](https://github.com/GoogleChrome/workbox/commit/4ea3138a120fd2c87389b54130e25f47e0fd7089)

**Tree at this commit:** [GoogleChrome/workbox@4ea3138a120f](https://github.com/GoogleChrome/workbox/tree/4ea3138a120fd2c87389b54130e25f47e0fd7089)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | GoogleChrome/workbox |
| Description | 📦 Workbox: JavaScript libraries for Progressive Web Apps |
| Stars | 13049 |
| Forks | 890 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | v7 |
| Analysed commit | `4ea3138a120fd2c87389b54130e25f47e0fd7089` |
| Retrieved at | 2026-11-14T19:12:01.668463+00:00 |
| Files in this snapshot | 717 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (2 files)
    pull-request.yml
    scorecards-analysis.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.husky/  (3 files)
  .gitignore
  pre-commit
  pre-push
demos/  (66 files)
  src/  (65 files)
    workbox-background-sync-demo/  (5 files)
      … 5 files under this directory
    workbox-broadcast-update-demo/  (4 files)
      … 4 files under this directory
    workbox-cacheable-response/  (4 files)
      … 4 files under this directory
    workbox-core/  (4 files)
      … 4 files under this directory
    workbox-expiration/  (4 files)
      … 4 files under this directory
    workbox-google-analytics/  (4 files)
      … 4 files under this directory
    workbox-navigation-preload/  (4 files)
      … 4 files under this directory
    workbox-precaching/  (8 files)
      … 8 files under this directory
    workbox-range-requests/  (4 files)
      … 4 files under this directory
    workbox-routing/  (4 files)
      … 4 files under this directory
    workbox-strategies/  (7 files)
      … 7 files under this directory
    workbox-streams/  (4 files)
      … 4 files under this directory
    workbox-sw/  (5 files)
      … 5 files under this directory
    workbox-window/  (4 files)
      … 4 files under this directory
  README.md
gulp-tasks/  (31 files)
  utils/  (13 files)
    analyse-properties.js
    cdn-helper.js
    constants.js
    get-packages.js
    github-helper.js
    node-projects-babel.config.json
    output-filename-to-package-map.js
    package-runner.js
    pkg-path-to-name.js
    publish-helpers.js
    rollup-helper.js
    version-module.js
    versioned-cdn-url.js
  analyze-properties.js
  build-node-packages.js
  build-packages.js
  build-sw-packages.js
  build-window-packages.js
  build.js
  docs.js
  lint.js
  publish-cdn.js
  publish-github.js
  publish-glitch.js
  publish-lerna.js
  publish.js
  test-integration.js
  test-node.js
  test-server.js
  test.js
  transpile-typescript.js
infra/  (78 files)
  pr-bot/  (1 files)
    aggregate-size-plugin.js
  templates/  (24 files)
    reference-docs/  (24 files)
      … 24 files under this directory
  testing/  (50 files)
    comlink/  (3 files)
      … 3 files under this directory
    helpers/  (5 files)
      … 5 files under this directory
    server/  (26 files)
      … 26 files under this directory
    validator/  (1 files)
      … 1 files under this directory
    webdriver/  (5 files)
      … 5 files under this directory
    activate-and-control.js
    activate-sw-safari.js
    auto-stub-logger.mjs
    clean-sw.js
    confirm-directory-contains.js
    env-it.js
    expectError.js
    generate-variant-tests.js
    wait-until.js
    webpack-build-check.js
  utils/  (2 files)
    AsyncDebounce.js
    log-helper.js
  type-overrides.d.ts
packages/  (266 files)
  workbox-background-sync/  (12 files)
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-broadcast-update/  (9 files)
    src/  (6 files)
      … 6 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-build/  (46 files)
    src/  (42 files)
      … 42 files under this directory
    .ncurc.js
    README.md
    package.json
    tsconfig.json
  workbox-cacheable-response/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-cli/  (19 files)
    src/  (16 files)
      … 16 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-core/  (33 files)
    src/  (30 files)
      … 30 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-expiration/  (8 files)
    src/  (5 files)
      … 5 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-google-analytics/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-navigation-preload/  (8 files)
    src/  (5 files)
      … 5 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-precaching/  (28 files)
    src/  (25 files)
      … 25 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-range-requests/  (9 files)
    src/  (6 files)
      … 6 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-recipes/  (11 files)
    src/  (8 files)
      … 8 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-routing/  (16 files)
    src/  (13 files)
      … 13 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-strategies/  (14 files)
    src/  (11 files)
      … 11 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-streams/  (11 files)
    src/  (8 files)
      … 8 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-sw/  (6 files)
    controllers/  (1 files)
      … 1 files under this directory
    README.md
    _types.mjs
    _version.mjs
    index.mjs
    package.json
  workbox-webpack-plugin/  (12 files)
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
    tsconfig.json
  workbox-window/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    README.md
    package.json
    tsconfig.json
test/  (250 files)
  all/  (5 files)
    node/  (5 files)
      … 5 files under this directory
  workbox-background-sync/  (9 files)
    integration/  (1 files)
      … 1 files under this directory
    static/  (3 files)
      … 3 files under this directory
    sw/  (5 files)
      … 5 files under this directory
  workbox-broadcast-update/  (6 files)
    integration/  (1 files)
      … 1 files under this directory
    static/  (2 files)
      … 2 files under this directory
    sw/  (3 files)
      … 3 files under this directory
  workbox-build/  (44 files)
    node/  (26 files)
      … 26 files under this directory
    static/  (18 files)
      … 18 files under this directory
  workbox-cacheable-response/  (5 files)
    integration/  (1 files)
      … 1 files under this directory
    static/  (2 files)
      … 2 files under this directory
    sw/  (2 files)
      … 2 files under this directory
  workbox-cli/  (13 files)
    node/  (13 files)
      … 13 files under this directory
  workbox-core/  (19 files)
    integration/  (1 files)
      … 1 files under this directory
    static/  (3 files)
      … 3 files under this directory
    sw/  (15 files)
      … 15 files under this directory
  workbox-expiration/  (10 files)
    integration/  (1 files)
      … 1 files under this directory
    static/  (6 files)
      … 6 files under this directory
    sw/  (3 files)
      … 3 files under this directory
  workbox-google-analytics/  (4 files)
    integration/  (1 files)
      … 1 files under this directory
    static/  (2 files)
      … 2 files under this directory
    sw/  (1 files)
      … 1 files under this directory
  workbox-navigation-preload/  (9 files)
    integration/  (3 files)
      … 3 files under this directory
    static/  (3 files)
      … 3 files under this directory
    sw/  (3 files)
      … 3 files under this directory
  workbox-precaching/  (34 files)
    integration/  (3 files)
      … 3 files under this directory
    static/  (15 files)
      … 15 files under this directory
    sw/  (16 files)
      … 16 files under this directory
  workbox-range-requests/  (7 files)
    integration/  (1 files)
      … 1 files under this directory
    static/  (2 files)
      … 2 files under this directory
    sw/  (4 files)
      … 4 files under this directory
  workbox-routing/  (20 files)
    integration/  (4 files)
      … 4 files under this directory
    static/  (8 files)
      … 8 files under this directory
    sw/  (8 files)
      … 8 files under this directory
  workbox-strategies/  (21 files)
    integration/  (6 files)
      … 6 files under this directory
    static/  (6 files)
      … 6 files under this directory
    sw/  (9 files)
      … 9 files under this directory
  workbox-streams/  (6 files)
    integration/  (1 files)
      … 1 files under this directory
    static/  (3 files)
      … 3 files under this directory
    sw/  (2 files)
      … 2 files under this directory
  workbox-sw/  (9 files)
    integration/  (1 files)
      … 1 files under this directory
    static/  (7 files)
      … 7 files under this directory
    sw/  (1 files)
      … 1 files under this directory
  workbox-webpack-plugin/  (24 files)
    node/  (7 files)
      … 7 files under this directory
    static/  (17 files)
      … 17 files under this directory
  workbox-window/  (5 files)
    integration/  (1 files)
      … 1 files under this directory
    static/  (1 files)
      … 1 files under this directory
    window/  (3 files)
      … 3 files under this directory
.gitattributes
.gitignore
.ncurc.js
.nvmrc
.prettierignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
cdn-details.json
gulpfile.js
javascript.eslintrc.js
jsdoc.conf
lerna.json
package.json
prettier.config.js
tsconfig.json
typescript.eslintrc.js
```

## Entry points

- [demos/src/workbox-cacheable-response/server.js](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/demos/src/workbox-cacheable-response/server.js)
- [demos/src/workbox-streams/server.js](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/demos/src/workbox-streams/server.js)
- [infra/testing/server/index.js](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/infra/testing/server/index.js)
- [packages/workbox-background-sync/src/index.ts](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/packages/workbox-background-sync/src/index.ts)
- [packages/workbox-broadcast-update/src/index.ts](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/packages/workbox-broadcast-update/src/index.ts)
- [packages/workbox-build/src/index.ts](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/packages/workbox-build/src/index.ts)
- [packages/workbox-cacheable-response/src/index.ts](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/packages/workbox-cacheable-response/src/index.ts)
- [packages/workbox-cli/src/app.ts](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/packages/workbox-cli/src/app.ts)
- [packages/workbox-core/src/index.ts](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/packages/workbox-core/src/index.ts)
- [packages/workbox-expiration/src/index.ts](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/packages/workbox-expiration/src/index.ts)
- [packages/workbox-google-analytics/src/index.ts](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/packages/workbox-google-analytics/src/index.ts)
- [packages/workbox-navigation-preload/src/index.ts](https://github.com/GoogleChrome/workbox/blob/4ea3138a120fd2c87389b54130e25f47e0fd7089/packages/workbox-navigation-preload/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 11 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 60 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 29 file(s) under demos package (observed from repository paths and static analysis). |
| gulp-tasks package | library | Observed | Groups 30 file(s) under gulp-tasks package (observed from repository paths and static analysis). |
| infra package | library | Observed | Groups 34 file(s) under infra package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 201 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 250 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/pull-request.yml` (ci)
- `.github/workflows/scorecards-analysis.yml` (ci)
- `cdn-details.json` (config)
- `demos/src/workbox-background-sync-demo/package.json` (manifest)
- `demos/src/workbox-broadcast-update-demo/package.json` (manifest)
- `demos/src/workbox-cacheable-response/package.json` (manifest)
- `demos/src/workbox-core/package.json` (manifest)
- `demos/src/workbox-expiration/package.json` (manifest)
- `demos/src/workbox-google-analytics/package.json` (manifest)
- `demos/src/workbox-navigation-preload/package.json` (manifest)
- `demos/src/workbox-precaching/package.json` (manifest)
- `demos/src/workbox-range-requests/package.json` (manifest)
- `demos/src/workbox-routing/package.json` (manifest)
- `demos/src/workbox-streams/package.json` (manifest)
- `demos/src/workbox-sw/package.json` (manifest)
- `demos/src/workbox-window/package.json` (manifest)
- `gulp-tasks/utils/node-projects-babel.config.json` (config)
- `infra/templates/reference-docs/jsdoc/lang/en.yaml` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/workbox-background-sync/package.json` (manifest)
- `packages/workbox-background-sync/tsconfig.json` (config)
- `packages/workbox-broadcast-update/package.json` (manifest)
- `packages/workbox-broadcast-update/tsconfig.json` (config)
- `packages/workbox-build/package.json` (manifest)
- `packages/workbox-build/src/cdn-details.json` (config)
- `packages/workbox-build/src/schema/GenerateSWOptions.json` (config)
- `packages/workbox-build/src/schema/GetManifestOptions.json` (config)
- `packages/workbox-build/src/schema/InjectManifestOptions.json` (config)
- `packages/workbox-build/src/schema/WebpackGenerateSWOptions.json` (config)
- `packages/workbox-build/src/schema/WebpackInjectManifestOptions.json` (config)
- `packages/workbox-build/tsconfig.json` (config)
- `packages/workbox-cacheable-response/package.json` (manifest)
- `packages/workbox-cacheable-response/tsconfig.json` (config)
- `packages/workbox-cli/package.json` (manifest)
- `packages/workbox-cli/tsconfig.json` (config)
- `packages/workbox-core/package.json` (manifest)
- `packages/workbox-core/tsconfig.json` (config)
- `packages/workbox-expiration/package.json` (manifest)
- `packages/workbox-expiration/tsconfig.json` (config)
- `packages/workbox-google-analytics/package.json` (manifest)
- `packages/workbox-google-analytics/tsconfig.json` (config)
- `packages/workbox-navigation-preload/package.json` (manifest)
- `packages/workbox-navigation-preload/tsconfig.json` (config)
- `packages/workbox-precaching/package.json` (manifest)
- `packages/workbox-precaching/tsconfig.json` (config)
- `packages/workbox-range-requests/package.json` (manifest)
- `packages/workbox-range-requests/tsconfig.json` (config)
- `packages/workbox-recipes/package.json` (manifest)
- `packages/workbox-recipes/tsconfig.json` (config)
- `packages/workbox-routing/package.json` (manifest)
- `packages/workbox-routing/tsconfig.json` (config)
- `packages/workbox-strategies/package.json` (manifest)
- `packages/workbox-strategies/tsconfig.json` (config)
- `packages/workbox-streams/package.json` (manifest)
- `packages/workbox-streams/tsconfig.json` (config)
- `packages/workbox-sw/package.json` (manifest)
- `packages/workbox-webpack-plugin/package.json` (manifest)
- `packages/workbox-webpack-plugin/tsconfig.json` (config)
- `packages/workbox-window/package.json` (manifest)
- `packages/workbox-window/tsconfig.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 266 analysed file(s)
- `test` — 250 analysed file(s)
- `infra` — 78 analysed file(s)
- `demos` — 66 analysed file(s)
- `gulp-tasks` — 31 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 5 analysed file(s)
- `.husky` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 17 file(s) were skipped during inventory (17 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4ea3138a120fd2c87389b54130e25f47e0fd7089` is the revision these paths and observations refer to.
