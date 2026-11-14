# Project structure: prettier/eslint-config-prettier

**Analysed commit:** `bd6e6171434c7b34dec3dd0f325aab792c126ec6`

**Commit reference:** [bd6e6171434c7b34dec3dd0f325aab792c126ec6](https://github.com/prettier/eslint-config-prettier/commit/bd6e6171434c7b34dec3dd0f325aab792c126ec6)

**Tree at this commit:** [prettier/eslint-config-prettier@bd6e6171434c](https://github.com/prettier/eslint-config-prettier/tree/bd6e6171434c7b34dec3dd0f325aab792c126ec6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | prettier/eslint-config-prettier |
| Description | Turns off all rules that are unnecessary or might conflict with Prettier. |
| Stars | 5899 |
| Forks | 259 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `bd6e6171434c7b34dec3dd0f325aab792c126ec6` |
| Retrieved at | 2026-11-14T19:14:12.864124+00:00 |
| Files in this snapshot | 56 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (6 files)
  workflows/  (5 files)
    autofix.yml
    check.yml
    pkg-pr-new.yml
    release.yml
    test.yml
  FUNDING.yml
.yarn/  (1 files)
  plugins/  (1 files)
    plugin-prepare-lifecycle.cjs
bin/  (2 files)
  cli.js
  validators.js
patches/  (3 files)
  eslint-plugin-babel+5.3.1.patch
  eslint-plugin-flowtype+8.0.3.patch
  eslint-plugin-standard+5.0.0.patch
scripts/  (1 files)
  generate-stylistic.js
test/  (6 files)
  fixtures/  (2 files)
    empty-config/  (2 files)
      … 2 files under this directory
  cli.test.js
  lint-verify-fail.test.js
  rules.test.js
  validators.test.js
test-lint/  (15 files)
  .prettierrc.json
  @babel.js
  @stylistic.js
  @stylistic__js.js
  @stylistic__jsx.jsx
  @stylistic__ts.ts
  @typescript-eslint.ts
  babel.js
  core.js
  flowtype.js
  prettier.js
  react.js
  standard.js
  unicorn.js
  vue-file.vue
.eslintrc.base.js
.eslintrc.js
.gitignore
.prettierignore
.prettierrc.json
.renovaterc
.yarnrc.yml
CHANGELOG.md
LICENSE
README.md
babel.config.json
eslint.base.config.mjs
eslint.config.mjs
flat.d.ts
flat.js
index.d.ts
index.js
package.json
prettier.d.ts
prettier.js
```

## Entry points

- [index.js](https://github.com/prettier/eslint-config-prettier/blob/bd6e6171434c7b34dec3dd0f325aab792c126ec6/index.js)
- [bin/cli.js](https://github.com/prettier/eslint-config-prettier/blob/bd6e6171434c7b34dec3dd0f325aab792c126ec6/bin/cli.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| test-lint package | library | Observed | Groups 14 file(s) under test-lint package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/autofix.yml` (ci)
- `.github/workflows/check.yml` (ci)
- `.github/workflows/pkg-pr-new.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.prettierrc.json` (config)
- `.yarnrc.yml` (config)
- `babel.config.json` (config)
- `package.json` (manifest)
- `test-lint/.prettierrc.json` (config)

## Top-level layout

- `(root files)` — 20 analysed file(s)
- `test-lint` — 15 analysed file(s)
- `.github` — 6 analysed file(s)
- `test` — 6 analysed file(s)
- `patches` — 3 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `bin` — 2 analysed file(s)
- `.yarn` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bd6e6171434c7b34dec3dd0f325aab792c126ec6` is the revision these paths and observations refer to.
