# Project structure: gnab/remark

**Analysed commit:** `be58d65d59faca35f6ea3f55aeb8f65ef76305a3`

**Commit reference:** [be58d65d59faca35f6ea3f55aeb8f65ef76305a3](https://github.com/gnab/remark/commit/be58d65d59faca35f6ea3f55aeb8f65ef76305a3)

**Tree at this commit:** [gnab/remark@be58d65d59fa](https://github.com/gnab/remark/tree/be58d65d59faca35f6ea3f55aeb8f65ef76305a3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gnab/remark |
| Description | A simple, in-browser, markdown-driven slideshow tool. |
| Stars | 13002 |
| Forks | 863 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `be58d65d59faca35f6ea3f55aeb8f65ef76305a3` |
| Retrieved at | 2026-11-14T19:12:01.906536+00:00 |
| Files in this snapshot | 62 |

## Directory tree

```text
src/  (33 files)
  remark/  (26 files)
    components/  (4 files)
      … 4 files under this directory
    controllers/  (6 files)
      … 6 files under this directory
    models/  (4 files)
      … 4 files under this directory
    views/  (3 files)
      … 3 files under this directory
    api.js
    converter.js
    dom.js
    lexer.js
    macros.js
    parser.js
    resources.js
    scaler.js
    utils.js
  templates/  (3 files)
    boilerplate-single.html.template
    highlighter.js.template
    resources.js.template
  polyfills.js
  remark.html
  remark.js
  remark.less
test/  (14 files)
  remark/  (11 files)
    components/  (2 files)
      … 2 files under this directory
    controllers/  (1 files)
      … 1 files under this directory
    models/  (2 files)
      … 2 files under this directory
    views/  (2 files)
      … 2 files under this directory
    api_test.js
    converter_test.js
    lexer_test.js
    parser_test.js
  mocha.opts
  runner.html
  test_dom.js
.gitignore
.jshintignore
.jshintrc
.npmignore
.travis.yml
Gruntfile.js
HISTORY.md
LICENSE
Makefile
README.md
boilerplate-local.html
boilerplate-remote.html
bower.json
make.js
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). |
| polyfills.js package | library | Observed | Groups 1 file(s) under polyfills.js package (observed from repository paths and static analysis). |
| remark package | library | Observed | Groups 13 file(s) under remark package (observed from repository paths and static analysis). |
| remark.js package | library | Observed | Groups 1 file(s) under remark.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 33 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `test` — 14 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `be58d65d59faca35f6ea3f55aeb8f65ef76305a3` is the revision these paths and observations refer to.
