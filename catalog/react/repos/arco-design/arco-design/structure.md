# Project structure: arco-design/arco-design

**Analysed commit:** `84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2`

**Commit reference:** [84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2](https://github.com/arco-design/arco-design/commit/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2)

**Tree at this commit:** [arco-design/arco-design@84504beeaf68](https://github.com/arco-design/arco-design/tree/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | arco-design/arco-design |
| Description | A comprehensive React UI components library based on Arco Design |
| Stars | 5766 |
| Forks | 724 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2` |
| Retrieved at | 2026-11-14T19:14:14.792634+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.codebase/  (1 files)
  pipelines/  (1 files)
    mr_check.yaml
.codesandbox/  (1 files)
  ci.json
.config/  (4 files)
  docgen.config.js
  jest.config.js
  style.config.js
  webpack.config.js
.github/  (9 files)
  ISSUE_TEMPLATE/  (1 files)
    config.yml
  workflows/  (7 files)
    build_size.yml
    deploy-site-preview.yml
    main.yml
    npm-publish.yml
    pr_check.yml
    preview-start.yml
    release.yml
  PULL_REQUEST_TEMPLATE.md
.husky/  (1 files)
  pre-commit
.storybook/  (3 files)
  index.less
  main.js
  preview.js
components/  (765 files)
  Affix/  (19 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (5 files)
      … 5 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (2 files)
      … 2 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
  Alert/  (23 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (8 files)
      … 8 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
  Anchor/  (27 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (7 files)
      … 7 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (4 files)
      … 4 files under this directory
    README.en-US.md
    README.zh-CN.md
    anchor.tsx
    context.ts
    index.tsx
    interface.ts
    link.tsx
    utils.ts
  AutoComplete/  (23 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (8 files)
      … 8 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
  Avatar/  (23 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (5 files)
      … 5 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    avatar.tsx
    context.ts
    group.tsx
    index.tsx
    interface.ts
  BackTop/  (17 files)
    __changelog__/  (1 files)
      … 1 files under this directory
    __demo__/  (3 files)
      … 3 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
  Badge/  (24 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (8 files)
      … 8 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    count.tsx
    index.tsx
    interface.ts
  Breadcrumb/  (22 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (6 files)
      … 6 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
    item.tsx
  Button/  (25 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (9 files)
      … 9 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    group.tsx
    index.tsx
    interface.ts
  Calendar/  (25 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (4 files)
      … 4 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    header/  (2 files)
      … 2 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
    month.tsx
    week-list.tsx
    year.tsx
  Card/  (28 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (11 files)
      … 11 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    grid.tsx
    index.tsx
    interface.ts
    meta.tsx
  Carousel/  (26 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (8 files)
      … 8 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (4 files)
      … 4 files under this directory
    README.en-US.md
    README.zh-CN.md
    arrow.tsx
    index.tsx
    indicator.tsx
    interface.ts
  Cascader/  (47 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (21 files)
      … 21 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (6 files)
      … 6 files under this directory
    base/  (2 files)
      … 2 files under this directory
    hook/  (1 files)
      … 1 files under this directory
    panel/  (3 files)
      … 3 files under this directory
    style/  (4 files)
      … 4 files under this directory
    README.en-US.md
    README.zh-CN.md
    cascader.tsx
    index.tsx
    interface.ts
    util.tsx
  Checkbox/  (30 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (9 files)
      … 9 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (6 files)
      … 6 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    checkbox.tsx
    group.tsx
    icon-check.tsx
    index.tsx
    interface.ts
    useCheckbox.ts
  Collapse/  (27 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (10 files)
      … 10 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    collapse.tsx
    index.tsx
    interface.ts
    item.tsx
  ColorPicker/  (33 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (9 files)
      … 9 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (2 files)
      … 2 files under this directory
    hooks/  (2 files)
      … 2 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    colors.ts
    control-bar.tsx
    index.tsx
    input-alpha.tsx
    input-hex.tsx
    input-rgb.tsx
    interface.ts
    mode.ts
    palette.tsx
    panel.tsx
    utils.ts
  Comment/  (18 files)
    __demo__/  (5 files)
      … 5 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
  ConfigProvider/  (23 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (8 files)
      … 8 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (1 files)
      … 1 files under this directory
    README.en-US.md
    README.zh-CN.md
    context.tsx
    index.tsx
    interface.ts
    util.ts
  DatePicker/  (75 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (23 files)
      … 23 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (17 files)
      … 17 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    panels/  (11 files)
      … 11 files under this directory
    style/  (11 files)
      … 11 files under this directory
    README.en-US.md
    README.zh-CN.md
    context.ts
    index.tsx
    interface.tsx
    picker-range.tsx
    picker.tsx
    util.ts
  Descriptions/  (22 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (7 files)
      … 7 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
  Divider/  (18 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (3 files)
      … 3 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
  Drawer/  (21 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (7 files)
      … 7 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (3 files)
      … 3 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
  Dropdown/  (27 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (11 files)
      … 11 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    button.tsx
    index.tsx
    interface.ts
  Empty/  (16 files)
    __demo__/  (3 files)
      … 3 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    style/  (3 files)
      … 3 files under this directory
    README.en-US.md
    README.zh-CN.md
    index.tsx
    interface.ts
  Form/  (65 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (26 files)
      … 26 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (13 files)
      … 13 files under this directory
    hooks/  (3 files)
      … 3 files under this directory
    style/  (4 files)
      … 4 files under this directory
    README.en-US.md
    README.zh-CN.md
    context.ts
    control.tsx
    form-item.tsx
    form-label.tsx
    form-list.tsx
    form-provider.tsx
    form.tsx
    index.tsx
    interface.tsx
    promisify.ts
    store.tsx
    useForm.ts
    utils.tsx
  Grid/  (36 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (12 files)
      … 12 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    style/  (5 files)
      … 5 files under this directory
    README.en-US.md
    README.zh-CN.md
    col.tsx
    context.ts
    grid-item.tsx
    grid.tsx
    index.tsx
    interface.ts
    row.tsx
    utils.ts
  Icon/  (3 files)
    style/  (1 files)
      … 1 files under this directory
    addFromIconFontCn.tsx
    index.tsx
  Image/  (22 files)
    __changelog__/  (2 files)
      … 2 files under this directory
    __demo__/  (12 files)
      … 12 files under this directory
    __template__/  (2 files)
      … 2 files under this directory
    __test__/  (4 files)
      … 4 files under this directory
    README.en-US.md
    README.zh-CN.md
.browserslistrc
.editorconfig
.eslintignore
.eslintrc
.gitattributes
.gitignore
.prettierignore
.prettierrc
.stylelintignore
.stylelintrc
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTING.zh-CN.md
LICENSE
README.md
README.zh-CN.md
```

## Entry points

- [.storybook/main.js](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/.storybook/main.js)
- [components/Affix/index.tsx](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/Affix/index.tsx)
- [components/Affix/style/index.ts](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/Affix/style/index.ts)
- [components/Alert/index.tsx](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/Alert/index.tsx)
- [components/Alert/style/index.ts](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/Alert/style/index.ts)
- [components/Anchor/index.tsx](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/Anchor/index.tsx)
- [components/Anchor/style/index.ts](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/Anchor/style/index.ts)
- [components/AutoComplete/index.tsx](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/AutoComplete/index.tsx)
- [components/AutoComplete/style/index.ts](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/AutoComplete/style/index.ts)
- [components/Avatar/index.tsx](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/Avatar/index.tsx)
- [components/Avatar/style/index.ts](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/Avatar/style/index.ts)
- [components/BackTop/index.tsx](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/components/BackTop/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 248 file(s) under components package (observed from repository paths and static analysis). |

## Important files

- `.codebase/pipelines/mr_check.yaml` (config)
- `.codesandbox/ci.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/build_size.yml` (ci)
- `.github/workflows/deploy-site-preview.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/npm-publish.yml` (ci)
- `.github/workflows/pr_check.yml` (ci)
- `.github/workflows/preview-start.yml` (ci)
- `.github/workflows/release.yml` (ci)

## Top-level layout

- `components` — 765 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 9 analysed file(s)
- `.config` — 4 analysed file(s)
- `.storybook` — 3 analysed file(s)
- `.codebase` — 1 analysed file(s)
- `.codesandbox` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2` is the revision these paths and observations refer to.
