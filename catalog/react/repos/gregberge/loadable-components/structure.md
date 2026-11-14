# Project structure: gregberge/loadable-components

**Analysed commit:** `18544decdd0e9ecb3e85772708e1f2726430fdeb`

**Commit reference:** [18544decdd0e9ecb3e85772708e1f2726430fdeb](https://github.com/gregberge/loadable-components/commit/18544decdd0e9ecb3e85772708e1f2726430fdeb)

**Tree at this commit:** [gregberge/loadable-components@18544decdd0e](https://github.com/gregberge/loadable-components/tree/18544decdd0e9ecb3e85772708e1f2726430fdeb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gregberge/loadable-components |
| Description | The recommended Code Splitting library for React ✂️✨ |
| Stars | 7795 |
| Forks | 386 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `18544decdd0e9ecb3e85772708e1f2726430fdeb` |
| Retrieved at | 2026-11-14T19:13:45.558542+00:00 |
| Files in this snapshot | 251 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (4 files)
    bug.md
    feature.md
    question.md
    regression.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  SUPPORT.md
  opencollective.yml
  stale.yml
examples/  (127 files)
  client-side/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    .eslintrc.json
    README.md
    babel.config.js
    package.json
    webpack.config.js
  razzle/  (20 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (14 files)
      … 14 files under this directory
    .eslintrc.json
    .gitignore
    README.md
    package.json
    razzle.config.js
  server-side-rendering/  (22 files)
    src/  (15 files)
      … 15 files under this directory
    .eslintrc.json
    .gitignore
    README.md
    babel.config.js
    nodemon.json
    package.json
    webpack.config.babel.js
  server-side-rendering-async-node/  (22 files)
    src/  (15 files)
      … 15 files under this directory
    .eslintrc.json
    .gitignore
    README.md
    babel.config.js
    nodemon.json
    package.json
    webpack.config.babel.js
  suspense/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .eslintrc.json
    README.md
    babel.config.js
    package.json
    webpack.config.js
  typescript/  (14 files)
    src/  (6 files)
      … 6 files under this directory
    .eslintrc.json
    .gitignore
    README.md
    babel.config.js
    nodemon.json
    package.json
    tsconfig.json
    webpack.config.babel.js
  webpack/  (33 files)
    webpack4/  (16 files)
      … 16 files under this directory
    webpack5/  (16 files)
      … 16 files under this directory
    README.md
packages/  (64 files)
  babel-plugin/  (14 files)
    src/  (11 files)
      … 11 files under this directory
    CHANGELOG.md
    README.md
    package.json
  codemod/  (14 files)
    bin/  (2 files)
      … 2 files under this directory
    transforms/  (8 files)
      … 8 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
  component/  (17 files)
    src/  (11 files)
      … 11 files under this directory
    .npmignore
    .size-snapshot.json
    CHANGELOG.md
    README.md
    package.json
    rollup.config.js
  server/  (14 files)
    __fixtures__/  (1 files)
      … 1 files under this directory
    src/  (7 files)
      … 7 files under this directory
    .npmignore
    .size-snapshot.json
    CHANGELOG.md
    README.md
    package.json
    rollup.config.js
  webpack-plugin/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
scripts/  (3 files)
  copy-stats-fixture.js
  git-release.sh
  prepare.sh
website/  (29 files)
  src/  (21 files)
    pages/  (21 files)
      … 21 files under this directory
  .eslintignore
  .eslintrc.json
  .gitignore
  README.md
  _redirects
  gatsby-config.js
  gatsby-node.js
  package.json
.eslintignore
.eslintrc.json
.gitignore
.npmignore
.nvmrc
.prettierignore
.prettierrc
.travis.yml
BACKERS.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
babel.config.js
lerna.json
netlify.toml
package.json
```

## Entry points

- [packages/codemod/bin/main.js](https://github.com/gregberge/loadable-components/blob/18544decdd0e9ecb3e85772708e1f2726430fdeb/packages/codemod/bin/main.js)
- [packages/babel-plugin/src/index.js](https://github.com/gregberge/loadable-components/blob/18544decdd0e9ecb3e85772708e1f2726430fdeb/packages/babel-plugin/src/index.js)
- [packages/component/src/index.js](https://github.com/gregberge/loadable-components/blob/18544decdd0e9ecb3e85772708e1f2726430fdeb/packages/component/src/index.js)
- [packages/server/src/index.js](https://github.com/gregberge/loadable-components/blob/18544decdd0e9ecb3e85772708e1f2726430fdeb/packages/server/src/index.js)
- [packages/webpack-plugin/src/index.js](https://github.com/gregberge/loadable-components/blob/18544decdd0e9ecb3e85772708e1f2726430fdeb/packages/webpack-plugin/src/index.js)
- [website/src/pages/index.js](https://github.com/gregberge/loadable-components/blob/18544decdd0e9ecb3e85772708e1f2726430fdeb/website/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 41 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 3 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/opencollective.yml` (config)
- `.github/stale.yml` (config)
- `.travis.yml` (ci)
- `examples/client-side/.eslintrc.json` (config)
- `examples/client-side/package.json` (manifest)
- `examples/razzle/.eslintrc.json` (config)
- `examples/razzle/package.json` (manifest)
- `examples/server-side-rendering-async-node/.eslintrc.json` (config)
- `examples/server-side-rendering-async-node/nodemon.json` (config)
- `examples/server-side-rendering-async-node/package.json` (manifest)
- `examples/server-side-rendering/.eslintrc.json` (config)
- `examples/server-side-rendering/nodemon.json` (config)
- `examples/server-side-rendering/package.json` (manifest)
- `examples/suspense/.eslintrc.json` (config)
- `examples/suspense/package.json` (manifest)
- `examples/typescript/.eslintrc.json` (config)
- `examples/typescript/nodemon.json` (config)
- `examples/typescript/package.json` (manifest)
- `examples/typescript/tsconfig.json` (config)
- `examples/webpack/webpack4/.eslintrc.json` (config)
- `examples/webpack/webpack4/nodemon.json` (config)
- `examples/webpack/webpack4/package.json` (manifest)
- `examples/webpack/webpack5/.eslintrc.json` (config)
- `examples/webpack/webpack5/nodemon.json` (config)
- `examples/webpack/webpack5/package.json` (manifest)
- `lerna.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `packages/babel-plugin/package.json` (manifest)
- `packages/codemod/package.json` (manifest)
- `packages/component/.size-snapshot.json` (config)
- `packages/component/package.json` (manifest)
- `packages/server/.size-snapshot.json` (config)
- `packages/server/__fixtures__/stats.json` (config)
- `packages/server/package.json` (manifest)
- `packages/webpack-plugin/package.json` (manifest)
- `website/.eslintrc.json` (config)
- `website/package.json` (manifest)

## Top-level layout

- `examples` — 127 analysed file(s)
- `packages` — 64 analysed file(s)
- `website` — 29 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 10 analysed file(s)
- `scripts` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `18544decdd0e9ecb3e85772708e1f2726430fdeb` is the revision these paths and observations refer to.
