# Project structure: ixartz/Next-js-Boilerplate

**Analysed commit:** `b83157a8018f55b926a3c25a4b7a7e14b0dfbc35`

**Commit reference:** [b83157a8018f55b926a3c25a4b7a7e14b0dfbc35](https://github.com/ixartz/Next-js-Boilerplate/commit/b83157a8018f55b926a3c25a4b7a7e14b0dfbc35)

**Tree at this commit:** [ixartz/Next-js-Boilerplate@b83157a8018f](https://github.com/ixartz/Next-js-Boilerplate/tree/b83157a8018f55b926a3c25a4b7a7e14b0dfbc35)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ixartz/Next-js-Boilerplate |
| Description | 🚀🎉📚 Nextjs Boilerplate and Starter with App Router and Page Router support, Tailwind CSS 4 and TypeScript ⚡️ Made with developer experience first: Next.js 16 + TypeScript + ESLint + Prettier + Drizzle ORM + Husky + Lint-Staged + Vitest + Testing Library + Playwright + Storybook + Commitlint + VSCod… |
| Stars | 13094 |
| Forks | 2404 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `b83157a8018f55b926a3c25a4b7a7e14b0dfbc35` |
| Retrieved at | 2026-11-14T19:13:19.815264+00:00 |
| Files in this snapshot | 94 |

## Directory tree

```text
.github/  (6 files)
  actions/  (1 files)
    setup-project/  (1 files)
      … 1 files under this directory
  workflows/  (3 files)
    CI.yml
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
public/  (5 files)
  assets/  (5 files)
    images/  (5 files)
      … 5 files under this directory
src/  (48 files)
  app/  (18 files)
    [locale]/  (14 files)
      … 14 files under this directory
    api/  (1 files)
      … 1 files under this directory
    global-error.tsx
    robots.ts
    sitemap.ts
  components/  (7 files)
    CounterForm.tsx
    CurrentCount.tsx
    DemoBadge.tsx
    DemoBanner.tsx
    Hello.tsx
    LocaleSwitcher.tsx
    Sponsors.tsx
  libs/  (7 files)
    Arcjet.ts
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
  templates/  (3 files)
    BaseTemplate.stories.tsx
    BaseTemplate.test.tsx
    BaseTemplate.tsx
  types/  (1 files)
    I18n.ts
  utils/  (4 files)
    AppConfig.ts
    DBConnection.ts
    Helpers.test.ts
    Helpers.ts
  validations/  (1 files)
    CounterValidation.ts
  instrumentation-client.ts
  instrumentation.ts
  proxy.ts
tests/  (5 files)
  e2e/  (4 files)
    Counter.e2e.ts
    I18n.e2e.ts
    Sanity.check.e2e.ts
    Visual.e2e.ts
  integration/  (1 files)
    Counter.integ.ts
.coderabbit.yaml
.gitignore
AGENTS.md
CLAUDE.md
LICENSE
README.md
codecov.yml
commitlint.config.ts
crowdin.yml
drizzle.config.ts
knip.config.ts
lefthook.yml
next.config.ts
oxfmt.config.ts
oxlint.config.ts
package.json
playwright.config.ts
tsconfig.json
vitest.config.ts
```

## Entry points

- [.storybook/main.ts](https://github.com/ixartz/Next-js-Boilerplate/blob/b83157a8018f55b926a3c25a4b7a7e14b0dfbc35/.storybook/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 17 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 7 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| instrumentation-client.ts package | library | Observed | Groups 1 file(s) under instrumentation-client.ts package (observed from repository paths and static analysis). |
| instrumentation.ts package | library | Observed | Groups 1 file(s) under instrumentation.ts package (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 7 file(s) under libs package (observed from repository paths and static analysis). |
| proxy.ts package | library | Observed | Groups 1 file(s) under proxy.ts package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 3 file(s) under templates package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). |
| validations package | library | Observed | Groups 1 file(s) under validations package (observed from repository paths and static analysis). |

## Important files

- `.coderabbit.yaml` (config)
- `.github/FUNDING.yml` (config)
- `.github/actions/setup-project/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/CI.yml` (ci)
- `.github/workflows/crowdin.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `.vscode/tasks.json` (config)
- `codecov.yml` (config)
- `crowdin.yml` (config)
- `lefthook.yml` (config)
- `migrations/meta/0000_snapshot.json` (config)
- `migrations/meta/_journal.json` (config)
- `package.json` (manifest)
- `src/locales/en.json` (config)
- `src/locales/fr.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 48 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 6 analysed file(s)
- `public` — 5 analysed file(s)
- `tests` — 5 analysed file(s)
- `.storybook` — 4 analysed file(s)
- `.vscode` — 4 analysed file(s)
- `migrations` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b83157a8018f55b926a3c25a4b7a7e14b0dfbc35` is the revision these paths and observations refer to.
