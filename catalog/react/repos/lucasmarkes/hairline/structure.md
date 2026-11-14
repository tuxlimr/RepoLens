# Project structure: lucasmarkes/hairline

**Analysed commit:** `034f4bf9902c6adcf3cf39d82f85e6010cb4e094`

**Commit reference:** [034f4bf9902c6adcf3cf39d82f85e6010cb4e094](https://github.com/lucasmarkes/hairline/commit/034f4bf9902c6adcf3cf39d82f85e6010cb4e094)

**Tree at this commit:** [lucasmarkes/hairline@034f4bf9902c](https://github.com/lucasmarkes/hairline/tree/034f4bf9902c6adcf3cf39d82f85e6010cb4e094)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lucasmarkes/hairline |
| Description | Isometric line figures that answer the pointer. For React and for anything with a DOM. |
| Stars | 3841 |
| Forks | 238 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `034f4bf9902c6adcf3cf39d82f85e6010cb4e094` |
| Retrieved at | 2026-11-14T19:15:03.446906+00:00 |
| Files in this snapshot | 208 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (3 files)
    ci.yml
    consumers.yml
    publish.yml
  FUNDING.yml
apps/  (67 files)
  site/  (67 files)
    .vitest/  (1 files)
      … 1 files under this directory
    app/  (12 files)
      … 12 files under this directory
    components/  (14 files)
      … 14 files under this directory
    lib/  (11 files)
      … 11 files under this directory
    public/  (13 files)
      … 13 files under this directory
    test/  (7 files)
      … 7 files under this directory
    .gitignore
    next.config.mjs
    package.json
    playwright.config.ts
    postcss.config.mjs
    tsconfig.json
    turbo.json
    vercel.json
    vitest.config.ts
fixtures/  (13 files)
  next-app/  (8 files)
    app/  (4 files)
      … 4 files under this directory
    .gitignore
    next.config.mjs
    package.json
    tsconfig.json
  vite-vanilla/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    index.html
    package.json
    tsconfig.json
packages/  (92 files)
  hairline/  (92 files)
    src/  (44 files)
      … 44 files under this directory
    test/  (43 files)
      … 43 files under this directory
    package.json
    playwright.config.ts
    tsconfig.json
    tsup.config.ts
    vitest.config.ts
registry/  (3 files)
  src/  (1 files)
    hairline.tsx
  build.mjs
  validate.mjs
scripts/  (6 files)
  base-url.mjs
  changelog.mjs
  consumers.mjs
  kernel.mjs
  og.mjs
  release.mjs
skills/  (14 files)
  hairline-adopt/  (1 files)
    SKILL.md
  hairline-create/  (13 files)
    examples/  (2 files)
      … 2 files under this directory
    SKILL.md
    bench.html
    build.mjs
    concepts.md
    kernel.js
    look.md
    look.mjs
    read.mjs
    rules.md
    source.md
    validate.mjs
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
package.json
pnpm-workspace.yaml
tsconfig.base.json
turbo.json
```

## Entry points

- [apps/site/app/page.tsx](https://github.com/lucasmarkes/hairline/blob/034f4bf9902c6adcf3cf39d82f85e6010cb4e094/apps/site/app/page.tsx)
- [fixtures/next-app/app/page.tsx](https://github.com/lucasmarkes/hairline/blob/034f4bf9902c6adcf3cf39d82f85e6010cb4e094/fixtures/next-app/app/page.tsx)
- [fixtures/vite-vanilla/src/main.ts](https://github.com/lucasmarkes/hairline/blob/034f4bf9902c6adcf3cf39d82f85e6010cb4e094/fixtures/vite-vanilla/src/main.ts)
- [packages/hairline/src/index.ts](https://github.com/lucasmarkes/hairline/blob/034f4bf9902c6adcf3cf39d82f85e6010cb4e094/packages/hairline/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 38 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| fixtures package | library | Observed | Groups 6 file(s) under fixtures package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 43 file(s) under packages package (observed from repository paths and static analysis). |
| registry package | library | Observed | Groups 3 file(s) under registry package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 7 file(s) under skills package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 50 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/consumers.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `apps/site/.vitest/json/output.json` (config)
- `apps/site/package.json` (manifest)
- `apps/site/tsconfig.json` (config)
- `apps/site/turbo.json` (config)
- `apps/site/vercel.json` (config)
- `fixtures/next-app/package.json` (manifest)
- `fixtures/next-app/tsconfig.json` (config)
- `fixtures/vite-vanilla/package.json` (manifest)
- `fixtures/vite-vanilla/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/hairline/package.json` (manifest)
- `packages/hairline/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.base.json` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 92 analysed file(s)
- `apps` — 67 analysed file(s)
- `skills` — 14 analysed file(s)
- `fixtures` — 13 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `registry` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `034f4bf9902c6adcf3cf39d82f85e6010cb4e094` is the revision these paths and observations refer to.
