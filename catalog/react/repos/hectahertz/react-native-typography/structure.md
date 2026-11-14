# Project structure: hectahertz/react-native-typography

**Analysed commit:** `c66b2e8b8e4b73983e95016e53f42ec8327823fb`

**Commit reference:** [c66b2e8b8e4b73983e95016e53f42ec8327823fb](https://github.com/hectahertz/react-native-typography/commit/c66b2e8b8e4b73983e95016e53f42ec8327823fb)

**Tree at this commit:** [hectahertz/react-native-typography@c66b2e8b8e4b](https://github.com/hectahertz/react-native-typography/tree/c66b2e8b8e4b73983e95016e53f42ec8327823fb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hectahertz/react-native-typography |
| Description | Pixel–perfect, native–looking typographic styles for React Native ✒️ |
| Stars | 3558 |
| Forks | 112 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c66b2e8b8e4b73983e95016e53f42ec8327823fb` |
| Retrieved at | 2026-11-14T19:15:15.229780+00:00 |
| Files in this snapshot | 60 |

## Directory tree

```text
demo/  (24 files)
  app/  (18 files)
    _layout.tsx
    human.tsx
    humanDense.tsx
    humanTall.tsx
    iOSUIKit.tsx
    iOSUIKitDense.tsx
    iOSUIKitTall.tsx
    index.tsx
    material.tsx
    materialDense.tsx
    materialTall.tsx
    notoCJK.tsx
    notoTall.tsx
    robotoWeights.tsx
    sfWeights.tsx
    systemDenseWeights.tsx
    systemTallWeights.tsx
    systemWeights.tsx
  components/  (1 files)
    TypeDemo.js
  .gitignore
  README.md
  app.json
  package.json
  tsconfig.json
src/  (30 files)
  collections/  (9 files)
    human.js
    humanDense.js
    humanTall.js
    iOSUIKit.js
    iOSUIKitDense.js
    iOSUIKitTall.js
    material.js
    materialDense.js
    materialTall.js
  helpers/  (17 files)
    iOSColors.js
    materialColors.js
    notoCJKWeights.js
    notoTallWeights.js
    robotoWeights.js
    sanFranciscoSpacing.js
    sanFranciscoWeights.js
    systemDenseWeights.android.js
    systemDenseWeights.ios.js
    systemDenseWeights.web.js
    systemTallWeights.android.js
    systemTallWeights.ios.js
    systemTallWeights.web.js
    systemWeights.android.js
    systemWeights.ios.js
    systemWeights.web.js
    webWeights.js
  internal/  (2 files)
    CombinedStyleSheet.js
    suffixProperties.js
  index.d.ts
  index.js
.babelrc
.gitignore
DENSE_TALL.md
LICENSE
README.md
package.json
```

## Entry points

- [demo/app/index.tsx](https://github.com/hectahertz/react-native-typography/blob/c66b2e8b8e4b73983e95016e53f42ec8327823fb/demo/app/index.tsx)
- [src/index.js](https://github.com/hectahertz/react-native-typography/blob/c66b2e8b8e4b73983e95016e53f42ec8327823fb/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| collections package | library | Observed | Groups 9 file(s) under collections package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 19 file(s) under demo package (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 17 file(s) under helpers package (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 2 file(s) under internal package (observed from repository paths and static analysis). |

## Important files

- `demo/app.json` (config)
- `demo/package.json` (manifest)
- `demo/tsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 30 analysed file(s)
- `demo` — 24 analysed file(s)
- `(root files)` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c66b2e8b8e4b73983e95016e53f42ec8327823fb` is the revision these paths and observations refer to.
