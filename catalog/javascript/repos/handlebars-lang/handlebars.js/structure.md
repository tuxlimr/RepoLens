# Project structure: handlebars-lang/handlebars.js

**Analysed commit:** `13a7a679910d2adbfe7f6fad61ce8f98426b0378`

**Commit reference:** [13a7a679910d2adbfe7f6fad61ce8f98426b0378](https://github.com/handlebars-lang/handlebars.js/commit/13a7a679910d2adbfe7f6fad61ce8f98426b0378)

**Tree at this commit:** [handlebars-lang/handlebars.js@13a7a679910d](https://github.com/handlebars-lang/handlebars.js/tree/13a7a679910d2adbfe7f6fad61ce8f98426b0378)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | handlebars-lang/handlebars.js |
| Description | Minimal templating on steroids. |
| Stars | 18692 |
| Forks | 2080 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `13a7a679910d2adbfe7f6fad61ce8f98426b0378` |
| Retrieved at | 2026-11-14T19:11:20.747600+00:00 |
| Files in this snapshot | 143 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (2 files)
    ci.yml
    release.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
bin/  (1 files)
  handlebars.js
components/  (7 files)
  lib/  (1 files)
    handlebars/  (1 files)
      … 1 files under this directory
  bower.json
  component.json
  composer.json
  handlebars-source.gemspec
  handlebars.js.nuspec
  package.json
docs/  (2 files)
  compiler-api.md
  decorators-api.md
lib/  (28 files)
  handlebars/  (24 files)
    compiler/  (6 files)
      … 6 files under this directory
    decorators/  (1 files)
      … 1 files under this directory
    helpers/  (7 files)
      … 7 files under this directory
    internal/  (2 files)
      … 2 files under this directory
    base.js
    decorators.js
    helpers.js
    logger.js
    no-conflict.js
    runtime.js
    safe-string.js
    utils.js
  handlebars.js
  handlebars.runtime.js
  index.js
  precompiler.js
spec/  (36 files)
  artifacts/  (7 files)
    bom.handlebars
    empty.handlebars
    example_1.handlebars
    example_2.hbs
    known.helpers.handlebars
    non.default.extension.hbs
    partial.template.handlebars
  env/  (5 files)
    browser-vitest-pre.js
    browser-vitest.js
    browser.js
    common.js
    node.js
  expected/  (3 files)
    compiled.string.txt
    empty.namespace.js
    help.menu.txt
  tmp/  (1 files)
    .gitkeep
  ast.js
  basic.js
  blocks.js
  builtins.js
  compiler.js
  data.js
  helpers.js
  index.html
  javascript-compiler.js
  partials.js
  precompiler.js
  regressions.js
  runtime.js
  security.js
  source-map.js
  spec.js
  strict.js
  subexpressions.js
  utils.js
  whitespace-control.js
tasks/  (8 files)
  tests/  (5 files)
    README.md
    cli.test.js
    fake-s3.js
    git.test.js
    publish-to-aws.test.js
  util/  (1 files)
    git.js
  publish-to-aws.js
  version.js
tests/  (33 files)
  bench/  (5 files)
    compare.js
    perf.js
    report.js
    size.js
    templates.js
  browser/  (3 files)
    tests/  (1 files)
      … 1 files under this directory
    README.md
    playwright.config.js
  integration/  (23 files)
    multi-nodejs-test/  (5 files)
      … 5 files under this directory
    rollup-test/  (5 files)
      … 5 files under this directory
    webpack-test/  (11 files)
      … 11 files under this directory
    README.md
    run-integration-tests.sh
  rspack/  (1 files)
    rspack.test.js
  print-script.js
types/  (3 files)
  __typetests__/  (1 files)
    handlebars.tst.ts
  index.d.ts
  tsconfig.json
.editorconfig
.git-blame-ignore-revs
.gitattributes
.gitignore
.gitmodules
.oxfmtrc.json
.oxlintrc.json
CONTRIBUTING.md
FAQ.md
LICENSE
README.md
SECURITY.md
eslint.config.js
package.json
pnpm-workspace.yaml
release-notes.md
rspack.config.js
runtime.d.ts
runtime.js
vitest.config.js
```

## Entry points

- [lib/index.js](https://github.com/handlebars-lang/handlebars.js/blob/13a7a679910d2adbfe7f6fad61ce8f98426b0378/lib/index.js)
- [bin/handlebars.js](https://github.com/handlebars-lang/handlebars.js/blob/13a7a679910d2adbfe7f6fad61ce8f98426b0378/bin/handlebars.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 1 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 28 file(s) under lib package (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 25 file(s) under spec package (observed from repository paths and static analysis). |
| tasks package | library | Observed | Groups 3 file(s) under tasks package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 38 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 2 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `components/bower.json` (config)
- `components/component.json` (config)
- `components/composer.json` (config)
- `components/package.json` (manifest)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `types/tsconfig.json` (config)

## Top-level layout

- `spec` — 36 analysed file(s)
- `tests` — 33 analysed file(s)
- `lib` — 28 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `tasks` — 8 analysed file(s)
- `components` — 7 analysed file(s)
- `.github` — 5 analysed file(s)
- `types` — 3 analysed file(s)
- `docs` — 2 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `13a7a679910d2adbfe7f6fad61ce8f98426b0378` is the revision these paths and observations refer to.
