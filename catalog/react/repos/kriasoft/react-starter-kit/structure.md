# Project structure: kriasoft/react-starter-kit

**Analysed commit:** `dbdb0d4991bbaae1671ff62180089f2733dd406a`

**Commit reference:** [dbdb0d4991bbaae1671ff62180089f2733dd406a](https://github.com/kriasoft/react-starter-kit/commit/dbdb0d4991bbaae1671ff62180089f2733dd406a)

**Tree at this commit:** [kriasoft/react-starter-kit@dbdb0d4991bb](https://github.com/kriasoft/react-starter-kit/tree/dbdb0d4991bbaae1671ff62180089f2733dd406a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | kriasoft/react-starter-kit |
| Description | Modern React starter kit with Bun, TypeScript, Tailwind CSS, tRPC, Stripe, and Cloudflare Workers. Production-ready monorepo for building fast web apps. |
| Stars | 23717 |
| Forks | 4193 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `dbdb0d4991bbaae1671ff62180089f2733dd406a` |
| Retrieved at | 2026-11-14T19:13:06.679713+00:00 |
| Files in this snapshot | 312 |

## Directory tree

```text
.agents/  (14 files)
  skills/  (14 files)
    merge-seed/  (1 files)
      … 1 files under this directory
    shadcn/  (13 files)
      … 13 files under this directory
.claude/  (1 files)
  commands/  (1 files)
    validate-auth-schema.md
.gemini/  (1 files)
  settings.json
.github/  (10 files)
  workflows/  (4 files)
    ci.yml
    deploy.yml
    infra.yml
    pr-title.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  SECURITY.md
  copilot-instructions.md
  dependabot.yml
.husky/  (2 files)
  .gitignore
  pre-commit
.vscode/  (3 files)
  extensions.json
  mcp.json
  settings.json
apps/  (113 files)
  api/  (24 files)
    lib/  (10 files)
      … 10 files under this directory
    routers/  (3 files)
      … 3 files under this directory
    AGENTS.md
    CLAUDE.md
    Dockerfile
    README.md
    dev.ts
    index.ts
    package.json
    tsconfig.json
    vitest.config.ts
    worker.ts
    wrangler.jsonc
  app/  (57 files)
    components/  (15 files)
      … 15 files under this directory
    lib/  (18 files)
      … 18 files under this directory
    public/  (3 files)
      … 3 files under this directory
    routes/  (7 files)
      … 7 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    AGENTS.md
    CLAUDE.md
    README.md
    components.json
    global.d.ts
    index.html
    index.tsx
    package.json
    tailwind.config.css
    tsconfig.json
    vite.config.ts
    vitest.setup.ts
    wrangler.jsonc
  email/  (15 files)
    assets/  (1 files)
      … 1 files under this directory
    components/  (1 files)
      … 1 files under this directory
    emails/  (5 files)
      … 5 files under this directory
    templates/  (3 files)
      … 3 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    README.md
    index.ts
    package.json
    tsconfig.json
  web/  (17 files)
    layouts/  (1 files)
      … 1 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    public/  (3 files)
      … 3 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    .env.example
    README.md
    astro.config.mjs
    package.json
    tailwind.config.css
    tsconfig.json
    worker.ts
    wrangler.jsonc
db/  (29 files)
  backups/  (1 files)
    .gitignore
  migrations/  (3 files)
    meta/  (2 files)
      … 2 files under this directory
    0000_init.sql
  schema/  (8 files)
    id.ts
    index.test.ts
    index.ts
    invitation.ts
    organization.ts
    passkey.ts
    subscription.ts
    user.ts
  scripts/  (7 files)
    export.ts
    generate-auth-schema.ts
    grant-app-role.sql
    guard-push.ts
    local-database.test.ts
    local-database.ts
    seed.ts
  seeds/  (1 files)
    users.ts
  AGENTS.md
  CLAUDE.md
  README.md
  drizzle.config.ts
  index.ts
  package.json
  testing.ts
  tsconfig.json
  vitest.config.ts
docs/  (65 files)
  .vitepress/  (6 files)
    public/  (1 files)
      … 1 files under this directory
    theme/  (4 files)
      … 4 files under this directory
    config.ts
  adr/  (8 files)
    000-template.md
    001-auth-hint-cookie.md
    002-terraform-wrangler-boundary.md
    003-hcp-terraform-state.md
    004-typescript-7-native-compiler.md
    005-oxlint-oxfmt.md
    006-subpath-imports.md
    007-oxfmt-sorts-imports.md
  api/  (4 files)
    context.md
    index.md
    procedures.md
    validation-errors.md
  architecture/  (2 files)
    edge.md
    index.md
  auth/  (6 files)
    email-otp.md
    index.md
    organizations.md
    passkeys.md
    sessions.md
    social-providers.md
  billing/  (4 files)
    checkout.md
    index.md
    plans.md
    webhooks.md
  database/  (5 files)
    index.md
    migrations.md
    queries.md
    schema.md
    seeding.md
  deployment/  (5 files)
    ci-cd.md
    cloudflare.md
    index.md
    monitoring.md
    production-database.md
  frontend/  (4 files)
    forms.md
    routing.md
    state.md
    ui.md
  getting-started/  (4 files)
    environment-variables.md
    index.md
    project-structure.md
    quick-start.md
  public/  (1 files)
    CNAME
  recipes/  (6 files)
    file-uploads.md
    new-page.md
    new-procedure.md
    new-table.md
    teams.md
    websockets.md
  security/  (3 files)
    checklist.md
    incident-playbook.md
    policy-template.md
  specs/  (4 files)
    auth-form.md
    billing.md
    infra-terraform.md
    prefixed-ids.md
  email.md
  index.md
  testing.md
infra/  (11 files)
  envs/  (4 files)
    production/  (2 files)
      … 2 files under this directory
    staging/  (2 files)
      … 2 files under this directory
  modules/  (3 files)
    cloudflare/  (3 files)
      … 3 files under this directory
  .gitignore
  AGENTS.md
  CLAUDE.md
  README.md
packages/  (45 files)
  core/  (4 files)
    README.md
    index.ts
    package.json
    tsconfig.json
  typescript-config/  (6 files)
    README.md
    base.jsonc
    cloudflare.jsonc
    node.jsonc
    package.json
    react.jsonc
  ui/  (28 files)
    components/  (16 files)
      … 16 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    AGENTS.md
    CLAUDE.md
    README.md
    components.json
    index.ts
    package.json
    styles.css
    tsconfig.json
  ws-protocol/  (7 files)
    README.md
    example.ts
    index.ts
    messages.ts
    package.json
    router.ts
    tsconfig.json
scripts/  (5 files)
  deploy.ts
  mcp.ts
  package.json
  post-install.ts
  tsconfig.json
.editorconfig
.gitattributes
.gitignore
.oxfmtrc.json
.oxlintrc.json
AGENTS.md
CLAUDE.md
LICENSE
README.md
package.json
skills-lock.json
tsconfig.json
vitest.config.ts
```

## Entry points

- [packages/ui/index.ts](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/packages/ui/index.ts)
- [apps/api/index.ts](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/apps/api/index.ts)
- [apps/api/lib/app.ts](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/apps/api/lib/app.ts)
- [apps/app/index.tsx](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/apps/app/index.tsx)
- [apps/email/index.ts](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/apps/email/index.ts)
- [db/index.ts](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/db/index.ts)
- [db/schema/index.ts](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/db/schema/index.ts)
- [packages/core/index.ts](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/packages/core/index.ts)
- [packages/ws-protocol/index.ts](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/packages/ws-protocol/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 24 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 49 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 19 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 25 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.agents/skills/shadcn/agents/openai.yml` (config)
- `.agents/skills/shadcn/evals/evals.json` (config)
- `.editorconfig` (config)
- `.gemini/settings.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/infra.yml` (ci)
- `.github/workflows/pr-title.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/mcp.json` (config)
- `.vscode/settings.json` (config)
- `apps/api/Dockerfile` (container)
- `apps/api/package.json` (manifest)
- `apps/api/tsconfig.json` (config)
- `apps/app/components.json` (config)
- `apps/app/package.json` (manifest)
- `apps/app/tsconfig.json` (config)
- `apps/email/package.json` (manifest)
- `apps/email/tsconfig.json` (config)
- `apps/web/.env.example` (config)
- `apps/web/package.json` (manifest)
- `apps/web/tsconfig.json` (config)
- `db/migrations/meta/0000_snapshot.json` (config)
- `db/migrations/meta/_journal.json` (config)
- `db/package.json` (manifest)
- `db/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/typescript-config/package.json` (manifest)
- `packages/ui/components.json` (config)
- `packages/ui/package.json` (manifest)
- `packages/ui/tsconfig.json` (config)
- `packages/ws-protocol/package.json` (manifest)
- `packages/ws-protocol/tsconfig.json` (config)
- `scripts/package.json` (manifest)
- `scripts/tsconfig.json` (config)
- `skills-lock.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `apps` — 113 analysed file(s)
- `docs` — 65 analysed file(s)
- `packages` — 45 analysed file(s)
- `db` — 29 analysed file(s)
- `.agents` — 14 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `infra` — 11 analysed file(s)
- `.github` — 10 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.gemini` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dbdb0d4991bbaae1671ff62180089f2733dd406a` is the revision these paths and observations refer to.
