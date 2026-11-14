# Project structure: motdotla/dotenv

**Analysed commit:** `4c5450405612e4368e0d46d44da01942cf22a707`

**Commit reference:** [4c5450405612e4368e0d46d44da01942cf22a707](https://github.com/motdotla/dotenv/commit/4c5450405612e4368e0d46d44da01942cf22a707)

**Tree at this commit:** [motdotla/dotenv@4c5450405612](https://github.com/motdotla/dotenv/tree/4c5450405612e4368e0d46d44da01942cf22a707)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | motdotla/dotenv |
| Description | Loads environment variables from .env for nodejs projects. |
| Stars | 20565 |
| Forks | 984 |
| Licence | BSD-2-Clause |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `4c5450405612e4368e0d46d44da01942cf22a707` |
| Retrieved at | 2026-11-14T19:11:12.836753+00:00 |
| Files in this snapshot | 35 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
lib/  (4 files)
  config-options.js
  main.d.ts
  main.js
  spawn-command.js
scripts/  (2 files)
  build.js
  parse-perf.js
tests/  (13 files)
  types/  (2 files)
    test.ts
    tsconfig.json
  .env-multiline
  test-cli-signals.js
  test-cli.js
  test-config-import.js
  test-config-options.js
  test-config-quiet.js
  test-config.js
  test-parse-fast.js
  test-parse-multiline.js
  test-parse.js
  test-populate.js
.editorconfig
.gitignore
.npmignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
cli.js
config.d.ts
config.js
dotenv.svg
index.js
package.json
```

## Entry points

- [index.js](https://github.com/motdotla/dotenv/blob/4c5450405612e4368e0d46d44da01942cf22a707/index.js)
- [lib/main.js](https://github.com/motdotla/dotenv/blob/4c5450405612e4368e0d46d44da01942cf22a707/lib/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 4 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 13 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 14 analysed file(s)
- `tests` — 13 analysed file(s)
- `lib` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4c5450405612e4368e0d46d44da01942cf22a707` is the revision these paths and observations refer to.
