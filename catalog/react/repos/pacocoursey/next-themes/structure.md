# Project structure: pacocoursey/next-themes

**Analysed commit:** `a7eeabc39cfb37d74ea3d82eac674d0e1851b1cb`

**Commit reference:** [a7eeabc39cfb37d74ea3d82eac674d0e1851b1cb](https://github.com/pacocoursey/next-themes/commit/a7eeabc39cfb37d74ea3d82eac674d0e1851b1cb)

**Tree at this commit:** [pacocoursey/next-themes@a7eeabc39cfb](https://github.com/pacocoursey/next-themes/tree/a7eeabc39cfb37d74ea3d82eac674d0e1851b1cb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pacocoursey/next-themes |
| Description | Perfect Next.js dark mode in 2 lines of code. Support System preference and any other theme with no flashing |
| Stars | 6354 |
| Forks | 253 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `a7eeabc39cfb37d74ea3d82eac674d0e1851b1cb` |
| Retrieved at | 2026-11-14T19:14:07.964976+00:00 |
| Files in this snapshot | 64 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    1-bug-report.yaml
    2-feature-request.yaml
  workflows/  (2 files)
    e2e.yml
    test.yml
  FUNDING.yml
examples/  (37 files)
  example/  (7 files)
    pages/  (4 files)
      … 4 files under this directory
    .gitignore
    package.json
    styles.css
  multi-theme/  (12 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    next.config.js
    package.json
    postcss.config.js
    tailwind.config.ts
    tsconfig.json
  tailwind/  (8 files)
    pages/  (3 files)
      … 3 files under this directory
    .gitignore
    package.json
    postcss.config.js
    styles.css
    tailwind.config.js
  with-app-dir/  (10 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
    postcss.config.js
    tailwind.config.ts
    tsconfig.json
next-themes/  (9 files)
  __tests__/  (1 files)
    index.test.tsx
  src/  (3 files)
    index.tsx
    script.ts
    types.ts
  README.md
  license.md
  package.json
  tsconfig.json
  tsup.config.ts
test/  (5 files)
  forced-theme.test.ts
  storage-event.test.ts
  switch-theme.test.ts
  system-theme.test.ts
  util.ts
.gitignore
.prettierignore
.prettierrc
license.md
package.json
playwright.config.ts
pnpm-workspace.yaml
turbo.json
```

## Entry points

- [next-themes/src/index.tsx](https://github.com/pacocoursey/next-themes/blob/a7eeabc39cfb37d74ea3d82eac674d0e1851b1cb/next-themes/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| next-themes package | library | Observed | Groups 5 file(s) under next-themes package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/1-bug-report.yaml` (config)
- `.github/ISSUE_TEMPLATE/2-feature-request.yaml` (config)
- `.github/workflows/e2e.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `examples/example/package.json` (manifest)
- `examples/multi-theme/package.json` (manifest)
- `examples/multi-theme/tsconfig.json` (config)
- `examples/tailwind/package.json` (manifest)
- `examples/with-app-dir/package.json` (manifest)
- `examples/with-app-dir/tsconfig.json` (config)
- `next-themes/package.json` (manifest)
- `next-themes/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `turbo.json` (config)

## Top-level layout

- `examples` — 37 analysed file(s)
- `next-themes` — 9 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 5 analysed file(s)
- `test` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a7eeabc39cfb37d74ea3d82eac674d0e1851b1cb` is the revision these paths and observations refer to.
