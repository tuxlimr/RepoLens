# Project structure: formkit/formkit

**Analysed commit:** `990590a376c965e7a8fbd6f7061bc5b7528528f0`

**Commit reference:** [990590a376c965e7a8fbd6f7061bc5b7528528f0](https://github.com/formkit/formkit/commit/990590a376c965e7a8fbd6f7061bc5b7528528f0)

**Tree at this commit:** [formkit/formkit@990590a376c9](https://github.com/formkit/formkit/tree/990590a376c965e7a8fbd6f7061bc5b7528528f0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | formkit/formkit |
| Description | The form framework for coding agents |
| Stars | 4787 |
| Forks | 207 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `990590a376c965e7a8fbd6f7061bc5b7528528f0` |
| Retrieved at | 2026-11-14T19:14:35.664069+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.claude/  (1 files)
  agents/  (1 files)
    package-docs-generator.md
.dmux-hooks/  (7 files)
  examples/  (4 files)
    post_merge.example
    run_dev.example
    run_test.example
    worktree_created.example
  AGENTS.md
  CLAUDE.md
  README.md
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.yml
    config.yml
  workflows/  (3 files)
    publish-package.yml
    publish.yml
    tests.yml
  FUNDING.yml
  your-logo-here.svg
.husky/  (1 files)
  commit-msg
.tests/  (2 files)
  react18/  (1 files)
    package.json
  helpers.ts
.vscode/  (1 files)
  settings.json
bench/  (5 files)
  src/  (1 files)
    main.js
  README.md
  index.html
  run.mjs
  vite.config.mjs
e2e/  (8 files)
  servers/  (3 files)
    formKitMemoryServer.mjs
    formKitReactMemoryServer.mjs
    vueMemoryServer.mjs
  memoryDOM.spec.ts
  memoryNuxt.spec.ts
  memoryReactSSR.spec.ts
  memorySSR.spec.ts
  package.json
examples/  (53 files)
  react/  (4 files)
    src/  (3 files)
      … 3 files under this directory
    index.html
  src/  (45 files)
    assets/  (4 files)
      … 4 files under this directory
    types/  (1 files)
      … 1 files under this directory
    vue/  (39 files)
      … 39 files under this directory
    main.ts
  index.html
  package.json
  vite.config.mts
  vite.react.config.mts
packages/  (705 files)
  addons/  (41 files)
    __tests__/  (7 files)
      … 7 files under this directory
    src/  (29 files)
      … 29 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  cli/  (30 files)
    __tests__/  (11 files)
      … 11 files under this directory
    assets/  (3 files)
      … 3 files under this directory
    bin/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  core/  (30 files)
    __tests__/  (9 files)
      … 9 files under this directory
    src/  (16 files)
      … 16 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  dev/  (7 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  formkit/  (7 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  i18n/  (58 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (51 files)
      … 51 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  icons/  (159 files)
    src/  (154 files)
      … 154 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  inputs/  (79 files)
    __tests__/  (3 files)
      … 3 files under this directory
    src/  (71 files)
      … 71 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  nuxt/  (24 files)
    __tests__/  (3 files)
      … 3 files under this directory
    playground/  (10 files)
      … 10 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    build.config.ts
    package.json
    tsconfig.json
    vitest.config.mts
  observer/  (6 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    package.json
  react/  (62 files)
    __tests__/  (30 files)
      … 30 files under this directory
    playground/  (7 files)
      … 7 files under this directory
    src/  (20 files)
      … 20 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  rules/  (78 files)
    __tests__/  (36 files)
      … 36 files under this directory
    src/  (38 files)
      … 38 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    package.json
  tailwindcss/  (14 files)
    playground/  (8 files)
      … 8 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  themes/  (29 files)
    src/  (23 files)
      … 23 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
    tsconfig.json
  utils/  (6 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    CLAUDE.md
    LICENSE
    README.md
    package.json
  validation/  (8 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
  vue/  (67 files)
    __tests__/  (49 files)
      … 49 files under this directory
    src/  (13 files)
      … 13 files under this directory
    .npmignore
    CLAUDE.md
    LICENSE
    README.md
    package.json
.editorconfig
.gitignore
.prettierrc
CLAUDE.md
LICENSE
README.md
commitlint.config.js
eslint.config.js
package.json
```

## Entry points

- [e2e/memoryDOM.spec.ts](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/e2e/memoryDOM.spec.ts)
- [packages/cli/bin/formkit.mjs](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/packages/cli/bin/formkit.mjs)
- [packages/formkit/bin/formkit.mjs](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/packages/formkit/bin/formkit.mjs)
- [bench/src/main.js](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/bench/src/main.js)
- [packages/addons/src/index.ts](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/packages/addons/src/index.ts)
- [packages/cli/src/index.ts](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/packages/cli/src/index.ts)
- [packages/core/src/index.ts](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/packages/core/src/index.ts)
- [packages/dev/src/index.ts](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/packages/dev/src/index.ts)
- [packages/formkit/src/index.ts](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/packages/formkit/src/index.ts)
- [packages/i18n/src/index.ts](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/packages/i18n/src/index.ts)
- [packages/icons/src/index.ts](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/packages/icons/src/index.ts)
- [packages/inputs/src/index.ts](https://github.com/formkit/formkit/blob/990590a376c965e7a8fbd6f7061bc5b7528528f0/packages/inputs/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bench package | library | Observed | Groups 3 file(s) under bench package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 7 file(s) under e2e package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 546 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 25 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/publish-package.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.tests/react18/package.json` (manifest)
- `.vscode/settings.json` (config)
- `e2e/package.json` (manifest)
- `examples/package.json` (manifest)
- `package.json` (manifest)
- `packages/addons/package.json` (manifest)
- `packages/cli/assets/skills/formkit/agents/openai.yaml` (config)
- `packages/cli/package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/dev/package.json` (manifest)
- `packages/formkit/package.json` (manifest)
- `packages/i18n/package.json` (manifest)
- `packages/icons/package.json` (manifest)
- `packages/inputs/package.json` (manifest)
- `packages/nuxt/package.json` (manifest)
- `packages/nuxt/playground/package.json` (manifest)
- `packages/nuxt/tsconfig.json` (config)
- `packages/observer/package.json` (manifest)
- `packages/react/package.json` (manifest)
- `packages/rules/package.json` (manifest)
- `packages/tailwindcss/package.json` (manifest)
- `packages/themes/package.json` (manifest)
- `packages/themes/tsconfig.json` (config)
- `packages/utils/package.json` (manifest)
- `packages/validation/package.json` (manifest)
- `packages/vue/package.json` (manifest)

## Top-level layout

- `packages` — 705 analysed file(s)
- `examples` — 53 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `e2e` — 8 analysed file(s)
- `.dmux-hooks` — 7 analysed file(s)
- `.github` — 7 analysed file(s)
- `bench` — 5 analysed file(s)
- `.tests` — 2 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `990590a376c965e7a8fbd6f7061bc5b7528528f0` is the revision these paths and observations refer to.
