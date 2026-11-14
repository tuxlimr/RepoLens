# Project structure: jaredpalmer/tsdx

**Analysed commit:** `5b1aa0d67788bfb5ae46e6845e2e4e07c1c73e99`

**Commit reference:** [5b1aa0d67788bfb5ae46e6845e2e4e07c1c73e99](https://github.com/jaredpalmer/tsdx/commit/5b1aa0d67788bfb5ae46e6845e2e4e07c1c73e99)

**Tree at this commit:** [jaredpalmer/tsdx@5b1aa0d67788](https://github.com/jaredpalmer/tsdx/tree/5b1aa0d67788bfb5ae46e6845e2e4e07c1c73e99)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jaredpalmer/tsdx |
| Description | Zero-config CLI for TypeScript package development |
| Stars | 11464 |
| Forks | 490 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `5b1aa0d67788bfb5ae46e6845e2e4e07c1c73e99` |
| Retrieved at | 2026-11-14T19:13:25.266076+00:00 |
| Files in this snapshot | 78 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (2 files)
    nodejs.yml
    release.yml
  dependabot.yml
  stale.yml
src/  (1 files)
  index.ts
templates/  (25 files)
  basic/  (10 files)
    .github/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
    gitignore
    package.json
    tsconfig.json
    vitest.config.ts
  react/  (15 files)
    .github/  (2 files)
      … 2 files under this directory
    example/  (5 files)
      … 5 files under this directory
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
    gitignore
    package.json
    tsconfig.json
    vitest.config.ts
test/  (2 files)
  cli.test.ts
  e2e.test.ts
website/  (29 files)
  app/  (7 files)
    (home)/  (2 files)
      … 2 files under this directory
    docs/  (2 files)
      … 2 files under this directory
    global.css
    layout.config.tsx
    layout.tsx
  content/  (9 files)
    docs/  (9 files)
      … 9 files under this directory
  lib/  (1 files)
    source.ts
  public/  (3 files)
    favicon/  (1 files)
      … 1 files under this directory
    bg.svg
    logo.svg
  .gitignore
  bun.lock
  mdx-components.tsx
  next.config.mjs
  package.json
  postcss.config.js
  source.config.ts
  tsconfig.json
  vercel.json
.gitignore
CHANGELOG.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MIGRATION.md
README.md
bun.lock
package.json
tsconfig.json
vitest.config.ts
```

## Entry points

- [src/index.ts](https://github.com/jaredpalmer/tsdx/blob/5b1aa0d67788bfb5ae46e6845e2e4e07c1c73e99/src/index.ts)
- [templates/basic/src/index.ts](https://github.com/jaredpalmer/tsdx/blob/5b1aa0d67788bfb5ae46e6845e2e4e07c1c73e99/templates/basic/src/index.ts)
- [templates/react/src/index.tsx](https://github.com/jaredpalmer/tsdx/blob/5b1aa0d67788bfb5ae46e6845e2e4e07c1c73e99/templates/react/src/index.tsx)
- [website/app/(home)/page.tsx](https://github.com/jaredpalmer/tsdx/blob/5b1aa0d67788bfb5ae46e6845e2e4e07c1c73e99/website/app/%28home%29/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 6 file(s) under templates package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 9 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/nodejs.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `package.json` (manifest)
- `templates/basic/.github/workflows/main.yml` (ci)
- `templates/basic/.github/workflows/size.yml` (ci)
- `templates/basic/package.json` (manifest)
- `templates/basic/tsconfig.json` (config)
- `templates/react/.github/workflows/main.yml` (ci)
- `templates/react/.github/workflows/size.yml` (ci)
- `templates/react/example/package.json` (manifest)
- `templates/react/example/tsconfig.json` (config)
- `templates/react/package.json` (manifest)
- `templates/react/tsconfig.json` (config)
- `tsconfig.json` (config)
- `website/content/docs/meta.json` (config)
- `website/package.json` (manifest)
- `website/tsconfig.json` (config)
- `website/vercel.json` (config)

## Top-level layout

- `website` — 29 analysed file(s)
- `templates` — 25 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 7 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `test` — 2 analysed file(s)
- `src` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5b1aa0d67788bfb5ae46e6845e2e4e07c1c73e99` is the revision these paths and observations refer to.
