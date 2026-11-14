# Project structure: 7kms/react-illustration-series

**Analysed commit:** `1e71a14310bcb92cd29ef98dddb45f462df4b546`

**Commit reference:** [1e71a14310bcb92cd29ef98dddb45f462df4b546](https://github.com/7kms/react-illustration-series/commit/1e71a14310bcb92cd29ef98dddb45f462df4b546)

**Tree at this commit:** [7kms/react-illustration-series@1e71a14310bc](https://github.com/7kms/react-illustration-series/tree/1e71a14310bcb92cd29ef98dddb45f462df4b546)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | 7kms/react-illustration-series |
| Description | 图解react源码, 用大量配图的方式, 致力于将react原理表述清楚. |
| Stars | 7909 |
| Forks | 833 |
| Licence | AGPL-3.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `1e71a14310bcb92cd29ef98dddb45f462df4b546` |
| Retrieved at | 2026-11-14T19:13:44.153681+00:00 |
| Files in this snapshot | 40 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
.husky/  (2 files)
  commit-msg
  pre-commit
docs/  (27 files)
  algorithm/  (6 files)
    bitfield.md
    dfs.md
    diff.md
    heapsort.md
    linkedlist.md
    stack.md
  interview/  (3 files)
    01-setstate.md
    06-key.md
    index.md
  main/  (17 files)
    bootstrap.md
    context.md
    fibertree-commit.md
    fibertree-create.md
    fibertree-prepare.md
    fibertree-update.md
    hook-effect.md
    hook-state.md
    hook-summary.md
    macro-structure.md
    object-structure.md
    priority.md
    reconciler-workflow.md
    scheduler.md
    state-effects.md
    synthetic-event.md
    workloop.md
  index.md
.dumirc.ts
.editorconfig
.gitignore
.prettierignore
.prettierrc
.prettierrc.js
licence
package.json
readme.md
tsconfig.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `docs` — 27 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1e71a14310bcb92cd29ef98dddb45f462df4b546` is the revision these paths and observations refer to.
