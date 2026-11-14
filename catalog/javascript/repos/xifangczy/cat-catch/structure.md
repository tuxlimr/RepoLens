# Project structure: xifangczy/cat-catch

**Analysed commit:** `019c465794b5871701383e4485c0e9ee7be2f840`

**Commit reference:** [019c465794b5871701383e4485c0e9ee7be2f840](https://github.com/xifangczy/cat-catch/commit/019c465794b5871701383e4485c0e9ee7be2f840)

**Tree at this commit:** [xifangczy/cat-catch@019c465794b5](https://github.com/xifangczy/cat-catch/tree/019c465794b5871701383e4485c0e9ee7be2f840)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xifangczy/cat-catch |
| Description | 猫抓 浏览器资源嗅探扩展 / cat-catch Browser Resource Sniffing Extension |
| Stars | 22956 |
| Forks | 1989 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `019c465794b5871701383e4485c0e9ee7be2f840` |
| Retrieved at | 2026-11-14T19:11:05.601632+00:00 |
| Files in this snapshot | 85 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug.yaml
    功能-添加-修改-增强-请求.md
  FUNDING.yml
_locales/  (11 files)
  en/  (1 files)
    messages.json
  es/  (1 files)
    messages.json
  fr/  (1 files)
    messages.json
  ja/  (1 files)
    messages.json
  ko/  (1 files)
    messages.json
  pt_BR/  (1 files)
    messages.json
  ru/  (1 files)
    messages.json
  tr/  (1 files)
    messages.json
  vi/  (1 files)
    messages.json
  zh_CN/  (1 files)
    messages.json
  zh_TW/  (1 files)
    messages.json
catch-script/  (6 files)
  catch.js
  i18n.js
  recorder.js
  recorder2.js
  search.js
  webrtc.js
css/  (6 files)
  install.css
  mobile.css
  options.css
  popup.css
  preview.css
  public.css
img/  (17 files)
  delete-dark.svg
  delete.svg
  download-dark.svg
  download.svg
  invoke-dark.svg
  invoke.svg
  mqtt-dark.svg
  mqtt.svg
  music.svg
  retry-dark.svg
  retry.svg
  send-dark.svg
  send.svg
  send2ffmpeg-dark.svg
  send2ffmpeg.svg
  stop-dark.svg
  stop.svg
js/  (18 files)
  background.js
  content-script.js
  downloader.js
  function.js
  i18n.js
  init.js
  install.js
  json.js
  m3u8.downloader.js
  m3u8.js
  media-control.js
  mpd.js
  options.js
  polyfill.js
  popup-utils.js
  popup.js
  preview.js
  templates.js
lib/  (5 files)
  StreamSaver.js
  base64.js
  jquery.json-viewer.js
  m3u8-decrypt.js
  third-party-libraries.md
tools/  (1 files)
  sync-locales.js
.gitignore
CHANGELOG.md
LICENSE
README.md
README_en.md
README_es.md
README_ru.md
downloader.html
install.html
json.html
justfile
m3u8.html
manifest.firefox.json
manifest.json
mpd.html
options.html
popup.html
preview.html
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| catch-script package | library | Observed | Groups 6 file(s) under catch-script package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 18 file(s) under js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 4 file(s) under lib package (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug.yaml` (config)
- `_locales/en/messages.json` (config)
- `_locales/es/messages.json` (config)
- `_locales/fr/messages.json` (config)
- `_locales/ja/messages.json` (config)
- `_locales/ko/messages.json` (config)
- `_locales/pt_BR/messages.json` (config)
- `_locales/ru/messages.json` (config)
- `_locales/tr/messages.json` (config)
- `_locales/vi/messages.json` (config)
- `_locales/zh_CN/messages.json` (config)
- `_locales/zh_TW/messages.json` (config)
- `manifest.firefox.json` (config)
- `manifest.json` (config)

## Top-level layout

- `(root files)` — 18 analysed file(s)
- `js` — 18 analysed file(s)
- `img` — 17 analysed file(s)
- `_locales` — 11 analysed file(s)
- `catch-script` — 6 analysed file(s)
- `css` — 6 analysed file(s)
- `lib` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `tools` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `019c465794b5871701383e4485c0e9ee7be2f840` is the revision these paths and observations refer to.
