# Project structure: alibaba/x-render

**Analysed commit:** `33027864d98ab917f06a4e2656fd7c5bba3bfa2c`

**Commit reference:** [33027864d98ab917f06a4e2656fd7c5bba3bfa2c](https://github.com/alibaba/x-render/commit/33027864d98ab917f06a4e2656fd7c5bba3bfa2c)

**Tree at this commit:** [alibaba/x-render@33027864d98a](https://github.com/alibaba/x-render/tree/33027864d98ab917f06a4e2656fd7c5bba3bfa2c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alibaba/x-render |
| Description | 🚴‍♀️ Very easy to use process form table chart solution. |
| Stars | 7847 |
| Forks | 1072 |
| Licence | Not detected |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `33027864d98ab917f06a4e2656fd7c5bba3bfa2c` |
| Retrieved at | 2026-11-14T19:13:44.914051+00:00 |
| Files in this snapshot | 713 |

## Directory tree

```text
.dumi/  (63 files)
  theme/  (8 files)
    builtins/  (2 files)
      … 2 files under this directory
    layouts/  (1 files)
      … 1 files under this directory
    slots/  (5 files)
      … 5 files under this directory
  tmp-production/  (54 files)
    core/  (13 files)
      … 13 files under this directory
    dumi/  (38 files)
      … 38 files under this directory
    exports.ts
    testBrowser.tsx
    umi.ts
  loading.tsx
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    feature_request.md
  workflows/  (6 files)
    ci.yml
    coverage.yml
    deploy.yml
    emoji-helper.yml
    issue-helper.yml
    mirror.yml
.turbo/  (4 files)
  daemon/  (4 files)
    58af6c43ce0c4d29-turbo.log.2024-12-04
    9af73f40ad414c73-turbo.log.2024-12-03
    9af73f40ad414c73-turbo.log.2024-12-04
    ae401ef4dd981f33-turbo.log.2024-08-26
docs/  (197 files)
  data-render/  (3 files)
    data/  (1 files)
      … 1 files under this directory
    schema/  (1 files)
      … 1 files under this directory
    index.md
  form-render/  (44 files)
    demo/  (15 files)
      … 15 files under this directory
    schema/  (6 files)
      … 6 files under this directory
    test/  (6 files)
      … 6 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    advaced-example.md
    advanced-bind.md
    advanced-layout.md
    advanced-linkage.md
    advanced-path.md
    advanced-slimrender.md
    advanced-validate.md
    advanced-widget.md
    api-props.md
    api-schema.md
    changelog.md
    disaply-search.md
    display-row.md
    faq.md
    index.md
    migrate.md
  form-render-mobile/  (12 files)
    demo/  (7 files)
      … 7 files under this directory
    test/  (2 files)
      … 2 files under this directory
    api.md
    disaply.md
    index.md
  playground/  (18 files)
    controller/  (2 files)
      … 2 files under this directory
    customized/  (1 files)
      … 1 files under this directory
    example/  (1 files)
      … 1 files under this directory
    json/  (10 files)
      … 10 files under this directory
    index.less
    index.md
    index.tsx
    serialize.js
  schema-builder/  (2 files)
    api.md
    index.md
  schema-builder-online/  (1 files)
    index.md
  table-render/  (19 files)
    .test/  (1 files)
      … 1 files under this directory
    demo/  (4 files)
      … 4 files under this directory
    static/  (3 files)
      … 3 files under this directory
    api.md
    basic.md
    collapsed.md
    custom-table.md
    index.md
    migrate.md
    noSearch.md
    promptly-search.md
    tabs.md
    toolbar.md
    valueType.md
  tools/  (2 files)
    proptypes/  (1 files)
      … 1 files under this directory
    vscode/  (1 files)
      … 1 files under this directory
  xflow/  (94 files)
    data/  (1 files)
      … 1 files under this directory
    demo/  (76 files)
      … 76 files under this directory
    schema/  (3 files)
      … 3 files under this directory
    FlowProvider.md
    api.md
    best-practices.md
    custom-node-setting.md
    custom-node-view.md
    index.md
    layout.md
    log.md
    nodeBuildIn.md
    nodeSetting.md
    question.md
    quickStart.md
    singlePointDebug.md
    updateLog.md
  index.en-US.md
  index.zh-CN.md
packages/  (377 files)
  chart-render/  (16 files)
    src/  (11 files)
      … 11 files under this directory
    .fatherrc.ts
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  data-render/  (84 files)
    src/  (77 files)
      … 77 files under this directory
    .fatherrc.js
    CHANGELOG.md
    CONTRIBUTING.md
    LICENSE
    README.md
    package.json
    tsconfig.json
  form-render/  (119 files)
    __tests__/  (8 files)
      … 8 files under this directory
    src/  (104 files)
      … 104 files under this directory
    .fatherrc.js
    CHANGELOG.md
    CONTRIBUTING.md
    LICENSE
    README.md
    package.json
    tsconfig.json
  form-render-mobile/  (41 files)
    src/  (34 files)
      … 34 files under this directory
    .fatherrc.js
    CHANGELOG.md
    CONTRIBUTING.md
    LICENSE
    README.md
    package.json
    tsconfig.json
  table-render/  (35 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (26 files)
      … 26 files under this directory
    .fatherrc.ts
    CHANGELOG.md
    CONTRIBUTION.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    开发文档.md
  x-flow/  (82 files)
    src/  (75 files)
      … 75 files under this directory
    .fatherrc.js
    CHANGELOG.md
    CONTRIBUTING.md
    LICENSE
    README.md
    package.json
    tsconfig.json
scripts/  (3 files)
  dumi-plugin/  (2 files)
    publicPath.ts
    redirect.ts
  prettier-plugin/  (1 files)
    index.js
tools/  (33 files)
  schema-builder/  (33 files)
    src/  (27 files)
      … 27 files under this directory
    .fatherrc.js
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
widgets/  (12 files)
  AsyncOptions/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    .fatherrc.js
    README.md
    package.json
  RichText/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    .fatherrc.js
    README.md
    package.json
  template/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    .fatherrc.js
    README.md
    package.json
.dumirc.ts
.editorconfig
.fatherrc.js
.gitignore
.prettierignore
.prettierrc
CODE_OF_CONDUCT.md
CONTRIBUTING.md
README.md
app.ts
lerna.json
package.json
tsconfig.jest.json
turbo.json
typing.d.ts
vitest.config.ts
```

## Entry points

- [app.ts](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/app.ts)
- [packages/chart-render/src/index.ts](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/packages/chart-render/src/index.ts)
- [packages/data-render/src/index.ts](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/packages/data-render/src/index.ts)
- [packages/form-render-mobile/src/index.tsx](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/packages/form-render-mobile/src/index.tsx)
- [packages/form-render/src/index.ts](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/packages/form-render/src/index.ts)
- [packages/table-render/src/index.tsx](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/packages/table-render/src/index.tsx)
- [packages/x-flow/src/index.ts](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/packages/x-flow/src/index.ts)
- [scripts/prettier-plugin/index.js](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/scripts/prettier-plugin/index.js)
- [tools/schema-builder/src/index.ts](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/tools/schema-builder/src/index.ts)
- [tools/schema-builder/src/main.tsx](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/tools/schema-builder/src/main.tsx)
- [widgets/AsyncOptions/src/index.js](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/widgets/AsyncOptions/src/index.js)
- [widgets/RichText/src/index.js](https://github.com/alibaba/x-render/blob/33027864d98ab917f06a4e2656fd7c5bba3bfa2c/widgets/RichText/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 44 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 29 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 221 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 19 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 5 file(s) under tools package (observed from repository paths and static analysis). |
| widgets package | library | Observed | Groups 6 file(s) under widgets package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/coverage.yml` (ci)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/emoji-helper.yml` (ci)
- `.github/workflows/issue-helper.yml` (ci)
- `.github/workflows/mirror.yml` (ci)
- `docs/playground/json/basic.json` (config)
- `docs/playground/json/demo.json` (config)
- `docs/playground/json/format.json` (config)
- `docs/playground/json/function.json` (config)
- `docs/playground/json/input.json` (config)
- `docs/playground/json/new-feature.json` (config)
- `docs/playground/json/select.json` (config)
- `docs/playground/json/simplest.json` (config)
- `docs/playground/json/test.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/chart-render/package.json` (manifest)
- `packages/chart-render/tsconfig.json` (config)
- `packages/data-render/package.json` (manifest)
- `packages/data-render/tsconfig.json` (config)
- `packages/form-render-mobile/package.json` (manifest)
- `packages/form-render-mobile/tsconfig.json` (config)
- `packages/form-render/package.json` (manifest)
- `packages/form-render/tsconfig.json` (config)
- `packages/table-render/package.json` (manifest)
- `packages/table-render/tsconfig.json` (config)
- `packages/x-flow/package.json` (manifest)
- `packages/x-flow/tsconfig.json` (config)
- `tools/schema-builder/package.json` (manifest)
- `tools/schema-builder/tsconfig.json` (config)
- `tsconfig.jest.json` (config)
- `turbo.json` (config)
- `widgets/AsyncOptions/package.json` (manifest)
- `widgets/RichText/package.json` (manifest)
- `widgets/template/package.json` (manifest)

## Top-level layout

- `packages` — 377 analysed file(s)
- `docs` — 197 analysed file(s)
- `.dumi` — 63 analysed file(s)
- `tools` — 33 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `widgets` — 12 analysed file(s)
- `.github` — 8 analysed file(s)
- `.turbo` — 4 analysed file(s)
- `scripts` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `33027864d98ab917f06a4e2656fd7c5bba3bfa2c` is the revision these paths and observations refer to.
