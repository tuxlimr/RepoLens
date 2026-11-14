# Project structure: BetaSu/big-react

**Analysed commit:** `0b5bb94d3bb750bed2255b4519eed0d4fb6aed53`

**Commit reference:** [0b5bb94d3bb750bed2255b4519eed0d4fb6aed53](https://github.com/BetaSu/big-react/commit/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53)

**Tree at this commit:** [BetaSu/big-react@0b5bb94d3bb7](https://github.com/BetaSu/big-react/tree/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BetaSu/big-react |
| Description | 跟着我，从0实现React18 |
| Stars | 3898 |
| Forks | 403 |
| Licence | Not detected |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `0b5bb94d3bb750bed2255b4519eed0d4fb6aed53` |
| Retrieved at | 2026-11-14T19:14:58.850183+00:00 |
| Files in this snapshot | 104 |

## Directory tree

```text
.husky/  (2 files)
  commit-msg
  pre-commit
.vscode/  (1 files)
  settings.json
demos/  (34 files)
  context/  (3 files)
    index.html
    main.tsx
    vite-env.d.ts
  performance/  (10 files)
    Context.tsx
    Hook.tsx
    Principle_demo1.tsx
    Principle_demo2.tsx
    Simple.tsx
    index.html
    main.tsx
    memo.tsx
    useMemo.tsx
    vite-env.d.ts
  ref/  (3 files)
    index.html
    main.tsx
    vite-env.d.ts
  suspense-lazy/  (3 files)
    Cpn.tsx
    index.html
    main.tsx
  suspense-use/  (4 files)
    Cpn.tsx
    index.html
    main.tsx
    vite-env.d.ts
  test-fc/  (4 files)
    index.html
    main.ts
    main.tsx
    style.css
  transition/  (7 files)
    AboutTab.tsx
    ContactTab.tsx
    PostsTab.tsx
    TabButton.tsx
    index.html
    main.tsx
    style.css
packages/  (48 files)
  react/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    index.ts
    jsx-dev-runtime.ts
    package.json
  react-dom/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    client.ts
    index.ts
    package.json
    test-utils.ts
  react-noop-renderer/  (4 files)
    src/  (2 files)
      … 2 files under this directory
    index.ts
    package.json
  react-reconciler/  (22 files)
    src/  (21 files)
      … 21 files under this directory
    package.json
  shared/  (5 files)
    ReactSymbols.ts
    ReactTypes.ts
    internals.ts
    package.json
    shallowEquals.ts
scripts/  (10 files)
  jest/  (4 files)
    jest.config.js
    reactTestMatchers.js
    schedulerTestMatchers.js
    setupJest.js
  rollup/  (5 files)
    dev.config.js
    react-dom.config.js
    react-noop-renderer.config.js
    react.config.js
    utils.js
  vite/  (1 files)
    vite.config.js
.commitlintrc.js
.eslintrc.json
.gitignore
.prettierrc.json
README.md
babel.config.js
package.json
pnpm-workspace.yaml
tsconfig.json
```

## Entry points

- [demos/context/main.tsx](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/demos/context/main.tsx)
- [demos/performance/main.tsx](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/demos/performance/main.tsx)
- [demos/ref/main.tsx](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/demos/ref/main.tsx)
- [demos/suspense-lazy/main.tsx](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/demos/suspense-lazy/main.tsx)
- [demos/suspense-use/main.tsx](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/demos/suspense-use/main.tsx)
- [demos/test-fc/main.ts](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/demos/test-fc/main.ts)
- [demos/test-fc/main.tsx](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/demos/test-fc/main.tsx)
- [demos/transition/main.tsx](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/demos/transition/main.tsx)
- [packages/react-dom/index.ts](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/packages/react-dom/index.ts)
- [packages/react-noop-renderer/index.ts](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/packages/react-noop-renderer/index.ts)
- [packages/react/index.ts](https://github.com/BetaSu/big-react/blob/0b5bb94d3bb750bed2255b4519eed0d4fb6aed53/packages/react/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 25 file(s) under demos package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 43 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 10 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.prettierrc.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `packages/react-dom/package.json` (manifest)
- `packages/react-noop-renderer/package.json` (manifest)
- `packages/react-reconciler/package.json` (manifest)
- `packages/react/package.json` (manifest)
- `packages/shared/package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 48 analysed file(s)
- `demos` — 34 analysed file(s)
- `scripts` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0b5bb94d3bb750bed2255b4519eed0d4fb6aed53` is the revision these paths and observations refer to.
