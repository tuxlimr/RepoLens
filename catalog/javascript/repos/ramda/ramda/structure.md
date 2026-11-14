# Project structure: ramda/ramda

**Analysed commit:** `f4b2e35ff433e18c751326b82acc3c6ab3585e18`

**Commit reference:** [f4b2e35ff433e18c751326b82acc3c6ab3585e18](https://github.com/ramda/ramda/commit/f4b2e35ff433e18c751326b82acc3c6ab3585e18)

**Tree at this commit:** [ramda/ramda@f4b2e35ff433](https://github.com/ramda/ramda/tree/f4b2e35ff433e18c751326b82acc3c6ab3585e18)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ramda/ramda |
| Description | :ram: Practical functional Javascript |
| Stars | 24051 |
| Forks | 1457 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f4b2e35ff433e18c751326b82acc3c6ab3585e18` |
| Retrieved at | 2026-11-14T19:11:03.741384+00:00 |
| Files in this snapshot | 713 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    build.yml
    coverage.yml
  FUNDING.yml
lib/  (27 files)
  bench/  (17 files)
    concat.bench.js
    curry.bench.js
    each.bench.js
    either.bench.js
    filter-where.bench.js
    filter.bench.js
    find-where.bench.js
    find.bench.js
    findIndex-where.bench.js
    findIndex.bench.js
    includes.bench.js
    indexof.bench.js
    map.bench.js
    maxWith.bench.js
    propEq.bench.js
    reduce.bench.js
    uniq.bench.js
  sauce/  (10 files)
    android.js
    apple.js
    browsers.js
    conf.js
    ie8-shim.js
    ios.js
    linux.js
    mocharun.js
    server.js
    windows.js
scripts/  (11 files)
  transpile/  (2 files)
    esm-to-cjs.js
    wrap-constructor-pattern.js
  BOOKMARKLET.tmpl.md
  addModulePackageScope.js
  beforePublish.js
  benchRunner
  bookmarklet
  bookmarklet.tmpl.js
  doc-blob
  partialBuild.js
  prepublish
source/  (370 files)
  internal/  (97 files)
    _Set.js
    _aperture.js
    _arity.js
    _arrayFromIterator.js
    _arrayReduce.js
    _assertPromise.js
    _assoc.js
    _chain.js
    _checkForMethod.js
    _clone.js
    _cloneRegExp.js
    _complement.js
    _concat.js
    _createPartialApplicator.js
    _createReduce.js
    _curry1.js
    _curry2.js
    _curry3.js
    _curryN.js
    _dispatchable.js
    _dissoc.js
    _dropLast.js
    _dropLastWhile.js
    _equals.js
    … 73 more files
  F.js
  T.js
  __.js
  add.js
  addIndex.js
  addIndexRight.js
  adjust.js
  all.js
  allPass.js
  always.js
  and.js
  andThen.js
  any.js
  anyPass.js
  ap.js
  aperture.js
  append.js
  apply.js
  applySpec.js
  applyTo.js
  ascend.js
  ascendNatural.js
  assoc.js
  assocPath.js
  … 249 more files
test/  (281 files)
  helpers/  (2 files)
    listXf.js
    test.examplesRunner.js
  internal/  (3 files)
    _curry2.js
    _curry3.js
    _isArrayLike.js
  shared/  (4 files)
    Id.js
    Maybe.js
    Pair.js
    eq.js
  F.js
  T.js
  add.js
  addIndex.js
  addIndexRight.js
  adjust.js
  all.js
  allPass.js
  always.js
  and.js
  andThen.js
  any.js
  anyPass.js
  ap.js
  aperture.js
  append.js
  apply.js
  applySpec.js
  applyTo.js
  ascend.js
  ascendNatural.js
  assoc.js
  assocPath.js
  binary.js
  … 248 more files
.babelrc
.codeclimate.yml
.editorconfig
.eslintignore
.eslintrc
.gitattributes
.gitignore
BOOKMARKLET.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE.txt
Makefile
README.md
SECURITY.md
bower.json
egg.json
mod.ts
package.json
repl
rollup.config.js
testem.json
```

## Entry points

- [lib/sauce/server.js](https://github.com/ramda/ramda/blob/f4b2e35ff433e18c751326b82acc3c6ab3585e18/lib/sauce/server.js)
- [source/index.js](https://github.com/ramda/ramda/blob/f4b2e35ff433e18c751326b82acc3c6ab3585e18/source/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 27 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| source package | library | Observed | Groups 370 file(s) under source package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 281 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/coverage.yml` (ci)
- `bower.json` (config)
- `egg.json` (config)
- `package.json` (manifest)
- `testem.json` (config)

## Top-level layout

- `source` — 370 analysed file(s)
- `test` — 281 analysed file(s)
- `lib` — 27 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `scripts` — 11 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f4b2e35ff433e18c751326b82acc3c6ab3585e18` is the revision these paths and observations refer to.
