# Project structure: qishibo/AnotherRedisDesktopManager

**Analysed commit:** `c149855106628babcdfb7675a8e7ba9434d2492a`

**Commit reference:** [c149855106628babcdfb7675a8e7ba9434d2492a](https://github.com/qishibo/AnotherRedisDesktopManager/commit/c149855106628babcdfb7675a8e7ba9434d2492a)

**Tree at this commit:** [qishibo/AnotherRedisDesktopManager@c14985510662](https://github.com/qishibo/AnotherRedisDesktopManager/tree/c149855106628babcdfb7675a8e7ba9434d2492a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | qishibo/AnotherRedisDesktopManager |
| Description | 🚀🚀🚀A faster, better and more stable Redis desktop manager [GUI client], compatible with Linux, Windows, Mac. |
| Stars | 34860 |
| Forks | 2718 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c149855106628babcdfb7675a8e7ba9434d2492a` |
| Retrieved at | 2026-11-14T19:10:43.560486+00:00 |
| Files in this snapshot | 117 |

## Directory tree

```text
.github/  (10 files)
  workflows/  (8 files)
    build_appx.yaml
    build_linux.yml
    build_mac.yml
    build_snap.yml
    build_windows.yml
    codeql-analysis.yml.bak
    gen_sponsors.yaml
    publish_winget.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
config/  (3 files)
  dev.env.js
  index.js
  prod.env.js
pack/  (6 files)
  electron/  (5 files)
    electron-main.js
    font-manager.js
    package.json
    update.js
    win-state.js
  scripts/  (1 files)
    notarize.js
src/  (81 files)
  components/  (56 files)
    contents/  (10 files)
      … 10 files under this directory
    viewers/  (15 files)
      … 15 files under this directory
    CliContent.vue
    CliTab.vue
    CommandLog.vue
    ConnectionMenu.vue
    ConnectionWrapper.vue
    Connections.vue
    CustomFormatter.vue
    DeleteBatch.vue
    FileInput.vue
    FormatViewer.vue
    HotKeys.vue
    InputBinary.vue
    InputPassword.vue
    JsonEditor.vue
    KeyDetail.vue
    KeyHeader.vue
    KeyList.vue
    KeyListNormal.vue
    KeyListVirtualTree.vue
    LanguageSelector.vue
    MemoryAnalysis.vue
    NewConnectionDialog.vue
    OperateItem.vue
    PaginationTable.vue
    … 7 more files
  i18n/  (14 files)
    langs/  (13 files)
      … 13 files under this directory
    i18n.js
  router/  (1 files)
    index.js
  App.vue
  Aside.vue
  addon.js
  bus.js
  commands.js
  main.js
  redisClient.js
  shortcut.js
  storage.js
  util.js
static/  (2 files)
  theme/  (1 files)
    light/  (1 files)
      … 1 files under this directory
  .gitkeep
.editorconfig
.eslintrc.json
.gitattributes
.gitignore
.jshintrc
.postcssrc.js
LICENSE
PRIVACY.md
README.md
README.zh-CN.md
SECURITY.md
babel.config.json
element-variables.scss
index.html
package.json
```

## Entry points

- [pack/electron/electron-main.js](https://github.com/qishibo/AnotherRedisDesktopManager/blob/c149855106628babcdfb7675a8e7ba9434d2492a/pack/electron/electron-main.js)
- [config/index.js](https://github.com/qishibo/AnotherRedisDesktopManager/blob/c149855106628babcdfb7675a8e7ba9434d2492a/config/index.js)
- [src/main.js](https://github.com/qishibo/AnotherRedisDesktopManager/blob/c149855106628babcdfb7675a8e7ba9434d2492a/src/main.js)
- [src/router/index.js](https://github.com/qishibo/AnotherRedisDesktopManager/blob/c149855106628babcdfb7675a8e7ba9434d2492a/src/router/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| addon.js package | library | Observed | Groups 1 file(s) under addon.js package (observed from repository paths and static analysis). |
| App.vue package | library | Observed | Groups 1 file(s) under app.vue package (observed from repository paths and static analysis). |
| Aside.vue package | library | Observed | Groups 1 file(s) under aside.vue package (observed from repository paths and static analysis). |
| bus.js package | library | Observed | Groups 1 file(s) under bus.js package (observed from repository paths and static analysis). |
| commands.js package | library | Observed | Groups 1 file(s) under commands.js package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 56 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| i18n package | library | Observed | Groups 14 file(s) under i18n package (observed from repository paths and static analysis). |
| main.js package | library | Observed | Groups 1 file(s) under main.js package (observed from repository paths and static analysis). |
| pack package | library | Observed | Groups 5 file(s) under pack package (observed from repository paths and static analysis). |
| redisClient.js package | library | Observed | Groups 1 file(s) under redisclient.js package (observed from repository paths and static analysis). |
| router package | library | Observed | Groups 1 file(s) under router package (observed from repository paths and static analysis). |
| shortcut.js package | library | Observed | Groups 1 file(s) under shortcut.js package (observed from repository paths and static analysis). |
| storage.js package | library | Observed | Groups 1 file(s) under storage.js package (observed from repository paths and static analysis). |
| util.js package | library | Observed | Groups 1 file(s) under util.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/build_appx.yaml` (ci)
- `.github/workflows/build_linux.yml` (ci)
- `.github/workflows/build_mac.yml` (ci)
- `.github/workflows/build_snap.yml` (ci)
- `.github/workflows/build_windows.yml` (ci)
- `.github/workflows/codeql-analysis.yml.bak` (ci)
- `.github/workflows/gen_sponsors.yaml` (ci)
- `.github/workflows/publish_winget.yml` (ci)
- `babel.config.json` (config)
- `pack/electron/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `src` — 81 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 10 analysed file(s)
- `pack` — 6 analysed file(s)
- `config` — 3 analysed file(s)
- `static` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (7 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c149855106628babcdfb7675a8e7ba9434d2492a` is the revision these paths and observations refer to.
