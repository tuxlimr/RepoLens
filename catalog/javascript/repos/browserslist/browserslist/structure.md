# Project structure: browserslist/browserslist

**Analysed commit:** `8253b7071aae92f6ea755aee54bc93dee47048a1`

**Commit reference:** [8253b7071aae92f6ea755aee54bc93dee47048a1](https://github.com/browserslist/browserslist/commit/8253b7071aae92f6ea755aee54bc93dee47048a1)

**Tree at this commit:** [browserslist/browserslist@8253b7071aae](https://github.com/browserslist/browserslist/tree/8253b7071aae92f6ea755aee54bc93dee47048a1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | browserslist/browserslist |
| Description | 🦔 Share target browsers between different front-end tools, like Autoprefixer, Stylelint and babel-preset-env |
| Stars | 13588 |
| Forks | 798 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `8253b7071aae92f6ea755aee54bc93dee47048a1` |
| Retrieved at | 2026-11-14T19:11:55.862248+00:00 |
| Files in this snapshot | 96 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    release.yml
    test.yml
  FUNDING.yml
docs/  (3 files)
  INCIDENT_RESPONSE.md
  SECURITY.md
  THREAT_MODEL.md
img/  (5 files)
  complement.svg
  icon.svg
  intersection.svg
  logo.svg
  union.svg
test/  (64 files)
  benchmark/  (6 files)
    one/  (2 files)
      … 2 files under this directory
    three/  (1 files)
      … 1 files under this directory
    two/  (2 files)
      … 2 files under this directory
    run.js
  fixtures/  (22 files)
    both1/  (2 files)
      … 2 files under this directory
    both2/  (2 files)
      … 2 files under this directory
    both3/  (2 files)
      … 2 files under this directory
    dir/  (1 files)
      … 1 files under this directory
    env-config/  (2 files)
      … 2 files under this directory
    env-package/  (1 files)
      … 1 files under this directory
    package/  (1 files)
      … 1 files under this directory
    package2/  (1 files)
      … 1 files under this directory
    rc/  (1 files)
      … 1 files under this directory
    string/  (1 files)
      … 1 files under this directory
    typo/  (1 files)
      … 1 files under this directory
    wrong1/  (1 files)
      … 1 files under this directory
    wrong2/  (1 files)
      … 1 files under this directory
    android-stats.json
    browserslist
    browserslist-stats.json
    explorers
    stats.json
  all.test.js
  and.test.js
  baseline.test.js
  browser.test.js
  cache.test.js
  cli.test.js
  config-query.test.js
  config.test.js
  continuation.test.js
  country.test.js
  cover.test.js
  coverage.test.js
  custom.test.js
  dead.test.js
  defaults.test.js
  direct.test.js
  electron.test.js
  error.test.js
  esr.test.js
  extends.test.js
  feature.test.js
  global.test.js
  last.test.js
  main.test.js
  … 12 more files
.devcontainer.json
.editorconfig
.gitignore
.npmignore
.prettierrc.mjs
CHANGELOG.md
LICENSE
README.md
browser.js
cli.js
error.d.ts
error.js
eslint.config.mjs
grammar.w3c-ebnf
index.d.ts
index.js
node.js
oxfmt.config.ts
package.json
parse.js
pnpm-workspace.yaml
```

## Entry points

- [cli.js](https://github.com/browserslist/browserslist/blob/8253b7071aae92f6ea755aee54bc93dee47048a1/cli.js)
- [index.js](https://github.com/browserslist/browserslist/blob/8253b7071aae92f6ea755aee54bc93dee47048a1/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 10 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 64 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)

## Top-level layout

- `test` — 64 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `img` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `docs` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8253b7071aae92f6ea755aee54bc93dee47048a1` is the revision these paths and observations refer to.
