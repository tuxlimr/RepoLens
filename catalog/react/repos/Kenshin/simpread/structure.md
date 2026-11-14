# Project structure: Kenshin/simpread

**Analysed commit:** `d6534a7d67ab606e0390ff7172360fac88af4422`

**Commit reference:** [d6534a7d67ab606e0390ff7172360fac88af4422](https://github.com/Kenshin/simpread/commit/d6534a7d67ab606e0390ff7172360fac88af4422)

**Tree at this commit:** [Kenshin/simpread@d6534a7d67ab](https://github.com/Kenshin/simpread/tree/d6534a7d67ab606e0390ff7172360fac88af4422)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Kenshin/simpread |
| Description | 简悦 ( SimpRead ) - 让你瞬间进入沉浸式阅读的扩展 |
| Stars | 8751 |
| Forks | 557 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d6534a7d67ab606e0390ff7172360fac88af4422` |
| Retrieved at | 2026-11-14T19:13:39.139357+00:00 |
| Files in this snapshot | 138 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yaml
    config.yml
    feature_request.yml
    new_site.yml
    yinxiang_code.yml
ext/  (3 files)
  background.js
  contentscripts.js
  manifest.json
src/  (123 files)
  _locales/  (3 files)
    en/  (1 files)
      … 1 files under this directory
    zh_CN/  (1 files)
      … 1 files under this directory
    zh_TW/  (1 files)
      … 1 files under this directory
  assets/  (18 files)
    css/  (17 files)
      … 17 files under this directory
    images/  (1 files)
      … 1 files under this directory
  focus/  (2 files)
    controlbar.jsx
    focus.js
  module/  (30 files)
    common/  (7 files)
      … 7 files under this directory
    about.jsx
    account.jsx
    actionbar.jsx
    authorize.jsx
    common.jsx
    enhancesite.jsx
    feedback.jsx
    focus.jsx
    guide.jsx
    keyboard.js
    labs.jsx
    notice.jsx
    pluginbar.jsx
    plugins.jsx
    read.jsx
    setting.jsx
    sharecard.jsx
    sitebar.jsx
    siteeditor.jsx
    sites.jsx
    unrdist.jsx
    urlscheme.jsx
    welcome.jsx
  options/  (10 files)
    corb.html
    corb.js
    custom.html
    custom.js
    notice.html
    notice.js
    options.html
    options.js
    sitemgr.html
    sitemgr.js
  read/  (5 files)
    controlbar.jsx
    progressbar.jsx
    read.jsx
    special.jsx
    toc.jsx
  service/  (19 files)
    browser.js
    config.js
    export.js
    highlight.js
    local.js
    menu.js
    message.js
    offline.js
    output.js
    permission.js
    runtime.js
    snapshot.js
    storage.js
    stylesheet.js
    theme.js
    tips.js
    util.js
    version.js
    watch.js
  vender/  (30 files)
    carousel/  (2 files)
      … 2 files under this directory
    mduikit/  (19 files)
      … 19 files under this directory
    notify/  (2 files)
      … 2 files under this directory
    turndown/  (2 files)
      … 2 files under this directory
    waves/  (1 files)
      … 1 files under this directory
    instapaper.js
    sha1.js
    webdav.js
    wiz.js
  background.js
  contentscripts.js
  ga.js
  help_tips.json
  manifest.json
  website_list.json
.gitignore
LICENSE
README.md
npmw.cmd
package.json
webpack.config.ext.js
webpack.config.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| background.js package | library | Observed | Groups 1 file(s) under background.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| contentscripts.js package | library | Observed | Groups 1 file(s) under contentscripts.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| ext package | library | Observed | Groups 2 file(s) under ext package (observed from repository paths and static analysis). |
| focus package | library | Observed | Groups 2 file(s) under focus package (observed from repository paths and static analysis). |
| ga.js package | library | Observed | Groups 1 file(s) under ga.js package (observed from repository paths and static analysis). |
| module package | library | Observed | Groups 30 file(s) under module package (observed from repository paths and static analysis). |
| options package | library | Observed | Groups 5 file(s) under options package (observed from repository paths and static analysis). |
| read package | library | Observed | Groups 5 file(s) under read package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 19 file(s) under service / domain layer (observed from repository paths and static analysis). |
| vender package | library | Observed | Groups 26 file(s) under vender package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/new_site.yml` (config)
- `.github/ISSUE_TEMPLATE/yinxiang_code.yml` (config)
- `ext/manifest.json` (config)
- `package.json` (manifest)
- `src/_locales/en/messages.json` (config)
- `src/_locales/zh_CN/messages.json` (config)
- `src/_locales/zh_TW/messages.json` (config)
- `src/help_tips.json` (config)
- `src/manifest.json` (config)
- `src/website_list.json` (config)

## Top-level layout

- `src` — 123 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 5 analysed file(s)
- `ext` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x generated/minified file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d6534a7d67ab606e0390ff7172360fac88af4422` is the revision these paths and observations refer to.
