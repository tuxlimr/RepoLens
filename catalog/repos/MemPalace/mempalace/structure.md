# Project structure: MemPalace/mempalace

**Analysed commit:** `9fc486dc0ce259131da20179847314cabcbb9e15`

**Commit reference:** [9fc486dc0ce259131da20179847314cabcbb9e15](https://github.com/MemPalace/mempalace/commit/9fc486dc0ce259131da20179847314cabcbb9e15)

**Tree at this commit:** [MemPalace/mempalace@9fc486dc0ce2](https://github.com/MemPalace/mempalace/tree/9fc486dc0ce259131da20179847314cabcbb9e15)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | MemPalace/mempalace |
| Description | The best-benchmarked open-source AI memory system. And it's free. |
| Stars | 60556 |
| Forks | 7669 |
| Licence | MIT |
| Language | Python |
| Default branch | develop |
| Analysed commit | `9fc486dc0ce259131da20179847314cabcbb9e15` |
| Retrieved at | 2026-11-14T19:06:24.484271+00:00 |
| Files in this snapshot | 561 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.claude-plugin/  (18 files)
  commands/  (6 files)
    audit.md
    help.md
    init.md
    mine.md
    search.md
    status.md
  hooks/  (5 files)
    hooks.json
    mempal-precompact-hook.sh
    mempal-session-end-hook.sh
    mempal-stop-hook.sh
    mempal_hook_run.sh
  skills/  (3 files)
    mempalace/  (1 files)
      … 1 files under this directory
    mempalace-recall/  (1 files)
      … 1 files under this directory
    mempalace-task/  (1 files)
      … 1 files under this directory
  .mcp.json
  README.md
  marketplace.json
  plugin.json
.codex-plugin/  (11 files)
  hooks/  (2 files)
    mempal-hook.sh
    mempal_hook_run.sh
  skills/  (6 files)
    audit/  (1 files)
      … 1 files under this directory
    help/  (1 files)
      … 1 files under this directory
    init/  (1 files)
      … 1 files under this directory
    mine/  (1 files)
      … 1 files under this directory
    search/  (1 files)
      … 1 files under this directory
    status/  (1 files)
      … 1 files under this directory
  README.md
  hooks.json
  plugin.json
.cursor-plugin/  (4 files)
  README.md
  marketplace.json
  mcp.json
  plugin.json
.devcontainer/  (2 files)
  devcontainer.json
  post-create.sh
.dsh-plugin/  (14 files)
  lib/  (4 files)
    autosave.js
    palace.js
    recall.js
    transcript.js
  test/  (7 files)
    agent-created.test.mjs
    autosave.test.mjs
    host.mjs
    manifest.test.mjs
    palace.test.mjs
    read-retry.test.mjs
    recall.test.mjs
  README.md
  cordis.patch.yml
  package.json
.github/  (13 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (7 files)
    bump-plugin-version.yml.disabled
    ci.yml
    deploy-docs.yml
    docker-publish.yml
    publish.yml
    release-native.yml
    version-guard.yml
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
  coverage-milvus.toml
  dependabot.yml
benchmarks/  (116 files)
  lean_mempalace/  (15 files)
    go/  (5 files)
      … 5 files under this directory
    rust/  (2 files)
      … 2 files under this directory
    ts_bun/  (4 files)
      … 4 files under this directory
    README.md
    bench_python.py
    benchmark_results.json
    runner.py
  model_eval/  (79 files)
    datasets/  (47 files)
      … 47 files under this directory
    reports/  (4 files)
      … 4 files under this directory
    results/  (7 files)
      … 7 files under this directory
    tasks/  (13 files)
      … 13 files under this directory
    README.md
    __init__.py
    candidates.yaml
    metrics.py
    orchestrator.py
    runner.py
    summarize.py
    translate_datasets.py
  BENCHMARKS.md
  HYBRID_MODE.md
  PRIVATE_PALACE.md
  README.md
  convomem_bench.py
  lme_split_50_450.json
  locomo_bench.py
  longmemeval_bench.py
  membench_bench.py
  mine_bench.py
  private_palace_bench.py
  results_convomem_raw_top10_20260414_1649.json
  results_high_sensitivity_stress.json
  results_ninfer_qwen27b.json
  results_ollama_medical_palace.json
  results_ollama_ornith_routine.json
  search_benchmark.py
  soak_test_rust_exact.py
  test_ninfer_qwen27b.py
  test_ollama_high_sensitivity.py
  test_ollama_medical_private_palace.py
  test_ollama_ornith_routine.py
commands/  (6 files)
  mempalace-audit.md
  mempalace-help.md
  mempalace-init.md
  mempalace-mine.md
  mempalace-search.md
  mempalace-status.md
crates/  (9 files)
  mempalace-cli/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    Cargo.toml
  mempalace-core/  (2 files)
    src/  (1 files)
      … 1 files under this directory
    Cargo.toml
  mempalace-py/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    Cargo.toml
    pyproject.toml
  README.md
deploy/  (3 files)
  docker-compose.server.yml
  mempalace-server.service
  server.env.example
docs/  (19 files)
  recovery/  (2 files)
    index-metadata-recovery.md
    wing-name-migration.md
  rfcs/  (6 files)
    001-storage-backend-plugin-spec.md
    002-source-adapter-plugin-spec.md
    003-agent-logstream-coordination.md
    004-replicated-palace.md
    005-agent-identity-routing.md
    007-source-revision-publication.md
  CLOSETS.md
  HISTORY.md
  RELEASING.md
  authored-at.md
  cli-write-routing.md
  embeddinggemma2.md
  format-coverage.md
  hook-write-routing.md
  schema.sql
  virtual-line-numbering.md
  write-routing-policy.md
examples/  (16 files)
  antigravity/  (3 files)
    README.md
    hooks.json
    mcp_config.json
  cursor/  (6 files)
    rules/  (3 files)
      … 3 files under this directory
    README.md
    hooks.json
    hooks.minimal.json
  HOOKS_TUTORIAL.md
  basic_mining.py
  convo_import.py
  gemini_cli_setup.md
  mcp_setup.md
  mx3_public_shim_embeddings_rerank.md
  mx3_public_shim_embeddings_rerank.py
hooks/  (21 files)
  antigravity/  (9 files)
    lib/  (1 files)
      … 1 files under this directory
    INVESTIGATION.md
    README.md
    STDIN_SHAPE.md
    export_standalone.py
    hooks.json.tmpl
    install.sh
    mempal_save_hook_antigravity.sh
    mempal_wake_hook_antigravity.sh
  cursor/  (7 files)
    lib/  (1 files)
      … 1 files under this directory
    README.md
    STDIN_SHAPE.md
    install.sh
    mempal_precompact_hook_cursor.sh
    mempal_save_hook_cursor.sh
    mempal_wake_hook_cursor.sh
  README.md
  mempal_hook_run.sh
  mempal_precompact_hook.sh
  mempal_save_hook.sh
  mempal_session_end_hook.sh
integrations/  (5 files)
  openclaw/  (3 files)
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  shared/  (2 files)
    coordination-protocol.md
    recall-protocol.md
landing/  (1 files)
  index.html
mempalace/  (185 files)
  backends/  (16 files)
    __init__.py
    _filters.py
    _inproc_sqlite.py
    _magic.py
    _remote_common.py
    _sidecar.py
    base.py
    chroma.py
    chroma_sqlite.py
    embedding_wrapper.py
    milvus.py
    pgvector.py
    qdrant.py
    registry.py
    rust_exact.py
    sqlite_exact.py
  cli/  (18 files)
    __init__.py
    __main__.py
    _common.py
    _hub.py
    cmd_audit.py
    cmd_coord.py
    cmd_init.py
    cmd_kg.py
    cmd_mine.py
    cmd_query.py
    cmd_repair.py
    cmd_rooms.py
    cmd_serve.py
    cmd_sync.py
    cmd_tunnels.py
    cmd_update.py
    cmd_wings.py
    parser.py
  data/  (2 files)
    coca_content_words.json
    known_systems.json
  i18n/  (15 files)
    __init__.py
    be.json
    de.json
    en.json
    es.json
    fr.json
    hi.json
    id.json
    it.json
    ja.json
    ko.json
    pt-br.json
    ru.json
    zh-CN.json
    zh-TW.json
  instructions/  (7 files)
    audit.md
    help.md
    init.md
    mine.md
    search.md
    shared_brain_rules.md
    status.md
  integrations/  (2 files)
    hermes/  (1 files)
      … 1 files under this directory
    __init__.py
  mcp_server/  (14 files)
    __init__.py
    __main__.py
    _guards.py
    _logging.py
    _session.py
    http.py
    protocol.py
    runtime.py
    schemas.py
    tools_coord.py
    tools_diary.py
    tools_kg.py
    tools_read.py
    tools_write.py
  palace/  (8 files)
    __init__.py
    backend.py
    closets.py
    collection.py
    mine_lock.py
    mined.py
    palace_lock.py
    writes.py
  searcher/  (9 files)
    __init__.py
    candidates.py
    cli_search.py
    filters.py
    media_search.py
    query.py
    ranking.py
    render.py
    sqlite_bm25.py
  sources/  (6 files)
    __init__.py
    base.py
    context.py
    media.py
    registry.py
    transforms.py
  README.md
  __init__.py
  __main__.py
  _env.py
  _mine_exit_watchdog.py
  _net.py
  _once.py
  _proc.py
  _stdio.py
  backups.py
  cli_write_routing.py
  closet_llm.py
  collision_scan.py
  config.py
  convo_miner.py
  convo_scanner.py
  corpus_origin.py
  daemon.py
  date_window.py
  dialect.py
  diary_ingest.py
  dynamics.py
  embedding.py
  embeddinggemma2.py
  … 64 more files
plugins/  (18 files)
  mempalace/  (18 files)
    assets/  (1 files)
      … 1 files under this directory
    rules/  (1 files)
      … 1 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    sidecars/  (6 files)
      … 6 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    LICENSE
    README.md
    hooks.json
    mcp_config.json
    plugin.json
rules/  (1 files)
  mempalace-recall.mdc
scripts/  (4 files)
  backfill_authored_at.py
  check_versions.py
  docker-smoke.sh
  mempalace_repair_encoding.py
skills/  (3 files)
  mempalace/  (1 files)
    SKILL.md
  mempalace-recall/  (1 files)
    SKILL.md
  mempalace-task/  (1 files)
    SKILL.md
tests/  (69 files)
  benchmarks/  (17 files)
    README.md
    __init__.py
    benchmark_dialect.py
    conftest.py
    data_generator.py
    report.py
    test_chromadb_stress.py
    test_ingest_bench.py
    test_knowledge_graph_bench.py
    test_layers_bench.py
    test_mcp_bench.py
    test_mcp_light_bench.py
    test_memory_profile.py
    test_palace_boost.py
    test_performance_budgets.py
    test_recall_threshold.py
    test_search_bench.py
  mcp/  (12 files)
    __init__.py
    test_argument_validation.py
    test_diary.py
    test_guards.py
    test_kg.py
    test_protocol.py
    test_read_tools.py
    test_search.py
    test_stale_library.py
    test_tool_capabilities.py
    test_wing_aliases.py
    test_write_tools.py
  _backend_conformance.py
  _chroma_palace_helper.py
  _mcp_server_helpers.py
  conftest.py
  coverage_gate.py
  test_aaak_collection.py
  test_al_ps1_readable_extensions.py
  test_antigravity_hooks_install.py
  test_antigravity_hooks_shell.py
  test_antigravity_node_hooks.py
  test_antigravity_plugin_manifest.py
  test_antigravity_sidecar_pagination.py
  test_audit_skill_wiring.py
  test_backend_conformance.py
  test_backend_header_probe_locks.py
  test_backends.py
  test_backfill_authored_at.py
  test_backups.py
  test_bookkeeping_rows.py
  test_bulk_drawer_tools.py
  test_chroma_caller_vectors.py
  test_chroma_collection_lock.py
  test_chroma_listing_snapshot.py
  test_chroma_metadata_contracts.py
  … 16 more files
website/  (1 files)
  .vitepress/  (1 files)
    theme/  (1 files)
      … 1 files under this directory
.dockerignore
.gitattributes
.gitignore
.mcp.json
.pre-commit-config.yaml
.python-version
CLAUDE.md
CONTRIBUTING.md
Cargo.toml
Dockerfile
Dockerfile.gpu
LICENSE
MISSION.md
README.md
ROADMAP.md
SECURITY.md
docker-compose.yml
docker-entrypoint.sh
mcp.json
openarena-claim.txt
pyproject.toml
```

## Entry points

- [benchmarks/convomem_bench.py:314](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/convomem_bench.py#L314)
- [benchmarks/lean_mempalace/bench_python.py:202](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/lean_mempalace/bench_python.py#L202)
- [benchmarks/lean_mempalace/runner.py:76](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/lean_mempalace/runner.py#L76)
- [benchmarks/locomo_bench.py:960](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/locomo_bench.py#L960)
- [benchmarks/longmemeval_bench.py:3265](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/longmemeval_bench.py#L3265)
- [benchmarks/membench_bench.py:431](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/membench_bench.py#L431)
- [benchmarks/mine_bench.py:297](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/mine_bench.py#L297)
- [benchmarks/model_eval/orchestrator.py:299](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/model_eval/orchestrator.py#L299)
- [benchmarks/model_eval/runner.py:508](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/model_eval/runner.py#L508)
- [benchmarks/model_eval/summarize.py:334](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/model_eval/summarize.py#L334)
- [benchmarks/model_eval/translate_datasets.py:212](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/model_eval/translate_datasets.py#L212)
- [benchmarks/private_palace_bench.py:7](https://github.com/MemPalace/mempalace/blob/9fc486dc0ce259131da20179847314cabcbb9e15/benchmarks/private_palace_bench.py#L7)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 18 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level classes: HostInfo, TimingAggregate, TimingSample, VRAMPoller. Observed top-level functions: _is_valid,… |
| Configuration and deployment | config | Observed | Groups 42 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: MempalaceConfig. Observed top-level functions: _cursor_wing_slug, _is_wal_without_si… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| crates package | library | Observed | Groups 3 file(s) under crates package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 36 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BenchmarkCase, DaemonClient, DaemonError, DaemonRuntime, DaemonWaitTimeout, Dialect. Obse… |
| External integrations | external | Observed | Groups 4 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AnthropicProvider, HubClient, LLMError, LLMProvider, LLMResponse, MempalaceProvider. Observe… |
| hooks package | library | Observed | Groups 13 file(s) under hooks package (observed from repository paths and static analysis). |
| mempalace package | library | Observed | Groups 136 file(s) under mempalace package (observed from repository paths and static analysis). Observed top-level classes: AdapterClosedError, AdapterSchema, AuthRequiredError, BackendClosedError, BackendError, Backen… |
| plugins package | library | Observed | Groups 5 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level functions: _apply_backend, _capture, _daemon_result_from_mcp_refusal, _restores_palace_env, execute_… |
| Tests | test | Observed | Groups 86 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH mempalace.cli.MempalaceConfig, PATCH mempalace.cli.MempalaceConfig, PATCH mempalace.cli.MempalaceConfig, PATCH m… |
| website package | library | Observed | Groups 1 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/.mcp.json` (config)
- `.claude-plugin/hooks/hooks.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.codex-plugin/hooks.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.cursor-plugin/marketplace.json` (config)
- `.cursor-plugin/mcp.json` (config)
- `.cursor-plugin/plugin.json` (config)
- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.dsh-plugin/cordis.patch.yml` (config)
- `.dsh-plugin/package.json` (manifest)
- `.github/coverage-milvus.toml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/bump-plugin-version.yml.disabled` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-docs.yml` (ci)
- `.github/workflows/docker-publish.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/release-native.yml` (ci)
- `.github/workflows/version-guard.yml` (ci)
- `.mcp.json` (config)
- `.pre-commit-config.yaml` (config)
- `Cargo.toml` (manifest)
- `Dockerfile` (container)
- `Dockerfile.gpu` (container)
- `benchmarks/lean_mempalace/benchmark_results.json` (config)
- `benchmarks/lean_mempalace/go/go.mod` (manifest)
- `benchmarks/lean_mempalace/rust/Cargo.toml` (manifest)
- `benchmarks/lme_split_50_450.json` (config)
- `benchmarks/model_eval/candidates.yaml` (config)
- `benchmarks/results_convomem_raw_top10_20260414_1649.json` (config)
- `benchmarks/results_high_sensitivity_stress.json` (config)
- `benchmarks/results_ninfer_qwen27b.json` (config)
- `benchmarks/results_ollama_medical_palace.json` (config)
- `benchmarks/results_ollama_ornith_routine.json` (config)
- `crates/mempalace-cli/Cargo.toml` (manifest)
- `crates/mempalace-core/Cargo.toml` (manifest)
- `crates/mempalace-py/Cargo.toml` (manifest)
- `crates/mempalace-py/pyproject.toml` (manifest)
- `deploy/docker-compose.server.yml` (config)
- `docker-compose.yml` (container)
- `examples/antigravity/hooks.json` (config)
- `examples/antigravity/mcp_config.json` (config)
- `examples/cursor/hooks.json` (config)
- `examples/cursor/hooks.minimal.json` (config)
- `mcp.json` (config)
- `mempalace/data/coca_content_words.json` (config)
- `mempalace/data/known_systems.json` (config)
- `mempalace/i18n/be.json` (config)
- `mempalace/i18n/de.json` (config)
- `mempalace/i18n/en.json` (config)
- `mempalace/i18n/es.json` (config)
- `mempalace/i18n/fr.json` (config)
- `mempalace/i18n/hi.json` (config)
- `mempalace/i18n/id.json` (config)
- `mempalace/i18n/it.json` (config)
- `mempalace/i18n/ja.json` (config)
- `mempalace/i18n/ko.json` (config)
- `mempalace/i18n/pt-br.json` (config)
- `mempalace/i18n/ru.json` (config)
- `mempalace/i18n/zh-CN.json` (config)
- `mempalace/i18n/zh-TW.json` (config)
- `plugins/mempalace/hooks.json` (config)
- `plugins/mempalace/mcp_config.json` (config)
- `plugins/mempalace/plugin.json` (config)
- `plugins/mempalace/sidecars/palace/sidecar.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `mempalace` — 185 analysed file(s)
- `benchmarks` — 116 analysed file(s)
- `tests` — 69 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `hooks` — 21 analysed file(s)
- `docs` — 19 analysed file(s)
- `.claude-plugin` — 18 analysed file(s)
- `plugins` — 18 analysed file(s)
- `examples` — 16 analysed file(s)
- `.dsh-plugin` — 14 analysed file(s)
- `.github` — 13 analysed file(s)
- `.codex-plugin` — 11 analysed file(s)
- `crates` — 9 analysed file(s)
- `commands` — 6 analysed file(s)
- `integrations` — 5 analysed file(s)
- `.cursor-plugin` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `deploy` — 3 analysed file(s)
- `skills` — 3 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `landing` — 1 analysed file(s)
- `rules` — 1 analysed file(s)
- `website` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9fc486dc0ce259131da20179847314cabcbb9e15` is the revision these paths and observations refer to.
