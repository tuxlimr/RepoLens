# Project structure: mobxjs/mobx

**Analysed commit:** `bf94b8e866c58995f78189c5412cf06042012720`

**Commit reference:** [bf94b8e866c58995f78189c5412cf06042012720](https://github.com/mobxjs/mobx/commit/bf94b8e866c58995f78189c5412cf06042012720)

**Tree at this commit:** [mobxjs/mobx@bf94b8e866c5](https://github.com/mobxjs/mobx/tree/bf94b8e866c58995f78189c5412cf06042012720)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mobxjs/mobx |
| Description | Simple, scalable state management. |
| Stars | 28211 |
| Forks | 1811 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `bf94b8e866c58995f78189c5412cf06042012720` |
| Retrieved at | 2026-11-14T19:13:04.458929+00:00 |
| Files in this snapshot | 366 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (11 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.md
    config.yml
    documentation.md
  workflows/  (3 files)
    build_and_test.yml
    coveralls.yml
    release.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  lock.yml
  stale.yml
.vscode/  (2 files)
  launch.json
  settings.json
docs/  (73 files)
  assets/  (19 files)
    getting-started-assets/  (13 files)
      … 13 files under this directory
    action-state-view.excalidraw
    canva.svg
    flow.excalidraw..excalidraw..excalidraw
    mobservable.svg
    overview.svg
    overview_bw.svg
  best/  (4 files)
    debugging-mobx.md
    decorators.md
    store.md
    what-does-mobx-react-to.md
  faq/  (1 files)
    migrate-to-6.md
  intro/  (3 files)
    concepts.md
    how-to-read.md
    installation.md
  react/  (2 files)
    react-integration.md
    react-performance.md
  refguide/  (15 files)
    action.md
    api.md
    autorun.md
    computed-with-args.md
    computed.md
    configure.md
    extending.md
    mobx-utils.md
    modifiers.md
    object-api.md
    object.md
    observable.md
    observe.md
    on-become-observed.md
    set.md
  styles/  (1 files)
    website.css
  LINKS.md
  README.md
  about-this-documentation.md
  actions.md
  analyzing-reactivity.md
  api.md
  backers-sponsors.md
  collection-utilities.md
  computeds-with-args.md
  computeds.md
  configuration.md
  custom-observables.md
  defining-data-stores.md
  enabling-decorators.md
  installation.md
  intercept-and-observe.md
  lazy-observables.md
  migrating-from-4-or-5.md
  migrating-from-6-to-7.md
  mobx-utils.md
  observable-state.md
  react-compiler.md
  react-integration.md
  react-optimizations.md
  … 4 more files
packages/  (245 files)
  eslint-plugin-mobx/  (24 files)
    __tests__/  (5 files)
      … 5 files under this directory
    preview/  (5 files)
      … 5 files under this directory
    src/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    jest.config-eslint-7.js
    jest.config-eslint-9.js
    jest.setup.js
    package.json
    tsconfig.json
  mobx/  (115 files)
    __tests__/  (49 files)
      … 49 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    src/  (56 files)
      … 56 files under this directory
    .gitignore
    CHANGELOG.md
    jest.config.js
    jest.projects.js
    jest.setup.ts
    package.json
    rollup.config.mjs
    tsconfig.json
  mobx-react/  (37 files)
    __mocks__/  (1 files)
      … 1 files under this directory
    __tests__/  (20 files)
      … 20 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .browserlistrc
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    jest.setup.ts
    package.json
    rollup.config.mjs
    tsconfig.json
    tsconfig.test.json
  mobx-react-lite/  (37 files)
    __tests__/  (17 files)
      … 17 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .eslintignore
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    jest.setup.ts
    package.json
    rollup.config.mjs
    tsconfig.json
    tsconfig.test.json
  mobx-react-plugin/  (20 files)
    __tests__/  (5 files)
      … 5 files under this directory
    src/  (8 files)
      … 8 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
    tsconfig.test.json
  mobx-undecorate/  (12 files)
    __tests__/  (4 files)
      … 4 files under this directory
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    cli.js
    jest.config.js
    package.json
    tsconfig.json
scripts/  (3 files)
  size/  (2 files)
    index.js
    minimal-example.js
  create-rollup-config.mjs
website/  (12 files)
  core/  (1 files)
    Footer.js
  i18n/  (1 files)
    en.json
  scripts/  (1 files)
    generate-error-docs.js
  static/  (6 files)
    css/  (1 files)
      … 1 files under this directory
    img/  (2 files)
      … 2 files under this directory
    js/  (1 files)
      … 1 files under this directory
    getting-started.html
    index.html
  package.json
  sidebars.json
  siteConfig.js
.editorconfig
.eslintrc.js
.gitignore
.prettierignore
.prettierrc
.watchmanconfig
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
jest.base.config.js
jest.config.js
jest.setup.base.ts
package.json
sponsors.md
tsconfig.json
tsconfig.test.json
```

## Entry points

- [packages/mobx-undecorate/cli.js](https://github.com/mobxjs/mobx/blob/bf94b8e866c58995f78189c5412cf06042012720/packages/mobx-undecorate/cli.js)
- [packages/eslint-plugin-mobx/src/index.ts](https://github.com/mobxjs/mobx/blob/bf94b8e866c58995f78189c5412cf06042012720/packages/eslint-plugin-mobx/src/index.ts)
- [packages/mobx-react-lite/src/index.ts](https://github.com/mobxjs/mobx/blob/bf94b8e866c58995f78189c5412cf06042012720/packages/mobx-react-lite/src/index.ts)
- [packages/mobx-react/src/index.ts](https://github.com/mobxjs/mobx/blob/bf94b8e866c58995f78189c5412cf06042012720/packages/mobx-react/src/index.ts)
- [scripts/size/index.js](https://github.com/mobxjs/mobx/blob/bf94b8e866c58995f78189c5412cf06042012720/scripts/size/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 22 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 160 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 9 file(s) under service / domain layer (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 3 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/lock.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/build_and_test.yml` (ci)
- `.github/workflows/coveralls.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `packages/eslint-plugin-mobx/package.json` (manifest)
- `packages/eslint-plugin-mobx/tsconfig.json` (config)
- `packages/mobx-react-lite/__tests__/.eslintrc.yaml` (config)
- `packages/mobx-react-lite/__tests__/tsconfig.json` (config)
- `packages/mobx-react-lite/package.json` (manifest)
- `packages/mobx-react-lite/tsconfig.json` (config)
- `packages/mobx-react-lite/tsconfig.test.json` (config)
- `packages/mobx-react-plugin/package.json` (manifest)
- `packages/mobx-react-plugin/tsconfig.json` (config)
- `packages/mobx-react-plugin/tsconfig.test.json` (config)
- `packages/mobx-react/__tests__/.eslintrc.yaml` (config)
- `packages/mobx-react/__tests__/tsconfig.json` (config)
- `packages/mobx-react/package.json` (manifest)
- `packages/mobx-react/tsconfig.json` (config)
- `packages/mobx-react/tsconfig.test.json` (config)
- `packages/mobx-undecorate/__tests__/tsconfig.json` (config)
- `packages/mobx-undecorate/package.json` (manifest)
- `packages/mobx-undecorate/tsconfig.json` (config)
- `packages/mobx/__tests__/perf/tsconfig.decorator.json` (config)
- `packages/mobx/__tests__/tsconfig.json` (config)
- `packages/mobx/package.json` (manifest)
- `packages/mobx/tsconfig.json` (config)
- `tsconfig.json` (config)
- `tsconfig.test.json` (config)
- `website/i18n/en.json` (config)
- `website/package.json` (manifest)
- `website/sidebars.json` (config)

## Top-level layout

- `packages` — 245 analysed file(s)
- `docs` — 73 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `website` — 12 analysed file(s)
- `.github` — 11 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (2 x lockfile excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bf94b8e866c58995f78189c5412cf06042012720` is the revision these paths and observations refer to.
