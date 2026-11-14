# Project structure: Kanaries/graphic-walker

**Analysed commit:** `a4b3bc1e87c059c220fa02633fd0207c01b5ad66`

**Commit reference:** [a4b3bc1e87c059c220fa02633fd0207c01b5ad66](https://github.com/Kanaries/graphic-walker/commit/a4b3bc1e87c059c220fa02633fd0207c01b5ad66)

**Tree at this commit:** [Kanaries/graphic-walker@a4b3bc1e87c0](https://github.com/Kanaries/graphic-walker/tree/a4b3bc1e87c059c220fa02633fd0207c01b5ad66)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Kanaries/graphic-walker |
| Description | An open source alternative to Tableau. Embeddable visual analytic |
| Stars | 3292 |
| Forks | 190 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `a4b3bc1e87c059c220fa02633fd0207c01b5ad66` |
| Retrieved at | 2026-11-14T19:15:25.992163+00:00 |
| Files in this snapshot | 527 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (4 files)
    auto-build.yml
    bump-version.yml
    release-duckdb.yml
    release.yml
docs/  (6 files)
  computation-divergences.md
  dsl-design-review.md
  explain-data-redesign.md
  explain-data-worklog.md
  handoff-playground-terse-examples.md
  terse-spec-design.md
packages/  (504 files)
  computation-conformance/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    jest.config.js
    package.json
    tsconfig.json
  duckdb-wasm-computation/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    package.json
    tsconfig.json
    vite.config.ts
  graphic-walker/  (365 files)
    public/  (1 files)
      … 1 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    src/  (319 files)
      … 319 files under this directory
    tests/  (29 files)
      … 29 files under this directory
    .gitignore
    .npmignore
    components.json
    index.html
    jest.config.js
    package.json
    playwright.config.ts
    postcss.config.js
    tailwind.config.js
    tsconfig.app-dist.json
    tsconfig.build.json
    tsconfig.json
    vite-app.config.ts
    vite.config.ts
  playground/  (85 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (70 files)
      … 70 files under this directory
    .eslintrc.cjs
    .gitignore
    README.md
    examples.html
    gallery.html
    index.html
    package.json
    postcss.config.js
    tailwind.config.js
    tsconfig.json
    tsconfig.node.json
    vercel.json
    vite.config.ts
  worksheet-renderer/  (33 files)
    src/  (17 files)
      … 17 files under this directory
    tests/  (14 files)
      … 14 files under this directory
    package.json
    tsconfig.json
  .npmignore
scripts/  (3 files)
  consumer-smoke-test.mjs
  demo-datasets.d.mts
  demo-datasets.mjs
.gitattributes
.gitignore
.npmignore
LICENSE
LICENSE2
README.ja-JP.md
README.md
README.zh-CN.md
computation.md
package.json
```

## Entry points

- [packages/duckdb-wasm-computation/src/index.ts](https://github.com/Kanaries/graphic-walker/blob/a4b3bc1e87c059c220fa02633fd0207c01b5ad66/packages/duckdb-wasm-computation/src/index.ts)
- [packages/graphic-walker/src/App.tsx](https://github.com/Kanaries/graphic-walker/blob/a4b3bc1e87c059c220fa02633fd0207c01b5ad66/packages/graphic-walker/src/App.tsx)
- [packages/graphic-walker/src/index.tsx](https://github.com/Kanaries/graphic-walker/blob/a4b3bc1e87c059c220fa02633fd0207c01b5ad66/packages/graphic-walker/src/index.tsx)
- [packages/graphic-walker/src/main.tsx](https://github.com/Kanaries/graphic-walker/blob/a4b3bc1e87c059c220fa02633fd0207c01b5ad66/packages/graphic-walker/src/main.tsx)
- [packages/playground/src/main.tsx](https://github.com/Kanaries/graphic-walker/blob/a4b3bc1e87c059c220fa02633fd0207c01b5ad66/packages/playground/src/main.tsx)
- [packages/worksheet-renderer/src/index.ts](https://github.com/Kanaries/graphic-walker/blob/a4b3bc1e87c059c220fa02633fd0207c01b5ad66/packages/worksheet-renderer/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 408 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 43 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/auto-build.yml` (ci)
- `.github/workflows/bump-version.yml` (ci)
- `.github/workflows/release-duckdb.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `package.json` (manifest)
- `packages/computation-conformance/package.json` (manifest)
- `packages/computation-conformance/tsconfig.json` (config)
- `packages/duckdb-wasm-computation/package.json` (manifest)
- `packages/duckdb-wasm-computation/tsconfig.json` (config)
- `packages/graphic-walker/components.json` (config)
- `packages/graphic-walker/package.json` (manifest)
- `packages/graphic-walker/public/tersespec_v1.json` (config)
- `packages/graphic-walker/src/locales/en-US.json` (config)
- `packages/graphic-walker/src/locales/ja-JP.json` (config)
- `packages/graphic-walker/src/locales/zh-CN.json` (config)
- `packages/graphic-walker/tsconfig.app-dist.json` (config)
- `packages/graphic-walker/tsconfig.build.json` (config)
- `packages/graphic-walker/tsconfig.json` (config)
- `packages/playground/package.json` (manifest)
- `packages/playground/public/tersespec_v1.json` (config)
- `packages/playground/src/examples/specs/student-chart-filter.json` (config)
- `packages/playground/src/examples/specs/student-chart.json` (config)
- `packages/playground/tsconfig.json` (config)
- `packages/playground/tsconfig.node.json` (config)
- `packages/playground/vercel.json` (config)
- `packages/worksheet-renderer/package.json` (manifest)
- `packages/worksheet-renderer/tsconfig.json` (config)

## Top-level layout

- `packages` — 504 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `docs` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `scripts` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x binary-looking content excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a4b3bc1e87c059c220fa02633fd0207c01b5ad66` is the revision these paths and observations refer to.
