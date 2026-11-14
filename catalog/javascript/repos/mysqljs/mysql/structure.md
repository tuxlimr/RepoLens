# Project structure: mysqljs/mysql

**Analysed commit:** `dc9c152a87ec51a1f647447268917243d2eab1fd`

**Commit reference:** [dc9c152a87ec51a1f647447268917243d2eab1fd](https://github.com/mysqljs/mysql/commit/dc9c152a87ec51a1f647447268917243d2eab1fd)

**Tree at this commit:** [mysqljs/mysql@dc9c152a87ec](https://github.com/mysqljs/mysql/tree/dc9c152a87ec51a1f647447268917243d2eab1fd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mysqljs/mysql |
| Description | A pure node.js JavaScript Client implementing the MySQL protocol. |
| Stars | 18606 |
| Forks | 2515 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `dc9c152a87ec51a1f647447268917243d2eab1fd` |
| Retrieved at | 2026-11-14T19:11:21.249303+00:00 |
| Files in this snapshot | 280 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
benchmark/  (3 files)
  analyze.js
  parse-100k-blog-rows.js
  select-100k-blog-rows.js
lib/  (56 files)
  protocol/  (48 files)
    constants/  (7 files)
      … 7 files under this directory
    packets/  (24 files)
      … 24 files under this directory
    sequences/  (8 files)
      … 8 files under this directory
    Auth.js
    BufferList.js
    PacketHeader.js
    PacketWriter.js
    Parser.js
    Protocol.js
    ResultSet.js
    SqlString.js
    Timer.js
  Connection.js
  ConnectionConfig.js
  Pool.js
  PoolCluster.js
  PoolConfig.js
  PoolConnection.js
  PoolNamespace.js
  PoolSelector.js
test/  (203 files)
  fixtures/  (2 files)
    data.csv
    server.crt
  integration/  (36 files)
    connection/  (36 files)
      … 36 files under this directory
  unit/  (162 files)
    connection/  (76 files)
      … 76 files under this directory
    pool/  (41 files)
      … 41 files under this directory
    pool-cluster/  (26 files)
      … 26 files under this directory
    protocol/  (2 files)
      … 2 files under this directory
    query/  (14 files)
      … 14 files under this directory
    test-ConnectionConfig.js
    test-Mysql.js
    test-PoolConfig.js
  FakeServer.js
  common.js
  run.js
tool/  (8 files)
  free-port.js
  generate-error-constants.js
  generate-type-constants.js
  install-nyc.js
  lint-readme.js
  mysql-version.js
  version-changes.js
  wait-mysql.js
.eslintignore
.eslintrc
.gitignore
Changes.md
License
Readme.md
appveyor.yml
index.js
package.json
```

## Entry points

- [index.js](https://github.com/mysqljs/mysql/blob/dc9c152a87ec51a1f647447268917243d2eab1fd/index.js)
- [lib/protocol/packets/index.js](https://github.com/mysqljs/mysql/blob/dc9c152a87ec51a1f647447268917243d2eab1fd/lib/protocol/packets/index.js)
- [lib/protocol/sequences/index.js](https://github.com/mysqljs/mysql/blob/dc9c152a87ec51a1f647447268917243d2eab1fd/lib/protocol/sequences/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmark package | library | Observed | Groups 3 file(s) under benchmark package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 56 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 203 file(s) under tests (observed from repository paths and static analysis). |
| tool package | library | Observed | Groups 8 file(s) under tool package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci.yml` (ci)
- `appveyor.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 203 analysed file(s)
- `lib` — 56 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `tool` — 8 analysed file(s)
- `benchmark` — 3 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dc9c152a87ec51a1f647447268917243d2eab1fd` is the revision these paths and observations refer to.
