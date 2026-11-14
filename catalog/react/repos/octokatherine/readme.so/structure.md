# Project structure: octokatherine/readme.so

**Analysed commit:** `90420ff0f33d1ef0e9cf4fd67515662ab626acee`

**Commit reference:** [90420ff0f33d1ef0e9cf4fd67515662ab626acee](https://github.com/octokatherine/readme.so/commit/90420ff0f33d1ef0e9cf4fd67515662ab626acee)

**Tree at this commit:** [octokatherine/readme.so@90420ff0f33d](https://github.com/octokatherine/readme.so/tree/90420ff0f33d1ef0e9cf4fd67515662ab626acee)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | octokatherine/readme.so |
| Description | An online drag-and-drop editor to easily build READMEs |
| Stars | 4634 |
| Forks | 362 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `90420ff0f33d1ef0e9cf4fd67515662ab626acee` |
| Retrieved at | 2026-11-14T19:14:40.265373+00:00 |
| Files in this snapshot | 117 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    deploy.yml
  copilot-instructions.md
.husky/  (2 files)
  .gitignore
  pre-commit
__tests__/  (1 files)
  editor.test.js
components/  (26 files)
  __tests__/  (11 files)
    CustomSection.test.js
    DownloadModal.test.js
    EditorColumn.test.js
    EditorPreviewContainer.test.js
    Nav.test.js
    PreviewColumn.test.js
    RawPreview.test.js
    SectionFilter.test.js
    SectionsColumn.test.js
    SortableItem.test.js
    Tabs.test.js
  icons/  (2 files)
    Close.js
    Menu.js
  ColumnHeader.js
  CustomSection.js
  DownloadModal.js
  EditPreviewContainer.js
  EditorColumn.js
  LanguageDropDown.js
  Nav.js
  PreviewColumn.js
  RawPreview.js
  SectionFilter.js
  SectionsColumn.js
  SortableItem.js
  Tabs.js
data/  (5 files)
  index.js
  section-templates-cn_CN.js
  section-templates-en_EN.js
  section-templates-pt_BR.js
  section-templates-tr_TR.js
hooks/  (2 files)
  useDeviceDetect.js
  useLocalStorage.js
pages/  (4 files)
  _app.js
  _document.js
  editor.js
  index.js
public/  (52 files)
  locales/  (38 files)
    ar/  (2 files)
      … 2 files under this directory
    bn/  (2 files)
      … 2 files under this directory
    cn/  (2 files)
      … 2 files under this directory
    de/  (2 files)
      … 2 files under this directory
    en/  (2 files)
      … 2 files under this directory
    es/  (2 files)
      … 2 files under this directory
    fil/  (2 files)
      … 2 files under this directory
    fr/  (2 files)
      … 2 files under this directory
    hi/  (2 files)
      … 2 files under this directory
    id/  (2 files)
      … 2 files under this directory
    it/  (2 files)
      … 2 files under this directory
    ja/  (2 files)
      … 2 files under this directory
    nl/  (2 files)
      … 2 files under this directory
    pt/  (2 files)
      … 2 files under this directory
    ru/  (2 files)
      … 2 files under this directory
    sw/  (2 files)
      … 2 files under this directory
    tl/  (2 files)
      … 2 files under this directory
    tr/  (2 files)
      … 2 files under this directory
    uz/  (2 files)
      … 2 files under this directory
  .nojekyll
  CNAME
  download.svg
  drag.svg
  github.svg
  heart.svg
  language.svg
  manifest.json
  readme.svg
  reset-light.svg
  reset.svg
  toggle_moon.svg
  toggle_sun.svg
  trash.svg
styles/  (1 files)
  globals.css
utils/  (1 files)
  constants.js
.babelrc
.dockerignore
.gitignore
.prettierignore
.prettierrc
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
docker-compose.yml
jest.config.js
jest.setup.js
next-i18next.config.js
next-seo.config.js
next.config.js
package.json
postcss.config.js
tailwind.config.js
template.md
```

## Entry points

- [data/index.js](https://github.com/octokatherine/readme.so/blob/90420ff0f33d1ef0e9cf4fd67515662ab626acee/data/index.js)
- [pages/index.js](https://github.com/octokatherine/readme.so/blob/90420ff0f33d1ef0e9cf4fd67515662ab626acee/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 26 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 42 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 2 file(s) under hooks package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 4 file(s) under pages package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 1 file(s) under __tests__ package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/workflows/deploy.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `public/locales/ar/common.json` (config)
- `public/locales/ar/editor.json` (config)
- `public/locales/bn/common.json` (config)
- `public/locales/bn/editor.json` (config)
- `public/locales/cn/common.json` (config)
- `public/locales/cn/editor.json` (config)
- `public/locales/de/common.json` (config)
- `public/locales/de/editor.json` (config)
- `public/locales/en/common.json` (config)
- `public/locales/en/editor.json` (config)
- `public/locales/es/common.json` (config)
- `public/locales/es/editor.json` (config)
- `public/locales/fil/common.json` (config)
- `public/locales/fil/editor.json` (config)
- `public/locales/fr/common.json` (config)
- `public/locales/fr/editor.json` (config)
- `public/locales/hi/common.json` (config)
- `public/locales/hi/editor.json` (config)
- `public/locales/id/common.json` (config)
- `public/locales/id/editor.json` (config)
- `public/locales/it/common.json` (config)
- `public/locales/it/editor.json` (config)
- `public/locales/ja/common.json` (config)
- `public/locales/ja/editor.json` (config)
- `public/locales/nl/common.json` (config)
- `public/locales/nl/editor.json` (config)
- `public/locales/pt/common.json` (config)
- `public/locales/pt/editor.json` (config)
- `public/locales/ru/common.json` (config)
- `public/locales/ru/editor.json` (config)
- `public/locales/sw/common.json` (config)
- `public/locales/sw/editor.json` (config)
- `public/locales/tl/common.json` (config)
- `public/locales/tl/editor.json` (config)
- `public/locales/tr/common.json` (config)
- `public/locales/tr/editor.json` (config)
- `public/locales/uz/common.json` (config)
- `public/locales/uz/editor.json` (config)
- `public/manifest.json` (config)

## Top-level layout

- `public` — 52 analysed file(s)
- `components` — 26 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `data` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `pages` — 4 analysed file(s)
- `.husky` — 2 analysed file(s)
- `hooks` — 2 analysed file(s)
- `__tests__` — 1 analysed file(s)
- `styles` — 1 analysed file(s)
- `utils` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `90420ff0f33d1ef0e9cf4fd67515662ab626acee` is the revision these paths and observations refer to.
