# Project structure: fastapi/sqlmodel

**Analysed commit:** `273cb2e40e15628ef3d576679ff7289176c16265`

**Commit reference:** [273cb2e40e15628ef3d576679ff7289176c16265](https://github.com/fastapi/sqlmodel/commit/273cb2e40e15628ef3d576679ff7289176c16265)

**Tree at this commit:** [fastapi/sqlmodel@273cb2e40e15](https://github.com/fastapi/sqlmodel/tree/273cb2e40e15628ef3d576679ff7289176c16265)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fastapi/sqlmodel |
| Description | SQL databases in Python, designed for simplicity, compatibility, and robustness. |
| Stars | 18609 |
| Forks | 900 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `273cb2e40e15628ef3d576679ff7289176c16265` |
| Retrieved at | 2026-11-14T19:08:23.220818+00:00 |
| Files in this snapshot | 474 |

## Directory tree

```text
.github/  (19 files)
  workflows/  (15 files)
    add-to-project.yml
    build-docs.yml
    bump-pre-commit-hooks.yml
    create-draft-release.yml
    deploy-docs.yml
    detect-conflicts.yml
    guard-dependencies.yml
    issue-manager.yml
    pre-commit.yml
    prepare-release.yml
    publish.yml
    smokeshow.yml
    test-redistribute.yml
    test.yml
    zizmor.yml
  dependabot.yml
  latest-changes.yml
  pr-push.yml
  pr-submit.yml
data/  (1 files)
  sponsors.yml
docs/  (89 files)
  about/  (1 files)
    index.md
  advanced/  (4 files)
    datetime.md
    decimal.md
    index.md
    uuid.md
  css/  (2 files)
    custom.css
    termynal.css
  img/  (19 files)
    databases/  (1 files)
      … 1 files under this directory
    logo-margin/  (4 files)
      … 4 files under this directory
    tutorial/  (11 files)
      … 11 files under this directory
    github-social-preview.svg
    icon-white.svg
    icon.svg
  js/  (2 files)
    custom.js
    termynal.js
  learn/  (1 files)
    index.md
  overrides/  (1 files)
    main.html
  resources/  (1 files)
    index.md
  tutorial/  (45 files)
    connect/  (6 files)
      … 6 files under this directory
    fastapi/  (13 files)
      … 13 files under this directory
    many-to-many/  (5 files)
      … 5 files under this directory
    relationship-attributes/  (8 files)
      … 8 files under this directory
    automatic-id-none-refresh.md
    code-structure.md
    create-db-and-table-with-db-browser.md
    create-db-and-table.md
    delete.md
    index.md
    indexes.md
    insert.md
    limit-and-offset.md
    one.md
    select.md
    update.md
    where.md
  ai-development.md
  alternatives.md
  contributing.md
  databases.md
  db-to-code.md
  environment-variables.md
  features.md
  help.md
  index.md
  install.md
  management.md
  release-notes.md
  virtual-environments.md
docs_src/  (162 files)
  advanced/  (12 files)
    datetime/  (6 files)
      … 6 files under this directory
    decimal/  (2 files)
      … 2 files under this directory
    uuid/  (3 files)
      … 3 files under this directory
    __init__.py
  tutorial/  (149 files)
    automatic_id_none_refresh/  (4 files)
      … 4 files under this directory
    code_structure/  (10 files)
      … 10 files under this directory
    connect/  (15 files)
      … 15 files under this directory
    create_db_and_table/  (5 files)
      … 5 files under this directory
    delete/  (4 files)
      … 4 files under this directory
    fastapi/  (40 files)
      … 40 files under this directory
    indexes/  (3 files)
      … 3 files under this directory
    insert/  (5 files)
      … 5 files under this directory
    many_to_many/  (4 files)
      … 4 files under this directory
    offset_and_limit/  (5 files)
      … 5 files under this directory
    one/  (10 files)
      … 10 files under this directory
    relationship_attributes/  (18 files)
      … 18 files under this directory
    select/  (6 files)
      … 6 files under this directory
    update/  (7 files)
      … 7 files under this directory
    where/  (12 files)
      … 12 files under this directory
    __init__.py
  __init__.py
includes/  (1 files)
  agent-banner.md
scripts/  (9 files)
  add_latest_release_date.py
  agent_banner.py
  deploy_docs_status.py
  docs.py
  format.sh
  generate_select.py
  lint.sh
  prepare_release.py
  test.sh
sqlmodel/  (19 files)
  .agents/  (1 files)
    skills/  (1 files)
      … 1 files under this directory
  ext/  (3 files)
    asyncio/  (2 files)
      … 2 files under this directory
    __init__.py
  orm/  (2 files)
    __init__.py
    session.py
  pool/  (1 files)
    __init__.py
  sql/  (7 files)
    __init__.py
    _expression_select_cls.py
    _expression_select_gen.py
    _expression_select_gen.py.jinja2
    base.py
    expression.py
    sqltypes.py
  __init__.py
  _compat.py
  default.py
  main.py
  py.typed
tests/  (164 files)
  test_advanced/  (12 files)
    test_datetime/  (6 files)
      … 6 files under this directory
    test_decimal/  (2 files)
      … 2 files under this directory
    test_uuid/  (3 files)
      … 3 files under this directory
    __init__.py
  test_pydantic/  (3 files)
    __init__.py
    test_field.py
    test_model_dump.py
  test_tutorial/  (119 files)
    test_automatic_id_none_refresh/  (2 files)
      … 2 files under this directory
    test_code_structure/  (3 files)
      … 3 files under this directory
    test_connect/  (14 files)
      … 14 files under this directory
    test_create_db_and_table/  (4 files)
      … 4 files under this directory
    test_delete/  (2 files)
      … 2 files under this directory
    test_fastapi/  (31 files)
      … 31 files under this directory
    test_indexes/  (3 files)
      … 3 files under this directory
    test_insert/  (4 files)
      … 4 files under this directory
    test_limit_and_offset/  (5 files)
      … 5 files under this directory
    test_many_to_many/  (4 files)
      … 4 files under this directory
    test_one/  (10 files)
      … 10 files under this directory
    test_relationship_attributes/  (18 files)
      … 18 files under this directory
    test_select/  (3 files)
      … 3 files under this directory
    test_update/  (3 files)
      … 3 files under this directory
    test_where/  (12 files)
      … 12 files under this directory
    __init__.py
  __init__.py
  conftest.py
  test_aliases.py
  test_annotated_uuid.py
  test_asyncio.py
  test_dataclass_transform.py
  test_datetime.py
  test_default.py
  test_deprecations.py
  test_docs_cleanup.py
  test_enums.py
  test_enums_models.py
  test_field_sa_args_kwargs.py
  test_field_sa_column.py
  test_field_sa_relationship.py
  test_field_sa_type.py
  test_fields_set.py
  test_future_annotations.py
  test_instance_no_args.py
  test_main.py
  test_missing_type.py
  test_nullable.py
  test_ondelete_raises.py
  test_prepare_release.py
  … 6 more files
.gitignore
.pre-commit-config.yaml
.python-version
CITATION.cff
LICENSE
README.md
compose.yml
mkdocs.env.yml
mkdocs.yml
pyproject.toml
```

## Entry points

- [docs_src/advanced/datetime/tutorial001.py:29](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/advanced/datetime/tutorial001.py#L29)
- [docs_src/advanced/datetime/tutorial002.py:20](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/advanced/datetime/tutorial002.py#L20)
- [docs_src/advanced/datetime/tutorial003.py:17](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/advanced/datetime/tutorial003.py#L17)
- [docs_src/advanced/datetime/tutorial005.py:17](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/advanced/datetime/tutorial005.py#L17)
- [docs_src/advanced/decimal/tutorial001.py:59](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/advanced/decimal/tutorial001.py#L59)
- [docs_src/advanced/uuid/tutorial001.py:63](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/advanced/uuid/tutorial001.py#L63)
- [docs_src/advanced/uuid/tutorial002.py:62](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/advanced/uuid/tutorial002.py#L62)
- [docs_src/tutorial/automatic_id_none_refresh/tutorial001.py:78](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/tutorial/automatic_id_none_refresh/tutorial001.py#L78)
- [docs_src/tutorial/automatic_id_none_refresh/tutorial002.py:79](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/tutorial/automatic_id_none_refresh/tutorial002.py#L79)
- [docs_src/tutorial/code_structure/tutorial001/app.py:28](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/tutorial/code_structure/tutorial001/app.py#L28)
- [docs_src/tutorial/code_structure/tutorial002/app.py:29](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/tutorial/code_structure/tutorial002/app.py#L29)
- [docs_src/tutorial/connect/create_tables/tutorial001.py:33](https://github.com/fastapi/sqlmodel/blob/273cb2e40e15628ef3d576679ff7289176c16265/docs_src/tutorial/connect/create_tables/tutorial001.py#L33)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Hero, Team. Observed top-level functions: create_db_and_tables. |
| docs_src package | library | Observed | Groups 49 file(s) under docs_src package (observed from repository paths and static analysis). Observed top-level classes: Hero, Team. Observed top-level functions: downgrade, upgrade. |
| Application entry point | entrypoint | Observed | Groups 94 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Typer. Observed routes: POST /heroes/, GET /heroes/, GET /heroes/{he… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: AgentBannerExtension, AgentBannerPreprocessor, Arg. Observed top-level functions: makeExtension. |
| sqlmodel package | library | Observed | Groups 15 file(s) under sqlmodel package (observed from repository paths and static analysis). Observed top-level classes: AsyncSession, AutoString, Executable, FakeMetadata, ObjectWithUpdateWrapper, SQLModelConfig. Obs… |
| Tests | test | Observed | Groups 178 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BaseModel, FlatModel, InheritModel, Item, Modules, MyEnum1. Observed top-level functions: check_calls, cle… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/latest-changes.yml` (config)
- `.github/pr-push.yml` (config)
- `.github/pr-submit.yml` (config)
- `.github/workflows/add-to-project.yml` (ci)
- `.github/workflows/build-docs.yml` (ci)
- `.github/workflows/bump-pre-commit-hooks.yml` (ci)
- `.github/workflows/create-draft-release.yml` (ci)
- `.github/workflows/deploy-docs.yml` (ci)
- `.github/workflows/detect-conflicts.yml` (ci)
- `.github/workflows/guard-dependencies.yml` (ci)
- `.github/workflows/issue-manager.yml` (ci)
- `.github/workflows/pre-commit.yml` (ci)
- `.github/workflows/prepare-release.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/smokeshow.yml` (ci)
- `.github/workflows/test-redistribute.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `compose.yml` (container)
- `data/sponsors.yml` (config)
- `mkdocs.env.yml` (config)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 164 analysed file(s)
- `docs_src` — 162 analysed file(s)
- `docs` — 89 analysed file(s)
- `.github` — 19 analysed file(s)
- `sqlmodel` — 19 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `scripts` — 9 analysed file(s)
- `data` — 1 analysed file(s)
- `includes` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `273cb2e40e15628ef3d576679ff7289176c16265` is the revision these paths and observations refer to.
