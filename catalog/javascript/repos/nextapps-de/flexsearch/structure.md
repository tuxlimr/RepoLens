# Project structure: nextapps-de/flexsearch

**Analysed commit:** `f7ed963096a0792da7b2fd63bb7114b3fbac55ed`

**Commit reference:** [f7ed963096a0792da7b2fd63bb7114b3fbac55ed](https://github.com/nextapps-de/flexsearch/commit/f7ed963096a0792da7b2fd63bb7114b3fbac55ed)

**Tree at this commit:** [nextapps-de/flexsearch@f7ed963096a0](https://github.com/nextapps-de/flexsearch/tree/f7ed963096a0792da7b2fd63bb7114b3fbac55ed)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nextapps-de/flexsearch |
| Description | Next-generation full-text search library for Browser and Node.js |
| Stars | 13821 |
| Forks | 527 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f7ed963096a0792da7b2fd63bb7114b3fbac55ed` |
| Retrieved at | 2026-11-14T19:11:49.858053+00:00 |
| Files in this snapshot | 279 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    node.js.yml
  FUNDING.yml
demo/  (1 files)
  autocomplete.html
doc/  (29 files)
  antithesis_logo.svg
  async.md
  bountysource.svg
  context-index.svg
  custom-builds.md
  customization.md
  document-search.md
  encoder-workflow.svg
  encoder.md
  export-import.md
  flexsearch-logo-glass-animated.svg
  flexsearch-logo-glass.svg
  flexsearch-logo.svg
  keystore.md
  liberapay.svg
  memory-comparison.svg
  persistent-clickhouse.md
  persistent-indexeddb.md
  persistent-mongodb.md
  persistent-postgres.md
  persistent-redis.md
  persistent-sqlite.md
  persistent.md
  pipeline.svg
  … 5 more files
example/  (149 files)
  browser-legacy/  (11 files)
    basic/  (1 files)
      … 1 files under this directory
    basic-persistent/  (1 files)
      … 1 files under this directory
    basic-resolver/  (1 files)
      … 1 files under this directory
    basic-suggestion/  (1 files)
      … 1 files under this directory
    basic-worker/  (1 files)
      … 1 files under this directory
    document/  (1 files)
      … 1 files under this directory
    document-highlighting/  (1 files)
      … 1 files under this directory
    document-persistent/  (1 files)
      … 1 files under this directory
    document-resolver/  (1 files)
      … 1 files under this directory
    document-worker/  (1 files)
      … 1 files under this directory
    language-pack/  (1 files)
      … 1 files under this directory
  browser-module/  (16 files)
    basic/  (1 files)
      … 1 files under this directory
    basic-persistent/  (1 files)
      … 1 files under this directory
    basic-resolver/  (1 files)
      … 1 files under this directory
    basic-suggestion/  (1 files)
      … 1 files under this directory
    basic-worker/  (1 files)
      … 1 files under this directory
    basic-worker-extern-config/  (2 files)
      … 2 files under this directory
    document/  (1 files)
      … 1 files under this directory
    document-highlighting/  (1 files)
      … 1 files under this directory
    document-persistent/  (1 files)
      … 1 files under this directory
    document-resolver/  (1 files)
      … 1 files under this directory
    document-worker/  (1 files)
      … 1 files under this directory
    document-worker-extern-config/  (3 files)
      … 3 files under this directory
    language-pack/  (1 files)
      … 1 files under this directory
  nodejs-commonjs/  (63 files)
    .document-worker-persistent/  (5 files)
      … 5 files under this directory
    basic/  (3 files)
      … 3 files under this directory
    basic-export-import/  (3 files)
      … 3 files under this directory
    basic-persistent/  (3 files)
      … 3 files under this directory
    basic-resolver/  (3 files)
      … 3 files under this directory
    basic-suggestion/  (3 files)
      … 3 files under this directory
    basic-worker/  (3 files)
      … 3 files under this directory
    basic-worker-export-import/  (3 files)
      … 3 files under this directory
    basic-worker-extern-config/  (3 files)
      … 3 files under this directory
    document/  (4 files)
      … 4 files under this directory
    document-export-import/  (4 files)
      … 4 files under this directory
    document-persistent/  (4 files)
      … 4 files under this directory
    document-resolver/  (3 files)
      … 3 files under this directory
    document-worker/  (4 files)
      … 4 files under this directory
    document-worker-export-import/  (6 files)
      … 6 files under this directory
    document-worker-extern-config/  (6 files)
      … 6 files under this directory
    language-pack/  (3 files)
      … 3 files under this directory
  nodejs-esm/  (59 files)
    basic/  (3 files)
      … 3 files under this directory
    basic-export-import/  (3 files)
      … 3 files under this directory
    basic-persistent/  (3 files)
      … 3 files under this directory
    basic-resolver/  (3 files)
      … 3 files under this directory
    basic-suggestion/  (3 files)
      … 3 files under this directory
    basic-worker/  (3 files)
      … 3 files under this directory
    basic-worker-export-import/  (3 files)
      … 3 files under this directory
    basic-worker-extern-config/  (4 files)
      … 4 files under this directory
    document/  (4 files)
      … 4 files under this directory
    document-export-import/  (4 files)
      … 4 files under this directory
    document-persistent/  (4 files)
      … 4 files under this directory
    document-resolver/  (3 files)
      … 3 files under this directory
    document-worker/  (4 files)
      … 4 files under this directory
    document-worker-export-import/  (6 files)
      … 6 files under this directory
    document-worker-extern-config/  (6 files)
      … 6 files under this directory
    language-pack/  (3 files)
      … 3 files under this directory
src/  (57 files)
  charset/  (8 files)
    latin/  (4 files)
      … 4 files under this directory
    cjk.js
    exact.js
    normalize.js
    polyfill.js
  db/  (12 files)
    clickhouse/  (2 files)
      … 2 files under this directory
    indexeddb/  (1 files)
      … 1 files under this directory
    mongodb/  (2 files)
      … 2 files under this directory
    postgres/  (2 files)
      … 2 files under this directory
    redis/  (2 files)
      … 2 files under this directory
    sqlite/  (2 files)
      … 2 files under this directory
    interface.js
  document/  (3 files)
    add.js
    highlight.js
    search.js
  index/  (3 files)
    add.js
    remove.js
    search.js
  lang/  (3 files)
    de.js
    en.js
    fr.js
  resolve/  (6 files)
    and.js
    default.js
    handler.js
    not.js
    or.js
    xor.js
  worker/  (4 files)
    handler.js
    node.js
    node.mjs
    worker.js
  async.js
  bundle.js
  cache.js
  charset.js
  common.js
  compress.js
  config.js
  document.js
  encoder.js
  index.js
  intersect.js
  keystore.js
  preset.js
  profiler.js
  resolver.js
  serialize.js
  type.js
  worker.js
task/  (5 files)
  babel.bundle.json
  babel.debug.json
  babel.js
  babel.min.json
  build.js
test/  (27 files)
  misc/  (2 files)
    reporter.js
    runner.js
  .c8rc.json
  async.js
  basic.js
  cache.js
  context.js
  debug.js
  document.js
  document.tag.js
  encoder.js
  highlight.js
  issues.js
  keystore.js
  package.json
  persistent.clickhouse.js
  persistent.js
  persistent.mongo.js
  persistent.postgres.js
  persistent.redis.js
  persistent.sqlite.js
  resolver.js
  scoring.js
  serialize.js
  tokenize.js
  types.ts
  … 1 more files
.gitattributes
.gitignore
CHANGELOG.md
LICENSE
README.md
SECURITY.md
docker-compose.yml
index.d.ts
package.json
```

## Entry points

- [src/db/clickhouse/index.js](https://github.com/nextapps-de/flexsearch/blob/f7ed963096a0792da7b2fd63bb7114b3fbac55ed/src/db/clickhouse/index.js)
- [src/db/mongodb/index.js](https://github.com/nextapps-de/flexsearch/blob/f7ed963096a0792da7b2fd63bb7114b3fbac55ed/src/db/mongodb/index.js)
- [src/db/postgres/index.js](https://github.com/nextapps-de/flexsearch/blob/f7ed963096a0792da7b2fd63bb7114b3fbac55ed/src/db/postgres/index.js)
- [src/db/redis/index.js](https://github.com/nextapps-de/flexsearch/blob/f7ed963096a0792da7b2fd63bb7114b3fbac55ed/src/db/redis/index.js)
- [src/db/sqlite/index.js](https://github.com/nextapps-de/flexsearch/blob/f7ed963096a0792da7b2fd63bb7114b3fbac55ed/src/db/sqlite/index.js)
- [src/db/indexeddb/index.js](https://github.com/nextapps-de/flexsearch/blob/f7ed963096a0792da7b2fd63bb7114b3fbac55ed/src/db/indexeddb/index.js)
- [src/index.js](https://github.com/nextapps-de/flexsearch/blob/f7ed963096a0792da7b2fd63bb7114b3fbac55ed/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| async.js package | library | Observed | Groups 1 file(s) under async.js package (observed from repository paths and static analysis). |
| bundle.js package | library | Observed | Groups 1 file(s) under bundle.js package (observed from repository paths and static analysis). |
| cache.js package | library | Observed | Groups 1 file(s) under cache.js package (observed from repository paths and static analysis). |
| charset package | library | Observed | Groups 8 file(s) under charset package (observed from repository paths and static analysis). |
| charset.js package | library | Observed | Groups 1 file(s) under charset.js package (observed from repository paths and static analysis). |
| common.js package | library | Observed | Groups 1 file(s) under common.js package (observed from repository paths and static analysis). |
| compress.js package | library | Observed | Groups 1 file(s) under compress.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 7 file(s) under data layer (observed from repository paths and static analysis). |
| document package | library | Observed | Groups 3 file(s) under document package (observed from repository paths and static analysis). |
| document.js package | library | Observed | Groups 1 file(s) under document.js package (observed from repository paths and static analysis). |
| encoder.js package | library | Observed | Groups 1 file(s) under encoder.js package (observed from repository paths and static analysis). |
| index package | library | Observed | Groups 3 file(s) under index package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| intersect.js package | library | Observed | Groups 1 file(s) under intersect.js package (observed from repository paths and static analysis). |
| keystore.js package | library | Observed | Groups 1 file(s) under keystore.js package (observed from repository paths and static analysis). |
| lang package | library | Observed | Groups 3 file(s) under lang package (observed from repository paths and static analysis). |
| preset.js package | library | Observed | Groups 1 file(s) under preset.js package (observed from repository paths and static analysis). |
| profiler.js package | library | Observed | Groups 1 file(s) under profiler.js package (observed from repository paths and static analysis). |
| resolve package | library | Observed | Groups 6 file(s) under resolve package (observed from repository paths and static analysis). |
| resolver.js package | library | Observed | Groups 1 file(s) under resolver.js package (observed from repository paths and static analysis). |
| serialize.js package | library | Observed | Groups 1 file(s) under serialize.js package (observed from repository paths and static analysis). |
| task package | library | Observed | Groups 2 file(s) under task package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 27 file(s) under tests (observed from repository paths and static analysis). |
| type.js package | library | Observed | Groups 1 file(s) under type.js package (observed from repository paths and static analysis). |
| worker package | library | Observed | Groups 4 file(s) under worker package (observed from repository paths and static analysis). |
| worker.js package | library | Observed | Groups 1 file(s) under worker.js package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/node.js.yml` (ci)
- `docker-compose.yml` (container)
- `example/nodejs-commonjs/.document-worker-persistent/data.json` (config)
- `example/nodejs-commonjs/.document-worker-persistent/package.json` (manifest)
- `example/nodejs-commonjs/basic-export-import/package.json` (manifest)
- `example/nodejs-commonjs/basic-persistent/package.json` (manifest)
- `example/nodejs-commonjs/basic-resolver/package.json` (manifest)
- `example/nodejs-commonjs/basic-suggestion/package.json` (manifest)
- `example/nodejs-commonjs/basic-worker-export-import/package.json` (manifest)
- `example/nodejs-commonjs/basic-worker-extern-config/package.json` (manifest)
- `example/nodejs-commonjs/basic-worker/package.json` (manifest)
- `example/nodejs-commonjs/basic/package.json` (manifest)
- `example/nodejs-commonjs/document-export-import/data.json` (config)
- `example/nodejs-commonjs/document-export-import/package.json` (manifest)
- `example/nodejs-commonjs/document-persistent/data.json` (config)
- `example/nodejs-commonjs/document-persistent/package.json` (manifest)
- `example/nodejs-commonjs/document-resolver/package.json` (manifest)
- `example/nodejs-commonjs/document-worker-export-import/data.json` (config)
- `example/nodejs-commonjs/document-worker-export-import/package.json` (manifest)
- `example/nodejs-commonjs/document-worker-extern-config/data.json` (config)
- `example/nodejs-commonjs/document-worker-extern-config/package.json` (manifest)
- `example/nodejs-commonjs/document-worker/data.json` (config)
- `example/nodejs-commonjs/document-worker/package.json` (manifest)
- `example/nodejs-commonjs/document/data.json` (config)
- `example/nodejs-commonjs/document/package.json` (manifest)
- `example/nodejs-commonjs/language-pack/package.json` (manifest)
- `example/nodejs-esm/basic-export-import/package.json` (manifest)
- `example/nodejs-esm/basic-persistent/package.json` (manifest)
- `example/nodejs-esm/basic-resolver/package.json` (manifest)
- `example/nodejs-esm/basic-suggestion/package.json` (manifest)
- `example/nodejs-esm/basic-worker-export-import/package.json` (manifest)
- `example/nodejs-esm/basic-worker-extern-config/package.json` (manifest)
- `example/nodejs-esm/basic-worker/package.json` (manifest)
- `example/nodejs-esm/basic/package.json` (manifest)
- `example/nodejs-esm/document-export-import/data.json` (config)
- `example/nodejs-esm/document-export-import/package.json` (manifest)
- `example/nodejs-esm/document-persistent/data.json` (config)
- `example/nodejs-esm/document-persistent/package.json` (manifest)
- `example/nodejs-esm/document-resolver/package.json` (manifest)
- `example/nodejs-esm/document-worker-export-import/data.json` (config)
- `example/nodejs-esm/document-worker-export-import/package.json` (manifest)
- `example/nodejs-esm/document-worker-extern-config/data.json` (config)
- `example/nodejs-esm/document-worker-extern-config/package.json` (manifest)
- `example/nodejs-esm/document-worker/data.json` (config)
- `example/nodejs-esm/document-worker/package.json` (manifest)
- `example/nodejs-esm/document/data.json` (config)
- `example/nodejs-esm/document/package.json` (manifest)
- `example/nodejs-esm/language-pack/package.json` (manifest)
- `package.json` (manifest)
- `src/db/clickhouse/package.json` (manifest)
- `src/db/mongodb/package.json` (manifest)
- `src/db/postgres/package.json` (manifest)
- `src/db/redis/package.json` (manifest)
- `src/db/sqlite/package.json` (manifest)
- `task/babel.bundle.json` (config)
- `task/babel.debug.json` (config)
- `task/babel.min.json` (config)

## Top-level layout

- `example` — 149 analysed file(s)
- `src` — 57 analysed file(s)
- `doc` — 29 analysed file(s)
- `test` — 27 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `task` — 5 analysed file(s)
- `.github` — 2 analysed file(s)
- `demo` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 168 file(s) were skipped during inventory (1 x lockfile excluded; 167 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f7ed963096a0792da7b2fd63bb7114b3fbac55ed` is the revision these paths and observations refer to.
