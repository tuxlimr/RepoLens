# Project structure: SortableJS/Sortable

**Analysed commit:** `48b626bbc61afbb0f179730c1dd3cca3dcc8b788`

**Commit reference:** [48b626bbc61afbb0f179730c1dd3cca3dcc8b788](https://github.com/SortableJS/Sortable/commit/48b626bbc61afbb0f179730c1dd3cca3dcc8b788)

**Tree at this commit:** [SortableJS/Sortable@48b626bbc61a](https://github.com/SortableJS/Sortable/tree/48b626bbc61afbb0f179730c1dd3cca3dcc8b788)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | SortableJS/Sortable |
| Description | Reorderable drag-and-drop lists for modern browsers and touch devices. No jQuery or framework required. |
| Stars | 31212 |
| Forks | 3714 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `48b626bbc61afbb0f179730c1dd3cca3dcc8b788` |
| Retrieved at | 2026-11-14T19:10:46.281798+00:00 |
| Files in this snapshot | 65 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (3 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    custom-template.md
    feature-request.md
entry/  (3 files)
  entry-complete.js
  entry-core.js
  entry-defaults.js
modular/  (3 files)
  sortable.complete.esm.js
  sortable.core.esm.js
  sortable.esm.js
plugins/  (13 files)
  AutoScroll/  (3 files)
    AutoScroll.js
    README.md
    index.js
  MultiDrag/  (3 files)
    MultiDrag.js
    README.md
    index.js
  OnSpill/  (3 files)
    OnSpill.js
    README.md
    index.js
  Swap/  (3 files)
    README.md
    Swap.js
    index.js
  README.md
scripts/  (7 files)
  banner.js
  build.js
  esm-build.js
  minify.js
  test-compat.js
  test.js
  umd-build.js
src/  (6 files)
  Animation.js
  BrowserInfo.js
  EventDispatcher.js
  PluginManager.js
  Sortable.js
  utils.js
st/  (8 files)
  iframe/  (2 files)
    frame.html
    index.html
  prettify/  (3 files)
    prettify.css
    prettify.js
    run_prettify.js
  app.js
  saucelabs.svg
  theme.css
tests/  (9 files)
  Sortable.compat.test.js
  Sortable.test.js
  dual-list.html
  empty-list.html
  filter.html
  handles.html
  nested.html
  single-list.html
  style.css
.editorconfig
.gitignore
.jshintrc
.testcaferc.json
CONTRIBUTING.md
LICENSE
README.md
Sortable.js
babel.config.js
bower.json
index.html
package.json
```

## Entry points

- [plugins/AutoScroll/index.js](https://github.com/SortableJS/Sortable/blob/48b626bbc61afbb0f179730c1dd3cca3dcc8b788/plugins/AutoScroll/index.js)
- [plugins/MultiDrag/index.js](https://github.com/SortableJS/Sortable/blob/48b626bbc61afbb0f179730c1dd3cca3dcc8b788/plugins/MultiDrag/index.js)
- [plugins/OnSpill/index.js](https://github.com/SortableJS/Sortable/blob/48b626bbc61afbb0f179730c1dd3cca3dcc8b788/plugins/OnSpill/index.js)
- [plugins/Swap/index.js](https://github.com/SortableJS/Sortable/blob/48b626bbc61afbb0f179730c1dd3cca3dcc8b788/plugins/Swap/index.js)
- [st/app.js](https://github.com/SortableJS/Sortable/blob/48b626bbc61afbb0f179730c1dd3cca3dcc8b788/st/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Animation.js package | library | Observed | Groups 1 file(s) under animation.js package (observed from repository paths and static analysis). |
| BrowserInfo.js package | library | Observed | Groups 1 file(s) under browserinfo.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| entry package | library | Observed | Groups 3 file(s) under entry package (observed from repository paths and static analysis). |
| EventDispatcher.js package | library | Observed | Groups 1 file(s) under eventdispatcher.js package (observed from repository paths and static analysis). |
| modular package | library | Observed | Groups 3 file(s) under modular package (observed from repository paths and static analysis). |
| PluginManager.js package | library | Observed | Groups 1 file(s) under pluginmanager.js package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 8 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). |
| Sortable.js package | library | Observed | Groups 1 file(s) under sortable.js package (observed from repository paths and static analysis). |
| st package | library | Observed | Groups 3 file(s) under st package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.editorconfig` (config)
- `.testcaferc.json` (config)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `plugins` — 13 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `tests` — 9 analysed file(s)
- `st` — 8 analysed file(s)
- `scripts` — 7 analysed file(s)
- `src` — 6 analysed file(s)
- `.github` — 3 analysed file(s)
- `entry` — 3 analysed file(s)
- `modular` — 3 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `48b626bbc61afbb0f179730c1dd3cca3dcc8b788` is the revision these paths and observations refer to.
