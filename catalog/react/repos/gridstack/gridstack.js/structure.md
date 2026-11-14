# Project structure: gridstack/gridstack.js

**Analysed commit:** `400eb8c29ab416215d618fdd7006ea2ef3b281a1`

**Commit reference:** [400eb8c29ab416215d618fdd7006ea2ef3b281a1](https://github.com/gridstack/gridstack.js/commit/400eb8c29ab416215d618fdd7006ea2ef3b281a1)

**Tree at this commit:** [gridstack/gridstack.js@400eb8c29ab4](https://github.com/gridstack/gridstack.js/tree/400eb8c29ab416215d618fdd7006ea2ef3b281a1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gridstack/gridstack.js |
| Description | Build interactive dashboards in minutes. |
| Stars | 9244 |
| Forks | 1419 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `400eb8c29ab416215d618fdd7006ea2ef3b281a1` |
| Retrieved at | 2026-11-14T19:13:35.274703+00:00 |
| Files in this snapshot | 279 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (2 files)
    ci.yml
    deploy-docs.yml
  FUNDING.yml
angular/  (50 files)
  doc/  (6 files)
    api/  (6 files)
      … 6 files under this directory
  projects/  (34 files)
    demo/  (21 files)
      … 21 files under this directory
    lib/  (13 files)
      … 13 files under this directory
  .editorconfig
  .gitignore
  README.md
  README_build.md
  angular.json
  package.json
  tsconfig.doc.json
  tsconfig.json
  typedoc.html.json
  typedoc.json
demo/  (39 files)
  anijs.html
  canvasJS.html
  cell-height.html
  column.html
  css_attributes.html
  custom-engine.html
  demo.css
  esmodule.html
  events.js
  float.html
  grid-lines.html
  index.html
  knockout.html
  lazy_load.html
  list.html
  list_advanced.html
  locked.html
  mobile.html
  nested.html
  nested_advanced.html
  nested_constraint.html
  old_nested-jq.html
  old_two-jq.html
  print.html
  … 15 more files
doc/  (2 files)
  API.md
  CHANGES.md
e2e/  (4 files)
  fixtures/  (1 files)
    gridstack-with-height.html
  cancelled-cross-grid-drag.spec.ts
  cancelled-drag-after-leave.spec.ts
  gridstack-e2e.spec.ts
react/  (43 files)
  doc/  (9 files)
    api/  (9 files)
      … 9 files under this directory
  projects/  (11 files)
    lib/  (11 files)
      … 11 files under this directory
  src/  (6 files)
    assets/  (1 files)
      … 1 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    App.tsx
    main.tsx
    vite-env.d.ts
  .gitignore
  DESIGN-DECISIONS.md
  README.md
  eslint.config.js
  index.html
  package.json
  tsconfig.app.json
  tsconfig.app.tsbuildinfo
  tsconfig.doc.json
  tsconfig.json
  tsconfig.node.json
  tsconfig.node.tsbuildinfo
  typedoc.html.json
  typedoc.json
  vite.config.ts
  vitest.config.ts
  vitest.setup.ts
scripts/  (3 files)
  generate-docs.js
  reorder-docs.js
  reorder-html-docs.js
spec/  (61 files)
  e2e/  (48 files)
    html/  (47 files)
      … 47 files under this directory
    gridstack-html-spec.js
  integration/  (2 files)
    gridstack-integration.spec.ts
    gridstack-resize-direction.spec.ts
  dd-base-impl-spec.ts
  dd-draggable-touch-spec.ts
  dd-droppable-spec.ts
  dd-manager-spec.ts
  dd-simple-integration-spec.ts
  dd-touch-spec.ts
  gridstack-engine-spec.ts
  gridstack-spec.ts
  regression-spec.ts
  test.html
  utils-spec.ts
src/  (14 files)
  dd-base-impl.ts
  dd-draggable.ts
  dd-droppable.ts
  dd-element.ts
  dd-gridstack.ts
  dd-manager.ts
  dd-resizable-handle.ts
  dd-resizable.ts
  dd-touch.ts
  gridstack-engine.ts
  gridstack.scss
  gridstack.ts
  types.ts
  utils.ts
vue/  (37 files)
  doc/  (8 files)
    api/  (8 files)
      … 8 files under this directory
  projects/  (10 files)
    lib/  (10 files)
      … 10 files under this directory
  src/  (4 files)
    demo/  (2 files)
      … 2 files under this directory
    App.vue
    main.ts
  DESIGN-DECISIONS.md
  README.md
  index.html
  package.json
  tsconfig.app.json
  tsconfig.app.tsbuildinfo
  tsconfig.doc.json
  tsconfig.json
  tsconfig.node.json
  tsconfig.node.tsbuildinfo
  typedoc.html.json
  typedoc.json
  vite.config.ts
  vitest.config.ts
  vitest.setup.ts
.eslintignore
.eslintrc.js
.gitignore
.vitestrc.coverage.ts
Gruntfile.js
LICENSE
PULL_REQUEST_TEMPLATE.md
README.md
TESTING.md
TODO.md
package.json
playwright.config.ts
print_README.md
protractor.conf.js
tsconfig.build.json
tsconfig.docs.json
tsconfig.json
typedoc.html.json
typedoc.json
vitest.config.ts
vitest.setup.ts
webpack.config.js
```

## Entry points

- [react/src/App.tsx](https://github.com/gridstack/gridstack.js/blob/400eb8c29ab416215d618fdd7006ea2ef3b281a1/react/src/App.tsx)
- [react/src/main.tsx](https://github.com/gridstack/gridstack.js/blob/400eb8c29ab416215d618fdd7006ea2ef3b281a1/react/src/main.tsx)
- [vue/src/main.ts](https://github.com/gridstack/gridstack.js/blob/400eb8c29ab416215d618fdd7006ea2ef3b281a1/vue/src/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| angular package | library | Observed | Groups 21 file(s) under angular package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 36 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| dd-base-impl.ts package | library | Observed | Groups 1 file(s) under dd-base-impl.ts package (observed from repository paths and static analysis). |
| dd-draggable.ts package | library | Observed | Groups 1 file(s) under dd-draggable.ts package (observed from repository paths and static analysis). |
| dd-droppable.ts package | library | Observed | Groups 1 file(s) under dd-droppable.ts package (observed from repository paths and static analysis). |
| dd-element.ts package | library | Observed | Groups 1 file(s) under dd-element.ts package (observed from repository paths and static analysis). |
| dd-gridstack.ts package | library | Observed | Groups 1 file(s) under dd-gridstack.ts package (observed from repository paths and static analysis). |
| dd-manager.ts package | library | Observed | Groups 1 file(s) under dd-manager.ts package (observed from repository paths and static analysis). |
| dd-resizable-handle.ts package | library | Observed | Groups 1 file(s) under dd-resizable-handle.ts package (observed from repository paths and static analysis). |
| dd-resizable.ts package | library | Observed | Groups 1 file(s) under dd-resizable.ts package (observed from repository paths and static analysis). |
| dd-touch.ts package | library | Observed | Groups 1 file(s) under dd-touch.ts package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 1 file(s) under demo package (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 3 file(s) under e2e package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). |
| gridstack-engine.ts package | library | Observed | Groups 1 file(s) under gridstack-engine.ts package (observed from repository paths and static analysis). |
| gridstack.ts package | library | Observed | Groups 1 file(s) under gridstack.ts package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 18 file(s) under react package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 11 file(s) under spec package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |
| vue package | library | Observed | Groups 15 file(s) under vue package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-docs.yml` (ci)
- `angular/.editorconfig` (config)
- `angular/angular.json` (config)
- `angular/package.json` (manifest)
- `angular/projects/demo/tsconfig.app.json` (config)
- `angular/projects/demo/tsconfig.spec.json` (config)
- `angular/projects/lib/ng-package.json` (config)
- `angular/projects/lib/package.json` (manifest)
- `angular/projects/lib/tsconfig.lib.json` (config)
- `angular/projects/lib/tsconfig.lib.prod.json` (config)
- `angular/projects/lib/tsconfig.spec.json` (config)
- `angular/tsconfig.doc.json` (config)
- `angular/tsconfig.json` (config)
- `angular/typedoc.html.json` (config)
- `angular/typedoc.json` (config)
- `package.json` (manifest)
- `react/package.json` (manifest)
- `react/projects/lib/tsconfig.build.json` (config)
- `react/tsconfig.app.json` (config)
- `react/tsconfig.doc.json` (config)
- `react/tsconfig.json` (config)
- `react/tsconfig.node.json` (config)
- `react/typedoc.html.json` (config)
- `react/typedoc.json` (config)
- `tsconfig.build.json` (config)
- `tsconfig.docs.json` (config)
- `tsconfig.json` (config)
- `typedoc.html.json` (config)
- `typedoc.json` (config)
- `vue/package.json` (manifest)
- `vue/projects/lib/tsconfig.build.json` (config)
- `vue/tsconfig.app.json` (config)
- `vue/tsconfig.doc.json` (config)
- `vue/tsconfig.json` (config)
- `vue/tsconfig.node.json` (config)
- `vue/typedoc.html.json` (config)
- `vue/typedoc.json` (config)

## Top-level layout

- `spec` — 61 analysed file(s)
- `angular` — 50 analysed file(s)
- `react` — 43 analysed file(s)
- `demo` — 39 analysed file(s)
- `vue` — 37 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `src` — 14 analysed file(s)
- `.github` — 4 analysed file(s)
- `e2e` — 4 analysed file(s)
- `scripts` — 3 analysed file(s)
- `doc` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `400eb8c29ab416215d618fdd7006ea2ef3b281a1` is the revision these paths and observations refer to.
