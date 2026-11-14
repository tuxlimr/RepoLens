# Project structure: JakeChampion/fetch

**Analysed commit:** `ba5cf1ed2e02ebb96fa1e60b4fd2eb04071b60e4`

**Commit reference:** [ba5cf1ed2e02ebb96fa1e60b4fd2eb04071b60e4](https://github.com/JakeChampion/fetch/commit/ba5cf1ed2e02ebb96fa1e60b4fd2eb04071b60e4)

**Tree at this commit:** [JakeChampion/fetch@ba5cf1ed2e02](https://github.com/JakeChampion/fetch/tree/ba5cf1ed2e02ebb96fa1e60b4fd2eb04071b60e4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | JakeChampion/fetch |
| Description | A window.fetch JavaScript polyfill. |
| Stars | 25819 |
| Forks | 2811 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `ba5cf1ed2e02ebb96fa1e60b4fd2eb04071b60e4` |
| Retrieved at | 2026-11-14T19:10:56.314026+00:00 |
| Files in this snapshot | 28 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (4 files)
    lock.yml
    node.js.yml
    release.yml
    scorecard.yml
  dependabot.yml
test/  (6 files)
  karma-worker.config.js
  karma.config.js
  server.js
  test.js
  worker-adapter.js
  worker.js
.eslintignore
.eslintrc.js
.gitignore
.npmignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
SECURITY.md
bower.json
fetch.js
fetch.js.flow
package.json
prettier.config.js
rollup.config.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/lock.yml` (ci)
- `.github/workflows/node.js.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 17 analysed file(s)
- `test` — 6 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ba5cf1ed2e02ebb96fa1e60b4fd2eb04071b60e4` is the revision these paths and observations refer to.
