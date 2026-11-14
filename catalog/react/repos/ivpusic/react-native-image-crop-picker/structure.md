# Project structure: ivpusic/react-native-image-crop-picker

**Analysed commit:** `a18a50d4e7935aeaf45ce44b098bdcac3365be2c`

**Commit reference:** [a18a50d4e7935aeaf45ce44b098bdcac3365be2c](https://github.com/ivpusic/react-native-image-crop-picker/commit/a18a50d4e7935aeaf45ce44b098bdcac3365be2c)

**Tree at this commit:** [ivpusic/react-native-image-crop-picker@a18a50d4e793](https://github.com/ivpusic/react-native-image-crop-picker/tree/a18a50d4e7935aeaf45ce44b098bdcac3365be2c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ivpusic/react-native-image-crop-picker |
| Description | iOS/Android image picker with support for camera, video, configurable compression, multiple images and cropping |
| Stars | 6350 |
| Forks | 1611 |
| Licence | MIT |
| Language | Objective-C |
| Default branch | master |
| Analysed commit | `a18a50d4e7935aeaf45ce44b098bdcac3365be2c` |
| Retrieved at | 2026-11-14T19:14:07.639738+00:00 |
| Files in this snapshot | 138 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
AwesomeExample/  (45 files)
  .bundle/  (1 files)
    config
  __tests__/  (1 files)
    App.test.tsx
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
  ios/  (12 files)
    AwesomeExample/  (6 files)
      … 6 files under this directory
    AwesomeExample.xcodeproj/  (2 files)
      … 2 files under this directory
    AwesomeExample.xcworkspace/  (1 files)
      … 1 files under this directory
    .xcode.env
    Podfile
    Podfile.lock
  .eslintrc.js
  .gitignore
  .prettierrc.js
  .watchmanconfig
  App.tsx
  Gemfile
  Gemfile.lock
  README.md
  app.json
  babel.config.js
  index.js
  jest.config.js
  metro.config.js
  package
  package.json
  tsconfig.json
android/  (18 files)
  gradle/  (1 files)
    wrapper/  (1 files)
      … 1 files under this directory
  src/  (13 files)
    main/  (10 files)
      … 10 files under this directory
    newArch/  (1 files)
      … 1 files under this directory
    oldArch/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
  android.iml
  build.gradle
  gradlew
  gradlew.bat
ios/  (61 files)
  ImageCropPickerSDK/  (4 files)
    QBImagePicker.framework/  (4 files)
      … 4 files under this directory
  QBImagePicker/  (47 files)
    QBImagePicker/  (42 files)
      … 42 files under this directory
    QBImagePicker.xcodeproj/  (2 files)
      … 2 files under this directory
    .gitignore
    LICENSE
    QBImagePickerController.podspec
  imageCropPicker.xcodeproj/  (1 files)
    project.pbxproj
  src/  (8 files)
    Compression.h
    Compression.m
    ImageCropPicker.h
    ImageCropPicker.mm
    UIImage+Extension.h
    UIImage+Extension.m
    UIImage+Resize.h
    UIImage+Resize.m
  PrivacyInfo.xcprivacy
src/  (1 files)
  NativeImageCropPicker.ts
.gitignore
.npmignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
README.md
RNImageCropPicker.podspec
index.d.ts
index.js
package.json
svg.svg
```

## Entry points

- [index.js](https://github.com/ivpusic/react-native-image-crop-picker/blob/a18a50d4e7935aeaf45ce44b098bdcac3365be2c/index.js)
- [AwesomeExample/App.tsx](https://github.com/ivpusic/react-native-image-crop-picker/blob/a18a50d4e7935aeaf45ce44b098bdcac3365be2c/AwesomeExample/App.tsx)
- [AwesomeExample/index.js](https://github.com/ivpusic/react-native-image-crop-picker/blob/a18a50d4e7935aeaf45ce44b098bdcac3365be2c/AwesomeExample/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| android package | library | Observed | Groups 10 file(s) under android package (observed from repository paths and static analysis). |
| AwesomeExample package | library | Observed | Groups 8 file(s) under awesomeexample package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| ios package | library | Observed | Groups 16 file(s) under ios package (observed from repository paths and static analysis). |
| NativeImageCropPicker.ts package | library | Observed | Groups 1 file(s) under nativeimagecroppicker.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `AwesomeExample/android/app/build.gradle` (manifest)
- `AwesomeExample/android/build.gradle` (manifest)
- `AwesomeExample/app.json` (config)
- `AwesomeExample/ios/AwesomeExample/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `AwesomeExample/ios/AwesomeExample/Images.xcassets/Contents.json` (config)
- `AwesomeExample/package.json` (manifest)
- `AwesomeExample/tsconfig.json` (config)
- `android/build.gradle` (manifest)
- `package.json` (manifest)

## Top-level layout

- `ios` — 61 analysed file(s)
- `AwesomeExample` — 45 analysed file(s)
- `android` — 18 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 1 analysed file(s)
- `src` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a18a50d4e7935aeaf45ce44b098bdcac3365be2c` is the revision these paths and observations refer to.
