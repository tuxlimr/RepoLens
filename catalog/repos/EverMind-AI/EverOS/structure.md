# Project structure: EverMind-AI/EverOS

**Analysed commit:** `489ac7e921a81cf82cc9273674a0fa2429b861eb`

**Commit reference:** [489ac7e921a81cf82cc9273674a0fa2429b861eb](https://github.com/EverMind-AI/EverOS/commit/489ac7e921a81cf82cc9273674a0fa2429b861eb)

**Tree at this commit:** [EverMind-AI/EverOS@489ac7e921a8](https://github.com/EverMind-AI/EverOS/tree/489ac7e921a81cf82cc9273674a0fa2429b861eb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | EverMind-AI/EverOS |
| Description | One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows. |
| Stars | 13913 |
| Forks | 976 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `489ac7e921a81cf82cc9273674a0fa2429b861eb` |
| Retrieved at | 2026-11-14T19:09:37.513477+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.claude/  (17 files)
  rules/  (10 files)
    architecture.md
    async-programming.md
    code-style.md
    datetime-handling.md
    imports.md
    init-py-and-reexport.md
    language-policy.md
    logging-observability.md
    module-docstring.md
    testing.md
  skills/  (6 files)
    add-memory-kind/  (1 files)
      … 1 files under this directory
    commit/  (1 files)
      … 1 files under this directory
    new-branch/  (1 files)
      … 1 files under this directory
    pr/  (1 files)
      … 1 files under this directory
    release/  (1 files)
      … 1 files under this directory
    verify-everos/  (1 files)
      … 1 files under this directory
  settings.json
.github/  (12 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yml
    config.yml
    docs.yml
    feature_request.yml
    use_case.yml
  workflows/  (4 files)
    ci.yml
    commits.yml
    docs.yml
    release.yml
  BRANCH_PROTECTION.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
benchmarks/  (31 files)
  adapters/  (7 files)
    __init__.py
    _profile.py
    base.py
    evermembench.py
    locomo.py
    longmemeval.py
    subtlememory.py
  configs/  (6 files)
    default.toml
    evermembench.toml
    locomo-step.toml
    locomo.toml
    longmemeval.toml
    subtlememory.toml
  data/  (1 files)
    .gitkeep
  metrics/  (3 files)
    __init__.py
    core.py
    ir.py
  .env.example
  README.md
  README.zh.md
  __init__.py
  config.py
  config_hybrid.toml
  config_hybrid_judge4o.toml
  config_keyword.toml
  config_vector.toml
  config_vector_judge4o.toml
  decider_probe.py
  download_data.sh
  preflight.py
  reproduce.sh
data/  (4 files)
  solo_chat_en.json
  solo_chat_zh.json
  team_chat_en.json
  team_chat_zh.json
deploy/  (6 files)
  netlify_relay/  (6 files)
    netlify/  (1 files)
      … 1 files under this directory
    public/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    netlify.toml
    package.json
docs/  (24 files)
  api.md
  architecture.md
  cascade_runbook.md
  cli.md
  configuration.md
  custom_instructions.md
  datetime.md
  engineering.md
  everos-demo.md
  github-sync.md
  how-memory-works.md
  index.md
  knowledge.md
  mcp.md
  migration-to-1.0.0.md
  multimodal.md
  openapi.json
  overview.md
  reflection.md
  release-notes-1.1.0.md
  storage_layout.md
  use-cases.md
  windows.md
  windows.zh.md
examples/  (5 files)
  langfuse/  (5 files)
    .gitignore
    README.md
    demo.py
    record_trace.py
    replay.py
scripts/  (16 files)
  e2e_memorize/  (4 files)
    fixtures/  (2 files)
      … 2 files under this directory
    README.md
    run.py
  check_cjk.py
  check_commit_messages.py
  check_consistency.py
  check_datetime_discipline.py
  check_deprecated_names.py
  check_docs.py
  check_file_sizes.py
  check_github_contributor_docs.py
  check_pr_title.py
  check_repo_assets.py
  check_singletons.py
  dump_openapi.py
src/  (430 files)
  everos/  (430 files)
    component/  (29 files)
      … 29 files under this directory
    config/  (11 files)
      … 11 files under this directory
    core/  (25 files)
      … 25 files under this directory
    entrypoints/  (63 files)
      … 63 files under this directory
    infra/  (185 files)
      … 185 files under this directory
    memory/  (78 files)
      … 78 files under this directory
    service/  (34 files)
      … 34 files under this directory
    templates/  (2 files)
      … 2 files under this directory
    README.md
    __init__.py
    py.typed
tests/  (235 files)
  acceptance/  (45 files)
    memory_delete/  (22 files)
      … 22 files under this directory
    purge/  (22 files)
      … 22 files under this directory
    __init__.py
  e2e/  (12 files)
    __init__.py
    conftest.py
    test_add_flush_agent_pipeline_e2e.py
    test_add_flush_user_pipeline_e2e.py
    test_full_pipeline_timezone_e2e.py
    test_get_endpoint_e2e.py
    test_knowledge_e2e.py
    test_multimodal_add_e2e.py
    test_openapi_endpoint_matches_docs.py
    test_ops_endpoints_e2e.py
    test_reflection_e2e.py
    test_search_endpoint_e2e.py
  fakes/  (44 files)
    llm_scripts/  (32 files)
      … 32 files under this directory
    __init__.py
    _filter.py
    application.py
    backfill.py
    deps.py
    embedding.py
    indexes.py
    llm.py
    sources.py
    storage.py
    stores.py
    trajectories.py
  fixtures/  (13 files)
    agent_trajectories/  (3 files)
      … 3 files under this directory
    allocator_probe/  (1 files)
      … 1 files under this directory
    compatibility/  (5 files)
      … 5 files under this directory
    search_seed/  (1 files)
      … 1 files under this directory
    README.md
    _dump_search_seed.py
    long_conversation_locomo_caroline_melanie.json
  helpers/  (3 files)
    __init__.py
    knowledge_md.py
    ome.py
  integration/  (47 files)
    search/  (6 files)
      … 6 files under this directory
    test_api/  (5 files)
      … 5 files under this directory
    test_cli/  (7 files)
      … 7 files under this directory
    test_infra/  (2 files)
      … 2 files under this directory
    test_tiers/  (6 files)
      … 6 files under this directory
    __init__.py
    test_cascade_all_kinds_consistency.py
    test_cascade_cli_integration.py
    test_cascade_fsevents_repro.py
    test_cascade_integration.py
    test_cascade_scenarios.py
    test_delete_api.py
    test_knowledge_integration.py
    test_memorize_agent_mode.py
    test_memorize_async_order.py
    test_memorize_concurrent_session_lock.py
    test_memorize_integration.py
    test_memorize_window_segmentation.py
    test_milvus_remote.py
    test_ome_partition_admission.py
    test_ome_strategies_integration.py
    test_purge_interleavings.py
    test_reflection_integration.py
    test_session_delete_cluster_cleanup.py
    test_startup_root_lock.py
    test_vector_projection_backfill.py
  unit/  (67 files)
    test_component/  (31 files)
      … 31 files under this directory
    test_config/  (6 files)
      … 6 files under this directory
    __init__.py
    test_benchmark_add_failure_gate.py
    test_benchmark_answer_route.py
    test_benchmark_cli_portability.py
    test_benchmark_config.py
    test_benchmark_decider_endpoint.py
    test_benchmark_decider_trace_gate.py
    test_benchmark_evermembench_owner_mapping.py
    test_benchmark_fleet_shard_guard.py
    test_benchmark_flush_scope.py
    test_benchmark_gold_audit.py
    test_benchmark_harness_own.py
    test_benchmark_headline_definition.py
    test_benchmark_last_seventeen.py
    test_benchmark_locomo_image_caption.py
    test_benchmark_locomo_step_config.py
    test_benchmark_message_owner.py
    test_benchmark_metrics_definitions.py
    test_benchmark_no_exemptions.py
    test_benchmark_ome_strategies.py
    test_benchmark_onboarding.py
    test_benchmark_operational.py
    test_benchmark_owner_in_store.py
    test_benchmark_pipeline.py
    … 6 more files
  __init__.py
  _consistency_assertions.py
  _dotenv_guard.py
  conftest.py
.env.example
.gitignore
.gitlint
.pre-commit-config.yaml
ACKNOWLEDGMENTS.md
CHANGELOG.md
CITATION.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
Makefile
NOTICE
QUICKSTART.md
README.md
README.zh-CN.md
SECURITY.md
config.example.toml
pyproject.toml
```

## Entry points

- [src/everos/entrypoints/api/app.py:97](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/src/everos/entrypoints/api/app.py#L97)
- [src/everos/entrypoints/cli/commands/cascade.py:59](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/src/everos/entrypoints/cli/commands/cascade.py#L59)
- [src/everos/entrypoints/cli/commands/config.py:26](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/src/everos/entrypoints/cli/commands/config.py#L26)
- [src/everos/entrypoints/cli/commands/server.py:23](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/src/everos/entrypoints/cli/commands/server.py#L23)
- [src/everos/entrypoints/cli/launcher.py](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/src/everos/entrypoints/cli/launcher.py)
- [src/everos/entrypoints/cli/main.py:18](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/src/everos/entrypoints/cli/main.py#L18)
- [src/everos/entrypoints/tui/demo/readme_media.py:268](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/src/everos/entrypoints/tui/demo/readme_media.py#L268)
- [benchmarks/adapters/evermembench.py:694](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/benchmarks/adapters/evermembench.py#L694)
- [benchmarks/decider_probe.py:161](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/benchmarks/decider_probe.py#L161)
- [scripts/check_cjk.py:100](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/scripts/check_cjk.py#L100)
- [scripts/check_commit_messages.py:137](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/scripts/check_commit_messages.py#L137)
- [scripts/check_consistency.py:349](https://github.com/EverMind-AI/EverOS/blob/489ac7e921a81cf82cc9273674a0fa2429b861eb/scripts/check_consistency.py#L349)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 31 file(s) under api layer (observed from repository paths and static analysis). Observed routes: POST /quiesce, POST /delete, POST /delete_by_ids, POST /get, GET /health. Observed top-level classes: AcceptedResp… |
| benchmarks package | library | Observed | Groups 7 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level functions: _dcg, _is_unset, _missing_data, _missing_keys, _required_server_keys, blocking_problems. |
| Configuration and deployment | config | Observed | Groups 35 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AgentMemorySettings, AnswerResult, ApiSettings, AsyncQueueSettings, BenchmarkConfig,… |
| Data layer | data | Observed | Groups 129 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AgentCase, AgentCaseDailyFrontmatter, AgentCaseIndexAdapter, AgentCaseReader, AgentCaseWriter, AgentS… |
| deploy package | library | Observed | Groups 1 file(s) under deploy package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 22 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Typer. Observed top-level classes: BaseRefError, DeciderProbeReply,… |
| everos package | library | Observed | Groups 188 file(s) under everos package (observed from repository paths and static analysis). Observed top-level classes: AgentCaseExtracted, AgentCaseHandler, AgentCaseIndex, AgentCaseRecaller, AgentCaseStore, AgentMem… |
| External integrations | external | Observed | Groups 6 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: DatasetAdapter. Observed top-level functions: _build_context, _deterministic_verdict, _extra… |
| Service / domain layer | service | Observed | Groups 60 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AppError, Application, BackfillDeps, BackfillOutcome, BackfillPresenter, BackfillSummary.… |
| Tests | test | Observed | Groups 236 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: Evidence, FakeEmbeddingProvider, FakeOmeLock, FakeUpstrea… |

## Important files

- `.claude/settings.json` (config)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/docs.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/use_case.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/commits.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `benchmarks/.env.example` (config)
- `benchmarks/config_hybrid.toml` (config)
- `benchmarks/config_hybrid_judge4o.toml` (config)
- `benchmarks/config_keyword.toml` (config)
- `benchmarks/config_vector.toml` (config)
- `benchmarks/config_vector_judge4o.toml` (config)
- `benchmarks/configs/default.toml` (config)
- `benchmarks/configs/evermembench.toml` (config)
- `benchmarks/configs/locomo-step.toml` (config)
- `benchmarks/configs/locomo.toml` (config)
- `benchmarks/configs/longmemeval.toml` (config)
- `benchmarks/configs/subtlememory.toml` (config)
- `config.example.toml` (config)
- `data/solo_chat_en.json` (config)
- `data/solo_chat_zh.json` (config)
- `data/team_chat_en.json` (config)
- `data/team_chat_zh.json` (config)
- `deploy/netlify_relay/netlify.toml` (config)
- `deploy/netlify_relay/package.json` (manifest)
- `docs/openapi.json` (config)
- `pyproject.toml` (manifest)
- `scripts/e2e_memorize/fixtures/agent_session.json` (config)
- `scripts/e2e_memorize/fixtures/chat_session.json` (config)
- `src/everos/config/custom_instructions/boundary_detection.yaml` (config)
- `src/everos/config/custom_instructions/episode_extract.yaml` (config)
- `src/everos/config/custom_instructions/profile_extract.yaml` (config)
- `src/everos/config/custom_instructions/reflect.yaml` (config)
- `src/everos/config/default.toml` (config)
- `src/everos/config/default_ome.toml` (config)

## Top-level layout

- `src` — 430 analysed file(s)
- `tests` — 235 analysed file(s)
- `benchmarks` — 31 analysed file(s)
- `docs` — 24 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.claude` — 17 analysed file(s)
- `scripts` — 16 analysed file(s)
- `.github` — 12 analysed file(s)
- `deploy` — 6 analysed file(s)
- `examples` — 5 analysed file(s)
- `data` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `489ac7e921a81cf82cc9273674a0fa2429b861eb` is the revision these paths and observations refer to.
