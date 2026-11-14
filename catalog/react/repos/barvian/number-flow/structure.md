# Project structure: barvian/number-flow

**Analysed commit:** `c5906cf35c86583e756a6b91e043291c10b416e0`

**Commit reference:** [c5906cf35c86583e756a6b91e043291c10b416e0](https://github.com/barvian/number-flow/commit/c5906cf35c86583e756a6b91e043291c10b416e0)

**Tree at this commit:** [barvian/number-flow@c5906cf35c86](https://github.com/barvian/number-flow/tree/c5906cf35c86583e756a6b91e043291c10b416e0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | barvian/number-flow |
| Description | An animated number component for React, Vue, Svelte, and TS/JS. |
| Stars | 7809 |
| Forks | 164 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `c5906cf35c86583e756a6b91e043291c10b416e0` |
| Retrieved at | 2026-11-14T19:13:45.499680+00:00 |
| Files in this snapshot | 371 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    0-bug.yml
    1-docs.yml
    config.yml
  workflows/  (2 files)
    ci.yml
    release.yml
  FUNDING.yml
.vscode/  (1 files)
  settings.json
lib/  (1 files)
  playwright.ts
packages/  (130 files)
  number-flow/  (38 files)
    src/  (15 files)
      … 15 files under this directory
    test/  (17 files)
      … 17 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.mjs
  react/  (40 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (33 files)
      … 33 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
  svelte/  (27 files)
    src/  (17 files)
      … 17 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    package.json
    playwright.config.ts
    postcss.config.js
    svelte.config.js
    tailwind.config.ts
    tsconfig.json
    vite.config.ts
  vue/  (25 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (15 files)
      … 15 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
    vite.config.mjs
site/  (212 files)
  .vscode/  (2 files)
    extensions.json
    launch.json
  src/  (201 files)
    assets/  (22 files)
      … 22 files under this directory
    components/  (96 files)
      … 96 files under this directory
    context/  (1 files)
      … 1 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    layouts/  (3 files)
      … 3 files under this directory
    lib/  (6 files)
      … 6 files under this directory
    pages/  (68 files)
      … 68 files under this directory
    stores/  (1 files)
      … 1 files under this directory
    env.d.ts
    middleware.ts
    react.d.ts
  .gitignore
  astro.config.mjs
  blackout.json
  package.json
  postcss.config.cjs
  svelte.config.mjs
  tailwind.config.ts
  tsconfig.json
  whiteout.json
test-suites/  (9 files)
  wrapper/  (9 files)
    animated.test.ts
    can-animate.test.ts
    group-1-unchanged.test.ts
    hashes.test.ts
    nonce.test.ts
    parts.test.ts
    render.test.ts
    ssr.test.ts
    update.test.ts
.gitattributes
.gitignore
.prettierignore
LICENSE.md
README.md
package.json
pnpm-workspace.yaml
prettier.config.js
tsconfig.build.json
tsconfig.json
```

## Entry points

- [packages/number-flow/src/index.ts](https://github.com/barvian/number-flow/blob/c5906cf35c86583e756a6b91e043291c10b416e0/packages/number-flow/src/index.ts)
- [packages/react/src/index.tsx](https://github.com/barvian/number-flow/blob/c5906cf35c86583e756a6b91e043291c10b416e0/packages/react/src/index.tsx)
- [packages/vue/src/index.ts](https://github.com/barvian/number-flow/blob/c5906cf35c86583e756a6b91e043291c10b416e0/packages/vue/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 21 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 1 file(s) under lib package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 33 file(s) under packages package (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 85 file(s) under site package (observed from repository paths and static analysis). |
| test-suites package | library | Observed | Groups 9 file(s) under test-suites package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 65 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/0-bug.yml` (config)
- `.github/ISSUE_TEMPLATE/1-docs.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `packages/number-flow/package.json` (manifest)
- `packages/number-flow/tsconfig.build.json` (config)
- `packages/number-flow/tsconfig.json` (config)
- `packages/react/package.json` (manifest)
- `packages/react/tsconfig.build.json` (config)
- `packages/react/tsconfig.json` (config)
- `packages/svelte/package.json` (manifest)
- `packages/svelte/tsconfig.json` (config)
- `packages/vue/package.json` (manifest)
- `packages/vue/tsconfig.build.json` (config)
- `packages/vue/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `site/.vscode/extensions.json` (config)
- `site/.vscode/launch.json` (config)
- `site/blackout.json` (config)
- `site/package.json` (manifest)
- `site/tsconfig.json` (config)
- `site/whiteout.json` (config)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `site` — 212 analysed file(s)
- `packages` — 130 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `test-suites` — 9 analysed file(s)
- `.github` — 6 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `lib` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c5906cf35c86583e756a6b91e043291c10b416e0` is the revision these paths and observations refer to.
