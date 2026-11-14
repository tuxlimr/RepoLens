# Project structure: less/less.js

**Analysed commit:** `713331655e437401dfea6cd233893a69762734e1`

**Commit reference:** [713331655e437401dfea6cd233893a69762734e1](https://github.com/less/less.js/commit/713331655e437401dfea6cd233893a69762734e1)

**Tree at this commit:** [less/less.js@713331655e43](https://github.com/less/less.js/tree/713331655e437401dfea6cd233893a69762734e1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | less/less.js |
| Description | Less. The dynamic stylesheet language. |
| Stars | 17000 |
| Forks | 3363 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `713331655e437401dfea6cd233893a69762734e1` |
| Retrieved at | 2026-11-14T19:11:29.071984+00:00 |
| Files in this snapshot | 797 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug.md
    config.yml
  workflows/  (3 files)
    ci.yml
    create-release-pr.yml
    publish.yml
  PULL_REQUEST_TEMPLATE.md
  SECURITY.md
  TESTING_PUBLISHING.md
  stale.yml
.husky/  (2 files)
  post-merge
  pre-commit
.vscode/  (1 files)
  launch.json
config/  (1 files)
  eslint/  (1 files)
    base.cjs
packages/  (773 files)
  less/  (248 files)
    benchmark/  (13 files)
      … 13 files under this directory
    bin/  (1 files)
      … 1 files under this directory
    lib/  (115 files)
      … 115 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    test/  (105 files)
      … 105 files under this directory
    .eslintignore
    .eslintrc.cjs
    .gitignore
    .npmignore
    Gruntfile.cjs
    README.md
    bower.json
    index.cjs
    package.json
    test.less
    tsconfig.json
  test-data/  (525 files)
    data/  (2 files)
      … 2 files under this directory
    plugin/  (13 files)
      … 13 files under this directory
    tests-config/  (180 files)
      … 180 files under this directory
    tests-error/  (202 files)
      … 202 files under this directory
    tests-unit/  (126 files)
      … 126 files under this directory
    index.js
    package.json
.all-contributorsrc
.coderabbit.yaml
.editorconfig
.gitattributes
.gitignore
.nvmrc
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
package.json
```

## Entry points

- [packages/less/bin/lessc](https://github.com/less/less.js/blob/713331655e437401dfea6cd233893a69762734e1/packages/less/bin/lessc)
- [packages/less/benchmark/index.js](https://github.com/less/less.js/blob/713331655e437401dfea6cd233893a69762734e1/packages/less/benchmark/index.js)
- [packages/test-data/index.js](https://github.com/less/less.js/blob/713331655e437401dfea6cd233893a69762734e1/packages/test-data/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 181 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 105 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.coderabbit.yaml` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/create-release-pr.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.vscode/launch.json` (config)
- `package.json` (manifest)
- `packages/less/benchmark/results/latest/macbook-pro_arm64.json` (config)
- `packages/less/benchmark/results/runs/2026-03-09T21-34-11Z_macbook-pro_arm64.json` (config)
- `packages/less/benchmark/results/runs/2026-03-09_macbook-pro_arm64.json` (config)
- `packages/less/bower.json` (config)
- `packages/less/package.json` (manifest)
- `packages/less/tsconfig.json` (config)
- `packages/test-data/package.json` (manifest)
- `packages/test-data/tests-config/globalVars/extended.json` (config)
- `packages/test-data/tests-config/globalVars/simple.json` (config)
- `packages/test-data/tests-config/modifyVars/extended.json` (config)
- `packages/test-data/tests-config/sourcemaps/basic.json` (config)

## Top-level layout

- `packages` — 773 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 9 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `config` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (1 x lockfile excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `713331655e437401dfea6cd233893a69762734e1` is the revision these paths and observations refer to.
