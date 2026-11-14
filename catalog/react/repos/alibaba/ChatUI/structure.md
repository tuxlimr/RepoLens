# Project structure: alibaba/ChatUI

**Analysed commit:** `06c3126ad25a0735c9b48f40582075371ad04cf3`

**Commit reference:** [06c3126ad25a0735c9b48f40582075371ad04cf3](https://github.com/alibaba/ChatUI/commit/06c3126ad25a0735c9b48f40582075371ad04cf3)

**Tree at this commit:** [alibaba/ChatUI@06c3126ad25a](https://github.com/alibaba/ChatUI/tree/06c3126ad25a0735c9b48f40582075371ad04cf3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alibaba/ChatUI |
| Description | The UI design language and React library for Conversational UI |
| Stars | 4464 |
| Forks | 426 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `06c3126ad25a0735c9b48f40582075371ad04cf3` |
| Retrieved at | 2026-11-14T19:14:44.827285+00:00 |
| Files in this snapshot | 510 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    feature-request-------.md
.husky/  (2 files)
  .gitignore
  commit-msg
demo/  (85 files)
  src/  (78 files)
    components/  (5 files)
      … 5 files under this directory
    demo/  (64 files)
      … 64 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    index.less
    main.tsx
    navConfig.ts
    routerConfig.tsx
    vite-env.d.ts
  .gitignore
  index.html
  package.json
  tsconfig.app.json
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
src/  (403 files)
  components/  (353 files)
    Avatar/  (4 files)
      … 4 files under this directory
    BackBottom/  (3 files)
      … 3 files under this directory
    Backdrop/  (4 files)
      … 4 files under this directory
    Bubble/  (4 files)
      … 4 files under this directory
    Button/  (4 files)
      … 4 files under this directory
    Card/  (16 files)
      … 16 files under this directory
    Carousel/  (4 files)
      … 4 files under this directory
    Chat/  (3 files)
      … 3 files under this directory
    Checkbox/  (6 files)
      … 6 files under this directory
    ClickOutside/  (3 files)
      … 3 files under this directory
    ComponentsProvider/  (4 files)
      … 4 files under this directory
    Composer/  (11 files)
      … 11 files under this directory
    ConfigProvider/  (8 files)
      … 8 files under this directory
    Countdown/  (3 files)
      … 3 files under this directory
    Coupon/  (3 files)
      … 3 files under this directory
    Divider/  (4 files)
      … 4 files under this directory
    Empty/  (4 files)
      … 4 files under this directory
    ErrorBoundary/  (2 files)
      … 2 files under this directory
    FileCard/  (4 files)
      … 4 files under this directory
    Filter/  (3 files)
      … 3 files under this directory
    Flex/  (7 files)
      … 7 files under this directory
    Form/  (9 files)
      … 9 files under this directory
    Goods/  (4 files)
      … 4 files under this directory
    HelpText/  (4 files)
      … 4 files under this directory
    Icon/  (4 files)
      … 4 files under this directory
    IconButton/  (4 files)
      … 4 files under this directory
    Image/  (4 files)
      … 4 files under this directory
    ImageList/  (3 files)
      … 3 files under this directory
    InfiniteScroll/  (3 files)
      … 3 files under this directory
    Input/  (4 files)
      … 4 files under this directory
    KvList/  (5 files)
      … 5 files under this directory
    Label/  (4 files)
      … 4 files under this directory
    LazyComponent/  (4 files)
      … 4 files under this directory
    List/  (6 files)
      … 6 files under this directory
    Loading/  (4 files)
      … 4 files under this directory
    MediaObject/  (4 files)
      … 4 files under this directory
    Message/  (6 files)
      … 6 files under this directory
    MessageContainer/  (4 files)
      … 4 files under this directory
    MessageStatus/  (3 files)
      … 3 files under this directory
    Modal/  (11 files)
      … 11 files under this directory
    MultiRedPacket/  (3 files)
      … 3 files under this directory
    Navbar/  (4 files)
      … 4 files under this directory
    Notice/  (4 files)
      … 4 files under this directory
    OrderObject/  (3 files)
      … 3 files under this directory
    Popover/  (4 files)
      … 4 files under this directory
    Portal/  (2 files)
      … 2 files under this directory
    Price/  (4 files)
      … 4 files under this directory
    Progress/  (4 files)
      … 4 files under this directory
    PullToRefresh/  (3 files)
      … 3 files under this directory
    QuickReplies/  (7 files)
      … 7 files under this directory
    Quote/  (3 files)
      … 3 files under this directory
    Radio/  (7 files)
      … 7 files under this directory
    RateActions/  (4 files)
      … 4 files under this directory
    Recorder/  (3 files)
      … 3 files under this directory
    RedPacket/  (3 files)
      … 3 files under this directory
    Ribbon/  (3 files)
      … 3 files under this directory
    RichText/  (5 files)
      … 5 files under this directory
    ScrollGrid/  (3 files)
      … 3 files under this directory
    ScrollView/  (6 files)
      … 6 files under this directory
    Search/  (3 files)
      … 3 files under this directory
    Select/  (3 files)
      … 3 files under this directory
    SendConfirm/  (4 files)
      … 4 files under this directory
    Skeleton/  (3 files)
      … 3 files under this directory
    Stepper/  (7 files)
      … 7 files under this directory
    Tabs/  (7 files)
      … 7 files under this directory
    Tag/  (4 files)
      … 4 files under this directory
    Text/  (4 files)
      … 4 files under this directory
    Think/  (3 files)
      … 3 files under this directory
    Time/  (6 files)
      … 6 files under this directory
    Tips/  (3 files)
      … 3 files under this directory
    Toast/  (6 files)
      … 6 files under this directory
    Toolbar/  (6 files)
      … 6 files under this directory
    Tooltip/  (1 files)
      … 1 files under this directory
    Tree/  (4 files)
      … 4 files under this directory
    Typing/  (6 files)
      … 6 files under this directory
    TypingBubble/  (2 files)
      … 2 files under this directory
    Video/  (4 files)
      … 4 files under this directory
    VisuallyHidden/  (5 files)
      … 5 files under this directory
    VoiceInput/  (3 files)
      … 3 files under this directory
  hooks/  (16 files)
    __test__/  (3 files)
      … 3 files under this directory
    useClickOutside.ts
    useColorScheme.ts
    useCountdown.ts
    useForwardRef.ts
    useIsomorphicLayoutEffect.ts
    useLatest.ts
    useMessages.ts
    useMount.ts
    useNextId.ts
    useQuickReplies.ts
    useTitleTyping.ts
    useTypewriter.ts
    useWindowResize.ts
  styles/  (8 files)
    animation.less
    dark.less
    font-face.less
    index.less
    root.less
    scale.less
    utils.less
    var.less
  utils/  (24 files)
    __tests__/  (5 files)
      … 5 files under this directory
    canUse.ts
    countLines.ts
    date.ts
    formatTime.ts
    getExtName.ts
    getFps.ts
    getRandomInt.ts
    getToBottom.ts
    importScript.ts
    index.ts
    lazyComponent.tsx
    mountComponent.ts
    parseDataTransfer.ts
    prettyBytes.ts
    smoothScroll.ts
    style.ts
    throttle.ts
    toggleClass.ts
    ua.ts
  global.d.ts
  index.ts
.eslintignore
.eslintrc.js
.gitignore
.prettierrc
CHANGELOG.md
LICENSE
README.md
README.zh-CN.md
babel.config.js
commitlint.config.js
jest.config.js
jest.setup.ts
package.json
postcss.config.js
rollup.config.js
tsconfig.build.json
tsconfig.eslint.json
tsconfig.json
```

## Entry points

- [demo/src/components/index.ts](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/demo/src/components/index.ts)
- [demo/src/demo/index.ts](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/demo/src/demo/index.ts)
- [demo/src/main.tsx](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/demo/src/main.tsx)
- [demo/src/utils/index.ts](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/demo/src/utils/index.ts)
- [src/components/Avatar/index.tsx](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/src/components/Avatar/index.tsx)
- [src/components/BackBottom/index.tsx](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/src/components/BackBottom/index.tsx)
- [src/components/Backdrop/index.tsx](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/src/components/Backdrop/index.tsx)
- [src/components/Bubble/index.tsx](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/src/components/Bubble/index.tsx)
- [src/components/Button/index.tsx](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/src/components/Button/index.tsx)
- [src/components/Card/index.ts](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/src/components/Card/index.ts)
- [src/components/Carousel/index.tsx](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/src/components/Carousel/index.tsx)
- [src/components/Chat/index.tsx](https://github.com/alibaba/ChatUI/blob/06c3126ad25a0735c9b48f40582075371ad04cf3/src/components/Chat/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 207 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 78 file(s) under demo package (observed from repository paths and static analysis). |
| global.d.ts package | library | Observed | Groups 1 file(s) under global.d.ts package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 16 file(s) under hooks package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 24 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `demo/package.json` (manifest)
- `demo/tsconfig.app.json` (config)
- `demo/tsconfig.json` (config)
- `demo/tsconfig.node.json` (config)
- `package.json` (manifest)
- `tsconfig.build.json` (config)
- `tsconfig.eslint.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 403 analysed file(s)
- `demo` — 85 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `06c3126ad25a0735c9b48f40582075371ad04cf3` is the revision these paths and observations refer to.
