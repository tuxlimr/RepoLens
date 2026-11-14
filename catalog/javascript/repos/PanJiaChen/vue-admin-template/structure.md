# Project structure: PanJiaChen/vue-admin-template

**Analysed commit:** `4c18a3f47bdb417ad8a25f09910f848cb574dee2`

**Commit reference:** [4c18a3f47bdb417ad8a25f09910f848cb574dee2](https://github.com/PanJiaChen/vue-admin-template/commit/4c18a3f47bdb417ad8a25f09910f848cb574dee2)

**Tree at this commit:** [PanJiaChen/vue-admin-template@4c18a3f47bdb](https://github.com/PanJiaChen/vue-admin-template/tree/4c18a3f47bdb417ad8a25f09910f848cb574dee2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | PanJiaChen/vue-admin-template |
| Description | a vue2.0 minimal admin template  |
| Stars | 20343 |
| Forks | 7336 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `4c18a3f47bdb417ad8a25f09910f848cb574dee2` |
| Retrieved at | 2026-11-14T19:11:14.043450+00:00 |
| Files in this snapshot | 91 |

## Directory tree

```text
mock/  (5 files)
  index.js
  mock-server.js
  table.js
  user.js
  utils.js
public/  (1 files)
  index.html
src/  (63 files)
  api/  (2 files)
    table.js
    user.js
  components/  (3 files)
    Breadcrumb/  (1 files)
      … 1 files under this directory
    Hamburger/  (1 files)
      … 1 files under this directory
    SvgIcon/  (1 files)
      … 1 files under this directory
  icons/  (13 files)
    svg/  (11 files)
      … 11 files under this directory
    index.js
    svgo.yml
  layout/  (11 files)
    components/  (9 files)
      … 9 files under this directory
    mixin/  (1 files)
      … 1 files under this directory
    index.vue
  router/  (1 files)
    index.js
  store/  (5 files)
    modules/  (3 files)
      … 3 files under this directory
    getters.js
    index.js
  styles/  (6 files)
    element-ui.scss
    index.scss
    mixin.scss
    sidebar.scss
    transition.scss
    variables.scss
  utils/  (5 files)
    auth.js
    get-page-title.js
    index.js
    request.js
    validate.js
  views/  (13 files)
    dashboard/  (1 files)
      … 1 files under this directory
    form/  (1 files)
      … 1 files under this directory
    login/  (1 files)
      … 1 files under this directory
    nested/  (7 files)
      … 7 files under this directory
    table/  (1 files)
      … 1 files under this directory
    tree/  (1 files)
      … 1 files under this directory
    404.vue
  App.vue
  main.js
  permission.js
  settings.js
tests/  (8 files)
  unit/  (8 files)
    components/  (3 files)
      … 3 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    .eslintrc.js
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.travis.yml
LICENSE
README-zh.md
README.md
babel.config.js
jest.config.js
jsconfig.json
package.json
postcss.config.js
vue.config.js
```

## Entry points

- [mock/index.js](https://github.com/PanJiaChen/vue-admin-template/blob/4c18a3f47bdb417ad8a25f09910f848cb574dee2/mock/index.js)
- [src/icons/index.js](https://github.com/PanJiaChen/vue-admin-template/blob/4c18a3f47bdb417ad8a25f09910f848cb574dee2/src/icons/index.js)
- [src/layout/components/index.js](https://github.com/PanJiaChen/vue-admin-template/blob/4c18a3f47bdb417ad8a25f09910f848cb574dee2/src/layout/components/index.js)
- [src/main.js](https://github.com/PanJiaChen/vue-admin-template/blob/4c18a3f47bdb417ad8a25f09910f848cb574dee2/src/main.js)
- [src/router/index.js](https://github.com/PanJiaChen/vue-admin-template/blob/4c18a3f47bdb417ad8a25f09910f848cb574dee2/src/router/index.js)
- [src/store/index.js](https://github.com/PanJiaChen/vue-admin-template/blob/4c18a3f47bdb417ad8a25f09910f848cb574dee2/src/store/index.js)
- [src/store/modules/app.js](https://github.com/PanJiaChen/vue-admin-template/blob/4c18a3f47bdb417ad8a25f09910f848cb574dee2/src/store/modules/app.js)
- [src/utils/index.js](https://github.com/PanJiaChen/vue-admin-template/blob/4c18a3f47bdb417ad8a25f09910f848cb574dee2/src/utils/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 15 file(s) under api layer (observed from repository paths and static analysis). |
| App.vue package | library | Observed | Groups 1 file(s) under app.vue package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 3 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| icons package | library | Observed | Groups 1 file(s) under icons package (observed from repository paths and static analysis). |
| layout package | library | Observed | Groups 11 file(s) under layout package (observed from repository paths and static analysis). |
| main.js package | library | Observed | Groups 1 file(s) under main.js package (observed from repository paths and static analysis). |
| mock package | library | Observed | Groups 5 file(s) under mock package (observed from repository paths and static analysis). |
| permission.js package | library | Observed | Groups 1 file(s) under permission.js package (observed from repository paths and static analysis). |
| router package | library | Observed | Groups 1 file(s) under router package (observed from repository paths and static analysis). |
| settings.js package | library | Observed | Groups 1 file(s) under settings.js package (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 5 file(s) under store package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `src/icons/svgo.yml` (config)

## Top-level layout

- `src` — 63 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `tests` — 8 analysed file(s)
- `mock` — 5 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (3 x likely secret file excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4c18a3f47bdb417ad8a25f09910f848cb574dee2` is the revision these paths and observations refer to.
