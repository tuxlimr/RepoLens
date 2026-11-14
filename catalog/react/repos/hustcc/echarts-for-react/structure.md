# Project structure: hustcc/echarts-for-react

**Analysed commit:** `a0e9565e858824896f9bff526253e59065f57e44`

**Commit reference:** [a0e9565e858824896f9bff526253e59065f57e44](https://github.com/hustcc/echarts-for-react/commit/a0e9565e858824896f9bff526253e59065f57e44)

**Tree at this commit:** [hustcc/echarts-for-react@a0e9565e8588](https://github.com/hustcc/echarts-for-react/tree/a0e9565e858824896f9bff526253e59065f57e44)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hustcc/echarts-for-react |
| Description | ⛳️  Apache ECharts components for React wrapper. 一个简单的 Apache echarts 的 React 封装。 |
| Stars | 5009 |
| Forks | 648 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `a0e9565e858824896f9bff526253e59065f57e44` |
| Retrieved at | 2026-11-14T19:14:29.681079+00:00 |
| Files in this snapshot | 39 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    build.yml
__tests__/  (6 files)
  charts/  (1 files)
    simple-spec.tsx
  helper/  (4 files)
    is-equal-spec.ts
    is-fucntion-spec.ts
    is-string-spec.ts
    pick-spec.ts
  utils/  (1 files)
    index.ts
docs/  (12 files)
  examples/  (11 files)
    api.md
    dynamic.md
    event.md
    gl.md
    graph.md
    html-props.md
    loading.md
    locale.md
    simple.md
    svg.md
    theme.md
  index.md
src/  (7 files)
  helper/  (4 files)
    is-equal.ts
    is-function.ts
    is-string.ts
    pick.ts
  core.tsx
  index.ts
  types.ts
.commitlintrc.js
.editorconfig
.eslintignore
.eslintrc
.gitignore
.lintmdrc
.prettierignore
.prettierrc
.umirc.js
LICENSE
README.md
package.json
tsconfig.json
```

## Entry points

- [src/index.ts](https://github.com/hustcc/echarts-for-react/blob/a0e9565e858824896f9bff526253e59065f57e44/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| core.tsx package | library | Observed | Groups 1 file(s) under core.tsx package (observed from repository paths and static analysis). |
| helper package | library | Observed | Groups 4 file(s) under helper package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 6 file(s) under __tests__ package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/build.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 13 analysed file(s)
- `docs` — 12 analysed file(s)
- `src` — 7 analysed file(s)
- `__tests__` — 6 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a0e9565e858824896f9bff526253e59065f57e44` is the revision these paths and observations refer to.
