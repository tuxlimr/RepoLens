# Project structure: d2-projects/d2-admin

**Analysed commit:** `35d7aa1fc1fc8a9f35c707993fc7370393a41a48`

**Commit reference:** [35d7aa1fc1fc8a9f35c707993fc7370393a41a48](https://github.com/d2-projects/d2-admin/commit/35d7aa1fc1fc8a9f35c707993fc7370393a41a48)

**Tree at this commit:** [d2-projects/d2-admin@35d7aa1fc1fc](https://github.com/d2-projects/d2-admin/tree/35d7aa1fc1fc8a9f35c707993fc7370393a41a48)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | d2-projects/d2-admin |
| Description | An elegant dashboard |
| Stars | 12611 |
| Forks | 2397 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `35d7aa1fc1fc8a9f35c707993fc7370393a41a48` |
| Retrieved at | 2026-11-14T19:12:05.363817+00:00 |
| Files in this snapshot | 399 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (8 files)
    bug.md
    demo.md
    display.md
    doc.md
    feature.md
    other.md
    question.md
    update.md
  workflows/  (2 files)
    release.yml
    star.yml
docs/  (1 files)
  CHANGELOG.md
public/  (114 files)
  html/  (1 files)
    demo.html
  image/  (1 files)
    loading/  (1 files)
      … 1 files under this directory
  lib/  (109 files)
    UEditor/  (109 files)
      … 109 files under this directory
  markdown/  (1 files)
    demo.md
  index.html
  mobile.html
src/  (235 files)
  api/  (4 files)
    _service.js
    _tools.js
    demo.js
    sys.user.js
  assets/  (43 files)
    style/  (28 files)
      … 28 files under this directory
    svg-icons/  (15 files)
      … 15 files under this directory
  components/  (33 files)
    d2-container/  (10 files)
      … 10 files under this directory
    d2-container-frame/  (1 files)
      … 1 files under this directory
    d2-count-up/  (1 files)
      … 1 files under this directory
    d2-highlight/  (3 files)
      … 3 files under this directory
    d2-icon/  (1 files)
      … 1 files under this directory
    d2-icon-select/  (2 files)
      … 2 files under this directory
    d2-icon-svg/  (1 files)
      … 1 files under this directory
    d2-icon-svg-select/  (1 files)
      … 1 files under this directory
    d2-link-btn/  (1 files)
      … 1 files under this directory
    d2-markdown/  (2 files)
      … 2 files under this directory
    d2-module-index-banner/  (1 files)
      … 1 files under this directory
    d2-module-index-menu/  (3 files)
      … 3 files under this directory
    d2-quill/  (1 files)
      … 1 files under this directory
    d2-scrollbar/  (1 files)
      … 1 files under this directory
    d2-ueditor/  (3 files)
      … 3 files under this directory
    index.js
  layout/  (21 files)
    header-aside/  (21 files)
      … 21 files under this directory
  libs/  (6 files)
    util.cookies.js
    util.db.js
    util.import.development.js
    util.import.production.js
    util.js
    util.log.js
  locales/  (5 files)
    en.json
    ja.json
    mixin.js
    zh-chs.json
    zh-cht.json
  menu/  (4 files)
    modules/  (3 files)
      … 3 files under this directory
    index.js
  plugin/  (4 files)
    d2admin/  (1 files)
      … 1 files under this directory
    error/  (1 files)
      … 1 files under this directory
    log/  (1 files)
      … 1 files under this directory
    open/  (1 files)
      … 1 files under this directory
  router/  (5 files)
    modules/  (3 files)
      … 3 files under this directory
    index.js
    routes.js
  store/  (17 files)
    modules/  (16 files)
      … 16 files under this directory
    index.js
  views/  (89 files)
    demo/  (78 files)
      … 78 files under this directory
    system/  (11 files)
      … 11 files under this directory
  App.vue
  i18n.js
  main.js
  setting.js
src.mobile/  (6 files)
  router/  (1 files)
    index.js
  store/  (1 files)
    index.js
  views/  (1 files)
    index.vue
  App.vue
  main.js
  vant.js
tests/  (17 files)
  unit/  (17 files)
    .eslintrc.js
    d2-container-card-bs.spec.js
    d2-container-card.spec.js
    d2-container-frame.spec.js
    d2-container-full-bs.spec.js
    d2-container-full.spec.js
    d2-container-ghost-bs.spec.js
    d2-container-ghost.spec.js
    d2-count-up.spec.js
    d2-icon-select.spec.js
    d2-icon-svg.spec.js
    d2-icon.spec.js
    d2-link-btn.spec.js
    d2-module-index-banner.spec.js
    d2-module-index-menu.spec.js
    d2-page-cover.spec.js
    d2-source.spec.js
.browserslistrc
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.postcssrc.js
.releaserc.js
LICENSE
README.md
README.zh.md
babel.config.js
d2-admin.babel
jest.config.js
jsconfig.json
package.json
vue.config.js
```

## Entry points

- [src.mobile/main.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src.mobile/main.js)
- [src.mobile/router/index.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src.mobile/router/index.js)
- [src.mobile/store/index.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src.mobile/store/index.js)
- [src/assets/svg-icons/index.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src/assets/svg-icons/index.js)
- [src/components/d2-container/index.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src/components/d2-container/index.js)
- [src/components/index.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src/components/index.js)
- [src/layout/header-aside/index.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src/layout/header-aside/index.js)
- [src/main.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src/main.js)
- [src/menu/index.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src/menu/index.js)
- [src/plugin/d2admin/index.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src/plugin/d2admin/index.js)
- [src/plugin/error/index.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src/plugin/error/index.js)
- [src/plugin/log/index.js](https://github.com/d2-projects/d2-admin/blob/35d7aa1fc1fc8a9f35c707993fc7370393a41a48/src/plugin/log/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 89 file(s) under api layer (observed from repository paths and static analysis). |
| App.vue package | library | Observed | Groups 1 file(s) under app.vue package (observed from repository paths and static analysis). |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 31 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 6 file(s) under external integrations (observed from repository paths and static analysis). |
| i18n.js package | library | Observed | Groups 1 file(s) under i18n.js package (observed from repository paths and static analysis). |
| layout package | library | Observed | Groups 21 file(s) under layout package (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 6 file(s) under libs package (observed from repository paths and static analysis). |
| locales package | library | Observed | Groups 1 file(s) under locales package (observed from repository paths and static analysis). |
| main.js package | library | Observed | Groups 1 file(s) under main.js package (observed from repository paths and static analysis). |
| menu package | library | Observed | Groups 4 file(s) under menu package (observed from repository paths and static analysis). |
| plugin package | library | Observed | Groups 4 file(s) under plugin package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 56 file(s) under public package (observed from repository paths and static analysis). |
| router package | library | Observed | Groups 5 file(s) under router package (observed from repository paths and static analysis). |
| setting.js package | library | Observed | Groups 1 file(s) under setting.js package (observed from repository paths and static analysis). |
| src.mobile package | library | Observed | Groups 5 file(s) under src.mobile package (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 17 file(s) under store package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/star.yml` (ci)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `public/lib/UEditor/jsp/config.json` (config)
- `src/locales/en.json` (config)
- `src/locales/ja.json` (config)
- `src/locales/zh-chs.json` (config)
- `src/locales/zh-cht.json` (config)

## Top-level layout

- `src` — 235 analysed file(s)
- `public` — 114 analysed file(s)
- `tests` — 17 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 10 analysed file(s)
- `src.mobile` — 6 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (3 x generated/minified file excluded; 3 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `35d7aa1fc1fc8a9f35c707993fc7370393a41a48` is the revision these paths and observations refer to.
