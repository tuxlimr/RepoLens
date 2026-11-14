# Project structure: capricorn86/happy-dom

**Analysed commit:** `5e100dedb73111a276f75a3daff3a506e2524759`

**Commit reference:** [5e100dedb73111a276f75a3daff3a506e2524759](https://github.com/capricorn86/happy-dom/commit/5e100dedb73111a276f75a3daff3a506e2524759)

**Tree at this commit:** [capricorn86/happy-dom@5e100dedb731](https://github.com/capricorn86/happy-dom/tree/5e100dedb73111a276f75a3daff3a506e2524759)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | capricorn86/happy-dom |
| Description | A JavaScript implementation of a web browser without its graphical user interface |
| Stars | 4743 |
| Forks | 380 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `5e100dedb73111a276f75a3daff3a506e2524759` |
| Retrieved at | 2026-11-14T19:14:37.512406+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    custom.md
    feature_request.md
  workflows/  (3 files)
    auto-assign.yml
    pull_request.yml
    release.yml
  CODEOWNERS
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
.husky/  (2 files)
  .gitignore
  pre-commit
.vscode/  (1 files)
  extensions.json
integration-test/  (13 files)
  test/  (7 files)
    browser-exception-observer/  (1 files)
      … 1 files under this directory
    Browser.test.js
    CommonJS.test.cjs
    Fetch.test.js
    WebSocket.test.js
    WindowGlobals.test.js
    XMLHttpRequest.test.js
  .editorconfig
  .gitignore
  .npmignore
  LICENSE
  README.md
  package.json
packages/  (761 files)
  @happy-dom/  (82 files)
    global-registrator/  (19 files)
      … 19 files under this directory
    jest-environment/  (16 files)
      … 16 files under this directory
    node-canvas-adapter/  (9 files)
      … 9 files under this directory
    server-renderer/  (38 files)
      … 38 files under this directory
  happy-dom/  (679 files)
    bin/  (3 files)
      … 3 files under this directory
    src/  (610 files)
      … 610 files under this directory
    test/  (61 files)
      … 61 files under this directory
    .gitignore
    .npmignore
    LICENSE
    README.md
    package.json
.editorconfig
.eslintignore
.eslintrc.cjs
.gitignore
.prettierignore
.prettierrc.cjs
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
cspell.json
package.json
```

## Entry points

- [packages/happy-dom/src/index.ts](https://github.com/capricorn86/happy-dom/blob/5e100dedb73111a276f75a3daff3a506e2524759/packages/happy-dom/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 24 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 629 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 99 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/auto-assign.yml` (ci)
- `.github/workflows/pull_request.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.vscode/extensions.json` (config)
- `cspell.json` (config)
- `integration-test/.editorconfig` (config)
- `integration-test/package.json` (manifest)
- `package.json` (manifest)
- `packages/@happy-dom/global-registrator/package.json` (manifest)
- `packages/@happy-dom/global-registrator/tsconfig.json` (config)
- `packages/@happy-dom/jest-environment/package.json` (manifest)
- `packages/@happy-dom/jest-environment/tsconfig.json` (config)
- `packages/@happy-dom/node-canvas-adapter/package.json` (manifest)
- `packages/@happy-dom/node-canvas-adapter/tsconfig.json` (config)
- `packages/@happy-dom/server-renderer/bin/tsconfig.json` (config)
- `packages/@happy-dom/server-renderer/package.json` (manifest)
- `packages/@happy-dom/server-renderer/tsconfig.json` (config)
- `packages/happy-dom/package.json` (manifest)

## Top-level layout

- `packages` — 761 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `integration-test` — 13 analysed file(s)
- `.github` — 9 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5e100dedb73111a276f75a3daff3a506e2524759` is the revision these paths and observations refer to.
