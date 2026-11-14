# Project structure: oliviertassinari/react-swipeable-views

**Analysed commit:** `c637ad7d222fce9df3b51d94453209049d442de3`

**Commit reference:** [c637ad7d222fce9df3b51d94453209049d442de3](https://github.com/oliviertassinari/react-swipeable-views/commit/c637ad7d222fce9df3b51d94453209049d442de3)

**Tree at this commit:** [oliviertassinari/react-swipeable-views@c637ad7d222f](https://github.com/oliviertassinari/react-swipeable-views/tree/c637ad7d222fce9df3b51d94453209049d442de3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | oliviertassinari/react-swipeable-views |
| Description | A React component for swipeable views. :snowflake: |
| Stars | 4466 |
| Forks | 477 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c637ad7d222fce9df3b51d94453209049d442de3` |
| Retrieved at | 2026-11-14T19:14:44.553801+00:00 |
| Files in this snapshot | 164 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
docs/  (41 files)
  src/  (40 files)
    modules/  (19 files)
      … 19 files under this directory
    pages/  (21 files)
      … 21 files under this directory
  webpackBaseConfig.js
examples/  (8 files)
  create-react-app/  (7 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    package.json
  .gitignore
native/  (51 files)
  packages/  (10 files)
    react-swipeable-views-native/  (10 files)
      … 10 files under this directory
  src/  (29 files)
    demo/  (21 files)
      … 21 files under this directory
    pagination/  (3 files)
      … 3 files under this directory
    App.tsx
    Footer.tsx
    Home.tsx
    Main.tsx
    styles.ts
  .buckconfig
  .editorconfig
  .gitattributes
  .gitignore
  .watchmanconfig
  App.js
  app.json
  index.js
  jest.config.js
  package.json
  tsconfig.json
  tslint.json
packages/  (26 files)
  react-swipeable-views/  (5 files)
    src/  (3 files)
      … 3 files under this directory
    .npmignore
    package.json
  react-swipeable-views-core/  (12 files)
    src/  (10 files)
      … 10 files under this directory
    .npmignore
    package.json
  react-swipeable-views-utils/  (9 files)
    src/  (7 files)
      … 7 files under this directory
    .npmignore
    package.json
pages/  (9 files)
  api/  (1 files)
    api.js
  demos/  (1 files)
    demos.js
  getting-started/  (4 files)
    example-projects.js
    installation.js
    supported-platforms.js
    usage.js
  .eslintrc.js
  _document.js
  index.js
scripts/  (2 files)
  babel-plugin-preval.js
  get-replacement.js
static/  (1 files)
  manifest.json
test/  (4 files)
  consoleError.js
  dom.js
  mocha.opts
  setup.js
.buckconfig
.codecov.yml
.eslintignore
.eslintrc.js
.firebaserc
.gitattributes
.gitignore
.size-limit
.watchmanconfig
CHANGELOG.md
LICENSE
README.md
app.json
babel.config.js
firebase.json
lerna.json
next.config.js
package.json
prettier.config.js
```

## Entry points

- [native/App.js](https://github.com/oliviertassinari/react-swipeable-views/blob/c637ad7d222fce9df3b51d94453209049d442de3/native/App.js)
- [native/index.js](https://github.com/oliviertassinari/react-swipeable-views/blob/c637ad7d222fce9df3b51d94453209049d442de3/native/index.js)
- [native/src/App.tsx](https://github.com/oliviertassinari/react-swipeable-views/blob/c637ad7d222fce9df3b51d94453209049d442de3/native/src/App.tsx)
- [native/src/Main.tsx](https://github.com/oliviertassinari/react-swipeable-views/blob/c637ad7d222fce9df3b51d94453209049d442de3/native/src/Main.tsx)
- [packages/react-swipeable-views-core/src/index.js](https://github.com/oliviertassinari/react-swipeable-views/blob/c637ad7d222fce9df3b51d94453209049d442de3/packages/react-swipeable-views-core/src/index.js)
- [packages/react-swipeable-views-utils/src/index.js](https://github.com/oliviertassinari/react-swipeable-views/blob/c637ad7d222fce9df3b51d94453209049d442de3/packages/react-swipeable-views-utils/src/index.js)
- [packages/react-swipeable-views/src/index.js](https://github.com/oliviertassinari/react-swipeable-views/blob/c637ad7d222fce9df3b51d94453209049d442de3/packages/react-swipeable-views/src/index.js)
- [pages/index.js](https://github.com/oliviertassinari/react-swipeable-views/blob/c637ad7d222fce9df3b51d94453209049d442de3/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| native package | library | Observed | Groups 28 file(s) under native package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 20 file(s) under packages package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 8 file(s) under pages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.codecov.yml` (config)
- `app.json` (config)
- `examples/create-react-app/package.json` (manifest)
- `examples/create-react-app/public/manifest.json` (config)
- `firebase.json` (config)
- `lerna.json` (config)
- `native/.editorconfig` (config)
- `native/app.json` (config)
- `native/package.json` (manifest)
- `native/packages/react-swipeable-views-native/package.json` (manifest)
- `native/packages/react-swipeable-views-native/tsconfig.json` (config)
- `native/packages/react-swipeable-views-native/tsconfig.prod.json` (config)
- `native/packages/react-swipeable-views-native/tslint.json` (config)
- `native/tsconfig.json` (config)
- `native/tslint.json` (config)
- `package.json` (manifest)
- `packages/react-swipeable-views-core/package.json` (manifest)
- `packages/react-swipeable-views-utils/package.json` (manifest)
- `packages/react-swipeable-views/package.json` (manifest)
- `static/manifest.json` (config)

## Top-level layout

- `native` — 51 analysed file(s)
- `docs` — 41 analysed file(s)
- `packages` — 26 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `pages` — 9 analysed file(s)
- `examples` — 8 analysed file(s)
- `test` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `static` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c637ad7d222fce9df3b51d94453209049d442de3` is the revision these paths and observations refer to.
