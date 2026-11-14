# Project structure: rematch/rematch

**Analysed commit:** `bde199f08c7709e81458394d2bb9374ad95600a2`

**Commit reference:** [bde199f08c7709e81458394d2bb9374ad95600a2](https://github.com/rematch/rematch/commit/bde199f08c7709e81458394d2bb9374ad95600a2)

**Tree at this commit:** [rematch/rematch@bde199f08c77](https://github.com/rematch/rematch/tree/bde199f08c7709e81458394d2bb9374ad95600a2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | rematch/rematch |
| Description | The Redux Framework |
| Stars | 8390 |
| Forks | 408 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `bde199f08c7709e81458394d2bb9374ad95600a2` |
| Retrieved at | 2026-11-14T19:13:42.091270+00:00 |
| Files in this snapshot | 274 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    documentation.md
    feature_request.md
  workflows/  (5 files)
    ci.yml
    deploy-docs.yml
    lint-pr-title.yml
    next-typescript-ci.yml
    test-size.yml
  FUNDING.yml
  stale.yml
.husky/  (3 files)
  .gitignore
  commit-msg
  pre-commit
blog/  (2 files)
  2021-02-01-welcome.md
  2021-08-30-release-2.1.0.md
docs/  (20 files)
  api-reference/  (5 files)
    index.md
    models.md
    plugins.md
    redux.md
    store.md
  migrating/  (2 files)
    from-redux.md
    from-v1-to-v2.md
  plugins/  (7 files)
    immer.md
    index.md
    loading.md
    persist.md
    select.md
    typed-state.md
    updated.md
  recipes/  (3 files)
    redux-devtools.md
    redux-plugins.md
    testing.md
  installation.md
  introduction.md
  typescript.md
examples/  (117 files)
  all-plugins-react-ts/  (19 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (14 files)
      … 14 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  count-react/  (7 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    package.json
  count-react-ts/  (14 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  gatsby-example/  (22 files)
    src/  (11 files)
      … 11 files under this directory
    .gitignore
    .prettierignore
    .prettierrc
    LICENSE
    README.md
    gatsby-browser.js
    gatsby-config.js
    gatsby-node.js
    gatsby-ssr.js
    package.json
    tsconfig.json
  hooks-react-ts/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (8 files)
      … 8 files under this directory
    README.md
    package.json
    tsconfig.json
  loading-react/  (6 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  multi-react/  (8 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    README.md
    package.json
  nextjs-blog/  (8 files)
    models/  (2 files)
      … 2 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
  persist-react/  (6 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  select-react/  (7 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    README.md
    package.json
  updated-react/  (6 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  README.md
  count.js
packages/  (70 files)
  core/  (28 files)
    src/  (8 files)
      … 8 files under this directory
    test/  (15 files)
      … 15 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.build.json
    tsconfig.json
    tsdx.config.js
  immer/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.build.json
    tsconfig.json
  loading/  (9 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.build.json
    tsconfig.json
  persist/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.build.json
    tsconfig.json
  select/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.build.json
    tsconfig.json
  typed-state/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
  updated/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    package.json
    tsconfig.build.json
    tsconfig.json
website/  (35 files)
  scripts/  (1 files)
    format.mjs
  src/  (10 files)
    components/  (3 files)
      … 3 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (5 files)
      … 5 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
  static/  (16 files)
    icons/  (6 files)
      … 6 files under this directory
    img/  (8 files)
      … 8 files under this directory
    .nojekyll
    CNAME
  .eslintignore
  .gitignore
  README.md
  babel.config.js
  docusaurus.config.js
  package.json
  sidebars.js
  tsconfig.json
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.gitpod.yml
.npmignore
.prettierignore
.prettierrc.json
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
jest.config.js
lerna.json
package.json
testsetup.js
tsconfig.base.json
```

## Entry points

- [packages/core/src/index.ts](https://github.com/rematch/rematch/blob/bde199f08c7709e81458394d2bb9374ad95600a2/packages/core/src/index.ts)
- [packages/immer/src/index.ts](https://github.com/rematch/rematch/blob/bde199f08c7709e81458394d2bb9374ad95600a2/packages/immer/src/index.ts)
- [packages/loading/src/index.ts](https://github.com/rematch/rematch/blob/bde199f08c7709e81458394d2bb9374ad95600a2/packages/loading/src/index.ts)
- [packages/persist/src/index.ts](https://github.com/rematch/rematch/blob/bde199f08c7709e81458394d2bb9374ad95600a2/packages/persist/src/index.ts)
- [packages/select/src/index.ts](https://github.com/rematch/rematch/blob/bde199f08c7709e81458394d2bb9374ad95600a2/packages/select/src/index.ts)
- [packages/typed-state/src/index.ts](https://github.com/rematch/rematch/blob/bde199f08c7709e81458394d2bb9374ad95600a2/packages/typed-state/src/index.ts)
- [packages/updated/src/index.ts](https://github.com/rematch/rematch/blob/bde199f08c7709e81458394d2bb9374ad95600a2/packages/updated/src/index.ts)
- [website/src/pages/index.tsx](https://github.com/rematch/rematch/blob/bde199f08c7709e81458394d2bb9374ad95600a2/website/src/pages/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 26 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 7 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 9 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 25 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 11 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-docs.yml` (ci)
- `.github/workflows/lint-pr-title.yml` (ci)
- `.github/workflows/next-typescript-ci.yml` (ci)
- `.github/workflows/test-size.yml` (ci)
- `.gitpod.yml` (config)
- `.prettierrc.json` (config)
- `examples/all-plugins-react-ts/package.json` (manifest)
- `examples/all-plugins-react-ts/tsconfig.json` (config)
- `examples/count-react-ts/package.json` (manifest)
- `examples/count-react-ts/tsconfig.json` (config)
- `examples/count-react/package.json` (manifest)
- `examples/gatsby-example/package.json` (manifest)
- `examples/gatsby-example/tsconfig.json` (config)
- `examples/hooks-react-ts/package.json` (manifest)
- `examples/hooks-react-ts/tsconfig.json` (config)
- `examples/loading-react/package.json` (manifest)
- `examples/multi-react/package.json` (manifest)
- `examples/nextjs-blog/package.json` (manifest)
- `examples/persist-react/package.json` (manifest)
- `examples/select-react/package.json` (manifest)
- `examples/updated-react/package.json` (manifest)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.build.json` (config)
- `packages/core/tsconfig.json` (config)
- `packages/immer/package.json` (manifest)
- `packages/immer/tsconfig.build.json` (config)
- `packages/immer/tsconfig.json` (config)
- `packages/loading/package.json` (manifest)
- `packages/loading/tsconfig.build.json` (config)
- `packages/loading/tsconfig.json` (config)
- `packages/persist/package.json` (manifest)
- `packages/persist/tsconfig.build.json` (config)
- `packages/persist/tsconfig.json` (config)
- `packages/select/package.json` (manifest)
- `packages/select/tsconfig.build.json` (config)
- `packages/select/tsconfig.json` (config)
- `packages/typed-state/package.json` (manifest)
- `packages/typed-state/tsconfig.build.json` (config)
- `packages/typed-state/tsconfig.json` (config)
- `packages/updated/package.json` (manifest)
- `packages/updated/tsconfig.build.json` (config)
- `packages/updated/tsconfig.json` (config)
- `tsconfig.base.json` (config)
- `website/package.json` (manifest)
- `website/tsconfig.json` (config)

## Top-level layout

- `examples` — 117 analysed file(s)
- `packages` — 70 analysed file(s)
- `website` — 35 analysed file(s)
- `docs` — 20 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 10 analysed file(s)
- `.husky` — 3 analysed file(s)
- `blog` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 11 file(s) were skipped during inventory (9 x likely secret file excluded; 2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `bde199f08c7709e81458394d2bb9374ad95600a2` is the revision these paths and observations refer to.
