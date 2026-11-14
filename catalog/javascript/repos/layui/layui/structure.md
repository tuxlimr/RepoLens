# Project structure: layui/layui

**Analysed commit:** `13725717407d23fac11b15b1a1155d26328b6d99`

**Commit reference:** [13725717407d23fac11b15b1a1155d26328b6d99](https://github.com/layui/layui/commit/13725717407d23fac11b15b1a1155d26328b6d99)

**Tree at this commit:** [layui/layui@13725717407d](https://github.com/layui/layui/tree/13725717407d23fac11b15b1a1155d26328b6d99)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | layui/layui |
| Description | 一套遵循浏览器原生态开发模式的 Web UI 组件库。 |
| Stars | 30584 |
| Forks | 7339 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `13725717407d23fac11b15b1a1155d26328b6d99` |
| Retrieved at | 2026-11-14T19:10:46.839364+00:00 |
| Files in this snapshot | 181 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-feature.yml
    config.yml
  workflows/  (6 files)
    ci.yml
    issue-closed.yml
    issue-labeled.yml
    issue-opened.yml
    pr-preview.yml
    release.yml
  FUNDING.yml
  copilot-instructions.md
  pull_request_template.md
.husky/  (2 files)
  install.mjs
  pre-commit
docs/  (5 files)
  .template/  (4 files)
    detail/  (2 files)
      … 2 files under this directory
    examples/  (1 files)
      … 1 files under this directory
    index.md
  README.md
scripts/  (4 files)
  dev-builder.mjs
  dev.mjs
  release.mjs
  rollup-plugins.mjs
src/  (71 files)
  components/  (25 files)
    breadcrumb.js
    carousel.js
    code.js
    collapse.js
    colorPicker.js
    datePicker.js
    dropdown.js
    floatbar.js
    flow.js
    form.js
    initializer.js
    layer.js
    laypage.js
    menu.js
    nav.js
    popup.js
    progress.js
    rate.js
    slider.js
    table.js
    tabs.js
    transfer.js
    tree.js
    treeTable.js
    … 1 more files
  core/  (7 files)
    component.js
    i18n.js
    lay.js
    laytpl.js
    loader.js
    logger.js
    router.js
  css/  (33 files)
    modules/  (30 files)
      … 30 files under this directory
    base.css
    index.css
    var.css
  utils/  (4 files)
    browser.js
    date.js
    events.js
    index.js
  index.js
  index.umd.js
tests/  (68 files)
  unit/  (2 files)
    core.test.js
    layExtend.test.js
  visual/  (66 files)
    assets/  (17 files)
      … 17 files under this directory
    esm/  (1 files)
      … 1 files under this directory
    template/  (8 files)
      … 8 files under this directory
    base.html
    button.html
    carousel.html
    code.html
    collapse.html
    colorPicker.html
    datePicker.html
    dropdown.html
    floatbar.html
    flow.html
    form.html
    i18n.html
    layer.html
    layout-admin.html
    layout-grid.html
    laypage.html
    laytpl.html
    loader.html
    menu.html
    nav.html
    popup.html
    progress.html
    rate.html
    router.html
    … 16 more files
.editorconfig
.gitattributes
.gitignore
.nvmrc
.prettierignore
.prettierrc
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DISCLAIMER.md
LICENSE
README.en-US.md
README.md
SECURITY.md
biome.json
eslint.config.mjs
jest.config.mjs
package.json
postcss.config.mjs
rollup.config.mjs
```

## Entry points

- [tests/visual/template/pr-preview/index.js](https://github.com/layui/layui/blob/13725717407d23fac11b15b1a1155d26328b6d99/tests/visual/template/pr-preview/index.js)
- [src/index.js](https://github.com/layui/layui/blob/13725717407d23fac11b15b1a1155d26328b6d99/src/index.js)
- [src/utils/index.js](https://github.com/layui/layui/blob/13725717407d23fac11b15b1a1155d26328b6d99/src/utils/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 25 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| index.umd.js package | library | Observed | Groups 1 file(s) under index.umd.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 7 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 68 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-feature.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/issue-closed.yml` (ci)
- `.github/workflows/issue-labeled.yml` (ci)
- `.github/workflows/issue-opened.yml` (ci)
- `.github/workflows/pr-preview.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `biome.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 71 analysed file(s)
- `tests` — 68 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 11 analysed file(s)
- `docs` — 5 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `13725717407d23fac11b15b1a1155d26328b6d99` is the revision these paths and observations refer to.
