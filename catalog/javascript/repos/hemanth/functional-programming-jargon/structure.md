# Project structure: hemanth/functional-programming-jargon

**Analysed commit:** `a362b3a6117eeaa6042fc21e032afa30bab8b5d6`

**Commit reference:** [a362b3a6117eeaa6042fc21e032afa30bab8b5d6](https://github.com/hemanth/functional-programming-jargon/commit/a362b3a6117eeaa6042fc21e032afa30bab8b5d6)

**Tree at this commit:** [hemanth/functional-programming-jargon@a362b3a6117e](https://github.com/hemanth/functional-programming-jargon/tree/a362b3a6117eeaa6042fc21e032afa30bab8b5d6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hemanth/functional-programming-jargon |
| Description | Jargon from the functional programming world in simple terms! |
| Stars | 18744 |
| Forks | 1002 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `a362b3a6117eeaa6042fc21e032afa30bab8b5d6` |
| Retrieved at | 2026-11-14T19:11:19.950744+00:00 |
| Files in this snapshot | 30 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    deploy.yml
  FUNDING.yml
app/  (22 files)
  public/  (4 files)
    data/  (1 files)
      … 1 files under this directory
    llms-full.txt
    llms.txt
    robots.txt
  scripts/  (1 files)
    parse-jargons.js
  src/  (10 files)
    components/  (5 files)
      … 5 files under this directory
    data/  (1 files)
      … 1 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    App.jsx
    index.css
    main.jsx
  tests/  (1 files)
    e2e.test.mjs
  README.md
  index.html
  package.json
  postcss.config.mjs
  tailwind.config.js
  vite.config.mjs
.eslintrc.yml
.gitignore
LICENSE
contributing.md
package.json
readme.md
```

## Entry points

- [app/src/App.jsx](https://github.com/hemanth/functional-programming-jargon/blob/a362b3a6117eeaa6042fc21e032afa30bab8b5d6/app/src/App.jsx)
- [app/src/main.jsx](https://github.com/hemanth/functional-programming-jargon/blob/a362b3a6117eeaa6042fc21e032afa30bab8b5d6/app/src/main.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 12 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/deploy.yml` (ci)
- `app/package.json` (manifest)
- `app/public/data/jargons.json` (config)
- `app/src/data/jargons.json` (config)
- `package.json` (manifest)

## Top-level layout

- `app` — 22 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a362b3a6117eeaa6042fc21e032afa30bab8b5d6` is the revision these paths and observations refer to.
