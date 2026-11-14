# Project structure: iamvishnusankar/next-sitemap

**Analysed commit:** `144fad921e8ee30f03c73ed72208bfa7355eb75d`

**Commit reference:** [144fad921e8ee30f03c73ed72208bfa7355eb75d](https://github.com/iamvishnusankar/next-sitemap/commit/144fad921e8ee30f03c73ed72208bfa7355eb75d)

**Tree at this commit:** [iamvishnusankar/next-sitemap@144fad921e8e](https://github.com/iamvishnusankar/next-sitemap/tree/144fad921e8ee30f03c73ed72208bfa7355eb75d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | iamvishnusankar/next-sitemap |
| Description | Sitemap generator for next.js. Generate sitemap(s) and robots.txt for all static/pre-rendered/dynamic/server-side pages. |
| Stars | 3751 |
| Forks | 138 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `144fad921e8ee30f03c73ed72208bfa7355eb75d` |
| Retrieved at | 2026-11-14T19:15:05.822875+00:00 |
| Files in this snapshot | 235 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    codeql-analysis.yml
    stale.yml
    test.yml
  FUNDING.yml
  dependabot.yml
.vscode/  (1 files)
  settings.json
assets/  (9 files)
  NextJS/  (4 files)
    icon/  (2 files)
      … 2 files under this directory
    logotype/  (2 files)
      … 2 files under this directory
  Vercel/  (4 files)
    icon/  (2 files)
      … 2 files under this directory
    logotype/  (2 files)
      … 2 files under this directory
  banner.svg
docs/  (69 files)
  app/  (35 files)
    api/  (1 files)
      … 1 files under this directory
    components/  (29 files)
      … 29 files under this directory
    docs/  (2 files)
      … 2 files under this directory
    examples/  (1 files)
      … 1 files under this directory
    layout.tsx
    page.tsx
  config/  (2 files)
    docs.ts
    site.ts
  content/  (13 files)
    docs/  (13 files)
      … 13 files under this directory
  hooks/  (1 files)
    use-mounted.ts
  lib/  (3 files)
    validations/  (1 files)
      … 1 files under this directory
    toc.ts
    utils.ts
  public/  (2 files)
    next.svg
    vercel.svg
  styles/  (2 files)
    globals.css
    mdx.css
  types/  (1 files)
    index.d.ts
  .eslintrc
  .gitignore
  contentlayer.config.js
  env.mjs
  next-sitemap.config.js
  next.config.js
  package.json
  postcss.config.js
  tailwind.config.js
  tsconfig.json
examples/  (95 files)
  amp/  (7 files)
    pages/  (2 files)
      … 2 files under this directory
    README.md
    next-env.d.ts
    next-sitemap.config.js
    package.json
    tsconfig.json
  app-dir/  (11 files)
    .vscode/  (1 files)
      … 1 files under this directory
    app/  (5 files)
      … 5 files under this directory
    next-env.d.ts
    next-sitemap.config.js
    next.config.js
    package.json
    tsconfig.json
  basic/  (10 files)
    pages/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    next-env.d.ts
    next-sitemap.config.js
    package.json
    tsconfig.json
  commonjs/  (10 files)
    pages/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    next-env.d.ts
    next-sitemap.config.js
    package.json
    tsconfig.json
  custom-config-file/  (10 files)
    pages/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    awesome-sitemap.config.js
    next-env.d.ts
    package.json
    tsconfig.json
  custom-overrides/  (7 files)
    pages/  (1 files)
      … 1 files under this directory
    .gitignore
    next-env.d.ts
    next-sitemap.config.js
    next.config.js
    package.json
    tsconfig.json
  custom-robots-txt-transformer/  (9 files)
    pages/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    art.js
    next-env.d.ts
    next-sitemap.config.js
    package.json
    tsconfig.json
  no-index-sitemaps/  (8 files)
    pages/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    next-env.d.ts
    next-sitemap.config.js
    package.json
    tsconfig.json
  static-export/  (12 files)
    app/  (4 files)
      … 4 files under this directory
    public/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    next-sitemap.config.js
    next.config.js
    package.json
    tsconfig.json
  with-next-sitemap-i18n/  (11 files)
    pages/  (5 files)
      … 5 files under this directory
    README.md
    next-env.d.ts
    next-sitemap.config.js
    next.config.js
    package.json
    tsconfig.json
packages/  (39 files)
  next-sitemap/  (39 files)
    bin/  (2 files)
      … 2 files under this directory
    src/  (33 files)
      … 33 files under this directory
    .npmignore
    README.md
    package.json
    tsconfig.json
.eslintignore
.eslintrc
.gitattributes
.gitignore
.prettierignore
.prettierrc
CODE_OF_CONDUCT.md
LICENSE
README.md
SECURITY.md
azure-pipeline.yml
changelog.md
package.json
tsconfig.json
turbo.json
```

## Entry points

- [packages/next-sitemap/bin/next-sitemap.mjs](https://github.com/iamvishnusankar/next-sitemap/blob/144fad921e8ee30f03c73ed72208bfa7355eb75d/packages/next-sitemap/bin/next-sitemap.mjs)
- [packages/next-sitemap/bin/next-sitemap.cjs](https://github.com/iamvishnusankar/next-sitemap/blob/144fad921e8ee30f03c73ed72208bfa7355eb75d/packages/next-sitemap/bin/next-sitemap.cjs)
- [packages/next-sitemap/src/index.ts](https://github.com/iamvishnusankar/next-sitemap/blob/144fad921e8ee30f03c73ed72208bfa7355eb75d/packages/next-sitemap/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 32 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.vscode/settings.json` (config)
- `azure-pipeline.yml` (config)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `examples/amp/package.json` (manifest)
- `examples/amp/tsconfig.json` (config)
- `examples/app-dir/.vscode/settings.json` (config)
- `examples/app-dir/package.json` (manifest)
- `examples/app-dir/tsconfig.json` (config)
- `examples/basic/package.json` (manifest)
- `examples/basic/tsconfig.json` (config)
- `examples/commonjs/package.json` (manifest)
- `examples/commonjs/tsconfig.json` (config)
- `examples/custom-config-file/package.json` (manifest)
- `examples/custom-config-file/tsconfig.json` (config)
- `examples/custom-overrides/package.json` (manifest)
- `examples/custom-overrides/tsconfig.json` (config)
- `examples/custom-robots-txt-transformer/package.json` (manifest)
- `examples/custom-robots-txt-transformer/tsconfig.json` (config)
- `examples/no-index-sitemaps/package.json` (manifest)
- `examples/no-index-sitemaps/tsconfig.json` (config)
- `examples/static-export/package.json` (manifest)
- `examples/static-export/tsconfig.json` (config)
- `examples/with-next-sitemap-i18n/package.json` (manifest)
- `examples/with-next-sitemap-i18n/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/next-sitemap/package.json` (manifest)
- `packages/next-sitemap/tsconfig.json` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)

## Top-level layout

- `examples` — 95 analysed file(s)
- `docs` — 69 analysed file(s)
- `packages` — 39 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `assets` — 9 analysed file(s)
- `.github` — 7 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `144fad921e8ee30f03c73ed72208bfa7355eb75d` is the revision these paths and observations refer to.
