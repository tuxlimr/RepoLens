# Project structure: rahuldkjain/github-profile-readme-generator

**Analysed commit:** `5ae90bfcbd7ab2f69809b094601f7975c32ae077`

**Commit reference:** [5ae90bfcbd7ab2f69809b094601f7975c32ae077](https://github.com/rahuldkjain/github-profile-readme-generator/commit/5ae90bfcbd7ab2f69809b094601f7975c32ae077)

**Tree at this commit:** [rahuldkjain/github-profile-readme-generator@5ae90bfcbd7a](https://github.com/rahuldkjain/github-profile-readme-generator/tree/5ae90bfcbd7ab2f69809b094601f7975c32ae077)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | rahuldkjain/github-profile-readme-generator |
| Description | 🚀 Generate GitHub profile README easily with the latest add-ons like visitors count, GitHub stats, etc using minimal UI. |
| Stars | 24481 |
| Forks | 8422 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `5ae90bfcbd7ab2f69809b094601f7975c32ae077` |
| Retrieved at | 2026-11-14T19:13:06.236710+00:00 |
| Files in this snapshot | 284 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature-enhancement-request.md
    feature_request.md
  workflows/  (1 files)
    deploy.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  config.yml
.husky/  (1 files)
  pre-commit
public/  (2 files)
  manifest.json
  robots.txt
src/  (249 files)
  app/  (8 files)
    about/  (1 files)
      … 1 files under this directory
    addons/  (1 files)
      … 1 files under this directory
    support/  (1 files)
      … 1 files under this directory
    globals.css
    layout.tsx
    page.tsx
    robots.ts
    sitemap.ts
  components/  (24 files)
    analytics/  (1 files)
      … 1 files under this directory
    forms/  (6 files)
      … 6 files under this directory
    layout/  (3 files)
      … 3 files under this directory
    sections/  (4 files)
      … 4 files under this directory
    ui/  (10 files)
      … 10 files under this directory
  constants/  (2 files)
    defaults.ts
    skills.ts
  hooks/  (3 files)
    use-consent.ts
    use-local-storage.ts
    use-theme.ts
  images/  (197 files)
    icons/  (197 files)
      … 197 files under this directory
  lib/  (7 files)
    analytics.ts
    asset-path.ts
    github-api.ts
    markdown-generator.ts
    storage.ts
    store.ts
    validations.ts
  markdown-pages/  (3 files)
    about.md
    addons.md
    support.md
  styles/  (1 files)
    tailwind.css
  test/  (1 files)
    setup.ts
  types/  (3 files)
    profile.ts
    skills.ts
    theme.ts
.all-contributorsrc
.eslintignore
.eslintrc.json
.gitignore
.prettierignore
.prettierrc
CHANGELOG.md
CHEATSHEET.md
CODE_OF_CONDUCT.md
CODE_STYLE_GUIDE.md
COMMIT_CONVENTION.md
CONTRIBUTING.md
DEPLOYMENT.md
LICENSE
README.md
env.example
eslint.config.mjs
next.config.ts
package.json
postcss.config.mjs
setupTests.js
tailwind.config.js
tailwind.config.ts
tsconfig.json
… 1 more files
```

## Entry points

- [src/app/about/page.tsx](https://github.com/rahuldkjain/github-profile-readme-generator/blob/5ae90bfcbd7ab2f69809b094601f7975c32ae077/src/app/about/page.tsx)
- [src/app/addons/page.tsx](https://github.com/rahuldkjain/github-profile-readme-generator/blob/5ae90bfcbd7ab2f69809b094601f7975c32ae077/src/app/addons/page.tsx)
- [src/app/page.tsx](https://github.com/rahuldkjain/github-profile-readme-generator/blob/5ae90bfcbd7ab2f69809b094601f7975c32ae077/src/app/page.tsx)
- [src/app/support/page.tsx](https://github.com/rahuldkjain/github-profile-readme-generator/blob/5ae90bfcbd7ab2f69809b094601f7975c32ae077/src/app/support/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 7 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 24 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants package | library | Observed | Groups 2 file(s) under constants package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 3 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 7 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 3 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/config.yml` (config)
- `.github/workflows/deploy.yml` (ci)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 249 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `.github` — 7 analysed file(s)
- `public` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5ae90bfcbd7ab2f69809b094601f7975c32ae077` is the revision these paths and observations refer to.
