# Project structure: meliorence/react-native-snap-carousel

**Analysed commit:** `9c39995f4813f0e8ee1be7797512f4e89708167f`

**Commit reference:** [9c39995f4813f0e8ee1be7797512f4e89708167f](https://github.com/meliorence/react-native-snap-carousel/commit/9c39995f4813f0e8ee1be7797512f4e89708167f)

**Tree at this commit:** [meliorence/react-native-snap-carousel@9c39995f4813](https://github.com/meliorence/react-native-snap-carousel/tree/9c39995f4813f0e8ee1be7797512f4e89708167f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | meliorence/react-native-snap-carousel |
| Description | Swiper/carousel component for React Native featuring previews, multiple layouts, parallax images, performant handling of huge numbers of items, and more. Compatible with Android & iOS. |
| Stars | 10486 |
| Forks | 2257 |
| Licence | BSD-3-Clause |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9c39995f4813f0e8ee1be7797512f4e89708167f` |
| Retrieved at | 2026-11-14T19:12:38.592044+00:00 |
| Files in this snapshot | 78 |

## Directory tree

```text
doc/  (7 files)
  CUSTOM_INTERPOLATIONS.md
  KNOWN_ISSUES.md
  PAGINATION.md
  PARALLAX_IMAGE.md
  PROPS_METHODS_AND_GETTERS.md
  TIPS_AND_TRICKS.md
  VERSION_4.md
example/  (53 files)
  __tests__/  (1 files)
    index.js
  android/  (18 files)
    .settings/  (1 files)
      … 1 files under this directory
    app/  (10 files)
      … 10 files under this directory
    gradle/  (1 files)
      … 1 files under this directory
    .project
    build.gradle
    gradle.properties
    gradlew
    gradlew.bat
    settings.gradle
  ios/  (17 files)
    example/  (7 files)
      … 7 files under this directory
    example-tvOS/  (1 files)
      … 1 files under this directory
    example-tvOSTests/  (1 files)
      … 1 files under this directory
    example.xcodeproj/  (3 files)
      … 3 files under this directory
    example.xcworkspace/  (1 files)
      … 1 files under this directory
    exampleTests/  (2 files)
      … 2 files under this directory
    Podfile
    Podfile.lock
  src/  (6 files)
    components/  (1 files)
      … 1 files under this directory
    static/  (1 files)
      … 1 files under this directory
    styles/  (2 files)
      … 2 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    index.js
  .buckconfig
  .flowconfig
  .gitattributes
  .gitignore
  .prettierrc.js
  .watchmanconfig
  app.json
  babel.config.js
  index.js
  metro.config.js
  package.json
src/  (8 files)
  carousel/  (1 files)
    Carousel.js
  pagination/  (3 files)
    Pagination.js
    Pagination.style.js
    PaginationDot.js
  parallaximage/  (2 files)
    ParallaxImage.js
    ParallaxImage.style.js
  utils/  (1 files)
    animations.js
  index.js
.eslintrc
.gitignore
.npmignore
CHANGELOG.md
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
PULL_REQUEST_TEMPLATE.md
README.md
package.json
```

## Entry points

- [src/index.js](https://github.com/meliorence/react-native-snap-carousel/blob/9c39995f4813f0e8ee1be7797512f4e89708167f/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| carousel package | library | Observed | Groups 1 file(s) under carousel package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| pagination package | library | Observed | Groups 3 file(s) under pagination package (observed from repository paths and static analysis). |
| parallaximage package | library | Observed | Groups 2 file(s) under parallaximage package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `example/android/app/build.gradle` (manifest)
- `example/android/build.gradle` (manifest)
- `example/app.json` (config)
- `example/ios/example/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `example/ios/example/Images.xcassets/Contents.json` (config)
- `example/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `example` — 53 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `src` — 8 analysed file(s)
- `doc` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9c39995f4813f0e8ee1be7797512f4e89708167f` is the revision these paths and observations refer to.
