# Project structure: janl/mustache.js

**Analysed commit:** `972fd2b27a036888acfcb60d6119317744fac7ee`

**Commit reference:** [972fd2b27a036888acfcb60d6119317744fac7ee](https://github.com/janl/mustache.js/commit/972fd2b27a036888acfcb60d6119317744fac7ee)

**Tree at this commit:** [janl/mustache.js@972fd2b27a03](https://github.com/janl/mustache.js/tree/972fd2b27a036888acfcb60d6119317744fac7ee)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | janl/mustache.js |
| Description | Minimal templating with {{mustaches}} in JavaScript |
| Stars | 16723 |
| Forks | 2336 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `972fd2b27a036888acfcb60d6119317744fac7ee` |
| Retrieved at | 2026-11-14T19:11:30.313238+00:00 |
| Files in this snapshot | 249 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    usage.yml
    verify.yml
bin/  (1 files)
  mustache
scripts/  (1 files)
  bump-version-in-source
spec/  (3 files)
  _files/  (3 files)
    bom_as_whitespace.js
    bom_as_whitespace.mustache
    bom_as_whitespace.txt
test/  (219 files)
  _files/  (199 files)
    ampersand_escape.js
    ampersand_escape.mustache
    ampersand_escape.txt
    apostrophe.js
    apostrophe.mustache
    apostrophe.txt
    array_of_strings.js
    array_of_strings.mustache
    array_of_strings.txt
    avoids_obj_prototype_in_view_cache.js
    avoids_obj_prototype_in_view_cache.mustache
    avoids_obj_prototype_in_view_cache.txt
    backslashes.js
    backslashes.mustache
    backslashes.txt
    bug_11_eating_whitespace.js
    bug_11_eating_whitespace.mustache
    bug_11_eating_whitespace.txt
    bug_length_property.js
    bug_length_property.mustache
    bug_length_property.txt
    changing_delimiters.js
    changing_delimiters.mustache
    changing_delimiters.txt
    … 175 more files
  module-systems/  (8 files)
    _fixtures/  (2 files)
      … 2 files under this directory
    .eslintrc
    browser-test.js
    commonjs-test.js
    deno-test.ts
    esm-test-exports.mjs
    esm-test.mjs
  .eslintrc
  cli-test.js
  context-test.js
  create-browser-suite.js
  helper.js
  mustache-spec-test.js
  parse-test.js
  partial-test.js
  render-helper.js
  render-test-browser-tmpl.mustache
  render-test.js
  scanner-test.js
wrappers/  (10 files)
  dojo/  (2 files)
    mustache.js.post
    mustache.js.pre
  jquery/  (2 files)
    mustache.js.post
    mustache.js.pre
  mootools/  (2 files)
    mustache.js.post
    mustache.js.pre
  qooxdoo/  (2 files)
    mustache.js.post
    mustache.js.pre
  yui3/  (2 files)
    mustache.js.post
    mustache.js.pre
.eslintrc
.esmrc
.gitignore
.gitmodules
.travis.yml
.zuul.yml
CHANGELOG.md
LICENSE
MIGRATING.md
README.md
Rakefile
mustache.js
package.json
```

## Entry points

- [mustache.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/mustache.js)
- [bin/mustache](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/bin/mustache)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 1 file(s) under spec package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 219 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/usage.yml` (ci)
- `.github/workflows/verify.yml` (ci)
- `.travis.yml` (ci)
- `.zuul.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 219 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `wrappers` — 10 analysed file(s)
- `spec` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `bin` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `972fd2b27a036888acfcb60d6119317744fac7ee` is the revision these paths and observations refer to.
