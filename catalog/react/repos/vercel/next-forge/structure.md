# Project structure: vercel/next-forge

**Analysed commit:** `f189de79ceef7c1ef69f61f12e272f99b4cdb699`

**Commit reference:** [f189de79ceef7c1ef69f61f12e272f99b4cdb699](https://github.com/vercel/next-forge/commit/f189de79ceef7c1ef69f61f12e272f99b4cdb699)

**Tree at this commit:** [vercel/next-forge@f189de79ceef](https://github.com/vercel/next-forge/tree/f189de79ceef7c1ef69f61f12e272f99b4cdb699)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vercel/next-forge |
| Description | Production-grade Turborepo template for Next.js apps. |
| Stars | 7778 |
| Forks | 736 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `f189de79ceef7c1ef69f61f12e272f99b4cdb699` |
| Retrieved at | 2026-11-14T19:13:46.281321+00:00 |
| Files in this snapshot | 647 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    release.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  SECURITY.md
  copilot-instructions.md.example
  dependabot.yml
  pull_request_template.md
.vscode/  (3 files)
  extensions.json
  launch.json
  settings.json
apps/  (181 files)
  api/  (20 files)
    __tests__/  (1 files)
      … 1 files under this directory
    app/  (6 files)
      … 6 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    .env.example
    .gitignore
    env.ts
    instrumentation-client.ts
    instrumentation.ts
    next.config.ts
    package.json
    sentry.edge.config.ts
    sentry.server.config.ts
    tsconfig.json
    vercel.json
    vitest.config.mts
  app/  (39 files)
    __tests__/  (2 files)
      … 2 files under this directory
    app/  (21 files)
      … 21 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    .env.example
    .gitignore
    env.ts
    instrumentation-client.ts
    instrumentation.ts
    liveblocks.config.ts
    next.config.ts
    package.json
    postcss.config.mjs
    proxy.ts
    sentry.edge.config.ts
    sentry.server.config.ts
    tsconfig.json
    vercel.json
    vitest.config.mts
  docs/  (22 files)
    api-reference/  (5 files)
      … 5 files under this directory
    essentials/  (6 files)
      … 6 files under this directory
    images/  (2 files)
      … 2 files under this directory
    logo/  (2 files)
      … 2 files under this directory
    snippets/  (1 files)
      … 1 files under this directory
    development.mdx
    favicon.svg
    introduction.mdx
    mint.json
    package.json
    quickstart.mdx
  email/  (2 files)
    package.json
    tsconfig.json
  storybook/  (56 files)
    .storybook/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    stories/  (46 files)
      … 46 files under this directory
    README.md
    next.config.ts
    package.json
    postcss.config.mjs
    tsconfig.json
    vercel.json
  studio/  (2 files)
    package.json
    tsconfig.json
  web/  (40 files)
    app/  (25 files)
      … 25 files under this directory
    components/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    .env.example
    .gitignore
    env.ts
    instrumentation-client.ts
    instrumentation.ts
    next.config.ts
    package.json
    postcss.config.mjs
    proxy.ts
    sentry.edge.config.ts
    sentry.server.config.ts
    tsconfig.json
    vercel.json
docs/  (233 files)
  app/  (52 files)
    [lang]/  (41 files)
      … 41 files under this directory
    actions/  (2 files)
      … 2 files under this directory
    api/  (5 files)
      … 5 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    global.css
    robots.ts
    sitemap.ts
  components/  (63 files)
    ai-elements/  (8 files)
      … 8 files under this directory
    geistdocs/  (31 files)
      … 31 files under this directory
    ui/  (23 files)
      … 23 files under this directory
    vercel.tsx
  content/  (97 files)
    docs/  (97 files)
      … 97 files under this directory
  hooks/  (3 files)
    geistdocs/  (2 files)
      … 2 files under this directory
    use-mobile.ts
  lib/  (6 files)
    geistdocs/  (5 files)
      … 5 files under this directory
    utils.ts
  .env.example
  .gitignore
  README.md
  components.json
  geistdocs.tsx
  next.config.ts
  package.json
  postcss.config.mjs
  proxy.ts
  source.config.ts
  tsconfig.json
  turbo.json
packages/  (197 files)
  ai/  (8 files)
    components/  (2 files)
      … 2 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    index.ts
    keys.ts
    package.json
    tsconfig.json
  analytics/  (7 files)
    index.ts
    instrumentation-client.ts
    keys.ts
    package.json
    provider.tsx
    server.ts
    tsconfig.json
  auth/  (9 files)
    components/  (2 files)
      … 2 files under this directory
    client.ts
    keys.ts
    package.json
    provider.tsx
    proxy.ts
    server.ts
    tsconfig.json
  cms/  (15 files)
    components/  (6 files)
      … 6 files under this directory
    .env.example
    basehub-types.d.ts
    basehub.config.ts
    index.ts
    keys.ts
    next-config.ts
    package.json
    tsconfig.json
    typescript-config.json
  collaboration/  (7 files)
    auth.ts
    config.ts
    hooks.ts
    keys.ts
    package.json
    room.tsx
    tsconfig.json
  database/  (7 files)
    prisma/  (1 files)
      … 1 files under this directory
    .env.example
    index.ts
    keys.ts
    package.json
    prisma.config.ts
    tsconfig.json
  design-system/  (64 files)
    components/  (54 files)
      … 54 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    providers/  (1 files)
      … 1 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    components.json
    index.tsx
    package.json
    postcss.config.mjs
    tsconfig.json
  email/  (5 files)
    templates/  (1 files)
      … 1 files under this directory
    index.ts
    keys.ts
    package.json
    tsconfig.json
  feature-flags/  (8 files)
    components/  (1 files)
      … 1 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    access.ts
    index.ts
    keys.ts
    package.json
    tsconfig.json
  internationalization/  (13 files)
    dictionaries/  (6 files)
      … 6 files under this directory
    .env.example
    index.ts
    languine.json
    languine.lock
    package.json
    proxy.ts
    tsconfig.json
  next-config/  (4 files)
    index.ts
    keys.ts
    package.json
    tsconfig.json
  notifications/  (7 files)
    components/  (2 files)
      … 2 files under this directory
    index.ts
    keys.ts
    package.json
    styles.css
    tsconfig.json
  observability/  (12 files)
    status/  (2 files)
      … 2 files under this directory
    client.ts
    edge.ts
    error.ts
    instrumentation.ts
    keys.ts
    log.ts
    next-config.ts
    package.json
    server.ts
    tsconfig.json
  payments/  (5 files)
    ai.ts
    index.ts
    keys.ts
    package.json
    tsconfig.json
  rate-limit/  (3 files)
    index.ts
    keys.ts
    package.json
  security/  (5 files)
    index.ts
    keys.ts
    package.json
    proxy.ts
    tsconfig.json
  seo/  (4 files)
    json-ld.tsx
    metadata.ts
    package.json
    tsconfig.json
  storage/  (5 files)
    client.ts
    index.ts
    keys.ts
    package.json
    tsconfig.json
  typescript-config/  (4 files)
    base.json
    nextjs.json
    package.json
    react-library.json
  webhooks/  (5 files)
    lib/  (1 files)
      … 1 files under this directory
    index.ts
    keys.ts
    package.json
    tsconfig.json
scripts/  (4 files)
  index.ts
  initialize.ts
  update.ts
  utils.ts
skills/  (5 files)
  next-forge/  (5 files)
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
turbo/  (4 files)
  generators/  (4 files)
    templates/  (2 files)
      … 2 files under this directory
    config.ts
    package.json
.autorc
.cursorrules.example
.gitignore
CHANGELOG.md
README.md
biome.jsonc
license.md
package.json
tsconfig.json
tsup.config.ts
turbo.json
```

## Entry points

- [packages/database/index.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/database/index.ts)
- [apps/storybook/.storybook/main.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/apps/storybook/.storybook/main.ts)
- [packages/ai/index.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/ai/index.ts)
- [packages/analytics/index.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/analytics/index.ts)
- [packages/analytics/server.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/analytics/server.ts)
- [packages/auth/server.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/auth/server.ts)
- [packages/cms/index.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/cms/index.ts)
- [packages/design-system/index.tsx](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/design-system/index.tsx)
- [packages/email/index.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/email/index.ts)
- [packages/feature-flags/index.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/feature-flags/index.ts)
- [packages/internationalization/index.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/internationalization/index.ts)
- [packages/next-config/index.ts](https://github.com/vercel/next-forge/blob/f189de79ceef7c1ef69f61f12e272f99b4cdb699/packages/next-config/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 15 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 116 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 79 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 6 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 134 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| turbo package | library | Observed | Groups 1 file(s) under turbo package (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `apps/api/.env.example` (config)
- `apps/api/package.json` (manifest)
- `apps/api/tsconfig.json` (config)
- `apps/api/vercel.json` (config)
- `apps/app/.env.example` (config)
- `apps/app/package.json` (manifest)
- `apps/app/tsconfig.json` (config)
- `apps/app/vercel.json` (config)
- `apps/docs/api-reference/openapi.json` (config)
- `apps/docs/mint.json` (config)
- `apps/docs/package.json` (manifest)
- `apps/email/package.json` (manifest)
- `apps/email/tsconfig.json` (config)
- `apps/storybook/package.json` (manifest)
- `apps/storybook/tsconfig.json` (config)
- `apps/storybook/vercel.json` (config)
- `apps/studio/package.json` (manifest)
- `apps/studio/tsconfig.json` (config)
- `apps/web/.env.example` (config)
- `apps/web/package.json` (manifest)
- `apps/web/tsconfig.json` (config)
- `apps/web/vercel.json` (config)
- `docs/.env.example` (config)
- `docs/components.json` (config)
- `docs/content/docs/meta.json` (config)
- `docs/content/docs/packages/cms/meta.json` (config)
- `docs/content/docs/packages/design-system/meta.json` (config)
- `docs/content/docs/packages/meta.json` (config)
- `docs/content/docs/packages/next-config/meta.json` (config)
- `docs/content/docs/packages/seo/meta.json` (config)
- `docs/content/docs/setup/meta.json` (config)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `docs/turbo.json` (config)
- `package.json` (manifest)
- `packages/ai/package.json` (manifest)
- `packages/ai/tsconfig.json` (config)
- `packages/analytics/package.json` (manifest)
- `packages/analytics/tsconfig.json` (config)
- `packages/auth/package.json` (manifest)
- `packages/auth/tsconfig.json` (config)
- `packages/cms/.env.example` (config)
- `packages/cms/package.json` (manifest)
- `packages/cms/tsconfig.json` (config)
- `packages/cms/typescript-config.json` (config)
- `packages/collaboration/package.json` (manifest)
- `packages/collaboration/tsconfig.json` (config)
- `packages/database/.env.example` (config)
- `packages/database/package.json` (manifest)
- `packages/database/tsconfig.json` (config)
- `packages/design-system/components.json` (config)
- `packages/design-system/package.json` (manifest)
- `packages/design-system/tsconfig.json` (config)
- `packages/email/package.json` (manifest)
- `packages/email/tsconfig.json` (config)
- `packages/feature-flags/package.json` (manifest)
- `packages/feature-flags/tsconfig.json` (config)
- `packages/internationalization/.env.example` (config)
- `packages/internationalization/dictionaries/de.json` (config)
- `packages/internationalization/dictionaries/en.json` (config)
- `packages/internationalization/dictionaries/es.json` (config)
- `packages/internationalization/dictionaries/fr.json` (config)
- `packages/internationalization/dictionaries/pt.json` (config)
- `packages/internationalization/dictionaries/zh.json` (config)
- `packages/internationalization/languine.json` (config)
- `packages/internationalization/package.json` (manifest)
- `packages/internationalization/tsconfig.json` (config)
- `packages/next-config/package.json` (manifest)
- `packages/next-config/tsconfig.json` (config)
- `packages/notifications/package.json` (manifest)
- `packages/notifications/tsconfig.json` (config)
- `packages/observability/package.json` (manifest)
- `packages/observability/tsconfig.json` (config)
- `packages/payments/package.json` (manifest)
- `packages/payments/tsconfig.json` (config)
- `packages/rate-limit/package.json` (manifest)
- `packages/security/package.json` (manifest)
- `packages/security/tsconfig.json` (config)
- `packages/seo/package.json` (manifest)
- `packages/seo/tsconfig.json` (config)
- `packages/storage/package.json` (manifest)
- `packages/storage/tsconfig.json` (config)
- `packages/typescript-config/base.json` (config)
- `packages/typescript-config/nextjs.json` (config)
- `packages/typescript-config/package.json` (manifest)
- `packages/typescript-config/react-library.json` (config)
- `packages/webhooks/package.json` (manifest)
- `packages/webhooks/tsconfig.json` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)
- `turbo/generators/package.json` (manifest)

## Top-level layout

- `docs` — 233 analysed file(s)
- `packages` — 197 analysed file(s)
- `apps` — 181 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 9 analysed file(s)
- `skills` — 5 analysed file(s)
- `scripts` — 4 analysed file(s)
- `turbo` — 4 analysed file(s)
- `.vscode` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f189de79ceef7c1ef69f61f12e272f99b4cdb699` is the revision these paths and observations refer to.
