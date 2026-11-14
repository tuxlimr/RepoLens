# Project structure: FormidableLabs/webpack-dashboard

**Analysed commit:** `9333a27e4b8f784fee13132df4f88e73aca3ca31`

**Commit reference:** [9333a27e4b8f784fee13132df4f88e73aca3ca31](https://github.com/FormidableLabs/webpack-dashboard/commit/9333a27e4b8f784fee13132df4f88e73aca3ca31)

**Tree at this commit:** [FormidableLabs/webpack-dashboard@9333a27e4b8f](https://github.com/FormidableLabs/webpack-dashboard/tree/9333a27e4b8f784fee13132df4f88e73aca3ca31)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | FormidableLabs/webpack-dashboard |
| Description | A CLI dashboard for webpack dev server |
| Stars | 13945 |
| Forks | 374 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9333a27e4b8f784fee13132df4f88e73aca3ca31` |
| Retrieved at | 2026-11-14T19:11:48.789097+00:00 |
| Files in this snapshot | 52 |

## Directory tree

```text
.changeset/  (2 files)
  cold-wolves-occur.md
  config.json
.github/  (2 files)
  workflows/  (2 files)
    ci.yml
    release.yml
bin/  (1 files)
  webpack-dashboard.js
dashboard/  (1 files)
  index.js
docs/  (1 files)
  getting-started.md
examples/  (9 files)
  config/  (2 files)
    webpack.config.js
    webpack.config.ts
  duplicates-esm/  (2 files)
    src/  (1 files)
      … 1 files under this directory
    package.json
  simple/  (2 files)
    src/  (1 files)
      … 1 files under this directory
    package.json
  tree-shaking/  (2 files)
    src/  (1 files)
      … 1 files under this directory
    package.json
  .eslintrc.json
plugin/  (2 files)
  index.d.ts
  index.js
test/  (10 files)
  bin/  (1 files)
    webpack-dashboard.spec.js
  dashboard/  (1 files)
    index.spec.js
  plugin/  (1 files)
    index.spec.js
  utils/  (4 files)
    format-assets.spec.js
    format-modules.spec.js
    format-output.spec.js
    format-versions.spec.js
  .eslintrc.json
  base.spec.js
  setup.js
utils/  (7 files)
  error-serialization.js
  format-assets.js
  format-duplicates.js
  format-modules.js
  format-output.js
  format-problems.js
  format-versions.js
.editorconfig
.eslintignore
.eslintrc.json
.gitignore
.mocharc.yml
.npmignore
.nycrc
.prettierignore
.prettierrc
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
README.md
index.js
package.json
```

## Entry points

- [examples/duplicates-esm/src/index.js](https://github.com/FormidableLabs/webpack-dashboard/blob/9333a27e4b8f784fee13132df4f88e73aca3ca31/examples/duplicates-esm/src/index.js)
- [examples/simple/src/index.js](https://github.com/FormidableLabs/webpack-dashboard/blob/9333a27e4b8f784fee13132df4f88e73aca3ca31/examples/simple/src/index.js)
- [examples/tree-shaking/src/index.js](https://github.com/FormidableLabs/webpack-dashboard/blob/9333a27e4b8f784fee13132df4f88e73aca3ca31/examples/tree-shaking/src/index.js)
- [index.js](https://github.com/FormidableLabs/webpack-dashboard/blob/9333a27e4b8f784fee13132df4f88e73aca3ca31/index.js)
- [bin/webpack-dashboard.js](https://github.com/FormidableLabs/webpack-dashboard/blob/9333a27e4b8f784fee13132df4f88e73aca3ca31/bin/webpack-dashboard.js)
- [dashboard/index.js](https://github.com/FormidableLabs/webpack-dashboard/blob/9333a27e4b8f784fee13132df4f88e73aca3ca31/dashboard/index.js)
- [plugin/index.js](https://github.com/FormidableLabs/webpack-dashboard/blob/9333a27e4b8f784fee13132df4f88e73aca3ca31/plugin/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| dashboard package | library | Observed | Groups 1 file(s) under dashboard package (observed from repository paths and static analysis). |
| plugin package | library | Observed | Groups 2 file(s) under plugin package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 7 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.mocharc.yml` (config)
- `examples/.eslintrc.json` (config)
- `examples/duplicates-esm/package.json` (manifest)
- `examples/simple/package.json` (manifest)
- `examples/tree-shaking/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 17 analysed file(s)
- `test` — 10 analysed file(s)
- `examples` — 9 analysed file(s)
- `utils` — 7 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.github` — 2 analysed file(s)
- `plugin` — 2 analysed file(s)
- `bin` — 1 analysed file(s)
- `dashboard` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 15 file(s) were skipped during inventory (1 x lockfile excluded; 14 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9333a27e4b8f784fee13132df4f88e73aca3ca31` is the revision these paths and observations refer to.
