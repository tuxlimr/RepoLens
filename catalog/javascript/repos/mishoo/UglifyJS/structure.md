# Project structure: mishoo/UglifyJS

**Analysed commit:** `111746bbae5f55c88e3b82b42f14fd0f3129ea53`

**Commit reference:** [111746bbae5f55c88e3b82b42f14fd0f3129ea53](https://github.com/mishoo/UglifyJS/commit/111746bbae5f55c88e3b82b42f14fd0f3129ea53)

**Tree at this commit:** [mishoo/UglifyJS@111746bbae5f](https://github.com/mishoo/UglifyJS/tree/111746bbae5f55c88e3b82b42f14fd0f3129ea53)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mishoo/UglifyJS |
| Description |  JavaScript parser / mangler / compressor / beautifier toolkit |
| Stars | 13365 |
| Forks | 1223 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `111746bbae5f55c88e3b82b42f14fd0f3129ea53` |
| Retrieved at | 2026-11-14T19:11:58.025128+00:00 |
| Files in this snapshot | 278 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (4 files)
    build.yml
    ci.yml
    moz.yml
    ufuzz.yml
bin/  (1 files)
  uglifyjs
lib/  (10 files)
  ast.js
  minify.js
  mozilla-ast.js
  output.js
  parse.js
  propmangle.js
  scope.js
  sourcemap.js
  transform.js
  utils.js
test/  (251 files)
  compress/  (125 files)
    annotations.js
    arguments.js
    arrays.js
    arrows.js
    asm.js
    assignments.js
    awaits.js
    bigint.js
    blocks.js
    booleans.js
    classes.js
    comparisons.js
    concat-strings.js
    conditionals.js
    const.js
    dead-code.js
    debugger.js
    default-values.js
    destructured.js
    directives.js
    drop-console.js
    drop-unused.js
    evaluate.js
    exponentiation.js
    … 101 more files
  input/  (74 files)
    comments/  (1 files)
      … 1 files under this directory
    enclose/  (1 files)
      … 1 files under this directory
    global_defs/  (2 files)
      … 2 files under this directory
    invalid/  (29 files)
      … 29 files under this directory
    issue-1236/  (1 files)
      … 1 files under this directory
    issue-1242/  (4 files)
      … 4 files under this directory
    issue-1323/  (1 files)
      … 1 files under this directory
    issue-1431/  (1 files)
      … 1 files under this directory
    issue-1482/  (4 files)
      … 4 files under this directory
    issue-1632/  (1 files)
      … 1 files under this directory
    issue-2082/  (1 files)
      … 1 files under this directory
    issue-2310/  (1 files)
      … 1 files under this directory
    issue-3040/  (2 files)
      … 2 files under this directory
    issue-3294/  (2 files)
      … 2 files under this directory
    issue-3315/  (2 files)
      … 2 files under this directory
    issue-3441/  (1 files)
      … 1 files under this directory
    issue-505/  (2 files)
      … 2 files under this directory
    issue-520/  (2 files)
      … 2 files under this directory
    module/  (2 files)
      … 2 files under this directory
    reduce/  (13 files)
      … 13 files under this directory
    rename/  (1 files)
      … 1 files under this directory
  mocha/  (25 files)
    arguments.js
    awaits.js
    bug-report.js
    cli.js
    comments.js
    directives.js
    exports.js
    getter-setter.js
    glob.js
    imports.js
    let.js
    line-endings.js
    minify-file-map.js
    minify.js
    number-literal.js
    operator.js
    parentheses.js
    reduce.js
    sourcemaps.js
    spidermonkey.js
    string-literal.js
    templates.js
    tokens.js
    with.js
    … 1 more files
  release/  (13 files)
    acorn.sh
    benchmark.js
    bootstrap.sh
    buble.sh
    butternut.sh
    install.sh
    jetstream.js
    mathjs.sh
    rollup-es.sh
    rollup-ts.sh
    run.js
    sucrase.sh
    web-tooling-benchmark.sh
  ufuzz/  (4 files)
    actions.js
    index.js
    job.js
    options.json
  benchmark.js
  compress.js
  exports.js
  fetch.js
  jetstream.js
  mocha.js
  mozilla-ast.js
  node.js
  reduce.js
  sandbox.js
tools/  (5 files)
  domprops.html
  domprops.json
  exports.js
  node.js
  tty.js
.gitattributes
.gitignore
CONTRIBUTING.md
LICENSE
README.md
package.json
```

## Entry points

- [tools/node.js](https://github.com/mishoo/UglifyJS/blob/111746bbae5f55c88e3b82b42f14fd0f3129ea53/tools/node.js)
- [bin/uglifyjs](https://github.com/mishoo/UglifyJS/blob/111746bbae5f55c88e3b82b42f14fd0f3129ea53/bin/uglifyjs)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 10 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 251 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 3 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/build.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/moz.yml` (ci)
- `.github/workflows/ufuzz.yml` (ci)
- `package.json` (manifest)
- `tools/domprops.json` (config)

## Top-level layout

- `test` — 251 analysed file(s)
- `lib` — 10 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `tools` — 5 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `111746bbae5f55c88e3b82b42f14fd0f3129ea53` is the revision these paths and observations refer to.
