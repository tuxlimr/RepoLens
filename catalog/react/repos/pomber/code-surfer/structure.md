# Project structure: pomber/code-surfer

**Analysed commit:** `948452f7c1c8adaf019e29600d7d158747a91a90`

**Commit reference:** [948452f7c1c8adaf019e29600d7d158747a91a90](https://github.com/pomber/code-surfer/commit/948452f7c1c8adaf019e29600d7d158747a91a90)

**Tree at this commit:** [pomber/code-surfer@948452f7c1c8](https://github.com/pomber/code-surfer/tree/948452f7c1c8adaf019e29600d7d158747a91a90)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pomber/code-surfer |
| Description | Rad code slides <🏄/> |
| Stars | 6366 |
| Forks | 174 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `948452f7c1c8adaf019e29600d7d158747a91a90` |
| Retrieved at | 2026-11-14T19:14:07.571060+00:00 |
| Files in this snapshot | 178 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
.vscode/  (1 files)
  settings.json
packs/  (69 files)
  code-surfer/  (18 files)
    src/  (14 files)
      … 14 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
    readme.md
    tsconfig.json
  standalone/  (18 files)
    src/  (15 files)
      … 15 files under this directory
    package.json
    readme.md
    tsconfig.json
  step-parser/  (17 files)
    src/  (14 files)
      … 14 files under this directory
    package.json
    readme.md
    tsconfig.json
  themes/  (16 files)
    src/  (14 files)
      … 14 files under this directory
    package.json
    tsconfig.json
sites/  (99 files)
  book/  (64 files)
    src/  (62 files)
      … 62 files under this directory
    .gitignore
    package.json
  docs/  (34 files)
    decks/  (13 files)
      … 13 files under this directory
    src/  (14 files)
      … 14 files under this directory
    static/  (2 files)
      … 2 files under this directory
    .gitignore
    gatsby-browser.js
    gatsby-config.js
    gatsby-ssr.js
    package.json
  build.js
.gitignore
.travis.yml
contributing.md
license
netlify.toml
package.json
readme-zh.md
readme.md
```

## Entry points

- [packs/code-surfer/src/index.ts](https://github.com/pomber/code-surfer/blob/948452f7c1c8adaf019e29600d7d158747a91a90/packs/code-surfer/src/index.ts)
- [packs/standalone/src/index.tsx](https://github.com/pomber/code-surfer/blob/948452f7c1c8adaf019e29600d7d158747a91a90/packs/standalone/src/index.tsx)
- [packs/step-parser/src/index.ts](https://github.com/pomber/code-surfer/blob/948452f7c1c8adaf019e29600d7d158747a91a90/packs/step-parser/src/index.ts)
- [packs/themes/src/index.ts](https://github.com/pomber/code-surfer/blob/948452f7c1c8adaf019e29600d7d158747a91a90/packs/themes/src/index.ts)
- [sites/book/src/index.js](https://github.com/pomber/code-surfer/blob/948452f7c1c8adaf019e29600d7d158747a91a90/sites/book/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packs package | library | Observed | Groups 53 file(s) under packs package (observed from repository paths and static analysis). |
| sites package | library | Observed | Groups 62 file(s) under sites package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `.vscode/settings.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `packs/code-surfer/package.json` (manifest)
- `packs/code-surfer/tsconfig.json` (config)
- `packs/standalone/package.json` (manifest)
- `packs/standalone/tsconfig.json` (config)
- `packs/step-parser/package.json` (manifest)
- `packs/step-parser/tsconfig.json` (config)
- `packs/themes/package.json` (manifest)
- `packs/themes/tsconfig.json` (config)
- `sites/book/package.json` (manifest)
- `sites/docs/package.json` (manifest)

## Top-level layout

- `sites` — 99 analysed file(s)
- `packs` — 69 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `948452f7c1c8adaf019e29600d7d158747a91a90` is the revision these paths and observations refer to.
