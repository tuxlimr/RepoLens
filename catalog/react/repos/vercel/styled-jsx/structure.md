# Project structure: vercel/styled-jsx

**Analysed commit:** `a737ac442a9d032f9f824050b23dc9b6d766657e`

**Commit reference:** [a737ac442a9d032f9f824050b23dc9b6d766657e](https://github.com/vercel/styled-jsx/commit/a737ac442a9d032f9f824050b23dc9b6d766657e)

**Tree at this commit:** [vercel/styled-jsx@a737ac442a9d](https://github.com/vercel/styled-jsx/tree/a737ac442a9d032f9f824050b23dc9b6d766657e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vercel/styled-jsx |
| Description | Full CSS support for JSX without compromises |
| Stars | 7770 |
| Forks | 265 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `a737ac442a9d032f9f824050b23dc9b6d766657e` |
| Retrieved at | 2026-11-14T19:13:46.190237+00:00 |
| Files in this snapshot | 107 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    main.yml
    prs.yml
  ISSUE_TEMPLATE.md
lib/  (2 files)
  style-transform.js
  stylesheet.js
src/  (14 files)
  lib/  (3 files)
    hash.js
    style-transform.js
    stylesheet.js
  .babelrc
  _constants.js
  _utils.js
  babel-external.js
  babel-test.js
  babel.js
  index.js
  macro.js
  style.js
  stylesheet-registry.js
  webpack.js
test/  (66 files)
  __snapshots__/  (6 files)
    attribute.js.snap
    external.js.snap
    index.js.snap
    macro.js.snap
    plugins.js.snap
    styles.js.snap
  fixtures/  (40 files)
    plugins/  (5 files)
      … 5 files under this directory
    absent.js
    attribute-generation-classname-rewriting.js
    attribute-generation-modes.js
    class.js
    component-attribute.js
    conflicts.js
    css-tag-same-file.js
    different-jsx-ids.js
    dynamic-element-class.js
    dynamic-element-external.js
    dynamic-element.js
    dynamic-this-value-in-arrow.js
    expressions.js
    external-stylesheet-global.js
    external-stylesheet-multi-line.js
    external-stylesheet.js
    fragment.js
    global.js
    ignore.js
    macro.js
    mixed-global-scoped.js
    multiple-jsx.js
    nested-style-tags.js
    non-styled-jsx-style.js
    … 11 more files
  helpers/  (2 files)
    babel-test.macro.js
    with-mock.js
  snapshots/  (6 files)
    attribute.js.md
    external.js.md
    index.js.md
    macro.js.md
    plugins.js.md
    styles.js.md
  .babelrc
  _read.js
  _transform.js
  attribute.js
  external.js
  index.js
  index.ts
  macro.js
  plugins.js
  styles.js
  stylesheet-registry.js
  stylesheet.js
.eslintignore
.gitignore
.prettierrc.json
CODEOWNERS
Changelog.md
babel-test.js
babel.js
css.d.ts
css.js
global.d.ts
index.d.ts
index.js
license.md
macro.d.ts
macro.js
package.json
pnpm-workspace.yaml
readme.md
style.d.ts
style.js
tsconfig.json
webpack.js
```

## Entry points

- [index.js](https://github.com/vercel/styled-jsx/blob/a737ac442a9d032f9f824050b23dc9b6d766657e/index.js)
- [src/index.js](https://github.com/vercel/styled-jsx/blob/a737ac442a9d032f9f824050b23dc9b6d766657e/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| babel-external.js package | library | Observed | Groups 1 file(s) under babel-external.js package (observed from repository paths and static analysis). |
| babel.js package | library | Observed | Groups 1 file(s) under babel.js package (observed from repository paths and static analysis). |
| babel-test.js package | library | Observed | Groups 1 file(s) under babel-test.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| _constants.js package | library | Observed | Groups 1 file(s) under _constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 12 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 5 file(s) under lib package (observed from repository paths and static analysis). |
| macro.js package | library | Observed | Groups 1 file(s) under macro.js package (observed from repository paths and static analysis). |
| style.js package | library | Observed | Groups 1 file(s) under style.js package (observed from repository paths and static analysis). |
| stylesheet-registry.js package | library | Observed | Groups 1 file(s) under stylesheet-registry.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 66 file(s) under tests (observed from repository paths and static analysis). |
| _utils.js package | library | Observed | Groups 1 file(s) under _utils.js package (observed from repository paths and static analysis). |
| webpack.js package | library | Observed | Groups 1 file(s) under webpack.js package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/main.yml` (ci)
- `.github/workflows/prs.yml` (ci)
- `.prettierrc.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 66 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `src` — 14 analysed file(s)
- `.github` — 3 analysed file(s)
- `lib` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a737ac442a9d032f9f824050b23dc9b6d766657e` is the revision these paths and observations refer to.
