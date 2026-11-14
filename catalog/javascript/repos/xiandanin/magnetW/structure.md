# Project structure: xiandanin/magnetW

**Analysed commit:** `012a86b799b3bff59f34319b5d0ac21fac7a7e20`

**Commit reference:** [012a86b799b3bff59f34319b5d0ac21fac7a7e20](https://github.com/xiandanin/magnetW/commit/012a86b799b3bff59f34319b5d0ac21fac7a7e20)

**Tree at this commit:** [xiandanin/magnetW@012a86b799b3](https://github.com/xiandanin/magnetW/tree/012a86b799b3bff59f34319b5d0ac21fac7a7e20)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xiandanin/magnetW |
| Description | [已失效，不再维护] |
| Stars | 11230 |
| Forks | 2049 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `012a86b799b3bff59f34319b5d0ac21fac7a7e20` |
| Retrieved at | 2026-11-14T19:12:23.942952+00:00 |
| Files in this snapshot | 88 |

## Directory tree

```text
.electron-vue/  (6 files)
  build.js
  dev-client.js
  dev-runner.js
  webpack.main.config.js
  webpack.renderer.config.js
  webpack.web.config.js
.github/  (1 files)
  ISSUE_TEMPLATE/  (1 files)
    issue_template.md
scripts/  (2 files)
  build-service.js
  merge-filter-db.js
src/  (65 files)
  main/  (18 files)
    filter/  (1 files)
      … 1 files under this directory
    middleware/  (2 files)
      … 2 files under this directory
    api.js
    axios.js
    cache.js
    defaultConfig.js
    electron-cache.js
    format-parser.js
    index.dev.js
    index.js
    ipc.js
    logger.js
    memory-cache.js
    menu.js
    process-config.js
    repository.js
    service.js
  renderer/  (46 files)
    assets/  (5 files)
      … 5 files under this directory
    components/  (22 files)
      … 22 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    plugins/  (13 files)
      … 13 files under this directory
    router/  (1 files)
      … 1 files under this directory
    App.vue
    main.js
  index.ejs
static/  (2 files)
  .gitkeep
  robots.txt
.babelrc
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.travis.yml
LICENSE
README.md
appveyor.yml
icns.sh
package.json
rule.json
```

## Entry points

- [src/main/index.js](https://github.com/xiandanin/magnetW/blob/012a86b799b3bff59f34319b5d0ac21fac7a7e20/src/main/index.js)
- [src/renderer/main.js](https://github.com/xiandanin/magnetW/blob/012a86b799b3bff59f34319b5d0ac21fac7a7e20/src/renderer/main.js)
- [src/renderer/plugins/app.js](https://github.com/xiandanin/magnetW/blob/012a86b799b3bff59f34319b5d0ac21fac7a7e20/src/renderer/plugins/app.js)
- [src/renderer/plugins/index.js](https://github.com/xiandanin/magnetW/blob/012a86b799b3bff59f34319b5d0ac21fac7a7e20/src/renderer/plugins/index.js)
- [src/renderer/router/index.js](https://github.com/xiandanin/magnetW/blob/012a86b799b3bff59f34319b5d0ac21fac7a7e20/src/renderer/router/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| main package | library | Observed | Groups 18 file(s) under main package (observed from repository paths and static analysis). |
| renderer package | library | Observed | Groups 41 file(s) under renderer package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `appveyor.yml` (config)
- `package.json` (manifest)
- `rule.json` (config)

## Top-level layout

- `src` — 65 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.electron-vue` — 6 analysed file(s)
- `scripts` — 2 analysed file(s)
- `static` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (7 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `012a86b799b3bff59f34319b5d0ac21fac7a7e20` is the revision these paths and observations refer to.
