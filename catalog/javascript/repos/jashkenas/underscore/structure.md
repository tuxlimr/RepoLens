# Project structure: jashkenas/underscore

**Analysed commit:** `5c1e5f686f8500af9c9d15614ed60289d6d35d6b`

**Commit reference:** [5c1e5f686f8500af9c9d15614ed60289d6d35d6b](https://github.com/jashkenas/underscore/commit/5c1e5f686f8500af9c9d15614ed60289d6d35d6b)

**Tree at this commit:** [jashkenas/underscore@5c1e5f686f85](https://github.com/jashkenas/underscore/tree/5c1e5f686f8500af9c9d15614ed60289d6d35d6b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jashkenas/underscore |
| Description | JavaScript's utility _ belt |
| Stars | 27294 |
| Forks | 5410 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5c1e5f686f8500af9c9d15614ed60289d6d35d6b` |
| Retrieved at | 2026-11-14T19:10:52.080301+00:00 |
| Files in this snapshot | 375 |

## Directory tree

```text
.github/  (3 files)
  config/  (1 files)
    codeql.yml
  workflows/  (1 files)
    codeql-analysis.yml
  FUNDING.yml
docs/  (166 files)
  modules/  (161 files)
    _baseCreate.html
    _baseIteratee.html
    _cb.html
    _chainResult.html
    _collectNonEnumProps.html
    _createAssigner.html
    _createEscaper.html
    _createIndexFinder.html
    _createPredicateIndexFinder.html
    _createReduce.html
    _createSizePropertyCheck.html
    _deepGet.html
    _escapeMap.html
    _executeBound.html
    _flatten.html
    _getByteLength.html
    _getLength.html
    _group.html
    _has.html
    _hasObjectTag.html
    _isArrayLike.html
    _isBufferLike.html
    _keyInObj.html
    _methodFingerprint.html
    … 137 more files
  public/  (1 files)
    stylesheets/  (1 files)
      … 1 files under this directory
  .eslintrc
  docco.css
  linked-esm.jst
  main.js
modules/  (163 files)
  .eslintrc
  _baseCreate.js
  _baseIteratee.js
  _cb.js
  _chainResult.js
  _collectNonEnumProps.js
  _createAssigner.js
  _createEscaper.js
  _createIndexFinder.js
  _createPredicateIndexFinder.js
  _createReduce.js
  _createSizePropertyCheck.js
  _deepGet.js
  _escapeMap.js
  _executeBound.js
  _flatten.js
  _getByteLength.js
  _getLength.js
  _group.js
  _has.js
  _hasObjectTag.js
  _isArrayLike.js
  _isBufferLike.js
  _keyInObj.js
  … 139 more files
patches/  (1 files)
  docco+0.8.0.patch
test/  (12 files)
  .eslintrc
  arrays.js
  chaining.js
  collections.js
  cross-document.js
  functions.js
  index.html
  objects.js
  overrides.js
  qunit-setup.js
  treeshake.js
  utility.js
test-treeshake/  (3 files)
  map.js
  rollup.config.js
  template.js
.editorconfig
.eslintrc
.gitignore
.travis.yml
CNAME
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
bower.json
index.html
karma.conf-sauce.js
karma.conf.js
package.json
rollup.common.js
rollup.config.js
rollup.config2.js
underscore-esm-min.js
underscore-esm.js
underscore-min.js
underscore-node-f.cjs
underscore-node.cjs
underscore-node.mjs
… 3 more files
```

## Entry points

- [underscore-umd.js](https://github.com/jashkenas/underscore/blob/5c1e5f686f8500af9c9d15614ed60289d6d35d6b/underscore-umd.js)
- [modules/index.js](https://github.com/jashkenas/underscore/blob/5c1e5f686f8500af9c9d15614ed60289d6d35d6b/modules/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 14 file(s) under core modules (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 161 file(s) under modules package (observed from repository paths and static analysis). |
| test-treeshake package | library | Observed | Groups 3 file(s) under test-treeshake package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/config/codeql.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.travis.yml` (ci)
- `bower.json` (config)
- `modules/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `docs` — 166 analysed file(s)
- `modules` — 163 analysed file(s)
- `(root files)` — 27 analysed file(s)
- `test` — 12 analysed file(s)
- `.github` — 3 analysed file(s)
- `test-treeshake` — 3 analysed file(s)
- `patches` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5c1e5f686f8500af9c9d15614ed60289d6d35d6b` is the revision these paths and observations refer to.
