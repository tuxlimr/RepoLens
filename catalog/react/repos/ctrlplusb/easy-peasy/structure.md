# Project structure: ctrlplusb/easy-peasy

**Analysed commit:** `c1ffaf3937746ac8456e24187b46c4aa3890b699`

**Commit reference:** [c1ffaf3937746ac8456e24187b46c4aa3890b699](https://github.com/ctrlplusb/easy-peasy/commit/c1ffaf3937746ac8456e24187b46c4aa3890b699)

**Tree at this commit:** [ctrlplusb/easy-peasy@c1ffaf393774](https://github.com/ctrlplusb/easy-peasy/tree/c1ffaf3937746ac8456e24187b46c4aa3890b699)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ctrlplusb/easy-peasy |
| Description | Vegetarian friendly state for React |
| Stars | 5040 |
| Forks | 184 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c1ffaf3937746ac8456e24187b46c4aa3890b699` |
| Retrieved at | 2026-11-14T19:14:29.601819+00:00 |
| Files in this snapshot | 381 |

## Directory tree

```text
.github/  (5 files)
  actions/  (2 files)
    prepare/  (1 files)
      … 1 files under this directory
    setup-node/  (1 files)
      … 1 files under this directory
  workflows/  (2 files)
    codeql-analysis.yml
    pr-validate.yml
  FUNDING.yml
.husky/  (1 files)
  pre-commit
examples/  (192 files)
  kanban/  (34 files)
    src/  (20 files)
      … 20 files under this directory
    .eslintignore
    .eslintrc.js
    .gitignore
    .prettierignore
    .prettierrc.js
    README.md
    index.html
    package.json
    postcss.config.js
    tailwind.config.js
    testSetup.ts
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  nextjs-app-router/  (13 files)
    app/  (4 files)
      … 4 files under this directory
    lib/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    next-env.d.ts
    next.config.js
    package.json
    tsconfig.json
  nextjs-ssr/  (12 files)
    components/  (4 files)
      … 4 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    store/  (1 files)
      … 1 files under this directory
    .eslintrc.json
    .gitignore
    README.md
    package.json
  nextjs-todo/  (11 files)
    pages/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    store/  (2 files)
      … 2 files under this directory
    .eslintrc.json
    .gitignore
    README.md
    next.config.js
    package.json
    tsconfig.json
  react-native-todo/  (54 files)
    .bundle/  (1 files)
      … 1 files under this directory
    __tests__/  (1 files)
      … 1 files under this directory
    android/  (17 files)
      … 17 files under this directory
    ios/  (15 files)
      … 15 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .eslintrc.js
    .gitignore
    .node-version
    .prettierrc.js
    .ruby-version
    .watchmanconfig
    Gemfile
    Gemfile.lock
    README.md
    app.json
    babel.config.js
    index.js
    metro.config.js
    package.json
    tsconfig.json
  reduxtagram/  (35 files)
    src/  (22 files)
      … 22 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .editorconfig
    .eslintignore
    .eslintrc.json
    .gitignore
    .prettierrc.json
    README.md
    index.html
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  simple-todo/  (16 files)
    src/  (5 files)
      … 5 files under this directory
    .eslintignore
    .eslintrc.js
    .gitignore
    .prettierignore
    .prettierrc.js
    README.md
    index.html
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  v7-concurrent/  (16 files)
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  README.md
src/  (24 files)
  actions.js
  computed-properties.js
  constants.js
  context.js
  create-context-store.js
  create-reducer.js
  create-store.js
  create-transform.js
  effects.js
  extract-data-from-model.js
  helpers.js
  hooks.js
  index.js
  lib.js
  listeners.js
  migrations.js
  persistence.js
  provider.js
  reference.txt
  server.js
  thunks.js
  transitions.js
  use-local-store.js
  use-memo-one.js
tests/  (68 files)
  lib/  (1 files)
    enable-immer-map-set.js
  testing/  (5 files)
    README.md
    actions.test.js
    listeners.test.js
    react.test.js
    thunks.test.js
  typescript/  (33 files)
    action.ts
    actions.ts
    complex-store-inheritance.ts
    composed-store.ts
    computed.ts
    create-context-store.tsx
    create-store.ts
    debug.ts
    effect-on.ts
    external-type-defs.ts
    generic-model.ts
    giant-model.ts
    hooks.ts
    issue117.ts
    issue224.ts
    issue246.ts
    issue427.ts
    issue66.tsx
    issue802.ts
    issue87.ts
    listener-action.ts
    listener-thunk.ts
    listeners.ts
    persist.tsx
    … 9 more files
  actions.test.js
  computed.test.js
  create-context-store.test.js
  create-typed-hooks.test.js
  debug.test.js
  dependency-injection.test.js
  dev-tools.test.js
  dynamic-store.test.js
  effect-on.test.js
  generic.test.js
  immer.test.js
  lib.test.js
  listener-actions.test.js
  migrations.test.js
  persist.test.js
  react.test.js
  reducer.test.js
  rehydration-transition.test.js
  server-export.test.js
  server-rendering.test.js
  store.test.js
  thunks.test.js
  use-local-store.test.js
  use-store-deferred-state.test.js
  … 5 more files
website/  (73 files)
  docs/  (70 files)
    .vuepress/  (3 files)
      … 3 files under this directory
    docs/  (65 files)
      … 65 files under this directory
    releases/  (1 files)
      … 1 files under this directory
    README.md
  .gitignore
  package.json
  vercel.json
.babelrc.js
.gitignore
.nvmrc
.yarnrc
CHANGELOG.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
eslint.config.js
index.d.ts
map-set-support.d.ts
map-set-support.js
package.json
rollup.config.js
server.d.ts
vitest.config.js
```

## Entry points

- [src/index.js](https://github.com/ctrlplusb/easy-peasy/blob/c1ffaf3937746ac8456e24187b46c4aa3890b699/src/index.js)
- [src/server.js](https://github.com/ctrlplusb/easy-peasy/blob/c1ffaf3937746ac8456e24187b46c4aa3890b699/src/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| actions.js package | library | Observed | Groups 1 file(s) under actions.js package (observed from repository paths and static analysis). |
| computed-properties.js package | library | Observed | Groups 1 file(s) under computed-properties.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| context.js package | library | Observed | Groups 1 file(s) under context.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| create-context-store.js package | library | Observed | Groups 1 file(s) under create-context-store.js package (observed from repository paths and static analysis). |
| create-reducer.js package | library | Observed | Groups 1 file(s) under create-reducer.js package (observed from repository paths and static analysis). |
| create-store.js package | library | Observed | Groups 1 file(s) under create-store.js package (observed from repository paths and static analysis). |
| create-transform.js package | library | Observed | Groups 1 file(s) under create-transform.js package (observed from repository paths and static analysis). |
| effects.js package | library | Observed | Groups 1 file(s) under effects.js package (observed from repository paths and static analysis). |
| extract-data-from-model.js package | library | Observed | Groups 1 file(s) under extract-data-from-model.js package (observed from repository paths and static analysis). |
| helpers.js package | library | Observed | Groups 1 file(s) under helpers.js package (observed from repository paths and static analysis). |
| hooks.js package | library | Observed | Groups 1 file(s) under hooks.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| lib.js package | library | Observed | Groups 1 file(s) under lib.js package (observed from repository paths and static analysis). |
| listeners.js package | library | Observed | Groups 1 file(s) under listeners.js package (observed from repository paths and static analysis). |
| migrations.js package | library | Observed | Groups 1 file(s) under migrations.js package (observed from repository paths and static analysis). |
| persistence.js package | library | Observed | Groups 1 file(s) under persistence.js package (observed from repository paths and static analysis). |
| provider.js package | library | Observed | Groups 1 file(s) under provider.js package (observed from repository paths and static analysis). |
| server.js package | library | Observed | Groups 1 file(s) under server.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 70 file(s) under tests (observed from repository paths and static analysis). |
| thunks.js package | library | Observed | Groups 1 file(s) under thunks.js package (observed from repository paths and static analysis). |
| transitions.js package | library | Observed | Groups 1 file(s) under transitions.js package (observed from repository paths and static analysis). |
| use-local-store.js package | library | Observed | Groups 1 file(s) under use-local-store.js package (observed from repository paths and static analysis). |
| use-memo-one.js package | library | Observed | Groups 1 file(s) under use-memo-one.js package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/actions/prepare/action.yml` (config)
- `.github/actions/setup-node/action.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/pr-validate.yml` (ci)
- `examples/kanban/package.json` (manifest)
- `examples/kanban/tsconfig.json` (config)
- `examples/kanban/tsconfig.node.json` (config)
- `examples/nextjs-app-router/package.json` (manifest)
- `examples/nextjs-app-router/tsconfig.json` (config)
- `examples/nextjs-ssr/.eslintrc.json` (config)
- `examples/nextjs-ssr/package.json` (manifest)
- `examples/nextjs-todo/.eslintrc.json` (config)
- `examples/nextjs-todo/package.json` (manifest)
- `examples/nextjs-todo/tsconfig.json` (config)
- `examples/react-native-todo/android/app/build.gradle` (manifest)
- `examples/react-native-todo/android/build.gradle` (manifest)
- `examples/react-native-todo/app.json` (config)
- `examples/react-native-todo/ios/ReactNativeTodo/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `examples/react-native-todo/ios/ReactNativeTodo/Images.xcassets/Contents.json` (config)
- `examples/react-native-todo/package.json` (manifest)
- `examples/react-native-todo/tsconfig.json` (config)
- `examples/reduxtagram/.editorconfig` (config)
- `examples/reduxtagram/.eslintrc.json` (config)
- `examples/reduxtagram/.prettierrc.json` (config)
- `examples/reduxtagram/package.json` (manifest)
- `examples/reduxtagram/tsconfig.json` (config)
- `examples/reduxtagram/tsconfig.node.json` (config)
- `examples/simple-todo/package.json` (manifest)
- `examples/simple-todo/tsconfig.json` (config)
- `examples/simple-todo/tsconfig.node.json` (config)
- `examples/v7-concurrent/package.json` (manifest)
- `examples/v7-concurrent/tsconfig.json` (config)
- `examples/v7-concurrent/tsconfig.node.json` (config)
- `package.json` (manifest)
- `website/package.json` (manifest)
- `website/vercel.json` (config)

## Top-level layout

- `examples` — 192 analysed file(s)
- `website` — 73 analysed file(s)
- `tests` — 68 analysed file(s)
- `src` — 24 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 5 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 8 file(s) were skipped during inventory (1 x likely secret file excluded; 7 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c1ffaf3937746ac8456e24187b46c4aa3890b699` is the revision these paths and observations refer to.
