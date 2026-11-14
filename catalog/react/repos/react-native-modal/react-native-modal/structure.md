# Project structure: react-native-modal/react-native-modal

**Analysed commit:** `3e413c4c3e774697caebe202e7be5856b62444bf`

**Commit reference:** [3e413c4c3e774697caebe202e7be5856b62444bf](https://github.com/react-native-modal/react-native-modal/commit/3e413c4c3e774697caebe202e7be5856b62444bf)

**Tree at this commit:** [react-native-modal/react-native-modal@3e413c4c3e77](https://github.com/react-native-modal/react-native-modal/tree/3e413c4c3e774697caebe202e7be5856b62444bf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-native-modal/react-native-modal |
| Description | An enhanced, animated, customizable Modal for React Native. |
| Stars | 5650 |
| Forks | 658 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `3e413c4c3e774697caebe202e7be5856b62444bf` |
| Retrieved at | 2026-11-14T19:14:15.607512+00:00 |
| Files in this snapshot | 61 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (1 files)
    BUG_REPORT.md
  workflows/  (1 files)
    tests.yml
  CODEOWNERS
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
examples/  (39 files)
  bare/  (39 files)
    .bundle/  (1 files)
      … 1 files under this directory
    android/  (15 files)
      … 15 files under this directory
    ios/  (10 files)
      … 10 files under this directory
    .gitignore
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
    package.json
    tsconfig.json
src/  (6 files)
  back-handler.ts
  index.ts
  modal.style.ts
  modal.tsx
  types.ts
  utils.ts
.gitattributes
.gitignore
.npmignore
.prettierignore
.prettierrc
.yarnrc.yml
ISSUE_TEMPLATE.md
LICENSE.md
README.md
package.json
tsconfig.json
```

## Entry points

- [src/index.ts](https://github.com/react-native-modal/react-native-modal/blob/3e413c4c3e774697caebe202e7be5856b62444bf/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| back-handler.ts package | library | Observed | Groups 1 file(s) under back-handler.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| modal.style.ts package | library | Observed | Groups 1 file(s) under modal.style.ts package (observed from repository paths and static analysis). |
| modal.tsx package | library | Observed | Groups 1 file(s) under modal.tsx package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/tests.yml` (ci)
- `.yarnrc.yml` (config)
- `examples/bare/android/app/build.gradle` (manifest)
- `examples/bare/android/build.gradle` (manifest)
- `examples/bare/app.json` (config)
- `examples/bare/ios/bare/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `examples/bare/ios/bare/Images.xcassets/Contents.json` (config)
- `examples/bare/package.json` (manifest)
- `examples/bare/tsconfig.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `examples` — 39 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `src` — 6 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3e413c4c3e774697caebe202e7be5856b62444bf` is the revision these paths and observations refer to.
