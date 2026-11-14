# Project structure: radix-ui/themes

**Analysed commit:** `1faff10ac26ae17f09944d418c6949b93fc6b566`

**Commit reference:** [1faff10ac26ae17f09944d418c6949b93fc6b566](https://github.com/radix-ui/themes/commit/1faff10ac26ae17f09944d418c6949b93fc6b566)

**Tree at this commit:** [radix-ui/themes@1faff10ac26a](https://github.com/radix-ui/themes/tree/1faff10ac26ae17f09944d418c6949b93fc6b566)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | radix-ui/themes |
| Description | Radix Themes is an open-source component library optimized for fast development, easy maintenance, and accessibility. Maintained by @workos. |
| Stars | 8851 |
| Forks | 347 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `1faff10ac26ae17f09944d418c6949b93fc6b566` |
| Retrieved at | 2026-11-14T19:13:38.364022+00:00 |
| Files in this snapshot | 446 |

## Directory tree

```text
.github/  (5 files)
  actions/  (1 files)
    ci-setup/  (1 files)
      … 1 files under this directory
  workflows/  (2 files)
    ci.yml
    publish.yml
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
.vscode/  (2 files)
  extensions.json
  settings.json
apps/  (111 files)
  playground/  (111 files)
    app/  (100 files)
      … 100 files under this directory
    components/  (2 files)
      … 2 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    eslint.config.mjs
    next.config.mts
    package.json
    playwright.config.ts
    postcss.config.mjs
    tsconfig.json
packages/  (314 files)
  radix-ui-themes/  (314 files)
    scripts/  (3 files)
      … 3 files under this directory
    src/  (299 files)
      … 299 files under this directory
    .browserslistrc
    .stylelintrc.cjs
    CHANGELOG.md
    README.md
    eslint.config.js
    package.json
    postcss-breakpoints.cjs
    postcss-breakpoints.js
    postcss-whitespace.cjs
    postcss-whitespace.js
    postcss.config.js
    tsconfig.json
.gitignore
.nvmrc
.prettierignore
.prettierrc
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
LICENSE
README.md
context7.json
package.json
pnpm-workspace.yaml
release-process.md
turbo.json
```

## Entry points

- [packages/radix-ui-themes/src/index.ts](https://github.com/radix-ui/themes/blob/1faff10ac26ae17f09944d418c6949b93fc6b566/packages/radix-ui-themes/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 75 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 159 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 27 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/actions/ci-setup/action.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `apps/playground/package.json` (manifest)
- `apps/playground/tsconfig.json` (config)
- `context7.json` (config)
- `package.json` (manifest)
- `packages/radix-ui-themes/package.json` (manifest)
- `packages/radix-ui-themes/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 314 analysed file(s)
- `apps` — 111 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 5 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1faff10ac26ae17f09944d418c6949b93fc6b566` is the revision these paths and observations refer to.
