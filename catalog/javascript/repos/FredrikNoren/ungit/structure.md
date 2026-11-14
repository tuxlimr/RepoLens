# Project structure: FredrikNoren/ungit

**Analysed commit:** `b1df1a168b9208766342070ebd42782036dfd18d`

**Commit reference:** [b1df1a168b9208766342070ebd42782036dfd18d](https://github.com/FredrikNoren/ungit/commit/b1df1a168b9208766342070ebd42782036dfd18d)

**Tree at this commit:** [FredrikNoren/ungit@b1df1a168b92](https://github.com/FredrikNoren/ungit/tree/b1df1a168b9208766342070ebd42782036dfd18d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FredrikNoren/ungit |
| Description | The easiest way to use git. On any platform. Anywhere. |
| Stars | 10615 |
| Forks | 648 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b1df1a168b9208766342070ebd42782036dfd18d` |
| Retrieved at | 2026-11-14T19:12:35.733777+00:00 |
| Files in this snapshot | 175 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    bump.yml
    ci.yml
assets/  (2 files)
  images/  (2 files)
    icon.svg
    logo.svg
bin/  (2 files)
  credentials-helper
  ungit
clicktests/  (13 files)
  environment.js
  spec.authentication.js
  spec.bare.js
  spec.branches.js
  spec.commands.js
  spec.discard.js
  spec.generic.js
  spec.load-ahead.js
  spec.no-header.js
  spec.remotes.js
  spec.screens.js
  spec.stash.js
  spec.submodules.js
components/  (89 files)
  app/  (4 files)
    app.html
    app.js
    app.less
    ungit-plugin.json
  branches/  (4 files)
    branches.html
    branches.js
    branches.less
    ungit-plugin.json
  commit/  (4 files)
    commit.html
    commit.js
    commit.less
    ungit-plugin.json
  commitdiff/  (5 files)
    commitdiff.html
    commitdiff.js
    commitdiff.less
    commitlinediff.js
    ungit-plugin.json
  crash/  (4 files)
    crash.html
    crash.js
    crash.less
    ungit-plugin.json
  gitErrors/  (3 files)
    gitErrors.html
    gitErrors.js
    ungit-plugin.json
  graph/  (12 files)
    animateable.js
    edge.js
    git-graph-actions.js
    git-node.js
    git-ref.js
    graph-graphics.html
    graph.html
    graph.js
    graph.less
    hover-actions.js
    selectable.js
    ungit-plugin.json
  header/  (4 files)
    header.html
    header.js
    header.less
    ungit-plugin.json
  home/  (4 files)
    home.html
    home.js
    home.less
    ungit-plugin.json
  imagediff/  (4 files)
    imagediff.html
    imagediff.js
    imagediff.less
    ungit-plugin.json
  login/  (3 files)
    login.html
    login.js
    ungit-plugin.json
  modals/  (7 files)
    formModal.html
    forms.ts
    modalBase.ts
    modals.ts
    promptModal.html
    prompts.ts
    ungit-plugin.json
  path/  (4 files)
    path.html
    path.js
    path.less
    ungit-plugin.json
  refreshbutton/  (4 files)
    refreshbutton.html
    refreshbutton.js
    refreshbutton.less
    ungit-plugin.json
  remotes/  (3 files)
    remotes.html
    remotes.js
    ungit-plugin.json
  repository/  (4 files)
    repository.html
    repository.js
    repository.less
    ungit-plugin.json
  staging/  (4 files)
    staging.html
    staging.js
    staging.less
    ungit-plugin.json
  stash/  (4 files)
    stash.html
    stash.js
    stash.less
    ungit-plugin.json
  submodules/  (3 files)
    submodules.html
    submodules.js
    ungit-plugin.json
  textdiff/  (4 files)
    textdiff.html
    textdiff.js
    textdiff.less
    ungit-plugin.json
  ComponentRoot.ts
public/  (15 files)
  less/  (4 files)
    bootstrap.less
    d2h.less
    styles.less
    variables.less
  source/  (9 files)
    bootstrap.js
    components.js
    jquery-ui.js
    knockout-bindings.js
    main.js
    navigation.js
    program-events.js
    server.js
    storage.js
  index.html
  main.js
scripts/  (5 files)
  build.js
  electronpackage.js
  electronzip.js
  npmpublish.js
  teststabilitytester.js
source/  (12 files)
  utils/  (3 files)
    cache.js
    file-type.js
    logger.js
  address-parser.js
  bugtracker.js
  config.js
  git-api.js
  git-parser.js
  git-promise.js
  server.js
  sysinfo.js
  ungit-plugin.js
test/  (18 files)
  common-es6.js
  spec.address-parser.js
  spec.cache.js
  spec.credentials-helper.js
  spec.file-type.js
  spec.git-api.branching.js
  spec.git-api.conflict-no-auto-stash.js
  spec.git-api.conflict.js
  spec.git-api.diff.js
  spec.git-api.discardchanges.js
  spec.git-api.ignorefile.js
  spec.git-api.js
  spec.git-api.patch.js
  spec.git-api.remote.js
  spec.git-api.squash.js
  spec.git-api.stash.js
  spec.git-api.submodule.js
  spec.git-parser.js
.gitattributes
.gitignore
.mochaclicktest.json
.mochatest.json
.npmignore
.prettierignore
.prettierrc
CHANGELOG.md
CONTRIBUTING.md
LICENSE.md
MERGETOOL.md
PLUGINS.md
README.md
appveyor.yml
eslint.config.mjs
package.json
tsconfig.json
```

## Entry points

- [public/main.js](https://github.com/FredrikNoren/ungit/blob/b1df1a168b9208766342070ebd42782036dfd18d/public/main.js)
- [bin/ungit](https://github.com/FredrikNoren/ungit/blob/b1df1a168b9208766342070ebd42782036dfd18d/bin/ungit)
- [bin/credentials-helper](https://github.com/FredrikNoren/ungit/blob/b1df1a168b9208766342070ebd42782036dfd18d/bin/credentials-helper)
- [components/app/app.js](https://github.com/FredrikNoren/ungit/blob/b1df1a168b9208766342070ebd42782036dfd18d/components/app/app.js)
- [public/source/main.js](https://github.com/FredrikNoren/ungit/blob/b1df1a168b9208766342070ebd42782036dfd18d/public/source/main.js)
- [public/source/server.js](https://github.com/FredrikNoren/ungit/blob/b1df1a168b9208766342070ebd42782036dfd18d/public/source/server.js)
- [source/server.js](https://github.com/FredrikNoren/ungit/blob/b1df1a168b9208766342070ebd42782036dfd18d/source/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| clicktests package | library | Observed | Groups 13 file(s) under clicktests package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 31 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 10 file(s) under public package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| source package | library | Observed | Groups 12 file(s) under source package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/bump.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.mochaclicktest.json` (config)
- `.mochatest.json` (config)
- `appveyor.yml` (config)
- `components/app/ungit-plugin.json` (config)
- `components/branches/ungit-plugin.json` (config)
- `components/commit/ungit-plugin.json` (config)
- `components/commitdiff/ungit-plugin.json` (config)
- `components/crash/ungit-plugin.json` (config)
- `components/gitErrors/ungit-plugin.json` (config)
- `components/graph/ungit-plugin.json` (config)
- `components/header/ungit-plugin.json` (config)
- `components/home/ungit-plugin.json` (config)
- `components/imagediff/ungit-plugin.json` (config)
- `components/login/ungit-plugin.json` (config)
- `components/modals/ungit-plugin.json` (config)
- `components/path/ungit-plugin.json` (config)
- `components/refreshbutton/ungit-plugin.json` (config)
- `components/remotes/ungit-plugin.json` (config)
- `components/repository/ungit-plugin.json` (config)
- `components/staging/ungit-plugin.json` (config)
- `components/stash/ungit-plugin.json` (config)
- `components/submodules/ungit-plugin.json` (config)
- `components/textdiff/ungit-plugin.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `components` — 89 analysed file(s)
- `test` — 18 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `public` — 15 analysed file(s)
- `clicktests` — 13 analysed file(s)
- `source` — 12 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.github` — 2 analysed file(s)
- `assets` — 2 analysed file(s)
- `bin` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b1df1a168b9208766342070ebd42782036dfd18d` is the revision these paths and observations refer to.
