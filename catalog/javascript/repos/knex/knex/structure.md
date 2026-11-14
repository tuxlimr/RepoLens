# Project structure: knex/knex

**Analysed commit:** `e25d54bcb707714a17f5a5744eba5c4246bb4d1d`

**Commit reference:** [e25d54bcb707714a17f5a5744eba5c4246bb4d1d](https://github.com/knex/knex/commit/e25d54bcb707714a17f5a5744eba5c4246bb4d1d)

**Tree at this commit:** [knex/knex@e25d54bcb707](https://github.com/knex/knex/tree/e25d54bcb707714a17f5a5744eba5c4246bb4d1d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | knex/knex |
| Description | A query builder for PostgreSQL, MySQL, CockroachDB, SQL Server, SQLite3 and Oracle, designed to be flexible, portable, and fun to use. |
| Stars | 20340 |
| Forks | 2237 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e25d54bcb707714a17f5a5744eba5c4246bb4d1d` |
| Retrieved at | 2026-11-14T19:11:14.511800+00:00 |
| Files in this snapshot | 588 |

## Directory tree

```text
.github/  (13 files)
  workflows/  (10 files)
    assign-dri.yml
    codeql-analysis.yml
    coverage.yml
    ensure-labels.yml
    integration-tests.yml
    linting.yml
    mirror-images.yml
    release-drafter.yml
    release.yml
    unit-tests.yml
  ISSUE_TEMPLATE.md
  dependabot.yml
  release-drafter.yml
.husky/  (2 files)
  post-checkout
  pre-commit
bin/  (5 files)
  utils/  (3 files)
    cli-config-utils.js
    constants.js
    migrationsLister.js
  cli.js
  knexfile-runtime-error.js
docs/  (49 files)
  .vitepress/  (13 files)
    theme/  (9 files)
      … 9 files under this directory
    badges.ts
    config.mts
    knexDialects.ts
    slugify.ts
  scripts/  (6 files)
    deploy-doc.sh
    format-sql-bindings.mjs
    resolve-schema-snippets-docker.mjs
    resolve-schema-snippets.mjs
    snippet-utils.d.ts
    snippet-utils.mjs
  src/  (26 files)
    blog/  (8 files)
      … 8 files under this directory
    faq/  (3 files)
      … 3 files under this directory
    guide/  (10 files)
      … 10 files under this directory
    public/  (3 files)
      … 3 files under this directory
    changelog.md
    index.md
  .gitignore
  README.md
  package.json
  tsconfig.json
lib/  (169 files)
  dialects/  (83 files)
    better-sqlite3/  (1 files)
      … 1 files under this directory
    cockroachdb/  (6 files)
      … 6 files under this directory
    mariadb/  (4 files)
      … 4 files under this directory
    mssql/  (8 files)
      … 8 files under this directory
    mysql/  (9 files)
      … 9 files under this directory
    mysql2/  (2 files)
      … 2 files under this directory
    oracle/  (10 files)
      … 10 files under this directory
    oracledb/  (8 files)
      … 8 files under this directory
    pgnative/  (1 files)
      … 1 files under this directory
    postgres/  (9 files)
      … 9 files under this directory
    redshift/  (8 files)
      … 8 files under this directory
    sqlite3/  (15 files)
      … 15 files under this directory
    index.js
    index.ts
  execution/  (6 files)
    internal/  (3 files)
      … 3 files under this directory
    batch-insert.js
    runner.js
    transaction.js
  formatter/  (3 files)
    formatterUtils.js
    rawFormatter.js
    wrappingFormatter.js
  knex-builder/  (5 files)
    internal/  (2 files)
      … 2 files under this directory
    FunctionHelper.js
    Knex.js
    make-knex.js
  migrations/  (38 files)
    common/  (1 files)
      … 1 files under this directory
    migrate/  (22 files)
      … 22 files under this directory
    seed/  (10 files)
      … 10 files under this directory
    util/  (5 files)
      … 5 files under this directory
  query/  (6 files)
    analytic.js
    constants.js
    joinclause.js
    method-constants.js
    querybuilder.js
    querycompiler.js
  schema/  (9 files)
    internal/  (1 files)
      … 1 files under this directory
    builder.js
    columnbuilder.js
    columncompiler.js
    compiler.js
    tablebuilder.js
    tablecompiler.js
    viewbuilder.js
    viewcompiler.js
  util/  (9 files)
    finally-mixin.js
    helpers.js
    is.js
    nanoid.js
    noop.js
    save-async-stack.js
    security.js
    string.js
    timeout.js
  .gitignore
  builder-interface-augmenter.js
  client.js
  constants.js
  formatter.js
  index.js
  logger.js
  pool.js
  raw.js
  ref.js
scripts/  (14 files)
  stress-test/  (6 files)
    README.txt
    docker-compose.yml
    knex-stress-test.js
    mysql2-random-hanging-every-now-and-then.js
    mysql2-sudden-exit-without-error.js
    reconnect-test-mysql-based-drivers.js
  build-for-release.sh
  build.js
  clean.js
  docker-compose.yml
  oracledb-install-driver-libs.sh
  revert-release-to-draft.sh
  runkit-example.js
  update-changelog.mjs
test/  (293 files)
  cli/  (16 files)
    _justexit.js
    cli-config-utils.spec.js
    cli-test-utils.js
    esm-interop.spec.js
    help.spec.js
    knexfile-runtime-error.spec.js
    knexfile-test.spec.js
    migrate-disable-transactions.spec.js
    migrate-make.spec.js
    migrate-to-before.spec.js
    migrate-unlock.spec.js
    migrate.spec.js
    seed-make.spec.js
    seed.spec.js
    tempfiles.js
    version.spec.js
  integration/  (19 files)
    datatype/  (3 files)
      … 3 files under this directory
    dialects/  (1 files)
      … 1 files under this directory
    execution/  (1 files)
      … 1 files under this directory
    helpers/  (1 files)
      … 1 files under this directory
    query/  (5 files)
      … 5 files under this directory
    seed/  (4 files)
      … 4 files under this directory
    connection-config-provider.js
    index.js
    logger.js
    suite.js
  integration2/  (84 files)
    dialects/  (9 files)
      … 9 files under this directory
    migrate/  (44 files)
      … 44 files under this directory
    pool/  (1 files)
      … 1 files under this directory
    query/  (12 files)
      … 12 files under this directory
    schema/  (13 files)
      … 13 files under this directory
    transaction/  (3 files)
      … 3 files under this directory
    util/  (1 files)
      … 1 files under this directory
    knex.spec.js
  jake/  (2 files)
    jakelib/  (1 files)
      … 1 files under this directory
    Jakefile
  jake-util/  (93 files)
    helpers/  (1 files)
      … 1 files under this directory
    knexfile/  (4 files)
      … 4 files under this directory
    knexfile-custom-migration-source/  (2 files)
      … 2 files under this directory
    knexfile-errors/  (5 files)
      … 5 files under this directory
    knexfile-esm/  (7 files)
      … 7 files under this directory
    knexfile-esm-module/  (5 files)
      … 5 files under this directory
    knexfile-esm-package/  (5 files)
      … 5 files under this directory
    knexfile-imports/  (30 files)
      … 30 files under this directory
    knexfile-mjs/  (4 files)
      … 4 files under this directory
    knexfile-relative/  (6 files)
      … 6 files under this directory
    knexfile-stubs/  (3 files)
      … 3 files under this directory
    knexfile-ts/  (6 files)
      … 6 files under this directory
    knexfile_migrations/  (2 files)
      … 2 files under this directory
    knexfile_seeds/  (1 files)
      … 1 files under this directory
    migration-stubs/  (1 files)
      … 1 files under this directory
    seeds/  (2 files)
      … 2 files under this directory
    seeds-error/  (1 files)
      … 1 files under this directory
    seeds-recursive/  (3 files)
      … 3 files under this directory
    seeds-error-knexfile.js
    seeds-knexfile-async.js
    seeds-knexfile-directories-recursive.js
    seeds-knexfile-directories.js
    seeds-knexfile.js
  tape/  (13 files)
    crossdb-compatibility.js
    harness.js
    index.js
    invalid-db-setup.js
    knex.js
    migrate.js
    parse-connection.js
    pool.js
    query-builder.js
    raw.js
    seed.js
    stream.js
    transactions.js
  unit/  (47 files)
    client/  (2 files)
      … 2 files under this directory
    dialects/  (7 files)
      … 7 files under this directory
    migrations/  (18 files)
      … 18 files under this directory
    query/  (2 files)
      … 2 files under this directory
    schema/  (1 files)
      … 1 files under this directory
    schema-builder/  (10 files)
      … 10 files under this directory
    util/  (5 files)
      … 5 files under this directory
    builder-interface-augmenter.js
    knex.js
  util/  (6 files)
    assertHelper.js
    chai-setup.js
    constants.js
    dataInsertHelper.js
    db-helpers.js
    tableCreatorHelper.js
  .gitignore
  .istanbul.yml
  all-tests-suite.js
  cli-tests-suite.js
  db-less-test-suite.js
  integration-test-suite.js
  knexfile.js
  mocha-all-config-test.js
  mocha-integration-config-test.js
  mocha-unit-config-test.js
  prep-db-mocha.js
  prep-db.js
  testInitializer.js
test-tsd/  (18 files)
  batchInsert.test-d.ts
  common.ts
  having.test-d.ts
  mssql-config.test-d.ts
  pg-config.test-d.ts
  querybuilder.test-d.ts
  select.test-d.ts
  tables.test-d.ts
  transaction.test-d.ts
  tsd-tests1.test-d.ts
  tsd-tests2.test-d.ts
  tsd-tests3.test-d.ts
  tsd-tests4.test-d.ts
  tsd-tests5.test-d.ts
  tsd-tests6.test-d.ts
  tsd-tests7.test-d.ts
  tsd-tests8.test-d.ts
  types.test-d.ts
test-tstyche/  (5 files)
  cjs-subpath-exports.tst.cts
  esm-subpath-exports.tst.ts
  esm-types.tst.ts
  package.json
  tsconfig.json
types/  (3 files)
  index.d.ts
  result.d.ts
  tables.d.ts
.codecov.yml
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.prettierrc
CHANGELOG.md
CONTRIBUTING.md
ECOSYSTEM.md
LICENSE
README.md
UPGRADING.md
knex.d.mts
knex.js
knex.mjs
package.json
tsconfig.json
```

## Entry points

- [knex.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/knex.js)
- [bin/cli.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/bin/cli.js)
- [test/jake-util/knexfile-esm-package/knexfile.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/test/jake-util/knexfile-esm-package/knexfile.js)
- [lib/dialects/better-sqlite3/index.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/lib/dialects/better-sqlite3/index.js)
- [lib/dialects/cockroachdb/index.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/lib/dialects/cockroachdb/index.js)
- [lib/dialects/index.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/lib/dialects/index.js)
- [lib/dialects/index.ts](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/lib/dialects/index.ts)
- [lib/dialects/mariadb/index.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/lib/dialects/mariadb/index.js)
- [lib/dialects/mssql/index.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/lib/dialects/mssql/index.js)
- [lib/dialects/mysql/index.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/lib/dialects/mysql/index.js)
- [lib/dialects/mysql2/index.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/lib/dialects/mysql2/index.js)
- [lib/dialects/oracle/index.js](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/lib/dialects/oracle/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 5 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 147 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 11 file(s) under scripts package (observed from repository paths and static analysis). |
| test-tsd package | library | Observed | Groups 18 file(s) under test-tsd package (observed from repository paths and static analysis). |
| test-tstyche package | library | Observed | Groups 2 file(s) under test-tstyche package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 293 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 3 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.codecov.yml` (config)
- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/release-drafter.yml` (config)
- `.github/workflows/assign-dri.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/coverage.yml` (ci)
- `.github/workflows/ensure-labels.yml` (ci)
- `.github/workflows/integration-tests.yml` (ci)
- `.github/workflows/linting.yml` (ci)
- `.github/workflows/mirror-images.yml` (ci)
- `.github/workflows/release-drafter.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/unit-tests.yml` (ci)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `package.json` (manifest)
- `scripts/docker-compose.yml` (container)
- `scripts/stress-test/docker-compose.yml` (container)
- `test-tstyche/package.json` (manifest)
- `test-tstyche/tsconfig.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 293 analysed file(s)
- `lib` — 169 analysed file(s)
- `docs` — 49 analysed file(s)
- `test-tsd` — 18 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `scripts` — 14 analysed file(s)
- `.github` — 13 analysed file(s)
- `bin` — 5 analysed file(s)
- `test-tstyche` — 5 analysed file(s)
- `types` — 3 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e25d54bcb707714a17f5a5744eba5c4246bb4d1d` is the revision these paths and observations refer to.
