# Project structure: fkhadra/react-toastify

**Analysed commit:** `f3069891e0f2309cd53a691f38012b8960afc98b`

**Commit reference:** [f3069891e0f2309cd53a691f38012b8960afc98b](https://github.com/fkhadra/react-toastify/commit/f3069891e0f2309cd53a691f38012b8960afc98b)

**Tree at this commit:** [fkhadra/react-toastify@f3069891e0f2](https://github.com/fkhadra/react-toastify/tree/f3069891e0f2309cd53a691f38012b8960afc98b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fkhadra/react-toastify |
| Description | React notification made easy 🚀 ! |
| Stars | 13439 |
| Forks | 742 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `f3069891e0f2309cd53a691f38012b8960afc98b` |
| Retrieved at | 2026-11-14T19:13:18.547527+00:00 |
| Files in this snapshot | 83 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (1 files)
    build.yaml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
cypress/  (4 files)
  support/  (4 files)
    commands.ts
    component-index.html
    component.ts
    style.css
packages/  (4 files)
  use-notification-center/  (4 files)
    src/  (3 files)
      … 3 files under this directory
    package.json
playground/  (19 files)
  public/  (1 files)
    vite.svg
  src/  (11 files)
    assets/  (1 files)
      … 1 files under this directory
    components/  (7 files)
      … 7 files under this directory
    index.css
    main.tsx
    vite-env.d.ts
  .eslintrc.cjs
  .gitignore
  index.html
  package.json
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
src/  (38 files)
  components/  (13 files)
    CloseButton.cy.tsx
    CloseButton.tsx
    Icons.cy.tsx
    Icons.tsx
    ProgressBar.cy.tsx
    ProgressBar.tsx
    StyledToastContainer.cy.tsx
    StyledToastContainer.tsx
    Toast.cy.tsx
    Toast.tsx
    ToastContainer.tsx
    Transitions.tsx
    index.tsx
  core/  (6 files)
    containerObserver.ts
    genToastId.ts
    index.ts
    store.ts
    toast.cy.tsx
    toast.ts
  hooks/  (7 files)
    index.ts
    useIsomorphicLayoutEffect.ts
    useStyleSheet.cy.tsx
    useStyleSheet.ts
    useStyleSheetAppend.cy.tsx
    useToast.ts
    useToastContainer.ts
  utils/  (6 files)
    collapseToast.ts
    constant.ts
    cssTransition.tsx
    index.ts
    mapper.ts
    propValidator.ts
  css.d.ts
  index.ts
  style.css
  tests.cy.tsx
  types.ts
  unstyled.ts
.gitignore
.nycrc.json
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
cypress.config.ts
lefthook.yml
package.json
pnpm-workspace.yaml
tsconfig.json
tsdown.config.mts
vite.config.mts
```

## Entry points

- [packages/use-notification-center/src/index.ts](https://github.com/fkhadra/react-toastify/blob/f3069891e0f2309cd53a691f38012b8960afc98b/packages/use-notification-center/src/index.ts)
- [playground/src/components/App.tsx](https://github.com/fkhadra/react-toastify/blob/f3069891e0f2309cd53a691f38012b8960afc98b/playground/src/components/App.tsx)
- [playground/src/main.tsx](https://github.com/fkhadra/react-toastify/blob/f3069891e0f2309cd53a691f38012b8960afc98b/playground/src/main.tsx)
- [src/components/index.tsx](https://github.com/fkhadra/react-toastify/blob/f3069891e0f2309cd53a691f38012b8960afc98b/src/components/index.tsx)
- [src/core/index.ts](https://github.com/fkhadra/react-toastify/blob/f3069891e0f2309cd53a691f38012b8960afc98b/src/core/index.ts)
- [src/hooks/index.ts](https://github.com/fkhadra/react-toastify/blob/f3069891e0f2309cd53a691f38012b8960afc98b/src/hooks/index.ts)
- [src/index.ts](https://github.com/fkhadra/react-toastify/blob/f3069891e0f2309cd53a691f38012b8960afc98b/src/index.ts)
- [src/utils/index.ts](https://github.com/fkhadra/react-toastify/blob/f3069891e0f2309cd53a691f38012b8960afc98b/src/utils/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 13 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| css.d.ts package | library | Observed | Groups 1 file(s) under css.d.ts package (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 2 file(s) under cypress package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 7 file(s) under hooks package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 3 file(s) under packages package (observed from repository paths and static analysis). |
| playground package | library | Observed | Groups 11 file(s) under playground package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |
| tests.cy.tsx package | library | Observed | Groups 1 file(s) under tests.cy.tsx package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| unstyled.ts package | library | Observed | Groups 1 file(s) under unstyled.ts package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 6 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/build.yaml` (ci)
- `.nycrc.json` (config)
- `lefthook.yml` (config)
- `package.json` (manifest)
- `packages/use-notification-center/package.json` (manifest)
- `playground/package.json` (manifest)
- `playground/tsconfig.json` (config)
- `playground/tsconfig.node.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 38 analysed file(s)
- `playground` — 19 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 4 analysed file(s)
- `cypress` — 4 analysed file(s)
- `packages` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f3069891e0f2309cd53a691f38012b8960afc98b` is the revision these paths and observations refer to.
