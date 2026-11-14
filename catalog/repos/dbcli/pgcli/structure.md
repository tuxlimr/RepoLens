# Project structure: dbcli/pgcli

**Analysed commit:** `dc9ce9447e0fc005a347b75b7eb5d541e282b1c1`

**Commit reference:** [dc9ce9447e0fc005a347b75b7eb5d541e282b1c1](https://github.com/dbcli/pgcli/commit/dc9ce9447e0fc005a347b75b7eb5d541e282b1c1)

**Tree at this commit:** [dbcli/pgcli@dc9ce9447e0f](https://github.com/dbcli/pgcli/tree/dc9ce9447e0fc005a347b75b7eb5d541e282b1c1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dbcli/pgcli |
| Description | Postgres CLI with autocompletion and syntax highlighting |
| Stars | 13446 |
| Forks | 619 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `dc9ce9447e0fc005a347b75b7eb5d541e282b1c1` |
| Retrieved at | 2026-11-14T19:09:50.183226+00:00 |
| Files in this snapshot | 120 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (4 files)
    ci.yml
    codeql.yml
    codex-review.yml
    publish.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
pgcli/  (30 files)
  packages/  (14 files)
    formatter/  (2 files)
      … 2 files under this directory
    parseutils/  (5 files)
      … 5 files under this directory
    pgliterals/  (3 files)
      … 3 files under this directory
    __init__.py
    prioritization.py
    prompt_utils.py
    sqlcompletion.py
  __init__.py
  __main__.py
  auth.py
  completion_refresher.py
  config.py
  explain_output_formatter.py
  key_bindings.py
  magic.py
  main.py
  pgbuffer.py
  pgclirc
  pgcompleter.py
  pgexecute.py
  pgstyle.py
  pgtoolbar.py
  pyev.py
tests/  (62 files)
  features/  (32 files)
    fixture_data/  (3 files)
      … 3 files under this directory
    steps/  (13 files)
      … 13 files under this directory
    __init__.py
    auto_vertical.feature
    basic_commands.feature
    command_option.feature
    crud_database.feature
    crud_table.feature
    db_utils.py
    environment.py
    expanded.feature
    file_option.feature
    fixture_utils.py
    iocommands.feature
    named_queries.feature
    pgbouncer.feature
    specials.feature
    wrappager.py
  formatter/  (2 files)
    __init__.py
    test_sqlformatter.py
  parseutils/  (3 files)
    test_ctes.py
    test_function_metadata.py
    test_parseutils.py
  conftest.py
  metadata.py
  pytest.ini
  test_alias_dsn.py
  test_application_name.py
  test_auth.py
  test_completion_refresher.py
  test_config.py
  test_fuzzy_completion.py
  test_init_commands_simple.py
  test_main.py
  test_naive_completion.py
  test_pgcompleter.py
  test_pgexecute.py
  test_pgspecial.py
  test_prioritization.py
  test_prompt_utils.py
  test_rowlimit.py
  test_smart_completion_multiple_schemata.py
  test_smart_completion_public_schema_only.py
  test_sqlcompletion.py
  test_ssh_tunnel.py
  test_trailing_comments.py
  test_tuples_only.py
  … 1 more files
.coveragerc
.editorconfig
.git-blame-ignore-revs
.gitignore
.pre-commit-config.yaml
AUTHORS
CONTRIBUTING.rst
Dockerfile
LICENSE.txt
MANIFEST.in
README.rst
RELEASES.md
TODO
changelog.rst
pgcli-completion.bash
post-install
post-remove
pylintrc
pyproject.toml
release.py
sanity_checks.txt
tox.ini
```

## Entry points

- [pgcli/__main__.py:8](https://github.com/dbcli/pgcli/blob/dc9ce9447e0fc005a347b75b7eb5d541e282b1c1/pgcli/__main__.py#L8)
- [pgcli/main.py](https://github.com/dbcli/pgcli/blob/dc9ce9447e0fc005a347b75b7eb5d541e282b1c1/pgcli/main.py)
- [release.py:183](https://github.com/dbcli/pgcli/blob/dc9ce9447e0fc005a347b75b7eb5d541e282b1c1/release.py#L183)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: config_location, ensure_dir_exists, get_casing_file, get_config, get_config_filenam… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: PGCli, PgCliQuitError. Observed top-level functions: check_tag, checklist, cli, comment_on… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| pgcli package | library | Observed | Groups 24 file(s) under pgcli package (observed from repository paths and static analysis). Observed top-level classes: CompletionRefresher, ExplainOutputFormatter, FunctionMetadata, InvalidMapFile, PGCompleter, PGExecu… |
| Tests | test | Observed | Groups 62 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH pgcli.main.os. Observed top-level classes: MetaData, TestIsCompleteWithTrailingComments, VirtualCursor. Observed… |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/codex-review.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `pgcli/packages/pgliterals/pgliterals.json` (config)
- `pyproject.toml` (manifest)
- `tox.ini` (config)

## Top-level layout

- `tests` — 62 analysed file(s)
- `pgcli` — 30 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `dc9ce9447e0fc005a347b75b7eb5d541e282b1c1` is the revision these paths and observations refer to.
