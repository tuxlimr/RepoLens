# Project structure: Meituan-Dianping/mpvue

**Analysed commit:** `6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b`

**Commit reference:** [6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b](https://github.com/Meituan-Dianping/mpvue/commit/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b)

**Tree at this commit:** [Meituan-Dianping/mpvue@6c5d78ee04f5](https://github.com/Meituan-Dianping/mpvue/tree/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Meituan-Dianping/mpvue |
| Description | 基于 Vue.js 的小程序开发框架，从底层支持 Vue.js 语法和构建工具体系。 |
| Stars | 20209 |
| Forks | 2015 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b` |
| Retrieved at | 2026-11-14T19:11:14.704993+00:00 |
| Files in this snapshot | 491 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    Bug_report.md
    Feature_request.md
  CODE_OF_CONDUCT.md
  COMMIT_CONVENTION.md
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
  issue_template.yml
  stale.yml
benchmarks/  (16 files)
  big-table/  (3 files)
    demo.css
    index.html
    style.css
  dbmon/  (6 files)
    lib/  (3 files)
      … 3 files under this directory
    ENV.js
    app.js
    index.html
  reorder-list/  (1 files)
    index.html
  ssr/  (4 files)
    README.md
    common.js
    renderToStream.js
    renderToString.js
  svg/  (1 files)
    index.html
  uptime/  (1 files)
    index.html
examples/  (24 files)
  commits/  (2 files)
    app.js
    index.html
  elastic-header/  (2 files)
    index.html
    style.css
  firebase/  (3 files)
    app.js
    index.html
    style.css
  grid/  (3 files)
    grid.js
    index.html
    style.css
  markdown/  (2 files)
    index.html
    style.css
  modal/  (2 files)
    index.html
    style.css
  move-animations/  (1 files)
    index.html
  select2/  (1 files)
    index.html
  svg/  (3 files)
    index.html
    style.css
    svg.js
  todomvc/  (3 files)
    app.js
    index.html
    readme.md
  tree/  (2 files)
    index.html
    tree.js
flow/  (7 files)
  compiler.js
  component.js
  global-api.js
  modules.js
  options.js
  ssr.js
  vnode.js
packages/  (27 files)
  mpvue/  (3 files)
    README.md
    index.js
    package.json
  mpvue-template-compiler/  (4 files)
    README.md
    build.js
    index.js
    package.json
  vue-server-renderer/  (8 files)
    types/  (3 files)
      … 3 files under this directory
    README.md
    client-plugin.js
    index.js
    package.json
    server-plugin.js
  vue-template-compiler/  (4 files)
    README.md
    build.js
    index.js
    package.json
  weex-template-compiler/  (4 files)
    README.md
    build.js
    index.js
    package.json
  weex-vue-framework/  (4 files)
    README.md
    factory.js
    index.js
    package.json
src/  (228 files)
  compiler/  (17 files)
    codegen/  (2 files)
      … 2 files under this directory
    directives/  (4 files)
      … 4 files under this directory
    parser/  (5 files)
      … 5 files under this directory
    create-compiler.js
    error-detector.js
    helpers.js
    index.js
    optimizer.js
    to-function.js
  core/  (53 files)
    components/  (2 files)
      … 2 files under this directory
    global-api/  (5 files)
      … 5 files under this directory
    instance/  (16 files)
      … 16 files under this directory
    observer/  (5 files)
      … 5 files under this directory
    util/  (8 files)
      … 8 files under this directory
    vdom/  (15 files)
      … 15 files under this directory
    config.js
    index.js
  platforms/  (133 files)
    mp/  (59 files)
      … 59 files under this directory
    web/  (48 files)
      … 48 files under this directory
    weex/  (26 files)
      … 26 files under this directory
  server/  (22 files)
    bundle-renderer/  (3 files)
      … 3 files under this directory
    optimizing-compiler/  (5 files)
      … 5 files under this directory
    template-renderer/  (4 files)
      … 4 files under this directory
    webpack-plugin/  (3 files)
      … 3 files under this directory
    create-basic-renderer.js
    create-renderer.js
    render-context.js
    render-stream.js
    render.js
    util.js
    write.js
  sfc/  (1 files)
    parser.js
  shared/  (2 files)
    constants.js
    util.js
test/  (159 files)
  e2e/  (11 files)
    specs/  (8 files)
      … 8 files under this directory
    .eslintrc
    nightwatch.config.js
    runner.js
  helpers/  (8 files)
    .eslintrc
    classlist.js
    test-object-option.js
    to-equal.js
    to-have-been-warned.js
    trigger-event.js
    vdom.js
    wait-for-update.js
  mp/  (8 files)
    compiler/  (1 files)
      … 1 files under this directory
    helpers/  (2 files)
      … 2 files under this directory
    runtime/  (3 files)
      … 3 files under this directory
    .eslintrc
    jasmine.json
  ssr/  (17 files)
    fixtures/  (8 files)
      … 8 files under this directory
    .eslintrc
    async-loader.js
    compile-with-webpack.js
    jasmine.json
    ssr-basic-renderer.spec.js
    ssr-bundle-render.spec.js
    ssr-stream.spec.js
    ssr-string.spec.js
    ssr-template.spec.js
  unit/  (100 files)
    features/  (70 files)
      … 70 files under this directory
    modules/  (23 files)
      … 23 files under this directory
    .eslintrc
    index.js
    karma.base.config.js
    karma.cover.config.js
    karma.dev.config.js
    karma.sauce.config.js
    karma.unit.config.js
  weex/  (15 files)
    compiler/  (6 files)
      … 6 files under this directory
    helpers/  (1 files)
      … 1 files under this directory
    runtime/  (6 files)
      … 6 files under this directory
    .eslintrc
    jasmine.json
types/  (11 files)
  test/  (5 files)
    augmentation-test.ts
    options-test.ts
    plugin-test.ts
    tsconfig.json
    vue-test.ts
  index.d.ts
  options.d.ts
  plugin.d.ts
  typings.json
  vnode.d.ts
  vue.d.ts
.babelrc
.editorconfig
.eslintignore
.eslintrc
.flowconfig
.gitignore
BACKERS.md
LICENSE
README.md
circle.yml
package.json
```

## Entry points

- [packages/mpvue-template-compiler/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/packages/mpvue-template-compiler/index.js)
- [packages/mpvue/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/packages/mpvue/index.js)
- [packages/vue-server-renderer/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/packages/vue-server-renderer/index.js)
- [packages/vue-template-compiler/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/packages/vue-template-compiler/index.js)
- [packages/weex-template-compiler/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/packages/weex-template-compiler/index.js)
- [packages/weex-vue-framework/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/packages/weex-vue-framework/index.js)
- [benchmarks/dbmon/app.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/benchmarks/dbmon/app.js)
- [src/compiler/codegen/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/src/compiler/codegen/index.js)
- [src/compiler/directives/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/src/compiler/directives/index.js)
- [src/compiler/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/src/compiler/index.js)
- [src/compiler/parser/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/src/compiler/parser/index.js)
- [src/core/components/index.js](https://github.com/Meituan-Dianping/mpvue/blob/6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b/src/core/components/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 7 file(s) under benchmarks package (observed from repository paths and static analysis). |
| compiler package | library | Observed | Groups 17 file(s) under compiler package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| flow package | library | Observed | Groups 7 file(s) under flow package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 14 file(s) under packages package (observed from repository paths and static analysis). |
| platforms package | library | Observed | Groups 125 file(s) under platforms package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 22 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 53 file(s) under service / domain layer (observed from repository paths and static analysis). |
| sfc package | library | Observed | Groups 1 file(s) under sfc package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 2 file(s) under shared package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 164 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 5 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/issue_template.yml` (config)
- `.github/stale.yml` (config)
- `circle.yml` (config)
- `package.json` (manifest)
- `packages/mpvue-template-compiler/package.json` (manifest)
- `packages/mpvue/package.json` (manifest)
- `packages/vue-server-renderer/package.json` (manifest)
- `packages/vue-server-renderer/types/tsconfig.json` (config)
- `packages/vue-template-compiler/package.json` (manifest)
- `packages/weex-template-compiler/package.json` (manifest)
- `packages/weex-vue-framework/package.json` (manifest)
- `types/typings.json` (config)

## Top-level layout

- `src` — 228 analysed file(s)
- `test` — 159 analysed file(s)
- `packages` — 27 analysed file(s)
- `examples` — 24 analysed file(s)
- `benchmarks` — 16 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `types` — 11 analysed file(s)
- `.github` — 8 analysed file(s)
- `flow` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 16 file(s) were skipped during inventory (1 x lockfile excluded; 15 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6c5d78ee04f58c6d782c456dfcf0fe63c0b7f89b` is the revision these paths and observations refer to.
