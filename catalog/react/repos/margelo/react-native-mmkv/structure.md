# Project structure: margelo/react-native-mmkv

**Analysed commit:** `0ec4c96323aee2601f921b1cb8361f6adfc65e13`

**Commit reference:** [0ec4c96323aee2601f921b1cb8361f6adfc65e13](https://github.com/margelo/react-native-mmkv/commit/0ec4c96323aee2601f921b1cb8361f6adfc65e13)

**Tree at this commit:** [margelo/react-native-mmkv@0ec4c96323ae](https://github.com/margelo/react-native-mmkv/tree/0ec4c96323aee2601f921b1cb8361f6adfc65e13)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | margelo/react-native-mmkv |
| Description | ⚡️ The fastest key/value storage for React Native. ~30x faster than AsyncStorage! |
| Stars | 8530 |
| Forks | 346 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `0ec4c96323aee2601f921b1cb8361f6adfc65e13` |
| Retrieved at | 2026-11-14T19:13:41.015622+00:00 |
| Files in this snapshot | 178 |

## Directory tree

```text
.github/  (15 files)
  workflows/  (12 files)
    build-android-release.yml
    build-android.yml
    build-ios-release.yml
    build-ios.yml
    harness-android.yml
    harness-ios.yml
    harness-web.yml
    lint-cpp.yml
    lint-typescript.yml
    run-nitrogen.yml
    test-js.yml
    update-lockfiles.yml
  FUNDING.yml
  dependabot.yml
  funding-octocat.svg
docs/  (12 files)
  HOOKS.md
  LISTENERS.md
  MIGRATE_FROM_ASYNC_STORAGE.md
  V4_UPGRADE_GUIDE.md
  WRAPPER_JOTAI.md
  WRAPPER_MOBX.md
  WRAPPER_MOBXPERSIST.md
  WRAPPER_REACT_QUERY.md
  WRAPPER_RECOIL.md
  WRAPPER_REDUX.md
  WRAPPER_TINYBASE.md
  WRAPPER_ZUSTAND_PERSIST_MIDDLEWARE.md
example/  (46 files)
  __tests__/  (1 files)
    MMKV.harness.ts
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
  ios/  (12 files)
    MmkvExample/  (6 files)
      … 6 files under this directory
    MmkvExample.xcodeproj/  (2 files)
      … 2 files under this directory
    MmkvExample.xcworkspace/  (1 files)
      … 1 files under this directory
    .xcode.env
    Podfile
    Podfile.lock
  scripts/  (2 files)
    web-dev.mjs
    web-proxy.mjs
  src/  (1 files)
    App.tsx
  .eslintrc.js
  .gitignore
  .prettierrc.js
  .watchmanconfig
  Gemfile
  Gemfile.lock
  README.md
  app.json
  babel.config.js
  index.js
  index.web.js
  jest.config.js
  metro.config.js
  package.json
  rn-harness.config.mjs
  tsconfig.json
packages/  (92 files)
  react-native-mmkv/  (92 files)
    __bun_tests__/  (1 files)
      … 1 files under this directory
    __mocks__/  (1 files)
      … 1 files under this directory
    android/  (8 files)
      … 8 files under this directory
    cpp/  (8 files)
      … 8 files under this directory
    ios/  (1 files)
      … 1 files under this directory
    nitrogen/  (30 files)
      … 30 files under this directory
    src/  (34 files)
      … 34 files under this directory
    .gitignore
    .watchmanconfig
    NitroMmkv.podspec
    README.md
    babel.config.js
    nitro.json
    package.json
    react-native.config.js
    tsconfig.json
scripts/  (2 files)
  clang-format.sh
  release.sh
.clang-format
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
README_V3.md
babel.config.js
bunfig.toml
jest.config.js
package.json
```

## Entry points

- [packages/react-native-mmkv/src/index.ts](https://github.com/margelo/react-native-mmkv/blob/0ec4c96323aee2601f921b1cb8361f6adfc65e13/packages/react-native-mmkv/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 51 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build-android-release.yml` (ci)
- `.github/workflows/build-android.yml` (ci)
- `.github/workflows/build-ios-release.yml` (ci)
- `.github/workflows/build-ios.yml` (ci)
- `.github/workflows/harness-android.yml` (ci)
- `.github/workflows/harness-ios.yml` (ci)
- `.github/workflows/harness-web.yml` (ci)
- `.github/workflows/lint-cpp.yml` (ci)
- `.github/workflows/lint-typescript.yml` (ci)
- `.github/workflows/run-nitrogen.yml` (ci)
- `.github/workflows/test-js.yml` (ci)
- `.github/workflows/update-lockfiles.yml` (ci)
- `bunfig.toml` (config)
- `example/android/app/build.gradle` (manifest)
- `example/android/build.gradle` (manifest)
- `example/app.json` (config)
- `example/ios/MmkvExample/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `example/ios/MmkvExample/Images.xcassets/Contents.json` (config)
- `example/package.json` (manifest)
- `example/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/react-native-mmkv/android/build.gradle` (manifest)
- `packages/react-native-mmkv/nitro.json` (config)
- `packages/react-native-mmkv/package.json` (manifest)
- `packages/react-native-mmkv/tsconfig.json` (config)

## Top-level layout

- `packages` — 92 analysed file(s)
- `example` — 46 analysed file(s)
- `.github` — 15 analysed file(s)
- `docs` — 12 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0ec4c96323aee2601f921b1cb8361f6adfc65e13` is the revision these paths and observations refer to.
