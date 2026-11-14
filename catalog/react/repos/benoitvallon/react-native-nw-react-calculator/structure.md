# Project structure: benoitvallon/react-native-nw-react-calculator

**Analysed commit:** `4f9628fa75d5ad2c2b8d29b611768990087abc15`

**Commit reference:** [4f9628fa75d5ad2c2b8d29b611768990087abc15](https://github.com/benoitvallon/react-native-nw-react-calculator/commit/4f9628fa75d5ad2c2b8d29b611768990087abc15)

**Tree at this commit:** [benoitvallon/react-native-nw-react-calculator@4f9628fa75d5](https://github.com/benoitvallon/react-native-nw-react-calculator/tree/4f9628fa75d5ad2c2b8d29b611768990087abc15)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | benoitvallon/react-native-nw-react-calculator |
| Description | Mobile, desktop and website Apps with the same code |
| Stars | 5206 |
| Forks | 856 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `4f9628fa75d5ad2c2b8d29b611768990087abc15` |
| Retrieved at | 2026-11-14T19:14:25.743148+00:00 |
| Files in this snapshot | 89 |

## Directory tree

```text
android/  (15 files)
  app/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    app.iml
    build.gradle
    proguard-rules.pro
    react.gradle
  gradle/  (1 files)
    wrapper/  (1 files)
      … 1 files under this directory
  ReactNativeNWReactCalculator.iml
  build.gradle
  gradle.properties
  gradlew
  gradlew.bat
  settings.gradle
ios/  (12 files)
  ReactNativeNWReactCalculator/  (8 files)
    Base.lproj/  (1 files)
      … 1 files under this directory
    Images.xcassets/  (3 files)
      … 3 files under this directory
    AppDelegate.h
    AppDelegate.m
    Info.plist
    main.m
  ReactNativeNWReactCalculator.xcodeproj/  (2 files)
    xcshareddata/  (1 files)
      … 1 files under this directory
    project.pbxproj
  ReactNativeNWReactCalculatorTests/  (2 files)
    Info.plist
    ReactNativeNWReactCalculatorTests.m
src/  (45 files)
  __mocks__/  (1 files)
    uniqid.js
  __tests__/  (4 files)
    helpers/  (1 files)
      … 1 files under this directory
    spec/  (3 files)
      … 3 files under this directory
  common/  (34 files)
    actions/  (1 files)
      … 1 files under this directory
    components/  (29 files)
      … 29 files under this directory
    constants/  (2 files)
      … 2 files under this directory
    dispatcher/  (1 files)
      … 1 files under this directory
    stores/  (1 files)
      … 1 files under this directory
  styles/  (2 files)
    main.css
    normalize.css
  .babelrc
  index.android.js
  index.ios.js
  index.js
.editorconfig
.eslintrc
.flowconfig
.gitignore
.travis.yml
.watchmanconfig
Gruntfile.js
LICENSE
README.md
electron.js
index.desktop.html
index.web.html
karma.conf.js
package.json
rn-cli.config.js
webpack.config.js
webpack.dist.config.js
```

## Entry points

- [index.desktop.html](https://github.com/benoitvallon/react-native-nw-react-calculator/blob/4f9628fa75d5ad2c2b8d29b611768990087abc15/index.desktop.html)
- [src/common/components/App.js](https://github.com/benoitvallon/react-native-nw-react-calculator/blob/4f9628fa75d5ad2c2b8d29b611768990087abc15/src/common/components/App.js)
- [src/index.js](https://github.com/benoitvallon/react-native-nw-react-calculator/blob/4f9628fa75d5ad2c2b8d29b611768990087abc15/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| android package | library | Observed | Groups 1 file(s) under android package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 33 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| index.android.js package | library | Observed | Groups 1 file(s) under index.android.js package (observed from repository paths and static analysis). |
| index.ios.js package | library | Observed | Groups 1 file(s) under index.ios.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| ios package | library | Observed | Groups 1 file(s) under ios package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 4 file(s) under __tests__ package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `android/app/build.gradle` (manifest)
- `android/build.gradle` (manifest)
- `ios/ReactNativeNWReactCalculator/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `ios/ReactNativeNWReactCalculator/Images.xcassets/Contents.json` (config)
- `ios/ReactNativeNWReactCalculator/Images.xcassets/LaunchImage.launchimage/Contents.json` (config)
- `package.json` (manifest)
- `src/common/constants/keyCodes.json` (config)

## Top-level layout

- `src` — 45 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `android` — 15 analysed file(s)
- `ios` — 12 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4f9628fa75d5ad2c2b8d29b611768990087abc15` is the revision these paths and observations refer to.
