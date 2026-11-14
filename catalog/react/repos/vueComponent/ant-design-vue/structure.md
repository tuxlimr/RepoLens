# Project structure: vueComponent/ant-design-vue

**Analysed commit:** `7483836f0adac76516e527df893c3d84a7cd4005`

**Commit reference:** [7483836f0adac76516e527df893c3d84a7cd4005](https://github.com/vueComponent/ant-design-vue/commit/7483836f0adac76516e527df893c3d84a7cd4005)

**Tree at this commit:** [vueComponent/ant-design-vue@7483836f0ada](https://github.com/vueComponent/ant-design-vue/tree/7483836f0adac76516e527df893c3d84a7cd4005)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vueComponent/ant-design-vue |
| Description | 🌈  An enterprise-class UI components based on Ant Design and Vue. 🐜 |
| Stars | 21714 |
| Forks | 3884 |
| Licence | Other |
| Language | Vue |
| Default branch | main |
| Analysed commit | `7483836f0adac76516e527df893c3d84a7cd4005` |
| Retrieved at | 2026-11-14T19:13:10.120965+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (15 files)
  ISSUE_TEMPLATE/  (1 files)
    config.yml
  PULL_REQUEST_TEMPLATE/  (2 files)
    pr_cn.md
    pr_en.md
  workflows/  (10 files)
    ai-co-author.yml
    cloudflare.yml
    codecov.yml
    emoji-helper.yml
    issue-close-require.yml
    issue-labeled.yml
    issue-open-check.yml
    lock-issue.yml
    stale.yml
    test.yml
  FUNDING.yml
  issue-close-app.yml
.husky/  (2 files)
  .gitignore
  pre-commit
antd-tools/  (25 files)
  cli/  (2 files)
    index.js
    run.js
  generator-types/  (9 files)
    src/  (6 files)
      … 6 files under this directory
    README.md
    index.js
    tsconfig.json
  utils/  (5 files)
    CleanUpStatsPlugin.js
    get-npm-args.js
    getChangelog.js
    getRunCmdEnv.js
    projectHelper.js
  apiCollection.js
  getBabelCommonConfig.js
  getNpm.js
  getTSCommonConfig.js
  getWebpackConfig.js
  gulpfile.js
  replaceLib.js
  runCmd.js
  sortApiTable.js
components/  (734 files)
  __tests__/  (1 files)
    util/  (1 files)
      … 1 files under this directory
  _util/  (118 files)
    __mocks__/  (2 files)
      … 2 files under this directory
    __tests__/  (4 files)
      … 4 files under this directory
    copy-to-clipboard/  (2 files)
      … 2 files under this directory
    cssinjs/  (26 files)
      … 26 files under this directory
    hooks/  (21 files)
      … 21 files under this directory
    props-util/  (2 files)
      … 2 files under this directory
    static-style-extract/  (3 files)
      … 3 files under this directory
    vue-types/  (1 files)
      … 1 files under this directory
    wave/  (5 files)
      … 5 files under this directory
    ActionButton.tsx
    BaseInput.tsx
    BaseInputInner.tsx
    BaseMixin.ts
    EventInterface.ts
    KeyCode.ts
    Portal.tsx
    PortalWrapper.tsx
    canUseDom.ts
    classNames.ts
    collapseMotion.tsx
    colors.ts
    component-classes.ts
    createContext.ts
    createRef.ts
    debouncedWatch.ts
    eagerComputed.ts
    easings.ts
    env.ts
    extendsObject.ts
    firstNotUndefined.ts
    gapSize.ts
    getRequestAnimationFrame.ts
    getScroll.ts
    … 28 more files
  affix/  (12 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (4 files)
      … 4 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
    utils.ts
  alert/  (18 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (11 files)
      … 11 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  anchor/  (18 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (8 files)
      … 8 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Anchor.tsx
    AnchorLink.tsx
    context.ts
    index.en-US.md
    index.tsx
    index.zh-CN.md
  app/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (3 files)
      … 3 files under this directory
    style/  (1 files)
      … 1 files under this directory
    context.ts
    index.en-US.md
    index.tsx
    index.zh-CN.md
  auto-complete/  (18 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (10 files)
      … 10 files under this directory
    OptGroup.tsx
    Option.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  avatar/  (18 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (7 files)
      … 7 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Avatar.tsx
    AvatarContext.ts
    Group.tsx
    index.en-US.md
    index.ts
    index.zh-CN.md
  badge/  (23 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (11 files)
      … 11 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Badge.tsx
    Ribbon.tsx
    ScrollNumber.tsx
    SingleNumber.tsx
    index.en_US.md
    index.ts
    index.zh-CN.md
  breadcrumb/  (18 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (7 files)
      … 7 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Breadcrumb.tsx
    BreadcrumbItem.tsx
    BreadcrumbSeparator.tsx
    index.en-US.md
    index.ts
    index.zh-CN.md
  button/  (25 files)
    __tests__/  (5 files)
      … 5 files under this directory
    demo/  (11 files)
      … 11 files under this directory
    style/  (2 files)
      … 2 files under this directory
    LoadingIcon.tsx
    button-group.tsx
    button.tsx
    buttonTypes.ts
    index.en-US.md
    index.ts
    index.zh-CN.md
  calendar/  (81 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (6 files)
      … 6 files under this directory
    locale/  (62 files)
      … 62 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Header.tsx
    date-fns.tsx
    dayjs.tsx
    generateCalendar.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    moment.tsx
  card/  (22 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (11 files)
      … 11 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Card.tsx
    Grid.tsx
    Meta.tsx
    index.en-US.md
    index.ts
    index.zh-CN.md
  carousel/  (15 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (7 files)
      … 7 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  cascader/  (22 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (14 files)
      … 14 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  checkbox/  (19 files)
    __tests__/  (5 files)
      … 5 files under this directory
    demo/  (7 files)
      … 7 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Checkbox.tsx
    Group.tsx
    index.en-US.md
    index.ts
    index.zh-CN.md
    interface.ts
  col/  (2 files)
    style/  (1 files)
      … 1 files under this directory
    index.ts
  collapse/  (22 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (10 files)
      … 10 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Collapse.tsx
    CollapsePanel.tsx
    PanelContent.tsx
    commonProps.ts
    index.en-US.md
    index.ts
    index.zh-CN.md
  comment/  (13 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (5 files)
      … 5 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  config-provider/  (17 files)
    __tests__/  (1 files)
      … 1 files under this directory
    demo/  (5 files)
      … 5 files under this directory
    hooks/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    DisabledContext.ts
    SizeContext.ts
    context.ts
    cssVariables.ts
    index.en-US.md
    index.tsx
    index.zh-CN.md
    renderEmpty.tsx
  date-picker/  (112 files)
    __tests__/  (14 files)
      … 14 files under this directory
    demo/  (20 files)
      … 20 files under this directory
    generatePicker/  (5 files)
      … 5 files under this directory
    locale/  (63 files)
      … 63 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PickerButton.tsx
    PickerTag.tsx
    date-fns.tsx
    dayjs.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    moment.tsx
    util.ts
  descriptions/  (17 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (7 files)
      … 7 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Cell.tsx
    Row.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  divider/  (12 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (5 files)
      … 5 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  drawer/  (22 files)
    __tests__/  (7 files)
      … 7 files under this directory
    demo/  (10 files)
      … 10 files under this directory
    style/  (2 files)
      … 2 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  dropdown/  (26 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (13 files)
      … 13 files under this directory
    style/  (3 files)
      … 3 files under this directory
    dropdown-button.tsx
    dropdown.tsx
    index.en-US.md
    index.ts
    index.zh-CN.md
    props.ts
  empty/  (15 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (6 files)
      … 6 files under this directory
    style/  (1 files)
      … 1 files under this directory
    empty.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    simple.tsx
  flex/  (15 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (6 files)
      … 6 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
    interface.ts
    utils.ts
  float-button/  (22 files)
    __tests__/  (5 files)
      … 5 files under this directory
    demo/  (10 files)
      … 10 files under this directory
    BackTop.tsx
    FloatButton.tsx
    FloatButtonContent.tsx
    FloatButtonGroup.tsx
    context.ts
    index.en-US.md
    index.ts
  components.ts
.antd-tools.config.js
.codecov.yml
.editorconfig
.eslintignore
.eslintrc.js
.gitattributes
.gitignore
.huskyrc
.jest.js
.prettierignore
.prettierrc
.stylelintrc
.stylelintrc.json
.vcmrc
BACKERS.md
CHANGELOG.en-US.md
CHANGELOG.zh-CN.md
LICENSE
README-zh_CN.md
README.md
SECURITY.md
babel.config.js
build.sh
```

## Entry points

- [antd-tools/cli/index.js](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/antd-tools/cli/index.js)
- [antd-tools/generator-types/index.js](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/antd-tools/generator-types/index.js)
- [antd-tools/generator-types/src/index.ts](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/antd-tools/generator-types/src/index.ts)
- [components/_util/copy-to-clipboard/index.ts](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/components/_util/copy-to-clipboard/index.ts)
- [components/_util/cssinjs/index.ts](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/components/_util/cssinjs/index.ts)
- [components/_util/props-util/index.ts](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/components/_util/props-util/index.ts)
- [components/_util/static-style-extract/index.tsx](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/components/_util/static-style-extract/index.tsx)
- [components/_util/vue-types/index.ts](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/components/_util/vue-types/index.ts)
- [components/_util/wave/index.tsx](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/components/_util/wave/index.tsx)
- [components/affix/index.tsx](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/components/affix/index.tsx)
- [components/affix/style/index.ts](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/components/affix/style/index.ts)
- [components/alert/index.tsx](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/components/alert/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| antd-tools package | library | Observed | Groups 23 file(s) under antd-tools package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 639 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |

## Important files

- `.codecov.yml` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/issue-close-app.yml` (config)
- `.github/workflows/ai-co-author.yml` (ci)
- `.github/workflows/cloudflare.yml` (ci)
- `.github/workflows/codecov.yml` (ci)
- `.github/workflows/emoji-helper.yml` (ci)
- `.github/workflows/issue-close-require.yml` (ci)
- `.github/workflows/issue-labeled.yml` (ci)
- `.github/workflows/issue-open-check.yml` (ci)
- `.github/workflows/lock-issue.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.stylelintrc.json` (config)
- `antd-tools/generator-types/tsconfig.json` (config)
- `components/date-picker/locale/example.json` (config)

## Top-level layout

- `components` — 734 analysed file(s)
- `antd-tools` — 25 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `.github` — 15 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7483836f0adac76516e527df893c3d84a7cd4005` is the revision these paths and observations refer to.
