# Project structure: Vanessa219/vditor

**Analysed commit:** `0732967e1bd16de7716399b6926bf75ad9bfc5d8`

**Commit reference:** [0732967e1bd16de7716399b6926bf75ad9bfc5d8](https://github.com/Vanessa219/vditor/commit/0732967e1bd16de7716399b6926bf75ad9bfc5d8)

**Tree at this commit:** [Vanessa219/vditor@0732967e1bd1](https://github.com/Vanessa219/vditor/tree/0732967e1bd16de7716399b6926bf75ad9bfc5d8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Vanessa219/vditor |
| Description | ♏  一款浏览器端的 Markdown 编辑器，支持所见即所得（富文本）、即时渲染（类似 Typora）和分屏预览模式。An In-browser Markdown editor, support WYSIWYG (Rich Text),  Instant Rendering (Typora-like) and Split View modes. |
| Stars | 11449 |
| Forks | 1091 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `0732967e1bd16de7716399b6926bf75ad9bfc5d8` |
| Retrieved at | 2026-11-14T19:13:26.114445+00:00 |
| Files in this snapshot | 251 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (1 files)
    publish.yml
  PULL_REQUEST_TEMPLATE.md
  SECURITY.md
__test__/  (33 files)
  ir/  (2 files)
    copyHeadingMarker.test.js
    toolbarToggle.test.js
  markdown/  (14 files)
    callout.test.js
    commonmark-0.29.ts
    getMarkdownNbsp.browser.test.js
    getMarkdownNbsp.test.ts
    headingIDRaw.test.js
    inlineMath.test.ts
    linkBase.test.js
    listSetextContinuation.test.js
    lute.test.ts
    mediaRender.browser.test.js
    mermaid.browser.test.js
    tableBreak.test.js
    wavedrom.browser.test.js
    wavedrom.test.js
  methods/  (1 files)
    index.spec.ts
  sv/  (1 files)
    textarea.test.js
  util/  (3 files)
    Options.test.ts
    launchBrowser.ts
    textareaPosition.spec.ts
  wysiwyg/  (7 files)
    androidCursor.test.js
    callout.test.js
    headingInList.test.js
    inlineMathRoundTrip.test.js
    mobileToolbar.test.js
    multilineListHotkey.test.js
    pasteTableCell.test.js
  blockquoteInList.test.js
  imageCaption.test.js
  listEnter.test.js
  toolbarButton.test.js
  uploadError.test.js
demo/  (14 files)
  markdown/  (4 files)
    cute-list.md
    entity.md
    ko_KR.md
    zh_CN.md
  comment.html
  comment.js
  icon.html
  index.html
  index.js
  jest-puppeteer.html
  jest-puppeteer.js
  render.html
  render.js
  static.html
src/  (181 files)
  assets/  (10 files)
    less/  (10 files)
      … 10 files under this directory
  css/  (4 files)
    content-theme/  (4 files)
      … 4 files under this directory
  images/  (1 files)
    img-loading.svg
  js/  (56 files)
    graphviz/  (1 files)
      … 1 files under this directory
    highlight.js/  (2 files)
      … 2 files under this directory
    i18n/  (12 files)
      … 12 files under this directory
    icons/  (2 files)
      … 2 files under this directory
    markmap/  (1 files)
      … 1 files under this directory
    mathjax/  (37 files)
      … 37 files under this directory
    wavedrom/  (1 files)
      … 1 files under this directory
  ts/  (108 files)
    devtools/  (1 files)
      … 1 files under this directory
    export/  (1 files)
      … 1 files under this directory
    hint/  (1 files)
      … 1 files under this directory
    ir/  (6 files)
      … 6 files under this directory
    markdown/  (24 files)
      … 24 files under this directory
    outline/  (1 files)
      … 1 files under this directory
    preview/  (2 files)
      … 2 files under this directory
    resize/  (1 files)
      … 1 files under this directory
    sv/  (3 files)
      … 3 files under this directory
    tip/  (1 files)
      … 1 files under this directory
    toolbar/  (28 files)
      … 28 files under this directory
    ui/  (5 files)
      … 5 files under this directory
    undo/  (1 files)
      … 1 files under this directory
    upload/  (3 files)
      … 3 files under this directory
    util/  (19 files)
      … 19 files under this directory
    wysiwyg/  (10 files)
      … 10 files under this directory
    constants.ts
  index.ts
  method.ts
types/  (1 files)
  index.d.ts
.editorconfig
.gitignore
.prettierrc
CHANGELOG.md
LICENSE
README.md
README_en_US.md
bower.json
eslint.config.mjs
jest.config.cjs
package.json
pnpm-workspace.yaml
tsconfig.json
tsconfig.test.json
webpack.config.js
webpack.start.js
```

## Entry points

- [demo/index.js](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/demo/index.js)
- [src/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/index.ts)
- [src/ts/devtools/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/ts/devtools/index.ts)
- [src/ts/export/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/ts/export/index.ts)
- [src/ts/hint/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/ts/hint/index.ts)
- [src/ts/ir/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/ts/ir/index.ts)
- [src/ts/outline/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/ts/outline/index.ts)
- [src/ts/preview/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/ts/preview/index.ts)
- [src/ts/resize/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/ts/resize/index.ts)
- [src/ts/sv/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/ts/sv/index.ts)
- [src/ts/tip/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/ts/tip/index.ts)
- [src/ts/toolbar/index.ts](https://github.com/Vanessa219/vditor/blob/0732967e1bd16de7716399b6926bf75ad9bfc5d8/src/ts/toolbar/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 4 file(s) under demo package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 52 file(s) under js package (observed from repository paths and static analysis). |
| method.ts package | library | Observed | Groups 1 file(s) under method.ts package (observed from repository paths and static analysis). |
| __test__ package | library | Observed | Groups 33 file(s) under __test__ package (observed from repository paths and static analysis). |
| ts package | library | Observed | Groups 108 file(s) under ts package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/publish.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `tsconfig.test.json` (config)

## Top-level layout

- `src` — 181 analysed file(s)
- `__test__` — 33 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `demo` — 14 analysed file(s)
- `.github` — 6 analysed file(s)
- `types` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 252 file(s) were skipped during inventory (251 x generated/minified file excluded; 1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0732967e1bd16de7716399b6926bf75ad9bfc5d8` is the revision these paths and observations refer to.
