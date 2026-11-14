# Project structure: jd-opensource/taro-ui

**Analysed commit:** `d0653307e44015ebf6de382f0a31dab4c9756e15`

**Commit reference:** [d0653307e44015ebf6de382f0a31dab4c9756e15](https://github.com/jd-opensource/taro-ui/commit/d0653307e44015ebf6de382f0a31dab4c9756e15)

**Tree at this commit:** [jd-opensource/taro-ui@d0653307e440](https://github.com/jd-opensource/taro-ui/tree/d0653307e44015ebf6de382f0a31dab4c9756e15)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jd-opensource/taro-ui |
| Description | 一款基于 Taro 框架开发的多端 UI 组件库 |
| Stars | 4732 |
| Forks | 741 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | next |
| Analysed commit | `d0653307e44015ebf6de382f0a31dab4c9756e15` |
| Retrieved at | 2026-11-14T19:14:38.051811+00:00 |
| Files in this snapshot | 787 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (2 files)
    BUG_REPORT.md
    FEATURE_REQUEST.md
  workflows/  (7 files)
    deploy-pages.yml
    deploy-tcb.yml
    node.yml
    publish.yml
    rn-release.yml
    stale.yml
    test.yml
  CONTRIBUTING.md
.husky/  (2 files)
  commit-msg
  pre-commit
docs/  (177 files)
  .vitepress/  (5 files)
    theme/  (4 files)
      … 4 files under this directory
    config.mts
  assets/  (7 files)
    style/  (4 files)
      … 4 files under this directory
    dark.svg
    light.svg
    taro-ui-roadmap.svg
  components/  (9 files)
    footer/  (2 files)
      … 2 files under this directory
    header/  (2 files)
      … 2 files under this directory
    iconlist/  (3 files)
      … 3 files under this directory
    sidebar/  (2 files)
      … 2 files under this directory
  docs/  (59 files)
    components/  (50 files)
      … 50 files under this directory
    guide/  (8 files)
      … 8 files under this directory
    index.md
  lib/  (3 files)
    animations/  (2 files)
      … 2 files under this directory
    default.scss
  pages/  (3 files)
    docs.jsx
    guide.jsx
    index.jsx
  scripts/  (1 files)
    migrate-md.js
  utils/  (1 files)
    const.js
  view/  (81 files)
    Accordion/  (1 files)
      … 1 files under this directory
    ActionSheet/  (2 files)
      … 2 files under this directory
    ActivityIndicator/  (2 files)
      … 2 files under this directory
    Article/  (2 files)
      … 2 files under this directory
    Avatar/  (2 files)
      … 2 files under this directory
    Badge/  (2 files)
      … 2 files under this directory
    Button/  (2 files)
      … 2 files under this directory
    Calendar/  (1 files)
      … 1 files under this directory
    Card/  (2 files)
      … 2 files under this directory
    Changelog/  (2 files)
      … 2 files under this directory
    Checkbox/  (1 files)
      … 1 files under this directory
    Color/  (2 files)
      … 2 files under this directory
    ConfigProvider/  (1 files)
      … 1 files under this directory
    Countdown/  (1 files)
      … 1 files under this directory
    Curtain/  (1 files)
      … 1 files under this directory
    CustomizeTheme/  (1 files)
      … 1 files under this directory
    Divider/  (1 files)
      … 1 files under this directory
    Drawer/  (2 files)
      … 2 files under this directory
    Fab/  (1 files)
      … 1 files under this directory
    Flex/  (2 files)
      … 2 files under this directory
    FloatLayout/  (2 files)
      … 2 files under this directory
    Form/  (2 files)
      … 2 files under this directory
    Grid/  (2 files)
      … 2 files under this directory
    Icon/  (2 files)
      … 2 files under this directory
    ImagePicker/  (1 files)
      … 1 files under this directory
    Indexes/  (1 files)
      … 1 files under this directory
    Input/  (1 files)
      … 1 files under this directory
    InputNumber/  (1 files)
      … 1 files under this directory
    Introduction/  (1 files)
      … 1 files under this directory
    List/  (2 files)
      … 2 files under this directory
    LoadMore/  (1 files)
      … 1 files under this directory
    Message/  (1 files)
      … 1 files under this directory
    Modal/  (2 files)
      … 2 files under this directory
    NavBar/  (1 files)
      … 1 files under this directory
    Noticebar/  (2 files)
      … 2 files under this directory
    Pagination/  (2 files)
      … 2 files under this directory
    Picker/  (1 files)
      … 1 files under this directory
    Progress/  (2 files)
      … 2 files under this directory
    Questions/  (2 files)
      … 2 files under this directory
    Quickstart/  (1 files)
      … 1 files under this directory
    Radio/  (1 files)
      … 1 files under this directory
    Range/  (1 files)
      … 1 files under this directory
    Rate/  (1 files)
      … 1 files under this directory
    Resource/  (1 files)
      … 1 files under this directory
    SearchBar/  (1 files)
      … 1 files under this directory
    SegmentedControl/  (1 files)
      … 1 files under this directory
    Slider/  (1 files)
      … 1 files under this directory
    Steps/  (1 files)
      … 1 files under this directory
    SwipeAction/  (1 files)
      … 1 files under this directory
    Swiper/  (1 files)
      … 1 files under this directory
    Switch/  (1 files)
      … 1 files under this directory
    TabBar/  (1 files)
      … 1 files under this directory
    Tabs/  (1 files)
      … 1 files under this directory
    Tag/  (2 files)
      … 2 files under this directory
    Textarea/  (1 files)
      … 1 files under this directory
    Timeline/  (2 files)
      … 2 files under this directory
    Toast/  (2 files)
      … 2 files under this directory
  CHANGELOG.md
  MAINTENANCE.md
  MIGRATION_FC.md
  app.jsx
  index.html
  nav.config.yml
  package.json
  page-route.js
examples/  (510 files)
  demo/  (183 files)
    config/  (3 files)
      … 3 files under this directory
    src/  (173 files)
      … 173 files under this directory
    .node-version
    CHANGELOG.md
    babel.config.js
    global.d.ts
    package.json
    project.config.json
    tsconfig.json
  demo-rn/  (128 files)
    config/  (3 files)
      … 3 files under this directory
    src/  (117 files)
      … 117 files under this directory
    CHANGELOG.md
    babel.config.js
    global.d.ts
    index.js
    metro.config.js
    package.json
    project.config.json
    tsconfig.json
  demo-v4/  (180 files)
    config/  (3 files)
      … 3 files under this directory
    src/  (170 files)
      … 170 files under this directory
    .node-version
    CHANGELOG.md
    babel.config.js
    global.d.ts
    package.json
    project.config.json
    tsconfig.json
  lazy-load-component/  (19 files)
    config/  (3 files)
      … 3 files under this directory
    src/  (7 files)
      … 7 files under this directory
    types/  (1 files)
      … 1 files under this directory
    .eslintrc
    .gitignore
    README.md
    babel.config.js
    package.json
    project.config.json
    project.tt.json
    tsconfig.json
packages/  (70 files)
  taro-ui/  (21 files)
    config/  (2 files)
      … 2 files under this directory
    rn/  (14 files)
      … 14 files under this directory
    CHANGELOG.md
    README.md
    babel.config.json
    jest.config.js
    package.json
  taro-ui-guide/  (49 files)
    references/  (48 files)
      … 48 files under this directory
    SKILL.md
.editorconfig
.eslintignore
.eslintrc.json
.gitignore
.node-version
.prettierrc.json
.stylelintignore
.stylelintrc.json
.travis.yml
CHANGELOG.md
LICENSE
PLANS.md
README.md
RN.md
ROADMAP.md
babel.config.json
commitlint.config.js
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 1 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/workflows/deploy-pages.yml` (ci)
- `.github/workflows/deploy-tcb.yml` (ci)
- `.github/workflows/node.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/rn-release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.prettierrc.json` (config)
- `.stylelintrc.json` (config)
- `.travis.yml` (ci)
- `babel.config.json` (config)
- `docs/nav.config.yml` (config)
- `docs/package.json` (manifest)
- `examples/demo-rn/package.json` (manifest)
- `examples/demo-rn/project.config.json` (config)
- `examples/demo-rn/tsconfig.json` (config)
- `examples/demo-v4/package.json` (manifest)
- `examples/demo-v4/project.config.json` (config)
- `examples/demo-v4/tsconfig.json` (config)
- `examples/demo/package.json` (manifest)
- `examples/demo/project.config.json` (config)
- `examples/demo/tsconfig.json` (config)
- `examples/lazy-load-component/package.json` (manifest)
- `examples/lazy-load-component/project.config.json` (config)
- `examples/lazy-load-component/project.tt.json` (config)
- `examples/lazy-load-component/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/taro-ui/babel.config.json` (config)
- `packages/taro-ui/package.json` (manifest)

## Top-level layout

- `examples` — 510 analysed file(s)
- `docs` — 177 analysed file(s)
- `packages` — 70 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 10 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 13 file(s) were skipped during inventory (1 x likely secret file excluded; 12 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d0653307e44015ebf6de382f0a31dab4c9756e15` is the revision these paths and observations refer to.
