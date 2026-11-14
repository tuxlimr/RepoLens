# Project structure: timolins/react-hot-toast

**Analysed commit:** `e725d38e0faec05f7b8fb10644b616ef978d2f4d`

**Commit reference:** [e725d38e0faec05f7b8fb10644b616ef978d2f4d](https://github.com/timolins/react-hot-toast/commit/e725d38e0faec05f7b8fb10644b616ef978d2f4d)

**Tree at this commit:** [timolins/react-hot-toast@e725d38e0fae](https://github.com/timolins/react-hot-toast/tree/e725d38e0faec05f7b8fb10644b616ef978d2f4d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | timolins/react-hot-toast |
| Description | Smoking Hot React Notifications 🔥  |
| Stars | 10993 |
| Forks | 376 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `e725d38e0faec05f7b8fb10644b616ef978d2f4d` |
| Retrieved at | 2026-11-14T19:13:28.544588+00:00 |
| Files in this snapshot | 65 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    main.yml
    size.yml
.vscode/  (1 files)
  settings.json
assets/  (1 files)
  header.svg
site/  (38 files)
  assets/  (7 files)
    arrow.svg
    butter-1.svg
    butter-2.svg
    checkmark.svg
    github.svg
    logo-small.svg
    logo.svg
  components/  (7 files)
    sections/  (4 files)
      … 4 files under this directory
    code.tsx
    docs-layout.tsx
    emoji-button.tsx
  pages/  (11 files)
    docs/  (9 files)
      … 9 files under this directory
    _app.tsx
    index.tsx
  styles/  (3 files)
    main.css
    prism-theme.css
    tailwind-utils.css
  types/  (2 files)
    mdx.d.ts
    svg.d.ts
  .gitignore
  README.md
  next-env.d.ts
  next.config.mjs
  package.json
  postcss.config.js
  tailwind.config.js
  tsconfig.json
src/  (13 files)
  components/  (6 files)
    checkmark.tsx
    error.tsx
    loader.tsx
    toast-bar.tsx
    toast-icon.tsx
    toaster.tsx
  core/  (5 files)
    store.ts
    toast.ts
    types.ts
    use-toaster.ts
    utils.ts
  headless/  (1 files)
    index.ts
  index.ts
test/  (3 files)
  setup.ts
  store.test.tsx
  toast.test.tsx
.gitignore
LICENSE
README.md
jest.config.js
package.json
tsconfig.json
tsup.config.ts
```

## Entry points

- [site/pages/index.tsx](https://github.com/timolins/react-hot-toast/blob/e725d38e0faec05f7b8fb10644b616ef978d2f4d/site/pages/index.tsx)
- [src/headless/index.ts](https://github.com/timolins/react-hot-toast/blob/e725d38e0faec05f7b8fb10644b616ef978d2f4d/src/headless/index.ts)
- [src/index.ts](https://github.com/timolins/react-hot-toast/blob/e725d38e0faec05f7b8fb10644b616ef978d2f4d/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 6 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| headless package | library | Observed | Groups 1 file(s) under headless package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 15 file(s) under site package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/main.yml` (ci)
- `.github/workflows/size.yml` (ci)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `site/package.json` (manifest)
- `site/tsconfig.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `site` — 38 analysed file(s)
- `src` — 13 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `test` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e725d38e0faec05f7b8fb10644b616ef978d2f4d` is the revision these paths and observations refer to.
