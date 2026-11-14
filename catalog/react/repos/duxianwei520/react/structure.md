# Project structure: duxianwei520/react

**Analysed commit:** `a385305a9b281949dac3525edd940cec5089e2f6`

**Commit reference:** [a385305a9b281949dac3525edd940cec5089e2f6](https://github.com/duxianwei520/react/commit/a385305a9b281949dac3525edd940cec5089e2f6)

**Tree at this commit:** [duxianwei520/react@a385305a9b28](https://github.com/duxianwei520/react/tree/a385305a9b281949dac3525edd940cec5089e2f6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | duxianwei520/react |
| Description |  React+vite+redux+ant design+axios+less全家桶后台管理框架 |
| Stars | 5339 |
| Forks | 1824 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `a385305a9b281949dac3525edd940cec5089e2f6` |
| Retrieved at | 2026-11-14T19:14:22.193888+00:00 |
| Files in this snapshot | 107 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
app/  (92 files)
  apis/  (2 files)
    common.js
    manage.js
  components/  (7 files)
    draw/  (4 files)
      … 4 files under this directory
    logo/  (2 files)
      … 2 files under this directory
    tableList/  (1 files)
      … 1 files under this directory
  configs/  (6 files)
    ajax.js
    common.js
    config.js
    regular.config.js
    router.config.jsx
    socket.js
  middleware/  (4 files)
    configureStore.js
    history.js
    index.js
    logger.js
  mocks/  (24 files)
    apis/  (21 files)
      … 21 files under this directory
    http.js
    interfaceFilter.js
    interfaceMap.js
  pages/  (34 files)
    base/  (13 files)
      … 13 files under this directory
    menu/  (3 files)
      … 3 files under this directory
    set/  (17 files)
      … 17 files under this directory
    example.js
  redux/  (5 files)
    actions/  (2 files)
      … 2 files under this directory
    reducers/  (3 files)
      … 3 files under this directory
  resource/  (1 files)
    iconfont/  (1 files)
      … 1 files under this directory
  styles/  (6 files)
    RichEditor.less
    base.less
    login.less
    personalCenter.less
    set.less
    theme.less
  utils/  (1 files)
    withRouter.js
  client.jsx
  index.html
.eslintignore
.eslintrc.json
.gitattributes
.gitignore
.lintstagedrc
.travis.yml
LICENSE
_config.yml
babel.config.js
index.html
package.json
postcss.config.js
readme.md
vite.config.js
```

## Entry points

- [app/middleware/index.js](https://github.com/duxianwei520/react/blob/a385305a9b281949dac3525edd940cec5089e2f6/app/middleware/index.js)
- [app/pages/base/app.js](https://github.com/duxianwei520/react/blob/a385305a9b281949dac3525edd940cec5089e2f6/app/pages/base/app.js)
- [app/pages/base/index.js](https://github.com/duxianwei520/react/blob/a385305a9b281949dac3525edd940cec5089e2f6/app/pages/base/index.js)
- [app/pages/menu/index.js](https://github.com/duxianwei520/react/blob/a385305a9b281949dac3525edd940cec5089e2f6/app/pages/menu/index.js)
- [app/pages/set/index.js](https://github.com/duxianwei520/react/blob/a385305a9b281949dac3525edd940cec5089e2f6/app/pages/set/index.js)
- [app/redux/reducers/index.js](https://github.com/duxianwei520/react/blob/a385305a9b281949dac3525edd940cec5089e2f6/app/redux/reducers/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 75 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.eslintrc.json` (config)
- `.travis.yml` (ci)
- `_config.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `app` — 92 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a385305a9b281949dac3525edd940cec5089e2f6` is the revision these paths and observations refer to.
