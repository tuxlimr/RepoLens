# Project structure: AhmadHassan-BTed/Jantt

**Analysed commit:** `52ec345e0e5778dd23585aa5fb9c944bab31b363`

**Commit reference:** [52ec345e0e5778dd23585aa5fb9c944bab31b363](https://github.com/AhmadHassan-BTed/Jantt/commit/52ec345e0e5778dd23585aa5fb9c944bab31b363)

**Tree at this commit:** [AhmadHassan-BTed/Jantt@52ec345e0e57](https://github.com/AhmadHassan-BTed/Jantt/tree/52ec345e0e5778dd23585aa5fb9c944bab31b363)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | AhmadHassan-BTed/Jantt |
| Description | The AI-native JSON Gantt chart engine. Dependency-free interactive timelines with React, script-tag, CLI, topological DAG solver, and formal JSON schema. |
| Stars | 6225 |
| Forks | 21 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `52ec345e0e5778dd23585aa5fb9c944bab31b363` |
| Retrieved at | 2026-11-14T19:14:08.648447+00:00 |
| Files in this snapshot | 345 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (4 files)
    ci.yml
    deploy-pages.yml
    release.yml
    security.yml
  PULL_REQUEST_TEMPLATE.md
.vscode/  (1 files)
  settings.json
apps/  (113 files)
  playground/  (113 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (105 files)
      … 105 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
assets/  (5 files)
  jantt-icon-duotone.svg
  jantt-icon-gradient.svg
  jantt-icon-monochrome.svg
  jantt-icon-outline.svg
  jantt-logo.svg
cli/  (4 files)
  bin/  (1 files)
    jantt.js
  tests/  (1 files)
    cli.test.ts
  README.md
  package.json
docs/  (6 files)
  JANTT_JSON_CHEATSHEET.md
  algorithms.md
  api-reference.md
  architecture.md
  schema-spec.md
  security.md
examples/  (8 files)
  academic-roadmap.json
  basic.json
  broken-bad-date.json
  broken-dangling-dependency.json
  broken-missing-id.json
  cheatsheet-default.json
  construction-enterprise.json
  master-template.json
packages/  (169 files)
  core/  (107 files)
    src/  (73 files)
      … 73 files under this directory
    tests/  (29 files)
      … 29 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
    vite.config.ts
  elements/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    tsconfig.json
    vite.config.ts
  interop/  (12 files)
    src/  (5 files)
      … 5 files under this directory
    tests/  (4 files)
      … 4 files under this directory
    README.md
    package.json
    tsconfig.json
  mcp/  (6 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    tsconfig.json
  react/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
    vite.config.ts
  render-canvas/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    tsconfig.json
  standalone/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
    vite.config.ts
  svelte/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    tsconfig.json
    vite.config.ts
  vue/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    tsconfig.json
    vite.config.ts
  yjs/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    tsconfig.json
    vite.config.ts
python/  (8 files)
  src/  (4 files)
    jantt/  (4 files)
      … 4 files under this directory
  tests/  (1 files)
    test_jantt.py
  .gitignore
  README.md
  pyproject.toml
schema/  (1 files)
  jantt.schema.json
worker/  (3 files)
  src/  (1 files)
    worker.js
  README.md
  wrangler.toml
.editorconfig
.env.example
.gitattributes
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
Makefile
README.md
ROADMAP.md
SECURITY.md
SUPPORT.md
changes_required.md
database.rules.json
docker-compose.yml
firebase.json
package.json
```

## Entry points

- [cli/bin/jantt.js](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/cli/bin/jantt.js)
- [packages/mcp/bin/jantt-mcp.js](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/packages/mcp/bin/jantt-mcp.js)
- [apps/playground/src/App.tsx](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/apps/playground/src/App.tsx)
- [apps/playground/src/main.tsx](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/apps/playground/src/main.tsx)
- [packages/core/src/index.ts](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/packages/core/src/index.ts)
- [packages/elements/src/index.ts](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/packages/elements/src/index.ts)
- [packages/interop/src/index.ts](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/packages/interop/src/index.ts)
- [packages/mcp/src/index.ts](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/packages/mcp/src/index.ts)
- [packages/react/src/index.ts](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/packages/react/src/index.ts)
- [packages/render-canvas/src/index.ts](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/packages/render-canvas/src/index.ts)
- [packages/svelte/src/index.ts](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/packages/svelte/src/index.ts)
- [packages/vue/src/index.ts](https://github.com/AhmadHassan-BTed/Jantt/blob/52ec345e0e5778dd23585aa5fb9c944bab31b363/packages/vue/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 16 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 74 file(s) under apps package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 1 file(s) under cli package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 31 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 6 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: JanttPlan, Task. |
| packages package | library | Observed | Groups 24 file(s) under packages package (observed from repository paths and static analysis). |
| python package | library | Observed | Groups 3 file(s) under python package (observed from repository paths and static analysis). Observed top-level functions: _format_date, from_dataframe, from_records, show, streamlit, to_dataframe. |
| Service / domain layer | service | Observed | Groups 83 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 41 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestJanttPython. |
| worker package | library | Observed | Groups 1 file(s) under worker package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-pages.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/security.yml` (ci)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `apps/playground/package.json` (manifest)
- `apps/playground/public/schema/v1.json` (config)
- `apps/playground/tsconfig.json` (config)
- `cli/package.json` (manifest)
- `database.rules.json` (config)
- `docker-compose.yml` (container)
- `examples/academic-roadmap.json` (config)
- `examples/basic.json` (config)
- `examples/broken-bad-date.json` (config)
- `examples/broken-dangling-dependency.json` (config)
- `examples/broken-missing-id.json` (config)
- `examples/cheatsheet-default.json` (config)
- `examples/construction-enterprise.json` (config)
- `examples/master-template.json` (config)
- `firebase.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/elements/package.json` (manifest)
- `packages/elements/tsconfig.json` (config)
- `packages/interop/package.json` (manifest)
- `packages/interop/tsconfig.json` (config)
- `packages/mcp/package.json` (manifest)
- `packages/mcp/tsconfig.json` (config)
- `packages/react/package.json` (manifest)
- `packages/react/tsconfig.json` (config)
- `packages/render-canvas/package.json` (manifest)
- `packages/render-canvas/tsconfig.json` (config)
- `packages/standalone/package.json` (manifest)
- `packages/svelte/package.json` (manifest)
- `packages/svelte/tsconfig.json` (config)
- `packages/vue/package.json` (manifest)
- `packages/vue/tsconfig.json` (config)
- `packages/yjs/package.json` (manifest)
- `packages/yjs/tsconfig.json` (config)
- `python/pyproject.toml` (manifest)
- `schema/jantt.schema.json` (config)
- `worker/wrangler.toml` (config)

## Top-level layout

- `packages` — 169 analysed file(s)
- `apps` — 113 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 8 analysed file(s)
- `examples` — 8 analysed file(s)
- `python` — 8 analysed file(s)
- `docs` — 6 analysed file(s)
- `assets` — 5 analysed file(s)
- `cli` — 4 analysed file(s)
- `worker` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `schema` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `52ec345e0e5778dd23585aa5fb9c944bab31b363` is the revision these paths and observations refer to.
