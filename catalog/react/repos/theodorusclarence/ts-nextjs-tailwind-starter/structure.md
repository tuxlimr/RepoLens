# Project structure: theodorusclarence/ts-nextjs-tailwind-starter

**Analysed commit:** `749ead17ba98170f713da39de0e5b2306f7e86bf`

**Commit reference:** [749ead17ba98170f713da39de0e5b2306f7e86bf](https://github.com/theodorusclarence/ts-nextjs-tailwind-starter/commit/749ead17ba98170f713da39de0e5b2306f7e86bf)

**Tree at this commit:** [theodorusclarence/ts-nextjs-tailwind-starter@749ead17ba98](https://github.com/theodorusclarence/ts-nextjs-tailwind-starter/tree/749ead17ba98170f713da39de0e5b2306f7e86bf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | theodorusclarence/ts-nextjs-tailwind-starter |
| Description | 🔋 Next.js + Tailwind CSS + TypeScript starter and boilerplate packed with useful development features |
| Stars | 3405 |
| Forks | 607 |
| Licence | Not detected |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `749ead17ba98170f713da39de0e5b2306f7e86bf` |
| Retrieved at | 2026-11-14T19:15:19.921363+00:00 |
| Files in this snapshot | 65 |

## Directory tree

```text
.github/  (7 files)
  workflows/  (4 files)
    create-branch.yml
    issue-autolink.yml
    lint.yml
    release-please.yml
  FUNDING.yml
  issue-branch.yml
  pull_request_template.md
.husky/  (3 files)
  commit-msg
  post-merge
  pre-commit
.vscode/  (4 files)
  css.code-snippets
  extensions.json
  settings.json
  typescriptreact.code-snippets
public/  (3 files)
  favicon/  (1 files)
    site.webmanifest
  svg/  (2 files)
    Logo.svg
    Vercel.svg
src/  (30 files)
  __mocks__/  (1 files)
    svg.tsx
  __tests__/  (1 files)
    pages/  (1 files)
      … 1 files under this directory
  app/  (7 files)
    api/  (1 files)
      … 1 files under this directory
    components/  (2 files)
      … 2 files under this directory
    error.tsx
    layout.tsx
    not-found.tsx
    page.tsx
  components/  (11 files)
    buttons/  (3 files)
      … 3 files under this directory
    links/  (6 files)
      … 6 files under this directory
    NextImage.tsx
    Skeleton.tsx
  constant/  (2 files)
    config.ts
    env.ts
  lib/  (6 files)
    __tests__/  (1 files)
      … 1 files under this directory
    env.ts
    helper.ts
    logger.ts
    og.ts
    utils.ts
  styles/  (2 files)
    colors.css
    globals.css
.env.example
.gitignore
.nvmrc
.prettierignore
.prettierrc.js
CHANGELOG.md
README.md
commitlint.config.js
eslint.config.mjs
jest.config.js
jest.setup.js
next-sitemap.config.js
next.config.js
package.json
pnpm-workspace.yaml
postcss.config.js
tsconfig.json
vercel.json
```

## Entry points

- [src/app/components/page.tsx](https://github.com/theodorusclarence/ts-nextjs-tailwind-starter/blob/749ead17ba98170f713da39de0e5b2306f7e86bf/src/app/components/page.tsx)
- [src/app/page.tsx](https://github.com/theodorusclarence/ts-nextjs-tailwind-starter/blob/749ead17ba98170f713da39de0e5b2306f7e86bf/src/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 6 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 11 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constant package | library | Observed | Groups 2 file(s) under constant package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 6 file(s) under lib package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 1 file(s) under __tests__ package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/issue-branch.yml` (config)
- `.github/workflows/create-branch.yml` (ci)
- `.github/workflows/issue-autolink.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/release-please.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `src` — 30 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 7 analysed file(s)
- `.vscode` — 4 analysed file(s)
- `.husky` — 3 analysed file(s)
- `public` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `749ead17ba98170f713da39de0e5b2306f7e86bf` is the revision these paths and observations refer to.
