# Project structure: timarney/react-app-rewired

**Analysed commit:** `bfe2390b92bb2f32864bdd09b1b6bbecdc261960`

**Commit reference:** [bfe2390b92bb2f32864bdd09b1b6bbecdc261960](https://github.com/timarney/react-app-rewired/commit/bfe2390b92bb2f32864bdd09b1b6bbecdc261960)

**Tree at this commit:** [timarney/react-app-rewired@bfe2390b92bb](https://github.com/timarney/react-app-rewired/tree/bfe2390b92bb2f32864bdd09b1b6bbecdc261960)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | timarney/react-app-rewired |
| Description | Override create-react-app webpack configs without ejecting |
| Stars | 9836 |
| Forks | 418 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `bfe2390b92bb2f32864bdd09b1b6bbecdc261960` |
| Retrieved at | 2026-11-14T19:13:32.429176+00:00 |
| Files in this snapshot | 37 |

## Directory tree

```text
bin/  (2 files)
  index.js
  jest.js
config/  (3 files)
  paths.js
  webpack.config.js
  webpackDevServer.config.js
overrides/  (4 files)
  devServer.js
  jest.js
  paths.js
  webpack.js
scripts/  (7 files)
  utils/  (4 files)
    babelTransform.js
    dependRequire.js
    paths.js
    rewireJestConfig.js
  build.js
  start.js
  test.js
test/  (13 files)
  react-app/  (13 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (7 files)
      … 7 files under this directory
    .gitignore
    README.md
    config-overrides.js
    package.json
.gitignore
.travis.yml
LICENSE
README.md
README_zh.md
config-overrides.js
index.js
package.json
```

## Entry points

- [bin/index.js](https://github.com/timarney/react-app-rewired/blob/bfe2390b92bb2f32864bdd09b1b6bbecdc261960/bin/index.js)
- [index.js](https://github.com/timarney/react-app-rewired/blob/bfe2390b92bb2f32864bdd09b1b6bbecdc261960/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| overrides package | library | Observed | Groups 4 file(s) under overrides package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 13 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `test` — 13 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `scripts` — 7 analysed file(s)
- `overrides` — 4 analysed file(s)
- `config` — 3 analysed file(s)
- `bin` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bfe2390b92bb2f32864bdd09b1b6bbecdc261960` is the revision these paths and observations refer to.
