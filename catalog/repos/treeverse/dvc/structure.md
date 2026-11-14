# Project structure: treeverse/dvc

**Analysed commit:** `b59add99ee667f2b352cc1be337619f965fe3fea`

**Commit reference:** [b59add99ee667f2b352cc1be337619f965fe3fea](https://github.com/treeverse/dvc/commit/b59add99ee667f2b352cc1be337619f965fe3fea)

**Tree at this commit:** [treeverse/dvc@b59add99ee66](https://github.com/treeverse/dvc/tree/b59add99ee667f2b352cc1be337619f965fe3fea)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | treeverse/dvc |
| Description | 🦉 Data Versioning and ML Experiments |
| Stars | 15973 |
| Forks | 1343 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `b59add99ee667f2b352cc1be337619f965fe3fea` |
| Retrieved at | 2026-11-14T19:08:57.112310+00:00 |
| Files in this snapshot | 589 |

## Directory tree

```text
.dvc/  (2 files)
  .gitignore
  config
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (5 files)
    benchmarks.yaml
    build.yaml
    codeql.yml
    plugin_tests.yaml
    tests.yaml
  PULL_REQUEST_TEMPLATE.md
  codecov.yml
  dependabot.yml
  release.yml
dvc/  (300 files)
  __pyinstaller/  (8 files)
    __init__.py
    hook-asyncssh.py
    hook-celery.py
    hook-dvc.py
    hook-dvc.utils.flatten.py
    hook-dvc_task.py
    hook-fsspec.py
    hook-pydrive2.py
  api/  (7 files)
    __init__.py
    artifacts.py
    data.py
    dataset.py
    experiments.py
    scm.py
    show.py
  cli/  (6 files)
    __init__.py
    command.py
    completion.py
    formatter.py
    parser.py
    utils.py
  commands/  (66 files)
    experiments/  (15 files)
      … 15 files under this directory
    ls/  (2 files)
      … 2 files under this directory
    queue/  (7 files)
      … 7 files under this directory
    __init__.py
    add.py
    artifacts.py
    cache.py
    check_ignore.py
    checkout.py
    commit.py
    completion.py
    config.py
    daemon.py
    dag.py
    data.py
    data_sync.py
    dataset.py
    destroy.py
    diff.py
    du.py
    freeze.py
    gc.py
    get.py
    get_url.py
    git_hook.py
    imp.py
    imp_db.py
    … 18 more files
  dependency/  (6 files)
    __init__.py
    base.py
    dataset.py
    db.py
    param.py
    repo.py
  fs/  (6 files)
    __init__.py
    callbacks.py
    data.py
    dvc.py
    dvc_path.py
    git.py
  parsing/  (3 files)
    __init__.py
    context.py
    interpolate.py
  render/  (6 files)
    converter/  (3 files)
      … 3 files under this directory
    __init__.py
    convert.py
    match.py
  repo/  (81 files)
    experiments/  (33 files)
      … 33 files under this directory
    metrics/  (3 files)
      … 3 files under this directory
    params/  (3 files)
      … 3 files under this directory
    plots/  (2 files)
      … 2 files under this directory
    __init__.py
    add.py
    artifacts.py
    brancher.py
    cache.py
    checkout.py
    collect.py
    commit.py
    data.py
    datasets.py
    destroy.py
    diff.py
    du.py
    fetch.py
    freeze.py
    gc.py
    get.py
    get_url.py
    graph.py
    imp.py
    imp_db.py
    imp_url.py
    index.py
    init.py
    … 16 more files
  stage/  (10 files)
    __init__.py
    cache.py
    decorators.py
    exceptions.py
    imports.py
    loader.py
    params.py
    run.py
    serialize.py
    utils.py
  testing/  (42 files)
    benchmarks/  (29 files)
      … 29 files under this directory
    README.rst
    __init__.py
    api_tests.py
    cloud.py
    conftest.py
    fixtures.py
    matchers.py
    path_info.py
    plugin.py
    remote_tests.py
    scripts.py
    tmp_dir.py
    workspace_tests.py
  ui/  (4 files)
    __init__.py
    _rich_progress.py
    pager.py
    table.py
  utils/  (22 files)
    serialize/  (6 files)
      … 6 files under this directory
    .gitignore
    __init__.py
    cli_parse.py
    collections.py
    diff.py
    flatten.py
    fs.py
    humanize.py
    hydra.py
    objects.py
    packaging.py
    plots.py
    strictyaml.py
    studio.py
    table.py
    threadpool.py
  __init__.py
  __main__.py
  _debug.py
  analytics.py
  annotations.py
  build.py
  cachemgr.py
  compare.py
  config.py
  config_schema.py
  daemon.py
  dagascii.py
  data_cloud.py
  database.py
  dirs.py
  dvcfile.py
  env.py
  exceptions.py
  ignore.py
  info.py
  lock.py
  log.py
  logger.py
  output.py
  … 9 more files
tests/  (260 files)
  func/  (104 files)
    api/  (6 files)
      … 6 files under this directory
    artifacts/  (2 files)
      … 2 files under this directory
    data/  (3 files)
      … 3 files under this directory
    experiments/  (15 files)
      … 15 files under this directory
    metrics/  (3 files)
      … 3 files under this directory
    params/  (3 files)
      … 3 files under this directory
    parsing/  (7 files)
      … 7 files under this directory
    plots/  (5 files)
      … 5 files under this directory
    repro/  (4 files)
      … 4 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    __init__.py
    test_add.py
    test_analytics.py
    test_check_ignore.py
    test_checkout.py
    test_cli.py
    test_commit.py
    test_config.py
    test_daemon.py
    test_data_cloud.py
    test_data_status.py
    test_dataset.py
    test_diff.py
    test_download.py
    test_du.py
    test_dvcfile.py
    test_external_repo.py
    test_fs.py
    test_gc.py
    test_get.py
    test_get_url.py
    test_ignore.py
    test_import.py
    test_import_db.py
    … 29 more files
  integration/  (7 files)
    plots/  (4 files)
      … 4 files under this directory
    __init__.py
    conftest.py
    test_studio_live_experiments.py
  remotes/  (4 files)
    git-init/  (1 files)
      … 1 files under this directory
    __init__.py
    git_server.py
    user.key.pub
  unit/  (136 files)
    cli/  (2 files)
      … 2 files under this directory
    command/  (34 files)
      … 34 files under this directory
    data/  (3 files)
      … 3 files under this directory
    dependency/  (3 files)
      … 3 files under this directory
    fs/  (8 files)
      … 8 files under this directory
    output/  (5 files)
      … 5 files under this directory
    remote/  (5 files)
      … 5 files under this directory
    render/  (5 files)
      … 5 files under this directory
    repo/  (17 files)
      … 17 files under this directory
    scm/  (2 files)
      … 2 files under this directory
    stage/  (8 files)
      … 8 files under this directory
    ui/  (4 files)
      … 4 files under this directory
    utils/  (13 files)
      … 13 files under this directory
    __init__.py
    test_analytics.py
    test_api.py
    test_collect.py
    test_compare.py
    test_config.py
    test_context.py
    test_daemon.py
    test_dirs.py
    test_dvcfile.py
    test_hashinfo.py
    test_ignore.py
    test_imports.py
    test_info.py
    test_interpolate.py
    test_lockfile.py
    test_logger.py
    test_metrics.py
    test_params.py
    test_pathspec_math.py
    test_progress.py
    test_prompt.py
    test_run.py
    test_rwlock.py
    … 3 more files
  utils/  (3 files)
    __init__.py
    asserts.py
    plots.py
  __init__.py
  conftest.py
  dir_helpers.py
  docker-compose.yml
  remotes_env.sample
  scripts.py
.dvcignore
.git-blame-ignore-revs
.git_archival.txt
.gitattributes
.gitignore
.mailmap
.pre-commit-config.yaml
.pre-commit-hooks.yaml
.zenodo.json
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.rst
pyproject.toml
```

## Entry points

- [dvc/__main__.py:7](https://github.com/treeverse/dvc/blob/b59add99ee667f2b352cc1be337619f965fe3fea/dvc/__main__.py#L7)
- [dvc/cli/__init__.py](https://github.com/treeverse/dvc/blob/b59add99ee667f2b352cc1be337619f965fe3fea/dvc/cli/__init__.py)
- [dvc/parsing/context.py:556](https://github.com/treeverse/dvc/blob/b59add99ee667f2b352cc1be337619f965fe3fea/dvc/parsing/context.py#L556)
- [dvc/ui/__init__.py:369](https://github.com/treeverse/dvc/blob/b59add99ee667f2b352cc1be337619f965fe3fea/dvc/ui/__init__.py#L369)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 8 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: DVCDataset, DatachainDataset, URLDataset, _OpenContextManager. Observed top-level functions: _open, _pos… |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: CmdConfig, Config, ConfigError, NoRemoteError, RemoteConfigError, RemoteNotFoundError… |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AbstractDependency, Client, DbDependency, Serializer. Observed top-level functions: atomic_file, client… |
| dvc package | library | Observed | Groups 253 file(s) under dvc package (observed from repository paths and static analysis). Observed top-level classes: AmbiguousExpRefInfo, Annotation, ApplyStash, ApplyStashEntry, ArgumentDuplicationError, Artifact. Ob… |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CmdExperimentsRun, Console, Container, Context, ContextError, CtxDict. Observed top-level… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 284 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ANY, DVCFixtures, DVCTestConfig, GitRemote, GitSSH, MockedDatachainVersionInfo. Observed top-level functio… |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/codecov.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/release.yml` (config)
- `.github/workflows/benchmarks.yaml` (ci)
- `.github/workflows/build.yaml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/plugin_tests.yaml` (ci)
- `.github/workflows/tests.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.pre-commit-hooks.yaml` (config)
- `.zenodo.json` (config)
- `pyproject.toml` (manifest)
- `tests/docker-compose.yml` (container)

## Top-level layout

- `dvc` — 300 analysed file(s)
- `tests` — 260 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 12 analysed file(s)
- `.dvc` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b59add99ee667f2b352cc1be337619f965fe3fea` is the revision these paths and observations refer to.
