# Project structure: styled-components/styled-components

**Analysed commit:** `e2aa1c8f6e40b74ae164e7489f68067019d47772`

**Commit reference:** [e2aa1c8f6e40b74ae164e7489f68067019d47772](https://github.com/styled-components/styled-components/commit/e2aa1c8f6e40b74ae164e7489f68067019d47772)

**Tree at this commit:** [styled-components/styled-components@e2aa1c8f6e40](https://github.com/styled-components/styled-components/tree/e2aa1c8f6e40b74ae164e7489f68067019d47772)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | styled-components/styled-components |
| Description | Fast, expressive styling for React. Server components, client components, streaming SSR, React Native—one API. |
| Stars | 41048 |
| Forks | 2595 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `e2aa1c8f6e40b74ae164e7489f68067019d47772` |
| Retrieved at | 2026-11-14T19:12:59.563541+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.biome/  (2 files)
  no-effects.grit
  no-insertion-effect.grit
.changeset/  (131 files)
  ampersand-in-strings-and-escapes.md
  anchor-name-rename-releases-old-rect.md
  attrs-ast-bridge.md
  attrs-type-perf.md
  attrs-win-over-undefined.md
  brackets-and-multiline-strings-contained.md
  buffered-injection-default.md
  client-references-in-server-styles.md
  comments-and-open-parens-contained.md
  component-scope-escape.md
  component-selector-before-type.md
  config.json
  configure-server-styles-namespace.md
  configure-server-styles.md
  consumer-type-check-cost.md
  createTheme-native-parity.md
  declaration-block-at-rules.md
  declared-style-merges.md
  disjoint-union-props.md
  drop-default-props.md
  edge-runtime-error.md
  empty-custom-property-values.md
  extract-css-and-drop-speedy-toggle.md
  fragment-missing-semicolon-warning.md
  … 107 more files
.github/  (7 files)
  codeql/  (1 files)
    codeql-config.yml
  workflows/  (4 files)
    codeql-analysis.yml
    pullfrog.yml
    release.yml
    test.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
.husky/  (1 files)
  pre-commit
.vscode/  (2 files)
  extensions.json
  settings.json
docs/  (13 files)
  animation-adapters.md
  attrs.md
  bundling.md
  css-polyfills.md
  global-styles.md
  jest.md
  namespace.md
  performance.md
  profiling.md
  react-native.md
  react.md
  rendering-flow.md
  typescript-performance.md
packages/  (630 files)
  benchmarks/  (80 files)
    headless/  (5 files)
      … 5 files under this directory
    src/  (69 files)
      … 69 files under this directory
    LICENSE.md
    README.md
    babel.config.js
    index.html
    package.json
    webpack.config.js
  ios-benchmark/  (55 files)
    .bundle/  (1 files)
      … 1 files under this directory
    ios/  (14 files)
      … 14 files under this directory
    scripts/  (5 files)
      … 5 files under this directory
    src/  (23 files)
      … 23 files under this directory
    .gitignore
    .watchmanconfig
    App.tsx
    Gemfile
    Gemfile.lock
    README.md
    app.json
    babel.config.js
    index.js
    metro.config.js
    package.json
    tsconfig.json
  native-showcase/  (115 files)
    android/  (19 files)
      … 19 files under this directory
    app/  (3 files)
      … 3 files under this directory
    ios/  (17 files)
      … 17 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    src/  (68 files)
      … 68 files under this directory
    AGENTS.md
    README.md
    app.json
    babel.config.js
    metro.config.js
    package.json
    tsconfig.json
  sandbox/  (50 files)
    app/  (43 files)
      … 43 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    next-env.d.ts
    next.config.ts
    package.json
    tsconfig.composite.json
    tsconfig.json
  styled-components/  (330 files)
    docs/  (13 files)
      … 13 files under this directory
    native/  (3 files)
      … 3 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    scripts/  (7 files)
      … 7 files under this directory
    src/  (294 files)
      … 294 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    babel.config.js
    jest.config.base.js
    jest.config.bench-rsc.js
    jest.config.bench.js
    jest.config.build.js
    jest.config.main.js
    jest.config.native.js
    package.json
    rollup.config.mjs
.editorconfig
.gitattributes
.gitignore
.nvmrc
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CORE_TEAM.md
LICENSE
babel-preset.cjs
babel.config.cjs
biome.jsonc
knip.jsonc
package.json
```

## Entry points

- [packages/benchmarks/src/index.js](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/packages/benchmarks/src/index.js)
- [packages/ios-benchmark/App.tsx](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/packages/ios-benchmark/App.tsx)
- [packages/ios-benchmark/index.js](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/packages/ios-benchmark/index.js)
- [packages/native-showcase/app/index.tsx](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/packages/native-showcase/app/index.tsx)
- [packages/sandbox/app/page.tsx](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/packages/sandbox/app/page.tsx)
- [packages/styled-components/src/index.ts](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/packages/styled-components/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 6 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 11 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 408 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 110 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/codeql/codeql-config.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/pullfrog.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `packages/benchmarks/package.json` (manifest)
- `packages/ios-benchmark/app.json` (config)
- `packages/ios-benchmark/ios/iosbench/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `packages/ios-benchmark/ios/iosbench/Images.xcassets/Contents.json` (config)
- `packages/ios-benchmark/package.json` (manifest)
- `packages/ios-benchmark/tsconfig.json` (config)
- `packages/native-showcase/android/app/build.gradle` (manifest)
- `packages/native-showcase/android/build.gradle` (manifest)
- `packages/native-showcase/app.json` (config)
- `packages/native-showcase/ios/NativeShowcase/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `packages/native-showcase/ios/NativeShowcase/Images.xcassets/Contents.json` (config)
- `packages/native-showcase/ios/Podfile.properties.json` (config)
- `packages/native-showcase/package.json` (manifest)
- `packages/native-showcase/tsconfig.json` (config)
- `packages/sandbox/package.json` (manifest)
- `packages/sandbox/tsconfig.composite.json` (config)
- `packages/sandbox/tsconfig.json` (config)
- `packages/styled-components/native/package.json` (manifest)
- `packages/styled-components/native/reanimated/package.json` (manifest)
- `packages/styled-components/native/web-bridge/package.json` (manifest)
- `packages/styled-components/package.json` (manifest)
- `packages/styled-components/plugins/package.json` (manifest)

## Top-level layout

- `packages` — 630 analysed file(s)
- `.changeset` — 131 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `docs` — 13 analysed file(s)
- `.github` — 7 analysed file(s)
- `.biome` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e2aa1c8f6e40b74ae164e7489f68067019d47772` is the revision these paths and observations refer to.
