# Project structure: immerjs/immer

**Analysed commit:** `784c86bb234e805566481c9425fcb2a3897e8bcc`

**Commit reference:** [784c86bb234e805566481c9425fcb2a3897e8bcc](https://github.com/immerjs/immer/commit/784c86bb234e805566481c9425fcb2a3897e8bcc)

**Tree at this commit:** [immerjs/immer@784c86bb234e](https://github.com/immerjs/immer/tree/784c86bb234e805566481c9425fcb2a3897e8bcc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | immerjs/immer |
| Description | Create the next immutable state by mutating the current one |
| Stars | 29003 |
| Forks | 909 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `784c86bb234e805566481c9425fcb2a3897e8bcc` |
| Retrieved at | 2026-11-14T19:10:48.766282+00:00 |
| Files in this snapshot | 158 |

## Directory tree

```text
.codesandbox/  (1 files)
  ci.json
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.md
    feature.md
    question.md
  workflows/  (3 files)
    docs-public.yml
    release.yml
    test.yml
  FUNDING.yml
  lock.yml
.vscode/  (2 files)
  launch.json
  settings.json
__performance_tests__/  (5 files)
  add-data.mjs
  incremental.mjs
  large-obj.mjs
  measure.mjs
  todo.mjs
__tests__/  (43 files)
  __prod_snapshots__/  (7 files)
    base.js.snap
    curry.js.snap
    frozen.js.snap
    manual.js.snap
    patch.js.snap
    plugins.js.snap
    readme.js.snap
  __snapshots__/  (7 files)
    base.js.snap
    curry.js.snap
    frozen.js.snap
    manual.js.snap
    patch.js.snap
    plugins.js.snap
    readme.js.snap
  flow/  (2 files)
    .flowconfig
    flow.js.flow
  array-methods-filter-length.js
  base.js
  current.js
  curry.js
  draft.ts
  empty.ts
  frozen.js
  immutable.ts
  isDraftable.js
  isModified.js
  manual.js
  map-set.js
  not-strict-copy.ts
  null.js
  original.js
  patch.js
  plugins.js
  produce.ts
  prototype-inspection.js
  readme.js
  redux.ts
  regressions.js
  spec_ts.ts
  test-data.json
  … 3 more files
_site/  (3 files)
  .github/  (2 files)
    ISSUE_TEMPLATE/  (2 files)
      … 2 files under this directory
  readme/  (1 files)
    index.html
images/  (1 files)
  immer-logo.svg
perf-testing/  (7 files)
  .gitignore
  README.md
  immutability-benchmarks.mjs
  immutability-profiling.mjs
  package.json
  read-cpuprofile.js
  rolldown.config.js
src/  (18 files)
  core/  (5 files)
    current.ts
    finalize.ts
    immerClass.ts
    proxy.ts
    scope.ts
  plugins/  (3 files)
    arrayMethods.ts
    mapset.ts
    patches.ts
  types/  (4 files)
    globals.d.ts
    index.js.flow
    types-external.ts
    types-internal.ts
  utils/  (4 files)
    common.ts
    env.ts
    errors.ts
    plugins.ts
  immer.ts
  internal.ts
website/  (57 files)
  docs/  (24 files)
    api.md
    array-methods.md
    async.mdx
    built-with.md
    complex-objects.md
    current.md
    curried-produce.mdx
    example-setstate.mdx
    faq.md
    freezing.mdx
    installation.mdx
    introduction.md
    map-set.md
    original.md
    other-lang.md
    patches.mdx
    performance.mdx
    pitfalls.md
    produce.mdx
    resources.md
    return.mdx
    support.md
    typescript.mdx
    update-patterns.md
  i18n/  (27 files)
    zh-CN/  (27 files)
      … 27 files under this directory
  src/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  static/  (2 files)
    img/  (1 files)
      … 1 files under this directory
    .nojekyll
  docusaurus.config.js
  package.json
  sidebars.js
.coveralls.yml
.gitignore
.prettierrc
.watchmanconfig
LICENSE
SECURITY.md
package.json
readme.md
tsconfig.json
tsup.config.ts
vitest-custom-reporter.ts
vitest.config.build.ts
vitest.config.ts
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| immer.ts package | library | Observed | Groups 1 file(s) under immer.ts package (observed from repository paths and static analysis). |
| internal.ts package | library | Observed | Groups 1 file(s) under internal.ts package (observed from repository paths and static analysis). |
| perf-testing package | library | Observed | Groups 4 file(s) under perf-testing package (observed from repository paths and static analysis). |
| __performance_tests__ package | library | Observed | Groups 5 file(s) under __performance_tests__ package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 3 file(s) under plugins package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 25 file(s) under __tests__ package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 3 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 2 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.codesandbox/ci.json` (config)
- `.coveralls.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/lock.yml` (config)
- `.github/workflows/docs-public.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `__tests__/test-data.json` (config)
- `__tests__/tsconfig.json` (config)
- `package.json` (manifest)
- `perf-testing/package.json` (manifest)
- `tsconfig.json` (config)
- `website/i18n/zh-CN/docusaurus-plugin-content-docs/current.json` (config)
- `website/i18n/zh-CN/docusaurus-theme-classic/footer.json` (config)
- `website/i18n/zh-CN/docusaurus-theme-classic/navbar.json` (config)
- `website/package.json` (manifest)

## Top-level layout

- `website` — 57 analysed file(s)
- `__tests__` — 43 analysed file(s)
- `src` — 18 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 8 analysed file(s)
- `perf-testing` — 7 analysed file(s)
- `__performance_tests__` — 5 analysed file(s)
- `_site` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.codesandbox` — 1 analysed file(s)
- `images` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `784c86bb234e805566481c9425fcb2a3897e8bcc` is the revision these paths and observations refer to.
