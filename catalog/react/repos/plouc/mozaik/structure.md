# Project structure: plouc/mozaik

**Analysed commit:** `5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b`

**Commit reference:** [5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b](https://github.com/plouc/mozaik/commit/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b)

**Tree at this commit:** [plouc/mozaik@5fc9070d9c3a](https://github.com/plouc/mozaik/tree/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | plouc/mozaik |
| Description | Mozaïk is a tool based on nodejs / react / redux / nivo / d3 to easily craft beautiful dashboards |
| Stars | 3596 |
| Forks | 352 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b` |
| Retrieved at | 2026-11-14T19:15:12.350134+00:00 |
| Files in this snapshot | 232 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
demo/  (18 files)
  conf/  (9 files)
    config-ga.yml
    config-github-stats.yml
    config-github.yml
    config-gitlab-labels-charts.yml
    config-gitlab.yml
    config-json.yml
    config-time.yml
    config-travis.yml
    config.yml
  public/  (2 files)
    index.html
    manifest.json
  src/  (3 files)
    index.js
    register_extensions.js
    register_themes.js
  README.md
  package.json
  register_apis.js
  server.js
packages/  (135 files)
  babel-preset/  (2 files)
    index.js
    package.json
  server/  (24 files)
    src/  (6 files)
      … 6 files under this directory
    test/  (11 files)
      … 11 files under this directory
    .gitignore
    .npmignore
    .prettierrc
    README.md
    package.json
    tsconfig.json
    tslint.json
  themes/  (31 files)
    src/  (25 files)
      … 25 files under this directory
    .babelrc
    .gitignore
    .npmignore
    LICENSE.md
    README.md
    package.json
  ui/  (78 files)
    .storybook/  (2 files)
      … 2 files under this directory
    src/  (58 files)
      … 58 files under this directory
    stories/  (11 files)
      … 11 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .babelrc
    .gitignore
    .npmignore
    README.md
    package.json
website/  (64 files)
  src/  (58 files)
    assets/  (2 files)
      … 2 files under this directory
    components/  (17 files)
      … 17 files under this directory
    data/  (3 files)
      … 3 files under this directory
    layouts/  (3 files)
      … 3 files under this directory
    pages/  (26 files)
      … 26 files under this directory
    styles/  (5 files)
      … 5 files under this directory
    templates/  (2 files)
      … 2 files under this directory
  static/  (1 files)
    CNAME
  README.md
  gatsby-browser.js
  gatsby-config.js
  gatsby-node.js
  package.json
.editorconfig
.eslintrc.yml
.gitignore
.npmignore
.prettierignore
.prettierrc
.travis.yml
CHANGELOG.md
LICENSE.md
Makefile
README.md
browserlist
lerna.json
package.json
```

## Entry points

- [demo/server.js](https://github.com/plouc/mozaik/blob/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b/demo/server.js)
- [demo/src/index.js](https://github.com/plouc/mozaik/blob/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b/demo/src/index.js)
- [packages/babel-preset/index.js](https://github.com/plouc/mozaik/blob/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b/packages/babel-preset/index.js)
- [packages/server/src/index.ts](https://github.com/plouc/mozaik/blob/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b/packages/server/src/index.ts)
- [packages/themes/src/index.js](https://github.com/plouc/mozaik/blob/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b/packages/themes/src/index.js)
- [packages/ui/src/App.js](https://github.com/plouc/mozaik/blob/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b/packages/ui/src/App.js)
- [packages/ui/src/index.js](https://github.com/plouc/mozaik/blob/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b/packages/ui/src/index.js)
- [website/src/layouts/index.js](https://github.com/plouc/mozaik/blob/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b/website/src/layouts/index.js)
- [website/src/pages/index.js](https://github.com/plouc/mozaik/blob/5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b/website/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 25 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 5 file(s) under demo package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 101 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 13 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 32 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.yml` (config)
- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `demo/conf/config-ga.yml` (config)
- `demo/conf/config-github-stats.yml` (config)
- `demo/conf/config-github.yml` (config)
- `demo/conf/config-gitlab-labels-charts.yml` (config)
- `demo/conf/config-gitlab.yml` (config)
- `demo/conf/config-json.yml` (config)
- `demo/conf/config-time.yml` (config)
- `demo/conf/config-travis.yml` (config)
- `demo/conf/config.yml` (config)
- `demo/package.json` (manifest)
- `demo/public/manifest.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/babel-preset/package.json` (manifest)
- `packages/server/package.json` (manifest)
- `packages/server/tsconfig.json` (config)
- `packages/server/tslint.json` (config)
- `packages/themes/package.json` (manifest)
- `packages/ui/package.json` (manifest)
- `website/package.json` (manifest)
- `website/src/data/extensions.yml` (config)
- `website/src/data/references.yml` (config)
- `website/src/data/useCases.yml` (config)

## Top-level layout

- `packages` — 135 analysed file(s)
- `website` — 64 analysed file(s)
- `demo` — 18 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (4 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5fc9070d9c3aeb1c53ef1719daa3a7239c23a31b` is the revision these paths and observations refer to.
