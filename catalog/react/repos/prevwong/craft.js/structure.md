# Project structure: prevwong/craft.js

**Analysed commit:** `23f44f3208ebf78d1632ec4aa7094001f513eb41`

**Commit reference:** [23f44f3208ebf78d1632ec4aa7094001f513eb41](https://github.com/prevwong/craft.js/commit/23f44f3208ebf78d1632ec4aa7094001f513eb41)

**Tree at this commit:** [prevwong/craft.js@23f44f3208eb](https://github.com/prevwong/craft.js/tree/23f44f3208ebf78d1632ec4aa7094001f513eb41)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | prevwong/craft.js |
| Description | 🚀 A React Framework for building extensible drag and drop page editors |
| Stars | 8767 |
| Forks | 838 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `23f44f3208ebf78d1632ec4aa7094001f513eb41` |
| Retrieved at | 2026-11-14T19:13:38.585979+00:00 |
| Files in this snapshot | 355 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    improve-documentation.md
  workflows/  (2 files)
    pull-request.yml
    release.yml
  .kodiak.toml
  FUNDING.yml
cypress/  (9 files)
  integration/  (4 files)
    frame.ts
    history.ts
    props.ts
    toolbox.ts
  plugins/  (1 files)
    index.js
  support/  (3 files)
    commands.ts
    dnd.ts
    index.ts
  tsconfig.json
examples/  (85 files)
  basic/  (18 files)
    components/  (8 files)
      … 8 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    src/  (2 files)
      … 2 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    next.config.js
    package.json
  landing/  (67 files)
    components/  (26 files)
      … 26 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    public/  (22 files)
      … 22 files under this directory
    seo/  (3 files)
      … 3 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    types/  (1 files)
      … 1 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    .babelrc
    .gitignore
    README.md
    next-env.d.ts
    next.config.js
    package.json
    postcss.config.js
    tailwind.config.js
    tsconfig.json
experimental/  (40 files)
  slate/  (39 files)
    src/  (32 files)
      … 32 files under this directory
    .npmignore
    LICENSE
    README.md
    nodemon.json
    package.json
    rollup.config.js
    tsconfig.json
  README.md
jest/  (1 files)
  setup.js
packages/  (142 files)
  core/  (76 files)
    src/  (68 files)
      … 68 files under this directory
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    nodemon.json
    package.json
    rollup.config.js
    tsconfig.json
  layers/  (34 files)
    src/  (26 files)
      … 26 files under this directory
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    rollup.config.js
    svg.d.ts
    tsconfig.json
  utils/  (32 files)
    src/  (23 files)
      … 23 files under this directory
    .gitignore
    .npmignore
    CHANGELOG.md
    LICENSE
    README.md
    nodemon.json
    package.json
    rollup.config.js
    tsconfig.json
scripts/  (5 files)
  build.sh
  deploy.sh
  dev.sh
  publish.sh
  yalc.sh
site/  (45 files)
  docs/  (20 files)
    additional/  (1 files)
      … 1 files under this directory
    api/  (10 files)
      … 10 files under this directory
    concepts/  (3 files)
      … 3 files under this directory
    guides/  (2 files)
      … 2 files under this directory
    migrating/  (1 files)
      … 1 files under this directory
    acknowledgements.md
    overview.md
    sponsor.md
  src/  (16 files)
    components/  (4 files)
      … 4 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    theme/  (9 files)
      … 9 files under this directory
  static/  (5 files)
    img/  (5 files)
      … 5 files under this directory
  .gitignore
  docusaurus.config.js
  package.json
  sidebars.js
.all-contributorsrc
.eslintignore
.eslintrc.js
.gitignore
.prettierignore
.prettierrc
.yarnrc.yml
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
cypress.json
jest.config.js
lerna.json
package.json
rollup.config.js
tsconfig.base.json
tsconfig.jest.json
tsconfig.json
```

## Entry points

- [cypress/plugins/index.js](https://github.com/prevwong/craft.js/blob/23f44f3208ebf78d1632ec4aa7094001f513eb41/cypress/plugins/index.js)
- [cypress/support/index.ts](https://github.com/prevwong/craft.js/blob/23f44f3208ebf78d1632ec4aa7094001f513eb41/cypress/support/index.ts)
- [experimental/slate/src/index.ts](https://github.com/prevwong/craft.js/blob/23f44f3208ebf78d1632ec4aa7094001f513eb41/experimental/slate/src/index.ts)
- [packages/core/src/index.tsx](https://github.com/prevwong/craft.js/blob/23f44f3208ebf78d1632ec4aa7094001f513eb41/packages/core/src/index.tsx)
- [packages/layers/src/index.tsx](https://github.com/prevwong/craft.js/blob/23f44f3208ebf78d1632ec4aa7094001f513eb41/packages/layers/src/index.tsx)
- [packages/utils/src/index.ts](https://github.com/prevwong/craft.js/blob/23f44f3208ebf78d1632ec4aa7094001f513eb41/packages/utils/src/index.ts)
- [site/src/components/index.js](https://github.com/prevwong/craft.js/blob/23f44f3208ebf78d1632ec4aa7094001f513eb41/site/src/components/index.js)
- [site/src/pages/index.js](https://github.com/prevwong/craft.js/blob/23f44f3208ebf78d1632ec4aa7094001f513eb41/site/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 4 file(s) under cypress package (observed from repository paths and static analysis). |
| experimental package | library | Observed | Groups 28 file(s) under experimental package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 4 file(s) under external integrations (observed from repository paths and static analysis). |
| jest package | library | Observed | Groups 1 file(s) under jest package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 44 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 57 file(s) under service / domain layer (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 13 file(s) under site package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 21 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/.kodiak.toml` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/pull-request.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.yarnrc.yml` (config)
- `cypress.json` (config)
- `cypress/tsconfig.json` (config)
- `examples/basic/package.json` (manifest)
- `examples/landing/package.json` (manifest)
- `examples/landing/tsconfig.json` (config)
- `experimental/slate/nodemon.json` (config)
- `experimental/slate/package.json` (manifest)
- `experimental/slate/tsconfig.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/core/nodemon.json` (config)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/layers/package.json` (manifest)
- `packages/layers/tsconfig.json` (config)
- `packages/utils/nodemon.json` (config)
- `packages/utils/package.json` (manifest)
- `packages/utils/tsconfig.json` (config)
- `site/package.json` (manifest)
- `tsconfig.base.json` (config)
- `tsconfig.jest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 142 analysed file(s)
- `examples` — 85 analysed file(s)
- `site` — 45 analysed file(s)
- `experimental` — 40 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `cypress` — 9 analysed file(s)
- `.github` — 7 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `jest` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `23f44f3208ebf78d1632ec4aa7094001f513eb41` is the revision these paths and observations refer to.
