# Project structure: redis/redis-py

**Analysed commit:** `68b1342409df85537264b50418fc8a8bcb2dd0c7`

**Commit reference:** [68b1342409df85537264b50418fc8a8bcb2dd0c7](https://github.com/redis/redis-py/commit/68b1342409df85537264b50418fc8a8bcb2dd0c7)

**Tree at this commit:** [redis/redis-py@68b1342409df](https://github.com/redis/redis-py/tree/68b1342409df85537264b50418fc8a8bcb2dd0c7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | redis/redis-py |
| Description | Redis Python client |
| Stars | 13664 |
| Forks | 2835 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `68b1342409df85537264b50418fc8a8bcb2dd0c7` |
| Retrieved at | 2026-11-14T19:09:44.868783+00:00 |
| Files in this snapshot | 440 |

## Directory tree

```text
.agents/  (13 files)
  references/  (2 files)
    command-metadata.md
    maint-notifications.md
  skills/  (10 files)
    add-new-command/  (2 files)
      … 2 files under this directory
    generate-release-notes/  (3 files)
      … 3 files under this directory
    maintainer-review/  (2 files)
      … 2 files under this directory
    pr-draft-summary/  (1 files)
      … 1 files under this directory
    prepare-for-takeover/  (1 files)
      … 1 files under this directory
    sync-claude-md/  (1 files)
      … 1 files under this directory
  sync_async_type_hints_overload_guide.md
.github/  (17 files)
  actions/  (1 files)
    run-tests/  (1 files)
      … 1 files under this directory
  workflows/  (10 files)
    benchmarks.yaml
    codeql-analysis.yml
    docs.yaml
    hiredis-py-integration.yaml
    install_and_test.sh
    integration.yaml
    nightly-metrics.yaml
    pypi-publish.yaml
    spellcheck.yml
    stale-issues.yml
  CODEOWNERS
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  spellcheck-settings.yml
  wordlist.txt
benchmarks/  (24 files)
  measure_read_path/  (12 files)
    .gitignore
    __init__.py
    ci_matrix.py
    csc_bench.py
    gate.py
    mem_probe.py
    parser_micro.py
    prepare_worktrees.sh
    recorder_micro.py
    routing_micro.py
    run_bench.py
    worker.py
  README.md
  __init__.py
  base.py
  basic_operations.py
  client_side_caching.py
  cluster_async.py
  cluster_async_pipeline.py
  command_packer_benchmark.py
  connection_handshake.py
  otel_benchmark.py
  requirements.txt
  socket_read_size.py
dockers/  (1 files)
  sentinel.conf
docs/  (45 files)
  _static/  (2 files)
    .keep
    logo-redis.svg
  _templates/  (1 files)
    .keep
  examples/  (22 files)
    opentelemetry/  (8 files)
      … 8 files under this directory
    README.md
    asyncio_examples.ipynb
    connection_examples.ipynb
    hash_examples.ipynb
    opentelemetry_api_examples.ipynb
    pipeline_examples.ipynb
    pubsub_examples.ipynb
    redis-stream-example.ipynb
    search_json_examples.ipynb
    search_vector_similarity_examples.ipynb
    set_and_get_examples.ipynb
    sorted_set_examples.ipynb
    ssl_connection_examples.ipynb
    timeseries_examples.ipynb
  Makefile
  advanced_features.rst
  backoff.rst
  clustering.rst
  commands.rst
  conf.py
  connections.rst
  examples.rst
  exceptions.rst
  genindex.rst
  geographic_failover.rst
  index.rst
  lock.rst
  lua_scripting.rst
  opentelemetry.rst
  redismodules.rst
  requirements.txt
  resp3_features.rst
  retry.rst
  unified_responses.rst
doctests/  (44 files)
  data/  (2 files)
    query_em.json
    query_vector.json
  README.md
  cmds_cnxmgmt.py
  cmds_generic.py
  cmds_hash.py
  cmds_list.py
  cmds_servermgmt.py
  cmds_set.py
  cmds_sorted_set.py
  cmds_string.py
  dt_bitfield.py
  dt_bitmap.py
  dt_bloom.py
  dt_cms.py
  dt_cuckoo.py
  dt_geo.py
  dt_hash.py
  dt_hll.py
  dt_json.py
  dt_list.py
  dt_set.py
  dt_ss.py
  dt_stream.py
  dt_string.py
  dt_tdigest.py
  … 18 more files
redis/  (118 files)
  _parsers/  (10 files)
    __init__.py
    base.py
    commands.py
    encoders.py
    helpers.py
    hiredis.py
    resp2.py
    resp3.py
    response_callbacks.py
    socket.py
  asyncio/  (23 files)
    http/  (2 files)
      … 2 files under this directory
    multidb/  (9 files)
      … 9 files under this directory
    observability/  (2 files)
      … 2 files under this directory
    __init__.py
    _himport_exec.py
    client.py
    connection.py
    keyspace_notifications.py
    lock.py
    maint_notifications.py
    retry.py
    sentinel.py
    utils.py
  auth/  (5 files)
    __init__.py
    err.py
    idp.py
    token.py
    token_manager.py
  commands/  (38 files)
    bf/  (3 files)
      … 3 files under this directory
    json/  (5 files)
      … 5 files under this directory
    search/  (16 files)
      … 16 files under this directory
    timeseries/  (4 files)
      … 4 files under this directory
    vectorset/  (3 files)
      … 3 files under this directory
    __init__.py
    cluster.py
    helpers.py
    metadata.py
    policies.py
    redismodules.py
    sentinel.py
  http/  (2 files)
    __init__.py
    http_client.py
  multidb/  (10 files)
    __init__.py
    circuit.py
    client.py
    command_executor.py
    config.py
    database.py
    event.py
    exception.py
    failover.py
    failure_detector.py
  observability/  (7 files)
    __init__.py
    attributes.py
    config.py
    metrics.py
    providers.py
    recorder.py
    registry.py
  __init__.py
  _defaults.py
  _himport_exec.py
  background.py
  backoff.py
  cache.py
  client.py
  crc.py
  credentials.py
  data_structure.py
  driver_info.py
  event.py
  exceptions.py
  himport.py
  keyspace_notifications.py
  lock.py
  maint_notifications.py
  ocsp.py
  py.typed
  retry.py
  sentinel.py
  typing.py
  utils.py
specs/  (4 files)
  keyspace-notifications/  (1 files)
    SPEC.md
  redis_commands_guide.md
  sync_async_deduplication_analysis.md
  unified_responses_migration_guide.md
tests/  (155 files)
  maint_notifications/  (7 files)
    proxy_server_helpers.py
    test_async_cluster_maint_notifications_handling.py
    test_async_maint_notifications_handling.py
    test_cluster_maint_notifications_handling.py
    test_connection_diagnostic_logging.py
    test_maint_notifications.py
    test_maint_notifications_handling.py
  test_asyncio/  (61 files)
    test_multidb/  (11 files)
      … 11 files under this directory
    test_observability/  (3 files)
      … 3 files under this directory
    test_scenario/  (6 files)
      … 6 files under this directory
    testdata/  (2 files)
      … 2 files under this directory
    __init__.py
    compat.py
    conftest.py
    helpers.py
    mocks.py
    test_bloom.py
    test_client.py
    test_cluster_transaction.py
    test_command_metadata.py
    test_command_parser.py
    test_command_policies.py
    test_connect.py
    test_connection.py
    test_connection_pool.py
    test_credentials.py
    test_cwe_404.py
    test_encoding.py
    test_function.py
    test_hash.py
    test_hello_fallback.py
    test_himport_integration.py
    test_http_client.py
    test_json.py
    test_keyspace_notifications.py
    … 15 more files
  test_auth/  (3 files)
    __init__.py
    test_token.py
    test_token_manager.py
  test_http/  (2 files)
    __init__.py
    test_http_client.py
  test_multidb/  (12 files)
    __init__.py
    _integration_endpoints.py
    conftest.py
    test_circuit.py
    test_client.py
    test_command_executor.py
    test_config.py
    test_event.py
    test_failover.py
    test_failure_detector.py
    test_integration.py
    test_pipeline.py
  test_observability/  (7 files)
    __init__.py
    test_cluster_metrics_error_handling.py
    test_config.py
    test_metrics_connection_attributes.py
    test_provider.py
    test_public_api.py
    test_recorder.py
  test_parsers/  (2 files)
    test_errors.py
    test_helpers.py
  test_scenario/  (7 files)
    __init__.py
    conftest.py
    fault_injector_client.py
    maint_notifications_helpers.py
    test_active_active.py
    test_maint_notifications.py
    test_pubsub.py
  testdata/  (2 files)
    jsontestdata.py
    titles.csv
  __init__.py
  conftest.py
  entraid_utils.py
  helpers.py
  mocks.py
  ssl_utils.py
  test_background.py
  test_backoff.py
  test_bloom.py
  test_cache.py
  test_client.py
  test_cluster_transaction.py
  test_command_metadata.py
  test_command_parser.py
  test_command_policies.py
  test_connect.py
  test_connection.py
  test_connection_pool.py
  test_crc.py
  test_credentials.py
  test_data_structure.py
  test_defaults.py
  test_driver_info.py
  test_encoding.py
  … 28 more files
util/  (1 files)
  wait-for-it.sh
.coveragerc
.dockerignore
.gitignore
.mypy.ini
.readthedocs.yml
AGENTS.md
CHANGES
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
codecov.yml
dev_requirements.txt
docker-compose.yml
pyproject.toml
tasks.py
whitelist.py
```

## Entry points

- [benchmarks/basic_operations.py:192](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/basic_operations.py#L192)
- [benchmarks/client_side_caching.py:708](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/client_side_caching.py#L708)
- [benchmarks/cluster_async.py:247](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/cluster_async.py#L247)
- [benchmarks/cluster_async_pipeline.py:95](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/cluster_async_pipeline.py#L95)
- [benchmarks/command_packer_benchmark.py:89](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/command_packer_benchmark.py#L89)
- [benchmarks/connection_handshake.py:185](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/connection_handshake.py#L185)
- [benchmarks/measure_read_path/ci_matrix.py:77](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/measure_read_path/ci_matrix.py#L77)
- [benchmarks/measure_read_path/csc_bench.py:242](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/measure_read_path/csc_bench.py#L242)
- [benchmarks/measure_read_path/mem_probe.py:333](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/measure_read_path/mem_probe.py#L333)
- [benchmarks/measure_read_path/parser_micro.py:327](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/measure_read_path/parser_micro.py#L327)
- [benchmarks/measure_read_path/recorder_micro.py:321](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/measure_read_path/recorder_micro.py#L321)
- [benchmarks/measure_read_path/routing_micro.py:348](https://github.com/redis/redis-py/blob/68b1342409df85537264b50418fc8a8bcb2dd0c7/benchmarks/measure_read_path/routing_micro.py#L348)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 5 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level classes: Benchmark. Observed top-level functions: add_gate_args, annotation, compare_pairs, delta_uncert… |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: DatabaseConfig, InitialHealthCheck, MetricGroup, MultiDbConfig, OTelConfig, Telemetr… |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: _ensure_junit_results_dir, _legacy_arg, _legacy_tag, _protocol_arg, _protocol_tag, all_tests. |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AbstractDatabase, AsyncDatabase, BaseDatabase, Database, SyncDatabase. |
| doctests package | library | Observed | Groups 40 file(s) under doctests package (observed from repository paths and static analysis). Observed top-level functions: create_query_table, embed_text, watched_sequence. |
| Application entry point | entrypoint | Observed | Groups 16 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AsyncComprehensiveLoadGenerator, BenchmarkResult, BenchmarkSummary, BufferSocket, Command… |
| External integrations | external | Observed | Groups 6 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AbstractRedis, AsyncHTTPClient, AsyncHTTPClientWrapper, AsyncPubsubWorkerExceptionHandler, A… |
| redis package | library | Observed | Groups 106 file(s) under redis package (observed from repository paths and static analysis). Observed top-level classes: AbstractAsyncKeyspaceNotifications, AbstractBackoff, AbstractBloom, AbstractCommandsParser, Abstra… |
| Tests | test | Observed | Groups 155 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH redis.asyncio.cluster.random.shuffle, PATCH redis.cluster.random.shuffle, PATCH redis.cluster.random.shuffle, P… |
| util package | library | Observed | Groups 1 file(s) under util package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/actions/run-tests/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/spellcheck-settings.yml` (config)
- `.github/workflows/benchmarks.yaml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/docs.yaml` (ci)
- `.github/workflows/hiredis-py-integration.yaml` (ci)
- `.github/workflows/install_and_test.sh` (ci)
- `.github/workflows/integration.yaml` (ci)
- `.github/workflows/nightly-metrics.yaml` (ci)
- `.github/workflows/pypi-publish.yaml` (ci)
- `.github/workflows/spellcheck.yml` (ci)
- `.github/workflows/stale-issues.yml` (ci)
- `.mypy.ini` (config)
- `.readthedocs.yml` (config)
- `benchmarks/requirements.txt` (manifest)
- `codecov.yml` (config)
- `docker-compose.yml` (container)
- `docs/examples/opentelemetry/config/alertmanager.yml` (config)
- `docs/examples/opentelemetry/config/otel-collector.yaml` (config)
- `docs/examples/opentelemetry/config/vector.toml` (config)
- `docs/examples/opentelemetry/docker-compose.yml` (container)
- `docs/examples/opentelemetry/requirements.txt` (manifest)
- `docs/examples/opentelemetry/uptrace.yml` (config)
- `docs/requirements.txt` (manifest)
- `doctests/data/query_em.json` (config)
- `doctests/data/query_vector.json` (config)
- `doctests/requirements.txt` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 155 analysed file(s)
- `redis` — 118 analysed file(s)
- `docs` — 45 analysed file(s)
- `doctests` — 44 analysed file(s)
- `benchmarks` — 24 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 17 analysed file(s)
- `.agents` — 13 analysed file(s)
- `specs` — 4 analysed file(s)
- `dockers` — 1 analysed file(s)
- `util` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `68b1342409df85537264b50418fc8a8bcb2dd0c7` is the revision these paths and observations refer to.
