# Project structure: suren-atoyan/monaco-react

**Analysed commit:** `f7ef2e686c83449babaea49815c69db3668d2ab7`

**Commit reference:** [f7ef2e686c83449babaea49815c69db3668d2ab7](https://github.com/suren-atoyan/monaco-react/commit/f7ef2e686c83449babaea49815c69db3668d2ab7)

**Tree at this commit:** [suren-atoyan/monaco-react@f7ef2e686c83](https://github.com/suren-atoyan/monaco-react/tree/f7ef2e686c83449babaea49815c69db3668d2ab7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | suren-atoyan/monaco-react |
| Description | Monaco Editor for React - use the monaco-editor in any React application without needing to use webpack (or rollup/parcel/etc) configuration files / plugins |
| Stars | 4756 |
| Forks | 322 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `f7ef2e686c83449babaea49815c69db3668d2ab7` |
| Retrieved at | 2026-11-14T19:14:36.876903+00:00 |
| Files in this snapshot | 94 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    auto-merge-dependabot.yml
    stale.yml
  FUNDING.yml
  dependabot.yml
.husky/  (1 files)
  pre-commit
demo/  (37 files)
  public/  (1 files)
    robots.txt
  src/  (26 files)
    DiffEditor/  (2 files)
      … 2 files under this directory
    Editor/  (8 files)
      … 8 files under this directory
    ErrorBoundary/  (3 files)
      … 3 files under this directory
    assets/  (2 files)
      … 2 files under this directory
    config/  (3 files)
      … 3 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    App.tsx
    index.css
    main.tsx
    monaco-themes.d.ts
    root.tsx
    styled.ts
    vite-env.d.ts
  .gitignore
  README.md
  biome.json
  eslint.config.js
  index.html
  package.json
  tsconfig.app.json
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
playground/  (8 files)
  src/  (3 files)
    App.tsx
    global.css
    main.tsx
  .gitignore
  index.html
  logo.svg
  package.json
  vite.config.ts
src/  (27 files)
  DiffEditor/  (5 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    DiffEditor.tsx
    index.spec.tsx
    index.ts
    types.ts
  Editor/  (5 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    Editor.tsx
    index.spec.tsx
    index.ts
    types.ts
  Loading/  (5 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    Loading.tsx
    index.spec.tsx
    index.ts
    styles.ts
  MonacoContainer/  (6 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    MonacoContainer.tsx
    index.spec.tsx
    index.ts
    styles.ts
    types.ts
  hooks/  (4 files)
    useMonaco/  (1 files)
      … 1 files under this directory
    useMount/  (1 files)
      … 1 files under this directory
    usePrevious/  (1 files)
      … 1 files under this directory
    useUpdate/  (1 files)
      … 1 files under this directory
  utils/  (1 files)
    index.ts
  index.ts
.gitignore
.npmignore
.prettierrc.json
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
README.md
eslint.config.mjs
package.json
setupTests.ts
tea.yaml
tsconfig.json
tsup.config.ts
v4.changes.md
vitest.config.ts
```

## Entry points

- [demo/src/App.tsx](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/demo/src/App.tsx)
- [demo/src/DiffEditor/index.ts](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/demo/src/DiffEditor/index.ts)
- [demo/src/Editor/index.ts](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/demo/src/Editor/index.ts)
- [demo/src/ErrorBoundary/index.ts](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/demo/src/ErrorBoundary/index.ts)
- [demo/src/config/index.ts](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/demo/src/config/index.ts)
- [demo/src/main.tsx](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/demo/src/main.tsx)
- [playground/src/App.tsx](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/playground/src/App.tsx)
- [playground/src/main.tsx](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/playground/src/main.tsx)
- [src/DiffEditor/index.ts](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/src/DiffEditor/index.ts)
- [src/Editor/index.ts](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/src/Editor/index.ts)
- [src/Loading/index.ts](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/src/Loading/index.ts)
- [src/MonacoContainer/index.ts](https://github.com/suren-atoyan/monaco-react/blob/f7ef2e686c83449babaea49815c69db3668d2ab7/src/MonacoContainer/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 18 file(s) under demo package (observed from repository paths and static analysis). |
| DiffEditor package | library | Observed | Groups 4 file(s) under diffeditor package (observed from repository paths and static analysis). |
| Editor package | library | Observed | Groups 4 file(s) under editor package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 4 file(s) under hooks package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| Loading package | library | Observed | Groups 4 file(s) under loading package (observed from repository paths and static analysis). |
| MonacoContainer package | library | Observed | Groups 5 file(s) under monacocontainer package (observed from repository paths and static analysis). |
| playground package | library | Observed | Groups 3 file(s) under playground package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/auto-merge-dependabot.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.prettierrc.json` (config)
- `demo/biome.json` (config)
- `demo/package.json` (manifest)
- `demo/tsconfig.app.json` (config)
- `demo/tsconfig.json` (config)
- `demo/tsconfig.node.json` (config)
- `package.json` (manifest)
- `playground/package.json` (manifest)
- `tea.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `demo` — 37 analysed file(s)
- `src` — 27 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `playground` — 8 analysed file(s)
- `.github` — 6 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 64 file(s) were skipped during inventory (1 x likely secret file excluded; 2 x lockfile excluded; 61 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f7ef2e686c83449babaea49815c69db3668d2ab7` is the revision these paths and observations refer to.
