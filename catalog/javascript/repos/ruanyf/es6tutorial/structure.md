# Project structure: ruanyf/es6tutorial

**Analysed commit:** `d27a751258f25cb4d27de70161d3bcd7fe19251e`

**Commit reference:** [d27a751258f25cb4d27de70161d3bcd7fe19251e](https://github.com/ruanyf/es6tutorial/commit/d27a751258f25cb4d27de70161d3bcd7fe19251e)

**Tree at this commit:** [ruanyf/es6tutorial@d27a751258f2](https://github.com/ruanyf/es6tutorial/tree/d27a751258f25cb4d27de70161d3bcd7fe19251e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ruanyf/es6tutorial |
| Description | 《ECMAScript 6入门》是一本开源的 JavaScript 语言教程，全面介绍 ECMAScript 6 新增的语法特性。 |
| Stars | 21409 |
| Forks | 8813 |
| Licence | Other |
| Language | JavaScript |
| Default branch | gh-pages |
| Analysed commit | `d27a751258f25cb4d27de70161d3bcd7fe19251e` |
| Retrieved at | 2026-11-14T19:11:10.781538+00:00 |
| Files in this snapshot | 274 |

## Directory tree

```text
app/  (221 files)
  bower_components/  (221 files)
    marked/  (216 files)
      … 216 files under this directory
    normalize-css/  (5 files)
      … 5 files under this directory
css/  (1 files)
  app.css
docs/  (37 files)
  acknowledgment.md
  array.md
  arraybuffer.md
  async-iterator.md
  async.md
  class-extends.md
  class.md
  decorator.md
  destructuring.md
  fp.md
  function.md
  generator-async.md
  generator.md
  intro.md
  iterator.md
  let.md
  mixin.md
  module-loader.md
  module.md
  number.md
  object-methods.md
  object.md
  operator.md
  promise.md
  … 13 more files
js/  (4 files)
  ditto.js
  marked.js
  prism.js
  store.js
.gitignore
.nojekyll
404.html
CNAME
LICENSE
README.md
SUMMARY.md
book.json
config.js
index.html
sidebar.md
```

## Entry points

- [app/bower_components/marked/lib/marked.js](https://github.com/ruanyf/es6tutorial/blob/d27a751258f25cb4d27de70161d3bcd7fe19251e/app/bower_components/marked/lib/marked.js)
- [app/bower_components/marked/bin/marked](https://github.com/ruanyf/es6tutorial/blob/d27a751258f25cb4d27de70161d3bcd7fe19251e/app/bower_components/marked/bin/marked)
- [app/bower_components/marked/index.js](https://github.com/ruanyf/es6tutorial/blob/d27a751258f25cb4d27de70161d3bcd7fe19251e/app/bower_components/marked/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 2 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 4 file(s) under js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 201 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `app/bower_components/marked/.bower.json` (config)
- `app/bower_components/marked/.travis.yml` (ci)
- `app/bower_components/marked/component.json` (config)
- `app/bower_components/marked/package.json` (manifest)
- `app/bower_components/normalize-css/.bower.json` (config)
- `app/bower_components/normalize-css/bower.json` (config)
- `book.json` (config)

## Top-level layout

- `app` — 221 analysed file(s)
- `docs` — 37 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `js` — 4 analysed file(s)
- `css` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d27a751258f25cb4d27de70161d3bcd7fe19251e` is the revision these paths and observations refer to.
