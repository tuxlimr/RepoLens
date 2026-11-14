# Project structure: dbcli/mycli

**Analysed commit:** `9a216b6c68294b4222e1780bfe66d00d3c1d1a91`

**Commit reference:** [9a216b6c68294b4222e1780bfe66d00d3c1d1a91](https://github.com/dbcli/mycli/commit/9a216b6c68294b4222e1780bfe66d00d3c1d1a91)

**Tree at this commit:** [dbcli/mycli@9a216b6c6829](https://github.com/dbcli/mycli/tree/9a216b6c68294b4222e1780bfe66d00d3c1d1a91)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dbcli/mycli |
| Description | Rich MySQL Terminal Client with AutoCompletion, Syntax Highlighting, and Dataframes |
| Stars | 11997 |
| Forks | 702 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `9a216b6c68294b4222e1780bfe66d00d3c1d1a91` |
| Retrieved at | 2026-11-14T19:10:19.896267+00:00 |
| Files in this snapshot | 211 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  actions/  (2 files)
    lint/  (1 files)
      … 1 files under this directory
    typecheck/  (1 files)
      … 1 files under this directory
  workflows/  (4 files)
    ci.yml
    lint.yml
    publish.yml
    typecheck.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
doc/  (5 files)
  cookbook.md
  key_bindings.md
  known_bugs.md
  llm.md
  transforms.md
docker/  (3 files)
  resources/  (2 files)
    dot_mycli_history.txt
    test_db_license.md
  Dockerfile
mycli/  (89 files)
  main_modes/  (6 files)
    batch.py
    checkup.py
    completions.py
    execute.py
    list_dsn.py
    repl.py
  packages/  (63 files)
    completion/  (5 files)
      … 5 files under this directory
    credentials/  (2 files)
      … 2 files under this directory
    dataframes/  (3 files)
      … 3 files under this directory
    execution/  (3 files)
      … 3 files under this directory
    integrations/  (13 files)
      … 13 files under this directory
    prompt_toolkit/  (8 files)
      … 8 files under this directory
    pygments/  (2 files)
      … 2 files under this directory
    redirection/  (2 files)
      … 2 files under this directory
    special_commands/  (10 files)
      … 10 files under this directory
    sql_result/  (2 files)
      … 2 files under this directory
    tabular_output/  (2 files)
      … 2 files under this directory
    utils/  (10 files)
      … 10 files under this directory
    __init__.py
  resources/  (3 files)
    completions/  (3 files)
      … 3 files under this directory
  AUTHORS.txt
  SPONSORS.txt
  TIPS.txt
  __init__.py
  app_state.py
  cli_runner.py
  client.py
  client_commands.py
  client_connection.py
  client_query.py
  compat.py
  config.py
  constants.py
  main.py
  myclirc
  output.py
  types.py
mycli_test/  (93 files)
  features/  (25 files)
    fixture_data/  (1 files)
      … 1 files under this directory
    steps/  (11 files)
      … 11 files under this directory
    __init__.py
    auto_vertical.feature
    basic_commands.feature
    connection.feature
    crud_database.feature
    crud_table.feature
    db_utils.py
    environment.py
    fixture_utils.py
    iocommands.feature
    named_queries.feature
    specials.feature
    wrappager.py
  pytests/  (65 files)
    conftest.py
    test_app_state.py
    test_background_runner.py
    test_bash_completion.py
    test_batch_utils.py
    test_boundary_tunnel.py
    test_checkup.py
    test_cli_runner.py
    test_cli_utils.py
    test_clibuffer.py
    test_client.py
    test_client_commands.py
    test_client_connection.py
    test_client_query.py
    test_completer_use_switch.py
    test_completion_engine.py
    test_completion_refresher.py
    test_config.py
    test_delimitercommand.py
    test_dsn_aliases.py
    test_favoritequeries.py
    test_fish_completion.py
    test_fzf.py
    test_hybrid_redirection.py
    … 41 more files
  __init__.py
  myclirc
  utils.py
.git-blame-ignore-revs
.gitignore
AGENTS.md
AUTHORS.md
CONTRIBUTING.md
LICENSE.txt
MANIFEST.in
README.md
SPONSORS.md
changelog.md
pyproject.toml
```

## Entry points

- [mycli/main.py](https://github.com/dbcli/mycli/blob/9a216b6c68294b4222e1780bfe66d00d3c1d1a91/mycli/main.py)
- [mycli_test/features/wrappager.py:16](https://github.com/dbcli/mycli/blob/9a216b6c68294b4222e1780bfe66d00d3c1d1a91/mycli_test/features/wrappager.py#L16)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: LimitedQuotePreservingConfigObj, SQLValuePreservingConfigObj, TripleQuotedConfigValue… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ArgType, CliArgs, CommandNotFound, CommandVerbosity, IntOrStringClickParamType, SpecialCom… |
| External integrations | external | Observed | Groups 14 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BoundaryTunnel, BoundaryTunnelError, Fzf, KubectlTunnel, KubectlTunnelError, MyCli. Observe… |
| mycli package | library | Observed | Groups 65 file(s) under mycli package (observed from repository paths and static analysis). Observed top-level classes: AppStateMixin, BackgroundCursor, BackgroundRunner, BackgroundSSCursor, CheckpointReplayError, Clien… |
| mycli_test package | library | Observed | Groups 17 file(s) under mycli_test package (observed from repository paths and static analysis). Observed top-level classes: DummyFormatter, DummyLogger, FakeCursorBase, RecordingSQLExecute, ReusableLock. Observed top-l… |
| Tests | test | Observed | Groups 66 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Group. Observed routes: PATCH mycli.packages.utils.path_utils.list_path, PATCH click.clear, PAT… |

## Important files

- `.github/actions/lint/action.yml` (config)
- `.github/actions/typecheck/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/typecheck.yml` (ci)
- `MANIFEST.in` (manifest)
- `docker/Dockerfile` (container)
- `pyproject.toml` (manifest)

## Top-level layout

- `mycli_test` — 93 analysed file(s)
- `mycli` — 89 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 10 analysed file(s)
- `doc` — 5 analysed file(s)
- `docker` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9a216b6c68294b4222e1780bfe66d00d3c1d1a91` is the revision these paths and observations refer to.
