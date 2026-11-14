# Project structure: unform/unform

**Analysed commit:** `db496d9369f1a776865d48d78f1b95c8e08a5139`

**Commit reference:** [db496d9369f1a776865d48d78f1b95c8e08a5139](https://github.com/unform/unform/commit/db496d9369f1a776865d48d78f1b95c8e08a5139)

**Tree at this commit:** [unform/unform@db496d9369f1](https://github.com/unform/unform/tree/db496d9369f1a776865d48d78f1b95c8e08a5139)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | unform/unform |
| Description | Performance-focused API for React forms 🚀 |
| Stars | 4399 |
| Forks | 461 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | develop |
| Analysed commit | `db496d9369f1a776865d48d78f1b95c8e08a5139` |
| Retrieved at | 2026-11-14T19:14:47.355607+00:00 |
| Files in this snapshot | 115 |

## Directory tree

```text
.github/  (14 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    config.yml
    documentation-report.md
    enhancement-request.md
  workflows/  (4 files)
    commit.yml
    lint.yml
    test.yml
    tsc.yml
  CODEOWNERS
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE
  labeler.json
  lock.yml
.husky/  (4 files)
  .gitignore
  commit-msg
  common.sh
  pre-commit
docs/  (41 files)
  config/  (1 files)
    sidebar.yml
  src/  (36 files)
    @rocketseat/  (3 files)
      … 3 files under this directory
    docs/  (32 files)
      … 32 files under this directory
    pages/  (1 files)
      … 1 files under this directory
  LICENSE
  gatsby-config.js
  package.json
  vercel.json
examples/  (11 files)
  typescript/  (5 files)
    checkbox.tsx
    input.tsx
    radio.tsx
    select.tsx
    textarea.tsx
  README.md
  checkbox.js
  input.js
  radio.js
  select.js
  textarea.js
packages/  (29 files)
  core/  (16 files)
    __tests__/  (7 files)
      … 7 files under this directory
    lib/  (6 files)
      … 6 files under this directory
    README.md
    jest.config.js
    package.json
  mobile/  (7 files)
    __tests__/  (2 files)
      … 2 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    README.md
    jest.config.js
    package.json
  web/  (6 files)
    __tests__/  (1 files)
      … 1 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    README.md
    jest.config.js
    package.json
.editorconfig
.eslintrc.json
.gitignore
.lintstagedrc.json
.npmignore
.prettierignore
LICENSE
babel.config.js
commitlint.config.js
jest.config.js
lerna.json
package.json
prettier.config.js
renovate.json
rollup.config.js
tsconfig.json
```

## Entry points

- [packages/core/lib/index.ts](https://github.com/unform/unform/blob/db496d9369f1a776865d48d78f1b95c8e08a5139/packages/core/lib/index.ts)
- [packages/mobile/lib/index.ts](https://github.com/unform/unform/blob/db496d9369f1a776865d48d78f1b95c8e08a5139/packages/mobile/lib/index.ts)
- [packages/web/lib/index.ts](https://github.com/unform/unform/blob/db496d9369f1a776865d48d78f1b95c8e08a5139/packages/web/lib/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 8 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/labeler.json` (config)
- `.github/lock.yml` (config)
- `.github/workflows/commit.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/tsc.yml` (ci)
- `.lintstagedrc.json` (config)
- `docs/config/sidebar.yml` (config)
- `docs/package.json` (manifest)
- `docs/vercel.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/mobile/package.json` (manifest)
- `packages/web/package.json` (manifest)
- `renovate.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `docs` — 41 analysed file(s)
- `packages` — 29 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 14 analysed file(s)
- `examples` — 11 analysed file(s)
- `.husky` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `db496d9369f1a776865d48d78f1b95c8e08a5139` is the revision these paths and observations refer to.
