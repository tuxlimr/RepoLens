# Project structure: infernojs/inferno

**Analysed commit:** `3ef5668c5d87c969c2dd9afde9fbbfdc3555043e`

**Commit reference:** [3ef5668c5d87c969c2dd9afde9fbbfdc3555043e](https://github.com/infernojs/inferno/commit/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e)

**Tree at this commit:** [infernojs/inferno@3ef5668c5d87](https://github.com/infernojs/inferno/tree/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | infernojs/inferno |
| Description | :fire: An extremely fast, React-like JavaScript library for building modern user interfaces |
| Stars | 16459 |
| Forks | 642 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `3ef5668c5d87c969c2dd9afde9fbbfdc3555043e` |
| Retrieved at | 2026-11-14T19:13:14.728043+00:00 |
| Files in this snapshot | 494 |

## Directory tree

```text
.github/  (8 files)
  workflows/  (3 files)
    ci-template.yml
    codeql-analysis.yml
    sauce-labs.yml
  COMMIT_TEMPLATE.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
browser/  (1 files)
  jsfiddle-integration-babel7v3.js
demo/  (22 files)
  inferno-router-demo/  (22 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (13 files)
      … 13 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .babelrc
    .gitignore
    .parcelrc
    .proxyrc
    README.md
    package.json
    tsconfig.json
docs/  (60 files)
  1kcomponents/  (3 files)
    app.js
    index.html
    style.css
  animation-glitch/  (3 files)
    app.css
    app.js
    index.html
  animations/  (3 files)
    app.css
    app.js
    index.html
  animations-demo/  (3 files)
    app.css
    app.js
    index.html
  animations-demo-inner/  (3 files)
    app.css
    app.js
    index.html
  animations-global-demo/  (4 files)
    app.css
    app.js
    index.html
    inferno-logo.svg
  async-render/  (2 files)
    app.js
    index.html
  autofocus_bug/  (3 files)
    app.css
    app.js
    index.html
  compat/  (2 files)
    app.js
    index.html
  dbmonster/  (4 files)
    ENV.js
    app.js
    index.html
    style.css
  dbmonster-mobx/  (3 files)
    app.js
    index.html
    style.css
  event-test/  (3 files)
    app.js
    index.html
    styles.css
  form/  (2 files)
    app.js
    index.html
  math-elements/  (3 files)
    app.js
    index.html
    style.css
  router_prompt/  (3 files)
    README.md
    app.js
    index.html
  svg/  (2 files)
    app.js
    tiger.html
  uibench/  (3 files)
    app.js
    custom-uibench.js
    index.html
  uibench-inferno-compat/  (2 files)
    app.js
    index.html
  uibench-lifecycle/  (2 files)
    app.js
    index.html
  uibench-normalization/  (2 files)
    app.js
    index.html
  uibench-reactlike/  (2 files)
    app.js
    index.html
  build.js
  index.html
  styles.css
documentation/  (6 files)
  v10-migration.md
  v10-release.md
  v4-migration.md
  v6-migration.md
  v6-release.md
  v9-migration.md
fixtures/  (8 files)
  browser/  (8 files)
    build-tests.js
    jasmine-browser.mjs
    package.json
    run-sauce.mjs
    run-transformers.mjs
    test.index.js
    test.no-compat.index.js
    webpack.config.js
packages/  (350 files)
  inferno/  (84 files)
    __tests__/  (56 files)
      … 56 files under this directory
    src/  (24 files)
      … 24 files under this directory
    README.md
    index.cjs
    index.mjs
    package.json
  inferno-animation/  (28 files)
    __tests__/  (16 files)
      … 16 files under this directory
    src/  (8 files)
      … 8 files under this directory
    index.cjs
    index.css
    package.json
    readme.md
  inferno-clone-vnode/  (5 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    index.cjs
    package.json
  inferno-compat/  (46 files)
    __tests__/  (27 files)
      … 27 files under this directory
    lib/  (12 files)
      … 12 files under this directory
    src/  (4 files)
      … 4 files under this directory
    README.md
    index.cjs
    package.json
  inferno-create-element/  (27 files)
    __tests__/  (23 files)
      … 23 files under this directory
    src/  (1 files)
      … 1 files under this directory
    index.cjs
    package.json
    readme.md
  inferno-extras/  (7 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    index.cjs
    package.json
  inferno-hydrate/  (6 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    index.cjs
    package.json
    readme.md
  inferno-hyperscript/  (5 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    index.cjs
    package.json
  inferno-mobx/  (21 files)
    __tests__/  (11 files)
      … 11 files under this directory
    src/  (7 files)
      … 7 files under this directory
    README.md
    index.cjs
    package.json
  inferno-redux/  (24 files)
    __tests__/  (6 files)
      … 6 files under this directory
    src/  (15 files)
      … 15 files under this directory
    README.md
    index.cjs
    package.json
  inferno-router/  (45 files)
    __tests__/  (24 files)
      … 24 files under this directory
    src/  (18 files)
      … 18 files under this directory
    README.md
    index.cjs
    package.json
  inferno-server/  (29 files)
    __tests__/  (18 files)
      … 18 files under this directory
    src/  (7 files)
      … 7 files under this directory
    README.md
    index.cjs
    index.mjs
    package.json
  inferno-shared/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    index.cjs
    package.json
  inferno-test-utils/  (11 files)
    __tests__/  (5 files)
      … 5 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    index.cjs
    package.json
  inferno-utils/  (3 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    package.json
  inferno-vnode-flags/  (6 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    index.cjs
    package.json
scripts/  (26 files)
  babel/  (2 files)
    assumptions.json
    targets.json
  bundle/  (4 files)
    bundle-size.js
    move-compiled.js
    move-typedefs.js
    read-files-in-dir.js
  ci/  (2 files)
    sauce-workflow.mjs
    sauce-workflow.test.mjs
  fakedom/  (7 files)
    libs/  (2 files)
      … 2 files under this directory
    uibench-reactlike/  (2 files)
      … 2 files under this directory
    build.js
    viewer.html
    viewer.js
  release/  (2 files)
    publish.js
    version.js
  rollup/  (4 files)
    plugins/  (3 files)
      … 3 files under this directory
    build.js
  test/  (5 files)
    globals.js
    jasmine-polyfill.js
    jsdom-environment.js
    request.ts
    requestAnimationFrame.ts
.editorconfig
.gitattributes
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE.md
README.md
eslint.config.js
jest.config-nodom.js
jest.config.js
package.json
pnpm-workspace.yaml
tsconfig.json
```

## Entry points

- [demo/inferno-router-demo/src/App.tsx](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/demo/inferno-router-demo/src/App.tsx)
- [demo/inferno-router-demo/src/index.tsx](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/demo/inferno-router-demo/src/index.tsx)
- [demo/inferno-router-demo/src/server.ts](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/demo/inferno-router-demo/src/server.ts)
- [packages/inferno-animation/src/index.ts](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/packages/inferno-animation/src/index.ts)
- [packages/inferno-clone-vnode/src/index.ts](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/packages/inferno-clone-vnode/src/index.ts)
- [packages/inferno-compat/src/index.ts](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/packages/inferno-compat/src/index.ts)
- [packages/inferno-create-element/src/index.ts](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/packages/inferno-create-element/src/index.ts)
- [packages/inferno-extras/src/index.ts](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/packages/inferno-extras/src/index.ts)
- [packages/inferno-hydrate/src/index.ts](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/packages/inferno-hydrate/src/index.ts)
- [packages/inferno-hyperscript/src/index.ts](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/packages/inferno-hyperscript/src/index.ts)
- [packages/inferno-mobx/src/index.ts](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/packages/inferno-mobx/src/index.ts)
- [packages/inferno-redux/src/index.ts](https://github.com/infernojs/inferno/blob/3ef5668c5d87c969c2dd9afde9fbbfdc3555043e/packages/inferno-redux/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| browser package | library | Observed | Groups 1 file(s) under browser package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 24 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 9 file(s) under demo package (observed from repository paths and static analysis). |
| fixtures package | library | Observed | Groups 7 file(s) under fixtures package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 306 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 18 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci-template.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/sauce-labs.yml` (ci)
- `demo/inferno-router-demo/package.json` (manifest)
- `demo/inferno-router-demo/tsconfig.json` (config)
- `fixtures/browser/package.json` (manifest)
- `package.json` (manifest)
- `packages/inferno-animation/package.json` (manifest)
- `packages/inferno-clone-vnode/package.json` (manifest)
- `packages/inferno-compat/package.json` (manifest)
- `packages/inferno-create-element/package.json` (manifest)
- `packages/inferno-extras/package.json` (manifest)
- `packages/inferno-hydrate/package.json` (manifest)
- `packages/inferno-hyperscript/package.json` (manifest)
- `packages/inferno-mobx/package.json` (manifest)
- `packages/inferno-redux/package.json` (manifest)
- `packages/inferno-router/package.json` (manifest)
- `packages/inferno-server/package.json` (manifest)
- `packages/inferno-shared/package.json` (manifest)
- `packages/inferno-test-utils/package.json` (manifest)
- `packages/inferno-utils/package.json` (manifest)
- `packages/inferno-vnode-flags/package.json` (manifest)
- `packages/inferno/package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `scripts/babel/assumptions.json` (config)
- `scripts/babel/targets.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 350 analysed file(s)
- `docs` — 60 analysed file(s)
- `scripts` — 26 analysed file(s)
- `demo` — 22 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 8 analysed file(s)
- `fixtures` — 8 analysed file(s)
- `documentation` — 6 analysed file(s)
- `browser` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 18 file(s) were skipped during inventory (1 x likely secret file excluded; 17 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3ef5668c5d87c969c2dd9afde9fbbfdc3555043e` is the revision these paths and observations refer to.
