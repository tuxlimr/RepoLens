# Project structure: dcloudio/mui

**Analysed commit:** `e216655901e51ca23112a65700e8f76d4fe008bc`

**Commit reference:** [e216655901e51ca23112a65700e8f76d4fe008bc](https://github.com/dcloudio/mui/commit/e216655901e51ca23112a65700e8f76d4fe008bc)

**Tree at this commit:** [dcloudio/mui@e216655901e5](https://github.com/dcloudio/mui/tree/e216655901e51ca23112a65700e8f76d4fe008bc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dcloudio/mui |
| Description | 最接近原生APP体验的高性能框架 |
| Stars | 13462 |
| Forks | 6447 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e216655901e51ca23112a65700e8f76d4fe008bc` |
| Retrieved at | 2026-11-14T19:11:56.536961+00:00 |
| Files in this snapshot | 273 |

## Directory tree

```text
examples/  (161 files)
  hello-mui/  (130 files)
    css/  (10 files)
      … 10 files under this directory
    examples/  (93 files)
      … 93 files under this directory
    js/  (23 files)
      … 23 files under this directory
    .project
    index-menu.html
    index.html
    manifest.json
  login/  (21 files)
    css/  (2 files)
      … 2 files under this directory
    js/  (6 files)
      … 6 files under this directory
    libs/  (4 files)
      … 4 files under this directory
    .project
    README.md
    forget_password.html
    login.html
    main.html
    manifest.json
    reg.html
    setting.html
    unlock.html
  nativeTab/  (10 files)
    css/  (1 files)
      … 1 files under this directory
    html/  (3 files)
      … 3 files under this directory
    js/  (1 files)
      … 1 files under this directory
    unpackage/  (2 files)
      … 2 files under this directory
    README.md
    index.html
    manifest.json
grunt/  (1 files)
  mui-namespace-generator.js
js/  (57 files)
  actions.js
  ajax.plugin.js
  input.plugin.js
  modals.js
  mui.active.js
  mui.ajax.5+.js
  mui.ajax.js
  mui.animation.js
  mui.animationframe.js
  mui.back.5+.js
  mui.back.js
  mui.button.js
  mui.class.js
  mui.class.scroll.js
  mui.class.scroll.pullrefresh.js
  mui.class.scroll.slider.js
  mui.detect.5+.js
  mui.detect.js
  mui.dialog.alert.js
  mui.dialog.confirm.js
  mui.dialog.prompt.js
  mui.dialog.toast.js
  mui.event.js
  mui.fixed.animation.js
  … 33 more files
plugin/  (9 files)
  picker/  (8 files)
    css/  (3 files)
      … 3 files under this directory
    js/  (3 files)
      … 3 files under this directory
    gulpfile.js
    package.json
  share/  (1 files)
    plusShare.js
sass/  (35 files)
  badges.scss
  bars.scss
  base.scss
  buttons.scss
  cards.scss
  forms.scss
  fullscreen.scss
  grid.scss
  hack.scss
  icon.scss
  iframe.scss
  iscroll.scss
  loadings.scss
  mixins.scss
  modals.scss
  mui.scss
  normalize.scss
  number.scss
  off-canvas.scss
  os.scss
  pagination.scss
  popovers.scss
  popup.scss
  progressbar.scss
  … 11 more files
template/  (4 files)
  feedback/  (4 files)
    css/  (1 files)
      … 1 files under this directory
    js/  (1 files)
      … 1 files under this directory
    feedback.html
    readme.md
.gitignore
Gruntfile.js
LICENSE
README.md
mui_snippets.rb
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| grunt package | library | Observed | Groups 1 file(s) under grunt package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 57 file(s) under js package (observed from repository paths and static analysis). |
| plugin package | library | Observed | Groups 5 file(s) under plugin package (observed from repository paths and static analysis). |
| template package | library | Observed | Groups 1 file(s) under template package (observed from repository paths and static analysis). |

## Important files

- `examples/hello-mui/manifest.json` (config)
- `examples/login/manifest.json` (config)
- `examples/nativeTab/manifest.json` (config)
- `package.json` (manifest)
- `plugin/picker/package.json` (manifest)

## Top-level layout

- `examples` — 161 analysed file(s)
- `js` — 57 analysed file(s)
- `sass` — 35 analysed file(s)
- `plugin` — 9 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `template` — 4 analysed file(s)
- `grunt` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (4 x generated/minified file excluded; 5 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e216655901e51ca23112a65700e8f76d4fe008bc` is the revision these paths and observations refer to.
