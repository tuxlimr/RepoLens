# Project structure: ant-design/ant-design-mobile-rn

**Analysed commit:** `ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1`

**Commit reference:** [ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1](https://github.com/ant-design/ant-design-mobile-rn/commit/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1)

**Tree at this commit:** [ant-design/ant-design-mobile-rn@ebf8a8d2f880](https://github.com/ant-design/ant-design-mobile-rn/tree/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ant-design/ant-design-mobile-rn |
| Description | Ant Design for React Native |
| Stars | 3343 |
| Forks | 612 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1` |
| Retrieved at | 2026-11-14T19:15:22.796147+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.dumi/  (78 files)
  _llms/  (37 files)
    accordion/  (1 files)
      … 1 files under this directory
    action-sheet/  (1 files)
      … 1 files under this directory
    activity-indicator/  (1 files)
      … 1 files under this directory
    badge/  (1 files)
      … 1 files under this directory
    button/  (1 files)
      … 1 files under this directory
    card/  (1 files)
      … 1 files under this directory
    carousel/  (1 files)
      … 1 files under this directory
    checkbox/  (1 files)
      … 1 files under this directory
    divider/  (1 files)
      … 1 files under this directory
    form/  (1 files)
      … 1 files under this directory
    grid/  (1 files)
      … 1 files under this directory
    input/  (1 files)
      … 1 files under this directory
    input-item/  (1 files)
      … 1 files under this directory
    list/  (1 files)
      … 1 files under this directory
    modal/  (1 files)
      … 1 files under this directory
    notice-bar/  (1 files)
      … 1 files under this directory
    pagination/  (1 files)
      … 1 files under this directory
    picker/  (1 files)
      … 1 files under this directory
    picker-view/  (1 files)
      … 1 files under this directory
    popover/  (1 files)
      … 1 files under this directory
    progress/  (1 files)
      … 1 files under this directory
    radio/  (1 files)
      … 1 files under this directory
    rate/  (1 files)
      … 1 files under this directory
    result/  (1 files)
      … 1 files under this directory
    search-bar/  (1 files)
      … 1 files under this directory
    skeleton/  (1 files)
      … 1 files under this directory
    slider/  (1 files)
      … 1 files under this directory
    stepper/  (1 files)
      … 1 files under this directory
    steps/  (1 files)
      … 1 files under this directory
    swipe-action/  (1 files)
      … 1 files under this directory
    switch/  (1 files)
      … 1 files under this directory
    tab-bar/  (1 files)
      … 1 files under this directory
    tabs/  (1 files)
      … 1 files under this directory
    tag/  (1 files)
      … 1 files under this directory
    textarea-item/  (1 files)
      … 1 files under this directory
    toast/  (1 files)
      … 1 files under this directory
    tooltip/  (1 files)
      … 1 files under this directory
  loaders/  (1 files)
    type-only-stub-loader.js
  pages/  (5 files)
    404/  (1 files)
      … 1 files under this directory
    index/  (2 files)
      … 2 files under this directory
    index-cn/  (2 files)
      … 2 files under this directory
  theme/  (31 files)
    builtins/  (10 files)
      … 10 files under this directory
    layouts/  (3 files)
      … 3 files under this directory
    locales/  (2 files)
      … 2 files under this directory
    plugins/  (3 files)
      … 3 files under this directory
    slots/  (11 files)
      … 11 files under this directory
    plugin.ts
    utils.ts
  global.less
  global.tsx
  theme.d.ts
  tsconfig.json
.github/  (9 files)
  ISSUE_TEMPLATE/  (4 files)
    ISSUE_TEMPLATE.md
    bug_report.yml
    bug_report_zh.yml
    config.yml
  workflows/  (2 files)
    issue-close-require.yml
    issue-open-check.yml
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
  lock.yml
.vscode/  (1 files)
  settings.json
components/  (616 files)
  _util/  (11 files)
    hooks/  (4 files)
      … 4 files under this directory
    devWarning.tsx
    getLocale.tsx
    isPromise.ts
    reactNode.ts
    traverse-react-node.tsx
    version.json
    with-default-props.tsx
  accordion/  (8 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  action-sheet/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    AndroidContainer.tsx
    index.en-US.md
    index.native.tsx
    index.tsx
    index.zh-CN.md
  activity-indicator/  (8 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  badge/  (9 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  button/  (11 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    ButtonWave.tsx
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  card/  (11 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    CardBody.tsx
    CardFooter.tsx
    CardHeader.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  carousel/  (9 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  checkbox/  (12 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    AgreeItem.tsx
    Checkbox.tsx
    CheckboxItem.tsx
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  collapse/  (8 files)
    demo/  (2 files)
      … 2 files under this directory
    CollapsePanelContent.tsx
    PropsType.tsx
    collapse.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  date-picker/  (22 files)
    datepicker/  (1 files)
      … 1 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    locale/  (9 files)
      … 9 files under this directory
    PropsType.tsx
    columns-extend.tsx
    date-picker-date-utils.ts
    date-picker-utils.ts
    date-picker-week-utils.ts
    date-picker.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    util.ts
  date-picker-view/  (17 files)
    demo/  (2 files)
      … 2 files under this directory
    locale/  (9 files)
      … 9 files under this directory
    PropsType.tsx
    date-picker-view.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    useRenderLabel.ts
  divider/  (11 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Divider.tsx
    Line.tsx
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  drawer/  (8 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  flex/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    Flex.tsx
    FlexItem.tsx
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  form/  (35 files)
    FormItem/  (3 files)
      … 3 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    hooks/  (8 files)
      … 8 files under this directory
    locale/  (9 files)
      … 9 files under this directory
    style/  (1 files)
      … 1 files under this directory
    ErrorList.tsx
    Form.tsx
    FormItemLabel.tsx
    FormList.tsx
    PropsType.tsx
    context.tsx
    index.en-US.md
    index.ts
    index.zh-CN.md
    interface.ts
    util.ts
    validateMessagesContext.tsx
  grid/  (9 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  icon/  (6 files)
    __tests__/  (1 files)
      … 1 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  image-picker/  (2 files)
    index.en-US.md
    index.zh-CN.md
  input/  (13 files)
    TextArea/  (3 files)
      … 3 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (2 files)
      … 2 files under this directory
    Input.tsx
    Item.tsx
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  input-item/  (18 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    locale/  (8 files)
      … 8 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Input.tsx
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  list/  (12 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Brief.tsx
    List.tsx
    ListItem.tsx
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  list-view/  (13 files)
    demo/  (2 files)
      … 2 files under this directory
    locale/  (8 files)
      … 8 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  locale-provider/  (10 files)
    en_US.tsx
    es_ES.tsx
    fa_IR.tsx
    index.tsx
    ko_KR.tsx
    pt_BR.tsx
    ru_RU.tsx
    sv_SE.tsx
    useLocale.tsx
    zh_CN.tsx
  modal/  (27 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    locale/  (8 files)
      … 8 files under this directory
    style/  (2 files)
      … 2 files under this directory
    useModal/  (1 files)
      … 1 files under this directory
    AlertContainer.tsx
    Modal.tsx
    ModalView.tsx
    OperationContainer.tsx
    PromptContainer.tsx
    PropsType.tsx
    alert.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    operation.tsx
    prompt.tsx
  notice-bar/  (9 files)
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Marquee.tsx
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    notice-bar.tsx
  pagination/  (18 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    locale/  (8 files)
      … 8 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  picker/  (24 files)
    __tests__/  (4 files)
      … 4 files under this directory
    demo/  (3 files)
      … 3 files under this directory
    locale/  (9 files)
      … 9 files under this directory
    style/  (1 files)
      … 1 files under this directory
    Picker.tsx
    Popup.tsx
    PopupPickerTypes.tsx
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  picker-view/  (10 files)
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    Wheel.tsx
    columns-extend.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    picker-view.tsx
  popover/  (8 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  portal/  (7 files)
    demo/  (1 files)
      … 1 files under this directory
    _README.md
    index.tsx
    portal-consumer.tsx
    portal-host.tsx
    portal-manager.tsx
    portal.tsx
  progress/  (9 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  provider/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    AccessibilityContext.tsx
    DisabledContext.tsx
    HapticsContext.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  radio/  (13 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    Radio.tsx
    RadioContext.tsx
    RadioGroup.tsx
    RadioItem.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  rate/  (13 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    AnimatedIcon.tsx
    PropsType.tsx
    RateIcon.tsx
    constants.ts
    index.en-US.md
    index.tsx
    index.zh-CN.md
    utils.ts
  result/  (10 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  search-bar/  (18 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    locale/  (8 files)
      … 8 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  segmented-control/  (2 files)
    index.en-US.md
    index.zh-CN.md
  skeleton/  (13 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    Skeleton.tsx
    SkeletonParagraph.tsx
    SkeletonProvider.tsx
    SkeletonTitle.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  slider/  (13 files)
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    marks.tsx
    slider.tsx
    thumb-icon.tsx
    thumb-popover.tsx
    thumb.tsx
    ticks.tsx
  stepper/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    stepper.tsx
  steps/  (9 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    StepsItem.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  style/  (2 files)
    themes/  (1 files)
      … 1 files under this directory
    index.tsx
  swipe-action/  (11 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    RenderActions.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    swipe-action.tsx
  switch/  (9 files)
    __tests__/  (1 files)
      … 1 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    Switch.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  tab-bar/  (10 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    TabBarItem.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  tabs/  (12 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (2 files)
      … 2 files under this directory
    DefaultTabBar.tsx
    PropsType.tsx
    Tabs.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  tag/  (10 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  text/  (1 files)
    index.tsx
  textarea-item/  (9 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
  toast/  (12 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    useToast/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    ToastContainer.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    methods.tsx
  tooltip/  (11 files)
    demo/  (2 files)
      … 2 files under this directory
    style/  (1 files)
      … 1 files under this directory
    PropsType.tsx
    Tooltip.tsx
    TooltipMenu.tsx
    Wrapper.tsx
    index.en-US.md
    index.tsx
    index.zh-CN.md
    normalize-placement.ts
  view/  (7 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  white-space/  (7 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  wing-blank/  (7 files)
    __tests__/  (2 files)
      … 2 files under this directory
    demo/  (2 files)
      … 2 files under this directory
    index.en-US.md
    index.tsx
    index.zh-CN.md
  index.tsx
  types.ts
docs/  (12 files)
  blog/  (6 files)
    headless.en-US.md
    headless.zh-CN.md
    llms-docs.en-US.md
    llms-docs.zh-CN.md
    what-is-styles.en-US.md
    what-is-styles.zh-CN.md
  react/  (6 files)
    introduce.en-US.md
    introduce.zh-CN.md
    support.en-US.md
    support.zh-CN.md
    upgrade-notes.en-US.md
    upgrade-notes.zh-CN.md
example/  (16 files)
  app/  (4 files)
    demo/  (1 files)
      … 1 files under this directory
    +html.tsx
    _layout.tsx
    index.tsx
  public/  (1 files)
    index.html
  .gitignore
  .nvmrc
  README.md
  app.config.js
  app.json
  babel.config.js
  eas.json
  index.js
  metro.config.js
  package.json
  tsconfig.json
rn-kitchen-sink/  (38 files)
  android/  (19 files)
    app/  (13 files)
      … 13 files under this directory
    gradle/  (1 files)
      … 1 files under this directory
    build.gradle
    gradle.properties
    gradlew
    gradlew.bat
    settings.gradle
  components/  (2 files)
    Theme.js
    index.js
  ios/  (14 files)
    KitchenSink/  (7 files)
      … 7 files under this directory
    KitchenSink.xcodeproj/  (2 files)
      … 2 files under this directory
    KitchenSink.xcworkspace/  (2 files)
      … 2 files under this directory
    KitchenSinkTests/  (2 files)
      … 2 files under this directory
    Podfile
  App.js
  demoList.js
  icon.svg
scripts/  (1 files)
  copy-app-res.js
.buckconfig
.dumirc.ts
.editorconfig
.flowconfig
.gitignore
.jest.config.js
.npmignore
.nvmrc
.prettierrc
.travis.yml
.watchmanconfig
AGENTS.md
AUTHORS.txt
CHANGELOG.en-US.md
CHANGELOG.zh-CN.md
CLAUDE.md
CNAME
LICENSE
README.md
README.zh-CN.md
babel.config.js
development.en-US.md
development.zh-CN.md
eslint.config.js
… 5 more files
```

## Entry points

- [example/index.js](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/example/index.js)
- [.dumi/pages/404/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/.dumi/pages/404/index.tsx)
- [components/accordion/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/components/accordion/index.tsx)
- [components/accordion/style/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/components/accordion/style/index.tsx)
- [components/action-sheet/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/components/action-sheet/index.tsx)
- [components/action-sheet/style/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/components/action-sheet/style/index.tsx)
- [components/activity-indicator/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/components/activity-indicator/index.tsx)
- [components/activity-indicator/style/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/components/activity-indicator/style/index.tsx)
- [components/badge/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/components/badge/index.tsx)
- [components/badge/style/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/components/badge/style/index.tsx)
- [components/button/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/components/button/index.tsx)
- [components/button/style/index.tsx](https://github.com/ant-design/ant-design-mobile-rn/blob/ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1/components/button/style/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 430 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| rn-kitchen-sink package | library | Observed | Groups 8 file(s) under rn-kitchen-sink package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.dumi/theme/locales/en-US.json` (config)
- `.dumi/theme/locales/zh-CN.json` (config)
- `.dumi/tsconfig.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report_zh.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/lock.yml` (config)
- `.github/workflows/issue-close-require.yml` (ci)
- `.github/workflows/issue-open-check.yml` (ci)
- `.travis.yml` (ci)
- `.vscode/settings.json` (config)
- `components/_util/version.json` (config)
- `components/picker/demo/data.json` (config)
- `example/app.json` (config)
- `example/eas.json` (config)
- `example/package.json` (manifest)
- `example/tsconfig.json` (config)
- `package.json` (manifest)
- `rn-kitchen-sink/android/app/build.gradle` (manifest)
- `rn-kitchen-sink/android/build.gradle` (manifest)
- `rn-kitchen-sink/ios/KitchenSink/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `rn-kitchen-sink/ios/KitchenSink/Images.xcassets/Contents.json` (config)

## Top-level layout

- `components` — 616 analysed file(s)
- `.dumi` — 78 analysed file(s)
- `rn-kitchen-sink` — 38 analysed file(s)
- `(root files)` — 29 analysed file(s)
- `example` — 16 analysed file(s)
- `docs` — 12 analysed file(s)
- `.github` — 9 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ebf8a8d2f8808623893980eaebb7ca6b5c0a77c1` is the revision these paths and observations refer to.
