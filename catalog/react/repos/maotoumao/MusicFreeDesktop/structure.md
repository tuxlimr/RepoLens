# Project structure: maotoumao/MusicFreeDesktop

**Analysed commit:** `f3b526a6c1ea9313b277810a8e12003605a98982`

**Commit reference:** [f3b526a6c1ea9313b277810a8e12003605a98982](https://github.com/maotoumao/MusicFreeDesktop/commit/f3b526a6c1ea9313b277810a8e12003605a98982)

**Tree at this commit:** [maotoumao/MusicFreeDesktop@f3b526a6c1ea](https://github.com/maotoumao/MusicFreeDesktop/tree/f3b526a6c1ea9313b277810a8e12003605a98982)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | maotoumao/MusicFreeDesktop |
| Description | 插件化、定制化、无广告的免费音乐播放器 |
| Stars | 9151 |
| Forks | 892 |
| Licence | AGPL-3.0 |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `f3b526a6c1ea9313b277810a8e12003605a98982` |
| Retrieved at | 2026-11-14T19:13:36.142542+00:00 |
| Files in this snapshot | 475 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    build.yml
    release.yml
  PULL_REQUEST_TEMPLATE.md
.husky/  (1 files)
  pre-commit
.vscode/  (1 files)
  settings.json
config/  (4 files)
  webpack.main.config.ts
  webpack.plugins.ts
  webpack.renderer.config.ts
  webpack.rules.ts
release/  (2 files)
  build-windows.iss
  version.json
res/  (4 files)
  .service/  (1 files)
    request-forwarder.js
  lang/  (3 files)
    en-US.json
    zh-CN.json
    zh-TW.json
scripts/  (1 files)
  feishu-upload.js
src/  (451 files)
  assets/  (67 files)
    icons/  (67 files)
      … 67 files under this directory
  common/  (17 files)
    async-memoize.ts
    camel-to-snake.ts
    constant.ts
    debounce.ts
    event-wrapper.ts
    file-util.ts
    get-resource-path.ts
    index-map.ts
    is-renderer.ts
    media-util.ts
    normalize-util.ts
    safe-serialization.ts
    store.ts
    thumb-bar-util.ts
    time-util.ts
    unique-map.ts
    void-callback.ts
  hooks/  (6 files)
    useAppConfig.ts
    useLocalFonts.ts
    useMediaDevices.ts
    useMounted.ts
    useStateRef.ts
    useVirtualList.ts
  main/  (5 files)
    deep-link/  (1 files)
      … 1 files under this directory
    native_modules/  (1 files)
      … 1 files under this directory
    tray-manager/  (1 files)
      … 1 files under this directory
    window-manager/  (1 files)
      … 1 files under this directory
    index.ts
  preload/  (3 files)
    common-preload.ts
    extension.ts
    index.ts
  renderer/  (274 files)
    components/  (104 files)
      … 104 files under this directory
    core/  (22 files)
      … 22 files under this directory
    document/  (12 files)
      … 12 files under this directory
    pages/  (121 files)
      … 121 files under this directory
    utils/  (13 files)
      … 13 files under this directory
    app.scss
    app.tsx
  renderer-lrc/  (6 files)
    document/  (4 files)
      … 4 files under this directory
    pages/  (2 files)
      … 2 files under this directory
  renderer-minimode/  (6 files)
    document/  (4 files)
      … 4 files under this directory
    pages/  (2 files)
      … 2 files under this directory
  shared/  (50 files)
    app-config/  (4 files)
      … 4 files under this directory
    database/  (4 files)
      … 4 files under this directory
    global-context/  (5 files)
      … 5 files under this directory
    i18n/  (4 files)
      … 4 files under this directory
    logger/  (2 files)
      … 2 files under this directory
    message-bus/  (6 files)
      … 6 files under this directory
    plugin-manager/  (8 files)
      … 8 files under this directory
    service-manager/  (4 files)
      … 4 files under this directory
    short-cut/  (3 files)
      … 3 files under this directory
    themepack/  (4 files)
      … 4 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    window-drag/  (3 files)
      … 3 files under this directory
  types/  (11 files)
    main/  (1 files)
      … 1 files under this directory
    app-config.d.ts
    assets.d.ts
    audio-controller.d.ts
    common.d.ts
    media.d.ts
    model.d.ts
    plugin.d.ts
    preload.d.ts
    user-perference.d.ts
    window.d.ts
  webworkers/  (6 files)
    db-worker/  (3 files)
      … 3 files under this directory
    db-worker.ts
    downloader.ts
    local-file-watcher.ts
.gitignore
LICENSE
README.md
changelog.md
eslint.config.mjs
forge.config.ts
package.json
tsconfig.json
```

## Entry points

- [src/main/deep-link/index.ts](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/main/deep-link/index.ts)
- [src/main/index.ts](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/main/index.ts)
- [src/main/tray-manager/index.ts](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/main/tray-manager/index.ts)
- [src/main/window-manager/index.ts](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/main/window-manager/index.ts)
- [src/preload/index.ts](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/preload/index.ts)
- [src/renderer-lrc/document/index.tsx](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/renderer-lrc/document/index.tsx)
- [src/renderer-lrc/pages/index.tsx](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/renderer-lrc/pages/index.tsx)
- [src/renderer-minimode/document/index.tsx](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/renderer-minimode/document/index.tsx)
- [src/renderer-minimode/pages/index.tsx](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/renderer-minimode/pages/index.tsx)
- [src/renderer/app.tsx](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/renderer/app.tsx)
- [src/renderer/document/index.tsx](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/renderer/document/index.tsx)
- [src/shared/app-config/main.ts](https://github.com/maotoumao/MusicFreeDesktop/blob/f3b526a6c1ea9313b277810a8e12003605a98982/src/shared/app-config/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 68 file(s) under api layer (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 17 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 6 file(s) under hooks package (observed from repository paths and static analysis). |
| main package | library | Observed | Groups 5 file(s) under main package (observed from repository paths and static analysis). |
| preload package | library | Observed | Groups 3 file(s) under preload package (observed from repository paths and static analysis). |
| renderer package | library | Observed | Groups 83 file(s) under renderer package (observed from repository paths and static analysis). |
| renderer-lrc package | library | Observed | Groups 3 file(s) under renderer-lrc package (observed from repository paths and static analysis). |
| renderer-minimode package | library | Observed | Groups 3 file(s) under renderer-minimode package (observed from repository paths and static analysis). |
| res package | library | Observed | Groups 1 file(s) under res package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 21 file(s) under service / domain layer (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 46 file(s) under shared package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 11 file(s) under types package (observed from repository paths and static analysis). |
| webworkers package | library | Observed | Groups 6 file(s) under webworkers package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/build.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `release/version.json` (config)
- `res/lang/en-US.json` (config)
- `res/lang/zh-CN.json` (config)
- `res/lang/zh-TW.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 451 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `config` — 4 analysed file(s)
- `res` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `release` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f3b526a6c1ea9313b277810a8e12003605a98982` is the revision these paths and observations refer to.
