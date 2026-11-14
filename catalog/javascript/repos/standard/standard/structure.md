# Project structure: standard/standard

**Analysed commit:** `753309b21bfd7c98e208e3fb45910ffd1bb95409`

**Commit reference:** [753309b21bfd7c98e208e3fb45910ffd1bb95409](https://github.com/standard/standard/commit/753309b21bfd7c98e208e3fb45910ffd1bb95409)

**Tree at this commit:** [standard/standard@753309b21bfd](https://github.com/standard/standard/tree/753309b21bfd7c98e208e3fb45910ffd1bb95409)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | standard/standard |
| Description | 🌟 JavaScript Style Guide, with linter & automatic code fixer |
| Stars | 29428 |
| Forks | 2298 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `753309b21bfd7c98e208e3fb45910ffd1bb95409` |
| Retrieved at | 2026-11-14T19:10:48.057984+00:00 |
| Files in this snapshot | 52 |

## Directory tree

```text
.github/  (9 files)
  workflows/  (4 files)
    add-to-project.yaml
    old-test.yml
    test-external.yml
    test-internal.yml
  FUNDING.yml
  config.yml
  dependabot.yml
  no-response.yml
  stale.yml
bin/  (1 files)
  cmd.cjs
docs/  (19 files)
  README-esla.md
  README-fr.md
  README-id.md
  README-iteu.md
  README-ja.md
  README-kokr.md
  README-ptbr.md
  README-zhcn.md
  README-zhtw.md
  RULES-esla.md
  RULES-fr.md
  RULES-id.md
  RULES-iteu.md
  RULES-ja.md
  RULES-kokr.md
  RULES-ptbr.md
  RULES-zhcn.md
  RULES-zhtw.md
  webstorm.md
lib/  (2 files)
  cli.js
  options.js
test/  (5 files)
  external/  (2 files)
    clone.js
    test.json
  api.js
  cmd.js
  validate-config.js
tools/  (2 files)
  test-exists.js
  update-authors.sh
.editorconfig
.gitignore
.npmignore
.pre-commit-hooks.yaml
AUTHORS.md
CHANGELOG.md
LICENSE
README.md
RULES.md
badge.svg
eslintrc.json
index.js
package.json
sticker.svg
```

## Entry points

- [index.js](https://github.com/standard/standard/blob/753309b21bfd7c98e208e3fb45910ffd1bb95409/index.js)
- [bin/cmd.cjs](https://github.com/standard/standard/blob/753309b21bfd7c98e208e3fb45910ffd1bb95409/bin/cmd.cjs)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 2 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 2 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/no-response.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/add-to-project.yaml` (ci)
- `.github/workflows/old-test.yml` (ci)
- `.github/workflows/test-external.yml` (ci)
- `.github/workflows/test-internal.yml` (ci)
- `.pre-commit-hooks.yaml` (config)
- `eslintrc.json` (config)
- `package.json` (manifest)

## Top-level layout

- `docs` — 19 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 9 analysed file(s)
- `test` — 5 analysed file(s)
- `lib` — 2 analysed file(s)
- `tools` — 2 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `753309b21bfd7c98e208e3fb45910ffd1bb95409` is the revision these paths and observations refer to.
