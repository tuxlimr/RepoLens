# Project structure: react-toolbox/react-toolbox

**Analysed commit:** `799da67838531b6ea35e464c4817edb189f925ca`

**Commit reference:** [799da67838531b6ea35e464c4817edb189f925ca](https://github.com/react-toolbox/react-toolbox/commit/799da67838531b6ea35e464c4817edb189f925ca)

**Tree at this commit:** [react-toolbox/react-toolbox@799da6783853](https://github.com/react-toolbox/react-toolbox/tree/799da67838531b6ea35e464c4817edb189f925ca)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-toolbox/react-toolbox |
| Description | A set of React components implementing Google's Material Design specification with the power of CSS Modules |
| Stars | 8603 |
| Forks | 972 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `799da67838531b6ea35e464c4817edb189f925ca` |
| Retrieved at | 2026-11-14T19:13:40.771110+00:00 |
| Files in this snapshot | 407 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    ci.yml
    release.yml
apps/  (84 files)
  docs/  (84 files)
    app/  (65 files)
      … 65 files under this directory
    public/  (1 files)
      … 1 files under this directory
    tests/  (9 files)
      … 9 files under this directory
    AGENTS.md
    README.md
    next-env.d.ts
    next.config.mjs
    package.json
    postcss.config.mjs
    styles.d.ts
    tsconfig.json
    vercel.json
docs/  (1 files)
  releases/  (1 files)
    3.0.0-next.0.md
packages/  (306 files)
  react-toolbox/  (306 files)
    scripts/  (10 files)
      … 10 files under this directory
    src/  (197 files)
      … 197 files under this directory
    tests/  (93 files)
      … 93 files under this directory
    LICENSE
    package.json
    registry.config.mjs
    tsconfig.json
    tsdown.config.ts
    vitest.config.ts
.editorconfig
.gitignore
.nvmrc
.vercelignore
AGENTS.md
CONTEXT.md
CONTRIBUTING.md
LICENSE
README.md
biome.json
package.json
playwright.config.js
pnpm-workspace.yaml
turbo.json
```

## Entry points

- [packages/react-toolbox/src/index.ts](https://github.com/react-toolbox/react-toolbox/blob/799da67838531b6ea35e464c4817edb189f925ca/packages/react-toolbox/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 169 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 102 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `apps/docs/package.json` (manifest)
- `apps/docs/tsconfig.json` (config)
- `apps/docs/vercel.json` (config)
- `biome.json` (config)
- `package.json` (manifest)
- `packages/react-toolbox/package.json` (manifest)
- `packages/react-toolbox/scripts/footprint-budgets.json` (config)
- `packages/react-toolbox/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 306 analysed file(s)
- `apps` — 84 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 2 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `799da67838531b6ea35e464c4817edb189f925ca` is the revision these paths and observations refer to.
