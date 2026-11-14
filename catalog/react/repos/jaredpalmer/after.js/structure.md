# Project structure: jaredpalmer/after.js

**Analysed commit:** `dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7`

**Commit reference:** [dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7](https://github.com/jaredpalmer/after.js/commit/dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7)

**Tree at this commit:** [jaredpalmer/after.js@dbc362fa9b72](https://github.com/jaredpalmer/after.js/tree/dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jaredpalmer/after.js |
| Description | Next.js-like framework for server-rendered React apps built with React Router |
| Stars | 4088 |
| Forks | 193 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7` |
| Retrieved at | 2026-11-14T19:14:53.879264+00:00 |
| Files in this snapshot | 241 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (11 files)
  ISSUE_TEMPLATE/  (4 files)
    Bug_report.md
    Documentation.md
    Feature_request.md
    Question.md
  workflows/  (3 files)
    label.yml
    main.yml
    size.yml
  CONTRIBUTING.md
  FUNDING.yml
  labeler.yml
  stale.yml
.husky/  (1 files)
  pre-commit
examples/  (131 files)
  basic/  (15 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  layout-component/  (17 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (11 files)
      … 11 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-context-api/  (18 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (12 files)
      … 12 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-material-ui/  (15 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-material-ui-rtl/  (16 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (10 files)
      … 10 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-redux/  (19 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (13 files)
      … 13 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-scss/  (15 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
  with-static-export/  (16 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (10 files)
      … 10 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
    razzle.config.js
packages/  (87 files)
  after.js/  (52 files)
    basic-example/  (16 files)
      … 16 files under this directory
    src/  (15 files)
      … 15 files under this directory
    test/  (15 files)
      … 15 files under this directory
    .eslintrc.json
    .gitignore
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
  babel-plugin-after/  (9 files)
    example/  (3 files)
      … 3 files under this directory
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    .gitignore
    README.md
    package.json
  create-after-app/  (26 files)
    bin/  (1 files)
      … 1 files under this directory
    lib/  (7 files)
      … 7 files under this directory
    templates/  (15 files)
      … 15 files under this directory
    README.md
    index.js
    package.json
scripts/  (1 files)
  release-notes.js
.gitignore
.prettierignore
LICENSE
SECURITY.md
UPGRADING.md
lerna.json
package.json
turbo.json
```

## Entry points

- [packages/create-after-app/index.js](https://github.com/jaredpalmer/after.js/blob/dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7/packages/create-after-app/index.js)
- [packages/create-after-app/bin/create-after-app](https://github.com/jaredpalmer/after.js/blob/dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7/packages/create-after-app/bin/create-after-app)
- [packages/after.js/src/index.tsx](https://github.com/jaredpalmer/after.js/blob/dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7/packages/after.js/src/index.tsx)
- [packages/babel-plugin-after/src/index.js](https://github.com/jaredpalmer/after.js/blob/dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7/packages/babel-plugin-after/src/index.js)
- [packages/create-after-app/lib/index.js](https://github.com/jaredpalmer/after.js/blob/dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7/packages/create-after-app/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 43 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 15 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/labeler.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/label.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/size.yml` (ci)
- `examples/basic/package.json` (manifest)
- `examples/layout-component/package.json` (manifest)
- `examples/with-context-api/package.json` (manifest)
- `examples/with-material-ui-rtl/package.json` (manifest)
- `examples/with-material-ui/package.json` (manifest)
- `examples/with-redux/package.json` (manifest)
- `examples/with-scss/package.json` (manifest)
- `examples/with-static-export/package.json` (manifest)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/after.js/.eslintrc.json` (config)
- `packages/after.js/basic-example/package.json` (manifest)
- `packages/after.js/package.json` (manifest)
- `packages/after.js/tsconfig.json` (config)
- `packages/babel-plugin-after/package.json` (manifest)
- `packages/create-after-app/package.json` (manifest)
- `packages/create-after-app/templates/default/package.json` (manifest)
- `turbo.json` (config)

## Top-level layout

- `examples` — 131 analysed file(s)
- `packages` — 87 analysed file(s)
- `.github` — 11 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dbc362fa9b7204349e2d8fdc8c7ea4d80132faf7` is the revision these paths and observations refer to.
