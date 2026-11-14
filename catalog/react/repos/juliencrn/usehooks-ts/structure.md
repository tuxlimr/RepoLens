# Project structure: juliencrn/usehooks-ts

**Analysed commit:** `61949134144d3690fe9f521260a16c779a6d3797`

**Commit reference:** [61949134144d3690fe9f521260a16c779a6d3797](https://github.com/juliencrn/usehooks-ts/commit/61949134144d3690fe9f521260a16c779a6d3797)

**Tree at this commit:** [juliencrn/usehooks-ts@61949134144d](https://github.com/juliencrn/usehooks-ts/tree/61949134144d3690fe9f521260a16c779a6d3797)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | juliencrn/usehooks-ts |
| Description | React hook library, ready to use, written in Typescript. |
| Stars | 7866 |
| Forks | 456 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `61949134144d3690fe9f521260a16c779a6d3797` |
| Retrieved at | 2026-11-14T19:13:44.551018+00:00 |
| Files in this snapshot | 271 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.yml
    config.yml
    update-docs.yml
  workflows/  (2 files)
    ci.yml
    update-algolia-index.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
.vscode/  (1 files)
  settings.json
apps/  (54 files)
  www/  (54 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (43 files)
      … 43 files under this directory
    .eslintrc.cjs
    .gitignore
    CHANGELOG.md
    env.js
    next-sitemap.config.js
    next.config.js
    package.json
    postcss.config.cjs
    tailwind.config.js
    tsconfig.json
packages/  (178 files)
  eslint-config-custom/  (6 files)
    .eslintrc.cjs
    .gitignore
    CHANGELOG.md
    README.md
    index.cjs
    package.json
  usehooks-ts/  (172 files)
    src/  (162 files)
      … 162 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    .eslintrc.cjs
    .gitignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    tsup.config.ts
    vitest.config.ts
scripts/  (9 files)
  utils/  (5 files)
    data-transform.js
    generate-doc-files.js
    get-hooks.js
    get-markdown-data.js
    update-readme.js
  env.js
  generate-doc.js
  update-algolia-index.js
  update-testing-issue.js
turbo/  (7 files)
  generators/  (7 files)
    templates/  (6 files)
      … 6 files under this directory
    config.cts
.all-contributorsrc
.editorconfig
.gitignore
.prettierignore
.prettierrc
LICENSE
README.md
package.json
pnpm-workspace.yaml
renovate.json
turbo.json
typedoc.json
```

## Entry points

- [packages/eslint-config-custom/index.cjs](https://github.com/juliencrn/usehooks-ts/blob/61949134144d3690fe9f521260a16c779a6d3797/packages/eslint-config-custom/index.cjs)
- [packages/usehooks-ts/src/index.ts](https://github.com/juliencrn/usehooks-ts/blob/61949134144d3690fe9f521260a16c779a6d3797/packages/usehooks-ts/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 39 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 134 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 9 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/update-docs.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/update-algolia-index.yml` (ci)
- `.vscode/settings.json` (config)
- `apps/www/package.json` (manifest)
- `apps/www/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/eslint-config-custom/package.json` (manifest)
- `packages/usehooks-ts/package.json` (manifest)
- `packages/usehooks-ts/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `renovate.json` (config)
- `turbo.json` (config)
- `typedoc.json` (config)

## Top-level layout

- `packages` — 178 analysed file(s)
- `apps` — 54 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `scripts` — 9 analysed file(s)
- `.github` — 8 analysed file(s)
- `turbo` — 7 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `61949134144d3690fe9f521260a16c779a6d3797` is the revision these paths and observations refer to.
