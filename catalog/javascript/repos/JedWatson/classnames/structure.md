# Project structure: JedWatson/classnames

**Analysed commit:** `abd6314010de053a09df5acc53e474ff65cea470`

**Commit reference:** [abd6314010de053a09df5acc53e474ff65cea470](https://github.com/JedWatson/classnames/commit/abd6314010de053a09df5acc53e474ff65cea470)

**Tree at this commit:** [JedWatson/classnames@abd6314010de](https://github.com/JedWatson/classnames/tree/abd6314010de053a09df5acc53e474ff65cea470)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | JedWatson/classnames |
| Description | A simple javascript utility for conditionally joining classNames together |
| Stars | 17773 |
| Forks | 557 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `abd6314010de053a09df5acc53e474ff65cea470` |
| Retrieved at | 2026-11-14T19:11:26.653258+00:00 |
| Files in this snapshot | 27 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    node.js.yml
    release.yml
  dependabot.yml
benchmarks/  (4 files)
  benchmarks.js
  index.html
  run.js
  runInBrowser.js
tests/  (6 files)
  bind.js
  bind.test-d.ts
  dedupe.js
  dedupe.test-d.ts
  index.js
  index.test-d.ts
.editorconfig
.gitignore
.npmignore
CONTRIBUTING.md
HISTORY.md
LICENSE
README.md
bind.d.ts
bind.js
dedupe.d.ts
dedupe.js
index.d.ts
index.js
package.json
```

## Entry points

- [index.js](https://github.com/JedWatson/classnames/blob/abd6314010de053a09df5acc53e474ff65cea470/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 3 file(s) under benchmarks package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/node.js.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 14 analysed file(s)
- `tests` — 6 analysed file(s)
- `benchmarks` — 4 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `abd6314010de053a09df5acc53e474ff65cea470` is the revision these paths and observations refer to.
