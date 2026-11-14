# Project structure: iib0011/omni-tools

**Analysed commit:** `9244e02923d99cde143ddd5b8d761d9ed0997da4`

**Commit reference:** [9244e02923d99cde143ddd5b8d761d9ed0997da4](https://github.com/iib0011/omni-tools/commit/9244e02923d99cde143ddd5b8d761d9ed0997da4)

**Tree at this commit:** [iib0011/omni-tools@9244e02923d9](https://github.com/iib0011/omni-tools/tree/9244e02923d99cde143ddd5b8d761d9ed0997da4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | iib0011/omni-tools |
| Description | Self-hosted collection of powerful web-based tools for everyday tasks. No ads, no tracking, just fast, accessible utilities right from your browser! |
| Stars | 10719 |
| Forks | 765 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `9244e02923d99cde143ddd5b8d761d9ed0997da4` |
| Retrieved at | 2026-11-14T19:13:30.261452+00:00 |
| Files in this snapshot | 789 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
.husky/  (1 files)
  pre-commit
.vitest/  (1 files)
  setup.ts
.vscode/  (1 files)
  settings.json
@types/  (2 files)
  i18n.d.ts
  theme.d.ts
docs-images/  (1 files)
  locizeSponsor.svg
public/  (150 files)
  assets/  (2 files)
    fonts/  (1 files)
      … 1 files under this directory
    background.svg
  locales/  (143 files)
    de/  (13 files)
      … 13 files under this directory
    en/  (13 files)
      … 13 files under this directory
    es/  (13 files)
      … 13 files under this directory
    fr/  (13 files)
      … 13 files under this directory
    hi/  (13 files)
      … 13 files under this directory
    ja/  (13 files)
      … 13 files under this directory
    nl/  (13 files)
      … 13 files under this directory
    pt/  (13 files)
      … 13 files under this directory
    ru/  (13 files)
      … 13 files under this directory
    uk/  (13 files)
      … 13 files under this directory
    zh/  (13 files)
      … 13 files under this directory
  _redirects
  favicon.svg
  gs.js
  robots.txt
  site.webmanifest
scripts/  (7 files)
  add-i18n-to-meta.js
  cleanup-empty-directories.js
  create-tool.mjs
  i18n-coverage.js
  locize-upload.js
  tools-diff-since-tag.mjs
  update-i18n-from-meta.js
src/  (609 files)
  @types/  (2 files)
    env.d.ts
    i18n.d.ts
  components/  (50 files)
    Navbar/  (1 files)
      … 1 files under this directory
    allTools/  (2 files)
      … 2 files under this directory
    examples/  (3 files)
      … 3 files under this directory
    input/  (14 files)
      … 14 files under this directory
    options/  (8 files)
      … 8 files under this directory
    result/  (6 files)
      … 6 files under this directory
    App.tsx
    BackButton.tsx
    Hero.tsx
    InputHeader.tsx
    Loading.css
    Loading.tsx
    ScrollToTopButton.tsx
    Separator.tsx
    ToolBreadcrumb.tsx
    ToolContent.tsx
    ToolHeader.tsx
    ToolInfo.tsx
    ToolInputAndResult.tsx
    ToolLayout.tsx
    UserTypeFilter.tsx
    index.css
  config/  (3 files)
    muiConfig.ts
    routesConfig.tsx
    uiConfig.ts
  contexts/  (1 files)
    CustomSnackBarContext.tsx
  datatables/  (4 files)
    data/  (2 files)
      … 2 files under this directory
    index.ts
    types.ts
  hooks/  (6 files)
    index.ts
    useDebounce.ts
    useFileDrop.ts
    usePrevious.ts
    useTimeout.ts
    useUpdateEffect.ts
  i18n/  (1 files)
    index.ts
  lib/  (4 files)
    ghostscript/  (3 files)
      … 3 files under this directory
    ffmpeg.ts
  pages/  (537 files)
    home/  (2 files)
      … 2 files under this directory
    tools/  (534 files)
      … 534 files under this directory
    tools-by-category/  (1 files)
      … 1 files under this directory
  index.tsx
.dockerignore
.editorconfig
.env.example
.eslintrc
.gitignore
.prettierrc
CODEOWNERS
Dockerfile
LICENSE
README.md
commitlint.config.js
index.html
package.json
playwright.config.ts
postcss.config.mjs
```

## Entry points

- [src/components/App.tsx](https://github.com/iib0011/omni-tools/blob/9244e02923d99cde143ddd5b8d761d9ed0997da4/src/components/App.tsx)
- [src/components/Navbar/index.tsx](https://github.com/iib0011/omni-tools/blob/9244e02923d99cde143ddd5b8d761d9ed0997da4/src/components/Navbar/index.tsx)
- [src/datatables/index.ts](https://github.com/iib0011/omni-tools/blob/9244e02923d99cde143ddd5b8d761d9ed0997da4/src/datatables/index.ts)
- [src/hooks/index.ts](https://github.com/iib0011/omni-tools/blob/9244e02923d99cde143ddd5b8d761d9ed0997da4/src/hooks/index.ts)
- [src/i18n/index.ts](https://github.com/iib0011/omni-tools/blob/9244e02923d99cde143ddd5b8d761d9ed0997da4/src/i18n/index.ts)
- [src/index.tsx](https://github.com/iib0011/omni-tools/blob/9244e02923d99cde143ddd5b8d761d9ed0997da4/src/index.tsx)
- [src/pages/home/index.tsx](https://github.com/iib0011/omni-tools/blob/9244e02923d99cde143ddd5b8d761d9ed0997da4/src/pages/home/index.tsx)
- [src/pages/tools-by-category/index.tsx](https://github.com/iib0011/omni-tools/blob/9244e02923d99cde143ddd5b8d761d9ed0997da4/src/pages/tools-by-category/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 48 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 148 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| contexts package | library | Observed | Groups 1 file(s) under contexts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 9 file(s) under data layer (observed from repository paths and static analysis). |
| datatables package | library | Observed | Groups 2 file(s) under datatables package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 6 file(s) under hooks package (observed from repository paths and static analysis). |
| i18n package | library | Observed | Groups 1 file(s) under i18n package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 4 file(s) under lib package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 530 file(s) under pages package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). |
| @types package | library | Observed | Groups 4 file(s) under @types package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `package.json` (manifest)
- `public/locales/de/audio.json` (config)
- `public/locales/de/converters.json` (config)
- `public/locales/de/csv.json` (config)
- `public/locales/de/image.json` (config)
- `public/locales/de/json.json` (config)
- `public/locales/de/list.json` (config)
- `public/locales/de/number.json` (config)
- `public/locales/de/pdf.json` (config)
- `public/locales/de/string.json` (config)
- `public/locales/de/time.json` (config)
- `public/locales/de/translation.json` (config)
- `public/locales/de/video.json` (config)
- `public/locales/de/xml.json` (config)
- `public/locales/en/audio.json` (config)
- `public/locales/en/converters.json` (config)
- `public/locales/en/csv.json` (config)
- `public/locales/en/image.json` (config)
- `public/locales/en/json.json` (config)
- `public/locales/en/list.json` (config)
- `public/locales/en/number.json` (config)
- `public/locales/en/pdf.json` (config)
- `public/locales/en/string.json` (config)
- `public/locales/en/time.json` (config)
- `public/locales/en/translation.json` (config)
- `public/locales/en/video.json` (config)
- `public/locales/en/xml.json` (config)
- `public/locales/es/audio.json` (config)
- `public/locales/es/converters.json` (config)
- `public/locales/es/csv.json` (config)
- `public/locales/es/image.json` (config)
- `public/locales/es/json.json` (config)
- `public/locales/es/list.json` (config)
- `public/locales/es/number.json` (config)
- `public/locales/es/pdf.json` (config)
- `public/locales/es/string.json` (config)
- `public/locales/es/time.json` (config)
- `public/locales/es/translation.json` (config)
- `public/locales/es/video.json` (config)
- `public/locales/es/xml.json` (config)
- `public/locales/fr/audio.json` (config)
- `public/locales/fr/converters.json` (config)
- `public/locales/fr/csv.json` (config)
- `public/locales/fr/image.json` (config)
- `public/locales/fr/json.json` (config)
- `public/locales/fr/list.json` (config)
- `public/locales/fr/number.json` (config)
- `public/locales/fr/pdf.json` (config)
- `public/locales/fr/string.json` (config)
- `public/locales/fr/time.json` (config)
- `public/locales/fr/translation.json` (config)
- `public/locales/fr/video.json` (config)
- `public/locales/fr/xml.json` (config)
- `public/locales/hi/audio.json` (config)
- `public/locales/hi/converters.json` (config)
- `public/locales/hi/csv.json` (config)
- `public/locales/hi/image.json` (config)
- `public/locales/hi/json.json` (config)
- `public/locales/hi/list.json` (config)
- `public/locales/hi/number.json` (config)
- `public/locales/hi/pdf.json` (config)
- `public/locales/hi/string.json` (config)
- `public/locales/hi/time.json` (config)
- `public/locales/hi/translation.json` (config)
- `public/locales/hi/video.json` (config)
- `public/locales/hi/xml.json` (config)
- `public/locales/ja/audio.json` (config)
- `public/locales/ja/converters.json` (config)
- `public/locales/ja/csv.json` (config)
- `public/locales/ja/image.json` (config)
- `public/locales/ja/json.json` (config)
- `public/locales/ja/list.json` (config)
- `public/locales/ja/number.json` (config)
- `public/locales/ja/pdf.json` (config)
- `public/locales/ja/string.json` (config)
- `public/locales/ja/time.json` (config)
- `public/locales/ja/translation.json` (config)
- `public/locales/ja/video.json` (config)
- `public/locales/ja/xml.json` (config)
- `public/locales/nl/audio.json` (config)
- `public/locales/nl/converters.json` (config)
- `public/locales/nl/csv.json` (config)
- `public/locales/nl/image.json` (config)
- `public/locales/nl/json.json` (config)
- `public/locales/nl/list.json` (config)
- `public/locales/nl/number.json` (config)
- `public/locales/nl/pdf.json` (config)
- `public/locales/nl/string.json` (config)
- `public/locales/nl/time.json` (config)
- `public/locales/nl/translation.json` (config)
- `public/locales/nl/video.json` (config)
- `public/locales/nl/xml.json` (config)
- `public/locales/pt/audio.json` (config)
- `public/locales/pt/converters.json` (config)
- `public/locales/pt/csv.json` (config)
- `public/locales/pt/image.json` (config)
- `public/locales/pt/json.json` (config)
- `public/locales/pt/list.json` (config)
- `public/locales/pt/number.json` (config)
- `public/locales/pt/pdf.json` (config)
- `public/locales/pt/string.json` (config)
- `public/locales/pt/time.json` (config)
- `public/locales/pt/translation.json` (config)
- `public/locales/pt/video.json` (config)
- `public/locales/pt/xml.json` (config)
- `public/locales/ru/audio.json` (config)
- `public/locales/ru/converters.json` (config)
- `public/locales/ru/csv.json` (config)
- `public/locales/ru/image.json` (config)
- `public/locales/ru/json.json` (config)
- `public/locales/ru/list.json` (config)
- `public/locales/ru/number.json` (config)
- `public/locales/ru/pdf.json` (config)
- `public/locales/ru/string.json` (config)
- `public/locales/ru/time.json` (config)
- `public/locales/ru/translation.json` (config)
- `public/locales/ru/video.json` (config)
- `public/locales/ru/xml.json` (config)
- `public/locales/uk/audio.json` (config)
- `public/locales/uk/converters.json` (config)
- `public/locales/uk/csv.json` (config)
- `public/locales/uk/image.json` (config)
- `public/locales/uk/json.json` (config)
- `public/locales/uk/list.json` (config)
- `public/locales/uk/number.json` (config)
- `public/locales/uk/pdf.json` (config)
- `public/locales/uk/string.json` (config)
- `public/locales/uk/time.json` (config)
- `public/locales/uk/translation.json` (config)
- `public/locales/uk/video.json` (config)
- `public/locales/uk/xml.json` (config)
- `public/locales/zh/audio.json` (config)
- `public/locales/zh/converters.json` (config)
- `public/locales/zh/csv.json` (config)
- `public/locales/zh/image.json` (config)
- `public/locales/zh/json.json` (config)
- `public/locales/zh/list.json` (config)
- `public/locales/zh/number.json` (config)
- `public/locales/zh/pdf.json` (config)
- `public/locales/zh/string.json` (config)
- `public/locales/zh/time.json` (config)
- `public/locales/zh/translation.json` (config)
- `public/locales/zh/video.json` (config)
- `public/locales/zh/xml.json` (config)

## Top-level layout

- `src` — 609 analysed file(s)
- `public` — 150 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `scripts` — 7 analysed file(s)
- `.github` — 2 analysed file(s)
- `@types` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.vitest` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `docs-images` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 11 file(s) were skipped during inventory (11 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9244e02923d99cde143ddd5b8d761d9ed0997da4` is the revision these paths and observations refer to.
