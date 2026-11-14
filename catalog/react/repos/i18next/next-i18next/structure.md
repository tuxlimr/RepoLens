# Project structure: i18next/next-i18next

**Analysed commit:** `09a2aa0975b54cd4684dcee9ab7b77224180d338`

**Commit reference:** [09a2aa0975b54cd4684dcee9ab7b77224180d338](https://github.com/i18next/next-i18next/commit/09a2aa0975b54cd4684dcee9ab7b77224180d338)

**Tree at this commit:** [i18next/next-i18next@09a2aa0975b5](https://github.com/i18next/next-i18next/tree/09a2aa0975b54cd4684dcee9ab7b77224180d338)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | i18next/next-i18next |
| Description | The easiest way to translate your NextJs apps. |
| Stars | 6164 |
| Forks | 754 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `09a2aa0975b54cd4684dcee9ab7b77224180d338` |
| Retrieved at | 2026-11-14T19:14:09.180608+00:00 |
| Files in this snapshot | 266 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    ci.yml
    next-compat.yml
  stale.yml
.husky/  (2 files)
  .gitignore
  pre-commit
cypress/  (2 files)
  e2e/  (1 files)
    spec.cy.ts
  tsconfig.json
examples/  (202 files)
  app-router-icu/  (15 files)
    @types/  (2 files)
      … 2 files under this directory
    app/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    i18n.config.ts
    i18next.config.ts
    next-env.d.ts
    package.json
    proxy.ts
    tsconfig.json
  app-router-no-locale-path/  (37 files)
    app/  (29 files)
      … 29 files under this directory
    public/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    eslint.config.mjs
    i18n.config.js
    next.config.js
    package.json
    proxy.js
  app-router-simple/  (43 files)
    @types/  (2 files)
      … 2 files under this directory
    app/  (31 files)
      … 31 files under this directory
    public/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    eslint.config.mjs
    i18n.config.ts
    next-env.d.ts
    next.config.js
    package.json
    proxy.ts
    tsconfig.json
  mixed-routers/  (26 files)
    app/  (4 files)
      … 4 files under this directory
    components/  (2 files)
      … 2 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    public/  (7 files)
      … 7 files under this directory
    i18n.config.ts
    i18n.shared.js
    next-env.d.ts
    next-i18next.config.js
    next.config.js
    package.json
    proxy.ts
    tsconfig.json
    vercel.json
  pages-router-auto-static-optimize/  (25 files)
    @types/  (2 files)
      … 2 files under this directory
    components/  (2 files)
      … 2 files under this directory
    pages/  (5 files)
      … 5 files under this directory
    public/  (9 files)
      … 9 files under this directory
    next-env.d.ts
    next-i18next.config.js
    next-utils.config.js
    next.config.js
    package.json
    tsconfig.json
    vercel.json
  pages-router-simple/  (22 files)
    @types/  (2 files)
      … 2 files under this directory
    components/  (2 files)
      … 2 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    public/  (7 files)
      … 7 files under this directory
    next-env.d.ts
    next-i18next.config.js
    next-utils.config.js
    next.config.js
    package.json
    tsconfig.json
    vercel.json
  pages-router-ssg/  (34 files)
    components/  (4 files)
      … 4 files under this directory
    lib/  (3 files)
      … 3 files under this directory
    pages/  (8 files)
      … 8 files under this directory
    public/  (13 files)
      … 13 files under this directory
    .gitignore
    README.md
    eslint.config.mjs
    next-i18next.config.js
    next.config.js
    package.json
src/  (34 files)
  appRouter/  (17 files)
    proxy/  (4 files)
      … 4 files under this directory
    client.ondemand.test.tsx
    client.ssr.test.tsx
    client.test.tsx
    client.tsx
    config.test.ts
    config.ts
    icu.test.tsx
    icu.tsx
    index.ts
    mf2.tsx
    server.test.ts
    server.ts
    types.ts
  pagesRouter/  (17 files)
    config/  (4 files)
      … 4 files under this directory
    createClient/  (4 files)
      … 4 files under this directory
    appWithTranslation.client.test.tsx
    appWithTranslation.server.test.tsx
    appWithTranslation.tsx
    index.tsx
    serverSideTranslations.test.tsx
    serverSideTranslations.ts
    types.test.ts
    types.ts
    utils.ts
.all-contributorsrc
.editorconfig
.gitignore
.npmignore
.size-limit.cjs
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
TROUBLESHOOT.md
babel.config.json
cypress.config.ts
eslint.config.mjs
jest.config.js
package.json
prettier.config.js
serverSideTranslations.d.ts
serverSideTranslations.js
tsconfig.appRouter.json
tsconfig.json
tsconfig.pagesRouter.json
tsdown.config.ts
```

## Entry points

- [src/appRouter/index.ts](https://github.com/i18next/next-i18next/blob/09a2aa0975b54cd4684dcee9ab7b77224180d338/src/appRouter/index.ts)
- [src/appRouter/proxy/index.ts](https://github.com/i18next/next-i18next/blob/09a2aa0975b54cd4684dcee9ab7b77224180d338/src/appRouter/proxy/index.ts)
- [src/appRouter/server.ts](https://github.com/i18next/next-i18next/blob/09a2aa0975b54cd4684dcee9ab7b77224180d338/src/appRouter/server.ts)
- [src/pagesRouter/index.tsx](https://github.com/i18next/next-i18next/blob/09a2aa0975b54cd4684dcee9ab7b77224180d338/src/pagesRouter/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| appRouter package | library | Observed | Groups 17 file(s) under approuter package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 1 file(s) under cypress package (observed from repository paths and static analysis). |
| pagesRouter package | library | Observed | Groups 13 file(s) under pagesrouter package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/stale.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/next-compat.yml` (ci)
- `babel.config.json` (config)
- `cypress/tsconfig.json` (config)
- `examples/app-router-icu/app/i18n/locales/de/common.json` (config)
- `examples/app-router-icu/app/i18n/locales/en/common.json` (config)
- `examples/app-router-icu/package.json` (manifest)
- `examples/app-router-icu/tsconfig.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/de/client-page.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/de/footer.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/de/second-client-page.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/de/second-page.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/de/translation.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/en/client-page.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/en/footer.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/en/second-client-page.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/en/second-page.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/en/translation.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/it/client-page.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/it/footer.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/it/second-client-page.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/it/second-page.json` (config)
- `examples/app-router-no-locale-path/app/i18n/locales/it/translation.json` (config)
- `examples/app-router-no-locale-path/package.json` (manifest)
- `examples/app-router-simple/app/i18n/locales/de/client-page.json` (config)
- `examples/app-router-simple/app/i18n/locales/de/footer.json` (config)
- `examples/app-router-simple/app/i18n/locales/de/second-client-page.json` (config)
- `examples/app-router-simple/app/i18n/locales/de/second-page.json` (config)
- `examples/app-router-simple/app/i18n/locales/de/translation.json` (config)
- `examples/app-router-simple/app/i18n/locales/en/client-page.json` (config)
- `examples/app-router-simple/app/i18n/locales/en/footer.json` (config)
- `examples/app-router-simple/app/i18n/locales/en/second-client-page.json` (config)
- `examples/app-router-simple/app/i18n/locales/en/second-page.json` (config)
- `examples/app-router-simple/app/i18n/locales/en/translation.json` (config)
- `examples/app-router-simple/app/i18n/locales/it/client-page.json` (config)
- `examples/app-router-simple/app/i18n/locales/it/footer.json` (config)
- `examples/app-router-simple/app/i18n/locales/it/second-client-page.json` (config)
- `examples/app-router-simple/app/i18n/locales/it/second-page.json` (config)
- `examples/app-router-simple/app/i18n/locales/it/translation.json` (config)
- `examples/app-router-simple/package.json` (manifest)
- `examples/app-router-simple/tsconfig.json` (config)
- `examples/mixed-routers/package.json` (manifest)
- `examples/mixed-routers/public/locales/de/common.json` (config)
- `examples/mixed-routers/public/locales/de/footer.json` (config)
- `examples/mixed-routers/public/locales/de/second-page.json` (config)
- `examples/mixed-routers/public/locales/en/common.json` (config)
- `examples/mixed-routers/public/locales/en/footer.json` (config)
- `examples/mixed-routers/public/locales/en/second-page.json` (config)
- `examples/mixed-routers/tsconfig.json` (config)
- `examples/mixed-routers/vercel.json` (config)
- `examples/pages-router-auto-static-optimize/package.json` (manifest)
- `examples/pages-router-auto-static-optimize/public/locales/de/common.json` (config)
- `examples/pages-router-auto-static-optimize/public/locales/de/footer.json` (config)
- `examples/pages-router-auto-static-optimize/public/locales/de/second-page.json` (config)
- `examples/pages-router-auto-static-optimize/public/locales/de/staticpage.json` (config)
- `examples/pages-router-auto-static-optimize/public/locales/en/common.json` (config)
- `examples/pages-router-auto-static-optimize/public/locales/en/footer.json` (config)
- `examples/pages-router-auto-static-optimize/public/locales/en/second-page.json` (config)
- `examples/pages-router-auto-static-optimize/public/locales/en/staticpage.json` (config)
- `examples/pages-router-auto-static-optimize/tsconfig.json` (config)
- `examples/pages-router-auto-static-optimize/vercel.json` (config)
- `examples/pages-router-simple/package.json` (manifest)
- `examples/pages-router-simple/public/locales/de/common.json` (config)
- `examples/pages-router-simple/public/locales/de/footer.json` (config)
- `examples/pages-router-simple/public/locales/de/second-page.json` (config)
- `examples/pages-router-simple/public/locales/en/common.json` (config)
- `examples/pages-router-simple/public/locales/en/footer.json` (config)
- `examples/pages-router-simple/public/locales/en/second-page.json` (config)
- `examples/pages-router-simple/tsconfig.json` (config)
- `examples/pages-router-simple/vercel.json` (config)
- `examples/pages-router-ssg/package.json` (manifest)
- `examples/pages-router-ssg/public/locales/de/404.json` (config)
- `examples/pages-router-ssg/public/locales/de/common.json` (config)
- `examples/pages-router-ssg/public/locales/de/footer.json` (config)
- `examples/pages-router-ssg/public/locales/de/second-page.json` (config)
- `examples/pages-router-ssg/public/locales/en/404.json` (config)
- `examples/pages-router-ssg/public/locales/en/common.json` (config)
- `examples/pages-router-ssg/public/locales/en/footer.json` (config)
- `examples/pages-router-ssg/public/locales/en/second-page.json` (config)
- `examples/pages-router-ssg/public/locales/it/404.json` (config)
- `examples/pages-router-ssg/public/locales/it/common.json` (config)
- `examples/pages-router-ssg/public/locales/it/footer.json` (config)
- `examples/pages-router-ssg/public/locales/it/second-page.json` (config)
- `package.json` (manifest)
- `tsconfig.appRouter.json` (config)
- `tsconfig.json` (config)
- `tsconfig.pagesRouter.json` (config)

## Top-level layout

- `examples` — 202 analysed file(s)
- `src` — 34 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `.github` — 3 analysed file(s)
- `.husky` — 2 analysed file(s)
- `cypress` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `09a2aa0975b54cd4684dcee9ab7b77224180d338` is the revision these paths and observations refer to.
