# Project structure: markdoc/markdoc

**Analysed commit:** `30a77b3c23c2d9279ee07d185faf95060b6cab75`

**Commit reference:** [30a77b3c23c2d9279ee07d185faf95060b6cab75](https://github.com/markdoc/markdoc/commit/30a77b3c23c2d9279ee07d185faf95060b6cab75)

**Tree at this commit:** [markdoc/markdoc@30a77b3c23c2](https://github.com/markdoc/markdoc/tree/30a77b3c23c2d9279ee07d185faf95060b6cab75)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | markdoc/markdoc |
| Description | A powerful, flexible, Markdown-based authoring framework. |
| Stars | 8525 |
| Forks | 266 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `30a77b3c23c2d9279ee07d185faf95060b6cab75` |
| Retrieved at | 2026-11-14T19:13:41.313392+00:00 |
| Files in this snapshot | 108 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (5 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.yml
  workflows/  (2 files)
    release.yml
    validate.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
.vscode/  (1 files)
  launch.json
packages/  (90 files)
  markdoc/  (69 files)
    spec/  (10 files)
      … 10 files under this directory
    src/  (52 files)
      … 52 files under this directory
    CHANGELOG.md
    LICENSE
    build.js
    eslint.config.mjs
    index.ts
    package.json
    tsconfig.json
  next.js/  (21 files)
    src/  (5 files)
      … 5 files under this directory
    tests/  (11 files)
      … 11 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    babel.config.json
    package.json
patches/  (1 files)
  markdown-it@15.0.1.patch
.gitignore
.node-version
.prettierrc
AGENTS.md
LICENSE
README.md
package.json
pnpm-workspace.yaml
turbo.json
```

## Entry points

- [packages/next.js/src/index.js](https://github.com/markdoc/markdoc/blob/30a77b3c23c2d9279ee07d185faf95060b6cab75/packages/next.js/src/index.js)
- [packages/markdoc/index.ts](https://github.com/markdoc/markdoc/blob/30a77b3c23c2d9279ee07d185faf95060b6cab75/packages/markdoc/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 67 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/validate.yml` (ci)
- `.vscode/launch.json` (config)
- `package.json` (manifest)
- `packages/markdoc/package.json` (manifest)
- `packages/markdoc/spec/marktest/tests.yaml` (config)
- `packages/markdoc/spec/support/jasmine.json` (config)
- `packages/markdoc/tsconfig.json` (config)
- `packages/next.js/babel.config.json` (config)
- `packages/next.js/package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 90 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 5 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `patches` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `30a77b3c23c2d9279ee07d185faf95060b6cab75` is the revision these paths and observations refer to.
