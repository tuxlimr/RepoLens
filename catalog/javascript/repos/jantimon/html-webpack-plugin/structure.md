# Project structure: jantimon/html-webpack-plugin

**Analysed commit:** `9e342d2202e18cd37d5ccc1428c46ad049e24733`

**Commit reference:** [9e342d2202e18cd37d5ccc1428c46ad049e24733](https://github.com/jantimon/html-webpack-plugin/commit/9e342d2202e18cd37d5ccc1428c46ad049e24733)

**Tree at this commit:** [jantimon/html-webpack-plugin@9e342d2202e1](https://github.com/jantimon/html-webpack-plugin/tree/9e342d2202e18cd37d5ccc1428c46ad049e24733)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jantimon/html-webpack-plugin |
| Description | Simplifies creation of HTML files to serve your webpack bundles |
| Stars | 10723 |
| Forks | 1284 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `9e342d2202e18cd37d5ccc1428c46ad049e24733` |
| Retrieved at | 2026-11-14T19:12:33.265123+00:00 |
| Files in this snapshot | 138 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    main.yml
  FUNDING.yml
  issue_template.md
  lock.yml
  stale.yml
.husky/  (2 files)
  commit-msg
  pre-commit
docs/  (1 files)
  template-option.md
examples/  (74 files)
  chunk-optimization/  (8 files)
    entryA.js
    entryB.js
    lib-concat.js
    lib-multiply.js
    lib-sum.js
    main.css
    readme.md
    webpack.config.js
  custom-insertion-position/  (4 files)
    example.js
    index.ejs
    readme.md
    webpack.config.js
  custom-template/  (6 files)
    example.js
    main.css
    partial.html
    readme.md
    template.html
    webpack.config.js
  default/  (4 files)
    example.js
    main.css
    readme.md
    webpack.config.js
  favicon/  (4 files)
    example.js
    main.css
    template.html
    webpack.config.js
  html-loader/  (4 files)
    example.js
    main.css
    template.html
    webpack.config.js
  inline/  (5 files)
    example.js
    main.css
    readme.md
    template.pug
    webpack.config.js
  javascript/  (7 files)
    example.js
    main.css
    partial.html
    readme.md
    template.js
    universal.js
    webpack.config.js
  javascript-advanced/  (7 files)
    example.js
    main.css
    partial.html
    readme.md
    template.js
    universal.js
    webpack.config.js
  multi-page/  (5 files)
    first.js
    main.css
    readme.md
    second.js
    webpack.config.js
  pug-loader/  (6 files)
    example.js
    main.css
    readme.md
    template.pug
    time.pug
    webpack.config.js
  sort-manually/  (8 files)
    a.js
    b.js
    c.js
    d.js
    e.js
    main.css
    template.html
    webpack.config.js
  template-parameters/  (4 files)
    example.js
    index.ejs
    readme.md
    webpack.config.js
  README.md
  build-examples.js
lib/  (7 files)
  cached-child-compiler.js
  child-compiler.js
  chunksorter.js
  errors.js
  hooks.js
  html-tags.js
  loader.js
spec/  (27 files)
  fixtures/  (23 files)
    src/  (1 files)
      … 1 files under this directory
    async.js
    common.js
    empty.html
    empty_html.html
    html-template-with-image.html
    index.js
    interpolation.html
    invalid.html
    logo.html
    main.css
    plain.html
    spaced_plain.html
    template-partial.hbs
    template.ejs
    template.hbs
    template.pug
    templateParam.cjs
    templateParam.js
    test.html
    theme.js
    util.js
    webpackconfig.html
  basic.spec.js
  caching.spec.js
  example.spec.js
  hot.spec.js
.cspell.json
.editorconfig
.eslintrc.js
.gitignore
.mailmap
.node-version
.prettierignore
CHANGELOG.md
LICENSE
README.md
commitlint.config.js
default_index.ejs
flow.puml
index.js
lint-staged.config.js
logs
migration.md
package.json
tsconfig.json
typings.d.ts
```

## Entry points

- [index.js](https://github.com/jantimon/html-webpack-plugin/blob/9e342d2202e18cd37d5ccc1428c46ad049e24733/index.js)
- [spec/fixtures/index.js](https://github.com/jantimon/html-webpack-plugin/blob/9e342d2202e18cd37d5ccc1428c46ad049e24733/spec/fixtures/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 7 file(s) under lib package (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 11 file(s) under spec package (observed from repository paths and static analysis). |

## Important files

- `.cspell.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/lock.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/main.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `examples` — 74 analysed file(s)
- `spec` — 27 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 7 analysed file(s)
- `lib` — 7 analysed file(s)
- `.husky` — 2 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 49 file(s) were skipped during inventory (49 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9e342d2202e18cd37d5ccc1428c46ad049e24733` is the revision these paths and observations refer to.
