# Project structure: commitizen/cz-cli

**Analysed commit:** `1a8c49c02c9d52d1b4ef8cdabefb538088ddea03`

**Commit reference:** [1a8c49c02c9d52d1b4ef8cdabefb538088ddea03](https://github.com/commitizen/cz-cli/commit/1a8c49c02c9d52d1b4ef8cdabefb538088ddea03)

**Tree at this commit:** [commitizen/cz-cli@1a8c49c02c9d](https://github.com/commitizen/cz-cli/tree/1a8c49c02c9d52d1b4ef8cdabefb538088ddea03)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | commitizen/cz-cli |
| Description | The commitizen command line utility. #BlackLivesMatter |
| Stars | 17504 |
| Forks | 564 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `1a8c49c02c9d52d1b4ef8cdabefb538088ddea03` |
| Retrieved at | 2026-11-14T19:11:27.400434+00:00 |
| Files in this snapshot | 70 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    release.yml
bin/  (6 files)
  commitizen
  commitizen.cmd
  commitizen.js
  git-cz
  git-cz.cmd
  git-cz.js
jobs/  (1 files)
  build.yml
logo/  (3 files)
  commitizen-logo-color.svg
  commitizen-logo-mono.svg
  generate.sh
src/  (29 files)
  cli/  (8 files)
    parsers/  (2 files)
      … 2 files under this directory
    strategies/  (2 files)
      … 2 files under this directory
    commitizen.js
    git-cz.js
    parsers.js
    strategies.js
  commitizen/  (6 files)
    adapter.js
    cache.js
    commit.js
    configLoader.js
    init.js
    staging.js
  common/  (1 files)
    util.js
  configLoader/  (4 files)
    findup.js
    getContent.js
    getNormalizedConfig.js
    loader.js
  git/  (5 files)
    add.js
    commit.js
    init.js
    log.js
    whatChanged.js
  commitizen.js
  configLoader.js
  git.js
  index.js
  npm.js
test/  (18 files)
  fixtures/  (3 files)
    invalid-json-rc
    invalid-json.json
    valid-json-rc
  tests/  (9 files)
    adapter.js
    cli.js
    commit.js
    configLoader.js
    index.js
    init.js
    parsers.js
    staging.js
    util.js
  tools/  (3 files)
    clean.js
    files.js
    repo.js
  config.js
  mochareporters.json
  tester.js
.editorconfig
.eslintrc
.gitignore
.npmignore
CONTRIBUTING.md
LICENSE
README.md
azure-pipelines.yml
babel.config.js
jsconfig.json
package.json
renovate.json
```

## Entry points

- [bin/git-cz](https://github.com/commitizen/cz-cli/blob/1a8c49c02c9d52d1b4ef8cdabefb538088ddea03/bin/git-cz)
- [bin/commitizen](https://github.com/commitizen/cz-cli/blob/1a8c49c02c9d52d1b4ef8cdabefb538088ddea03/bin/commitizen)
- [src/index.js](https://github.com/commitizen/cz-cli/blob/1a8c49c02c9d52d1b4ef8cdabefb538088ddea03/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 8 file(s) under cli package (observed from repository paths and static analysis). |
| commitizen package | library | Observed | Groups 6 file(s) under commitizen package (observed from repository paths and static analysis). |
| commitizen.js package | library | Observed | Groups 1 file(s) under commitizen.js package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 1 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| configLoader package | library | Observed | Groups 4 file(s) under configloader package (observed from repository paths and static analysis). |
| configLoader.js package | library | Observed | Groups 1 file(s) under configloader.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| git package | library | Observed | Groups 5 file(s) under git package (observed from repository paths and static analysis). |
| git.js package | library | Observed | Groups 1 file(s) under git.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| logo package | library | Observed | Groups 1 file(s) under logo package (observed from repository paths and static analysis). |
| npm.js package | library | Observed | Groups 1 file(s) under npm.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/release.yml` (ci)
- `azure-pipelines.yml` (ci)
- `jobs/build.yml` (config)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `renovate.json` (config)

## Top-level layout

- `src` — 29 analysed file(s)
- `test` — 18 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `bin` — 6 analysed file(s)
- `logo` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `jobs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1a8c49c02c9d52d1b4ef8cdabefb538088ddea03` is the revision these paths and observations refer to.
