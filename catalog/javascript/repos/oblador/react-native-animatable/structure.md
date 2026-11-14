# Project structure: oblador/react-native-animatable

**Analysed commit:** `dfd7413734eb693358defcac536b0b32e9dc0b8c`

**Commit reference:** [dfd7413734eb693358defcac536b0b32e9dc0b8c](https://github.com/oblador/react-native-animatable/commit/dfd7413734eb693358defcac536b0b32e9dc0b8c)

**Tree at this commit:** [oblador/react-native-animatable@dfd7413734eb](https://github.com/oblador/react-native-animatable/tree/dfd7413734eb693358defcac536b0b32e9dc0b8c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | oblador/react-native-animatable |
| Description | Standard set of easy to use animations and declarative transitions for React Native |
| Stars | 9924 |
| Forks | 688 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `dfd7413734eb693358defcac536b0b32e9dc0b8c` |
| Retrieved at | 2026-11-14T19:12:47.188560+00:00 |
| Files in this snapshot | 137 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    deploy.yml
    tests.yml
Examples/  (102 files)
  AnimatableExplorer/  (52 files)
    .bundle/  (1 files)
      … 1 files under this directory
    __tests__/  (1 files)
      … 1 files under this directory
    android/  (17 files)
      … 17 files under this directory
    ios/  (16 files)
      … 16 files under this directory
    .eslintrc.js
    .gitignore
    .prettierrc.js
    .watchmanconfig
    AnimationCell.tsx
    App.tsx
    Gemfile
    Gemfile.lock
    README.md
    app.json
    babel.config.js
    groupedAnimationTypes.ts
    index.js
    jest.config.js
    metro.config.js
    package.json
    tsconfig.json
  MakeItRain/  (50 files)
    .bundle/  (1 files)
      … 1 files under this directory
    __tests__/  (1 files)
      … 1 files under this directory
    android/  (17 files)
      … 17 files under this directory
    ios/  (16 files)
      … 16 files under this directory
    .eslintrc.js
    .gitignore
    .prettierrc.js
    .watchmanconfig
    App.js
    Gemfile
    Gemfile.lock
    README.md
    app.json
    babel.config.js
    index.js
    jest.config.js
    metro.config.js
    package.json
    tsconfig.json
__tests__/  (2 files)
  createAnimation.js
  getDefaultStyleValue.js
definitions/  (12 files)
  attention-seekers.js
  bouncing-entrances.js
  bouncing-exits.js
  fading-entrances.js
  fading-exits.js
  flippers.js
  index.js
  lightspeed.js
  sliding-entrances.js
  sliding-exits.js
  zooming-entrances.js
  zooming-exits.js
typings/  (1 files)
  react-native-animatable.d.ts
.editorconfig
.eslintrc.js
.gitignore
.npmignore
.prettierrc
LICENSE
README.md
babel.config.js
createAnimatableComponent.js
createAnimation.js
easing.js
flattenStyle.js
getDefaultStyleValue.js
getStyleValues.js
index.js
package.json
registry.js
wrapStyleTransforms.js
```

## Entry points

- [index.js](https://github.com/oblador/react-native-animatable/blob/dfd7413734eb693358defcac536b0b32e9dc0b8c/index.js)
- [definitions/index.js](https://github.com/oblador/react-native-animatable/blob/dfd7413734eb693358defcac536b0b32e9dc0b8c/definitions/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 10 file(s) under core modules (observed from repository paths and static analysis). |
| definitions package | library | Observed | Groups 12 file(s) under definitions package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 2 file(s) under __tests__ package (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 1 file(s) under typings package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `Examples/AnimatableExplorer/android/app/build.gradle` (manifest)
- `Examples/AnimatableExplorer/android/build.gradle` (manifest)
- `Examples/AnimatableExplorer/app.json` (config)
- `Examples/AnimatableExplorer/ios/AnimatableExplorer/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `Examples/AnimatableExplorer/ios/AnimatableExplorer/Images.xcassets/Contents.json` (config)
- `Examples/AnimatableExplorer/package.json` (manifest)
- `Examples/AnimatableExplorer/tsconfig.json` (config)
- `Examples/MakeItRain/android/app/build.gradle` (manifest)
- `Examples/MakeItRain/android/build.gradle` (manifest)
- `Examples/MakeItRain/app.json` (config)
- `Examples/MakeItRain/ios/MakeItRain/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `Examples/MakeItRain/ios/MakeItRain/Images.xcassets/Contents.json` (config)
- `Examples/MakeItRain/package.json` (manifest)
- `Examples/MakeItRain/tsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `Examples` — 102 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `definitions` — 12 analysed file(s)
- `.github` — 2 analysed file(s)
- `__tests__` — 2 analysed file(s)
- `typings` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dfd7413734eb693358defcac536b0b32e9dc0b8c` is the revision these paths and observations refer to.
