# Project structure: diegomura/react-pdf

**Analysed commit:** `f765c957902eb1f0d15b1571d6f61e5818e8bc50`

**Commit reference:** [f765c957902eb1f0d15b1571d6f61e5818e8bc50](https://github.com/diegomura/react-pdf/commit/f765c957902eb1f0d15b1571d6f61e5818e8bc50)

**Tree at this commit:** [diegomura/react-pdf@f765c957902e](https://github.com/diegomura/react-pdf/tree/f765c957902eb1f0d15b1571d6f61e5818e8bc50)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | diegomura/react-pdf |
| Description | 📄  Create PDF files using React |
| Stars | 16858 |
| Forks | 1348 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `f765c957902eb1f0d15b1571d6f61e5818e8bc50` |
| Retrieved at | 2026-11-14T19:13:15.074582+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    main.yml
    release.yml
    site.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  no-response.yml
.husky/  (1 files)
  pre-commit
apps/  (346 files)
  examples/  (65 files)
    public/  (8 files)
      … 8 files under this directory
    src/  (48 files)
      … 48 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    declarations.d.ts
    generate-pdfs.mjs
    package.json
    postcss.config.js
    tailwind.config.js
    vite.config.js
  site/  (281 files)
    app/  (23 files)
      … 23 files under this directory
    components/  (57 files)
      … 57 files under this directory
    content/  (130 files)
      … 130 files under this directory
    lib/  (61 files)
      … 61 files under this directory
    .gitignore
    AGENTS.md
    CLAUDE.md
    next.config.mjs
    package.json
    postcss.config.mjs
    source.config.ts
    tsconfig.json
    vercel.json
    vitest.config.ts
packages/  (429 files)
  fns/  (46 files)
    src/  (20 files)
      … 20 files under this directory
    tests/  (19 files)
      … 19 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    jest.config.js
    package.json
    rollup.config.js
    tsconfig.json
  font/  (18 files)
    src/  (6 files)
      … 6 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    declarations.d.ts
    globals.d.ts
    package.json
    rollup.config.js
    tsconfig.json
    vitest.config.js
  hyphenate/  (8 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
    rollup.config.js
    tsconfig.json
  image/  (22 files)
    src/  (7 files)
      … 7 files under this directory
    tests/  (5 files)
      … 5 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    declarations.d.ts
    globals.d.ts
    package.json
    rollup.config.js
    tsconfig.json
    vitest.config.js
    vitest.setup.js
  layout/  (199 files)
    src/  (129 files)
      … 129 files under this directory
    tests/  (61 files)
      … 61 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    globals.d.ts
    jest.config.js
    package.json
    rollup.config.js
    setupTests.js
    tsconfig.json
  math/  (15 files)
    src/  (4 files)
      … 4 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    package.json
    rollup.config.js
    tsconfig.json
    vitest.config.js
    vitest.polyfills.js
    vitest.setup.js
  mermaid/  (21 files)
    src/  (6 files)
      … 6 files under this directory
    tests/  (6 files)
      … 6 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    package.json
    rollup.config.js
    tsconfig.json
    vitest.config.js
    vitest.polyfills.js
    vitest.setup.js
  paginate/  (46 files)
    src/  (35 files)
      … 35 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    package.json
    rollup.config.js
    tsconfig.json
    vitest.config.js
    vitest.setup.js
  primitives/  (10 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    babel.config.js
    jest.config.js
    package.json
    rollup.config.js
    tsconfig.json
  reconciler/  (13 files)
    src/  (6 files)
      … 6 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    package.json
    rollup.config.js
    tsconfig.json
  render/  (31 files)
    src/  (24 files)
      … 24 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    globals.d.ts
    jest.config.js
    package.json
    rollup.config.js
.gitattributes
.gitignore
.nvmrc
.prettierignore
.prettierrc
CLAUDE.md
LICENSE
README.md
babel.config.js
eslint.config.ts
lerna.json
package.json
```

## Entry points

- [packages/fns/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/fns/src/index.ts)
- [packages/font/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/font/src/index.ts)
- [packages/hyphenate/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/hyphenate/src/index.ts)
- [packages/image/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/image/src/index.ts)
- [packages/layout/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/layout/src/index.ts)
- [packages/math/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/math/src/index.ts)
- [packages/mermaid/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/mermaid/src/index.ts)
- [packages/paginate/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/paginate/src/index.ts)
- [packages/primitives/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/primitives/src/index.ts)
- [packages/reconciler/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/reconciler/src/index.ts)
- [packages/render/src/index.ts](https://github.com/diegomura/react-pdf/blob/f765c957902eb1f0d15b1571d6f61e5818e8bc50/packages/render/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 188 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 31 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 274 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 102 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/no-response.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/site.yml` (ci)
- `apps/examples/package.json` (manifest)
- `apps/site/content/docs/v1/meta.json` (config)
- `apps/site/content/docs/v2/meta.json` (config)
- `apps/site/content/docs/v3/meta.json` (config)
- `apps/site/content/docs/v4/meta.json` (config)
- `apps/site/package.json` (manifest)
- `apps/site/tsconfig.json` (config)
- `apps/site/vercel.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/fns/package.json` (manifest)
- `packages/fns/tsconfig.json` (config)
- `packages/font/package.json` (manifest)
- `packages/font/tsconfig.json` (config)
- `packages/hyphenate/package.json` (manifest)
- `packages/hyphenate/tsconfig.json` (config)
- `packages/image/package.json` (manifest)
- `packages/image/tsconfig.json` (config)
- `packages/layout/package.json` (manifest)
- `packages/layout/tsconfig.json` (config)
- `packages/math/package.json` (manifest)
- `packages/math/tsconfig.json` (config)
- `packages/mermaid/package.json` (manifest)
- `packages/mermaid/tsconfig.json` (config)
- `packages/paginate/package.json` (manifest)
- `packages/paginate/tsconfig.json` (config)
- `packages/primitives/package.json` (manifest)
- `packages/primitives/tsconfig.json` (config)
- `packages/reconciler/package.json` (manifest)
- `packages/reconciler/tsconfig.json` (config)
- `packages/render/package.json` (manifest)

## Top-level layout

- `packages` — 429 analysed file(s)
- `apps` — 346 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 9 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f765c957902eb1f0d15b1571d6f61e5818e8bc50` is the revision these paths and observations refer to.
