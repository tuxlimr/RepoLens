# Project structure: preactjs/preact

**Analysed commit:** `a2e03dbc6a4a239552d43edb6580ecf86886cc39`

**Commit reference:** [a2e03dbc6a4a239552d43edb6580ecf86886cc39](https://github.com/preactjs/preact/commit/a2e03dbc6a4a239552d43edb6580ecf86886cc39)

**Tree at this commit:** [preactjs/preact@a2e03dbc6a4a](https://github.com/preactjs/preact/tree/a2e03dbc6a4a239552d43edb6580ecf86886cc39)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | preactjs/preact |
| Description | ⚛️ Fast 3kB React alternative with the same modern API. Components & Virtual DOM. |
| Stars | 39005 |
| Forks | 2462 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `a2e03dbc6a4a239552d43edb6580ecf86886cc39` |
| Retrieved at | 2026-11-14T19:10:41.056718+00:00 |
| Files in this snapshot | 308 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (8 files)
    benchmarks.yml
    build-test.yml
    ci.yml
    pr-reporter.yml
    release.yml
    run-bench.yml
    single-bench.yml
    size.yml
  CODEOWNERS
  CODE_OF_CONDUCT.md
.husky/  (1 files)
  pre-commit
compat/  (83 files)
  src/  (13 files)
    Children.js
    PureComponent.js
    forwardRef.js
    hooks.js
    index.d.ts
    index.js
    internal.d.ts
    memo.js
    portals.js
    render.js
    suspense.d.ts
    suspense.js
    util.js
  test/  (48 files)
    browser/  (37 files)
      … 37 files under this directory
    ts/  (11 files)
      … 11 files under this directory
  LICENSE
  client.d.ts
  client.js
  client.mjs
  compiler-runtime.d.ts
  compiler-runtime.js
  compiler-runtime.mjs
  jsx-dev-runtime.js
  jsx-dev-runtime.mjs
  jsx-runtime.js
  jsx-runtime.mjs
  mangle.json
  package.json
  scheduler.d.ts
  scheduler.js
  scheduler.mjs
  server.browser.mjs
  server.d.ts
  server.js
  server.mjs
  test-utils.js
  test-utils.mjs
config/  (1 files)
  compat-entries.js
debug/  (22 files)
  src/  (8 files)
    check-props.js
    component-stack.js
    constants.js
    debug.js
    index.d.ts
    index.js
    internal.d.ts
    util.js
  test/  (11 files)
    browser/  (11 files)
      … 11 files under this directory
  LICENSE
  mangle.json
  package.json
demo/  (52 files)
  nested-suspense/  (6 files)
    addnewcomponent.jsx
    component-container.jsx
    dropzone.jsx
    editor.jsx
    index.jsx
    subcomponent.jsx
  people/  (11 files)
    styles/  (6 files)
      … 6 files under this directory
    Readme.md
    index.tsx
    profile.tsx
    router.tsx
    store.ts
  pythagoras/  (2 files)
    index.jsx
    pythagoras.jsx
  suspense-router/  (4 files)
    bye.jsx
    hello.jsx
    index.jsx
    simple-router.jsx
  contenteditable.jsx
  context.jsx
  devtools.jsx
  fragments.jsx
  index.html
  index.jsx
  key_bug.jsx
  list.jsx
  logger.jsx
  mobx.jsx
  old.js.bak
  package.json
  preact.jsx
  profiler.jsx
  redux-toolkit.jsx
  redux.jsx
  reduxUpdate.jsx
  reorder.jsx
  spiral.jsx
  stateOrderBug.jsx
  style.css
  style.scss
  styled-components.jsx
  suspense.jsx
  … 5 more files
devtools/  (7 files)
  src/  (3 files)
    devtools.js
    index.d.ts
    index.js
  test/  (1 files)
    browser/  (1 files)
      … 1 files under this directory
  LICENSE
  mangle.json
  package.json
hooks/  (23 files)
  src/  (3 files)
    index.d.ts
    index.js
    internal.d.ts
  test/  (17 files)
    _util/  (1 files)
      … 1 files under this directory
    browser/  (16 files)
      … 16 files under this directory
  LICENSE
  mangle.json
  package.json
jsx-runtime/  (7 files)
  src/  (3 files)
    index.d.ts
    index.js
    utils.js
  test/  (1 files)
    browser/  (1 files)
      … 1 files under this directory
  LICENSE
  mangle.json
  package.json
scripts/  (2 files)
  babel-plugin-fast-rest.mjs
  build.mjs
src/  (17 files)
  diff/  (4 files)
    catch-error.js
    children.js
    index.js
    props.js
  component.js
  constants.js
  create-context.js
  create-element.js
  create-portal.js
  dom.d.ts
  index.d.ts
  index.js
  internal.d.ts
  jsx.d.ts
  options.js
  render.js
  util.js
test/  (59 files)
  _util/  (4 files)
    dom.js
    helpers.jsx
    logCall.js
    optionSpies.js
  browser/  (37 files)
    lifecycles/  (12 files)
      … 12 files under this directory
    cloneElement.test.jsx
    components.test.jsx
    context.test.jsx
    createContext.test.jsx
    customBuiltInElements.test.jsx
    events.test.jsx
    focus.test.jsx
    fragments.test.jsx
    getDomSibling.test.jsx
    hardened-js.test.jsx
    hydrate.test.jsx
    isValidElement.test.js
    keys.test.jsx
    mathml.test.jsx
    placeholders.test.jsx
    portals.test.jsx
    refs.test.jsx
    render.test.jsx
    select.test.jsx
    signals.test.jsx
    spec.test.jsx
    style.test.jsx
    svg.test.jsx
    toChildArray.test.jsx
    … 1 more files
  fixtures/  (1 files)
    preact.js
  node/  (1 files)
    index.test.js
  shared/  (5 files)
    createContext.test.jsx
    createElement.test.jsx
    exports.test.js
    isValidElement.test.js
    isValidElementTests.jsx
  ts/  (11 files)
    Component.test.tsx
    VNode.test.tsx
    custom-elements.tsx
    dom-attributes.test-d.tsx
    hoc.test.tsx
    jsx-namespace.test-d.tsx
    package.json
    preact-global.test-d.tsx
    preact.tsx
    refs.tsx
    tsconfig.json
test-utils/  (5 files)
  src/  (2 files)
    index.d.ts
    index.js
  test/  (2 files)
    shared/  (2 files)
      … 2 files under this directory
  package.json
types/  (1 files)
  weak-key.d.ts
.editorconfig
.gitignore
.gitmodules
.oxfmtrc.json
.oxlintrc.json
.prettierignore
CONTRIBUTING.md
LICENSE
README.md
jsconfig-lint.json
jsconfig.json
mangle.json
package.json
pnpm-workspace.yaml
vitest.config.mjs
vitest.setup.js
```

## Entry points

- [compat/server.js](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/compat/server.js)
- [compat/src/index.js](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/compat/src/index.js)
- [debug/src/index.js](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/debug/src/index.js)
- [demo/index.jsx](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/demo/index.jsx)
- [demo/nested-suspense/index.jsx](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/demo/nested-suspense/index.jsx)
- [demo/people/index.tsx](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/demo/people/index.tsx)
- [demo/pythagoras/index.jsx](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/demo/pythagoras/index.jsx)
- [demo/suspense-router/index.jsx](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/demo/suspense-router/index.jsx)
- [devtools/src/index.js](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/devtools/src/index.js)
- [hooks/src/index.js](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/hooks/src/index.js)
- [jsx-runtime/src/index.js](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/jsx-runtime/src/index.js)
- [src/diff/index.js](https://github.com/preactjs/preact/blob/a2e03dbc6a4a239552d43edb6580ecf86886cc39/src/diff/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| compat package | library | Observed | Groups 32 file(s) under compat package (observed from repository paths and static analysis). |
| component.js package | library | Observed | Groups 1 file(s) under component.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| create-context.js package | library | Observed | Groups 1 file(s) under create-context.js package (observed from repository paths and static analysis). |
| create-element.js package | library | Observed | Groups 1 file(s) under create-element.js package (observed from repository paths and static analysis). |
| create-portal.js package | library | Observed | Groups 1 file(s) under create-portal.js package (observed from repository paths and static analysis). |
| debug package | library | Observed | Groups 8 file(s) under debug package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 39 file(s) under demo package (observed from repository paths and static analysis). |
| devtools package | library | Observed | Groups 3 file(s) under devtools package (observed from repository paths and static analysis). |
| diff package | library | Observed | Groups 4 file(s) under diff package (observed from repository paths and static analysis). |
| dom.d.ts package | library | Observed | Groups 1 file(s) under dom.d.ts package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 3 file(s) under hooks package (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| internal.d.ts package | library | Observed | Groups 1 file(s) under internal.d.ts package (observed from repository paths and static analysis). |
| jsx.d.ts package | library | Observed | Groups 1 file(s) under jsx.d.ts package (observed from repository paths and static analysis). |
| jsx-runtime package | library | Observed | Groups 3 file(s) under jsx-runtime package (observed from repository paths and static analysis). |
| options.js package | library | Observed | Groups 1 file(s) under options.js package (observed from repository paths and static analysis). |
| render.js package | library | Observed | Groups 1 file(s) under render.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| test-utils package | library | Observed | Groups 2 file(s) under test-utils package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 139 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| util.js package | library | Observed | Groups 1 file(s) under util.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/benchmarks.yml` (ci)
- `.github/workflows/build-test.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/pr-reporter.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/run-bench.yml` (ci)
- `.github/workflows/single-bench.yml` (ci)
- `.github/workflows/size.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `compat/mangle.json` (config)
- `compat/package.json` (manifest)
- `debug/mangle.json` (config)
- `debug/package.json` (manifest)
- `demo/package.json` (manifest)
- `demo/tsconfig.json` (config)
- `devtools/mangle.json` (config)
- `devtools/package.json` (manifest)
- `hooks/mangle.json` (config)
- `hooks/package.json` (manifest)
- `jsconfig-lint.json` (config)
- `jsconfig.json` (config)
- `jsx-runtime/mangle.json` (config)
- `jsx-runtime/package.json` (manifest)
- `mangle.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `test-utils/package.json` (manifest)

## Top-level layout

- `compat` — 83 analysed file(s)
- `test` — 59 analysed file(s)
- `demo` — 52 analysed file(s)
- `hooks` — 23 analysed file(s)
- `debug` — 22 analysed file(s)
- `src` — 17 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 12 analysed file(s)
- `devtools` — 7 analysed file(s)
- `jsx-runtime` — 7 analysed file(s)
- `test-utils` — 5 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `config` — 1 analysed file(s)
- `types` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a2e03dbc6a4a239552d43edb6580ecf86886cc39` is the revision these paths and observations refer to.
