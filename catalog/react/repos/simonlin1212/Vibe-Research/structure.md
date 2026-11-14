# Project structure: simonlin1212/Vibe-Research

**Analysed commit:** `76bd805f9b8387035b9dbc9110d1484d782d0e3a`

**Commit reference:** [76bd805f9b8387035b9dbc9110d1484d782d0e3a](https://github.com/simonlin1212/Vibe-Research/commit/76bd805f9b8387035b9dbc9110d1484d782d0e3a)

**Tree at this commit:** [simonlin1212/Vibe-Research@76bd805f9b83](https://github.com/simonlin1212/Vibe-Research/tree/76bd805f9b8387035b9dbc9110d1484d782d0e3a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | simonlin1212/Vibe-Research |
| Description | Vibe-Research：A 股、美股、港股的投研工作台 · 自选与持仓、每日复盘、产业资讯、产业研究、个股深挖、回测、研报库，168 个数据端点。支持 Claude Code、Codex、WorkBuddy 订阅或任意模型 API。 | A research workbench for China A-shares, US and HK stocks. |
| Stars | 3710 |
| Forks | 699 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `76bd805f9b8387035b9dbc9110d1484d782d0e3a` |
| Retrieved at | 2026-11-14T19:15:08.691462+00:00 |
| Files in this snapshot | 620 |

## Directory tree

```text
.agents/  (104 files)
  skills/  (104 files)
    catalyst-risk/  (1 files)
      … 1 files under this directory
    company-research/  (1 files)
      … 1 files under this directory
    data-access/  (98 files)
      … 98 files under this directory
    earnings-analysis/  (1 files)
      … 1 files under this directory
    industry-chain/  (1 files)
      … 1 files under this directory
    valuation/  (1 files)
      … 1 files under this directory
    README.md
.github/  (2 files)
  workflows/  (2 files)
    cross-platform.yml
    portable.yml
assets/  (2 files)
  screenshots/  (1 files)
    2026-10-10/  (1 files)
      … 1 files under this directory
  README.md
backtest/  (56 files)
  engines/  (5 files)
    __init__.py
    _market_hooks.py
    base.py
    china_a.py
    global_equity.py
  tests/  (23 files)
    fixtures/  (1 files)
      … 1 files under this directory
    __init__.py
    test_audit_round3.py
    test_cli_errors.py
    test_constraints.py
    test_cost_compare.py
    test_datasource_health.py
    test_downside_metrics.py
    test_engine_rules.py
    test_event_study.py
    test_gate.py
    test_index_benchmark.py
    test_kline.py
    test_loader.py
    test_m31_audit.py
    test_portfolio_perf.py
    test_portfolio_xray.py
    test_report_data.py
    test_rsrs.py
    test_run.py
    test_scenario_replay.py
    test_sensitivity.py
    test_symbol_search.py
  LICENSE.upstream
  NOTICE.md
  README.md
  __init__.py
  benchmark.py
  cli.py
  constraints.py
  cost_compare.py
  event_study.py
  gate.py
  gics.py
  kline.py
  loader.py
  metrics.py
  models.py
  portfolio_perf.py
  portfolio_xray.py
  rebalance_notes.py
  report_data.py
  risk_xray.py
  run.py
  run_card.py
  scenario_replay.py
  sensitivity.py
  … 4 more files
calc/  (23 files)
  tests/  (11 files)
    fixtures/  (1 files)
      … 1 files under this directory
    test_cli.py
    test_contracts.py
    test_currency_ttm.py
    test_display.py
    test_earnings.py
    test_formulas.py
    test_indicators.py
    test_series.py
    test_stdio_utf8.py
    test_tool.py
  README.md
  SPEC.md
  __init__.py
  cli.py
  contracts.py
  display.py
  earnings.py
  formulas.py
  indicators.py
  series.py
  stdio_utf8.py
  tool.py
datasources/  (10 files)
  CATALOG.md
  README.md
  UPSTREAM.md
  chokepoint_keywords.json
  gen_catalog.py
  health.py
  industry_tags.json
  port_astock.py
  registry.json
  rss_sources.json
desktop/  (209 files)
  src/  (131 files)
    core/  (11 files)
      … 11 files under this directory
    verticals/  (118 files)
      … 118 files under this directory
    index.css
    main.tsx
  test/  (70 files)
    helpers/  (1 files)
      … 1 files under this directory
    abnormal.test.ts
    agent_error.test.ts
    ai_connection.test.ts
    ai_draft.test.ts
    ai_runtime.test.ts
    ai_settings_persistence.test.ts
    ai_surface.test.ts
    ai_threads.test.ts
    analysis_session.test.ts
    audit_round3.test.ts
    audit_view.test.ts
    backtest_agent.test.ts
    backtest_charts.test.ts
    calendar.test.ts
    candidates.test.ts
    chat_controls.test.ts
    chat_sources.test.ts
    chat_storage.test.ts
    daily_review_context.test.ts
    debate_cancel.test.ts
    download.test.ts
    earnings_brief.test.ts
    event_study_view.test.ts
    global_indices.test.ts
    … 45 more files
  index.html
  package.json
  postcss.config.js
  remote-access.ts
  tailwind.config.ts
  tsconfig.json
  vite-token.ts
  vite.config.ts
docs/  (38 files)
  AI接入与执行模式_v1_2026-09-04.md
  Agent开关与普通对话_M24_2026-09-06.md
  Mac安装包本地验收_M32_2026-09-06.md
  Mac正式签名与公证_M38_2026-09-07.md
  Mac独立窗口与引擎升级_M34_2026-09-06.md
  README.md
  README更新验收_M39_2026-09-07.md
  Windows云端验收_M19_2026-09-06.md
  ci-workflows-v2.2.3.md
  development-validation.md
  issue-pr-triage-2026-09-12.md
  issue-pr-triage-v1.2.0.md
  model-access.md
  release-checklist.md
  source-delivery.md
  workbuddy-cli-2.161.0-compatibility-2026-10-23.md
  上游Issue同步验收_2026-09-05.md
  公开版视觉与品牌Logo恢复_M21_2026-09-06.md
  剩余审计整改_M13_2026-09-05.md
  双引擎任务架构_v3_2026-09-04.md
  发布候选与Mac验收_M37_2026-09-07.md
  发布候选与隐私验收_M40_2026-09-07.md
  安装版AI接入修复_M35_2026-09-06.md
  完整版本机验收_M14_2026-09-05.md
  … 14 more files
knowledge/  (2 files)
  companies/  (1 files)
    _TEMPLATE/  (1 files)
      … 1 files under this directory
  manifest.json
methodology/  (1 files)
  constitution.md
orchestrator/  (164 files)
  src/  (118 files)
    engines/  (6 files)
      … 6 files under this directory
    finance/  (39 files)
      … 39 files under this directory
    access_token.ts
    agent_runner.ts
    alerts.ts
    api.ts
    arithmetic.ts
    assistant_bridge.ts
    assistant_tools_mcp.ts
    assistant_turn.ts
    audit_chain.ts
    batch.ts
    calc_projection.ts
    chat.ts
    config.ts
    data_root.ts
    debate.ts
    deep_target_registry.ts
    doctor.ts
    engine.ts
    fetchrun.ts
    fixture.ts
    formats.ts
    fsutil.ts
    gate.ts
    guided_tool.ts
    … 49 more files
  test/  (43 files)
    helpers/  (1 files)
      … 1 files under this directory
    abnormal.test.ts
    api_entry.test.ts
    arithmetic.test.ts
    assistant_tools.test.ts
    audit_chain.test.ts
    batch_alerts.test.ts
    browser_ui.test.ts
    caliber_hints.test.ts
    candidates.test.ts
    chat.test.ts
    chokepoint.test.ts
    core_purity.test.ts
    debate.test.ts
    deep_engine.test.ts
    delete_run.test.ts
    direct_stage_agent.test.ts
    direct_transport.test.ts
    earnings_brief.test.ts
    engine_boundary.test.ts
    events.test.ts
    fixture.test.ts
    gate.test.ts
    global_contract.test.ts
    guided_tool.test.ts
    … 18 more files
  README.md
  package.json
  tsconfig.json
scripts/  (1 files)
  doctor
.gitattributes
.gitignore
AGENTS.md
CLAUDE.md
LICENSE
README.md
README_en.md
mypy.ini
```

## Entry points

- [.agents/skills/data-access/scripts/core/retrieval_cli.py:40](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/.agents/skills/data-access/scripts/core/retrieval_cli.py#L40)
- [.agents/skills/data-access/scripts/fetch_announcements.py:82](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/.agents/skills/data-access/scripts/fetch_announcements.py#L82)
- [.agents/skills/data-access/scripts/fetch_endpoint.py:169](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/.agents/skills/data-access/scripts/fetch_endpoint.py#L169)
- [.agents/skills/data-access/scripts/fetch_estimates.py:143](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/.agents/skills/data-access/scripts/fetch_estimates.py#L143)
- [.agents/skills/data-access/scripts/fetch_financials.py:181](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/.agents/skills/data-access/scripts/fetch_financials.py#L181)
- [.agents/skills/data-access/scripts/fetch_kline.py:109](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/.agents/skills/data-access/scripts/fetch_kline.py#L109)
- [.agents/skills/data-access/scripts/fetch_pe_history.py:89](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/.agents/skills/data-access/scripts/fetch_pe_history.py#L89)
- [.agents/skills/data-access/scripts/fetch_profile.py:148](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/.agents/skills/data-access/scripts/fetch_profile.py#L148)
- [.agents/skills/data-access/scripts/fetch_quote.py:140](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/.agents/skills/data-access/scripts/fetch_quote.py#L140)
- [.agents/skills/data-access/scripts/fetch_trade_calendar.py:97](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/.agents/skills/data-access/scripts/fetch_trade_calendar.py#L97)
- [backtest/cli.py:324](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/backtest/cli.py#L324)
- [backtest/event_study.py:701](https://github.com/simonlin1212/Vibe-Research/blob/76bd805f9b8387035b9dbc9110d1484d782d0e3a/backtest/event_study.py#L701)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| backtest package | library | Observed | Groups 20 file(s) under backtest package (observed from repository paths and static analysis). Observed top-level classes: BaseEngine, BenchmarkResult, BuyAndHold, ChinaAEngine, GlobalEquityEngine, GroupExposure. Observ… |
| calc package | library | Observed | Groups 8 file(s) under calc package (observed from repository paths and static analysis). Observed top-level classes: CalcInputError. Observed top-level functions: _amount_suffix, _check_unit, _convert, _day, _ema, _err. |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: EquitySnapshot, FillRecord, Position, TradeRecord. |
| datasources package | library | Observed | Groups 1 file(s) under datasources package (observed from repository paths and static analysis). |
| desktop package | library | Observed | Groups 123 file(s) under desktop package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BacktestNotValid, EventError, KlineError, PerfError, ReplayError, Result. Observed top-le… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| orchestrator package | library | Observed | Groups 118 file(s) under orchestrator package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 10 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 179 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeTdx, FrameLoader, PagedRS, R, Signals, _Fake. Observed top-level functions: _ann, _artifacts, _bar, _b… |

## Important files

- `.agents/skills/data-access/scripts/requirements.lock.txt` (manifest)
- `.agents/skills/data-access/scripts/requirements.txt` (manifest)
- `.github/workflows/cross-platform.yml` (ci)
- `.github/workflows/portable.yml` (ci)
- `datasources/chokepoint_keywords.json` (config)
- `datasources/industry_tags.json` (config)
- `datasources/registry.json` (config)
- `datasources/rss_sources.json` (config)
- `desktop/package.json` (manifest)
- `desktop/src/verticals/finance/data/sectors.json` (config)
- `desktop/tsconfig.json` (config)
- `knowledge/manifest.json` (config)
- `mypy.ini` (config)
- `orchestrator/package.json` (manifest)
- `orchestrator/tsconfig.json` (config)

## Top-level layout

- `desktop` — 209 analysed file(s)
- `orchestrator` — 164 analysed file(s)
- `.agents` — 104 analysed file(s)
- `backtest` — 56 analysed file(s)
- `docs` — 38 analysed file(s)
- `calc` — 23 analysed file(s)
- `datasources` — 10 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 2 analysed file(s)
- `assets` — 2 analysed file(s)
- `knowledge` — 2 analysed file(s)
- `methodology` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `76bd805f9b8387035b9dbc9110d1484d782d0e3a` is the revision these paths and observations refer to.
