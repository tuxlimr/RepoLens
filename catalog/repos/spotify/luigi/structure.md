# Project structure: spotify/luigi

**Analysed commit:** `f5feb7a4655ad73ef56f0ab04d7903ab43b63e12`

**Commit reference:** [f5feb7a4655ad73ef56f0ab04d7903ab43b63e12](https://github.com/spotify/luigi/commit/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12)

**Tree at this commit:** [spotify/luigi@f5feb7a4655a](https://github.com/spotify/luigi/tree/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | spotify/luigi |
| Description | Luigi is a Python module that helps you build complex pipelines of batch jobs. It handles dependency resolution, workflow management, visualization etc. It also comes with Hadoop support built in. |
| Stars | 18788 |
| Forks | 2474 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `f5feb7a4655ad73ef56f0ab04d7903ab43b63e12` |
| Retrieved at | 2026-11-14T19:08:21.039658+00:00 |
| Files in this snapshot | 331 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (2 files)
    codeql.yml
    pythonbuild.yml
  CODEOWNERS
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  stale.yml
bin/  (2 files)
  luigi
  luigid
doc/  (16 files)
  .gitignore
  Makefile
  central_scheduler.rst
  conf.py
  configuration.rst
  design_and_limitations.rst
  example_top_artists.rst
  execution_model.rst
  index.rst
  logging.rst
  luigi_patterns.rst
  mypy.rst
  parameters.rst
  running_luigi.rst
  tasks.rst
  workflows.rst
examples/  (19 files)
  __init__.py
  config.toml
  dynamic_requirements.py
  elasticsearch_index.py
  execution_summary_example.py
  foo.py
  foo_complex.py
  ftp_experiment_outputs.py
  hello_world.py
  kubernetes.py
  per_task_retry_policy.py
  pyspark_wc.py
  spark_als.py
  ssh_remote_execution.py
  terasort.py
  top_artists.py
  top_artists_spark.py
  wordcount.py
  wordcount_hadoop.py
luigi/  (124 files)
  configuration/  (5 files)
    __init__.py
    base_parser.py
    cfg_parser.py
    core.py
    toml_parser.py
  contrib/  (58 files)
    hdfs/  (9 files)
      … 9 files under this directory
    __init__.py
    azureblob.py
    batch.py
    beam_dataflow.py
    bigquery.py
    bigquery_avro.py
    datadog_metric.py
    dataproc.py
    docker_runner.py
    dropbox.py
    ecs.py
    esindex.py
    external_daily_snapshot.py
    external_program.py
    ftp.py
    gcp.py
    gcs.py
    hadoop.py
    hadoop_jar.py
    hive.py
    kubernetes.py
    lsf.py
    lsf_runner.py
    mongodb.py
    … 25 more files
  static/  (16 files)
    visualiser/  (16 files)
      … 16 files under this directory
  templates/  (5 files)
    history.html
    layout.html
    menu.html
    recent.html
    show.html
  tools/  (5 files)
    __init__.py
    deps.py
    deps_tree.py
    luigi_grep.py
    range.py
  __init__.py
  __main__.py
  __version__.py
  batch_notifier.py
  cmdline.py
  cmdline_parser.py
  date_interval.py
  db_task_history.py
  event.py
  execution_summary.py
  format.py
  freezing.py
  interface.py
  local_target.py
  lock.py
  metrics.py
  mock.py
  mypy.py
  notifications.py
  parameter.py
  process.py
  py.typed
  retcodes.py
  rpc.py
  … 11 more files
scripts/  (4 files)
  ci/  (4 files)
    conditional_tox.sh
    install_start_azurite.sh
    setup_hadoop_env.sh
    stop_azurite.sh
test/  (148 files)
  auto_namespace_test/  (2 files)
    __init__.py
    my_namespace_test.py
  contrib/  (45 files)
    hdfs/  (1 files)
      … 1 files under this directory
    __init__.py
    _webhdfs_test.py
    azureblob_test.py
    batch_test.py
    beam_dataflow_test.py
    bigquery_avro_test.py
    bigquery_gcloud_test.py
    bigquery_test.py
    cascading_test.py
    datadog_metric_test.py
    dataproc_test.py
    docker_runner_test.py
    dropbox_test.py
    ecs_test.py
    esindex_test.py
    external_daily_snapshot_test.py
    external_program_test.py
    gcs_test.py
    hadoop_jar_test.py
    hadoop_test.py
    hdfs_test.py
    hive_test.py
    kubernetes_test.py
    lsf_test.py
    … 20 more files
  create_packages_archive_root/  (8 files)
    package/  (6 files)
      … 6 files under this directory
    package.egg-info/  (1 files)
      … 1 files under this directory
    module.py
  testconfig/  (8 files)
    core-site.xml
    log4j.properties
    logging.cfg
    luigi.cfg
    luigi.toml
    luigi_local.toml
    luigi_logging.toml
    pyproject.toml
  visualiser/  (3 files)
    __init__.py
    phantomjs_test.js
    visualiser_test.py
  _mysqldb_test.py
  _test_ftp.py
  batch_notifier_test.py
  choice_parameter_test.py
  clone_test.py
  cmdline_test.py
  config_env_test.py
  config_toml_test.py
  conftest.py
  custom_metrics_test.py
  customized_run_test.py
  date_interval_test.py
  date_parameter_test.py
  db_task_history_test.py
  decorator_test.py
  dict_parameter_test.py
  dynamic_import_test.py
  event_callbacks_test.py
  execution_summary_test.py
  factorial_test.py
  fib_test.py
  hdfs_client_test.py
  helpers.py
  helpers_test.py
  … 58 more files
.coveragerc
.gitignore
.readthedocs.yaml
CONTRIBUTING.rst
LICENSE
README.rst
RELEASE-PROCESS.rst
SECURITY.md
catalog-info.yaml
codecov.yml
pyproject.toml
tox.ini
```

## Entry points

- [luigi/__main__.py:19](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/__main__.py#L19)
- [luigi/cmdline.py](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/cmdline.py)
- [luigi/cmdline.py](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/cmdline.py)
- [luigi/contrib/lsf_runner.py:79](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/contrib/lsf_runner.py#L79)
- [luigi/contrib/mrrunner.py:95](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/contrib/mrrunner.py#L95)
- [luigi/contrib/pyspark_runner.py:133](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/contrib/pyspark_runner.py#L133)
- [luigi/contrib/sge_runner.py:93](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/contrib/sge_runner.py#L93)
- [luigi/server.py:378](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/server.py#L378)
- [luigi/tools/deps.py](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/tools/deps.py)
- [luigi/tools/deps_tree.py](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/tools/deps_tree.py)
- [luigi/tools/luigi_grep.py](https://github.com/spotify/luigi/blob/f5feb7a4655ad73ef56f0ab04d7903ab43b63e12/luigi/tools/luigi_grep.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: hadoopcli, hdfs. Observed top-level functions: get_configured_hadoop_version, get_con… |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AbstractPySparkRunner, AllRunHandler, BaseTaskHistoryHandler, ByIdHandler, ByNameHandler,… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: HdfsFileSystem, WebHdfsClient, webhdfs. |
| luigi package | library | Observed | Groups 97 file(s) under luigi package (observed from repository paths and static analysis). Observed top-level classes: ApacheHiveCommandClient, AsyncCompletionException, AtomicAzureBlobFile, AtomicFtpFile, AtomicGCSFil… |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 149 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH logging.getLogger, PATCH logging.getLogger, PATCH logging.getLogger, PATCH logging.getLogger, PATCH logging.get… |

## Important files

- `.github/stale.yml` (config)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/pythonbuild.yml` (ci)
- `.readthedocs.yaml` (config)
- `catalog-info.yaml` (config)
- `codecov.yml` (config)
- `examples/config.toml` (config)
- `pyproject.toml` (manifest)
- `tox.ini` (config)

## Top-level layout

- `test` — 148 analysed file(s)
- `luigi` — 124 analysed file(s)
- `examples` — 19 analysed file(s)
- `doc` — 16 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 6 analysed file(s)
- `scripts` — 4 analysed file(s)
- `bin` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (9 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f5feb7a4655ad73ef56f0ab04d7903ab43b63e12` is the revision these paths and observations refer to.
