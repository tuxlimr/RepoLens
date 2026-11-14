# Project structure: JCodesMore/ai-website-cloner-template

**Analysed commit:** `5426e0e2ec35dbc173a7a18f47a3dfe2a765313e`

**Commit reference:** [5426e0e2ec35dbc173a7a18f47a3dfe2a765313e](https://github.com/JCodesMore/ai-website-cloner-template/commit/5426e0e2ec35dbc173a7a18f47a3dfe2a765313e)

**Tree at this commit:** [JCodesMore/ai-website-cloner-template@5426e0e2ec35](https://github.com/JCodesMore/ai-website-cloner-template/tree/5426e0e2ec35dbc173a7a18f47a3dfe2a765313e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | JCodesMore/ai-website-cloner-template |
| Description | Clone any website with one command using AI coding agents |
| Stars | 39142 |
| Forks | 5818 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `5426e0e2ec35dbc173a7a18f47a3dfe2a765313e` |
| Retrieved at | 2026-11-14T19:13:00.109392+00:00 |
| Files in this snapshot | 44 |

## Directory tree

```text
.agents/  (3 files)
  skills/  (3 files)
    clone-website/  (3 files)
      … 3 files under this directory
.claude/  (1 files)
  commands/  (1 files)
    clone-website.md
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (2 files)
    ci.yml
    token-badge.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  copilot-setup-steps.yml
docs/  (1 files)
  design-references/  (1 files)
    .gitkeep
public/  (3 files)
  images/  (1 files)
    .gitkeep
  seo/  (1 files)
    .gitkeep
  videos/  (1 files)
    .gitkeep
scripts/  (1 files)
  .gitkeep
src/  (7 files)
  app/  (3 files)
    globals.css
    layout.tsx
    page.tsx
  components/  (1 files)
    ui/  (1 files)
      … 1 files under this directory
  hooks/  (1 files)
    .gitkeep
  lib/  (1 files)
    utils.ts
  types/  (1 files)
    .gitkeep
.dockerignore
.gitattributes
.gitignore
.nvmrc
AGENTS.md
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
Dockerfile
Dockerfile.dev
LICENSE
README.md
SECURITY.md
components.json
docker-compose.yml
eslint.config.mjs
next.config.ts
package.json
postcss.config.mjs
tsconfig.json
```

## Entry points

- [src/app/page.tsx](https://github.com/JCodesMore/ai-website-cloner-template/blob/5426e0e2ec35dbc173a7a18f47a3dfe2a765313e/src/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 2 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 1 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 1 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/copilot-setup-steps.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/token-badge.yml` (ci)
- `Dockerfile` (container)
- `Dockerfile.dev` (container)
- `components.json` (config)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 20 analysed file(s)
- `.github` — 8 analysed file(s)
- `src` — 7 analysed file(s)
- `.agents` — 3 analysed file(s)
- `public` — 3 analysed file(s)
- `.claude` — 1 analysed file(s)
- `docs` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5426e0e2ec35dbc173a7a18f47a3dfe2a765313e` is the revision these paths and observations refer to.
