# Project structure: zoontek/react-native-bootsplash

**Analysed commit:** `3dcb8e91edd0afa978f3bc65d92ccb77d00dd2fc`

**Commit reference:** [3dcb8e91edd0afa978f3bc65d92ccb77d00dd2fc](https://github.com/zoontek/react-native-bootsplash/commit/3dcb8e91edd0afa978f3bc65d92ccb77d00dd2fc)

**Tree at this commit:** [zoontek/react-native-bootsplash@3dcb8e91edd0](https://github.com/zoontek/react-native-bootsplash/tree/3dcb8e91edd0afa978f3bc65d92ccb77d00dd2fc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zoontek/react-native-bootsplash |
| Description | 🚀 Show a splash screen during app startup. Hide it when you are ready. |
| Stars | 4308 |
| Forks | 290 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `3dcb8e91edd0afa978f3bc65d92ccb77d00dd2fc` |
| Retrieved at | 2026-11-14T19:14:49.733669+00:00 |
| Files in this snapshot | 100 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (1 files)
    verify.yml
  CODE_OF_CONDUCT.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  funding-octocat.svg
  stale.yml
android/  (20 files)
  src/  (19 files)
    main/  (17 files)
      … 17 files under this directory
    newarch/  (1 files)
      … 1 files under this directory
    oldarch/  (1 files)
      … 1 files under this directory
  build.gradle
example/  (48 files)
  .bundle/  (1 files)
    config
  android/  (15 files)
    app/  (9 files)
      … 9 files under this directory
    gradle/  (1 files)
      … 1 files under this directory
    build.gradle
    gradle.properties
    gradlew
    gradlew.bat
    settings.gradle
  assets/  (1 files)
    bootsplash/  (1 files)
      … 1 files under this directory
  ios/  (15 files)
    RNBootSplashExample/  (9 files)
      … 9 files under this directory
    RNBootSplashExample.xcodeproj/  (2 files)
      … 2 files under this directory
    RNBootSplashExample.xcworkspace/  (1 files)
      … 1 files under this directory
    .xcode.env
    Podfile
    Podfile.lock
  public/  (1 files)
    index.html
  src/  (2 files)
    AnimatedBootSplash.tsx
    App.tsx
  svgs/  (4 files)
    dark-brand.svg
    dark-logo.svg
    light-brand.svg
    light-logo.svg
  Gemfile
  Gemfile.lock
  app.json
  babel.config.js
  index.js
  metro.config.js
  package.json
  tsconfig.json
  webpack.config.js
ios/  (3 files)
  RNBootSplash.xcodeproj/  (1 files)
    project.pbxproj
  RNBootSplash.h
  RNBootSplash.mm
src/  (6 files)
  extras/  (3 files)
    expo.ts
    generate.ts
    utils.ts
  specs/  (2 files)
    NativeRNBootSplash.ts
    NativeRNBootSplash.web.ts
  index.ts
types/  (1 files)
  xcode.d.ts
.editorconfig
.gitignore
.prettierignore
CODEOWNERS
LICENSE
MIGRATION.md
README.md
RNBootSplash.podspec
app.plugin.js
cli.js
oxlint.config.ts
package.json
tsconfig.json
```

## Entry points

- [cli.js](https://github.com/zoontek/react-native-bootsplash/blob/3dcb8e91edd0afa978f3bc65d92ccb77d00dd2fc/cli.js)
- [src/index.ts](https://github.com/zoontek/react-native-bootsplash/blob/3dcb8e91edd0afa978f3bc65d92ccb77d00dd2fc/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| extras package | library | Observed | Groups 3 file(s) under extras package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| ios package | library | Observed | Groups 1 file(s) under ios package (observed from repository paths and static analysis). |
| specs package | library | Observed | Groups 2 file(s) under specs package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/verify.yml` (ci)
- `android/build.gradle` (manifest)
- `example/android/app/build.gradle` (manifest)
- `example/android/build.gradle` (manifest)
- `example/app.json` (config)
- `example/assets/bootsplash/manifest.json` (config)
- `example/ios/RNBootSplashExample/Colors.xcassets/BootSplashBackground-152fed.colorset/Contents.json` (config)
- `example/ios/RNBootSplashExample/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `example/ios/RNBootSplashExample/Images.xcassets/BootSplashLogo-152fed.imageset/Contents.json` (config)
- `example/ios/RNBootSplashExample/Images.xcassets/Contents.json` (config)
- `example/package.json` (manifest)
- `example/tsconfig.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `example` — 48 analysed file(s)
- `android` — 20 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 9 analysed file(s)
- `src` — 6 analysed file(s)
- `ios` — 3 analysed file(s)
- `types` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3dcb8e91edd0afa978f3bc65d92ccb77d00dd2fc` is the revision these paths and observations refer to.
