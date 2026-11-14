# Project structure: akxcv/vuera

**Analysed commit:** `6322eba843982917e9585d5ee705576a7d42788d`

**Commit reference:** [6322eba843982917e9585d5ee705576a7d42788d](https://github.com/akxcv/vuera/commit/6322eba843982917e9585d5ee705576a7d42788d)

**Tree at this commit:** [akxcv/vuera@6322eba84398](https://github.com/akxcv/vuera/tree/6322eba843982917e9585d5ee705576a7d42788d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | akxcv/vuera |
| Description | :eyes: Vue in React, React in Vue. Seamless integration of the two. :dancers: |
| Stars | 4278 |
| Forks | 237 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `6322eba843982917e9585d5ee705576a7d42788d` |
| Retrieved at | 2026-11-14T19:14:50.101087+00:00 |
| Files in this snapshot | 56 |

## Directory tree

```text
src/  (8 files)
  resolvers/  (2 files)
    React.js
    Vue.js
  utils/  (1 files)
    isReactComponent.js
  wrappers/  (2 files)
    React.js
    Vue.js
  VuePlugin.js
  config.js
  index.js
tests/  (34 files)
  fixtures/  (22 files)
    babel/  (13 files)
      … 13 files under this directory
    ReactChildlessComponent.js
    ReactComponent.js
    ReactFunctionalComponent.js
    ReactPureFunctionalComponent.js
    StyledComponent.js
    VueComponent.js
    VueInstanceOptionsComponent.js
    VueRegisteredComponent.js
    VueSingleFileComponent.vue
  polyfills/  (1 files)
    raf.js
  resolvers/  (2 files)
    ReactResolver-test.js
    babelReactResolver-test.js
  utils/  (2 files)
    isReactComponent-test.js
    olderVueCompat.js
  wrappers/  (2 files)
    ReactWrapper-test.js
    VueWrapper-test.js
  .eslintrc.json
  VuePlugin-test.js
  __setup__.js
  babel-test.js
  config-test.js
.babelrc
.eslintignore
.eslintrc.json
.gitignore
.hound.yml
.prettierrc.json
.travis.yml
CHANGELOG.md
LICENSE
README.md
babel.js
jest.config.js
package.json
rollup.config.js
```

## Entry points

- [src/index.js](https://github.com/akxcv/vuera/blob/6322eba843982917e9585d5ee705576a7d42788d/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| resolvers package | library | Observed | Groups 2 file(s) under resolvers package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 34 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |
| VuePlugin.js package | library | Observed | Groups 1 file(s) under vueplugin.js package (observed from repository paths and static analysis). |
| wrappers package | library | Observed | Groups 2 file(s) under wrappers package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.hound.yml` (config)
- `.prettierrc.json` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `tests` — 34 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `src` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (1 x lockfile excluded; 3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `6322eba843982917e9585d5ee705576a7d42788d` is the revision these paths and observations refer to.
