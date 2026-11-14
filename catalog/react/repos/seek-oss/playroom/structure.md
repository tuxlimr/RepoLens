# Project structure: seek-oss/playroom

**Analysed commit:** `4bc32249e210d09c2fade5f9f756ae5ed64c5478`

**Commit reference:** [4bc32249e210d09c2fade5f9f756ae5ed64c5478](https://github.com/seek-oss/playroom/commit/4bc32249e210d09c2fade5f9f756ae5ed64c5478)

**Tree at this commit:** [seek-oss/playroom@4bc32249e210](https://github.com/seek-oss/playroom/tree/4bc32249e210d09c2fade5f9f756ae5ed64c5478)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | seek-oss/playroom |
| Description | Design with JSX, powered by your own component library. |
| Stars | 4594 |
| Forks | 190 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `4bc32249e210d09c2fade5f9f756ae5ed64c5478` |
| Retrieved at | 2026-11-14T19:14:41.720966+00:00 |
| Files in this snapshot | 214 |

## Directory tree

```text
.changeset/  (7 files)
  README.md
  config.json
  curly-impalas-help.md
  open-clubs-brake.md
  quiet-frames-blush.md
  quiet-frames-rest.md
  tolerate-uninspectable-exports.md
.github/  (4 files)
  workflows/  (3 files)
    preview-site.yml
    release.yml
    validate.yml
  CODEOWNERS
.husky/  (1 files)
  pre-commit
cypress/  (22 files)
  e2e/  (15 files)
    editor.cy.ts
    frameSettings.cy.ts
    frameStyles.cy.ts
    headerActions.cy.ts
    inspectElement.cy.ts
    keymaps.cy.ts
    mainMenu.cy.ts
    open.cy.ts
    reactFiberContract.cy.ts
    renderingErrors.cy.ts
    scope.cy.ts
    share.cy.ts
    smoke.cy.ts
    snippets.cy.ts
    urlHandling.cy.ts
  support/  (4 files)
    commands.ts
    e2e.ts
    fixtureConfigs.d.ts
    utils.ts
  cypress.config.ts
  package.json
  tsconfig.json
fixtures/  (23 files)
  basic/  (8 files)
    FrameComponent.js
    components.jsx
    context.js
    package.json
    playroom.config.js
    serve.json
    snippets.js
    useScope.js
  themed/  (6 files)
    components.jsx
    package.json
    playroom.config.js
    serve.json
    snippets.js
    themes.js
  typescript/  (9 files)
    components/  (3 files)
      … 3 files under this directory
    components.ts
    package.json
    playroom.config.js
    serve.json
    snippets.ts
    tsconfig.json
packages/  (142 files)
  playroom/  (142 files)
    src/  (136 files)
      … 136 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsdown.config.ts
scripts/  (2 files)
  package.json
  postCommitStatus.js
.editorconfig
.gitignore
.nvmrc
.prettierignore
.prettierrc
LICENSE
README.md
eslint.config.js
knip.jsonc
package.json
pnpm-workspace.yaml
tsconfig.json
vitest.config.ts
```

## Entry points

- [packages/playroom/src/cli.ts](https://github.com/seek-oss/playroom/blob/4bc32249e210d09c2fade5f9f756ae5ed64c5478/packages/playroom/src/cli.ts)
- [packages/playroom/src/index.ts](https://github.com/seek-oss/playroom/blob/4bc32249e210d09c2fade5f9f756ae5ed64c5478/packages/playroom/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 20 file(s) under cypress package (observed from repository paths and static analysis). |
| fixtures package | library | Observed | Groups 16 file(s) under fixtures package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 136 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/workflows/preview-site.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/validate.yml` (ci)
- `cypress/package.json` (manifest)
- `cypress/tsconfig.json` (config)
- `fixtures/basic/package.json` (manifest)
- `fixtures/basic/serve.json` (config)
- `fixtures/themed/package.json` (manifest)
- `fixtures/themed/serve.json` (config)
- `fixtures/typescript/package.json` (manifest)
- `fixtures/typescript/serve.json` (config)
- `fixtures/typescript/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/playroom/package.json` (manifest)
- `packages/playroom/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `scripts/package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 142 analysed file(s)
- `fixtures` — 23 analysed file(s)
- `cypress` — 22 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.changeset` — 7 analysed file(s)
- `.github` — 4 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4bc32249e210d09c2fade5f9f756ae5ed64c5478` is the revision these paths and observations refer to.
