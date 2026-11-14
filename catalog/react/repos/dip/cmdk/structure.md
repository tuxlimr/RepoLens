# Project structure: dip/cmdk

**Analysed commit:** `dd2250ed608443e8f32bafc5fa2d1d07a3746aa3`

**Commit reference:** [dd2250ed608443e8f32bafc5fa2d1d07a3746aa3](https://github.com/dip/cmdk/commit/dd2250ed608443e8f32bafc5fa2d1d07a3746aa3)

**Tree at this commit:** [dip/cmdk@dd2250ed6084](https://github.com/dip/cmdk/tree/dd2250ed608443e8f32bafc5fa2d1d07a3746aa3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dip/cmdk |
| Description | Fast, unstyled command menu React component. |
| Stars | 13147 |
| Forks | 383 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `dd2250ed608443e8f32bafc5fa2d1d07a3746aa3` |
| Retrieved at | 2026-11-14T19:13:19.443084+00:00 |
| Files in this snapshot | 70 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    test.yml
  FUNDING.yml
.husky/  (1 files)
  pre-commit
cmdk/  (4 files)
  src/  (2 files)
    command-score.ts
    index.tsx
  package.json
  tsup.config.ts
test/  (22 files)
  pages/  (11 files)
    _app.tsx
    dialog.tsx
    group.tsx
    huge.tsx
    index.tsx
    item-advanced.tsx
    item.tsx
    keybinds.tsx
    numeric.tsx
    portal.tsx
    props.tsx
  basic.test.ts
  dialog.test.ts
  group.test.ts
  item.test.ts
  keybind.test.ts
  next-env.d.ts
  numeric.test.ts
  package.json
  props.test.ts
  style.css
  tsconfig.json
website/  (31 files)
  components/  (9 files)
    cmdk/  (4 files)
      … 4 files under this directory
    code/  (2 files)
      … 2 files under this directory
    icons/  (2 files)
      … 2 files under this directory
    index.ts
  pages/  (3 files)
    _app.tsx
    _document.tsx
    index.tsx
  public/  (5 files)
    favicon.svg
    grid.svg
    line.svg
    robots.txt
    vercel.svg
  styles/  (6 files)
    cmdk/  (4 files)
      … 4 files under this directory
    globals.scss
    index.module.scss
  .eslintrc.json
  .gitignore
  README.md
  next-env.d.ts
  next.config.js
  package.json
  tsconfig.json
  vercel.json
.gitignore
.prettierignore
.prettierrc.js
ARCHITECTURE.md
LICENSE.md
README.md
package.json
playwright.config.ts
pnpm-workspace.yaml
tsconfig.json
```

## Entry points

- [cmdk/src/index.tsx](https://github.com/dip/cmdk/blob/dd2250ed608443e8f32bafc5fa2d1d07a3746aa3/cmdk/src/index.tsx)
- [website/components/code/index.tsx](https://github.com/dip/cmdk/blob/dd2250ed608443e8f32bafc5fa2d1d07a3746aa3/website/components/code/index.tsx)
- [website/components/icons/index.tsx](https://github.com/dip/cmdk/blob/dd2250ed608443e8f32bafc5fa2d1d07a3746aa3/website/components/icons/index.tsx)
- [website/components/index.ts](https://github.com/dip/cmdk/blob/dd2250ed608443e8f32bafc5fa2d1d07a3746aa3/website/components/index.ts)
- [website/pages/index.tsx](https://github.com/dip/cmdk/blob/dd2250ed608443e8f32bafc5fa2d1d07a3746aa3/website/pages/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cmdk package | library | Observed | Groups 3 file(s) under cmdk package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 12 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/test.yml` (ci)
- `cmdk/package.json` (manifest)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `website/.eslintrc.json` (config)
- `website/package.json` (manifest)
- `website/tsconfig.json` (config)
- `website/vercel.json` (config)

## Top-level layout

- `website` — 31 analysed file(s)
- `test` — 22 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `cmdk` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dd2250ed608443e8f32bafc5fa2d1d07a3746aa3` is the revision these paths and observations refer to.
