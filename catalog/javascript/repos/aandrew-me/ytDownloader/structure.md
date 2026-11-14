# Project structure: aandrew-me/ytDownloader

**Analysed commit:** `1381ad9417ec421fef830feb81b21479d7bed26f`

**Commit reference:** [1381ad9417ec421fef830feb81b21479d7bed26f](https://github.com/aandrew-me/ytDownloader/commit/1381ad9417ec421fef830feb81b21479d7bed26f)

**Tree at this commit:** [aandrew-me/ytDownloader@1381ad9417ec](https://github.com/aandrew-me/ytDownloader/tree/1381ad9417ec421fef830feb81b21479d7bed26f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | aandrew-me/ytDownloader |
| Description | Desktop app to download audio/video from hundreds of sites |
| Stars | 10668 |
| Forks | 942 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `1381ad9417ec421fef830feb81b21479d7bed26f` |
| Retrieved at | 2026-11-14T19:12:34.843019+00:00 |
| Files in this snapshot | 73 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    main.yml
    release_to_winget.yml
assets/  (4 files)
  css/  (2 files)
    index.css
    themes.css
  slimselect.css
  slimselect.js
flatpak/  (2 files)
  io.github.aandrew_me.ytdn.desktop
  io.github.aandrew_me.ytdn.metainfo.xml
html/  (1 files)
  index.html
src/  (11 files)
  common.js
  compressor.js
  history.js
  history_ui.js
  index.js
  logs.js
  playlist.js
  preferences.js
  renderer.js
  types.d.ts
  utils.js
tests/  (10 files)
  helpers/  (1 files)
    electronApp.js
  compressor-page-compression.spec.js
  format-video-codec.spec.js
  logs.spec.js
  main-page-downloads.spec.js
  playlist-page-downloads.spec.js
  playlist-preferences-integration.spec.js
  preferences-integration.spec.js
  preferences-page.spec.js
  translations-check.js
translations/  (25 files)
  ar-SA.json
  bn-BD.json
  de-DE.json
  el-GR.json
  en.json
  es-ES.json
  eu-ES.json
  fa-IR.json
  fi-FI.json
  fr-FR.json
  hi-IN.json
  hu-HU.json
  i18n-init.js
  i18n.js
  it-IT.json
  ja-JP.json
  ne-NP.json
  pl-PL.json
  pt-BR.json
  ru-RU.json
  tr-TR.json
  uk-UA.json
  vi-VN.json
  zh-CN.json
  … 1 more files
.gitignore
LICENSE
LICENSE.rtf
README.md
crowdin.yml
linux.sh
mac.sh
main.js
package.json
patch-snap.js
playwright.config.js
preload.js
test-appx.ps1
tsconfig.json
windows.ps1
ytdownloader.json
```

## Entry points

- [main.js](https://github.com/aandrew-me/ytDownloader/blob/1381ad9417ec421fef830feb81b21479d7bed26f/main.js)
- [src/index.js](https://github.com/aandrew-me/ytDownloader/blob/1381ad9417ec421fef830feb81b21479d7bed26f/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| common.js package | library | Observed | Groups 1 file(s) under common.js package (observed from repository paths and static analysis). |
| compressor.js package | library | Observed | Groups 1 file(s) under compressor.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 27 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| history.js package | library | Observed | Groups 1 file(s) under history.js package (observed from repository paths and static analysis). |
| history_ui.js package | library | Observed | Groups 1 file(s) under history_ui.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| logs.js package | library | Observed | Groups 1 file(s) under logs.js package (observed from repository paths and static analysis). |
| playlist.js package | library | Observed | Groups 1 file(s) under playlist.js package (observed from repository paths and static analysis). |
| preferences.js package | library | Observed | Groups 1 file(s) under preferences.js package (observed from repository paths and static analysis). |
| renderer.js package | library | Observed | Groups 1 file(s) under renderer.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). |
| translations package | library | Observed | Groups 2 file(s) under translations package (observed from repository paths and static analysis). |
| types.d.ts package | library | Observed | Groups 1 file(s) under types.d.ts package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/main.yml` (ci)
- `.github/workflows/release_to_winget.yml` (ci)
- `crowdin.yml` (config)
- `package.json` (manifest)
- `translations/ar-SA.json` (config)
- `translations/bn-BD.json` (config)
- `translations/de-DE.json` (config)
- `translations/el-GR.json` (config)
- `translations/en.json` (config)
- `translations/es-ES.json` (config)
- `translations/eu-ES.json` (config)
- `translations/fa-IR.json` (config)
- `translations/fi-FI.json` (config)
- `translations/fr-FR.json` (config)
- `translations/hi-IN.json` (config)
- `translations/hu-HU.json` (config)
- `translations/it-IT.json` (config)
- `translations/ja-JP.json` (config)
- `translations/ne-NP.json` (config)
- `translations/pl-PL.json` (config)
- `translations/pt-BR.json` (config)
- `translations/ru-RU.json` (config)
- `translations/tr-TR.json` (config)
- `translations/uk-UA.json` (config)
- `translations/vi-VN.json` (config)
- `translations/zh-CN.json` (config)
- `translations/zh-TW.json` (config)
- `tsconfig.json` (config)
- `ytdownloader.json` (config)

## Top-level layout

- `translations` — 25 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `src` — 11 analysed file(s)
- `tests` — 10 analysed file(s)
- `.github` — 4 analysed file(s)
- `assets` — 4 analysed file(s)
- `flatpak` — 2 analysed file(s)
- `html` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1381ad9417ec421fef830feb81b21479d7bed26f` is the revision these paths and observations refer to.
