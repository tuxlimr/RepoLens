# Project structure: ixartz/SaaS-Boilerplate

**Analysed commit:** `e3952a7ed5b0ef172ac4363c4644b8c334d1094b`

**Commit reference:** [e3952a7ed5b0ef172ac4363c4644b8c334d1094b](https://github.com/ixartz/SaaS-Boilerplate/commit/e3952a7ed5b0ef172ac4363c4644b8c334d1094b)

**Tree at this commit:** [ixartz/SaaS-Boilerplate@e3952a7ed5b0](https://github.com/ixartz/SaaS-Boilerplate/tree/e3952a7ed5b0ef172ac4363c4644b8c334d1094b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ixartz/SaaS-Boilerplate |
| Description | 🚀🎉📚 SaaS Boilerplate built with Next.js + Tailwind CSS + Shadcn UI + TypeScript. ⚡️ Full-stack React application with Auth, Multi-tenancy, Roles & Permissions, i18n, Landing Page, DB, Logging, Testing |
| Stars | 7489 |
| Forks | 1334 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `e3952a7ed5b0ef172ac4363c4644b8c334d1094b` |
| Retrieved at | 2026-11-14T19:13:49.725017+00:00 |
| Files in this snapshot | 130 |

## Directory tree

```text
.github/  (7 files)
  actions/  (1 files)
    setup-project/  (1 files)
      … 1 files under this directory
  workflows/  (4 files)
    CI.yml
    checkly.yml
    crowdin.yml
    release.yml
  FUNDING.yml
  dependabot.yml
.storybook/  (4 files)
  main.ts
  preview.ts
  vitest.config.ts
  vitest.setup.ts
.vscode/  (4 files)
  extensions.json
  launch.json
  settings.json
  tasks.json
migrations/  (3 files)
  meta/  (2 files)
    0000_snapshot.json
    _journal.json
  0000_init-db.sql
public/  (7 files)
  assets/  (7 files)
    images/  (7 files)
      … 7 files under this directory
skills/  (1 files)
  saas-builder/  (1 files)
    SKILL.md
src/  (83 files)
  app/  (14 files)
    [locale]/  (11 files)
      … 11 files under this directory
    global-error.tsx
    robots.ts
    sitemap.ts
  components/  (14 files)
    ui/  (7 files)
      … 7 files under this directory
    ActiveLink.tsx
    Background.stories.tsx
    Background.tsx
    DemoBadge.tsx
    LocaleSwitcher.tsx
    MenuToggle.test.tsx
    MenuToggle.tsx
  features/  (20 files)
    billing/  (3 files)
      … 3 files under this directory
    dashboard/  (7 files)
      … 7 files under this directory
    landing/  (9 files)
      … 9 files under this directory
    sponsors/  (1 files)
      … 1 files under this directory
  hooks/  (2 files)
    UseMenu.test.ts
    UseMenu.ts
  libs/  (6 files)
    DB.ts
    Env.ts
    I18n.ts
    I18nNavigation.ts
    I18nRouting.ts
    Logger.ts
  locales/  (2 files)
    en.json
    fr.json
  models/  (1 files)
    Schema.ts
  styles/  (1 files)
    global.css
  templates/  (10 files)
    CTA.tsx
    DemoBanner.tsx
    FAQ.tsx
    Features.tsx
    Footer.tsx
    Hero.tsx
    Logo.tsx
    Navbar.tsx
    Pricing.tsx
    Sponsors.tsx
  types/  (5 files)
    Auth.ts
    Enum.ts
    I18n.ts
    Subscription.ts
    globals.d.ts
  utils/  (5 files)
    AppConfig.ts
    DBConnection.ts
    Helpers.test.ts
    Helpers.ts
    PricingPlans.ts
  instrumentation-client.ts
  instrumentation.ts
  proxy.ts
tests/  (4 files)
  e2e/  (3 files)
    I18n.e2e.ts
    Sanity.check.e2e.ts
    Visual.e2e.ts
  integration/  (1 files)
    .gitkeep
.gitignore
LICENSE
README.md
checkly.config.ts
codecov.yml
commitlint.config.ts
components.json
crowdin.yml
drizzle.config.ts
eslint.config.mjs
knip.config.ts
lefthook.yml
next.config.ts
package.json
playwright.config.ts
tsconfig.json
vitest.config.ts
```

## Entry points

- [.storybook/main.ts](https://github.com/ixartz/SaaS-Boilerplate/blob/e3952a7ed5b0ef172ac4363c4644b8c334d1094b/.storybook/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 14 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 14 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| features package | library | Observed | Groups 20 file(s) under features package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 2 file(s) under hooks package (observed from repository paths and static analysis). |
| instrumentation-client.ts package | library | Observed | Groups 1 file(s) under instrumentation-client.ts package (observed from repository paths and static analysis). |
| instrumentation.ts package | library | Observed | Groups 1 file(s) under instrumentation.ts package (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 6 file(s) under libs package (observed from repository paths and static analysis). |
| proxy.ts package | library | Observed | Groups 1 file(s) under proxy.ts package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 10 file(s) under templates package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 5 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/actions/setup-project/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/CI.yml` (ci)
- `.github/workflows/checkly.yml` (ci)
- `.github/workflows/crowdin.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `.vscode/tasks.json` (config)
- `codecov.yml` (config)
- `components.json` (config)
- `crowdin.yml` (config)
- `lefthook.yml` (config)
- `migrations/meta/0000_snapshot.json` (config)
- `migrations/meta/_journal.json` (config)
- `package.json` (manifest)
- `src/locales/en.json` (config)
- `src/locales/fr.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 83 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 7 analysed file(s)
- `public` — 7 analysed file(s)
- `.storybook` — 4 analysed file(s)
- `.vscode` — 4 analysed file(s)
- `tests` — 4 analysed file(s)
- `migrations` — 3 analysed file(s)
- `skills` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e3952a7ed5b0ef172ac4363c4644b8c334d1094b` is the revision these paths and observations refer to.
