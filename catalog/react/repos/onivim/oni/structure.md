# Project structure: onivim/oni

**Analysed commit:** `17ceaa45311964a5509f5f4db8a330429d4ac0d7`

**Commit reference:** [17ceaa45311964a5509f5f4db8a330429d4ac0d7](https://github.com/onivim/oni/commit/17ceaa45311964a5509f5f4db8a330429d4ac0d7)

**Tree at this commit:** [onivim/oni@17ceaa453119](https://github.com/onivim/oni/tree/17ceaa45311964a5509f5f4db8a330429d4ac0d7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | onivim/oni |
| Description | Oni: Modern Modal Editing - powered by Neovim |
| Stars | 11232 |
| Forks | 297 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `17ceaa45311964a5509f5f4db8a330429d4ac0d7` |
| Retrieved at | 2026-11-14T19:13:25.953583+00:00 |
| Files in this snapshot | 789 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  config.yml
.oni/  (2 files)
  templates/  (1 files)
    UnitTestTemplate.ts.template
  config.js
.vscode/  (1 files)
  launch.json
@types/  (2 files)
  color-normalize/  (1 files)
    index.d.ts
  font-manager/  (1 files)
    index.d.ts
browser/  (486 files)
  src/  (415 files)
    Editor/  (35 files)
      … 35 files under this directory
    Input/  (8 files)
      … 8 files under this directory
    Plugins/  (15 files)
      … 15 files under this directory
    Redux/  (4 files)
      … 4 files under this directory
    Renderer/  (20 files)
      … 20 files under this directory
    Services/  (235 files)
      … 235 files under this directory
    UI/  (64 files)
      … 64 files under this directory
    neovim/  (18 files)
      … 18 files under this directory
    App.ts
    CSS.ts
    Constants.ts
    Font.ts
    Grid.ts
    Performance.ts
    PeriodicJobs.ts
    PersistentStore.ts
    Platform.ts
    Utility.ts
    index.tsx
    neovim-client.d.ts
    overlay.less
    startEditors.ts
    sudo-prompt.d.ts
    units-css.d.ts
  test/  (64 files)
    Editor/  (3 files)
      … 3 files under this directory
    Input/  (3 files)
      … 3 files under this directory
    Mocks/  (7 files)
      … 7 files under this directory
    Plugins/  (1 files)
      … 1 files under this directory
    Renderer/  (1 files)
      … 1 files under this directory
    Services/  (39 files)
      … 39 files under this directory
    Tabs/  (1 files)
      … 1 files under this directory
    neovim/  (4 files)
      … 4 files under this directory
    AppTests.ts
    GridTests.ts
    MarkdownTests.ts
    TestHelpers.ts
    UtilityTests.ts
  testCoverageReporter.js
  testHelpers.js
  tsconfig.json
  tsconfig.test.json
  webpack.debug.config.js
  webpack.development.config.js
  webpack.production.config.js
cli/  (6 files)
  linux/  (1 files)
    oni.sh
  mac/  (1 files)
    oni.sh
  src/  (2 files)
    cli.ts
    cli_args.ts
  win/  (1 files)
    oni.cmd
  tsconfig.json
configuration/  (1 files)
  config.default.js
extensions/  (78 files)
  clojure/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  csharp/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  css/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  elixir/  (3 files)
    syntaxes/  (3 files)
      … 3 files under this directory
  go/  (2 files)
    syntaxes/  (1 files)
      … 1 files under this directory
    README.md
  html/  (2 files)
    snippets/  (1 files)
      … 1 files under this directory
    package.json
  images/  (1 files)
    package.json
  java/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  javascript/  (4 files)
    snippets/  (1 files)
      … 1 files under this directory
    syntaxes/  (2 files)
      … 2 files under this directory
    package.json
  less/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  lua/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  markdown/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  objective-c/  (2 files)
    syntaxes/  (2 files)
      … 2 files under this directory
  oni-plugin-markdown-preview/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    package.json
    tsconfig.json
  oni-plugin-prettier/  (4 files)
    .eslintrc.json
    index.js
    package.json
    requirePackage.js
  oni-plugin-quickopen/  (6 files)
    src/  (4 files)
      … 4 files under this directory
    package.json
    tsconfig.json
  php/  (2 files)
    syntaxes/  (2 files)
      … 2 files under this directory
  python/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  reason/  (4 files)
    snippets/  (1 files)
      … 1 files under this directory
    syntaxes/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  ruby/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  rust/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  scss/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  shell/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  swift/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  theme-dracula/  (3 files)
    colors/  (2 files)
      … 2 files under this directory
    package.json
  theme-gruvbox/  (4 files)
    colors/  (3 files)
      … 3 files under this directory
    package.json
  theme-hybrid/  (4 files)
    colors/  (3 files)
      … 3 files under this directory
    package.json
  theme-icons-seti/  (4 files)
    icons/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    thirdpartynotices.txt
  theme-nord/  (4 files)
    colors/  (2 files)
      … 2 files under this directory
    README.md
    package.json
  theme-onedark/  (3 files)
    colors/  (2 files)
      … 2 files under this directory
    package.json
  theme-solarized/  (4 files)
    colors/  (3 files)
      … 3 files under this directory
    package.json
  typescript/  (4 files)
    snippets/  (1 files)
      … 1 files under this directory
    syntaxes/  (2 files)
      … 2 files under this directory
    package.json
  vue/  (1 files)
    syntaxes/  (1 files)
      … 1 files under this directory
  README.md
font-awesome/  (1 files)
  css/  (1 files)
    font-awesome.css
images/  (1 files)
  oni-icon-no-border.svg
main/  (9 files)
  src/  (6 files)
    Log.ts
    ProcessLifecycle.ts
    WindowManager.ts
    installDevTools.ts
    main.ts
    menu.ts
  test/  (1 files)
    WindowManagerTests.ts
  tsconfig.json
  tsconfig.test.json
scripts/  (2 files)
  dev_webpack_loader.js
  webm2gif.sh
test/  (67 files)
  ci/  (54 files)
    Api.Buffer.AddLayer.tsx
    Api.Overlays.AddRemoveTest.tsx
    Assert.ts
    AutoClosingPairsTest.ts
    AutoCompletionTest-CSS.ts
    AutoCompletionTest-HTML.ts
    AutoCompletionTest-Reason.ts
    AutoCompletionTest-TypeScript.ts
    Browser.LocationTest.ts
    ColorHighlight.BufferLayerTest.ts
    Common.ts
    Configuration.JavaScriptEditorTest.ts
    Configuration.TypeScriptEditor.CompletionTest.ts
    Configuration.TypeScriptEditor.NewConfigurationTest.ts
    Editor.BufferModifiedState.ts
    Editor.BuffersCursorTest.ts
    Editor.CloseTabWithTabModesTabsTest.ts
    Editor.ExternalCommandLineTest.ts
    Editor.NextPreviousErrorTest.ts
    Editor.OpenFile.PathWithSpacesTest.ts
    Editor.ScrollEventTest.ts
    Editor.TabModifiedState.ts
    Explorer.LocateBufferTest.ts
    IndentGuide.BufferLayerTest.tsx
    … 30 more files
  collateral/  (1 files)
    1799_test.csv
  common/  (4 files)
    Oni.ts
    ensureProcessNotRunning.ts
    index.ts
    runInProcTest.ts
  demo/  (3 files)
    DemoCommon.ts
    HeroDemo.ts
    HeroScreenshot.ts
  setup/  (1 files)
    WindowsInstallerTests.ts
  CiTests.ts
  Demo.ts
  Manual.md
  tsconfig.json
ui-tests/  (69 files)
  VersionControl/  (11 files)
    __snapshots__/  (3 files)
      … 3 files under this directory
    Help.test.tsx
    VersionControlCommits.test.tsx
    VersionControlComponents.test.tsx
    VersionControlManager.test.tsx
    VersionControlPane.test.tsx
    VersionControlSectionTitle.test.tsx
    VersionControlStore.test.ts
    VersionControlView.test.tsx
  __snapshots__/  (13 files)
    BrowserView.test.tsx.snap
    BufferScrollBar.test.tsx.snap
    CommandLine.test.tsx.snap
    ErrorInfo.test.tsx.snap
    ExternalMenus.test.tsx.snap
    NodeView.test.tsx.snap
    NotificationView.test.tsx.snap
    QuickInfo.test.tsx.snap
    Tabs.test.tsx.snap
    Text.test.tsx.snap
    WelcomeCommandsView.test.tsx.snap
    WelcomeView.test.tsx.snap
    WindowTitleView.test.tsx.snap
  mocks/  (15 files)
    CommandManager.ts
    Configuration.ts
    EditorManager.ts
    MenuManager.ts
    Notifications.ts
    Oni.ts
    PersistentSettings.ts
    SharedNeovimInstance.ts
    Sidebar.ts
    Statusbar.ts
    UserConfiguration.ts
    Utility.ts
    Workspace.ts
    electronMock.ts
    keyboardLayout.ts
  BrowserView.test.tsx
  BufferManager.test.ts
  BufferScrollBar.test.tsx
  CommandLine.test.tsx
  ContextMenuComponent.test.tsx
  ErrorInfo.test.tsx
  ExplorerSplit.test.tsx
  ExplorerView.test.tsx
  ExternalMenus.test.tsx
  HighlightText.test.tsx
  NeovimBufferLayersView.test.tsx
  NodeView.test.tsx
  NotificationView.test.tsx
  QuickInfo.test.tsx
  SessionManager.test.tsx
  Sessions.test.tsx
  SidebarStore.test.ts
  Tabs.test.tsx
  Text.test.tsx
  TokenScorer.test.ts
  TokenThemeProvider.test.tsx
  VersionControlBlameLayer.test.tsx
  VimNavigator.test.tsx
  WelcomeCommandsView.test.tsx
  … 6 more files
vim/  (36 files)
  core/  (34 files)
    colors/  (1 files)
      … 1 files under this directory
    oni-core-interop/  (2 files)
      … 2 files under this directory
    oni-core-statusbar/  (2 files)
      … 2 files under this directory
    oni-plugin-buffers/  (3 files)
      … 3 files under this directory
    oni-plugin-git/  (4 files)
      … 4 files under this directory
    oni-plugin-reasonml/  (3 files)
      … 3 files under this directory
    oni-plugin-typescript/  (19 files)
      … 19 files under this directory
  default/  (1 files)
    bundle/  (1 files)
      … 1 files under this directory
  noop.vim
webview_preload/  (2 files)
  src/  (1 files)
    index.ts
  tsconfig.json
.editorconfig
.gitattributes
.gitignore
.gitmodules
.npmignore
.nvmrc
.prettierignore
.prettierrc
.travis.yml
.yarnrc
ACCOUNTING.md
BACKERS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
appveyor.yml
codecov.yml
index.dev.html
index.html
jest.config.js
package.json
preload.js
tslint.json
```

## Entry points

- [extensions/oni-plugin-prettier/index.js](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/extensions/oni-plugin-prettier/index.js)
- [vim/core/oni-core-statusbar/index.js](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/vim/core/oni-core-statusbar/index.js)
- [vim/core/oni-plugin-buffers/index.js](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/vim/core/oni-plugin-buffers/index.js)
- [browser/src/App.ts](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/browser/src/App.ts)
- [browser/src/Redux/index.ts](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/browser/src/Redux/index.ts)
- [browser/src/Renderer/index.ts](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/browser/src/Renderer/index.ts)
- [browser/src/index.tsx](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/browser/src/index.tsx)
- [browser/src/neovim/index.ts](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/browser/src/neovim/index.ts)
- [extensions/oni-plugin-markdown-preview/src/index.tsx](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/extensions/oni-plugin-markdown-preview/src/index.tsx)
- [extensions/oni-plugin-quickopen/src/index.tsx](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/extensions/oni-plugin-quickopen/src/index.tsx)
- [main/src/main.ts](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/main/src/main.ts)
- [webview_preload/src/index.ts](https://github.com/onivim/oni/blob/17ceaa45311964a5509f5f4db8a330429d4ac0d7/webview_preload/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 8 file(s) under api layer (observed from repository paths and static analysis). |
| browser package | library | Observed | Groups 173 file(s) under browser package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 4 file(s) under cli package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 78 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| configuration package | library | Observed | Groups 1 file(s) under configuration package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| extensions package | library | Observed | Groups 7 file(s) under extensions package (observed from repository paths and static analysis). |
| main package | library | Observed | Groups 6 file(s) under main package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 253 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 132 file(s) under tests (observed from repository paths and static analysis). |
| @types package | library | Observed | Groups 2 file(s) under @types package (observed from repository paths and static analysis). |
| ui-tests package | library | Observed | Groups 52 file(s) under ui-tests package (observed from repository paths and static analysis). |
| webview_preload package | library | Observed | Groups 1 file(s) under webview_preload package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/config.yml` (config)
- `.travis.yml` (ci)
- `.vscode/launch.json` (config)
- `appveyor.yml` (config)
- `browser/tsconfig.json` (config)
- `browser/tsconfig.test.json` (config)
- `cli/tsconfig.json` (config)
- `codecov.yml` (config)
- `extensions/clojure/syntaxes/clojure.tmLanguage.json` (config)
- `extensions/csharp/syntaxes/csharp.tmLanguage.json` (config)
- `extensions/css/syntaxes/css.tmLanguage.json` (config)
- `extensions/elixir/syntaxes/eex.tmLanguage.json` (config)
- `extensions/elixir/syntaxes/elixir.tmLanguage.json` (config)
- `extensions/elixir/syntaxes/html(eex).tmLanguage.json` (config)
- `extensions/go/syntaxes/go.json` (config)
- `extensions/html/package.json` (manifest)
- `extensions/html/snippets/html.json` (config)
- `extensions/images/package.json` (manifest)
- `extensions/java/syntaxes/Java.tmLanguage.json` (config)
- `extensions/javascript/package.json` (manifest)
- `extensions/javascript/snippets/javascript.json` (config)
- `extensions/javascript/syntaxes/JavaScript.tmLanguage.json` (config)
- `extensions/javascript/syntaxes/JavaScriptReact.tmLanguage.json` (config)
- `extensions/less/syntaxes/less.tmLanguage.json` (config)
- `extensions/lua/syntaxes/lua.tmLanguage.json` (config)
- `extensions/markdown/syntaxes/markdown.tmLanguage.json` (config)
- `extensions/objective-c/syntaxes/objective-c++.tmLanguage.json` (config)
- `extensions/objective-c/syntaxes/objective-c.tmLanguage.json` (config)
- `extensions/oni-plugin-markdown-preview/package.json` (manifest)
- `extensions/oni-plugin-markdown-preview/tsconfig.json` (config)
- `extensions/oni-plugin-prettier/.eslintrc.json` (config)
- `extensions/oni-plugin-prettier/package.json` (manifest)
- `extensions/oni-plugin-quickopen/package.json` (manifest)
- `extensions/oni-plugin-quickopen/tsconfig.json` (config)
- `extensions/php/syntaxes/html.tmLanguage.json` (config)
- `extensions/php/syntaxes/php.tmLanguage.json` (config)
- `extensions/python/syntaxes/python.tmLanguage.json` (config)
- `extensions/reason/package.json` (manifest)
- `extensions/reason/snippets/reason.json` (config)
- `extensions/reason/syntaxes/reason.json` (config)
- `extensions/ruby/syntaxes/ruby.tmLanguage.json` (config)
- `extensions/rust/syntaxes/rust.tmLanguage.json` (config)
- `extensions/scss/syntaxes/scss.json` (config)
- `extensions/shell/syntaxes/shell.tmLanguage.json` (config)
- `extensions/swift/syntaxes/swift.tmLanguage.json` (config)
- `extensions/theme-dracula/colors/dracula.json` (config)
- `extensions/theme-dracula/package.json` (manifest)
- `extensions/theme-gruvbox/colors/gruvbox_dark.json` (config)
- `extensions/theme-gruvbox/colors/gruvbox_light.json` (config)
- `extensions/theme-gruvbox/package.json` (manifest)
- `extensions/theme-hybrid/colors/hybrid_dark.json` (config)
- `extensions/theme-hybrid/colors/hybrid_light.json` (config)
- `extensions/theme-hybrid/package.json` (manifest)
- `extensions/theme-icons-seti/icons/seti-icon-theme.json` (config)
- `extensions/theme-icons-seti/package.json` (manifest)
- `extensions/theme-nord/colors/nord.json` (config)
- `extensions/theme-nord/package.json` (manifest)
- `extensions/theme-onedark/colors/onedark.json` (config)
- `extensions/theme-onedark/package.json` (manifest)
- `extensions/theme-solarized/colors/solarized8_dark.json` (config)
- `extensions/theme-solarized/colors/solarized8_light.json` (config)
- `extensions/theme-solarized/package.json` (manifest)
- `extensions/typescript/package.json` (manifest)
- `extensions/typescript/snippets/typescript.json` (config)
- `extensions/typescript/syntaxes/TypeScript.tmLanguage.json` (config)
- `extensions/typescript/syntaxes/TypeScriptReact.tmLanguage.json` (config)
- `extensions/vue/syntaxes/vue.json` (config)
- `main/tsconfig.json` (config)
- `main/tsconfig.test.json` (config)
- `package.json` (manifest)
- `tslint.json` (config)
- `ui-tests/tsconfig.react.json` (config)
- `vim/core/oni-core-statusbar/package.json` (manifest)
- `vim/core/oni-plugin-buffers/jsconfig.json` (config)
- `vim/core/oni-plugin-buffers/package.json` (manifest)
- `vim/core/oni-plugin-git/package.json` (manifest)
- `vim/core/oni-plugin-git/tsconfig.json` (config)
- `vim/core/oni-plugin-typescript/package.json` (manifest)
- `vim/core/oni-plugin-typescript/tsconfig.json` (config)
- `vim/core/oni-plugin-typescript/tsconfig.test.json` (config)
- `webview_preload/tsconfig.json` (config)

## Top-level layout

- `browser` — 486 analysed file(s)
- `extensions` — 78 analysed file(s)
- `ui-tests` — 69 analysed file(s)
- `test` — 67 analysed file(s)
- `vim` — 36 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `main` — 9 analysed file(s)
- `cli` — 6 analysed file(s)
- `.github` — 2 analysed file(s)
- `.oni` — 2 analysed file(s)
- `@types` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `webview_preload` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `configuration` — 1 analysed file(s)
- `font-awesome` — 1 analysed file(s)
- `images` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 11 file(s) were skipped during inventory (1 x generated/minified file excluded; 10 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `17ceaa45311964a5509f5f4db8a330429d4ac0d7` is the revision these paths and observations refer to.
