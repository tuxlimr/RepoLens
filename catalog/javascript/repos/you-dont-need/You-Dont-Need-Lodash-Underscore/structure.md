# Project structure: you-dont-need/You-Dont-Need-Lodash-Underscore

**Analysed commit:** `8baa6bf52cf339b3e80ac72294ba848b5f31a38b`

**Commit reference:** [8baa6bf52cf339b3e80ac72294ba848b5f31a38b](https://github.com/you-dont-need/You-Dont-Need-Lodash-Underscore/commit/8baa6bf52cf339b3e80ac72294ba848b5f31a38b)

**Tree at this commit:** [you-dont-need/You-Dont-Need-Lodash-Underscore@8baa6bf52cf3](https://github.com/you-dont-need/You-Dont-Need-Lodash-Underscore/tree/8baa6bf52cf339b3e80ac72294ba848b5f31a38b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | you-dont-need/You-Dont-Need-Lodash-Underscore |
| Description | List of JavaScript methods which you can use natively + ESLint Plugin |
| Stars | 19113 |
| Forks | 814 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `8baa6bf52cf339b3e80ac72294ba848b5f31a38b` |
| Retrieved at | 2026-11-14T19:11:18.056831+00:00 |
| Files in this snapshot | 18 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    master.yml
    pr.yml
docs/  (3 files)
  .nojekyll
  README.md
  index.html
lib/  (2 files)
  rules/  (2 files)
    all.js
    rules.json
tests/  (3 files)
  lib/  (1 files)
    rules/  (1 files)
      … 1 files under this directory
  unit/  (1 files)
    all.js
  index.js
.gitignore
.travis.yml
LICENSE
README.md
TEMPLATE.md
configuring.md
index.js
package.json
```

## Entry points

- [index.js](https://github.com/you-dont-need/You-Dont-Need-Lodash-Underscore/blob/8baa6bf52cf339b3e80ac72294ba848b5f31a38b/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 1 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/master.yml` (ci)
- `.github/workflows/pr.yml` (ci)
- `.travis.yml` (ci)
- `lib/rules/rules.json` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 8 analysed file(s)
- `docs` — 3 analysed file(s)
- `tests` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `lib` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8baa6bf52cf339b3e80ac72294ba848b5f31a38b` is the revision these paths and observations refer to.
