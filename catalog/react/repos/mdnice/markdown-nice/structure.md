# Project structure: mdnice/markdown-nice

**Analysed commit:** `6525a5aba371209c2840593e8f537b4a69137a4b`

**Commit reference:** [6525a5aba371209c2840593e8f537b4a69137a4b](https://github.com/mdnice/markdown-nice/commit/6525a5aba371209c2840593e8f537b4a69137a4b)

**Tree at this commit:** [mdnice/markdown-nice@6525a5aba371](https://github.com/mdnice/markdown-nice/tree/6525a5aba371209c2840593e8f537b4a69137a4b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mdnice/markdown-nice |
| Description | 支持主题设计的 Markdown 编辑器，让排版变 Nice |
| Stars | 4679 |
| Forks | 725 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `6525a5aba371209c2840593e8f537b4a69137a4b` |
| Retrieved at | 2026-11-14T19:14:39.301637+00:00 |
| Files in this snapshot | 187 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
.storybook/  (2 files)
  .babelrc
  config.js
config/  (7 files)
  jest/  (2 files)
    cssTransform.js
    fileTransform.js
  env.js
  paths.js
  webpack.config.js
  webpack.config.lib.js
  webpackDevServer.config.js
public/  (3 files)
  favicon.svg
  index.html
  manifest.json
scripts/  (3 files)
  build.js
  start.js
  test.js
src/  (154 files)
  component/  (70 files)
    Dialog/  (9 files)
      … 9 files under this directory
    ImageHosting/  (4 files)
      … 4 files under this directory
    LocalHistory/  (4 files)
      … 4 files under this directory
    MenuLeft/  (43 files)
      … 43 files under this directory
    SearchBox/  (2 files)
      … 2 files under this directory
    Sidebar/  (8 files)
      … 8 files under this directory
  icon/  (20 files)
    Close.js
    Copy.js
    Down.js
    Environment.js
    FontCase.js
    GitHub.js
    Inbox.js
    Juejin.js
    Mobile.js
    More.js
    PC.js
    Rabbit.js
    Replace.js
    ReplaceAll.js
    Smile.js
    User.js
    Wechat.js
    Zhihu.js
    index.css
    index.js
  layout/  (10 files)
    Dialog.js
    EditorMenu.css
    EditorMenu.js
    Footer.css
    Footer.js
    Navbar.css
    Navbar.js
    Sidebar.css
    Sidebar.js
    StyleEditor.js
  store/  (8 files)
    content.js
    dialog.js
    footer.js
    imageHosting.js
    navbar.js
    title.js
    userInfo.js
    view.js
  template/  (17 files)
    code/  (6 files)
      … 6 files under this directory
    macCode/  (6 files)
      … 6 files under this directory
    markdown/  (2 files)
      … 2 files under this directory
    basic.js
    content.md
    index.js
  utils/  (20 files)
    appContext.js
    constant.js
    converter.js
    editorKeyEvents.js
    helper.js
    hotkey.js
    imageHosting.js
    langHighlight.js
    markdown-it-imageflow.js
    markdown-it-li.js
    markdown-it-linkfoot.js
    markdown-it-math.js
    markdown-it-multiquote.js
    markdown-it-removepre.js
    markdown-it-span.js
    markdown-it-table-container.js
    mdMirror.css
    pluginCenter.js
    sitdownConverter.js
    styleMirror.css
  App.css
  App.js
  App.test.js
  Lib.js
  index.css
  index.d.ts
  index.js
  logo.svg
  serviceWorker.js
stories/  (5 files)
  allImageHosting.js
  defaultImageHosting.js
  index.js
  noneImageHosting.js
  online.js
.eslintignore
.eslintrc
.gitignore
.npmignore
.prettierrc
CHANGELOG.md
LICENSE
README.md
main.js
package.json
watch.js
```

## Entry points

- [main.js](https://github.com/mdnice/markdown-nice/blob/6525a5aba371209c2840593e8f537b4a69137a4b/main.js)
- [src/App.js](https://github.com/mdnice/markdown-nice/blob/6525a5aba371209c2840593e8f537b4a69137a4b/src/App.js)
- [src/component/LocalHistory/index.js](https://github.com/mdnice/markdown-nice/blob/6525a5aba371209c2840593e8f537b4a69137a4b/src/component/LocalHistory/index.js)
- [src/component/SearchBox/index.js](https://github.com/mdnice/markdown-nice/blob/6525a5aba371209c2840593e8f537b4a69137a4b/src/component/SearchBox/index.js)
- [src/icon/index.js](https://github.com/mdnice/markdown-nice/blob/6525a5aba371209c2840593e8f537b4a69137a4b/src/icon/index.js)
- [src/index.js](https://github.com/mdnice/markdown-nice/blob/6525a5aba371209c2840593e8f537b4a69137a4b/src/index.js)
- [src/template/index.js](https://github.com/mdnice/markdown-nice/blob/6525a5aba371209c2840593e8f537b4a69137a4b/src/template/index.js)
- [stories/index.js](https://github.com/mdnice/markdown-nice/blob/6525a5aba371209c2840593e8f537b4a69137a4b/stories/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| App.test.js package | library | Observed | Groups 1 file(s) under app.test.js package (observed from repository paths and static analysis). |
| component package | library | Observed | Groups 59 file(s) under component package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| icon package | library | Observed | Groups 19 file(s) under icon package (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| layout package | library | Observed | Groups 6 file(s) under layout package (observed from repository paths and static analysis). |
| Lib.js package | library | Observed | Groups 1 file(s) under lib.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| serviceWorker.js package | library | Observed | Groups 1 file(s) under serviceworker.js package (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 8 file(s) under store package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 5 file(s) under stories package (observed from repository paths and static analysis). |
| template package | library | Observed | Groups 16 file(s) under template package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 18 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `package.json` (manifest)
- `public/manifest.json` (config)

## Top-level layout

- `src` — 154 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `config` — 7 analysed file(s)
- `stories` — 5 analysed file(s)
- `public` — 3 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `.storybook` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6525a5aba371209c2840593e8f537b4a69137a4b` is the revision these paths and observations refer to.
