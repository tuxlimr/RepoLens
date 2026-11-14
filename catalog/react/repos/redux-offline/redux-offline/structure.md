# Project structure: redux-offline/redux-offline

**Analysed commit:** `41c0958bce419028e96cd63095eda5baee5a64b0`

**Commit reference:** [41c0958bce419028e96cd63095eda5baee5a64b0](https://github.com/redux-offline/redux-offline/commit/41c0958bce419028e96cd63095eda5baee5a64b0)

**Tree at this commit:** [redux-offline/redux-offline@41c0958bce41](https://github.com/redux-offline/redux-offline/tree/41c0958bce419028e96cd63095eda5baee5a64b0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | redux-offline/redux-offline |
| Description | Build Offline-First Apps for Web and React Native |
| Stars | 6130 |
| Forks | 386 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `41c0958bce419028e96cd63095eda5baee5a64b0` |
| Retrieved at | 2026-11-14T19:14:09.589015+00:00 |
| Files in this snapshot | 94 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE/  (1 files)
    redux-offline-core-issues-template.md
docs/  (34 files)
  docs/  (17 files)
    api/  (4 files)
      … 4 files under this directory
    basics/  (6 files)
      … 6 files under this directory
    recepies/  (5 files)
      … 5 files under this directory
    introduction.md
    troubleshooting.md
  src/  (5 files)
    components/  (2 files)
      … 2 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
  static/  (6 files)
    img/  (5 files)
      … 5 files under this directory
    .nojekyll
  .gitignore
  README.md
  babel.config.js
  docusaurus.config.js
  package.json
  sidebars.js
examples/  (17 files)
  web/  (17 files)
    client/  (14 files)
      … 14 files under this directory
    README.md
    package.json
    server.js
flow-typed/  (2 files)
  npm/  (2 files)
    redux-logger_vx.x.x.js
    redux_v4.x.x.js
src/  (28 files)
  __tests__/  (6 files)
    defaults/  (2 files)
      … 2 files under this directory
    index.js
    middleware.js
    offlineActionTracker.js
    send.js
  defaults/  (13 files)
    defaultCommit.js
    defaultRollback.js
    detectNetwork.js
    detectNetwork.native.js
    discard.js
    effect.js
    index.js
    offlineStateLens.js
    persist.js
    persist.native.js
    persistAutoRehydrate.js
    queue.js
    retry.js
  actions.js
  config.js
  constants.js
  index.js
  middleware.js
  offlineActionTracker.js
  send.js
  types.js
  updater.js
.babelrc
.eslintignore
.eslintrc.js
.flowconfig
.gitignore
.npmignore
.prettierrc
.travis.yml
LICENSE
README.md
package.json
typings.d.ts
```

## Entry points

- [src/defaults/index.js](https://github.com/redux-offline/redux-offline/blob/41c0958bce419028e96cd63095eda5baee5a64b0/src/defaults/index.js)
- [src/index.js](https://github.com/redux-offline/redux-offline/blob/41c0958bce419028e96cd63095eda5baee5a64b0/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| actions.js package | library | Observed | Groups 1 file(s) under actions.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| defaults package | library | Observed | Groups 13 file(s) under defaults package (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 2 file(s) under flow-typed package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| middleware.js package | library | Observed | Groups 1 file(s) under middleware.js package (observed from repository paths and static analysis). |
| offlineActionTracker.js package | library | Observed | Groups 1 file(s) under offlineactiontracker.js package (observed from repository paths and static analysis). |
| send.js package | library | Observed | Groups 1 file(s) under send.js package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 6 file(s) under __tests__ package (observed from repository paths and static analysis). |
| types.js package | library | Observed | Groups 1 file(s) under types.js package (observed from repository paths and static analysis). |
| updater.js package | library | Observed | Groups 1 file(s) under updater.js package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `docs/docs/api/_category_.json` (config)
- `docs/docs/basics/_category_.json` (config)
- `docs/docs/recepies/_category_.json` (config)
- `docs/package.json` (manifest)
- `examples/web/client/package.json` (manifest)
- `examples/web/client/public/manifest.json` (config)
- `examples/web/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `docs` — 34 analysed file(s)
- `src` — 28 analysed file(s)
- `examples` — 17 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `flow-typed` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `41c0958bce419028e96cd63095eda5baee5a64b0` is the revision these paths and observations refer to.
