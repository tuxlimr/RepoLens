# Project structure: SortableJS/Vue.Draggable

**Analysed commit:** `431db153bfdfe09e31f622f01e9b3220b77e6b56`

**Commit reference:** [431db153bfdfe09e31f622f01e9b3220b77e6b56](https://github.com/SortableJS/Vue.Draggable/commit/431db153bfdfe09e31f622f01e9b3220b77e6b56)

**Tree at this commit:** [SortableJS/Vue.Draggable@431db153bfdf](https://github.com/SortableJS/Vue.Draggable/tree/431db153bfdfe09e31f622f01e9b3220b77e6b56)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | SortableJS/Vue.Draggable |
| Description | Vue drag-and-drop component based on Sortable.js |
| Stars | 20538 |
| Forks | 2826 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `431db153bfdfe09e31f622f01e9b3220b77e6b56` |
| Retrieved at | 2026-11-14T19:11:13.463790+00:00 |
| Files in this snapshot | 63 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (1 files)
  issue_template.md
.vscode/  (1 files)
  launch.json
docs/  (2 files)
  img/  (1 files)
    logo.c6a3753c.svg
  index.html
documentation/  (3 files)
  Vue.draggable.for.ReadME.md
  legacy.options.md
  migrate.md
example/  (29 files)
  assets/  (1 files)
    logo.svg
  components/  (21 files)
    infra/  (2 files)
      … 2 files under this directory
    nested/  (2 files)
      … 2 files under this directory
    clone-on-control.vue
    clone.vue
    custom-clone.vue
    footerslot.vue
    functional.vue
    handle.vue
    headerslot.vue
    nested-example.vue
    nested-with-vmodel.vue
    simple.vue
    table-column-example.vue
    table-example.vue
    third-party.vue
    transition-example-2.vue
    transition-example.vue
    two-list-headerslots.vue
    two-lists.vue
  debug-components/  (3 files)
    nested/  (1 files)
      … 1 files under this directory
    future-index.vue
    slot-example.vue
  App.vue
  main.js
  route.js
  store.js
public/  (1 files)
  index.html
src/  (3 files)
  util/  (1 files)
    helper.js
  vuedraggable.d.ts
  vuedraggable.js
tests/  (12 files)
  unit/  (12 files)
    helper/  (5 files)
      … 5 files under this directory
    util/  (2 files)
      … 2 files under this directory
    .eslintrc.js
    vuedraggable.integrated.spec.js
    vuedraggable.script.tag.spec.js
    vuedraggable.spec.js
    vuedraggable.ssr.spec.js
.codebeatignore
.gitignore
CONTRIBUTING.md
LICENSE
README.md
babel.config.js
jest.config.js
logo.svg
package.json
vue.config.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 1 file(s) under util package (observed from repository paths and static analysis). |
| vuedraggable.d.ts package | library | Observed | Groups 1 file(s) under vuedraggable.d.ts package (observed from repository paths and static analysis). |
| vuedraggable.js package | library | Observed | Groups 1 file(s) under vuedraggable.js package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.vscode/launch.json` (config)
- `package.json` (manifest)

## Top-level layout

- `example` — 29 analysed file(s)
- `tests` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `documentation` — 3 analysed file(s)
- `src` — 3 analysed file(s)
- `docs` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `.github` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (2 x likely secret file excluded; 3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `431db153bfdfe09e31f622f01e9b3220b77e6b56` is the revision these paths and observations refer to.
