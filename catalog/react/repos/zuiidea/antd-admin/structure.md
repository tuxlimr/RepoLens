# Project structure: zuiidea/antd-admin

**Analysed commit:** `4dc473ba55635e73b642f7de71a3ac0aa58a7bd6`

**Commit reference:** [4dc473ba55635e73b642f7de71a3ac0aa58a7bd6](https://github.com/zuiidea/antd-admin/commit/4dc473ba55635e73b642f7de71a3ac0aa58a7bd6)

**Tree at this commit:** [zuiidea/antd-admin@4dc473ba5563](https://github.com/zuiidea/antd-admin/tree/4dc473ba55635e73b642f7de71a3ac0aa58a7bd6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zuiidea/antd-admin |
| Description | AI-friendly enterprise front-end best practices |
| Stars | 9769 |
| Forks | 2465 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `4dc473ba55635e73b642f7de71a3ac0aa58a7bd6` |
| Retrieved at | 2026-11-14T19:13:33.048806+00:00 |
| Files in this snapshot | 317 |

## Directory tree

```text
.cursor/  (1 files)
  rules/  (1 files)
    english-only-comments.md
.githooks/  (2 files)
  README.md
  pre-commit
.github/  (2 files)
  workflows/  (2 files)
    publish-init-antd-admin.yml
    with-lingui-ci.yml
apps/  (271 files)
  basic/  (92 files)
    .agents/  (1 files)
      … 1 files under this directory
    .vite-hooks/  (1 files)
      … 1 files under this directory
    e2e/  (6 files)
      … 6 files under this directory
    public/  (2 files)
      … 2 files under this directory
    src/  (72 files)
      … 72 files under this directory
    .gitignore
    AGENTS.md
    README.md
    index.html
    package.json
    playwright.config.ts
    tsconfig.json
    vercel.json
    vite.config.ts
    vitest.config.ts
  docs/  (82 files)
    app/  (3 files)
      … 3 files under this directory
    content/  (70 files)
      … 70 files under this directory
    .gitignore
    README.md
    eslint.config.mjs
    mdx-components.tsx
    next-env.d.ts
    next.config.mjs
    package.json
    proxy.ts
    tsconfig.json
  with-lingui/  (97 files)
    .agents/  (1 files)
      … 1 files under this directory
    .vite-hooks/  (1 files)
      … 1 files under this directory
    e2e/  (6 files)
      … 6 files under this directory
    public/  (2 files)
      … 2 files under this directory
    src/  (76 files)
      … 76 files under this directory
    .gitignore
    AGENTS.md
    README.md
    index.html
    lingui.config.ts
    package.json
    playwright.config.ts
    tsconfig.json
    vercel.json
    vite.config.ts
    vitest.config.ts
docs/  (7 files)
  specs/  (5 files)
    2026-04-14-create-antd-admin-design.md
    2026-04-14-create-antd-admin-plan.md
    2026-04-15-apps-docs-nextra-design.md
    2026-04-15-apps-docs-nextra-plan.md
    2026-04-24-with-lingui-optimization-plan.md
  superpowers/  (2 files)
    plans/  (1 files)
      … 1 files under this directory
    specs/  (1 files)
      … 1 files under this directory
packages/  (27 files)
  create/  (27 files)
    fixtures/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (20 files)
      … 20 files under this directory
    README.md
    package.json
    tsconfig.json
    tsup.config.ts
    vitest.config.ts
.gitignore
AGENTS.md
LICENSE
README.md
package.json
pnpm-workspace.yaml
turbo.json
```

## Entry points

- [apps/basic/src/main.tsx](https://github.com/zuiidea/antd-admin/blob/4dc473ba55635e73b642f7de71a3ac0aa58a7bd6/apps/basic/src/main.tsx)
- [apps/with-lingui/src/main.tsx](https://github.com/zuiidea/antd-admin/blob/4dc473ba55635e73b642f7de71a3ac0aa58a7bd6/apps/with-lingui/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 54 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 99 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 22 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/publish-init-antd-admin.yml` (ci)
- `.github/workflows/with-lingui-ci.yml` (ci)
- `apps/basic/package.json` (manifest)
- `apps/basic/tsconfig.json` (config)
- `apps/basic/vercel.json` (config)
- `apps/docs/package.json` (manifest)
- `apps/docs/tsconfig.json` (config)
- `apps/with-lingui/package.json` (manifest)
- `apps/with-lingui/tsconfig.json` (config)
- `apps/with-lingui/vercel.json` (config)
- `package.json` (manifest)
- `packages/create/fixtures/minimal-app/package.json` (manifest)
- `packages/create/package.json` (manifest)
- `packages/create/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `turbo.json` (config)

## Top-level layout

- `apps` — 271 analysed file(s)
- `packages` — 27 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `docs` — 7 analysed file(s)
- `.githooks` — 2 analysed file(s)
- `.github` — 2 analysed file(s)
- `.cursor` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4dc473ba55635e73b642f7de71a3ac0aa58a7bd6` is the revision these paths and observations refer to.
