# Project structure: transitive-bullshit/nextjs-notion-starter-kit

**Analysed commit:** `e787e7b594f1ca6fe7445e1866d4d4668c533737`

**Commit reference:** [e787e7b594f1ca6fe7445e1866d4d4668c533737](https://github.com/transitive-bullshit/nextjs-notion-starter-kit/commit/e787e7b594f1ca6fe7445e1866d4d4668c533737)

**Tree at this commit:** [transitive-bullshit/nextjs-notion-starter-kit@e787e7b594f1](https://github.com/transitive-bullshit/nextjs-notion-starter-kit/tree/e787e7b594f1ca6fe7445e1866d4d4668c533737)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | transitive-bullshit/nextjs-notion-starter-kit |
| Description | Deploy your own Notion-powered website in minutes with Next.js and Vercel. |
| Stars | 7041 |
| Forks | 5634 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `e787e7b594f1ca6fe7445e1866d4d4668c533737` |
| Retrieved at | 2026-11-14T19:14:00.235721+00:00 |
| Files in this snapshot | 85 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (1 files)
    build.yml
  funding.yml
  issue_template.md
  pull_request_template.md
.vscode/  (2 files)
  launch.json
  settings.json
app/  (13 files)
  [pageId]/  (1 files)
    page.tsx
  api/  (2 files)
    search-notion/  (1 files)
      … 1 files under this directory
    social-image/  (1 files)
      … 1 files under this directory
  feed/  (1 files)
    route.ts
  robots.txt/  (1 files)
    route.ts
  sitemap.xml/  (1 files)
    route.ts
  error.tsx
  global-error.tsx
  layout.tsx
  loading.tsx
  not-found.tsx
  page.tsx
  providers.tsx
components/  (14 files)
  ErrorPage.tsx
  Footer.tsx
  GitHubShareButton.tsx
  Loading.tsx
  LoadingIcon.tsx
  NotionPage.tsx
  NotionPageHeader.tsx
  NotionPageRoute.tsx
  Page404.tsx
  PageActions.tsx
  PageAside.tsx
  PageSocial.module.css
  PageSocial.tsx
  styles.module.css
lib/  (31 files)
  icons/  (7 files)
    github.tsx
    like.tsx
    linkedin.tsx
    moon.tsx
    retweet.tsx
    sun.tsx
    twitter.tsx
  acl.ts
  bootstrap-client.ts
  config.ts
  db.ts
  get-canonical-page-id.ts
  get-config-value.ts
  get-page-data.ts
  get-page-tweet.ts
  get-site-map.ts
  get-social-image-url.ts
  get-tweets.ts
  map-image-url.ts
  map-page-url.ts
  notion-api.ts
  notion.ts
  oembed.ts
  page-metadata.ts
  preview-images.ts
  reset.d.ts
  resolve-notion-page.ts
  search-notion.ts
  site-config.ts
  types.ts
  use-dark-mode.ts
public/  (1 files)
  manifest.json
styles/  (3 files)
  global.css
  notion.css
  prism-theme.css
.editorconfig
.env.example
.gitignore
.prettierignore
.worktreeinclude
AGENTS.md
CODE_OF_CONDUCT.md
contributing.md
license
next.config.js
oxfmt.config.ts
oxlint.config.ts
package.json
pnpm-workspace.yaml
readme.md
site.config.ts
tsconfig.json
```

## Entry points

- [app/[pageId]/page.tsx](https://github.com/transitive-bullshit/nextjs-notion-starter-kit/blob/e787e7b594f1ca6fe7445e1866d4d4668c533737/app/%5BpageId%5D/page.tsx)
- [app/page.tsx](https://github.com/transitive-bullshit/nextjs-notion-starter-kit/blob/e787e7b594f1ca6fe7445e1866d4d4668c533737/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 11 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 12 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 31 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.env.example` (config)
- `.github/funding.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `public/manifest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `lib` — 31 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `components` — 14 analysed file(s)
- `app` — 13 analysed file(s)
- `.github` — 4 analysed file(s)
- `styles` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e787e7b594f1ca6fe7445e1866d4d4668c533737` is the revision these paths and observations refer to.
