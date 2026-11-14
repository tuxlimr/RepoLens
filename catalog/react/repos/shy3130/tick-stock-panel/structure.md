# Project structure: shy3130/tick-stock-panel

**Analysed commit:** `f9cb383c5918c6a88a412f3ce43d59fe81b94ccc`

**Commit reference:** [f9cb383c5918c6a88a412f3ce43d59fe81b94ccc](https://github.com/shy3130/tick-stock-panel/commit/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc)

**Tree at this commit:** [shy3130/tick-stock-panel@f9cb383c5918](https://github.com/shy3130/tick-stock-panel/tree/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | shy3130/tick-stock-panel |
| Description | TSP自托管、零运维的 A 股「自建策略 + 监控 + 回测」量化工作台  | LLM能力驱使策略定制+个股分析+复盘 | 自由接入第三方数据源与个性化扩展数据 | 个人开源 |
| Stars | 7778 |
| Forks | 1911 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `f9cb383c5918c6a88a412f3ce43d59fe81b94ccc` |
| Retrieved at | 2026-11-14T19:13:47.074991+00:00 |
| Files in this snapshot | 724 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (4 files)
    ci.yml
    dco.yml
    docker.yml
    release.yml
assets/  (1 files)
  architecture.svg
backend/  (707 files)
  app/  (313 files)
    api/  (42 files)
      … 42 files under this directory
    backtest/  (24 files)
      … 24 files under this directory
    custom/  (19 files)
      … 19 files under this directory
    data_providers/  (16 files)
      … 16 files under this directory
    extensions/  (5 files)
      … 5 files under this directory
    factors/  (7 files)
      … 7 files under this directory
    indicators/  (3 files)
      … 3 files under this directory
    jobs/  (2 files)
      … 2 files under this directory
    plugins/  (9 files)
      … 9 files under this directory
    services/  (104 files)
      … 104 files under this directory
    strategy/  (56 files)
      … 56 files under this directory
    tickflow/  (9 files)
      … 9 files under this directory
    __init__.py
    config.py
    db_safe.py
    definitions.py
    desktop.py
    enriched_generation.py
    frontend_static.py
    logfile.py
    main.py
    market_time.py
    parquet.py
    polars_guard.py
    price_limits.py
    secrets_store.py
    share_capital.py
    startup_diagnostics.py
    watchdog.py
  scripts/  (14 files)
    __init__.py
    bench_factor_materialize.py
    bench_feature_resolution.py
    bench_optimizer_prepare.py
    benchmark_cache_async.py
    benchmark_daily_sync_staging.py
    benchmark_ext_pull_client.py
    benchmark_matrix_axes.py
    benchmark_remaining_hotpaths.py
    cleanup_halt_days.py
    demo_ai_strategy_gate.py
    demo_recap_push_mode.py
    probe_tickflow_pro.py
    stress_polars_concurrency.py
  tests/  (379 files)
    backtest/  (41 files)
      … 41 files under this directory
    fixtures/  (47 files)
      … 47 files under this directory
    signal_seeds.py
    test_abnormal_intraday.py
    test_abnormal_moves.py
    test_adj_factor_event_columns.py
    test_adj_factor_standalone_sync.py
    test_ai_analysis_focus.py
    test_ai_generator_prompt.py
    test_ai_iterate.py
    test_ai_minute_integration.py
    test_ai_probe.py
    test_ai_provider.py
    test_ai_responses.py
    test_ai_strategy_meta_normalize.py
    test_ai_tool_calling.py
    test_alerts_query_bounds.py
    test_analysis_menu_url_template.py
    test_api_gateway.py
    test_api_position_policies.py
    test_api_strategy_bundle.py
    test_ashare_date_defaults_beijing_today.py
    test_assistant_actions.py
    test_assistant_asset_quotes.py
    test_assistant_auto_approve.py
    test_assistant_backtest_beijing_today.py
    … 267 more files
  pyproject.toml
mcp-server/  (1 files)
  src/  (1 files)
    tsp_mcp_server/  (1 files)
      … 1 files under this directory
.dockerignore
.env.example
.gitattributes
.gitignore
.zcodeignore
AGENTS.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
VERSION
```

## Entry points

- [backend/app/desktop.py:487](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/app/desktop.py#L487)
- [backend/app/main.py:564](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/app/main.py#L564)
- [backend/scripts/bench_factor_materialize.py:136](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/scripts/bench_factor_materialize.py#L136)
- [backend/scripts/bench_feature_resolution.py:119](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/scripts/bench_feature_resolution.py#L119)
- [backend/scripts/bench_optimizer_prepare.py:121](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/scripts/bench_optimizer_prepare.py#L121)
- [backend/scripts/benchmark_cache_async.py:144](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/scripts/benchmark_cache_async.py#L144)
- [backend/scripts/benchmark_daily_sync_staging.py:63](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/scripts/benchmark_daily_sync_staging.py#L63)
- [backend/scripts/benchmark_ext_pull_client.py:73](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/scripts/benchmark_ext_pull_client.py#L73)
- [backend/scripts/benchmark_matrix_axes.py:64](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/scripts/benchmark_matrix_axes.py#L64)
- [backend/scripts/benchmark_remaining_hotpaths.py:202](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/scripts/benchmark_remaining_hotpaths.py#L202)
- [backend/scripts/cleanup_halt_days.py:95](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/scripts/cleanup_halt_days.py#L95)
- [backend/scripts/demo_ai_strategy_gate.py:87](https://github.com/shy3130/tick-stock-panel/blob/f9cb383c5918c6a88a412f3ce43d59fe81b94ccc/backend/scripts/demo_ai_strategy_gate.py#L87)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 43 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /intraday, GET /overview, GET (path not a literal), DELETE (path not a literal), DELETE /{ts}. Observed top-le… |
| backend package | library | Observed | Groups 146 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: AIStrategyGenerator, AIStrategyIterator, ActionDecisionRequest, ActiveLimitGeneMatrixStrategy, A… |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AuthConfig, CustomSourceConfig, DatasetConfig, Settings. Observed top-level functions… |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /api/openapi.json. Observed top-level classes:… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: FuyaoClient, FuyaoError, FuyaoUnknownSymbolError, TdxQuantAuthError, TdxQuantClient, TdxQuan… |
| mcp-server package | library | Observed | Groups 1 file(s) under mcp-server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 106 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AIToolProtocolError, AbnormalRule, BacktestConfig, BacktestResult, BacktestService, Bundl… |
| Tests | test | Observed | Groups 379 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: ActiveLimitGeneMatrixStrategy, BollBreakoutMatrixStrategy… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/dco.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `Dockerfile` (container)
- `backend/app/plugins/fuyao/plugin.yaml` (config)
- `backend/app/plugins/tdxquant/plugin.yaml` (config)
- `backend/pyproject.toml` (manifest)

## Top-level layout

- `backend` — 707 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 4 analysed file(s)
- `assets` — 1 analysed file(s)
- `mcp-server` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f9cb383c5918c6a88a412f3ce43d59fe81b94ccc` is the revision these paths and observations refer to.
