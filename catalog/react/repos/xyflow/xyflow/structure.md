# Project structure: xyflow/xyflow

**Analysed commit:** `1bc405cd113618c17fd181b931a9fe573bec9fee`

**Commit reference:** [1bc405cd113618c17fd181b931a9fe573bec9fee](https://github.com/xyflow/xyflow/commit/1bc405cd113618c17fd181b931a9fe573bec9fee)

**Tree at this commit:** [xyflow/xyflow@1bc405cd1136](https://github.com/xyflow/xyflow/tree/1bc405cd113618c17fd181b931a9fe573bec9fee)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xyflow/xyflow |
| Description | React Flow | Svelte Flow - Powerful open source libraries for building node-based UIs with React (https://reactflow.dev) or Svelte (https://svelteflow.dev). Ready out-of-the-box and infinitely customizable. |
| Stars | 39015 |
| Forks | 2580 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `1bc405cd113618c17fd181b931a9fe573bec9fee` |
| Retrieved at | 2026-11-14T19:13:00.163662+00:00 |
| Files in this snapshot | 699 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  actions/  (2 files)
    ci-checks/  (1 files)
      … 1 files under this directory
    ci-setup/  (1 files)
      … 1 files under this directory
  workflows/  (4 files)
    codespell.yml
    dispatchWebsiteUpdate.yaml
    playwright.yml
    release.yml
  FUNDING.yml
examples/  (315 files)
  astro-xyflow/  (15 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    README.md
    astro.config.mjs
    package.json
    tsconfig.json
  react/  (196 files)
    cypress/  (32 files)
      … 32 files under this directory
    src/  (156 files)
      … 156 files under this directory
    .gitignore
    README.md
    cypress.config.ts
    index.html
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  svelte/  (103 files)
    src/  (94 files)
      … 94 files under this directory
    .gitignore
    .prettierignore
    .prettierrc
    README.md
    eslint.config.js
    package.json
    svelte.config.js
    tsconfig.json
    vite.config.ts
  README.md
packages/  (331 files)
  react/  (135 files)
    src/  (130 files)
      … 130 files under this directory
    .eslintrc.js
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  svelte/  (142 files)
    src/  (133 files)
      … 133 files under this directory
    .gitignore
    .prettierignore
    .prettierrc
    CHANGELOG.md
    README.md
    eslint.config.js
    package.json
    svelte.config.js
    tsconfig.json
  system/  (54 files)
    src/  (49 files)
      … 49 files under this directory
    .eslintrc.js
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
tests/  (17 files)
  playwright/  (17 files)
    e2e/  (11 files)
      … 11 files under this directory
    .gitignore
    README.md
    package.json
    playwright.react.config.ts
    playwright.shared.config.ts
    playwright.svelte.config.ts
tooling/  (9 files)
  eslint-config/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    package.json
  postcss-config/  (1 files)
    postcss.config.js
  rollup-config/  (2 files)
    src/  (1 files)
      … 1 files under this directory
    package.json
  tsconfig/  (3 files)
    base.json
    package.json
    react.json
.codespellrc
.gitattributes
.gitignore
.prettierignore
.prettierrc.json
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
dependabot.yml
package.json
pnpm-workspace.yaml
turbo.json
```

## Entry points

- [tooling/eslint-config/src/index.js](https://github.com/xyflow/xyflow/blob/1bc405cd113618c17fd181b931a9fe573bec9fee/tooling/eslint-config/src/index.js)
- [tooling/rollup-config/src/index.js](https://github.com/xyflow/xyflow/blob/1bc405cd113618c17fd181b931a9fe573bec9fee/tooling/rollup-config/src/index.js)
- [packages/react/src/index.ts](https://github.com/xyflow/xyflow/blob/1bc405cd113618c17fd181b931a9fe573bec9fee/packages/react/src/index.ts)
- [packages/system/src/index.ts](https://github.com/xyflow/xyflow/blob/1bc405cd113618c17fd181b931a9fe573bec9fee/packages/system/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 306 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 20 file(s) under tests (observed from repository paths and static analysis). |
| tooling package | library | Observed | Groups 3 file(s) under tooling package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/actions/ci-checks/action.yml` (config)
- `.github/actions/ci-setup/action.yml` (config)
- `.github/workflows/codespell.yml` (ci)
- `.github/workflows/dispatchWebsiteUpdate.yaml` (ci)
- `.github/workflows/playwright.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.prettierrc.json` (config)
- `dependabot.yml` (config)
- `examples/astro-xyflow/package.json` (manifest)
- `examples/astro-xyflow/tsconfig.json` (config)
- `examples/react/package.json` (manifest)
- `examples/react/tsconfig.json` (config)
- `examples/react/tsconfig.node.json` (config)
- `examples/svelte/package.json` (manifest)
- `examples/svelte/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/react/package.json` (manifest)
- `packages/react/tsconfig.json` (config)
- `packages/svelte/package.json` (manifest)
- `packages/svelte/tsconfig.json` (config)
- `packages/system/package.json` (manifest)
- `packages/system/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tooling/eslint-config/package.json` (manifest)
- `tooling/rollup-config/package.json` (manifest)
- `tooling/tsconfig/base.json` (config)
- `tooling/tsconfig/package.json` (manifest)
- `tooling/tsconfig/react.json` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 331 analysed file(s)
- `examples` — 315 analysed file(s)
- `tests` — 17 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 10 analysed file(s)
- `tooling` — 9 analysed file(s)
- `.changeset` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (5 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1bc405cd113618c17fd181b931a9fe573bec9fee` is the revision these paths and observations refer to.
