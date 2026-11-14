# Project structure: yezihaohao/react-admin

**Analysed commit:** `cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd`

**Commit reference:** [cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd](https://github.com/yezihaohao/react-admin/commit/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd)

**Tree at this commit:** [yezihaohao/react-admin@cfaaa12a98a5](https://github.com/yezihaohao/react-admin/tree/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yezihaohao/react-admin |
| Description | :sparkles: react-admin system solution : react 后台管理系统解决方案 |
| Stars | 6724 |
| Forks | 1832 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd` |
| Retrieved at | 2026-11-14T19:14:02.229395+00:00 |
| Files in this snapshot | 140 |

## Directory tree

```text
config/  (8 files)
  jest/  (2 files)
    cssTransform.js
    fileTransform.js
  env.js
  modules.js
  paths.js
  pnpTs.js
  webpack.config.js
  webpackDevServer.config.js
public/  (3 files)
  index.html
  manifest.json
  robots.txt
scripts/  (3 files)
  build.js
  start.js
  test.js
src/  (114 files)
  components/  (67 files)
    animation/  (2 files)
      … 2 files under this directory
    auth/  (2 files)
      … 2 files under this directory
    charts/  (12 files)
      … 12 files under this directory
    cssmodule/  (2 files)
      … 2 files under this directory
    dashboard/  (3 files)
      … 3 files under this directory
    env/  (1 files)
      … 1 files under this directory
    extension/  (3 files)
      … 3 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    smenu/  (2 files)
      … 2 files under this directory
    tables/  (9 files)
      … 9 files under this directory
    ui/  (17 files)
      … 17 files under this directory
    widget/  (7 files)
      … 7 files under this directory
    HeaderCustom.tsx
    Page.tsx
    SiderCustom.tsx
    SiderMenu.tsx
    index.tsx
  routes/  (3 files)
    RouteWrapper.tsx
    config.ts
    index.tsx
  service/  (3 files)
    config.ts
    index.ts
    tools.ts
  style/  (32 files)
    antd/  (7 files)
      … 7 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    theme/  (5 files)
      … 5 files under this directory
    app.less
    banner.less
    button.less
    card.less
    global.less
    icons.less
    img.less
    index.less
    login.less
    menu.less
    modal.less
    scroll.less
    table.less
    utils-border.less
    utils-color.less
    utils-size.less
    utils-spacing.less
    utils-text.less
    variables.less
  utils/  (2 files)
    hooks.ts
    index.ts
  App.test.tsx
  App.tsx
  Page.tsx
  index.tsx
  logo.svg
  react-app-env.d.ts
  serviceWorker.ts
.commitlintrc.js
.eslintrc
.gitignore
.prettierignore
.prettierrc
.travis.yml
CHANGELOG.md
LICENSE
README.md
package.json
theme.js
tsconfig.json
```

## Entry points

- [src/App.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/App.tsx)
- [src/Page.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/Page.tsx)
- [src/components/Page.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/Page.tsx)
- [src/components/cssmodule/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/cssmodule/index.tsx)
- [src/components/env/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/env/index.tsx)
- [src/components/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/index.tsx)
- [src/components/widget/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/widget/index.tsx)
- [src/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/index.tsx)
- [src/routes/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/routes/index.tsx)
- [src/service/index.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/service/index.ts)
- [src/style/theme/index.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/style/theme/index.js)
- [src/utils/index.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/utils/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| App.test.tsx package | library | Observed | Groups 1 file(s) under app.test.tsx package (observed from repository paths and static analysis). |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 66 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| Page.tsx package | library | Observed | Groups 1 file(s) under page.tsx package (observed from repository paths and static analysis). |
| react-app-env.d.ts package | library | Observed | Groups 1 file(s) under react-app-env.d.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 3 file(s) under service / domain layer (observed from repository paths and static analysis). |
| serviceWorker.ts package | library | Observed | Groups 1 file(s) under serviceworker.ts package (observed from repository paths and static analysis). |
| style package | library | Observed | Groups 1 file(s) under style package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 2 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `src/style/theme/theme-danger.json` (config)
- `src/style/theme/theme-grey.json` (config)
- `src/style/theme/theme-info.json` (config)
- `src/style/theme/theme-warn.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 114 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `config` — 8 analysed file(s)
- `public` — 3 analysed file(s)
- `scripts` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd` is the revision these paths and observations refer to.
