# Project structure: tone-row/flowchart-fun

**Analysed commit:** `5854f69b97dc247cac3b689c5c2c482fd78df81d`

**Commit reference:** [5854f69b97dc247cac3b689c5c2c482fd78df81d](https://github.com/tone-row/flowchart-fun/commit/5854f69b97dc247cac3b689c5c2c482fd78df81d)

**Tree at this commit:** [tone-row/flowchart-fun@5854f69b97dc](https://github.com/tone-row/flowchart-fun/tree/5854f69b97dc247cac3b689c5c2c482fd78df81d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tone-row/flowchart-fun |
| Description | Easily generate flowcharts and diagrams from text ⿻ |
| Stars | 3410 |
| Forks | 247 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `5854f69b97dc247cac3b689c5c2c482fd78df81d` |
| Retrieved at | 2026-11-14T19:15:20.387971+00:00 |
| Files in this snapshot | 523 |

## Directory tree

```text
.claude/  (46 files)
  skills/  (46 files)
    verify/  (46 files)
      … 46 files under this directory
.github/  (4 files)
  workflows/  (3 files)
    e2e.yml
    release.yml
    test.yml
  FUNDING.yml
.husky/  (2 files)
  .gitignore
  pre-commit
api/  (50 files)
  _fixtures/  (2 files)
    issues.json
    releases.json
  _lib/  (11 files)
    _dates.ts
    _helpers.ts
    _mail.ts
    _notion.ts
    _openai.ts
    _pass.test.ts
    _pass.ts
    _releases.ts
    _stripe.ts
    _supabase.ts
    _validStripePrices.ts
  blog/  (2 files)
    post.ts
    posts.ts
  cron/  (1 files)
    deleteDevUsers.ts
  data/  (7 files)
    fixtures/  (3 files)
      … 3 files under this directory
    _mapDataToGraph.test.ts
    _mapDataToGraph.ts
    import.ts
    process.ts
  prompt/  (8 files)
    _parseFlowchart.test.ts
    _parseFlowchart.ts
    _shared.ts
    choose-template.ts
    convert.ts
    edit.ts
    prompt.ts
    speech-to-text.ts
  .eslintrc
  cancel-subscription.ts
  changelog.ts
  create-checkout-session.ts
  create-customer-portal-session.ts
  customer-info.ts
  generate-public-id.ts
  jest.config.js
  loops-event.ts
  mail.ts
  order-history.ts
  package.json
  public.ts
  resume-subscription.ts
  roadmap.ts
  tsconfig.json
  types.d.ts
  update-email.ts
  version.ts
app/  (391 files)
  e2e/  (12 files)
    visual/  (6 files)
      … 6 files under this directory
    logged-in.spec.ts
    not-logged-in.spec.ts
    pass.spec.ts
    pro.spec.ts
    sign-up.spec.ts
    utils.ts
  public/  (66 files)
    font-previews/  (9 files)
      … 9 files under this directory
    fonts/  (20 files)
      … 20 files under this directory
    images/  (28 files)
      … 28 files under this directory
    _redirects
    browserconfig.xml
    favicon.svg
    index.html
    manifest.json
    robots.txt
    safari-pinned-tab.svg
    site.webmanifest
    sitemap.xml
  scripts/  (4 files)
    autotranslations.mjs
    generate-font-previews.mjs
    generate-frozen-fixtures.mjs
    screenshot-templates.mjs
  src/  (297 files)
    components/  (100 files)
      … 100 files under this directory
    lib/  (128 files)
      … 128 files under this directory
    locales/  (17 files)
      … 17 files under this directory
    pages/  (35 files)
      … 35 files under this directory
    slang/  (3 files)
      … 3 files under this directory
    types/  (1 files)
      … 1 files under this directory
    ui/  (7 files)
      … 7 files under this directory
    index.css
    index.tsx
    react-app-env.d.ts
    reportWebVitals.ts
    setupTests.ts
    test-utils.tsx
  .env.example
  .eslintignore
  .eslintrc.cjs
  .gitignore
  .linguirc
  .prettierignore
  .prettierrc
  package.json
  playwright.config.ts
  playwright.visual.config.ts
  tailwind.config.js
  tsconfig.json
formulaic/  (13 files)
  src/  (8 files)
    example/  (5 files)
      … 5 files under this directory
    README.md
    formulaic.test.tsx
    formulaic.tsx
  .gitignore
  .postcssrc
  package.json
  tailwind.config.js
  tsconfig.json
shared/  (7 files)
  src/  (4 files)
    ImportDataFormType.ts
    blog.ts
    index.ts
    templates.ts
  .gitignore
  package.json
  tsconfig.json
.gitignore
.node-version
CLAUDE.md
LICENSE
README.md
ff-pricing-redesign-plan.md
package.json
pnpm-workspace.yaml
pull_request_template.md
vercel.json
```

## Entry points

- [app/src/components/App.tsx](https://github.com/tone-row/flowchart-fun/blob/5854f69b97dc247cac3b689c5c2c482fd78df81d/app/src/components/App.tsx)
- [app/src/index.tsx](https://github.com/tone-row/flowchart-fun/blob/5854f69b97dc247cac3b689c5c2c482fd78df81d/app/src/index.tsx)
- [app/src/slang/index.tsx](https://github.com/tone-row/flowchart-fun/blob/5854f69b97dc247cac3b689c5c2c482fd78df81d/app/src/slang/index.tsx)
- [shared/src/index.ts](https://github.com/tone-row/flowchart-fun/blob/5854f69b97dc247cac3b689c5c2c482fd78df81d/shared/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 42 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 256 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| formulaic package | library | Observed | Groups 6 file(s) under formulaic package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 4 file(s) under shared package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/e2e.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `api/_fixtures/issues.json` (config)
- `api/_fixtures/releases.json` (config)
- `api/data/fixtures/simpleLucidChart.json` (config)
- `api/package.json` (manifest)
- `api/tsconfig.json` (config)
- `app/.env.example` (config)
- `app/package.json` (manifest)
- `app/public/manifest.json` (config)
- `app/src/lib/FFTheme.schema.json` (config)
- `app/src/lib/cyStyleToString/fixture.json` (config)
- `app/tsconfig.json` (config)
- `formulaic/package.json` (manifest)
- `formulaic/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `shared/package.json` (manifest)
- `shared/tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `app` — 391 analysed file(s)
- `api` — 50 analysed file(s)
- `.claude` — 46 analysed file(s)
- `formulaic` — 13 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `shared` — 7 analysed file(s)
- `.github` — 4 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5854f69b97dc247cac3b689c5c2c482fd78df81d` is the revision these paths and observations refer to.
