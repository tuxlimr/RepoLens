# Project structure: pmndrs/zustand

**Analysed commit:** `9fed2eb2f3af672da9f7bf694b996df3831fc207`

**Commit reference:** [9fed2eb2f3af672da9f7bf694b996df3831fc207](https://github.com/pmndrs/zustand/commit/9fed2eb2f3af672da9f7bf694b996df3831fc207)

**Tree at this commit:** [pmndrs/zustand@9fed2eb2f3af](https://github.com/pmndrs/zustand/tree/9fed2eb2f3af672da9f7bf694b996df3831fc207)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pmndrs/zustand |
| Description | 🐻 Bear necessities for state management in React |
| Stars | 58924 |
| Forks | 2191 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `9fed2eb2f3af672da9f7bf694b996df3831fc207` |
| Retrieved at | 2026-11-14T19:12:57.140007+00:00 |
| Files in this snapshot | 131 |

## Directory tree

```text
.github/  (14 files)
  DISCUSSION_TEMPLATE/  (1 files)
    bug-report.yml
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (8 files)
    compressed-size.yml
    docs.yml
    preview-release.yml
    publish.yml
    test-multiple-builds.yml
    test-multiple-versions.yml
    test-old-typescript.yml
    test.yml
  FUNDING.yml
  dependabot.yml
  pull_request_template.md
docs/  (42 files)
  learn/  (21 files)
    getting-started/  (2 files)
      … 2 files under this directory
    guides/  (18 files)
      … 18 files under this directory
    index.md
  reference/  (20 files)
    apis/  (4 files)
      … 4 files under this directory
    hooks/  (3 files)
      … 3 files under this directory
    integrations/  (3 files)
      … 3 files under this directory
    middlewares/  (6 files)
      … 6 files under this directory
    migrations/  (2 files)
      … 2 files under this directory
    previous-versions/  (1 files)
      … 1 files under this directory
    index.md
  index.md
examples/  (31 files)
  demo/  (22 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (14 files)
      … 14 files under this directory
    .gitignore
    eslint.config.js
    index.html
    package.json
    vite.config.js
  starter/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
src/  (16 files)
  middleware/  (7 files)
    combine.ts
    devtools.ts
    immer.ts
    persist.ts
    redux.ts
    ssrSafe.ts
    subscribeWithSelector.ts
  react/  (1 files)
    shallow.ts
  vanilla/  (1 files)
    shallow.ts
  index.ts
  middleware.ts
  react.ts
  shallow.ts
  traditional.ts
  types.d.ts
  vanilla.ts
tests/  (16 files)
  vanilla/  (3 files)
    basic.test.ts
    shallow.test.tsx
    subscribe.test.tsx
  basic.test.tsx
  devtools.test.tsx
  immer.test.tsx
  middlewareTypes.test.tsx
  persistAsync.test.tsx
  persistPromiseLike.test.ts
  persistSync.test.tsx
  setup.ts
  shallow.test.tsx
  ssr.test.tsx
  subscribe.test.tsx
  test-utils.ts
  types.test.tsx
.gitignore
.prettierignore
CONTRIBUTING.md
FUNDING.json
LICENSE
README.md
eslint.config.mjs
package.json
pnpm-workspace.yaml
rollup.config.mjs
tsconfig.json
vitest.config.mts
```

## Entry points

- [src/index.ts](https://github.com/pmndrs/zustand/blob/9fed2eb2f3af672da9f7bf694b996df3831fc207/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| middleware package | library | Observed | Groups 7 file(s) under middleware package (observed from repository paths and static analysis). |
| middleware.ts package | library | Observed | Groups 1 file(s) under middleware.ts package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 1 file(s) under react package (observed from repository paths and static analysis). |
| react.ts package | library | Observed | Groups 1 file(s) under react.ts package (observed from repository paths and static analysis). |
| shallow.ts package | library | Observed | Groups 1 file(s) under shallow.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). |
| traditional.ts package | library | Observed | Groups 1 file(s) under traditional.ts package (observed from repository paths and static analysis). |
| types.d.ts package | library | Observed | Groups 1 file(s) under types.d.ts package (observed from repository paths and static analysis). |
| vanilla package | library | Observed | Groups 1 file(s) under vanilla package (observed from repository paths and static analysis). |
| vanilla.ts package | library | Observed | Groups 1 file(s) under vanilla.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/DISCUSSION_TEMPLATE/bug-report.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/compressed-size.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/preview-release.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test-multiple-builds.yml` (ci)
- `.github/workflows/test-multiple-versions.yml` (ci)
- `.github/workflows/test-old-typescript.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `FUNDING.json` (config)
- `examples/demo/package.json` (manifest)
- `examples/demo/public/manifest.json` (config)
- `examples/starter/package.json` (manifest)
- `examples/starter/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `docs` — 42 analysed file(s)
- `examples` — 31 analysed file(s)
- `src` — 16 analysed file(s)
- `tests` — 16 analysed file(s)
- `.github` — 14 analysed file(s)
- `(root files)` — 12 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9fed2eb2f3af672da9f7bf694b996df3831fc207` is the revision these paths and observations refer to.
