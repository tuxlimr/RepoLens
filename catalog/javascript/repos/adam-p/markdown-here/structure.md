# Project structure: adam-p/markdown-here

**Analysed commit:** `e00d005299922198aef968e0cd42b275525c20a6`

**Commit reference:** [e00d005299922198aef968e0cd42b275525c20a6](https://github.com/adam-p/markdown-here/commit/e00d005299922198aef968e0cd42b275525c20a6)

**Tree at this commit:** [adam-p/markdown-here@e00d00529992](https://github.com/adam-p/markdown-here/tree/e00d005299922198aef968e0cd42b275525c20a6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | adam-p/markdown-here |
| Description | Google Chrome, Firefox, and Thunderbird extension that lets you write email in Markdown and render it before sending. |
| Stars | 60243 |
| Forks | 10980 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e00d005299922198aef968e0cd42b275525c20a6` |
| Retrieved at | 2026-11-14T19:10:36.632706+00:00 |
| Files in this snapshot | 379 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
contributors/  (5 files)
  adam-p.md
  dugite-code.md
  michaelstepner.md
  mtlynch.md
  wm8120.md
src/  (354 files)
  _locales/  (61 files)
    de/  (5 files)
      … 5 files under this directory
    en/  (1 files)
      … 1 files under this directory
    es/  (5 files)
      … 5 files under this directory
    fr/  (5 files)
      … 5 files under this directory
    it/  (5 files)
      … 5 files under this directory
    ja/  (5 files)
      … 5 files under this directory
    ko/  (5 files)
      … 5 files under this directory
    pl/  (5 files)
      … 5 files under this directory
    pt_BR/  (5 files)
      … 5 files under this directory
    ru/  (5 files)
      … 5 files under this directory
    tr/  (5 files)
      … 5 files under this directory
    zh_CN/  (5 files)
      … 5 files under this directory
    zh_TW/  (5 files)
      … 5 files under this directory
  chrome/  (5 files)
    background.html
    backgroundscript.js
    contentscript.js
    upgrade-notification-popup.html
    upgrade-notification-popup.js
  common/  (287 files)
    highlightjs/  (255 files)
      … 255 files under this directory
    images/  (3 files)
      … 3 files under this directory
    test/  (13 files)
      … 13 files under this directory
    CHANGES.md
    common-logic.js
    content-permissions.js
    default.css
    forgot-to-render-prompt.html
    jsHtmlToText.js
    markdown-here.js
    markdown-render.js
    marked.js
    mdh-html-to-text.js
    options-iframe.html
    options-iframe.js
    options-store.js
    options.html
    options.js
    utils.js
  manifest.json
store-assets/  (5 files)
  amo-reviewer-notes.txt
  description.txt
  markdown-here-image2.txt
  md-for-screenshot.md.txt
  screenshot-captions.txt
test/  (1 files)
  index.html
utils/  (2 files)
  build.js
  package.json
.eslintrc.json
.gitattributes
.gitignore
CHANGES.md
CLA-entity.md
CLA-individual.md
CONTRIBUTING.md
LICENSE
Makefile
PRIVACY.md
README.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| chrome package | library | Observed | Groups 3 file(s) under chrome package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 11 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `src/_locales/de/messages.json` (config)
- `src/_locales/en/messages.json` (config)
- `src/_locales/es/messages.json` (config)
- `src/_locales/fr/messages.json` (config)
- `src/_locales/it/messages.json` (config)
- `src/_locales/ja/messages.json` (config)
- `src/_locales/ko/messages.json` (config)
- `src/_locales/pl/messages.json` (config)
- `src/_locales/pt_BR/messages.json` (config)
- `src/_locales/ru/messages.json` (config)
- `src/_locales/tr/messages.json` (config)
- `src/_locales/zh_CN/messages.json` (config)
- `src/_locales/zh_TW/messages.json` (config)
- `src/common/highlightjs/styles/styles.json` (config)
- `src/manifest.json` (config)
- `utils/package.json` (manifest)

## Top-level layout

- `src` — 354 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `contributors` — 5 analysed file(s)
- `store-assets` — 5 analysed file(s)
- `utils` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `test` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e00d005299922198aef968e0cd42b275525c20a6` is the revision these paths and observations refer to.
