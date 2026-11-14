# Architecture report: yezihaohao/react-admin

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | yezihaohao/react-admin |
| Description | :sparkles: react-admin system solution : react 后台管理系统解决方案 |
| Language | TypeScript |
| Stars | 6724 |
| Licence | MIT |
| Analysed commit / branch | cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd / master |
| Framework(s) | React |
| Files analysed | 140 |
| Components | 14 |

## 2. Architecture in one minute

yezihaohao/react-admin - :sparkles: react-admin system solution : react 后台管理系统解决方案. This repository was analysed statically from 140 file(s) (0 Python). Detected technologies (observed from imports/manifests): React, axios, React Router, Jest, TypeScript, webpack. Files are grouped into 14 component(s): API layer, App.test.tsx package, App.tsx package, components package, Configuration and deployment, Core modules, index.tsx package, Page.tsx package. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    subgraph api_group
        api_layer["API layer"]
    end
    subgraph config_group
        config["Configuration and deployment"]
    end
    subgraph core_group
        core["Core modules"]
    end
    subgraph library_group
        app_test_tsx["App.test.tsx package"]
        app_tsx["App.tsx package"]
        components["components package"]
        index_tsx["index.tsx package"]
        page_tsx["Page.tsx package"]
        react_app_env_d_ts["react-app-env.d.ts package"]
        scripts["scripts package"]
        serviceworker_ts["serviceWorker.ts package"]
        style["style package"]
        utils["utils package"]
    end
    subgraph service_group
        service_layer["Service / domain layer"]
    end
```

## 4. Main components

### API layer (`api_layer`)

- **Kind:** api
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 3 file(s) under api layer (observed from repository paths and static analysis).
- **Paths:** `src/routes/RouteWrapper.tsx`, `src/routes/config.ts`, `src/routes/index.tsx`
- **Evidence:** [src/routes/RouteWrapper.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/routes/RouteWrapper.tsx); [src/routes/config.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/routes/config.ts); [src/routes/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/routes/index.tsx)

### App.test.tsx package (`app_test_tsx`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under app.test.tsx package (observed from repository paths and static analysis).
- **Paths:** `src/App.test.tsx`
- **Evidence:** [src/App.test.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/App.test.tsx)

### App.tsx package (`app_tsx`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis).
- **Paths:** `src/App.tsx`
- **Evidence:** [src/App.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/App.tsx)

### components package (`components`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 66 file(s) under components package (observed from repository paths and static analysis).
- **Paths:** `src/components/HeaderCustom.tsx`, `src/components/Page.tsx`, `src/components/SiderCustom.tsx`, `src/components/SiderMenu.tsx`, `src/components/animation/BasicAnimations.tsx`, `src/components/animation/ExampleAnimations.tsx`, `src/components/auth/Basic.tsx`, `src/components/auth/RouterEnter.tsx`, `src/components/charts/Echarts.tsx`, `src/components/charts/EchartsArea.tsx`, `src/components/charts/EchartsEffectScatter.tsx`, `src/components/charts/EchartsForce.tsx`, `src/components/charts/EchartsGraphnpm.tsx`, `src/components/charts/EchartsPie.tsx`, `src/components/charts/EchartsScatter.tsx`, `src/components/charts/Recharts.tsx`, `src/components/charts/RechartsBarChart.tsx`, `src/components/charts/RechartsRadarChart.tsx`, `src/components/charts/RechartsRadialBarChart.tsx`, `src/components/charts/RechartsSimpleLineChart.tsx`, `src/components/cssmodule/index.tsx`, `src/components/dashboard/Dashboard.tsx`, `src/components/dashboard/EchartsProjects.tsx`, `src/components/dashboard/EchartsViews.tsx`, `src/components/env/index.tsx`, `src/components/extension/MultipleMenu.tsx`, `src/components/extension/QueryParams.tsx`, `src/components/extension/Visitor.tsx`, `src/components/index.tsx`, `src/components/pages/Login.tsx`, `src/components/pages/NotFound.tsx`, `src/components/smenu/Sub1.tsx`, `src/components/smenu/Sub2.tsx`, `src/components/tables/AdvancedTables.tsx`, `src/components/tables/AsynchronousTable.tsx`, `src/components/tables/BasicTable.tsx`, `src/components/tables/BasicTables.tsx`, `src/components/tables/ExpandedTable.tsx`, `src/components/tables/FixedTable.tsx`, `src/components/tables/SearchTable.tsx`, `src/components/tables/SelectTable.tsx`, `src/components/tables/SortTable.tsx`, `src/components/ui/Buttons.tsx`, `src/components/ui/Draggable.tsx`, `src/components/ui/Gallery.tsx`, `src/components/ui/Icons.tsx`, `src/components/ui/Modals.tsx`, `src/components/ui/Notifications.tsx`, `src/components/ui/Spins.tsx`, `src/components/ui/Tabs.tsx`, `src/components/ui/Wysiwyg.tsx`, `src/components/ui/banners/AutoPlay.tsx`, `src/components/ui/banners/Basic.tsx`, `src/components/ui/banners/Custom.tsx`, `src/components/ui/banners/index.tsx`, `src/components/ui/emoji/iconfont.ts`, `src/components/ui/emoji/index.tsx`, `src/components/ui/map/Tencent.tsx`, `src/components/ui/map/index.tsx`, `src/components/widget/AuthWidget.tsx`, `src/components/widget/BreadcrumbCustom.tsx`, `src/components/widget/Copyright.tsx`, `src/components/widget/Loading.tsx`, `src/components/widget/PwaInstaller.tsx`, `src/components/widget/ThemePicker.tsx`, `src/components/widget/index.tsx`
- **Evidence:** [src/components/HeaderCustom.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/HeaderCustom.tsx); [src/components/Page.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/Page.tsx); [src/components/SiderCustom.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/SiderCustom.tsx); [src/components/SiderMenu.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/SiderMenu.tsx); [src/components/animation/BasicAnimations.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/animation/BasicAnimations.tsx); [src/components/animation/ExampleAnimations.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/animation/ExampleAnimations.tsx); [src/components/auth/Basic.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/auth/Basic.tsx); [src/components/auth/RouterEnter.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/auth/RouterEnter.tsx)

### Configuration and deployment (`config`)

- **Kind:** config
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis).
- **Paths:** `config/env.js`, `config/jest/cssTransform.js`, `config/jest/fileTransform.js`, `config/modules.js`, `config/paths.js`, `config/pnpTs.js`, `config/webpack.config.js`, `config/webpackDevServer.config.js`, `package.json`, `public/manifest.json`, `src/style/theme/theme-danger.json`, `src/style/theme/theme-grey.json`, `src/style/theme/theme-info.json`, `src/style/theme/theme-warn.json`, `tsconfig.json`
- **Evidence:** [config/env.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/env.js); [config/jest/cssTransform.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/jest/cssTransform.js); [config/jest/fileTransform.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/jest/fileTransform.js); [config/modules.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/modules.js); [config/paths.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/paths.js); [config/pnpTs.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/pnpTs.js); [config/webpack.config.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/webpack.config.js); [config/webpackDevServer.config.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/webpackDevServer.config.js)

### Core modules (`core`)

- **Kind:** core
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under core modules (observed from repository paths and static analysis).
- **Paths:** `theme.js`
- **Evidence:** [theme.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/theme.js)

### index.tsx package (`index_tsx`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis).
- **Paths:** `src/index.tsx`
- **Evidence:** [src/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/index.tsx)

### Page.tsx package (`page_tsx`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under page.tsx package (observed from repository paths and static analysis).
- **Paths:** `src/Page.tsx`
- **Evidence:** [src/Page.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/Page.tsx)

### react-app-env.d.ts package (`react_app_env_d_ts`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under react-app-env.d.ts package (observed from repository paths and static analysis).
- **Paths:** `src/react-app-env.d.ts`
- **Evidence:** [src/react-app-env.d.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/react-app-env.d.ts)

### scripts package (`scripts`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 3 file(s) under scripts package (observed from repository paths and static analysis).
- **Paths:** `scripts/build.js`, `scripts/start.js`, `scripts/test.js`
- **Evidence:** [scripts/build.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/scripts/build.js); [scripts/start.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/scripts/start.js); [scripts/test.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/scripts/test.js)

### Service / domain layer (`service_layer`)

- **Kind:** service
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 3 file(s) under service / domain layer (observed from repository paths and static analysis).
- **Paths:** `src/service/config.ts`, `src/service/index.ts`, `src/service/tools.ts`
- **Evidence:** [src/service/config.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/service/config.ts); [src/service/index.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/service/index.ts); [src/service/tools.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/service/tools.ts)

### serviceWorker.ts package (`serviceworker_ts`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under serviceworker.ts package (observed from repository paths and static analysis).
- **Paths:** `src/serviceWorker.ts`
- **Evidence:** [src/serviceWorker.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/serviceWorker.ts)

### style package (`style`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under style package (observed from repository paths and static analysis).
- **Paths:** `src/style/theme/index.js`
- **Evidence:** [src/style/theme/index.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/style/theme/index.js)

### utils package (`utils`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 2 file(s) under utils package (observed from repository paths and static analysis).
- **Paths:** `src/utils/hooks.ts`, `src/utils/index.ts`
- **Evidence:** [src/utils/hooks.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/utils/hooks.ts); [src/utils/index.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/utils/index.ts)

## 5. Execution flow

**Observed** entry point(s):

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

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. No internal import relationships between components were observed.

## 6. Project structure

### `(root)`

- `.commitlintrc.js` - source, JavaScript (87 bytes)
- `.eslintrc` - other (914 bytes)
- `.gitignore` - other (310 bytes)
- `.prettierignore` - other (17 bytes)
- `.prettierrc` - other (131 bytes)
- `.travis.yml` - ci, YAML (67 bytes)
- `CHANGELOG.md` - docs (5830 bytes)
- `LICENSE` - docs (1067 bytes)
- `README.md` - docs (10569 bytes)
- `package.json` - manifest (6884 bytes)
- `theme.js` - source, JavaScript (607 bytes)
- `tsconfig.json` - config (491 bytes)

### `config`

- `config/env.js` - source, JavaScript (3850 bytes)
- `config/jest/cssTransform.js` - source, JavaScript (314 bytes)
- `config/jest/fileTransform.js` - source, JavaScript (1261 bytes)
- `config/modules.js` - source, JavaScript (3897 bytes)
- `config/paths.js` - source, JavaScript (2732 bytes)
- `config/pnpTs.js` - source, JavaScript (620 bytes)
- `config/webpack.config.js` - source, JavaScript (31156 bytes)
- `config/webpackDevServer.config.js` - source, JavaScript (5639 bytes)

### `public`

- `public/index.html` - other (1989 bytes)
- `public/manifest.json` - config (1085 bytes)
- `public/robots.txt` - docs (57 bytes)

### `scripts`

- `scripts/build.js` - source, JavaScript (7384 bytes)
- `scripts/start.js` - source, JavaScript (5369 bytes)
- `scripts/test.js` - source, JavaScript (1352 bytes)

### `src`

- `src/App.test.tsx` - source, TypeScript (248 bytes)
- `src/App.tsx` - source, TypeScript (4378 bytes)
- `src/Page.tsx` - source, TypeScript (619 bytes)
- `src/components/HeaderCustom.tsx` - source, TypeScript (4731 bytes)
- `src/components/Page.tsx` - source, TypeScript (269 bytes)
- `src/components/SiderCustom.tsx` - source, TypeScript (3304 bytes)
- `src/components/SiderMenu.tsx` - source, TypeScript (3646 bytes)
- `src/components/animation/BasicAnimations.tsx` - source, TypeScript (4357 bytes)
- `src/components/animation/ExampleAnimations.tsx` - source, TypeScript (4001 bytes)
- `src/components/auth/Basic.tsx` - source, TypeScript (3100 bytes)
- `src/components/auth/RouterEnter.tsx` - source, TypeScript (1188 bytes)
- `src/components/charts/Echarts.tsx` - source, TypeScript (1996 bytes)
- `src/components/charts/EchartsArea.tsx` - source, TypeScript (2885 bytes)
- `src/components/charts/EchartsEffectScatter.tsx` - source, TypeScript (15879 bytes)
- `src/components/charts/EchartsForce.tsx` - source, TypeScript (6525 bytes)
- `src/components/charts/EchartsGraphnpm.tsx` - source, TypeScript (2751 bytes)
- `src/components/charts/EchartsPie.tsx` - source, TypeScript (2156 bytes)
- `src/components/charts/EchartsScatter.tsx` - source, TypeScript (4335 bytes)
- `src/components/charts/Recharts.tsx` - source, TypeScript (2045 bytes)
- `src/components/charts/RechartsBarChart.tsx` - source, TypeScript (1107 bytes)
- `src/components/charts/RechartsRadarChart.tsx` - source, TypeScript (1176 bytes)
- `src/components/charts/RechartsRadialBarChart.tsx` - source, TypeScript (1374 bytes)
- `src/components/charts/RechartsSimpleLineChart.tsx` - source, TypeScript (1184 bytes)
- `src/components/cssmodule/index.module.less` - other (993 bytes)
- `src/components/cssmodule/index.tsx` - source, TypeScript (823 bytes)
- `src/components/dashboard/Dashboard.tsx` - source, TypeScript (10468 bytes)
- `src/components/dashboard/EchartsProjects.tsx` - source, TypeScript (2505 bytes)
- `src/components/dashboard/EchartsViews.tsx` - source, TypeScript (2753 bytes)
- `src/components/env/index.tsx` - source, TypeScript (1136 bytes)
- `src/components/extension/MultipleMenu.tsx` - source, TypeScript (791 bytes)
- `src/components/extension/QueryParams.tsx` - source, TypeScript (1355 bytes)
- `src/components/extension/Visitor.tsx` - source, TypeScript (1030 bytes)
- `src/components/index.tsx` - source, TypeScript (1836 bytes)
- `src/components/pages/Login.tsx` - source, TypeScript (3801 bytes)
- `src/components/pages/NotFound.tsx` - source, TypeScript (740 bytes)
- `src/components/smenu/Sub1.tsx` - source, TypeScript (717 bytes)
- `src/components/smenu/Sub2.tsx` - source, TypeScript (717 bytes)
- `src/components/tables/AdvancedTables.tsx` - source, TypeScript (1614 bytes)
- `src/components/tables/AsynchronousTable.tsx` - source, TypeScript (3351 bytes)
- `src/components/tables/BasicTable.tsx` - source, TypeScript (1454 bytes)
- `src/components/tables/BasicTables.tsx` - source, TypeScript (1714 bytes)
- `src/components/tables/ExpandedTable.tsx` - source, TypeScript (1128 bytes)
- `src/components/tables/FixedTable.tsx` - source, TypeScript (1338 bytes)
- `src/components/tables/SearchTable.tsx` - source, TypeScript (4672 bytes)
- `src/components/tables/SelectTable.tsx` - source, TypeScript (2524 bytes)
- `src/components/tables/SortTable.tsx` - source, TypeScript (3513 bytes)
- `src/components/ui/Buttons.tsx` - source, TypeScript (7329 bytes)
- `src/components/ui/Draggable.tsx` - source, TypeScript (5535 bytes)
- `src/components/ui/Gallery.tsx` - source, TypeScript (9783 bytes)
- `src/components/ui/Icons.tsx` - source, TypeScript (6594 bytes)
- `src/components/ui/Modals.tsx` - source, TypeScript (10182 bytes)
- `src/components/ui/Notifications.tsx` - source, TypeScript (7172 bytes)
- `src/components/ui/Spins.tsx` - source, TypeScript (3788 bytes)
- `src/components/ui/Tabs.tsx` - source, TypeScript (10070 bytes)
- `src/components/ui/Wysiwyg.tsx` - source, TypeScript (7727 bytes)
- `src/components/ui/banners/AutoPlay.tsx` - source, TypeScript (2094 bytes)
- `src/components/ui/banners/Basic.tsx` - source, TypeScript (2124 bytes)
- `src/components/ui/banners/Custom.tsx` - source, TypeScript (6719 bytes)
- `src/components/ui/banners/index.tsx` - source, TypeScript (1671 bytes)
- `src/components/ui/emoji/iconfont.ts` - source, TypeScript (156128 bytes)
- `src/components/ui/emoji/index.tsx` - source, TypeScript (889 bytes)
- `src/components/ui/map/Tencent.tsx` - source, TypeScript (852 bytes)
- `src/components/ui/map/index.tsx` - source, TypeScript (548 bytes)
- `src/components/widget/AuthWidget.tsx` - source, TypeScript (441 bytes)
- `src/components/widget/BreadcrumbCustom.tsx` - source, TypeScript (696 bytes)
- `src/components/widget/Copyright.tsx` - source, TypeScript (388 bytes)
- `src/components/widget/Loading.tsx` - source, TypeScript (207 bytes)
- `src/components/widget/PwaInstaller.tsx` - source, TypeScript (2007 bytes)
- `src/components/widget/ThemePicker.tsx` - source, TypeScript (1419 bytes)
- `src/components/widget/index.tsx` - source, TypeScript (220 bytes)
- `src/index.tsx` - source, TypeScript (2167 bytes)
- `src/logo.svg` - other (8205 bytes)
- `src/react-app-env.d.ts` - source, TypeScript (1498 bytes)
- `src/routes/RouteWrapper.tsx` - source, TypeScript (1560 bytes)
- `src/routes/config.ts` - source, TypeScript (5422 bytes)
- `src/routes/index.tsx` - source, TypeScript (2575 bytes)
- `src/service/config.ts` - source, TypeScript (697 bytes)
- `src/service/index.ts` - source, TypeScript (1560 bytes)
- `src/service/tools.ts` - source, TypeScript (1056 bytes)
- `src/serviceWorker.ts` - source, TypeScript (5201 bytes)
- `src/style/antd/header.less` - other (266 bytes)
- `src/style/antd/index.less` - other (149 bytes)
- `src/style/antd/layout.less` - other (249 bytes)
- `src/style/antd/menu.less` - other (1194 bytes)
- `src/style/antd/reset.less` - other (153 bytes)
- `src/style/antd/utils.less` - other (86 bytes)
- `src/style/antd/variables.less` - other (526 bytes)
- `src/style/app.less` - other (394 bytes)
- `src/style/banner.less` - other (2404 bytes)
- `src/style/button.less` - other (42 bytes)
- `src/style/card.less` - other (762 bytes)
- `src/style/global.less` - other (701 bytes)
- `src/style/icons.less` - other (413 bytes)
- `src/style/img.less` - other (122 bytes)
- `src/style/index.less` - other (1362 bytes)
- `src/style/lib/animate.css` - other (79945 bytes)
- `src/style/login.less` - other (940 bytes)
- `src/style/menu.less` - other (1314 bytes)
- `src/style/modal.less` - other (485 bytes)
- `src/style/scroll.less` - other (138 bytes)
- `src/style/table.less` - other (177 bytes)
- `src/style/theme/index.js` - source, JavaScript (287 bytes)
- `src/style/theme/theme-danger.json` - config (49 bytes)
- `src/style/theme/theme-grey.json` - config (49 bytes)
- `src/style/theme/theme-info.json` - config (49 bytes)
- `src/style/theme/theme-warn.json` - config (49 bytes)
- `src/style/utils-border.less` - other (43 bytes)
- `src/style/utils-color.less` - other (546 bytes)
- `src/style/utils-size.less` - other (718 bytes)
- `src/style/utils-spacing.less` - other (588 bytes)
- `src/style/utils-text.less` - other (596 bytes)
- `src/style/variables.less` - other (1039 bytes)
- `src/utils/hooks.ts` - source, TypeScript (623 bytes)
- `src/utils/index.ts` - source, TypeScript (409 bytes)

## 7. Key dependencies and integrations

| Name | Category | Status | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| React | framework | Observed | 0.90 | [package.json:2](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L2); [package.json:21](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L21) |
| axios | library | Observed | 0.85 | [package.json:30](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L30) |
| React Router | library | Observed | 0.85 | [package.json:24](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L24) |
| Jest | tooling | Observed | 0.85 | [package.json:12](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L12) |
| TypeScript | tooling | Observed | 0.85 | [package.json:26](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L26) |
| webpack | tooling | Observed | 0.85 | [package.json:9](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L9) |

## 8. Data and state

No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.

## 9. Configuration and deployment clues

- `.travis.yml` (ci)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `src/style/theme/theme-danger.json` (config)
- `src/style/theme/theme-grey.json` (config)
- `src/style/theme/theme-info.json` (config)
- `src/style/theme/theme-warn.json` (config)
- `tsconfig.json` (config)

## 10. Design observations

- An entry/API layer is separated from other code (Inferred from paths and decorators).
- Service/domain code is distinct from entry and data code, suggesting layered separation (Inferred).

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

## 12. Source references

- [config/env.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/env.js)
- [config/jest/cssTransform.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/jest/cssTransform.js)
- [config/jest/fileTransform.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/jest/fileTransform.js)
- [config/modules.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/modules.js)
- [config/paths.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/paths.js)
- [config/pnpTs.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/pnpTs.js)
- [config/webpack.config.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/webpack.config.js)
- [config/webpackDevServer.config.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/config/webpackDevServer.config.js)
- [package.json:2](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L2)
- [package.json:9](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L9)
- [package.json:12](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L12)
- [package.json:21](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L21)
- [package.json:24](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L24)
- [package.json:26](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L26)
- [package.json:30](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/package.json#L30)
- [scripts/build.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/scripts/build.js)
- [scripts/start.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/scripts/start.js)
- [scripts/test.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/scripts/test.js)
- [src/App.test.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/App.test.tsx)
- [src/App.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/App.tsx)
- [src/Page.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/Page.tsx)
- [src/components/HeaderCustom.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/HeaderCustom.tsx)
- [src/components/Page.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/Page.tsx)
- [src/components/SiderCustom.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/SiderCustom.tsx)
- [src/components/SiderMenu.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/SiderMenu.tsx)
- [src/components/animation/BasicAnimations.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/animation/BasicAnimations.tsx)
- [src/components/animation/ExampleAnimations.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/animation/ExampleAnimations.tsx)
- [src/components/auth/Basic.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/auth/Basic.tsx)
- [src/components/auth/RouterEnter.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/auth/RouterEnter.tsx)
- [src/components/cssmodule/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/cssmodule/index.tsx)
- [src/components/env/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/env/index.tsx)
- [src/components/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/index.tsx)
- [src/components/widget/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/components/widget/index.tsx)
- [src/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/index.tsx)
- [src/react-app-env.d.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/react-app-env.d.ts)
- [src/routes/RouteWrapper.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/routes/RouteWrapper.tsx)
- [src/routes/config.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/routes/config.ts)
- [src/routes/index.tsx](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/routes/index.tsx)
- [src/service/config.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/service/config.ts)
- [src/service/index.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/service/index.ts)
- [src/service/tools.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/service/tools.ts)
- [src/serviceWorker.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/serviceWorker.ts)
- [src/style/theme/index.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/style/theme/index.js)
- [src/utils/hooks.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/utils/hooks.ts)
- [src/utils/index.ts](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/src/utils/index.ts)
- [theme.js](https://github.com/yezihaohao/react-admin/blob/cfaaa12a98a5fbc5fc77a1a5ccb8a85c6a2839fd/theme.js)
