# Project structure: 47ng/nuqs

**Analysed commit:** `149906a2a6388adf79e868786581eec9cfb16c00`

**Commit reference:** [149906a2a6388adf79e868786581eec9cfb16c00](https://github.com/47ng/nuqs/commit/149906a2a6388adf79e868786581eec9cfb16c00)

**Tree at this commit:** [47ng/nuqs@149906a2a638](https://github.com/47ng/nuqs/tree/149906a2a6388adf79e868786581eec9cfb16c00)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | 47ng/nuqs |
| Description | Type-safe search params state manager for React frameworks - Like useState, but stored in the URL query string. |
| Stars | 10907 |
| Forks | 298 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | next |
| Analysed commit | `149906a2a6388adf79e868786581eec9cfb16c00` |
| Retrieved at | 2026-11-14T19:13:29.818820+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.agents/  (7 files)
  docs/  (6 files)
    adapter-development.md
    api-design.md
    git-workflow.md
    parser-implementation.md
    quality-standards.md
    testing.md
  skills/  (1 files)
    bundle-size-bake-off/  (1 files)
      … 1 files under this directory
.github/  (17 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (13 files)
    analyse-nextjs-release.yml
    backlog-cleaner.yml
    ci-cd.yml
    mutation.yml
    pkg.pr.new.yml
    pr-lint.yml
    release-draft.yml
    release-edited.yml
    release-finalize.yml
    size-comment.yml
    size-compare.yml
    test-against-nextjs-pr.yml
    test-against-nextjs-release.yml
  FUNDING.yml
  dependabot.yml
.vscode/  (1 files)
  settings.json
errors/  (9 files)
  NUQS-101.md
  NUQS-303.md
  NUQS-404.md
  NUQS-409.md
  NUQS-414.md
  NUQS-422.md
  NUQS-429.md
  NUQS-500.md
  NUQS-501.md
packages/  (752 files)
  docs/  (286 files)
    content/  (45 files)
      … 45 files under this directory
    public/  (8 files)
      … 8 files under this directory
    src/  (219 files)
      … 219 files under this directory
    .env.example
    .gitignore
    CLAUDE.md
    README.md
    components.json
    mdx-components.tsx
    next.config.mjs
    package.json
    rehype-code.config.ts
    source.config.ts
    tsconfig.json
    turbo.json
    vercel-doctor.config.json
    vitest.config.ts
  e2e/  (466 files)
    next/  (242 files)
      … 242 files under this directory
    react-router/  (223 files)
      … 223 files under this directory
    package.json
.gitattributes
.gitconfig
.gitignore
.node-version
.npm-version
.prettierignore
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
knip.json
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 155 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 33 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 286 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/analyse-nextjs-release.yml` (ci)
- `.github/workflows/backlog-cleaner.yml` (ci)
- `.github/workflows/ci-cd.yml` (ci)
- `.github/workflows/mutation.yml` (ci)
- `.github/workflows/pkg.pr.new.yml` (ci)
- `.github/workflows/pr-lint.yml` (ci)
- `.github/workflows/release-draft.yml` (ci)
- `.github/workflows/release-edited.yml` (ci)
- `.github/workflows/release-finalize.yml` (ci)
- `.github/workflows/size-comment.yml` (ci)
- `.github/workflows/size-compare.yml` (ci)
- `.github/workflows/test-against-nextjs-pr.yml` (ci)
- `.github/workflows/test-against-nextjs-release.yml` (ci)
- `.vscode/settings.json` (config)
- `knip.json` (config)
- `package.json` (manifest)
- `packages/docs/.env.example` (config)
- `packages/docs/components.json` (config)
- `packages/docs/content/docs/meta.json` (config)
- `packages/docs/content/docs/parsers/community/meta.json` (config)
- `packages/docs/content/docs/parsers/meta.json` (config)
- `packages/docs/package.json` (manifest)
- `packages/docs/public/schemas/changelog-dto.v1.json` (config)
- `packages/docs/src/registry/items/adapter-inertia.json` (config)
- `packages/docs/src/registry/items/adapter-onejs.json` (config)
- `packages/docs/src/registry/items/adapter-react-router-v5.json` (config)
- `packages/docs/src/registry/items/adapter-waku.json` (config)
- `packages/docs/src/registry/items/next-typed-links.json` (config)
- `packages/docs/src/registry/items/parser-uuid.json` (config)
- `packages/docs/tsconfig.json` (config)
- `packages/docs/turbo.json` (config)
- `packages/docs/vercel-doctor.config.json` (config)
- `packages/e2e/next/package.json` (manifest)
- `packages/e2e/next/tsconfig.json` (config)
- `packages/e2e/next/turbo.json` (config)
- `packages/e2e/package.json` (manifest)
- `packages/e2e/react-router/package.json` (manifest)
- `packages/e2e/react-router/v5/package.json` (manifest)
- `packages/e2e/react-router/v5/tsconfig.app.json` (config)
- `packages/e2e/react-router/v5/tsconfig.json` (config)
- `packages/e2e/react-router/v5/tsconfig.node.json` (config)
- `packages/e2e/react-router/v5/turbo.json` (config)
- `packages/e2e/react-router/v6/package.json` (manifest)
- `packages/e2e/react-router/v6/tsconfig.app.json` (config)
- `packages/e2e/react-router/v6/tsconfig.json` (config)
- `packages/e2e/react-router/v6/tsconfig.node.json` (config)
- `packages/e2e/react-router/v6/turbo.json` (config)

## Top-level layout

- `packages` — 752 analysed file(s)
- `.github` — 17 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `errors` — 9 analysed file(s)
- `.agents` — 7 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `149906a2a6388adf79e868786581eec9cfb16c00` is the revision these paths and observations refer to.
