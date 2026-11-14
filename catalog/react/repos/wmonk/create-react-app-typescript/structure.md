# Project structure: wmonk/create-react-app-typescript

**Analysed commit:** `ef987c15acad6468a35ddb0a24ba22add819207e`

**Commit reference:** [ef987c15acad6468a35ddb0a24ba22add819207e](https://github.com/wmonk/create-react-app-typescript/commit/ef987c15acad6468a35ddb0a24ba22add819207e)

**Tree at this commit:** [wmonk/create-react-app-typescript@ef987c15acad](https://github.com/wmonk/create-react-app-typescript/tree/ef987c15acad6468a35ddb0a24ba22add819207e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wmonk/create-react-app-typescript |
| Description | DEPRECATED: Create React apps using typescript with no build configuration. |
| Stars | 3676 |
| Forks | 476 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ef987c15acad6468a35ddb0a24ba22add819207e` |
| Retrieved at | 2026-11-14T19:15:10.025698+00:00 |
| Files in this snapshot | 46 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
bin/  (1 files)
  react-scripts-ts.js
config/  (10 files)
  jest/  (4 files)
    babelTransform.js
    cssTransform.js
    fileTransform.js
    typescriptTransform.js
  env.js
  paths.js
  polyfills.js
  webpack.config.dev.js
  webpack.config.prod.js
  webpackDevServer.config.js
scripts/  (6 files)
  utils/  (1 files)
    createJestConfig.js
  build.js
  eject.js
  init.js
  start.js
  test.js
tasks/  (3 files)
  e2e-simple.sh
  publish.sh
  verdaccio.yaml
template/  (16 files)
  public/  (2 files)
    index.html
    manifest.json
  src/  (7 files)
    App.css
    App.test.tsx
    App.tsx
    index.css
    index.tsx
    logo.svg
    registerServiceWorker.ts
  README.md
  gitignore
  images.d.ts
  tsconfig.json
  tsconfig.prod.json
  tsconfig.test.json
  tslint.json
.eslintignore
.eslintrc
.gitignore
.travis.yml
.yarnrc
README.md
eslintrc
package.json
```

## Entry points

- [bin/react-scripts-ts.js](https://github.com/wmonk/create-react-app-typescript/blob/ef987c15acad6468a35ddb0a24ba22add819207e/bin/react-scripts-ts.js)
- [template/src/App.tsx](https://github.com/wmonk/create-react-app-typescript/blob/ef987c15acad6468a35ddb0a24ba22add819207e/template/src/App.tsx)
- [template/src/index.tsx](https://github.com/wmonk/create-react-app-typescript/blob/ef987c15acad6468a35ddb0a24ba22add819207e/template/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| tasks package | library | Observed | Groups 2 file(s) under tasks package (observed from repository paths and static analysis). |
| template package | library | Observed | Groups 5 file(s) under template package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)
- `tasks/verdaccio.yaml` (config)
- `template/public/manifest.json` (config)
- `template/tsconfig.json` (config)
- `template/tsconfig.prod.json` (config)
- `template/tsconfig.test.json` (config)
- `template/tslint.json` (config)

## Top-level layout

- `template` — 16 analysed file(s)
- `config` — 10 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `scripts` — 6 analysed file(s)
- `tasks` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `ef987c15acad6468a35ddb0a24ba22add819207e` is the revision these paths and observations refer to.
