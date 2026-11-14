# Project structure: goofychris/art-template

**Analysed commit:** `d09a96dd85ef3671286157d8a0c75948b90a3ebb`

**Commit reference:** [d09a96dd85ef3671286157d8a0c75948b90a3ebb](https://github.com/goofychris/art-template/commit/d09a96dd85ef3671286157d8a0c75948b90a3ebb)

**Tree at this commit:** [goofychris/art-template@d09a96dd85ef](https://github.com/goofychris/art-template/tree/d09a96dd85ef3671286157d8a0c75948b90a3ebb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | goofychris/art-template |
| Description | High performance JavaScript templating engine |
| Stars | 9835 |
| Forks | 2631 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d09a96dd85ef3671286157d8a0c75948b90a3ebb` |
| Retrieved at | 2026-11-14T19:12:49.556514+00:00 |
| Files in this snapshot | 104 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE.md
example/  (33 files)
  node-include/  (4 files)
    footer.art
    header.art
    index.art
    index.js
  node-layout/  (7 files)
    nested-block/  (4 files)
      … 4 files under this directory
    index.art
    index.js
    layout.art
  web-art-syntax/  (8 files)
    basic.html
    compile-error.html
    compile.html
    filter.html
    include.html
    no-escape.html
    print.html
    runtime-error.html
  web-ie-compatible/  (1 files)
    index.html
  web-native-syntax/  (8 files)
    basic.html
    compile-error.html
    compile.html
    filter.html
    include.html
    no-escape.html
    print.html
    runtime-error.html
  web-requirejs/  (2 files)
    index.html
    require.js
  web-test-speed/  (3 files)
    js/  (2 files)
      … 2 files under this directory
    index.html
lib/  (1 files)
  template-web.js
src/  (22 files)
  compile/  (16 files)
    adapter/  (9 files)
      … 9 files under this directory
    compiler.js
    defaults.js
    error.js
    es-tokenizer.js
    index.js
    runtime.js
    tpl-tokenizer.js
  defaults.js
  extension.js
  index.js
  precompile.js
  render.js
  runtime.js
test/  (33 files)
  compile/  (13 files)
    adapter/  (7 files)
      … 7 files under this directory
    compiler.js
    defaults.js
    es-tokenizer.js
    index.js
    runtime.js
    tpl-tokenizer.js
  res/  (18 files)
    extend-options/  (3 files)
      … 3 files under this directory
    index/  (2 files)
      … 2 files under this directory
    nested-block/  (4 files)
      … 4 files under this directory
    extension.compile-error.2.tpl
    extension.compile-error.tpl
    extension.file.html
    extension.file.tpl
    extension.runtime-error.2.tpl
    extension.runtime-error.tpl
    file.art
    file.html
    template.file.html
  index.js
  node.js
.babelrc
.editorconfig
.eslintignore
.eslintrc.json
.gitignore
.prettierrc
.travis.yml
CHANGELOG.md
LICENSE
README.md
index.d.ts
index.js
package.json
webpack.config.js
```

## Entry points

- [index.js](https://github.com/goofychris/art-template/blob/d09a96dd85ef3671286157d8a0c75948b90a3ebb/index.js)
- [src/compile/index.js](https://github.com/goofychris/art-template/blob/d09a96dd85ef3671286157d8a0c75948b90a3ebb/src/compile/index.js)
- [src/index.js](https://github.com/goofychris/art-template/blob/d09a96dd85ef3671286157d8a0c75948b90a3ebb/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| compile package | library | Observed | Groups 16 file(s) under compile package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| defaults.js package | library | Observed | Groups 1 file(s) under defaults.js package (observed from repository paths and static analysis). |
| extension.js package | library | Observed | Groups 1 file(s) under extension.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 1 file(s) under lib package (observed from repository paths and static analysis). |
| precompile.js package | library | Observed | Groups 1 file(s) under precompile.js package (observed from repository paths and static analysis). |
| render.js package | library | Observed | Groups 1 file(s) under render.js package (observed from repository paths and static analysis). |
| runtime.js package | library | Observed | Groups 1 file(s) under runtime.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 33 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `example` — 33 analysed file(s)
- `test` — 33 analysed file(s)
- `src` — 22 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 1 analysed file(s)
- `lib` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d09a96dd85ef3671286157d8a0c75948b90a3ebb` is the revision these paths and observations refer to.
