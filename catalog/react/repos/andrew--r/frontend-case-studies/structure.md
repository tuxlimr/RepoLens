# Project structure: andrew--r/frontend-case-studies

**Analysed commit:** `aa9329a0ddf5453c99a1b5d1de1356e9cf042f7f`

**Commit reference:** [aa9329a0ddf5453c99a1b5d1de1356e9cf042f7f](https://github.com/andrew--r/frontend-case-studies/commit/aa9329a0ddf5453c99a1b5d1de1356e9cf042f7f)

**Tree at this commit:** [andrew--r/frontend-case-studies@aa9329a0ddf5](https://github.com/andrew--r/frontend-case-studies/tree/aa9329a0ddf5453c99a1b5d1de1356e9cf042f7f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | andrew--r/frontend-case-studies |
| Description | 💼 A curated list of talks and articles about real world frontend development |
| Stars | 7437 |
| Forks | 424 |
| Licence | Not detected |
| Language | Astro |
| Default branch | master |
| Analysed commit | `aa9329a0ddf5453c99a1b5d1de1356e9cf042f7f` |
| Retrieved at | 2026-11-14T19:13:50.325633+00:00 |
| Files in this snapshot | 40 |

## Directory tree

```text
.claude/  (1 files)
  settings.local.json
website/  (36 files)
  public/  (2 files)
    s/  (1 files)
      … 1 files under this directory
    robots.txt
  src/  (27 files)
    components/  (8 files)
      … 8 files under this directory
    domain/  (7 files)
      … 7 files under this directory
    layouts/  (1 files)
      … 1 files under this directory
    pages/  (5 files)
      … 5 files under this directory
    styles/  (4 files)
      … 4 files under this directory
    config.ts
    content.config.ts
  .gitignore
  CLAUDE.md
  README.md
  astro.config.mjs
  package.json
  pnpm-workspace.yaml
  tsconfig.json
.editorconfig
.nvmrc
readme.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 5 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.claude/settings.local.json` (config)
- `.editorconfig` (config)
- `website/package.json` (manifest)
- `website/pnpm-workspace.yaml` (config)
- `website/src/domain/caseStudy/data.ru.toml` (config)
- `website/src/domain/company/data.ru.toml` (config)
- `website/src/domain/company/data.toml` (config)
- `website/tsconfig.json` (config)

## Top-level layout

- `website` — 36 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `.claude` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `aa9329a0ddf5453c99a1b5d1de1356e9cf042f7f` is the revision these paths and observations refer to.
