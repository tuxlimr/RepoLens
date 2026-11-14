# Project structure: giscus/giscus

**Analysed commit:** `3d6430237108ca4ee3eb6a1a20595201c09c72d5`

**Commit reference:** [3d6430237108ca4ee3eb6a1a20595201c09c72d5](https://github.com/giscus/giscus/commit/3d6430237108ca4ee3eb6a1a20595201c09c72d5)

**Tree at this commit:** [giscus/giscus@3d6430237108](https://github.com/giscus/giscus/tree/3d6430237108ca4ee3eb6a1a20595201c09c72d5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | giscus/giscus |
| Description | A commenting system powered by GitHub Discussions. :octocat: :speech_balloon: :gem: |
| Stars | 12221 |
| Forks | 489 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `3d6430237108ca4ee3eb6a1a20595201c09c72d5` |
| Retrieved at | 2026-11-14T19:13:21.202272+00:00 |
| Files in this snapshot | 227 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
  dependabot.yml
components/  (7 files)
  Comment.tsx
  CommentBox.tsx
  Configuration.tsx
  Giscus.tsx
  ReactButtons.tsx
  Reply.tsx
  Widget.tsx
lib/  (19 files)
  oauth/  (2 files)
    encryption.ts
    state.ts
  types/  (5 files)
    adapter.ts
    cache.ts
    common.ts
    giscus.ts
    github.ts
  adapter.ts
  config.ts
  context.ts
  cors.ts
  fetcher.ts
  hooks.ts
  i18n.tsx
  jwt.ts
  messages.ts
  reactions.ts
  utils.ts
  variables.ts
locales/  (70 files)
  ar/  (2 files)
    common.json
    config.json
  be/  (2 files)
    common.json
    config.json
  bg/  (2 files)
    common.json
    config.json
  ca/  (2 files)
    common.json
    config.json
  cs/  (2 files)
    common.json
    config.json
  da/  (2 files)
    common.json
    config.json
  de/  (2 files)
    common.json
    config.json
  en/  (2 files)
    common.json
    config.json
  eo/  (2 files)
    common.json
    config.json
  es/  (2 files)
    common.json
    config.json
  eu/  (2 files)
    common.json
    config.json
  fa/  (2 files)
    common.json
    config.json
  fr/  (2 files)
    common.json
    config.json
  gr/  (2 files)
    common.json
    config.json
  hbs/  (2 files)
    common.json
    config.json
  he/  (2 files)
    common.json
    config.json
  hu/  (2 files)
    common.json
    config.json
  id/  (2 files)
    common.json
    config.json
  it/  (2 files)
    common.json
    config.json
  ja/  (2 files)
    common.json
    config.json
  kh/  (2 files)
    common.json
    config.json
  ko/  (2 files)
    common.json
    config.json
  nl/  (2 files)
    common.json
    config.json
  pl/  (2 files)
    common.json
    config.json
  pt/  (2 files)
    common.json
    config.json
  ro/  (2 files)
    common.json
    config.json
  ru/  (2 files)
    common.json
    config.json
  th/  (2 files)
    common.json
    config.json
  tr/  (2 files)
    common.json
    config.json
  uk/  (2 files)
    common.json
    config.json
  uz/  (2 files)
    common.json
    config.json
  vi/  (2 files)
    common.json
    config.json
  zh-CN/  (2 files)
    common.json
    config.json
  zh-HK/  (2 files)
    common.json
    config.json
  zh-TW/  (2 files)
    common.json
    config.json
pages/  (10 files)
  api/  (6 files)
    discussions/  (2 files)
      … 2 files under this directory
    oauth/  (3 files)
      … 3 files under this directory
    webhook.ts
  _app.tsx
  _document.tsx
  index.tsx
  widget.tsx
public/  (6 files)
  attribution.txt
  default.css
  giscus.svg
  powered-by-vercel.svg
  robots.txt
  site.webmanifest
services/  (21 files)
  cache/  (4 files)
    index.ts
    postgrest.ts
    supabase.ts
    valkey.ts
  giscus/  (4 files)
    categories.ts
    createDiscussion.ts
    discussions.ts
    token.ts
  github/  (12 files)
    addDiscussionComment.ts
    addDiscussionReply.ts
    createDiscussion.ts
    getAppAccessToken.ts
    getConfig.ts
    getDiscussion.ts
    getDiscussionCategories.ts
    getFile.ts
    markdown.ts
    oauth.ts
    toggleReaction.ts
    toggleUpvote.ts
  config.ts
styles/  (29 files)
  themes/  (27 files)
    catppuccin_frappe.css
    catppuccin_latte.css
    catppuccin_macchiato.css
    catppuccin_mocha.css
    cobalt.css
    custom_example.css
    dark.css
    dark_dimmed.css
    dark_high_contrast.css
    dark_protanopia.css
    dark_tritanopia.css
    fro.css
    gruvbox.css
    gruvbox_dark.css
    gruvbox_light.css
    light.css
    light_high_contrast.css
    light_protanopia.css
    light_tritanopia.css
    noborder_dark.css
    noborder_gray.css
    noborder_light.css
    postcss.config.js
    preferred_color_scheme.css
    … 3 more files
  base.css
  globals.css
.editorconfig
.env.example
.eslintrc.js
.gitattributes
.gitignore
.gitmodules
.prettierignore
.stylelintignore
.stylelintrc.js
ADVANCED-USAGE.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
PRIVACY-POLICY.md
README.ar.md
README.be.md
README.bg.md
README.ca.md
README.cs.md
README.da.md
README.de.md
README.eo.md
README.es.md
README.eu.md
… 38 more files
```

## Entry points

- [pages/api/discussions/index.ts](https://github.com/giscus/giscus/blob/3d6430237108ca4ee3eb6a1a20595201c09c72d5/pages/api/discussions/index.ts)
- [pages/index.tsx](https://github.com/giscus/giscus/blob/3d6430237108ca4ee3eb6a1a20595201c09c72d5/pages/index.tsx)
- [services/cache/index.ts](https://github.com/giscus/giscus/blob/3d6430237108ca4ee3eb6a1a20595201c09c72d5/services/cache/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 6 file(s) under api layer (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 7 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 75 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 19 file(s) under lib package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 4 file(s) under pages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 21 file(s) under service / domain layer (observed from repository paths and static analysis). |
| styles package | library | Observed | Groups 2 file(s) under styles package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `giscus.json` (config)
- `i18n.fallbacks.json` (config)
- `locales/ar/common.json` (config)
- `locales/ar/config.json` (config)
- `locales/be/common.json` (config)
- `locales/be/config.json` (config)
- `locales/bg/common.json` (config)
- `locales/bg/config.json` (config)
- `locales/ca/common.json` (config)
- `locales/ca/config.json` (config)
- `locales/cs/common.json` (config)
- `locales/cs/config.json` (config)
- `locales/da/common.json` (config)
- `locales/da/config.json` (config)
- `locales/de/common.json` (config)
- `locales/de/config.json` (config)
- `locales/en/common.json` (config)
- `locales/en/config.json` (config)
- `locales/eo/common.json` (config)
- `locales/eo/config.json` (config)
- `locales/es/common.json` (config)
- `locales/es/config.json` (config)
- `locales/eu/common.json` (config)
- `locales/eu/config.json` (config)
- `locales/fa/common.json` (config)
- `locales/fa/config.json` (config)
- `locales/fr/common.json` (config)
- `locales/fr/config.json` (config)
- `locales/gr/common.json` (config)
- `locales/gr/config.json` (config)
- `locales/hbs/common.json` (config)
- `locales/hbs/config.json` (config)
- `locales/he/common.json` (config)
- `locales/he/config.json` (config)
- `locales/hu/common.json` (config)
- `locales/hu/config.json` (config)
- `locales/id/common.json` (config)
- `locales/id/config.json` (config)
- `locales/it/common.json` (config)
- `locales/it/config.json` (config)
- `locales/ja/common.json` (config)
- `locales/ja/config.json` (config)
- `locales/kh/common.json` (config)
- `locales/kh/config.json` (config)
- `locales/ko/common.json` (config)
- `locales/ko/config.json` (config)
- `locales/nl/common.json` (config)
- `locales/nl/config.json` (config)
- `locales/pl/common.json` (config)
- `locales/pl/config.json` (config)
- `locales/pt/common.json` (config)
- `locales/pt/config.json` (config)
- `locales/ro/common.json` (config)
- `locales/ro/config.json` (config)
- `locales/ru/common.json` (config)
- `locales/ru/config.json` (config)
- `locales/th/common.json` (config)
- `locales/th/config.json` (config)
- `locales/tr/common.json` (config)
- `locales/tr/config.json` (config)
- `locales/uk/common.json` (config)
- `locales/uk/config.json` (config)
- `locales/uz/common.json` (config)
- `locales/uz/config.json` (config)
- `locales/vi/common.json` (config)
- `locales/vi/config.json` (config)
- `locales/zh-CN/common.json` (config)
- `locales/zh-CN/config.json` (config)
- `locales/zh-HK/common.json` (config)
- `locales/zh-HK/config.json` (config)
- `locales/zh-TW/common.json` (config)
- `locales/zh-TW/config.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `locales` — 70 analysed file(s)
- `(root files)` — 62 analysed file(s)
- `styles` — 29 analysed file(s)
- `services` — 21 analysed file(s)
- `lib` — 19 analysed file(s)
- `pages` — 10 analysed file(s)
- `components` — 7 analysed file(s)
- `public` — 6 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (1 x lockfile excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3d6430237108ca4ee3eb6a1a20595201c09c72d5` is the revision these paths and observations refer to.
