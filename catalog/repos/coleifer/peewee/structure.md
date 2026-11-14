# Project structure: coleifer/peewee

**Analysed commit:** `dc0637b30f696d512d35aa10ccd78170f5776251`

**Commit reference:** [dc0637b30f696d512d35aa10ccd78170f5776251](https://github.com/coleifer/peewee/commit/dc0637b30f696d512d35aa10ccd78170f5776251)

**Tree at this commit:** [coleifer/peewee@dc0637b30f69](https://github.com/coleifer/peewee/tree/dc0637b30f696d512d35aa10ccd78170f5776251)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | coleifer/peewee |
| Description | a small, expressive orm -- supports postgresql, mysql, sqlite, now with asyncio |
| Stars | 12006 |
| Forks | 1389 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `dc0637b30f696d512d35aa10ccd78170f5776251` |
| Retrieved at | 2026-11-14T19:10:17.455260+00:00 |
| Files in this snapshot | 176 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    tests.yaml
    wheels.yaml
docs/  (36 files)
  _themes/  (5 files)
    flask/  (5 files)
      … 5 files under this directory
  extras/  (1 files)
    llms.txt
  peewee/  (24 files)
    asyncio.rst
    contributing.rst
    database.rst
    db_tools.rst
    example.rst
    framework_integration.rst
    installation.rst
    interactive.rst
    models.rst
    mysql.rst
    orm_utils.rst
    pool-snippet.rst
    postgres.rst
    query_builder.rst
    query_library.rst
    query_operators.rst
    querying.rst
    quickstart.rst
    recipes.rst
    relationships.rst
    schema.rst
    sqlite.rst
    transactions.rst
    writing.rst
  Makefile
  clubdata.sql
  conf.py
  index.rst
  make.bat
  requirements.txt
examples/  (47 files)
  analytics/  (4 files)
    app.py
    reports.py
    requirements.txt
    run_example.py
  blog/  (15 files)
    migrations/  (1 files)
      … 1 files under this directory
    static/  (3 files)
      … 3 files under this directory
    templates/  (8 files)
      … 8 files under this directory
    .pwmigrate
    app.py
    requirements.txt
  twitter/  (19 files)
    migrations/  (1 files)
      … 1 files under this directory
    static/  (1 files)
      … 1 files under this directory
    templates/  (13 files)
      … 13 files under this directory
    .pwmigrate
    app.py
    requirements.txt
    run_example.py
  adjacency_list.py
  anomaly_detection.py
  diary.py
  fastapi_example.py
  graph.py
  hexastore.py
  query_library.py
  reddit_ranking.py
  sqlite_fts_compression.py
peewee-stubs/  (1 files)
  __init__.pyi
playhouse/  (30 files)
  README.md
  __init__.py
  _sqlite_udf.pyx
  apsw_ext.py
  cockroachdb.py
  cysqlite_ext.py
  dataset.py
  db_url.py
  fields.py
  flask_utils.py
  fts_parser.py
  hybrid.py
  kv.py
  migrate.py
  migrations.py
  mysql_ext.py
  pool.py
  postgres_ext.py
  pwasyncio.py
  pydantic_utils.py
  reflection.py
  schema_diff.py
  shortcuts.py
  signals.py
  … 6 more files
tests/  (45 files)
  __init__.py
  __main__.py
  apsw_ext.py
  base.py
  base_models.py
  cockroachdb.py
  cysqlite_ext.py
  dataset.py
  db_tests.py
  db_url.py
  extra_fields.py
  fields.py
  flask_utils.py
  fts_parser.py
  hybrid.py
  json_field.py
  kv.py
  manytomany.py
  migrations.py
  model_sql.py
  mysql_ext.py
  pool.py
  postgres.py
  postgres_helpers.py
  … 21 more files
typecheck/  (2 files)
  check_stub.py
  stubtest_allowlist.txt
.gitignore
.readthedocs.yaml
.travis.yml
.travis_deps.sh
CHANGELOG.md
LICENSE
MANIFEST.in
README.rst
bench.py
pwiz.py
pyproject.toml
runtests.py
setup.py
```

## Entry points

- [bench.py:141](https://github.com/coleifer/peewee/blob/dc0637b30f696d512d35aa10ccd78170f5776251/bench.py#L141)
- [playhouse/migrations.py](https://github.com/coleifer/peewee/blob/dc0637b30f696d512d35aa10ccd78170f5776251/playhouse/migrations.py)
- [pwiz.py](https://github.com/coleifer/peewee/blob/dc0637b30f696d512d35aa10ccd78170f5776251/pwiz.py)
- [runtests.py:95](https://github.com/coleifer/peewee/blob/dc0637b30f696d512d35aa10ccd78170f5776251/runtests.py#L95)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Base, Collection, Item, Migration, MigrationError, Register. Observed top-level functions:… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| playhouse package | library | Observed | Groups 26 file(s) under playhouse package (observed from repository paths and static analysis). Observed top-level classes: APSWDatabase, ArrayField, ArrayValue, AsyncConnectionWrapper, AsyncCursor, AsyncDatabaseMixin.… |
| Tests | test | Observed | Groups 46 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Flask. Observed top-level classes: A, AComposite, ADirty, AFModel, ANoLazy, APIResponse. Observ… |
| typecheck package | library | Observed | Groups 1 file(s) under typecheck package (observed from repository paths and static analysis). Observed top-level classes: Event, Tweet, User. Observed top-level functions: bound, enqueue. |

## Important files

- `.github/workflows/tests.yaml` (ci)
- `.github/workflows/wheels.yaml` (ci)
- `.readthedocs.yaml` (config)
- `.travis.yml` (ci)
- `MANIFEST.in` (manifest)
- `docs/requirements.txt` (manifest)
- `examples/analytics/requirements.txt` (manifest)
- `examples/blog/requirements.txt` (manifest)
- `examples/twitter/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `examples` — 47 analysed file(s)
- `tests` — 45 analysed file(s)
- `docs` — 36 analysed file(s)
- `playhouse` — 30 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 2 analysed file(s)
- `typecheck` — 2 analysed file(s)
- `peewee-stubs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `dc0637b30f696d512d35aa10ccd78170f5776251` is the revision these paths and observations refer to.
