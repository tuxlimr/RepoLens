# Project structure: youzan/vant-weapp

**Analysed commit:** `5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f`

**Commit reference:** [5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f](https://github.com/youzan/vant-weapp/commit/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f)

**Tree at this commit:** [youzan/vant-weapp@5856ed6b1bc4](https://github.com/youzan/vant-weapp/tree/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | youzan/vant-weapp |
| Description | 轻量、可靠的小程序 UI 组件库 |
| Stars | 18478 |
| Forks | 3451 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | dev |
| Analysed commit | `5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f` |
| Retrieved at | 2026-11-14T19:11:21.962126+00:00 |
| Files in this snapshot | 326 |

## Directory tree

```text
.gitee/  (1 files)
  ISSUE_TEMPLATE.zh-CN.md
.github/  (11 files)
  ISSUE_TEMPLATE/  (3 files)
    config.yml
    template-1-bug-report-vant.zh-CN.yml
    template-3-feature-request-vant.zh-CN.yml
  workflows/  (4 files)
    deploy-site.yml
    pr-label.yaml
    release-tag.yml
    test.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  pr-labeler.yml
.husky/  (3 files)
  .gitignore
  commit-msg
  pre-commit
docs/  (5 files)
  markdown/  (5 files)
    changelog.md
    custom-style.md
    home.md
    quickstart.md
    theme.md
example/  (189 files)
  common/  (1 files)
    page.js
  components/  (12 files)
    demo-block/  (4 files)
      … 4 files under this directory
    demo-home/  (4 files)
      … 4 files under this directory
    demo-home-nav/  (4 files)
      … 4 files under this directory
  functions/  (2 files)
    foo/  (2 files)
      … 2 files under this directory
  pages/  (167 files)
    action-sheet/  (3 files)
      … 3 files under this directory
    area/  (3 files)
      … 3 files under this directory
    button/  (3 files)
      … 3 files under this directory
    calendar/  (3 files)
      … 3 files under this directory
    card/  (3 files)
      … 3 files under this directory
    cascader/  (3 files)
      … 3 files under this directory
    cell/  (3 files)
      … 3 files under this directory
    checkbox/  (3 files)
      … 3 files under this directory
    circle/  (3 files)
      … 3 files under this directory
    col/  (3 files)
      … 3 files under this directory
    collapse/  (3 files)
      … 3 files under this directory
    config-provider/  (3 files)
      … 3 files under this directory
    count-down/  (3 files)
      … 3 files under this directory
    dashboard/  (3 files)
      … 3 files under this directory
    datetime-picker/  (3 files)
      … 3 files under this directory
    dialog/  (3 files)
      … 3 files under this directory
    divider/  (3 files)
      … 3 files under this directory
    dropdown-menu/  (3 files)
      … 3 files under this directory
    empty/  (3 files)
      … 3 files under this directory
    field/  (3 files)
      … 3 files under this directory
    goods-action/  (3 files)
      … 3 files under this directory
    grid/  (3 files)
      … 3 files under this directory
    icon/  (3 files)
      … 3 files under this directory
    image/  (3 files)
      … 3 files under this directory
    index-bar/  (3 files)
      … 3 files under this directory
    loading/  (3 files)
      … 3 files under this directory
    nav-bar/  (3 files)
      … 3 files under this directory
    notice-bar/  (3 files)
      … 3 files under this directory
    notify/  (3 files)
      … 3 files under this directory
    overlay/  (3 files)
      … 3 files under this directory
    panel/  (3 files)
      … 3 files under this directory
    picker/  (3 files)
      … 3 files under this directory
    popup/  (4 files)
      … 4 files under this directory
    progress/  (3 files)
      … 3 files under this directory
    radio/  (3 files)
      … 3 files under this directory
    rate/  (4 files)
      … 4 files under this directory
    search/  (3 files)
      … 3 files under this directory
    share-sheet/  (3 files)
      … 3 files under this directory
    sidebar/  (4 files)
      … 4 files under this directory
    skeleton/  (3 files)
      … 3 files under this directory
    slider/  (3 files)
      … 3 files under this directory
    stepper/  (3 files)
      … 3 files under this directory
    steps/  (3 files)
      … 3 files under this directory
    sticky/  (4 files)
      … 4 files under this directory
    submit-bar/  (3 files)
      … 3 files under this directory
    swipe-cell/  (3 files)
      … 3 files under this directory
    switch/  (3 files)
      … 3 files under this directory
    tab/  (3 files)
      … 3 files under this directory
    tabbar/  (3 files)
      … 3 files under this directory
    tag/  (3 files)
      … 3 files under this directory
    toast/  (3 files)
      … 3 files under this directory
    transition/  (3 files)
      … 3 files under this directory
    tree-select/  (3 files)
      … 3 files under this directory
    uploader/  (4 files)
      … 4 files under this directory
  app.js
  app.json
  app.wxss
  config.js
  database_area.json
  project.config.json
  sitemap.json
lib/  (106 files)
  action-sheet/  (5 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxss
  area/  (6 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxs
    index.wxss
  button/  (6 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxs
    index.wxss
  calendar/  (21 files)
    components/  (11 files)
      … 11 files under this directory
    calendar.wxml
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxs
    index.wxss
    utils.d.ts
    utils.js
    utils.wxs
  card/  (5 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxss
  cascader/  (6 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxs
    index.wxss
  cell/  (6 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxs
    index.wxss
  cell-group/  (5 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxss
  checkbox/  (6 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxs
    index.wxss
  checkbox-group/  (5 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxss
  circle/  (7 files)
    canvas.d.ts
    canvas.js
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxss
  col/  (6 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxs
    index.wxss
  collapse/  (5 files)
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxss
  collapse-item/  (7 files)
    animate.d.ts
    animate.js
    index.d.ts
    index.js
    index.json
    index.wxml
    index.wxss
  common/  (10 files)
    style/  (3 files)
      … 3 files under this directory
    color.d.ts
    color.js
    component.d.ts
    component.js
    index.wxss
    relation.d.ts
    relation.js
.editorconfig
.eslintignore
.eslintrc
.gitignore
.prettierignore
.prettierrc
.stylelintrc
LICENSE
README.md
babel.config.js
jest.config.js
```

## Entry points

- [example/functions/foo/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/example/functions/foo/index.js)
- [lib/action-sheet/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/action-sheet/index.js)
- [lib/area/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/area/index.js)
- [lib/button/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/button/index.js)
- [lib/calendar/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/calendar/index.js)
- [lib/card/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/card/index.js)
- [lib/cascader/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/cascader/index.js)
- [lib/cell-group/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/cell-group/index.js)
- [lib/cell/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/cell/index.js)
- [lib/checkbox-group/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/checkbox-group/index.js)
- [lib/checkbox/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/checkbox/index.js)
- [lib/circle/index.js](https://github.com/youzan/vant-weapp/blob/5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f/lib/circle/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 44 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/template-1-bug-report-vant.zh-CN.yml` (config)
- `.github/ISSUE_TEMPLATE/template-3-feature-request-vant.zh-CN.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/pr-labeler.yml` (config)
- `.github/workflows/deploy-site.yml` (ci)
- `.github/workflows/pr-label.yaml` (ci)
- `.github/workflows/release-tag.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `example/app.json` (config)
- `example/components/demo-block/index.json` (config)
- `example/components/demo-home-nav/index.json` (config)
- `example/components/demo-home/index.json` (config)
- `example/database_area.json` (config)
- `example/functions/foo/package.json` (manifest)
- `example/pages/action-sheet/index.json` (config)
- `example/pages/area/index.json` (config)
- `example/pages/button/index.json` (config)
- `example/pages/calendar/index.json` (config)
- `example/pages/card/index.json` (config)
- `example/pages/cascader/index.json` (config)
- `example/pages/cell/index.json` (config)
- `example/pages/checkbox/index.json` (config)
- `example/pages/circle/index.json` (config)
- `example/pages/col/index.json` (config)
- `example/pages/collapse/index.json` (config)
- `example/pages/config-provider/index.json` (config)
- `example/pages/count-down/index.json` (config)
- `example/pages/dashboard/index.json` (config)
- `example/pages/datetime-picker/index.json` (config)
- `example/pages/dialog/index.json` (config)
- `example/pages/divider/index.json` (config)
- `example/pages/dropdown-menu/index.json` (config)
- `example/pages/empty/index.json` (config)
- `example/pages/field/index.json` (config)
- `example/pages/goods-action/index.json` (config)
- `example/pages/grid/index.json` (config)
- `example/pages/icon/index.json` (config)
- `example/pages/image/index.json` (config)
- `example/pages/index-bar/index.json` (config)
- `example/pages/loading/index.json` (config)
- `example/pages/nav-bar/index.json` (config)
- `example/pages/notice-bar/index.json` (config)
- `example/pages/notify/index.json` (config)
- `example/pages/overlay/index.json` (config)
- `example/pages/panel/index.json` (config)
- `example/pages/picker/index.json` (config)
- `example/pages/popup/index.json` (config)
- `example/pages/progress/index.json` (config)
- `example/pages/radio/index.json` (config)
- `example/pages/rate/index.json` (config)
- `example/pages/search/index.json` (config)
- `example/pages/share-sheet/index.json` (config)
- `example/pages/sidebar/index.json` (config)
- `example/pages/skeleton/index.json` (config)
- `example/pages/slider/index.json` (config)
- `example/pages/stepper/index.json` (config)
- `example/pages/steps/index.json` (config)
- `example/pages/sticky/index.json` (config)
- `example/pages/submit-bar/index.json` (config)
- `example/pages/swipe-cell/index.json` (config)
- `example/pages/switch/index.json` (config)
- `example/pages/tab/index.json` (config)
- `example/pages/tabbar/index.json` (config)
- `example/pages/tag/index.json` (config)
- `example/pages/toast/index.json` (config)
- `example/pages/transition/index.json` (config)
- `example/pages/tree-select/index.json` (config)
- `example/pages/uploader/index.json` (config)
- `example/project.config.json` (config)
- `example/sitemap.json` (config)
- `lib/action-sheet/index.json` (config)
- `lib/area/index.json` (config)
- `lib/button/index.json` (config)
- `lib/calendar/components/header/index.json` (config)
- `lib/calendar/components/month/index.json` (config)
- `lib/calendar/index.json` (config)
- `lib/card/index.json` (config)
- `lib/cascader/index.json` (config)
- `lib/cell-group/index.json` (config)
- `lib/cell/index.json` (config)
- `lib/checkbox-group/index.json` (config)
- `lib/checkbox/index.json` (config)
- `lib/circle/index.json` (config)
- `lib/col/index.json` (config)
- `lib/collapse-item/index.json` (config)
- `lib/collapse/index.json` (config)

## Top-level layout

- `example` — 189 analysed file(s)
- `lib` — 106 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 11 analysed file(s)
- `docs` — 5 analysed file(s)
- `.husky` — 3 analysed file(s)
- `.gitee` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 474 file(s) were skipped during inventory (1 x likely secret file excluded; 473 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5856ed6b1bc4fc8e9cdac73e61ebbf0df0be134f` is the revision these paths and observations refer to.
