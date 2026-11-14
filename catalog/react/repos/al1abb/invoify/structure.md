# Project structure: al1abb/invoify

**Analysed commit:** `3859b3cbae28ca4ec559db5ef87e41b798740340`

**Commit reference:** [3859b3cbae28ca4ec559db5ef87e41b798740340](https://github.com/al1abb/invoify/commit/3859b3cbae28ca4ec559db5ef87e41b798740340)

**Tree at this commit:** [al1abb/invoify@3859b3cbae28](https://github.com/al1abb/invoify/tree/3859b3cbae28ca4ec559db5ef87e41b798740340)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | al1abb/invoify |
| Description | An invoice generator app built using Next.js, Typescript, and Shadcn |
| Stars | 6391 |
| Forks | 751 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `3859b3cbae28ca4ec559db5ef87e41b798740340` |
| Retrieved at | 2026-11-14T19:14:07.052661+00:00 |
| Files in this snapshot | 195 |

## Directory tree

```text
.claude/  (1 files)
  launch.json
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    ci.yml
  dependabot.yml
app/  (89 files)
  [locale]/  (5 files)
    [...rest]/  (1 files)
      … 1 files under this directory
    guide/  (1 files)
      … 1 files under this directory
    layout.tsx
    opengraph-image.tsx
    page.tsx
  api/  (4 files)
    invoice/  (4 files)
      … 4 files under this directory
  components/  (73 files)
    dev/  (1 files)
      … 1 files under this directory
    invoice/  (24 files)
      … 24 files under this directory
    layout/  (4 files)
      … 4 files under this directory
    modals/  (11 files)
      … 11 files under this directory
    reusables/  (12 files)
      … 12 files under this directory
    templates/  (20 files)
      … 20 files under this directory
    index.ts
  globals.css
  layout.tsx
  manifest.ts
  not-found.tsx
  page.tsx
  robots.ts
  sitemap.ts
components/  (25 files)
  ui/  (25 files)
    alert-dialog.tsx
    aspect-ratio.tsx
    badge.tsx
    button.tsx
    calendar.tsx
    card.tsx
    dialog.tsx
    form.tsx
    input.tsx
    label.tsx
    popover.tsx
    progress.tsx
    scroll-area.tsx
    select.tsx
    separator.tsx
    sheet.tsx
    skeleton.tsx
    switch.tsx
    table.tsx
    tabs.tsx
    textarea.tsx
    toast.tsx
    toaster.tsx
    tooltip.tsx
    … 1 more files
contexts/  (7 files)
  ChargesContext.tsx
  InvoiceContext.tsx
  Providers.tsx
  SignatureContext.tsx
  ThemeProvider.tsx
  TranslationContext.tsx
  WizardContext.tsx
e2e/  (1 files)
  smoke.spec.ts
hooks/  (4 files)
  useCurrencies.tsx
  useFitScale.ts
  useMediaQuery.tsx
  useToasts.tsx
i18n/  (22 files)
  locales/  (18 files)
    ar.json
    az.json
    ca.json
    de.json
    en.json
    es.json
    fr.json
    he.json
    id.json
    it.json
    ja.json
    nb-NO.json
    nn-NO.json
    pl.json
    pt-BR.json
    sr.json
    tr.json
    zh-CN.json
  messages.ts
  navigation.ts
  request.ts
  routing.ts
lib/  (12 files)
  server/  (2 files)
    rateLimit.ts
    validateRequest.ts
  fonts.ts
  helpers.ts
  invoiceNumber.ts
  partyStore.ts
  schemas.ts
  secureStore.ts
  seo.ts
  utils.ts
  variables.ts
  wizardSteps.ts
public/  (3 files)
  assets/  (3 files)
    data/  (1 files)
      … 1 files under this directory
    favicon/  (1 files)
      … 1 files under this directory
    img/  (1 files)
      … 1 files under this directory
scripts/  (1 files)
  build-pdf-css.mjs
services/  (7 files)
  invoice/  (7 files)
    client/  (1 files)
      … 1 files under this directory
    server/  (6 files)
      … 6 files under this directory
.editorconfig
.gitignore
.prettierignore
.prettierrc.json
Dockerfile
LICENSE
README.md
components.json
eslint.config.mjs
middleware.ts
next-env.d.ts
next.config.js
package.json
playwright.config.ts
postcss.config.js
puppeteer.config.cjs
tailwind.config.js
tsconfig.json
types.ts
```

## Entry points

- [app/[locale]/[...rest]/page.tsx](https://github.com/al1abb/invoify/blob/3859b3cbae28ca4ec559db5ef87e41b798740340/app/%5Blocale%5D/%5B...rest%5D/page.tsx)
- [app/[locale]/guide/page.tsx](https://github.com/al1abb/invoify/blob/3859b3cbae28ca4ec559db5ef87e41b798740340/app/%5Blocale%5D/guide/page.tsx)
- [app/[locale]/page.tsx](https://github.com/al1abb/invoify/blob/3859b3cbae28ca4ec559db5ef87e41b798740340/app/%5Blocale%5D/page.tsx)
- [app/components/index.ts](https://github.com/al1abb/invoify/blob/3859b3cbae28ca4ec559db5ef87e41b798740340/app/components/index.ts)
- [app/page.tsx](https://github.com/al1abb/invoify/blob/3859b3cbae28ca4ec559db5ef87e41b798740340/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 84 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 25 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| contexts package | library | Observed | Groups 7 file(s) under contexts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 9 file(s) under core modules (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 1 file(s) under e2e package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 4 file(s) under hooks package (observed from repository paths and static analysis). |
| i18n package | library | Observed | Groups 4 file(s) under i18n package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 12 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.claude/launch.json` (config)
- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.prettierrc.json` (config)
- `Dockerfile` (container)
- `components.json` (config)
- `i18n/locales/ar.json` (config)
- `i18n/locales/az.json` (config)
- `i18n/locales/ca.json` (config)
- `i18n/locales/de.json` (config)
- `i18n/locales/en.json` (config)
- `i18n/locales/es.json` (config)
- `i18n/locales/fr.json` (config)
- `i18n/locales/he.json` (config)
- `i18n/locales/id.json` (config)
- `i18n/locales/it.json` (config)
- `i18n/locales/ja.json` (config)
- `i18n/locales/nb-NO.json` (config)
- `i18n/locales/nn-NO.json` (config)
- `i18n/locales/pl.json` (config)
- `i18n/locales/pt-BR.json` (config)
- `i18n/locales/sr.json` (config)
- `i18n/locales/tr.json` (config)
- `i18n/locales/zh-CN.json` (config)
- `package.json` (manifest)
- `public/assets/data/currencies.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `app` — 89 analysed file(s)
- `components` — 25 analysed file(s)
- `i18n` — 22 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `lib` — 12 analysed file(s)
- `contexts` — 7 analysed file(s)
- `services` — 7 analysed file(s)
- `.github` — 4 analysed file(s)
- `hooks` — 4 analysed file(s)
- `public` — 3 analysed file(s)
- `.claude` — 1 analysed file(s)
- `e2e` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3859b3cbae28ca4ec559db5ef87e41b798740340` is the revision these paths and observations refer to.
