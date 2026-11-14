# Project structure: trazyn/weweChat

**Analysed commit:** `27ab1fd48816392a252f9fd3c20b389dd55431ee`

**Commit reference:** [27ab1fd48816392a252f9fd3c20b389dd55431ee](https://github.com/trazyn/weweChat/commit/27ab1fd48816392a252f9fd3c20b389dd55431ee)

**Tree at this commit:** [trazyn/weweChat@27ab1fd48816](https://github.com/trazyn/weweChat/tree/27ab1fd48816392a252f9fd3c20b389dd55431ee)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | trazyn/weweChat |
| Description | 💬 Unofficial WeChat client built with React, MobX and Electron. |
| Stars | 5698 |
| Forks | 706 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `27ab1fd48816392a252f9fd3c20b389dd55431ee` |
| Retrieved at | 2026-11-14T19:14:15.144597+00:00 |
| Files in this snapshot | 112 |

## Directory tree

```text
config/  (5 files)
  index.js
  webpack.config.base.js
  webpack.config.dev.js
  webpack.config.electron.js
  webpack.config.production.js
scripts/  (2 files)
  dev.js
  publish.sh
src/  (90 files)
  assets/  (4 files)
    fonts/  (4 files)
      … 4 files under this directory
  js/  (83 files)
    components/  (21 files)
      … 21 files under this directory
    pages/  (40 files)
      … 40 files under this directory
    stores/  (15 files)
      … 15 files under this directory
    utils/  (6 files)
      … 6 files under this directory
    routes.js
  app.js
  global.css
  index.html
.babelrc
.ctrlpignore
.editorconfig
.eslintignore
.eslintrc.json
.gitattributes
.gitignore
.stylelintignore
.stylelintrc
.travis.yml
CHANGELOG.MD
LICENSE
README.MD
main.js
package.json
```

## Entry points

- [main.js](https://github.com/trazyn/weweChat/blob/27ab1fd48816392a252f9fd3c20b389dd55431ee/main.js)
- [config/index.js](https://github.com/trazyn/weweChat/blob/27ab1fd48816392a252f9fd3c20b389dd55431ee/config/index.js)
- [src/app.js](https://github.com/trazyn/weweChat/blob/27ab1fd48816392a252f9fd3c20b389dd55431ee/src/app.js)
- [src/js/pages/index.js](https://github.com/trazyn/weweChat/blob/27ab1fd48816392a252f9fd3c20b389dd55431ee/src/js/pages/index.js)
- [src/js/stores/index.js](https://github.com/trazyn/weweChat/blob/27ab1fd48816392a252f9fd3c20b389dd55431ee/src/js/stores/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 54 file(s) under js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 90 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `config` — 5 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `27ab1fd48816392a252f9fd3c20b389dd55431ee` is the revision these paths and observations refer to.
