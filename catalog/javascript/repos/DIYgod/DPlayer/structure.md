# Project structure: DIYgod/DPlayer

**Analysed commit:** `3d9940adc7dd3c085ee1d1ed1c20e034bc52765d`

**Commit reference:** [3d9940adc7dd3c085ee1d1ed1c20e034bc52765d](https://github.com/DIYgod/DPlayer/commit/3d9940adc7dd3c085ee1d1ed1c20e034bc52765d)

**Tree at this commit:** [DIYgod/DPlayer@3d9940adc7dd](https://github.com/DIYgod/DPlayer/tree/3d9940adc7dd3c085ee1d1ed1c20e034bc52765d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | DIYgod/DPlayer |
| Description | :lollipop: Wow, such a lovely HTML5 danmaku video player |
| Stars | 16535 |
| Forks | 2483 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `3d9940adc7dd3c085ee1d1ed1c20e034bc52765d` |
| Retrieved at | 2026-11-14T19:11:31.961022+00:00 |
| Files in this snapshot | 91 |

## Directory tree

```text
.github/  (2 files)
  FUNDING.yml
  ISSUE_TEMPLATE.md
.husky/  (1 files)
  pre-commit
demo/  (4 files)
  demo.css
  demo.js
  index.html
  modernizr.js
docs/  (17 files)
  .vuepress/  (8 files)
    components/  (1 files)
      … 1 files under this directory
    styles/  (2 files)
      … 2 files under this directory
    theme/  (4 files)
      … 4 files under this directory
    config.js
  zh/  (4 files)
    README.md
    ecosystem.md
    guide.md
    support.md
  README.md
  ecosystem.md
  guide.md
  package.json
  support.md
src/  (57 files)
  assets/  (18 files)
    airplay.svg
    camera.svg
    chromecast.svg
    comment-off.svg
    comment.svg
    full-web.svg
    full.svg
    loading.svg
    pallette.svg
    pause.svg
    play.svg
    right.svg
    send.svg
    setting.svg
    subtitle.svg
    volume-down.svg
    volume-off.svg
    volume-up.svg
  css/  (13 files)
    balloon.less
    bezel.less
    controller.less
    danmaku.less
    global.less
    index.less
    info-panel.less
    logo.less
    menu.less
    notice.less
    player.less
    subtitle.less
    video.less
  js/  (24 files)
    api.js
    bar.js
    bezel.js
    comment.js
    contextmenu.js
    controller.js
    danmaku.js
    events.js
    fullscreen.js
    hotkey.js
    i18n.js
    icons.js
    index.js
    info-panel.js
    options.js
    player.js
    setting.js
    subtitle.js
    subtitles.js
    template.js
    thumbnails.js
    timer.js
    user.js
    utils.js
  template/  (2 files)
    player.art
    video.art
webpack/  (2 files)
  dev.config.js
  prod.config.js
.gitignore
.prettierignore
.prettierrc
.travis.yml
LICENSE
README.md
package.json
tea.yaml
```

## Entry points

- [docs/.vuepress/theme/index.js](https://github.com/DIYgod/DPlayer/blob/3d9940adc7dd3c085ee1d1ed1c20e034bc52765d/docs/.vuepress/theme/index.js)
- [src/js/index.js](https://github.com/DIYgod/DPlayer/blob/3d9940adc7dd3c085ee1d1ed1c20e034bc52765d/src/js/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 2 file(s) under demo package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 24 file(s) under js package (observed from repository paths and static analysis). |
| webpack package | library | Observed | Groups 2 file(s) under webpack package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `docs/.vuepress/theme/package.json` (manifest)
- `docs/package.json` (manifest)
- `package.json` (manifest)
- `tea.yaml` (config)

## Top-level layout

- `src` — 57 analysed file(s)
- `docs` — 17 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `demo` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `webpack` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3d9940adc7dd3c085ee1d1ed1c20e034bc52765d` is the revision these paths and observations refer to.
