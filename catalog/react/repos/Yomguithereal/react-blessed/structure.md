# Project structure: Yomguithereal/react-blessed

**Analysed commit:** `b686438af2726111637ef17b998f0f6967623640`

**Commit reference:** [b686438af2726111637ef17b998f0f6967623640](https://github.com/Yomguithereal/react-blessed/commit/b686438af2726111637ef17b998f0f6967623640)

**Tree at this commit:** [Yomguithereal/react-blessed@b686438af272](https://github.com/Yomguithereal/react-blessed/tree/b686438af2726111637ef17b998f0f6967623640)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Yomguithereal/react-blessed |
| Description | A react renderer for blessed. |
| Stars | 4488 |
| Forks | 180 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b686438af2726111637ef17b998f0f6967623640` |
| Retrieved at | 2026-11-14T19:14:44.326695+00:00 |
| Files in this snapshot | 34 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
examples/  (15 files)
  components/  (1 files)
    AnimatedBox.jsx
  utils/  (1 files)
    colors.js
  animation.jsx
  context.jsx
  dashboard.jsx
  demo.jsx
  dispatch.jsx
  effects.jsx
  flex.jsx
  form.jsx
  hooks.jsx
  neo-blessed.jsx
  progressbar.jsx
  remove.jsx
  teardown.jsx
src/  (7 files)
  fiber/  (4 files)
    devtools.js
    events.js
    fiber.js
    index.js
  shared/  (2 files)
    solveClass.js
    update.js
  index.js
test/  (2 files)
  suites/  (1 files)
    solveClass.js
  endpoint.js
.babelrc
.gitignore
.npmignore
.prettierignore
LICENSE.txt
README.md
package.json
rollup.config.js
run.js
```

## Entry points

- [src/fiber/index.js](https://github.com/Yomguithereal/react-blessed/blob/b686438af2726111637ef17b998f0f6967623640/src/fiber/index.js)
- [src/index.js](https://github.com/Yomguithereal/react-blessed/blob/b686438af2726111637ef17b998f0f6967623640/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| fiber package | library | Observed | Groups 4 file(s) under fiber package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 2 file(s) under shared package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `examples` — 15 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `src` — 7 analysed file(s)
- `test` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b686438af2726111637ef17b998f0f6967623640` is the revision these paths and observations refer to.
