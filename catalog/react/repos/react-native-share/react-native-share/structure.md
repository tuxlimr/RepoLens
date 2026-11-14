# Project structure: react-native-share/react-native-share

**Analysed commit:** `0df4a3cd0a616fe9b9a3f7b30a3d070f62037e64`

**Commit reference:** [0df4a3cd0a616fe9b9a3f7b30a3d070f62037e64](https://github.com/react-native-share/react-native-share/commit/0df4a3cd0a616fe9b9a3f7b30a3d070f62037e64)

**Tree at this commit:** [react-native-share/react-native-share@0df4a3cd0a61](https://github.com/react-native-share/react-native-share/tree/0df4a3cd0a616fe9b9a3f7b30a3d070f62037e64)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-native-share/react-native-share |
| Description | Social share, sending simple data to other apps. |
| Stars | 3896 |
| Forks | 969 |
| Licence | MIT |
| Language | Java |
| Default branch | main |
| Analysed commit | `0df4a3cd0a616fe9b9a3f7b30a3d070f62037e64` |
| Retrieved at | 2026-11-14T19:15:02.707660+00:00 |
| Files in this snapshot | 200 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    question.md
  workflows/  (5 files)
    build-lint-example-app.yml
    codeql-analysis.yml
    docs.yml
    release.yml
    stale.yml
  PULL_REQUEST_TEMPLATE.md
  config.yml
android/  (36 files)
  src/  (34 files)
    main/  (31 files)
      … 31 files under this directory
    newarch/  (1 files)
      … 1 files under this directory
    oldarch/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
  .npmignore
  build.gradle
example/  (46 files)
  .bundle/  (1 files)
    config
  android/  (17 files)
    app/  (11 files)
      … 11 files under this directory
    gradle/  (1 files)
      … 1 files under this directory
    build.gradle
    gradle.properties
    gradlew
    gradlew.bat
    settings.gradle
  images/  (1 files)
    pdfBase64.js
  ios/  (17 files)
    example/  (7 files)
      … 7 files under this directory
    example.xcodeproj/  (3 files)
      … 3 files under this directory
    example.xcworkspace/  (2 files)
      … 2 files under this directory
    exampleTests/  (2 files)
      … 2 files under this directory
    .xcode.env
    Podfile
    Podfile.lock
  .eslintrc.js
  .gitignore
  .prettierrc.js
  App.js
  Gemfile
  app.json
  index.js
  jest.config.js
  react-native.config.js
  tsconfig.json
include/  (1 files)
  RNShare/  (1 files)
    RNShare.h
ios/  (34 files)
  RNShare.xcodeproj/  (1 files)
    project.pbxproj
  .npmignore
  DiscordShare.h
  DiscordShare.m
  EmailShare.h
  EmailShare.m
  FacebookStories.h
  FacebookStories.m
  GenericShare.h
  GenericShare.m
  GooglePlusShare.h
  GooglePlusShare.m
  InstagramShare.h
  InstagramShare.m
  InstagramStories.h
  InstagramStories.m
  MessengerShare.h
  MessengerShare.m
  RNShare.h
  RNShare.mm
  RNShareActivityItemSource.h
  RNShareActivityItemSource.m
  RNShareUtils.h
  RNShareUtils.m
  SmsShare.h
  … 9 more files
patches/  (1 files)
  react-native+0.72.6.patch
plugin/  (2 files)
  src/  (1 files)
    index.ts
  tsconfig.json
spm-headers/  (1 files)
  RNShareSpec.h
src/  (11 files)
  codegenSpec/  (1 files)
    NativeRNShare.ts
  components/  (4 files)
    Button.tsx
    Overlay.tsx
    ShareSheet.tsx
    Sheet.tsx
  helpers/  (4 files)
    android.ts
    checkPermissions.ts
    options.ts
    platform.ts
  index.tsx
  types.ts
website/  (23 files)
  docs/  (12 files)
    contributing.mdx
    installing.mdx
    language-support.mdx
    migrate-v3-to-v4.mdx
    migrate-v4-to-v5.mdx
    share-open.mdx
    share-package-installed.mdx
    share-remote-file.mdx
    share-single.mdx
    testing.mdx
    troubleshooting-ios.mdx
    ui-components.mdx
  src/  (3 files)
    css/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
  static/  (3 files)
    img/  (3 files)
      … 3 files under this directory
  .gitignore
  .yarnrc.yml
  docusaurus.config.js
  package.json
  sidebars.js
windows/  (15 files)
  ReactNativeShare/  (11 files)
    PropertySheet.props
    ReactNativeModule.h
    ReactNativeShare.def
    ReactNativeShare.vcxproj
    ReactNativeShare.vcxproj.filters
    ReactPackageProvider.cpp
    ReactPackageProvider.h
    ReactPackageProvider.idl
    packages.config
    pch.cpp
    pch.h
  .gitignore
  ExperimentalFeatures.props
  NuGet.Config
  ReactNativeShare.sln
.eslintignore
.eslintrc.js
.gitignore
.npmignore
.nvmrc
.watchmanconfig
.yarnrc.yml
CHANGELOG.md
CODEOWNERS
LICENSE
Package.swift
README.md
RNShare.podspec
app.plugin.js
commitlint.config.js
metro.config.js
package.json
react-native-spm-prefix.h
react-native.config.js
tsconfig.json
```

## Entry points

- [plugin/src/index.ts](https://github.com/react-native-share/react-native-share/blob/0df4a3cd0a616fe9b9a3f7b30a3d070f62037e64/plugin/src/index.ts)
- [src/index.tsx](https://github.com/react-native-share/react-native-share/blob/0df4a3cd0a616fe9b9a3f7b30a3d070f62037e64/src/index.tsx)
- [website/src/pages/index.js](https://github.com/react-native-share/react-native-share/blob/0df4a3cd0a616fe9b9a3f7b30a3d070f62037e64/website/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| android package | library | Observed | Groups 31 file(s) under android package (observed from repository paths and static analysis). |
| codegenSpec package | library | Observed | Groups 1 file(s) under codegenspec package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 4 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 4 file(s) under helpers package (observed from repository paths and static analysis). |
| include package | library | Observed | Groups 1 file(s) under include package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| ios package | library | Observed | Groups 16 file(s) under ios package (observed from repository paths and static analysis). |
| plugin package | library | Observed | Groups 1 file(s) under plugin package (observed from repository paths and static analysis). |
| spm-headers package | library | Observed | Groups 1 file(s) under spm-headers package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 3 file(s) under website package (observed from repository paths and static analysis). |
| windows package | library | Observed | Groups 5 file(s) under windows package (observed from repository paths and static analysis). |

## Important files

- `.github/config.yml` (config)
- `.github/workflows/build-lint-example-app.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.yarnrc.yml` (config)
- `android/build.gradle` (manifest)
- `example/android/app/build.gradle` (manifest)
- `example/android/build.gradle` (manifest)
- `example/app.json` (config)
- `example/ios/example/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `example/ios/example/Images.xcassets/Contents.json` (config)
- `example/tsconfig.json` (config)
- `package.json` (manifest)
- `plugin/tsconfig.json` (config)
- `tsconfig.json` (config)
- `website/.yarnrc.yml` (config)
- `website/package.json` (manifest)

## Top-level layout

- `example` — 46 analysed file(s)
- `android` — 36 analysed file(s)
- `ios` — 34 analysed file(s)
- `website` — 23 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `windows` — 15 analysed file(s)
- `src` — 11 analysed file(s)
- `.github` — 10 analysed file(s)
- `plugin` — 2 analysed file(s)
- `include` — 1 analysed file(s)
- `patches` — 1 analysed file(s)
- `spm-headers` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0df4a3cd0a616fe9b9a3f7b30a3d070f62037e64` is the revision these paths and observations refer to.
