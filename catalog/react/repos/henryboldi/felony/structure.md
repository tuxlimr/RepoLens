# Project structure: henryboldi/felony

**Analysed commit:** `8e948160125e3fb69ff1992f03ae0e246577aca7`

**Commit reference:** [8e948160125e3fb69ff1992f03ae0e246577aca7](https://github.com/henryboldi/felony/commit/8e948160125e3fb69ff1992f03ae0e246577aca7)

**Tree at this commit:** [henryboldi/felony@8e948160125e](https://github.com/henryboldi/felony/tree/8e948160125e3fb69ff1992f03ae0e246577aca7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | henryboldi/felony |
| Description | 🔑🔥📈 Next Level PGP |
| Stars | 3451 |
| Forks | 127 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `8e948160125e3fb69ff1992f03ae0e246577aca7` |
| Retrieved at | 2026-11-14T19:15:18.646372+00:00 |
| Files in this snapshot | 106 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE
  PULL_REQUEST_TEMPLATE
app/  (84 files)
  actions/  (4 files)
    AliasesActions.js
    KeychainActions.js
    UIActions.js
    index.js
  assets/  (29 files)
    fonts/  (1 files)
      … 1 files under this directory
    images/  (24 files)
      … 24 files under this directory
    styles/  (4 files)
      … 4 files under this directory
  components/  (30 files)
    alias/  (2 files)
      … 2 files under this directory
    common/  (6 files)
      … 6 files under this directory
    composer/  (6 files)
      … 6 files under this directory
    decrypt/  (2 files)
      … 2 files under this directory
    floating-button/  (3 files)
      … 3 files under this directory
    header/  (5 files)
      … 5 files under this directory
    keychain/  (4 files)
      … 4 files under this directory
    output/  (1 files)
      … 1 files under this directory
    Felony.js
  config/  (1 files)
    database.js
  constants/  (2 files)
    KeychainConstants.js
    UIConstants.js
  containers/  (7 files)
    App.js
    ComposerContainer.js
    DevTools.js
    FloatingButtonContainer.js
    HeaderContainer.js
    KeychainContainer.js
    OutputContainer.js
  reducers/  (3 files)
    index.js
    keychainReducer.js
    uiReducer.js
  utils/  (3 files)
    .gitkeep
    icons.js
    pgp.js
  app.global.css
  app.html
  index.js
  package.json
  routes.js
.babelrc
.editorconfig
.eslintignore
.eslintrc.js
.gitattributes
.gitignore
.jscsrc
.travis.yml
CONTRIBUTING.md
LICENSE
README.md
main.development.js
package.js
package.json
server.js
webpack.config.base.js
webpack.config.development.js
webpack.config.electron.js
webpack.config.node.js
webpack.config.production.js
```

## Entry points

- [app/actions/index.js](https://github.com/henryboldi/felony/blob/8e948160125e3fb69ff1992f03ae0e246577aca7/app/actions/index.js)
- [app/components/common/index.js](https://github.com/henryboldi/felony/blob/8e948160125e3fb69ff1992f03ae0e246577aca7/app/components/common/index.js)
- [app/containers/App.js](https://github.com/henryboldi/felony/blob/8e948160125e3fb69ff1992f03ae0e246577aca7/app/containers/App.js)
- [app/index.js](https://github.com/henryboldi/felony/blob/8e948160125e3fb69ff1992f03ae0e246577aca7/app/index.js)
- [app/reducers/index.js](https://github.com/henryboldi/felony/blob/8e948160125e3fb69ff1992f03ae0e246577aca7/app/reducers/index.js)
- [server.js](https://github.com/henryboldi/felony/blob/8e948160125e3fb69ff1992f03ae0e246577aca7/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 52 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `app/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `app` — 84 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8e948160125e3fb69ff1992f03ae0e246577aca7` is the revision these paths and observations refer to.
