# Project structure: vuejs/vue-router

**Analysed commit:** `680ccc68c506cca9be6207745043245d61fa715a`

**Commit reference:** [680ccc68c506cca9be6207745043245d61fa715a](https://github.com/vuejs/vue-router/commit/680ccc68c506cca9be6207745043245d61fa715a)

**Tree at this commit:** [vuejs/vue-router@680ccc68c506](https://github.com/vuejs/vue-router/tree/680ccc68c506cca9be6207745043245d61fa715a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vuejs/vue-router |
| Description | 🚦 The official router for Vue 2 |
| Stars | 18852 |
| Forks | 4950 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | dev |
| Analysed commit | `680ccc68c506cca9be6207745043245d61fa715a` |
| Retrieved at | 2026-11-14T19:11:19.400500+00:00 |
| Files in this snapshot | 460 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (4 files)
  workflows/  (1 files)
    release-tag.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  funding.yml
docs/  (134 files)
  .vuepress/  (21 files)
    components/  (3 files)
      … 3 files under this directory
    public/  (11 files)
      … 11 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    theme/  (5 files)
      … 5 files under this directory
    config.js
  api/  (1 files)
    README.md
  fr/  (18 files)
    api/  (1 files)
      … 1 files under this directory
    guide/  (15 files)
      … 15 files under this directory
    README.md
    installation.md
  guide/  (16 files)
    advanced/  (7 files)
      … 7 files under this directory
    essentials/  (8 files)
      … 8 files under this directory
    README.md
  ja/  (19 files)
    api/  (1 files)
      … 1 files under this directory
    guide/  (16 files)
      … 16 files under this directory
    README.md
    installation.md
  kr/  (19 files)
    api/  (1 files)
      … 1 files under this directory
    guide/  (16 files)
      … 16 files under this directory
    README.md
    installation.md
  ru/  (19 files)
    api/  (1 files)
      … 1 files under this directory
    guide/  (16 files)
      … 16 files under this directory
    README.md
    installation.md
  zh/  (19 files)
    api/  (1 files)
      … 1 files under this directory
    guide/  (16 files)
      … 16 files under this directory
    README.md
    installation.md
  README.md
  installation.md
docs-gitbook/  (148 files)
  assets/  (2 files)
    CNAME
    circle.yml
  de/  (22 files)
    advanced/  (6 files)
      … 6 files under this directory
    api/  (6 files)
      … 6 files under this directory
    essentials/  (8 files)
      … 8 files under this directory
    SUMMARY.md
    installation.md
  es/  (24 files)
    advanced/  (6 files)
      … 6 files under this directory
    api/  (6 files)
      … 6 files under this directory
    essentials/  (9 files)
      … 9 files under this directory
    README.md
    SUMMARY.md
    installation.md
  fr/  (24 files)
    advanced/  (6 files)
      … 6 files under this directory
    api/  (6 files)
      … 6 files under this directory
    essentials/  (9 files)
      … 9 files under this directory
    README.md
    SUMMARY.md
    installation.md
  ja/  (24 files)
    advanced/  (6 files)
      … 6 files under this directory
    api/  (6 files)
      … 6 files under this directory
    essentials/  (9 files)
      … 9 files under this directory
    README.md
    SUMMARY.md
    installation.md
  kr/  (24 files)
    advanced/  (6 files)
      … 6 files under this directory
    api/  (6 files)
      … 6 files under this directory
    essentials/  (9 files)
      … 9 files under this directory
    README.md
    SUMMARY.md
    installation.md
  old/  (2 files)
    README.md
    SUMMARY.md
  ru/  (24 files)
    advanced/  (6 files)
      … 6 files under this directory
    api/  (6 files)
      … 6 files under this directory
    essentials/  (9 files)
      … 9 files under this directory
    README.md
    SUMMARY.md
    installation.md
  LANGS.md
  book.json
examples/  (67 files)
  active-links/  (2 files)
    app.js
    index.html
  auth-flow/  (7 files)
    components/  (4 files)
      … 4 files under this directory
    app.js
    auth.js
    index.html
  basic/  (2 files)
    app.js
    index.html
  composables/  (2 files)
    app.js
    index.html
  data-fetching/  (4 files)
    Post.vue
    api.js
    app.js
    index.html
  discrete-components/  (2 files)
    app.js
    index.html
  hash-mode/  (2 files)
    app.js
    index.html
  hash-scroll-behavior/  (2 files)
    app.js
    index.html
  keepalive-view/  (2 files)
    app.js
    index.html
  lazy-loading/  (5 files)
    Bar.vue
    Baz.vue
    Foo.vue
    app.js
    index.html
  lazy-loading-before-mount/  (2 files)
    app.js
    index.html
  multi-app/  (2 files)
    app.js
    index.html
  named-routes/  (2 files)
    app.js
    index.html
  named-views/  (2 files)
    app.js
    index.html
  navigation-guards/  (2 files)
    app.js
    index.html
  nested-router/  (2 files)
    app.js
    index.html
  nested-routes/  (2 files)
    app.js
    index.html
  redirect/  (2 files)
    app.js
    index.html
  restart-app/  (2 files)
    app.js
    index.html
  route-alias/  (2 files)
    app.js
    index.html
  route-matching/  (2 files)
    app.js
    index.html
  route-params/  (2 files)
    app.js
    index.html
  route-props/  (3 files)
    Hello.vue
    app.js
    index.html
  router-errors/  (2 files)
    app.js
    index.html
  scroll-behavior/  (2 files)
    app.js
    index.html
  transitions/  (2 files)
    app.js
    index.html
  global.css
  index.html
  server.js
  webpack.config.js
flow/  (1 files)
  declarations.js
scripts/  (2 files)
  release.sh
  verifyCommitMsg.js
src/  (32 files)
  components/  (2 files)
    link.js
    view.js
  composables/  (5 files)
    globals.js
    guards.js
    index.js
    useLink.js
    utils.js
  entries/  (2 files)
    cjs.js
    esm.js
  history/  (4 files)
    abstract.js
    base.js
    hash.js
    html5.js
  util/  (14 files)
    async.js
    dom.js
    errors.js
    location.js
    misc.js
    params.js
    path.js
    push-state.js
    query.js
    resolve-components.js
    route.js
    scroll.js
    state-key.js
    warn.js
  create-matcher.js
  create-route-map.js
  index.js
  install.js
  router.js
test/  (48 files)
  e2e/  (31 files)
    specs/  (26 files)
      … 26 files under this directory
    .eslintrc
    browserstack-send-status.js
    nightwatch.browserstack.js
    nightwatch.config.js
    runner.js
  unit/  (16 files)
    specs/  (14 files)
      … 14 files under this directory
    .eslintrc
    jasmine.json
  .eslintrc
types/  (7 files)
  test/  (3 files)
    index.ts
    meta.ts
    tsconfig.json
  composables.d.ts
  index.d.ts
  router.d.ts
  vue.d.ts
vetur/  (2 files)
  attributes.json
  tags.json
.babelrc
.eslintignore
.eslintrc
.flowconfig
.gitignore
.prettierrc
CHANGELOG.md
LICENSE
README.md
composables.d.ts
composables.js
composables.mjs
netlify.toml
package.json
```

## Entry points

- [src/composables/index.js](https://github.com/vuejs/vue-router/blob/680ccc68c506cca9be6207745043245d61fa715a/src/composables/index.js)
- [src/index.js](https://github.com/vuejs/vue-router/blob/680ccc68c506cca9be6207745043245d61fa715a/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 2 file(s) under components package (observed from repository paths and static analysis). |
| composables package | library | Observed | Groups 5 file(s) under composables package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| create-matcher.js package | library | Observed | Groups 1 file(s) under create-matcher.js package (observed from repository paths and static analysis). |
| create-route-map.js package | library | Observed | Groups 1 file(s) under create-route-map.js package (observed from repository paths and static analysis). |
| entries package | library | Observed | Groups 2 file(s) under entries package (observed from repository paths and static analysis). |
| flow package | library | Observed | Groups 1 file(s) under flow package (observed from repository paths and static analysis). |
| history package | library | Observed | Groups 4 file(s) under history package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| install.js package | library | Observed | Groups 1 file(s) under install.js package (observed from repository paths and static analysis). |
| router.js package | library | Observed | Groups 1 file(s) under router.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 51 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 4 file(s) under types package (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 14 file(s) under util package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.github/funding.yml` (config)
- `.github/workflows/release-tag.yml` (ci)
- `docs-gitbook/assets/circle.yml` (config)
- `docs-gitbook/book.json` (config)
- `docs/.vuepress/components/sponsors.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `vetur/attributes.json` (config)
- `vetur/tags.json` (config)

## Top-level layout

- `docs-gitbook` — 148 analysed file(s)
- `docs` — 134 analysed file(s)
- `examples` — 67 analysed file(s)
- `test` — 48 analysed file(s)
- `src` — 32 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `types` — 7 analysed file(s)
- `.github` — 4 analysed file(s)
- `scripts` — 2 analysed file(s)
- `vetur` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `flow` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 8 file(s) were skipped during inventory (8 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `680ccc68c506cca9be6207745043245d61fa715a` is the revision these paths and observations refer to.
