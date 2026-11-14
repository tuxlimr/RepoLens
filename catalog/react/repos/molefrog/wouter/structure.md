# Project structure: molefrog/wouter

**Analysed commit:** `51b55c0dc1b2a16ca07954b8728b395325598d93`

**Commit reference:** [51b55c0dc1b2a16ca07954b8728b395325598d93](https://github.com/molefrog/wouter/commit/51b55c0dc1b2a16ca07954b8728b395325598d93)

**Tree at this commit:** [molefrog/wouter@51b55c0dc1b2](https://github.com/molefrog/wouter/tree/51b55c0dc1b2a16ca07954b8728b395325598d93)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | molefrog/wouter |
| Description | 🥢 A minimalist-friendly ~2.2KB routing for React and Preact |
| Stars | 7919 |
| Forks | 193 |
| Licence | Unlicense |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `51b55c0dc1b2a16ca07954b8728b395325598d93` |
| Retrieved at | 2026-11-14T19:13:43.464807+00:00 |
| Files in this snapshot | 108 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (3 files)
    ci-tests.yml
    release.yml
    size.yml
  FUNDING.yml
assets/  (4 files)
  icon_duotone.svg
  logo.svg
  wouter-skate.svg
  wouter.svg
packages/  (89 files)
  magazin/  (19 files)
    components/  (4 files)
      … 4 files under this directory
    db/  (1 files)
      … 1 files under this directory
    routes/  (5 files)
      … 5 files under this directory
    .gitignore
    App.tsx
    bun.lock
    client.tsx
    index.html
    index.tsx
    package.json
    styles.css
    tsconfig.json
  wouter/  (59 files)
    src/  (14 files)
      … 14 files under this directory
    test/  (37 files)
      … 37 files under this directory
    types/  (7 files)
      … 7 files under this directory
    package.json
  wouter-preact/  (11 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    types/  (7 files)
      … 7 files under this directory
    .gitignore
    package.json
specs/  (1 files)
  view-transitions-spec.md
.gitattributes
.gitignore
AGENTS.md
LICENSE
README.md
RELEASING.md
bun.lock
bunfig.toml
package.json
tsconfig.json
```

## Entry points

- [packages/wouter/src/index.js](https://github.com/molefrog/wouter/blob/51b55c0dc1b2a16ca07954b8728b395325598d93/packages/wouter/src/index.js)
- [packages/magazin/App.tsx](https://github.com/molefrog/wouter/blob/51b55c0dc1b2a16ca07954b8728b395325598d93/packages/magazin/App.tsx)
- [packages/magazin/index.tsx](https://github.com/molefrog/wouter/blob/51b55c0dc1b2a16ca07954b8728b395325598d93/packages/magazin/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 5 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 36 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 38 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/ci-tests.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/size.yml` (ci)
- `bunfig.toml` (config)
- `package.json` (manifest)
- `packages/magazin/package.json` (manifest)
- `packages/magazin/tsconfig.json` (config)
- `packages/wouter-preact/package.json` (manifest)
- `packages/wouter/package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 89 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 4 analysed file(s)
- `assets` — 4 analysed file(s)
- `specs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `51b55c0dc1b2a16ca07954b8728b395325598d93` is the revision these paths and observations refer to.
