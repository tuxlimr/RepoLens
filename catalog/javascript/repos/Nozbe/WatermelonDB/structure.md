# Project structure: Nozbe/WatermelonDB

**Analysed commit:** `5c463222ecd79928861385bac94b486fcc7623d4`

**Commit reference:** [5c463222ecd79928861385bac94b486fcc7623d4](https://github.com/Nozbe/WatermelonDB/commit/5c463222ecd79928861385bac94b486fcc7623d4)

**Tree at this commit:** [Nozbe/WatermelonDB@5c463222ecd7](https://github.com/Nozbe/WatermelonDB/tree/5c463222ecd79928861385bac94b486fcc7623d4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Nozbe/WatermelonDB |
| Description | 🍉 Reactive & asynchronous database for powerful React and React Native apps ⚡️ |
| Stars | 11802 |
| Forks | 664 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5c463222ecd79928861385bac94b486fcc7623d4` |
| Retrieved at | 2026-11-14T19:12:15.106087+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  stale.yml
docs-website/  (49 files)
  blog/  (2 files)
    2021-08-01-mdx-blog-post.mdx
    authors.yml
  docs/  (33 files)
    docs/  (33 files)
      … 33 files under this directory
  src/  (5 files)
    components/  (2 files)
      … 2 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
  static/  (3 files)
    img/  (1 files)
      … 1 files under this directory
    .nojekyll
    CNAME
  .gitignore
  README.md
  babel.config.js
  docusaurus.config.js
  package.json
  sidebars.js
examples/  (8 files)
  typescript/  (8 files)
    __typetests__/  (4 files)
      … 4 files under this directory
    AppSchema.ts
    package.json
    ts-example.ts
    tsconfig.json
flow-typed/  (3 files)
  custom/  (2 files)
    lokijs.js
    react-native.js
  npm/  (1 files)
    rxjs_v6.x.js
native/  (613 files)
  android/  (16 files)
    src/  (13 files)
      … 13 files under this directory
    .gitignore
    build.gradle
    gradle.properties
  android-jsi/  (11 files)
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    build.gradle
  androidTest/  (19 files)
    app/  (10 files)
      … 10 files under this directory
    gradle/  (1 files)
      … 1 files under this directory
    keystores/  (2 files)
      … 2 files under this directory
    .gitignore
    build.gradle
    gradle.properties
    gradlew
    gradlew.bat
    settings.gradle
  ios/  (23 files)
    WatermelonDB/  (23 files)
      … 23 files under this directory
  iosTest/  (480 files)
    Pods/  (460 files)
      … 460 files under this directory
    WatermelonTester/  (8 files)
      … 8 files under this directory
    WatermelonTester.xcodeproj/  (2 files)
      … 2 files under this directory
    WatermelonTester.xcworkspace/  (2 files)
      … 2 files under this directory
    WatermelonTesterTests/  (4 files)
      … 4 files under this directory
    .xcode.env
    Podfile
    Podfile.lock
    PrivacyInfo.xcprivacy
  shared/  (12 files)
    Database-batch.cpp
    Database-jsi.cpp
    Database-query.cpp
    Database-sqlite.cpp
    Database-turboSync.cpp
    Database.cpp
    Database.h
    DatabaseBridge.cpp
    DatabasePlatform.h
    JSIHelpers.h
    Sqlite.cpp
    Sqlite.h
  windows/  (16 files)
    WatermelonDB/  (12 files)
      … 12 files under this directory
    .gitignore
    ExperimentalFeatures.props
    NuGet.Config
    WatermelonDB.sln
  windowsE2E/  (8 files)
    test/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    babel.config.js
    custom-transformer.js
    jest.config.js
    package.json
    tsconfig.json
  windowsTest/  (25 files)
    WatermelonTester/  (21 files)
      … 21 files under this directory
    .gitignore
    ExperimentalFeatures.props
    NuGet.Config
    WatermelonTester.sln
  .clang-format
  .gitignore
  metro-transformer.js
scripts/  (11 files)
  any-android-device
  ccache-clang
  emulator.mjs
  emulatorWithJavaCheck
  make.mjs
  pkg.cjs
  release.mjs
  replace-docs-path.mjs
  retryEmuAndTest
  test-ios
  update-docusaurus
src/  (92 files)
  Collection/  (5 files)
    RecordCache.d.ts
    RecordCache.js
    index.d.ts
    index.js
    test.js
  Database/  (11 files)
    CollectionMap/  (3 files)
      … 3 files under this directory
    LocalStorage/  (3 files)
      … 3 files under this directory
    WorkQueue.d.ts
    WorkQueue.js
    index.d.ts
    index.js
    test.js
  DatabaseProvider/  (2 files)
    index.d.ts
    index.js
  Model/  (5 files)
    helpers.d.ts
    helpers.js
    index.d.ts
    index.js
    test.js
  Query/  (5 files)
    helpers.d.ts
    helpers.js
    index.d.ts
    index.js
    test.js
  QueryDescription/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    helpers.d.ts
    helpers.js
    index.d.ts
    index.js
    operators.d.ts
    operators.js
    type.d.ts
    type.js
  RawRecord/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    index.d.ts
    index.js
  Relation/  (5 files)
    helpers.d.ts
    helpers.js
    index.d.ts
    index.js
    test.js
  Schema/  (11 files)
    migrations/  (8 files)
      … 8 files under this directory
    index.d.ts
    index.js
    test.js
  __playground__/  (1 files)
    index.js
  __tests__/  (10 files)
    emptyMock/  (1 files)
      … 1 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    databaseTests.js
    integrationTests.js
    setUpIntegrationTestEnv.js
    setup.js
    testModels.js
  __typetests__/  (2 files)
    README.md
    query.js
  adapters/  (21 files)
    __tests__/  (2 files)
      … 2 files under this directory
    lokijs/  (15 files)
      … 15 files under this directory
    common.js
    compat.d.ts
    compat.js
    error.js
.eslintignore
.eslintrc.js
.flowconfig
.gitattributes
.gitignore
.imgbotconfig
CHANGELOG-Unreleased.md
CHANGELOG.md
CONTRIBUTING.md
Gemfile
Gemfile.lock
LICENSE
README.md
SECURITY.md
WatermelonDB.podspec
babel.config.js
jest.config.js
metro.config.js
package.json
prettier.config.js
react-native.config.js
```

## Entry points

- [docs-website/src/pages/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/docs-website/src/pages/index.js)
- [src/Collection/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/Collection/index.js)
- [src/Database/CollectionMap/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/Database/CollectionMap/index.js)
- [src/Database/LocalStorage/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/Database/LocalStorage/index.js)
- [src/Database/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/Database/index.js)
- [src/DatabaseProvider/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/DatabaseProvider/index.js)
- [src/Model/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/Model/index.js)
- [src/Query/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/Query/index.js)
- [src/QueryDescription/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/QueryDescription/index.js)
- [src/RawRecord/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/RawRecord/index.js)
- [src/Relation/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/Relation/index.js)
- [src/Schema/index.js](https://github.com/Nozbe/WatermelonDB/blob/5c463222ecd79928861385bac94b486fcc7623d4/src/Schema/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Collection package | library | Observed | Groups 5 file(s) under collection package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 67 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 11 file(s) under data layer (observed from repository paths and static analysis). |
| DatabaseProvider package | library | Observed | Groups 2 file(s) under databaseprovider package (observed from repository paths and static analysis). |
| docs-website package | library | Observed | Groups 5 file(s) under docs-website package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 21 file(s) under external integrations (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 3 file(s) under flow-typed package (observed from repository paths and static analysis). |
| Model package | library | Observed | Groups 5 file(s) under model package (observed from repository paths and static analysis). |
| native package | library | Observed | Groups 158 file(s) under native package (observed from repository paths and static analysis). |
| __playground__ package | library | Observed | Groups 1 file(s) under __playground__ package (observed from repository paths and static analysis). |
| Query package | library | Observed | Groups 5 file(s) under query package (observed from repository paths and static analysis). |
| QueryDescription package | library | Observed | Groups 10 file(s) under querydescription package (observed from repository paths and static analysis). |
| RawRecord package | library | Observed | Groups 4 file(s) under rawrecord package (observed from repository paths and static analysis). |
| Relation package | library | Observed | Groups 5 file(s) under relation package (observed from repository paths and static analysis). |
| Schema package | library | Observed | Groups 11 file(s) under schema package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). |
| __typetests__ package | library | Observed | Groups 1 file(s) under __typetests__ package (observed from repository paths and static analysis). |

## Important files

- `.github/stale.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `docs-website/blog/authors.yml` (config)
- `docs-website/package.json` (manifest)
- `examples/typescript/package.json` (manifest)
- `examples/typescript/tsconfig.json` (config)
- `native/android-jsi/build.gradle` (manifest)
- `native/android/build.gradle` (manifest)
- `native/androidTest/app/build.gradle` (manifest)
- `native/androidTest/build.gradle` (manifest)
- `native/iosTest/Pods/Local Podspecs/DoubleConversion.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/FBLazyVector.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/RCT-Folly.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/RCTDeprecation.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/RCTRequired.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/RCTTypeSafety.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-Codegen.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-Core.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-CoreModules.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-Fabric.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-FabricImage.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-ImageManager.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-Mapbuffer.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-NativeModulesApple.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTActionSheet.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTAnimation.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTAppDelegate.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTBlob.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTFabric.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTImage.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTLinking.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTNetwork.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTSettings.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTText.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RCTVibration.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RuntimeApple.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RuntimeCore.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-RuntimeHermes.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-callinvoker.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-cxxreact.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-debug.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-featureflags.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-graphics.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-hermes.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-jserrorhandler.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-jsi.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-jsiexecutor.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-jsinspector.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-jsitracing.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-logger.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-nativeconfig.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-perflogger.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-rendererdebug.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-rncore.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-runtimeexecutor.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-runtimescheduler.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React-utils.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/React.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/ReactCommon.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/WatermelonDB.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/Yoga.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/boost.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/fmt.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/glog.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/hermes-engine.podspec.json` (config)
- `native/iosTest/Pods/Local Podspecs/simdjson.podspec.json` (config)
- `native/iosTest/WatermelonTester/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `native/iosTest/WatermelonTester/Images.xcassets/Contents.json` (config)
- `native/windowsE2E/package.json` (manifest)
- `native/windowsE2E/tsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `native` — 613 analysed file(s)
- `src` — 92 analysed file(s)
- `docs-website` — 49 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `scripts` — 11 analysed file(s)
- `examples` — 8 analysed file(s)
- `flow-typed` — 3 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5c463222ecd79928861385bac94b486fcc7623d4` is the revision these paths and observations refer to.
