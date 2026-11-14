# Project structure: SimulatedGREG/electron-vue

**Analysed commit:** `8d4ed607d65300381a8f47d97923eb07832b1a9a`

**Commit reference:** [8d4ed607d65300381a8f47d97923eb07832b1a9a](https://github.com/SimulatedGREG/electron-vue/commit/8d4ed607d65300381a8f47d97923eb07832b1a9a)

**Tree at this commit:** [SimulatedGREG/electron-vue@8d4ed607d653](https://github.com/SimulatedGREG/electron-vue/tree/8d4ed607d65300381a8f47d97923eb07832b1a9a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | SimulatedGREG/electron-vue |
| Description | An Electron & Vue.js quick start boilerplate with vue-cli scaffolding, common Vue plugins, electron-packager/electron-builder, unit/e2e testing, vue-devtools, and webpack. |
| Stars | 15341 |
| Forks | 1500 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `8d4ed607d65300381a8f47d97923eb07832b1a9a` |
| Retrieved at | 2026-11-14T19:11:39.072747+00:00 |
| Files in this snapshot | 205 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE.md
docs/  (158 files)
  cn/  (31 files)
    README.md
    SUMMARY.md
    book.json
    building_your_app.md
    contributing.md
    development.md
    end-to-end_testing.md
    entry_indexhtml.md
    faqs.md
    file-tree.md
    getting_started.md
    global_configuration.md
    main-process.md
    meta.md
    migration-guide.md
    miscellaneous.md
    new-releases.md
    npm_scripts.md
    project_structure.md
    renderer-process.md
    savingreading-local-files.md
    testing.md
    unittesting.md
    using-electron-builder.md
    … 7 more files
  en/  (32 files)
    README.md
    SUMMARY.md
    book.json
    building_your_app.md
    contributing.md
    debugging-production.md
    development.md
    end-to-end_testing.md
    entry_indexhtml.md
    faqs.md
    file-tree.md
    getting_started.md
    global_configuration.md
    main-process.md
    meta.md
    migration-guide.md
    miscellaneous.md
    new-releases.md
    npm_scripts.md
    project_structure.md
    renderer-process.md
    savingreading-local-files.md
    testing.md
    unittesting.md
    … 8 more files
  ja/  (31 files)
    README.md
    SUMMARY.md
    book.json
    building_your_app.md
    contributing.md
    development.md
    end-to-end_testing.md
    entry_indexhtml.md
    faqs.md
    file-tree.md
    getting_started.md
    global_configuration.md
    main-process.md
    meta.md
    migration-guide.md
    miscellaneous.md
    new-releases.md
    npm_scripts.md
    project_structure.md
    renderer-process.md
    savingreading-local-files.md
    testing.md
    unittesting.md
    using-electron-builder.md
    … 7 more files
  ko/  (32 files)
    README.md
    SUMMARY.md
    book.json
    building_your_app.md
    contributing.md
    debugging-production.md
    development.md
    end-to-end_testing.md
    entry_indexhtml.md
    faqs.md
    file-tree.md
    getting_started.md
    global_configuration.md
    main-process.md
    meta.md
    migration-guide.md
    miscellaneous.md
    new-releases.md
    npm_scripts.md
    project_structure.md
    renderer-process.md
    savingreading-local-files.md
    testing.md
    unittesting.md
    … 8 more files
  pt_BR/  (31 files)
    README.md
    SUMMARY.md
    book.json
    building_your_app.md
    contributing.md
    development.md
    end-to-end_testing.md
    entry_indexhtml.md
    faqs.md
    file-tree.md
    getting_started.md
    global_configuration.md
    main-process.md
    meta.md
    migration-guide.md
    miscellaneous.md
    new-releases.md
    npm_scripts.md
    project_structure.md
    renderer-process.md
    savingreading-local-files.md
    testing.md
    unittesting.md
    using-electron-builder.md
    … 7 more files
  LANGS.md
template/  (35 files)
  .electron-vue/  (7 files)
    build.config.js
    build.js
    dev-client.js
    dev-runner.js
    webpack.main.config.js
    webpack.renderer.config.js
    webpack.web.config.js
  src/  (12 files)
    main/  (2 files)
      … 2 files under this directory
    renderer/  (9 files)
      … 9 files under this directory
    index.ejs
  static/  (1 files)
    .gitkeep
  test/  (7 files)
    e2e/  (3 files)
      … 3 files under this directory
    unit/  (3 files)
      … 3 files under this directory
    .eslintrc
  .babelrc
  .eslintignore
  .eslintrc.js
  .gitignore
  .travis.yml
  README.md
  appveyor.yml
  package.json
tests/  (5 files)
  builds/  (1 files)
    .gitkeep
  builds.json
  scaffold.js
  scaffold.sh
  wine.sh
.gitignore
LICENSE.md
README.md
book.json
meta.js
package.json
```

## Entry points

- [meta.js](https://github.com/SimulatedGREG/electron-vue/blob/8d4ed607d65300381a8f47d97923eb07832b1a9a/meta.js)
- [template/src/main/index.js](https://github.com/SimulatedGREG/electron-vue/blob/8d4ed607d65300381a8f47d97923eb07832b1a9a/template/src/main/index.js)
- [template/src/renderer/main.js](https://github.com/SimulatedGREG/electron-vue/blob/8d4ed607d65300381a8f47d97923eb07832b1a9a/template/src/renderer/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| template package | library | Observed | Groups 18 file(s) under template package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `book.json` (config)
- `docs/cn/book.json` (config)
- `docs/en/book.json` (config)
- `docs/ja/book.json` (config)
- `docs/ko/book.json` (config)
- `docs/pt_BR/book.json` (config)
- `package.json` (manifest)
- `template/.travis.yml` (ci)
- `template/appveyor.yml` (config)
- `template/package.json` (manifest)

## Top-level layout

- `docs` — 158 analysed file(s)
- `template` — 35 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `tests` — 5 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `8d4ed607d65300381a8f47d97923eb07832b1a9a` is the revision these paths and observations refer to.
