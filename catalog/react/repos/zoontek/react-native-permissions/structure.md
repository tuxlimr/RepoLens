# Project structure: zoontek/react-native-permissions

**Analysed commit:** `4f9f820e821abe1a3780f82ae30de62462b1f0eb`

**Commit reference:** [4f9f820e821abe1a3780f82ae30de62462b1f0eb](https://github.com/zoontek/react-native-permissions/commit/4f9f820e821abe1a3780f82ae30de62462b1f0eb)

**Tree at this commit:** [zoontek/react-native-permissions@4f9f820e821a](https://github.com/zoontek/react-native-permissions/tree/4f9f820e821abe1a3780f82ae30de62462b1f0eb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | zoontek/react-native-permissions |
| Description | An unified permissions API for React Native on iOS, Android and Windows. |
| Stars | 4373 |
| Forks | 842 |
| Licence | MIT |
| Language | Objective-C++ |
| Default branch | master |
| Analysed commit | `4f9f820e821abe1a3780f82ae30de62462b1f0eb` |
| Retrieved at | 2026-11-14T19:14:47.416333+00:00 |
| Files in this snapshot | 173 |

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
.vscode/  (2 files)
  c_cpp_properties.json
  settings.json
android/  (6 files)
  src/  (5 files)
    main/  (3 files)
      … 3 files under this directory
    newarch/  (1 files)
      … 1 files under this directory
    oldarch/  (1 files)
      … 1 files under this directory
  build.gradle
example/  (57 files)
  .bundle/  (1 files)
    config
  android/  (14 files)
    app/  (8 files)
      … 8 files under this directory
    gradle/  (1 files)
      … 1 files under this directory
    build.gradle
    gradle.properties
    gradlew
    gradlew.bat
    settings.gradle
  ios/  (14 files)
    RNPermissionsExample/  (7 files)
      … 7 files under this directory
    RNPermissionsExample.xcodeproj/  (2 files)
      … 2 files under this directory
    RNPermissionsExample.xcworkspace/  (2 files)
      … 2 files under this directory
    .xcode.env
    Podfile
    Podfile.lock
  src/  (1 files)
    App.tsx
  windows/  (18 files)
    Example/  (16 files)
      … 16 files under this directory
    .gitignore
    Example.sln
  .yarnrc
  Gemfile
  Gemfile.lock
  app.json
  babel.config.js
  index.js
  metro.config.js
  package.json
  tsconfig.json
ios/  (45 files)
  AppTrackingTransparency/  (2 files)
    RNPermissionHandlerAppTrackingTransparency.h
    RNPermissionHandlerAppTrackingTransparency.mm
  Bluetooth/  (2 files)
    RNPermissionHandlerBluetooth.h
    RNPermissionHandlerBluetooth.mm
  Calendars/  (2 files)
    RNPermissionHandlerCalendars.h
    RNPermissionHandlerCalendars.mm
  CalendarsWriteOnly/  (2 files)
    RNPermissionHandlerCalendarsWriteOnly.h
    RNPermissionHandlerCalendarsWriteOnly.mm
  Camera/  (2 files)
    RNPermissionHandlerCamera.h
    RNPermissionHandlerCamera.mm
  Contacts/  (3 files)
    RNPermissionHandlerContacts.h
    RNPermissionHandlerContacts.mm
    RNPermissionsContactPicker.swift
  FaceID/  (2 files)
    RNPermissionHandlerFaceID.h
    RNPermissionHandlerFaceID.mm
  LocationAccuracy/  (2 files)
    RNPermissionHandlerLocationAccuracy.h
    RNPermissionHandlerLocationAccuracy.mm
  LocationAlways/  (2 files)
    RNPermissionHandlerLocationAlways.h
    RNPermissionHandlerLocationAlways.mm
  LocationWhenInUse/  (2 files)
    RNPermissionHandlerLocationWhenInUse.h
    RNPermissionHandlerLocationWhenInUse.mm
  MediaLibrary/  (2 files)
    RNPermissionHandlerMediaLibrary.h
    RNPermissionHandlerMediaLibrary.mm
  Microphone/  (2 files)
    RNPermissionHandlerMicrophone.h
    RNPermissionHandlerMicrophone.mm
  Motion/  (2 files)
    RNPermissionHandlerMotion.h
    RNPermissionHandlerMotion.mm
  Notifications/  (2 files)
    RNPermissionHandlerNotifications.h
    RNPermissionHandlerNotifications.mm
  PhotoLibrary/  (2 files)
    RNPermissionHandlerPhotoLibrary.h
    RNPermissionHandlerPhotoLibrary.mm
  PhotoLibraryAddOnly/  (2 files)
    RNPermissionHandlerPhotoLibraryAddOnly.h
    RNPermissionHandlerPhotoLibraryAddOnly.mm
  RNPermissions.xcodeproj/  (1 files)
    project.pbxproj
  Reminders/  (2 files)
    RNPermissionHandlerReminders.h
    RNPermissionHandlerReminders.mm
  Siri/  (2 files)
    RNPermissionHandlerSiri.h
    RNPermissionHandlerSiri.mm
  SpeechRecognition/  (2 files)
    RNPermissionHandlerSpeechRecognition.h
    RNPermissionHandlerSpeechRecognition.mm
  StoreKit/  (2 files)
    RNPermissionHandlerStoreKit.h
    RNPermissionHandlerStoreKit.mm
  PrivacyInfo.xcprivacy
  RNPermissions.h
  RNPermissions.mm
scripts/  (2 files)
  podspec-check.mts
  setup.rb
src/  (17 files)
  extras/  (2 files)
    expo.ts
    mock.ts
  specs/  (1 files)
    NativeRNPermissions.ts
  contract.ts
  index.ts
  methods.android.ts
  methods.ios.ts
  methods.ts
  methods.windows.ts
  permissions.android.ts
  permissions.ios.ts
  permissions.ts
  permissions.windows.ts
  results.ts
  types.ts
  unsupportedMethods.ts
  utils.ts
windows/  (21 files)
  RNPermissions/  (18 files)
    codegen/  (3 files)
      … 3 files under this directory
    PropertySheet.props
    RNPermissions.cpp
    RNPermissions.def
    RNPermissions.h
    RNPermissions.vcxproj
    RNPermissions.vcxproj.filters
    ReactPackageProvider.cpp
    ReactPackageProvider.h
    ReactPackageProvider.idl
    packages.config
    packages.lock.json
    pch.cpp
    pch.h
    resource.h
    targetver.h
  .gitignore
  ExperimentalFeatures.props
  RNPermissions.sln
.editorconfig
.gitignore
.prettierignore
.prettierrc
CODEOWNERS
LICENSE
NuGet.config
README.md
RNPermissions.podspec
app.plugin.js
fetchWindowsCapabilites.js
oxlint.config.ts
package.json
tsconfig.json
```

## Entry points

- [src/index.ts](https://github.com/zoontek/react-native-permissions/blob/4f9f820e821abe1a3780f82ae30de62462b1f0eb/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| contract.ts package | library | Observed | Groups 1 file(s) under contract.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| extras package | library | Observed | Groups 2 file(s) under extras package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| ios package | library | Observed | Groups 21 file(s) under ios package (observed from repository paths and static analysis). |
| methods.android.ts package | library | Observed | Groups 1 file(s) under methods.android.ts package (observed from repository paths and static analysis). |
| methods.ios.ts package | library | Observed | Groups 1 file(s) under methods.ios.ts package (observed from repository paths and static analysis). |
| methods.ts package | library | Observed | Groups 1 file(s) under methods.ts package (observed from repository paths and static analysis). |
| methods.windows.ts package | library | Observed | Groups 1 file(s) under methods.windows.ts package (observed from repository paths and static analysis). |
| permissions.android.ts package | library | Observed | Groups 1 file(s) under permissions.android.ts package (observed from repository paths and static analysis). |
| permissions.ios.ts package | library | Observed | Groups 1 file(s) under permissions.ios.ts package (observed from repository paths and static analysis). |
| permissions.ts package | library | Observed | Groups 1 file(s) under permissions.ts package (observed from repository paths and static analysis). |
| permissions.windows.ts package | library | Observed | Groups 1 file(s) under permissions.windows.ts package (observed from repository paths and static analysis). |
| results.ts package | library | Observed | Groups 1 file(s) under results.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| specs package | library | Observed | Groups 1 file(s) under specs package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| unsupportedMethods.ts package | library | Observed | Groups 1 file(s) under unsupportedmethods.ts package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |
| windows package | library | Observed | Groups 10 file(s) under windows package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/verify.yml` (ci)
- `.vscode/c_cpp_properties.json` (config)
- `.vscode/settings.json` (config)
- `android/build.gradle` (manifest)
- `example/android/app/build.gradle` (manifest)
- `example/android/build.gradle` (manifest)
- `example/app.json` (config)
- `example/ios/RNPermissionsExample/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `example/ios/RNPermissionsExample/Images.xcassets/Contents.json` (config)
- `example/package.json` (manifest)
- `example/tsconfig.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `windows/RNPermissions/packages.lock.json` (config)

## Top-level layout

- `example` — 57 analysed file(s)
- `ios` — 45 analysed file(s)
- `windows` — 21 analysed file(s)
- `src` — 17 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 9 analysed file(s)
- `android` — 6 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4f9f820e821abe1a3780f82ae30de62462b1f0eb` is the revision these paths and observations refer to.
