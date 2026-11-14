# Project structure: alibaba/butterfly

**Analysed commit:** `a44f36a23a81aa513579e35a007f309ba8f5e0d7`

**Commit reference:** [a44f36a23a81aa513579e35a007f309ba8f5e0d7](https://github.com/alibaba/butterfly/commit/a44f36a23a81aa513579e35a007f309ba8f5e0d7)

**Tree at this commit:** [alibaba/butterfly@a44f36a23a81](https://github.com/alibaba/butterfly/tree/a44f36a23a81aa513579e35a007f309ba8f5e0d7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alibaba/butterfly |
| Description | 🦋Butterfly，A JavaScript/React/Vue2 Diagramming library which concentrate on flow layout field.    (基于JavaScript/React/Vue2的流程图组件) |
| Stars | 4637 |
| Forks | 609 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `a44f36a23a81aa513579e35a007f309ba8f5e0d7` |
| Retrieved at | 2026-11-14T19:14:40.158540+00:00 |
| Files in this snapshot | 549 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (2 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
docs/  (30 files)
  en-US/  (15 files)
    CODE_OF_CONDUCT.md
    CONTRIBUTING.md
    canvas.md
    edge.md
    endpoint.md
    group.md
    layout.md
    minimap.md
    node.md
    plugins-arrows.md
    plugins-hotkey.md
    plugins-pannel.md
    react.md
    tooltip.md
    vue.md
  zh-CN/  (15 files)
    CODE_OF_CONDUCT.md
    CONTRIBUTING.md
    canvas.md
    edge.md
    endpoint.md
    group.md
    layout.md
    minimap.md
    node.md
    plugins-arrows.md
    plugins-hotkey.md
    plugins-pannel.md
    react.md
    tooltip.md
    vue.md
example/  (286 files)
  cnzz/  (2 files)
    consts.js
    index.js
  components/  (2 files)
    sider/  (2 files)
      … 2 files under this directory
  demo/  (244 files)
    analysis/  (7 files)
      … 7 files under this directory
    circle/  (15 files)
      … 15 files under this directory
    compact-box-tree/  (6 files)
      … 6 files under this directory
    concent-layout/  (9 files)
      … 9 files under this directory
    dagre-group-layout/  (7 files)
      … 7 files under this directory
    dagreLayout/  (9 files)
      … 9 files under this directory
    decision/  (7 files)
      … 7 files under this directory
    diodes/  (7 files)
      … 7 files under this directory
    emergency/  (6 files)
      … 6 files under this directory
    emergency2/  (6 files)
      … 6 files under this directory
    entity-relationship/  (6 files)
      … 6 files under this directory
    fishbone/  (9 files)
      … 9 files under this directory
    flow/  (7 files)
      … 7 files under this directory
    force/  (6 files)
      … 6 files under this directory
    fruchterman/  (6 files)
      … 6 files under this directory
    graphviz/  (5 files)
      … 5 files under this directory
    grid/  (6 files)
      … 6 files under this directory
    indented-tree/  (7 files)
      … 7 files under this directory
    industry/  (10 files)
      … 10 files under this directory
    liteGraph/  (8 files)
      … 8 files under this directory
    login/  (8 files)
      … 8 files under this directory
    mindMap/  (5 files)
      … 5 files under this directory
    mindMap-new/  (4 files)
      … 4 files under this directory
    pluginPanel/  (3 files)
      … 3 files under this directory
    policy/  (8 files)
      … 8 files under this directory
    radial/  (6 files)
      … 6 files under this directory
    react/  (6 files)
      … 6 files under this directory
    relationalBooks/  (8 files)
      … 8 files under this directory
    relationalBooks-new/  (5 files)
      … 5 files under this directory
    relationalNetwork/  (12 files)
      … 12 files under this directory
    rule-tree/  (6 files)
      … 6 files under this directory
    schedule/  (8 files)
      … 8 files under this directory
    schedule2/  (8 files)
      … 8 files under this directory
    system/  (8 files)
      … 8 files under this directory
  dev/  (2 files)
    dev-server.js
    util.js
  i18n/  (2 files)
    en_US.json
    zh_CN.json
  lib/  (1 files)
    dynamic.js
  pages/  (22 files)
    code-box/  (16 files)
      … 16 files under this directory
    gallery/  (1 files)
      … 1 files under this directory
    home/  (2 files)
      … 2 files under this directory
    layout/  (3 files)
      … 3 files under this directory
  static/  (3 files)
    iconfont.css
    iconfont.svg
    newIconfont.css
  README.en_US.md
  README.md
  index.html
  index.jsx
  index.less
  package.json
  theme.less
  webpack.config.js
plugins/  (66 files)
  arrow/  (6 files)
    uml-1.svg
    uml-2.svg
    uml-3.svg
    uml-4.svg
    uml-5.svg
    uml-6.svg
  hotkey/  (4 files)
    src/  (2 files)
      … 2 files under this directory
    package.json
    rollup.config.js
  layout/  (41 files)
    example/  (12 files)
      … 12 files under this directory
    src/  (24 files)
      … 24 files under this directory
    .gitignore
    .npmignore
    README.md
    package.json
    rollup.config.js
  panel/  (15 files)
    example/  (7 files)
      … 7 files under this directory
    src/  (6 files)
      … 6 files under this directory
    package.json
    rollup.config.js
react/  (41 files)
  coms/  (9 files)
    common-render.jsx
    edge.js
    endpoint.jsx
    group.js
    node-render.jsx
    node.js
    react-group.jsx
    react-label.jsx
    react-node.jsx
  example/  (18 files)
    components/  (4 files)
      … 4 files under this directory
    pages/  (7 files)
      … 7 files under this directory
    index.html
    index.jsx
    index.less
    package.json
    router.jsx
    vite.config.js
    webpack.config.js
  util/  (6 files)
    check-render.js
    default-options.js
    diff.js
    process.js
    re-calc.js
    re-layout.js
  .eslintignore
  README.md
  context.js
  index.jsx
  index.less
  package.json
  props.js
  rollup.config.js
src/  (50 files)
  canvas/  (3 files)
    baseCanvas.js
    baseCanvas.less
    treeCanvas.js
  edge/  (2 files)
    baseEdge.js
    baseEdge.less
  endpoint/  (2 files)
    baseEndpoint.js
    baseEndpoint.less
  group/  (2 files)
    baseGroup.js
    baseGroup.less
  interface/  (5 files)
    canvas.js
    edge.js
    endpoint.js
    group.js
    node.js
  node/  (2 files)
    baseNode.js
    treeNode.js
  utils/  (33 files)
    layout/  (14 files)
      … 14 files under this directory
    link/  (10 files)
      … 10 files under this directory
    arrow.js
    coordinate.js
    gridService.js
    guidelineService.js
    minimap.js
    scopeCompare.js
    selectCanvas.js
    toolTip.js
    toolTip.less
  index.less
static/  (5 files)
  arrow/  (3 files)
    arrow1.svg
    arrow2.svg
    arrow3.svg
  butterfly.css
  butterfly.svg
test/  (7 files)
  common/  (1 files)
    init.js
  canvas.test.js
  edge.test.js
  group.test.js
  layout.test.js
  node.test.js
  window.js
vue/  (50 files)
  coms/  (7 files)
    edge.js
    group.js
    node.js
    tree-node.js
    vue-endpoint.vue
    vue-group.vue
    vue-node.vue
  example/  (32 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (28 files)
      … 28 files under this directory
    babel.config.js
    package.json
    vue.config.js
  util/  (6 files)
    add-com.js
    default-data.js
    diff.js
    process.js
    re-calc.js
    re-layout.js
  .npmignore
  butterfly-vue.vue
  index.js
  package.json
  rollup.config.js
.gitignore
.npmignore
LICENSE
README.en-US.md
README.md
azure-pipelines.yml
index.d.ts
index.js
package.json
rollup.config.js
webpack.config.js
```

## Entry points

- [index.js](https://github.com/alibaba/butterfly/blob/a44f36a23a81aa513579e35a007f309ba8f5e0d7/index.js)
- [plugins/hotkey/src/index.js](https://github.com/alibaba/butterfly/blob/a44f36a23a81aa513579e35a007f309ba8f5e0d7/plugins/hotkey/src/index.js)
- [plugins/layout/src/index.js](https://github.com/alibaba/butterfly/blob/a44f36a23a81aa513579e35a007f309ba8f5e0d7/plugins/layout/src/index.js)
- [plugins/panel/src/index.js](https://github.com/alibaba/butterfly/blob/a44f36a23a81aa513579e35a007f309ba8f5e0d7/plugins/panel/src/index.js)
- [react/index.jsx](https://github.com/alibaba/butterfly/blob/a44f36a23a81aa513579e35a007f309ba8f5e0d7/react/index.jsx)
- [src/utils/link/index.js](https://github.com/alibaba/butterfly/blob/a44f36a23a81aa513579e35a007f309ba8f5e0d7/src/utils/link/index.js)
- [vue/index.js](https://github.com/alibaba/butterfly/blob/a44f36a23a81aa513579e35a007f309ba8f5e0d7/vue/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| canvas package | library | Observed | Groups 2 file(s) under canvas package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| edge package | library | Observed | Groups 1 file(s) under edge package (observed from repository paths and static analysis). |
| endpoint package | library | Observed | Groups 1 file(s) under endpoint package (observed from repository paths and static analysis). |
| group package | library | Observed | Groups 1 file(s) under group package (observed from repository paths and static analysis). |
| interface package | library | Observed | Groups 5 file(s) under interface package (observed from repository paths and static analysis). |
| node package | library | Observed | Groups 2 file(s) under node package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 38 file(s) under plugins package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 31 file(s) under react package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 32 file(s) under utils package (observed from repository paths and static analysis). |
| vue package | library | Observed | Groups 45 file(s) under vue package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `azure-pipelines.yml` (ci)
- `example/demo/analysis/package.json` (manifest)
- `example/demo/circle/package.json` (manifest)
- `example/demo/compact-box-tree/package.json` (manifest)
- `example/demo/concent-layout/package.json` (manifest)
- `example/demo/dagre-group-layout/package.json` (manifest)
- `example/demo/dagreLayout/package.json` (manifest)
- `example/demo/decision/package.json` (manifest)
- `example/demo/diodes/package.json` (manifest)
- `example/demo/emergency/package.json` (manifest)
- `example/demo/emergency2/package.json` (manifest)
- `example/demo/entity-relationship/package.json` (manifest)
- `example/demo/fishbone/long_data.json` (config)
- `example/demo/fishbone/long_data2.json` (config)
- `example/demo/flow/package.json` (manifest)
- `example/demo/force/package.json` (manifest)
- `example/demo/fruchterman/package.json` (manifest)
- `example/demo/graphviz/long_data.json` (config)
- `example/demo/graphviz/long_data2.json` (config)
- `example/demo/grid/package.json` (manifest)
- `example/demo/indented-tree/package.json` (manifest)
- `example/demo/industry/package.json` (manifest)
- `example/demo/liteGraph/package.json` (manifest)
- `example/demo/login/package.json` (manifest)
- `example/demo/mindMap/package.json` (manifest)
- `example/demo/pluginPanel/package.json` (manifest)
- `example/demo/policy/package.json` (manifest)
- `example/demo/radial/package.json` (manifest)
- `example/demo/react/package.json` (manifest)
- `example/demo/relationalBooks/package.json` (manifest)
- `example/demo/relationalNetwork/package.json` (manifest)
- `example/demo/rule-tree/package.json` (manifest)
- `example/demo/schedule/package.json` (manifest)
- `example/demo/schedule2/package.json` (manifest)
- `example/demo/system/package.json` (manifest)
- `example/i18n/en_US.json` (config)
- `example/i18n/zh_CN.json` (config)
- `example/package.json` (manifest)
- `package.json` (manifest)
- `plugins/hotkey/package.json` (manifest)
- `plugins/layout/example/package.json` (manifest)
- `plugins/layout/example/src/mock_data.json` (config)
- `plugins/layout/example/src/mock_data1.json` (config)
- `plugins/layout/example/src/mock_data2.json` (config)
- `plugins/layout/package.json` (manifest)
- `plugins/panel/example/package.json` (manifest)
- `plugins/panel/package.json` (manifest)
- `react/example/package.json` (manifest)
- `react/package.json` (manifest)
- `vue/example/package.json` (manifest)
- `vue/package.json` (manifest)

## Top-level layout

- `example` — 286 analysed file(s)
- `plugins` — 66 analysed file(s)
- `src` — 50 analysed file(s)
- `vue` — 50 analysed file(s)
- `react` — 41 analysed file(s)
- `docs` — 30 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `test` — 7 analysed file(s)
- `static` — 5 analysed file(s)
- `.github` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a44f36a23a81aa513579e35a007f309ba8f5e0d7` is the revision these paths and observations refer to.
