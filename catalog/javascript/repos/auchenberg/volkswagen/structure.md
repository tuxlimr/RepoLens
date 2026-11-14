# Project structure: auchenberg/volkswagen

**Analysed commit:** `ae379b4459ee4dd71b4783246b99f6a3135fdc4b`

**Commit reference:** [ae379b4459ee4dd71b4783246b99f6a3135fdc4b](https://github.com/auchenberg/volkswagen/commit/ae379b4459ee4dd71b4783246b99f6a3135fdc4b)

**Tree at this commit:** [auchenberg/volkswagen@ae379b4459ee](https://github.com/auchenberg/volkswagen/tree/ae379b4459ee4dd71b4783246b99f6a3135fdc4b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | auchenberg/volkswagen |
| Description | :see_no_evil: Volkswagen detects when your tests are being run in a CI server, and makes them pass. |
| Stars | 15467 |
| Forks | 240 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ae379b4459ee4dd71b4783246b99f6a3135fdc4b` |
| Retrieved at | 2026-11-14T19:11:38.354268+00:00 |
| Files in this snapshot | 13 |

## Directory tree

```text
.these/  (1 files)
  aren't/  (1 files)
    the/  (1 files)
      … 1 files under this directory
test/  (7 files)
  _fake-ci.js
  assert.js
  chai.js
  exit-code.js
  tap.js
  tape.js
  throw.js
.gitignore
.travis.yml
LICENSE
README.md
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `test` — 7 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.these` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ae379b4459ee4dd71b4783246b99f6a3135fdc4b` is the revision these paths and observations refer to.
