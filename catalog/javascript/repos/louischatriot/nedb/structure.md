# Project structure: louischatriot/nedb

**Analysed commit:** `35be491ca67dbd4c6f75335f5f486307b192f2dc`

**Commit reference:** [35be491ca67dbd4c6f75335f5f486307b192f2dc](https://github.com/louischatriot/nedb/commit/35be491ca67dbd4c6f75335f5f486307b192f2dc)

**Tree at this commit:** [louischatriot/nedb@35be491ca67d](https://github.com/louischatriot/nedb/tree/35be491ca67dbd4c6f75335f5f486307b192f2dc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | louischatriot/nedb |
| Description | The JavaScript Database, for Node.js, nw.js, electron and the browser |
| Stars | 13525 |
| Forks | 1008 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `35be491ca67dbd4c6f75335f5f486307b192f2dc` |
| Retrieved at | 2026-11-14T19:11:55.910211+00:00 |
| Files in this snapshot | 54 |

## Directory tree

```text
benchmarks/  (9 files)
  commonUtilities.js
  ensureIndex.js
  find.js
  findOne.js
  findWithIn.js
  insert.js
  loadDatabase.js
  remove.js
  update.js
browser-version/  (18 files)
  browser-specific/  (2 files)
    lib/  (2 files)
      … 2 files under this directory
  test/  (14 files)
    async.js
    chai.js
    index.html
    localforage.js
    mocha.css
    mocha.js
    nedb-browser.js
    playground.html
    testLoad.html
    testLoad.js
    testPersistence.html
    testPersistence.js
    testPersistence2.html
    testPersistence2.js
  build.js
  package.json
lib/  (8 files)
  cursor.js
  customUtils.js
  datastore.js
  executor.js
  indexes.js
  model.js
  persistence.js
  storage.js
test/  (8 files)
  cursor.test.js
  customUtil.test.js
  db.test.js
  executor.test.js
  indexes.test.js
  mocha.opts
  model.test.js
  persistence.test.js
test_lac/  (5 files)
  loadAndCrash.test.js
  openFds.test.js
  openFdsLaunch.sh
  openFdsTestFile
  openFdsTestFile2
.gitignore
LICENSE
README.md
bower.json
index.js
package.json
```

## Entry points

- [index.js](https://github.com/louischatriot/nedb/blob/35be491ca67dbd4c6f75335f5f486307b192f2dc/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 9 file(s) under benchmarks package (observed from repository paths and static analysis). |
| browser-version package | library | Observed | Groups 3 file(s) under browser-version package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 8 file(s) under lib package (observed from repository paths and static analysis). |
| test_lac package | library | Observed | Groups 3 file(s) under test_lac package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `bower.json` (config)
- `browser-version/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `browser-version` — 18 analysed file(s)
- `benchmarks` — 9 analysed file(s)
- `lib` — 8 analysed file(s)
- `test` — 8 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `test_lac` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `35be491ca67dbd4c6f75335f5f486307b192f2dc` is the revision these paths and observations refer to.
