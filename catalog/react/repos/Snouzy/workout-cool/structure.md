# Project structure: Snouzy/workout-cool

**Analysed commit:** `d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e`

**Commit reference:** [d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e](https://github.com/Snouzy/workout-cool/commit/d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e)

**Tree at this commit:** [Snouzy/workout-cool@d52f9f62d2a5](https://github.com/Snouzy/workout-cool/tree/d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Snouzy/workout-cool |
| Description | 🏋 Modern open-source fitness coaching platform. Create workout plans, track progress, and access a comprehensive exercise database. |
| Stars | 8688 |
| Forks | 768 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e` |
| Retrieved at | 2026-11-14T19:13:40.010879+00:00 |
| Files in this snapshot | 737 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (5 files)
    ci.yml
    notify-discord-issues.yml
    notify-discord-pr.yml
    notify-discord.yml
    publish-ghcr-image.yml
  FUNDING.yml
  pull_request_template.md
.vscode/  (1 files)
  settings.json
app/  (170 files)
  [locale]/  (131 files)
    (admin)/  (9 files)
      … 9 files under this directory
    (app)/  (116 files)
      … 116 files under this directory
    @modal/  (2 files)
      … 2 files under this directory
    manifest.json/  (1 files)
      … 1 files under this directory
    layout.tsx
    not-found.tsx
    providers.tsx
  ads.txt/  (1 files)
    route.ts
  api/  (36 files)
    analytics/  (1 files)
      … 1 files under this directory
    auth/  (2 files)
      … 2 files under this directory
    billing/  (1 files)
      … 1 files under this directory
    exercises/  (7 files)
      … 7 files under this directory
    premium/  (4 files)
      … 4 files under this directory
    programs/  (7 files)
      … 7 files under this directory
    revenuecat/  (3 files)
      … 3 files under this directory
    user/  (3 files)
      … 3 files under this directory
    webhooks/  (2 files)
      … 2 files under this directory
    workout-sessions/  (6 files)
      … 6 files under this directory
  robots.txt
  sitemap.ts
content/  (24 files)
  about/  (6 files)
    en.mdx
    es.mdx
    fr.mdx
    pt.mdx
    ru.mdx
    zh-CN.mdx
  privacy-policy/  (6 files)
    en.mdx
    es.mdx
    fr.mdx
    pt.mdx
    ru.mdx
    zh-CN.mdx
  sales-terms/  (6 files)
    en.mdx
    es.mdx
    fr.mdx
    pt.mdx
    ru.mdx
    zh-CN.mdx
  terms/  (6 files)
    en.mdx
    es.mdx
    fr.mdx
    pt.mdx
    ru.mdx
    zh-CN.mdx
data/  (1 files)
  sample-exercises.csv
docs/  (3 files)
  superpowers/  (2 files)
    plans/  (1 files)
      … 1 files under this directory
    specs/  (1 files)
      … 1 files under this directory
  SELF-HOSTING.md
emails/  (6 files)
  utils/  (1 files)
    BaseEmailLayout.tsx
  ContactSupportEmail.tsx
  DeleteAccountEmail.tsx
  ResetPasswordEmail.tsx
  SponsorOnboardingEmail.tsx
  VerifyEmail.tsx
locales/  (10 files)
  client.ts
  en.ts
  es.ts
  fr.ts
  heart-rate-zones-translations.ts
  pt.ts
  ru.ts
  server.ts
  types.ts
  zh-CN.ts
prisma/  (39 files)
  migrations/  (1 files)
    0_init/  (1 files)
      … 1 files under this directory
  migrations_backup/  (37 files)
    20240726_simplify_subscription_model/  (1 files)
      … 1 files under this directory
    20250101000000_baseline/  (1 files)
      … 1 files under this directory
    20250117000000_add_statistics_indexes/  (1 files)
      … 1 files under this directory
    20250414120436_init/  (1 files)
      … 1 files under this directory
    20250414170807_add_feedbacks/  (1 files)
      … 1 files under this directory
    20250414174246_rename_feedbacks/  (1 files)
      … 1 files under this directory
    20250414232816_add_first_name_and_last_name/  (1 files)
      … 1 files under this directory
    20250416160303_add_plans/  (1 files)
      … 1 files under this directory
    20250416160502_map/  (1 files)
      … 1 files under this directory
    20250505114841_add_user_role/  (1 files)
      … 1 files under this directory
    20250505191954_admin_and_user_lowercase/  (1 files)
      … 1 files under this directory
    20250610182024_add_exercises_and_attributes/  (1 files)
      … 1 files under this directory
    20250610182815_add_exercise_enums/  (1 files)
      … 1 files under this directory
    20250610184725_simplified_exercises/  (1 files)
      … 1 files under this directory
    20250611190228_convert_text_to_enums/  (1 files)
      … 1 files under this directory
    20250611210106_add_enum_values/  (1 files)
      … 1 files under this directory
    20250612213546_workout_session_sets/  (1 files)
      … 1 files under this directory
    20250613095031_add_multi_column_support/  (1 files)
      … 1 files under this directory
    20250614125347_add_table_maps/  (1 files)
      … 1 files under this directory
    20250614153656_remove_value_int_value_sec_unit_from_workoutset/  (1 files)
      … 1 files under this directory
    20250615160343_add_muscle_to_a_workout_session/  (1 files)
      … 1 files under this directory
    20250615170916_add_cascade_delete_workout_sessions/  (1 files)
      … 1 files under this directory
    20250623142458_add_billing_and_subscriptions/  (1 files)
      … 1 files under this directory
    20250623143952_remove_webhook_events/  (1 files)
      … 1 files under this directory
    20250623144324_add_webhook_events/  (1 files)
      … 1 files under this directory
    20250625155932_add_admin/  (1 files)
      … 1 files under this directory
    20250625195907_add_program_visibility/  (1 files)
      … 1 files under this directory
    20250626102058_add_i18n_slugs_on_program/  (1 files)
      … 1 files under this directory
    20250626134345_remove_emoji_on_program/  (1 files)
      … 1 files under this directory
    20250626182857_cleanup_billing_system/  (1 files)
      … 1 files under this directory
    20250626204136_remove_payment_table/  (1 files)
      … 1 files under this directory
    20250626205121_remove_legacy_premium_fields/  (1 files)
      … 1 files under this directory
    20250626205904_remove_payment_table_keep_ispremium/  (1 files)
      … 1 files under this directory
    20250707114920_add_user_favorite_exercises/  (1 files)
      … 1 files under this directory
    20250708214116_add_rating_to_wkt_sessions/  (1 files)
      … 1 files under this directory
    20250709_add_revenuecat_fields/  (1 files)
      … 1 files under this directory
    migration_lock.toml
  schema.prisma
public/  (10 files)
  images/  (7 files)
    stores/  (7 files)
      … 7 files under this directory
  _ads.txt
  manifest.json
  sw.js
scripts/  (8 files)
  check-pricing-config.ts
  import-exercises-with-attributes.prompt.md
  import-exercises-with-attributes.ts
  seed-leaderboard-data.ts
  seed-multi-region-plans.ts
  seed-subscription-plans-simple.ts
  seed-workout-data-advanced.ts
  setup.sh
src/  (432 files)
  components/  (109 files)
    ads/  (25 files)
      … 25 files under this directory
    premium/  (1 files)
      … 1 files under this directory
    pwa/  (1 files)
      … 1 files under this directory
    seo/  (5 files)
      … 5 files under this directory
    svg/  (11 files)
      … 11 files under this directory
    tools/  (1 files)
      … 1 files under this directory
    ui/  (62 files)
      … 62 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    version.tsx
  entities/  (15 files)
    exercise/  (2 files)
      … 2 files under this directory
    program/  (1 files)
      … 1 files under this directory
    program-session/  (1 files)
      … 1 files under this directory
    user/  (11 files)
      … 11 files under this directory
  features/  (222 files)
    admin/  (32 files)
      … 32 files under this directory
    ads/  (1 files)
      … 1 files under this directory
    auth/  (24 files)
      … 24 files under this directory
    consent-banner/  (3 files)
      … 3 files under this directory
    contact/  (3 files)
      … 3 files under this directory
    contact-feedback/  (4 files)
      … 4 files under this directory
    dialogs-provider/  (2 files)
      … 2 files under this directory
    download/  (2 files)
      … 2 files under this directory
    email/  (3 files)
      … 3 files under this directory
    form/  (1 files)
      … 1 files under this directory
    layout/  (8 files)
      … 8 files under this directory
    leaderboard/  (10 files)
      … 10 files under this directory
    page/  (1 files)
      … 1 files under this directory
    premium/  (8 files)
      … 8 files under this directory
    programs/  (21 files)
      … 21 files under this directory
    release-notes/  (10 files)
      … 10 files under this directory
    sponsor/  (3 files)
      … 3 files under this directory
    statistics/  (12 files)
      … 12 files under this directory
    theme/  (3 files)
      … 3 files under this directory
    update-password/  (5 files)
      … 5 files under this directory
    user/  (1 files)
      … 1 files under this directory
    workout-builder/  (47 files)
      … 47 files under this directory
    workout-session/  (18 files)
      … 18 files under this directory
  shared/  (82 files)
    api/  (7 files)
      … 7 files under this directory
    config/  (2 files)
      … 2 files under this directory
    constants/  (10 files)
      … 10 files under this directory
    hooks/  (7 files)
      … 7 files under this directory
    lib/  (47 files)
      … 47 files under this directory
    schemas/  (1 files)
      … 1 files under this directory
    styles/  (3 files)
      … 3 files under this directory
    types/  (5 files)
      … 5 files under this directory
  widgets/  (2 files)
    language-selector/  (1 files)
      … 1 files under this directory
    404.tsx
  env.ts
  index.d.ts
.cursorrules
.env.example
.gitignore
.prettierrc
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
Dockerfile
LICENSE
Makefile
README.md
components.json
docker-compose.yml
eslint.config.mjs
next.config.ts
nextauth.d.ts
package.json
postcss.config.mjs
proxy.ts
tailwind.config.ts
tsconfig.json
vitest.config.ts
workout-cool.code-workspace
```

## Entry points

- [app/[locale]/(app)/page.tsx](https://github.com/Snouzy/workout-cool/blob/d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e/app/%5Blocale%5D/%28app%29/page.tsx)
- [locales/server.ts](https://github.com/Snouzy/workout-cool/blob/d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e/locales/server.ts)
- [src/components/ads/index.ts](https://github.com/Snouzy/workout-cool/blob/d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e/src/components/ads/index.ts)
- [src/features/release-notes/index.ts](https://github.com/Snouzy/workout-cool/blob/d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e/src/features/release-notes/index.ts)
- [src/features/workout-builder/index.ts](https://github.com/Snouzy/workout-cool/blob/d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e/src/features/workout-builder/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 42 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 130 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 109 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| emails package | library | Observed | Groups 6 file(s) under emails package (observed from repository paths and static analysis). |
| entities package | library | Observed | Groups 15 file(s) under entities package (observed from repository paths and static analysis). |
| env.ts package | library | Observed | Groups 1 file(s) under env.ts package (observed from repository paths and static analysis). |
| features package | library | Observed | Groups 219 file(s) under features package (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| locales package | library | Observed | Groups 10 file(s) under locales package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 70 file(s) under shared package (observed from repository paths and static analysis). |
| widgets package | library | Observed | Groups 2 file(s) under widgets package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/notify-discord-issues.yml` (ci)
- `.github/workflows/notify-discord-pr.yml` (ci)
- `.github/workflows/notify-discord.yml` (ci)
- `.github/workflows/publish-ghcr-image.yml` (ci)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `components.json` (config)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `prisma/migrations_backup/migration_lock.toml` (config)
- `public/manifest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 432 analysed file(s)
- `app` — 170 analysed file(s)
- `prisma` — 39 analysed file(s)
- `content` — 24 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `.github` — 10 analysed file(s)
- `locales` — 10 analysed file(s)
- `public` — 10 analysed file(s)
- `scripts` — 8 analysed file(s)
- `emails` — 6 analysed file(s)
- `docs` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `data` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d52f9f62d2a5fcbb78d67a95dc8763f9a34dbf9e` is the revision these paths and observations refer to.
