# Project structure: supasate/connected-react-router

**Analysed commit:** `5d4c197043deb89238f9b380a6a1ef4d909f14a7`

**Commit reference:** [5d4c197043deb89238f9b380a6a1ef4d909f14a7](https://github.com/supasate/connected-react-router/commit/5d4c197043deb89238f9b380a6a1ef4d909f14a7)

**Tree at this commit:** [supasate/connected-react-router@5d4c197043de](https://github.com/supasate/connected-react-router/tree/5d4c197043deb89238f9b380a6a1ef4d909f14a7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | supasate/connected-react-router |
| Description | A Redux binding for React Router v4 |
| Stars | 4681 |
| Forks | 580 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5d4c197043deb89238f9b380a6a1ef4d909f14a7` |
| Retrieved at | 2026-11-14T19:14:38.820275+00:00 |
| Files in this snapshot | 152 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    codeql-analysis.yml
examples/  (114 files)
  basic/  (20 files)
    src/  (13 files)
      … 13 files under this directory
    .babelrc
    .eslintrc
    README.md
    index.html
    package.json
    server.js
    webpack.config.js
  immutable/  (20 files)
    src/  (13 files)
      … 13 files under this directory
    .babelrc
    .eslintrc
    README.md
    index.html
    package.json
    server.js
    webpack.config.js
  react-native/  (56 files)
    android/  (16 files)
      … 16 files under this directory
    ios/  (17 files)
      … 17 files under this directory
    src/  (11 files)
      … 11 files under this directory
    .buckconfig
    .eslintrc.js
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
  typescript/  (18 files)
    src/  (13 files)
      … 13 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    webpack.config.js
src/  (13 files)
  structure/  (5 files)
    immutable/  (2 files)
      … 2 files under this directory
    plain/  (2 files)
      … 2 files under this directory
    seamless-immutable/  (1 files)
      … 1 files under this directory
  ConnectedRouter.js
  actions.js
  immutable.js
  index.js
  middleware.js
  reducer.js
  seamless-immutable.js
  selectors.js
test/  (6 files)
  .eslintrc
  ConnectedRouter.test.js
  actions.test.js
  middleware.test.js
  reducer.test.js
  selectors.test.js
.babelrc
.eslintignore
.eslintrc
.gitignore
.jestrc.json
.travis.yml
ACKNOWLEDGE.md
CODE_OF_CONDUCT.md
FAQ.md
LICENSE.md
README.md
immutable.d.ts
immutable.js
index.d.ts
package.json
seamless-immutable.d.ts
seamless-immutable.js
webpack.config.js
```

## Entry points

- [examples/basic/src/index.js](https://github.com/supasate/connected-react-router/blob/5d4c197043deb89238f9b380a6a1ef4d909f14a7/examples/basic/src/index.js)
- [examples/immutable/src/index.js](https://github.com/supasate/connected-react-router/blob/5d4c197043deb89238f9b380a6a1ef4d909f14a7/examples/immutable/src/index.js)
- [examples/typescript/src/index.tsx](https://github.com/supasate/connected-react-router/blob/5d4c197043deb89238f9b380a6a1ef4d909f14a7/examples/typescript/src/index.tsx)
- [src/index.js](https://github.com/supasate/connected-react-router/blob/5d4c197043deb89238f9b380a6a1ef4d909f14a7/src/index.js)
- [src/structure/immutable/index.js](https://github.com/supasate/connected-react-router/blob/5d4c197043deb89238f9b380a6a1ef4d909f14a7/src/structure/immutable/index.js)
- [src/structure/plain/index.js](https://github.com/supasate/connected-react-router/blob/5d4c197043deb89238f9b380a6a1ef4d909f14a7/src/structure/plain/index.js)
- [src/structure/seamless-immutable/index.js](https://github.com/supasate/connected-react-router/blob/5d4c197043deb89238f9b380a6a1ef4d909f14a7/src/structure/seamless-immutable/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| actions.js package | library | Observed | Groups 1 file(s) under actions.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| ConnectedRouter.js package | library | Observed | Groups 1 file(s) under connectedrouter.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| immutable.js package | library | Observed | Groups 1 file(s) under immutable.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| middleware.js package | library | Observed | Groups 1 file(s) under middleware.js package (observed from repository paths and static analysis). |
| reducer.js package | library | Observed | Groups 1 file(s) under reducer.js package (observed from repository paths and static analysis). |
| seamless-immutable.js package | library | Observed | Groups 1 file(s) under seamless-immutable.js package (observed from repository paths and static analysis). |
| selectors.js package | library | Observed | Groups 1 file(s) under selectors.js package (observed from repository paths and static analysis). |
| structure package | library | Observed | Groups 5 file(s) under structure package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/codeql-analysis.yml` (ci)
- `.jestrc.json` (config)
- `.travis.yml` (ci)
- `examples/basic/package.json` (manifest)
- `examples/immutable/package.json` (manifest)
- `examples/react-native/android/app/build.gradle` (manifest)
- `examples/react-native/android/build.gradle` (manifest)
- `examples/react-native/app.json` (config)
- `examples/react-native/ios/ConnectedReactRouter/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `examples/react-native/ios/ConnectedReactRouter/Images.xcassets/Contents.json` (config)
- `examples/react-native/package.json` (manifest)
- `examples/typescript/package.json` (manifest)
- `examples/typescript/tsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `examples` — 114 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `src` — 13 analysed file(s)
- `test` — 6 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5d4c197043deb89238f9b380a6a1ef4d909f14a7` is the revision these paths and observations refer to.
