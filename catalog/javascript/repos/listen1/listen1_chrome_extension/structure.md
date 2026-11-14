# Project structure: listen1/listen1_chrome_extension

**Analysed commit:** `3f24efa045125875a609dcb0f3f3f0be4edb8b37`

**Commit reference:** [3f24efa045125875a609dcb0f3f3f0be4edb8b37](https://github.com/listen1/listen1_chrome_extension/commit/3f24efa045125875a609dcb0f3f3f0be4edb8b37)

**Tree at this commit:** [listen1/listen1_chrome_extension@3f24efa04512](https://github.com/listen1/listen1_chrome_extension/tree/3f24efa045125875a609dcb0f3f3f0be4edb8b37)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | listen1/listen1_chrome_extension |
| Description | one for all free music in china (chrome extension, also works for firefox) |
| Stars | 12123 |
| Forks | 2041 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `3f24efa045125875a609dcb0f3f3f0be4edb8b37` |
| Retrieved at | 2026-11-14T19:12:10.175121+00:00 |
| Files in this snapshot | 60 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    eslint.yml
css/  (12 files)
  common.css
  common2.css
  cover.css
  hotkeys.css
  icon.css
  iparanoid.css
  iparanoid2.css
  notyf_custom.css
  origin.css
  origin2.css
  player.css
  reset.css
fonts/  (1 files)
  listen1-icon.svg
i18n/  (6 files)
  en-US.json
  fr-FR.json
  ko-KR.json
  pt-BR.json
  zh-CN.json
  zh-TC.json
images/  (2 files)
  feather-sprite.svg
  loading.svg
js/  (28 files)
  controller/  (8 files)
    auth.js
    instant_search.js
    my_playlist.js
    navigation.js
    platform.js
    play.js
    playlist.js
    profile.js
  provider/  (9 files)
    bilibili.js
    kugou.js
    kuwo.js
    localmusic.js
    migu.js
    netease.js
    qq.js
    taihe.js
    xiami.js
  app.js
  background.js
  bridge.js
  github.js
  l1_player.js
  lastfm.js
  loweb.js
  lowebutil.js
  myplaylist.js
  oauth_callback.js
  player_thread.js
.eslintrc.json
.gitignore
.prettierrc
LICENSE
README.md
README_EN.md
manifest.json
manifest_firefox.json
package.json
rules_1.json
```

## Entry points

- [js/app.js](https://github.com/listen1/listen1_chrome_extension/blob/3f24efa045125875a609dcb0f3f3f0be4edb8b37/js/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 28 file(s) under js package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/workflows/eslint.yml` (ci)
- `i18n/en-US.json` (config)
- `i18n/fr-FR.json` (config)
- `i18n/ko-KR.json` (config)
- `i18n/pt-BR.json` (config)
- `i18n/zh-CN.json` (config)
- `i18n/zh-TC.json` (config)
- `manifest.json` (config)
- `manifest_firefox.json` (config)
- `package.json` (manifest)
- `rules_1.json` (config)

## Top-level layout

- `js` — 28 analysed file(s)
- `css` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `i18n` — 6 analysed file(s)
- `images` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `fonts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x generated/minified file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3f24efa045125875a609dcb0f3f3f0be4edb8b37` is the revision these paths and observations refer to.
