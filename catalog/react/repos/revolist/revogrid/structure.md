# Project structure: revolist/revogrid

**Analysed commit:** `07e7c11f14e82d2d89418dac95d4b60e516d20ba`

**Commit reference:** [07e7c11f14e82d2d89418dac95d4b60e516d20ba](https://github.com/revolist/revogrid/commit/07e7c11f14e82d2d89418dac95d4b60e516d20ba)

**Tree at this commit:** [revolist/revogrid@07e7c11f14e8](https://github.com/revolist/revogrid/tree/07e7c11f14e82d2d89418dac95d4b60e516d20ba)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | revolist/revogrid |
| Description | Powerful virtual data table smartsheet with advanced customization. Best features from excel plus incredible  performance 🔋 |
| Stars | 3467 |
| Forks | 213 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `07e7c11f14e82d2d89418dac95d4b60e516d20ba` |
| Retrieved at | 2026-11-14T19:15:18.167626+00:00 |
| Files in this snapshot | 307 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (1 files)
    new-issue.md
  codex/  (1 files)
    prompts/  (1 files)
      … 1 files under this directory
  workflows/  (3 files)
    e2e.yml
    publish.yml
    unit.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
assets/  (7 files)
  angular.svg
  js.svg
  logo.svg
  python.svg
  react.svg
  svelte.svg
  vuejs.svg
e2e/  (38 files)
  helpers/  (9 files)
    assertions.ts
    clipboard.ts
    export.ts
    fixtures.ts
    grid.ts
    interactions.ts
    locators.ts
    selectors.ts
    types.ts
  accessibility.spec.ts
  auto-size.spec.ts
  clipboard.spec.ts
  column-groups.spec.ts
  defaults.spec.ts
  editing.spec.ts
  export.spec.ts
  filtering.spec.ts
  helpers.ts
  layout.spec.ts
  lifecycle.spec.ts
  navigation.spec.ts
  october-wcag-trim.spec.ts
  overlay-scrollbar.spec.ts
  pinning.spec.ts
  range.spec.ts
  rendering.spec.ts
  reordering.spec.ts
  resize-trim-regressions.spec.ts
  row-grouping.spec.ts
  row-headers.spec.ts
  row-resize.spec.ts
  scroll-resize.spec.ts
  set-data-at.spec.ts
  … 5 more files
merged-tests/  (2 files)
  e2e-auto-size.spec.ts
  test-auto-size.spec.ts
readme/  (24 files)
  angular.usage.md
  banner.md
  contribute.md
  e2e.md
  features.md
  framework.md
  install.framework.md
  install.md
  js.usage.md
  license.md
  pro.features.md
  react.cell.md
  react.install.md
  react.title.md
  react.usage.md
  sponsors.md
  svelte-5.usage.md
  svelte.usage.md
  usage.basic.md
  usage.deprecated.md
  version.md
  vue2.title.md
  vue2.usage.md
  vue3.usage.md
scripts/  (9 files)
  event-list.plugin.ts
  finalize-package.mjs
  generate_api.sh
  generate_readme.mjs
  hydrate-types.plugin.ts
  package-commit.mjs
  package-dirs.mjs
  package-formats.test.mjs
  package-version.mjs
src/  (171 files)
  components/  (57 files)
    attribution/  (1 files)
      … 1 files under this directory
    clipboard/  (1 files)
      … 1 files under this directory
    data/  (6 files)
      … 6 files under this directory
    editors/  (4 files)
      … 4 files under this directory
    extra/  (1 files)
      … 1 files under this directory
    header/  (7 files)
      … 7 files under this directory
    order/  (3 files)
      … 3 files under this directory
    overlay/  (6 files)
      … 6 files under this directory
    revoGrid/  (15 files)
      … 15 files under this directory
    rowHeaders/  (2 files)
      … 2 files under this directory
    scroll/  (2 files)
      … 2 files under this directory
    scrollable/  (3 files)
      … 3 files under this directory
    selectionFocus/  (2 files)
      … 2 files under this directory
    selectionTempRange/  (2 files)
      … 2 files under this directory
    vnode/  (2 files)
      … 2 files under this directory
  global/  (3 files)
    _buttons.scss
    _icons.scss
    _mixins.scss
  plugins/  (47 files)
    export/  (3 files)
      … 3 files under this directory
    filter/  (18 files)
      … 18 files under this directory
    groupingRow/  (8 files)
      … 8 files under this directory
    moveColumn/  (2 files)
      … 2 files under this directory
    row-resize/  (4 files)
      … 4 files under this directory
    rtl/  (1 files)
      … 1 files under this directory
    sorting/  (4 files)
      … 4 files under this directory
    wcag/  (1 files)
      … 1 files under this directory
    add-rows-on-paste.plugin.ts
    base.plugin.ts
    column.auto-size.plugin.ts
    column.stretch.plugin.ts
    dispatcher.ts
    index.ts
  serve/  (4 files)
    controller.js
    data.js
    index.html
    style.css
  services/  (9 files)
    cell.helpers.ts
    column.data.provider.ts
    data.provider.ts
    dimension.provider.ts
    local.scroll.service.ts
    local.scroll.timer.ts
    scroll.dimension.helpers.ts
    selection.store.connector.ts
    viewport.provider.ts
  store/  (17 files)
    dataSource/  (5 files)
      … 5 files under this directory
    dimension/  (5 files)
      … 5 files under this directory
    selection/  (3 files)
      … 3 files under this directory
    vp/  (3 files)
      … 3 files under this directory
    index.ts
  themeManager/  (8 files)
    presets/  (7 files)
      … 7 files under this directory
    theme.service.ts
  types/  (9 files)
    dimension.ts
    events.ts
    index.ts
    interfaces.ts
    plugin.ts
    plugin.types.ts
    selection.ts
    theme.ts
    viewport.interfaces.ts
  utils/  (15 files)
    browser.ts
    closest.polifill.ts
    column.utils.ts
    consts.ts
    events.ts
    header.utils.ts
    index.ts
    key.codes.ts
    key.utils.ts
    mobile.ts
    platform.ts
    row-header-utils.ts
    serialization.ts
    store.types.ts
    store.utils.ts
  components.d.ts
  index.ts
test/  (29 files)
  auto-size.spec.ts
  autohide-scroll.spec.ts
  base-plugin.spec.ts
  clipboard.spec.ts
  column-grouping.spec.ts
  column-service.spec.ts
  csv.spec.ts
  data.provider.spec.ts
  data.store.spec.ts
  dimension.spec.ts
  filter.spec.ts
  grouping.spec.ts
  hydrate-package-types.ts
  hydrate-types.ts
  keyboard.service.spec.ts
  october-wcag-items.spec.ts
  overlay-selection.spec.ts
  revogr-edit.spec.ts
  row-resize.spec.ts
  scroll.dimension.spec.ts
  serve.data.spec.ts
  sorting.spec.ts
  theme.spec.ts
  utils.spec.ts
  … 5 more files
.editorconfig
.gitignore
.gitmodules
.prettierrc.js
.prettierrc.json
.sonarcloud.properties
ACCESSIBILITY.md
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
SECURITY.md
package.json
playwright.config.ts
readme.md
stencil.config.ts
tsconfig.fw.json
tsconfig.json
typedoc.json
```

## Entry points

- [src/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/index.ts)
- [src/plugins/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/plugins/index.ts)
- [src/plugins/row-resize/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/plugins/row-resize/index.ts)
- [src/plugins/wcag/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/plugins/wcag/index.ts)
- [src/store/dataSource/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/store/dataSource/index.ts)
- [src/store/dimension/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/store/dimension/index.ts)
- [src/store/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/store/index.ts)
- [src/store/selection/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/store/selection/index.ts)
- [src/store/vp/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/store/vp/index.ts)
- [src/themeManager/presets/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/themeManager/presets/index.ts)
- [src/types/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/types/index.ts)
- [src/utils/index.ts](https://github.com/revolist/revogrid/blob/07e7c11f14e82d2d89418dac95d4b60e516d20ba/src/utils/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 36 file(s) under components package (observed from repository paths and static analysis). |
| components.d.ts package | library | Observed | Groups 1 file(s) under components.d.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 38 file(s) under e2e package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| merged-tests package | library | Observed | Groups 2 file(s) under merged-tests package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 46 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 9 file(s) under scripts package (observed from repository paths and static analysis). |
| serve package | library | Observed | Groups 2 file(s) under serve package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 9 file(s) under service / domain layer (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 17 file(s) under store package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 29 file(s) under tests (observed from repository paths and static analysis). |
| themeManager package | library | Observed | Groups 8 file(s) under thememanager package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 9 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 15 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/e2e.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/unit.yml` (ci)
- `.prettierrc.json` (config)
- `package.json` (manifest)
- `tsconfig.fw.json` (config)
- `tsconfig.json` (config)
- `typedoc.json` (config)

## Top-level layout

- `src` — 171 analysed file(s)
- `e2e` — 38 analysed file(s)
- `test` — 29 analysed file(s)
- `readme` — 24 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `scripts` — 9 analysed file(s)
- `.github` — 8 analysed file(s)
- `assets` — 7 analysed file(s)
- `merged-tests` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `07e7c11f14e82d2d89418dac95d4b60e516d20ba` is the revision these paths and observations refer to.
