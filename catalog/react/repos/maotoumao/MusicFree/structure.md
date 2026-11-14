# Project structure: maotoumao/MusicFree

**Analysed commit:** `d118b18b3d0c904400f7eea7bf99c0ceec6c1aee`

**Commit reference:** [d118b18b3d0c904400f7eea7bf99c0ceec6c1aee](https://github.com/maotoumao/MusicFree/commit/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee)

**Tree at this commit:** [maotoumao/MusicFree@d118b18b3d0c](https://github.com/maotoumao/MusicFree/tree/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | maotoumao/MusicFree |
| Description | 插件化、定制化、无广告的免费音乐播放器 |
| Stars | 28558 |
| Forks | 2031 |
| Licence | AGPL-3.0 |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `d118b18b3d0c904400f7eea7bf99c0ceec6c1aee` |
| Retrieved at | 2026-11-14T19:13:03.624539+00:00 |
| Files in this snapshot | 442 |

## Directory tree

```text
.bundle/  (1 files)
  config
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report_zh.yaml
    config.yml
    feature_request_zh.yaml
  workflows/  (1 files)
    build-beta.yml
.husky/  (2 files)
  commit-msg
  pre-commit
android/  (27 files)
  app/  (21 files)
    src/  (19 files)
      … 19 files under this directory
    build.gradle
    proguard-rules.pro
  gradle/  (1 files)
    wrapper/  (1 files)
      … 1 files under this directory
  build.gradle
  gradle.properties
  gradlew
  gradlew.bat
  settings.gradle
generator/  (1 files)
  generate-assets.mjs
ios/  (14 files)
  MusicFree/  (8 files)
    Images.xcassets/  (2 files)
      … 2 files under this directory
    AppDelegate.h
    AppDelegate.mm
    Info.plist
    LaunchScreen.storyboard
    PrivacyInfo.xcprivacy
    main.m
  MusicFree.xcodeproj/  (2 files)
    xcshareddata/  (1 files)
      … 1 files under this directory
    project.pbxproj
  MusicFreeTests/  (2 files)
    Info.plist
    MusicFreeNewTests.m
  .xcode.env
  Podfile
release/  (1 files)
  version.json
src/  (374 files)
  assets/  (73 files)
    icons/  (73 files)
      … 73 files under this directory
  components/  (98 files)
    base/  (36 files)
      … 36 files under this directory
    debug/  (1 files)
      … 1 files under this directory
    dialogs/  (13 files)
      … 13 files under this directory
    errorBoundary/  (1 files)
      … 1 files under this directory
    mediaItem/  (6 files)
      … 6 files under this directory
    musicBar/  (2 files)
      … 2 files under this directory
    musicList/  (1 files)
      … 1 files under this directory
    musicSheetPage/  (4 files)
      … 4 files under this directory
    panels/  (34 files)
      … 34 files under this directory
  constants/  (6 files)
    assetsConst.ts
    commonConst.ts
    globalStyle.ts
    pathConst.ts
    repeatModeConst.ts
    uiConst.ts
  core/  (23 files)
    i18n/  (4 files)
      … 4 files under this directory
    musicSheet/  (4 files)
      … 4 files under this directory
    pluginManager/  (3 files)
      … 3 files under this directory
    router/  (2 files)
      … 2 files under this directory
    trackPlayer/  (1 files)
      … 1 files under this directory
    appConfig.ts
    appMeta.ts
    backup.ts
    downloader.ts
    localMusicSheet.ts
    lyricManager.ts
    mediaCache.ts
    musicHistory.ts
    theme.ts
  core.defination/  (1 files)
    trackPlayer/  (1 files)
      … 1 files under this directory
  entry/  (4 files)
    bootstrap/  (3 files)
      … 3 files under this directory
    index.tsx
  hooks/  (11 files)
    useCheckUpdate.ts
    useColors.ts
    useDelayFalsy.ts
    useHardwareBack.ts
    useLogRerender.ts
    useMounted.ts
    useOnceEffect.ts
    useOrientation.ts
    usePrimaryColor.ts
    useRerender.ts
    useTextColor.ts
  lib/  (7 files)
    react-native-vdebug/  (7 files)
      … 7 files under this directory
  native/  (3 files)
    lyricUtil/  (1 files)
      … 1 files under this directory
    mp3Util/  (1 files)
      … 1 files under this directory
    utils/  (1 files)
      … 1 files under this directory
  pages/  (102 files)
    albumDetail/  (2 files)
      … 2 files under this directory
    artistDetail/  (9 files)
      … 9 files under this directory
    downloading/  (2 files)
      … 2 files under this directory
    fileSelector/  (2 files)
      … 2 files under this directory
    history/  (1 files)
      … 1 files under this directory
    home/  (9 files)
      … 9 files under this directory
    localMusic/  (3 files)
      … 3 files under this directory
    musicDetail/  (14 files)
      … 14 files under this directory
    musicListEditor/  (5 files)
      … 5 files under this directory
    permissions/  (1 files)
      … 1 files under this directory
    pluginSheetDetail/  (2 files)
      … 2 files under this directory
    recommendSheets/  (6 files)
      … 6 files under this directory
    searchMusicList/  (2 files)
      … 2 files under this directory
    searchPage/  (15 files)
      … 15 files under this directory
    setCustomTheme/  (2 files)
      … 2 files under this directory
    setting/  (15 files)
      … 15 files under this directory
    sheetDetail/  (4 files)
      … 4 files under this directory
    topList/  (6 files)
      … 6 files under this directory
    topListDetail/  (2 files)
      … 2 files under this directory
  service/  (1 files)
    index.ts
  types/  (16 files)
    core/  (5 files)
      … 5 files under this directory
    album.d.ts
    artist.d.ts
    common.d.ts
    declarations.d.ts
    infra.d.ts
    lyric.d.ts
    media.d.ts
    music.d.ts
    musicSheet.d.ts
    musicSheetGroup.d.ts
    plugin.d.ts
  utils/  (29 files)
    base64.ts
    checkUpdate.ts
    colorUtil.ts
    delay.ts
    eventBus.ts
    fileUtils.ts
    getOrCreateMMKV.ts
    getUrlExt.ts
    htmlUtil.ts
    jsonUtil.ts
    log.ts
    lrcParser.ts
    mediaExtra.ts
    mediaIndexMap.ts
    mediaUtils.ts
    minDistance.ts
    network.ts
    notImplementedFunction.ts
    openUrl.ts
    perfLogger.ts
    persistStatus.ts
    qualities.ts
    rpx.ts
    scheduleClose.ts
    … 5 more files
.commitlintrc.json
.eslintignore
.eslintrc.js
.gitignore
.prettierrc.js
.watchmanconfig
Gemfile
LICENSE
app.json
babel.config.js
changelog.md
index.js
jest.config.js
metro.config.js
package.json
readme-en.md
readme.md
tsconfig.json
```

## Entry points

- [index.js](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/index.js)
- [src/components/debug/index.tsx](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/components/debug/index.tsx)
- [src/components/dialogs/index.tsx](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/components/dialogs/index.tsx)
- [src/components/errorBoundary/index.tsx](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/components/errorBoundary/index.tsx)
- [src/components/musicBar/index.tsx](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/components/musicBar/index.tsx)
- [src/components/musicList/index.tsx](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/components/musicList/index.tsx)
- [src/components/musicSheetPage/index.tsx](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/components/musicSheetPage/index.tsx)
- [src/components/panels/index.tsx](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/components/panels/index.tsx)
- [src/core.defination/trackPlayer/index.ts](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/core.defination/trackPlayer/index.ts)
- [src/core/i18n/index.ts](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/core/i18n/index.ts)
- [src/core/musicSheet/index.ts](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/core/musicSheet/index.ts)
- [src/core/pluginManager/index.ts](https://github.com/maotoumao/MusicFree/blob/d118b18b3d0c904400f7eea7bf99c0ceec6c1aee/src/core/pluginManager/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 98 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants package | library | Observed | Groups 6 file(s) under constants package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| core.defination package | library | Observed | Groups 1 file(s) under core.defination package (observed from repository paths and static analysis). |
| entry package | library | Observed | Groups 4 file(s) under entry package (observed from repository paths and static analysis). |
| generator package | library | Observed | Groups 1 file(s) under generator package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 11 file(s) under hooks package (observed from repository paths and static analysis). |
| ios package | library | Observed | Groups 1 file(s) under ios package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 7 file(s) under lib package (observed from repository paths and static analysis). |
| native package | library | Observed | Groups 3 file(s) under native package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 99 file(s) under pages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 26 file(s) under service / domain layer (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 11 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 29 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.commitlintrc.json` (config)
- `.github/ISSUE_TEMPLATE/bug_report_zh.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request_zh.yaml` (config)
- `.github/workflows/build-beta.yml` (ci)
- `android/app/build.gradle` (manifest)
- `android/build.gradle` (manifest)
- `app.json` (config)
- `ios/MusicFree/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `ios/MusicFree/Images.xcassets/Contents.json` (config)
- `package.json` (manifest)
- `release/version.json` (config)
- `src/core/i18n/languages/en-us.json` (config)
- `src/core/i18n/languages/zh-cn.json` (config)
- `src/core/i18n/languages/zh-tw.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 374 analysed file(s)
- `android` — 27 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `ios` — 14 analysed file(s)
- `.github` — 4 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.bundle` — 1 analysed file(s)
- `generator` — 1 analysed file(s)
- `release` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d118b18b3d0c904400f7eea7bf99c0ceec6c1aee` is the revision these paths and observations refer to.
