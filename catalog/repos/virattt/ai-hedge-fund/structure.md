# Project structure: virattt/ai-hedge-fund

**Analysed commit:** `5c553b5222044f6a5527bd377b4104c50ee0ad28`

**Commit reference:** [5c553b5222044f6a5527bd377b4104c50ee0ad28](https://github.com/virattt/ai-hedge-fund/commit/5c553b5222044f6a5527bd377b4104c50ee0ad28)

**Tree at this commit:** [virattt/ai-hedge-fund@5c553b522204](https://github.com/virattt/ai-hedge-fund/tree/5c553b5222044f6a5527bd377b4104c50ee0ad28)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | virattt/ai-hedge-fund |
| Description | An AI Hedge Fund Team |
| Stars | 64674 |
| Forks | 11381 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `5c553b5222044f6a5527bd377b4104c50ee0ad28` |
| Retrieved at | 2026-11-14T19:06:20.230254+00:00 |
| Files in this snapshot | 150 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
assets/  (1 files)
  ai-hedge-fund-system.svg
hedge_fund/  (139 files)
  backtesting/  (5 files)
    __init__.py
    fund.py
    research.py
    test_fund.py
    test_research.py
  brokers/  (10 files)
    __init__.py
    costs.py
    models.py
    paper.py
    protocol.py
    sim.py
    test_costs.py
    test_models.py
    test_paper.py
    test_sim.py
  data/  (15 files)
    __init__.py
    bars.py
    cached.py
    client.py
    models.py
    protocol.py
    screener.py
    sessions.py
    test_bars.py
    test_cached.py
    test_client.py
    test_client_contract.py
    test_screener.py
    test_wallet.py
    wallet.py
  features/  (7 files)
    __init__.py
    breakpoints.py
    intraday.py
    snapshot.py
    test_breakpoints.py
    test_intraday.py
    test_snapshot.py
  fund/  (6 files)
    __init__.py
    example.yaml
    spec.py
    storage.py
    test_spec.py
    test_strategy_library.py
  llm/  (10 files)
    __init__.py
    api_models.json
    cache.py
    client.py
    contract.py
    registry.py
    test_client.py
    test_contract.py
    test_watch.py
    watch.py
  paper/  (8 files)
    __init__.py
    deployed.py
    ledger.py
    runner.py
    test_ledger.py
    test_runner.py
    test_tick.py
    tick.py
  pipeline/  (12 files)
    fixtures/  (1 files)
      … 1 files under this directory
    __init__.py
    clock.py
    execution.py
    models.py
    session.py
    stages.py
    test_clock.py
    test_execution.py
    test_session.py
    test_stages.py
    test_timing.py
  portfolio/  (4 files)
    __init__.py
    construction.py
    test_construction.py
    validation.py
  risk/  (5 files)
    __init__.py
    exposures.py
    limits.py
    test_exposures.py
    test_limits.py
  scorecard/  (7 files)
    __init__.py
    allocation.py
    analysts.py
    models.py
    strategies.py
    test_allocation.py
    test_scorecard.py
  signals/  (11 files)
    __init__.py
    base.py
    buffett.py
    druckenmiller.py
    graham.py
    llm_agent.py
    lynch.py
    munger.py
    pead.py
    test_llm_agents.py
    test_signals.py
  strategies/  (4 files)
    deep-value.yaml
    earnings-drift.yaml
    fundamental-ls.yaml
    inflections.yaml
  tui/  (27 files)
    __init__.py
    __main__.py
    app.py
    app.tcss
    backtest.py
    builder.py
    conftest.py
    fixtures.py
    funds.py
    home.py
    keys.py
    palette.py
    paper.py
    paper_view.py
    report.py
    scorecard_view.py
    session_report.py
    shared.py
    test_backtest.py
    test_builder.py
    test_funds.py
    test_home.py
    test_paper.py
    test_paper_view.py
    … 3 more files
  validation/  (1 files)
    __init__.py
  README.md
  __init__.py
  conftest.py
  models.py
  paths.py
  run.py
  test_run.py
.env.example
.gitignore
LICENSE
Makefile
README.md
ROADMAP.md
VISION.md
pyproject.toml
```

## Entry points

- [hedge_fund/run.py:404](https://github.com/virattt/ai-hedge-fund/blob/5c553b5222044f6a5527bd377b4104c50ee0ad28/hedge_fund/run.py#L404)
- [hedge_fund/tui/__main__.py:10](https://github.com/virattt/ai-hedge-fund/blob/5c553b5222044f6a5527bd377b4104c50ee0ad28/hedge_fund/tui/__main__.py#L10)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 13 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Allocated, AllocationRecord, AnalystScore, CachedDataClient, CallMeter, CompanyFacts. Observed top-lev… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: HedgeFundApp. Observed top-level functions: _backtest, _fund_dir, _paper, _parser, _status… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: ChatLLM, JevLLM, LLMCallError, LLMClient, LLMParseError. Observed top-level functions: Anthr… |
| hedge_fund package | library | Observed | Groups 67 file(s) under hedge_fund package (observed from repository paths and static analysis). Observed top-level classes: AllocationPolicy, AlphaModel, BacktestDecisionsScreen, BacktestScorecardScreen, BacktestScreen… |
| Tests | test | Observed | Groups 46 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BarClient, CountingClient, DailyOnly, DailyTape, DatedAnalyst, DayClient. Observed top-level functions: SPE… |

## Important files

- `.env.example` (config)
- `hedge_fund/fund/example.yaml` (config)
- `hedge_fund/llm/api_models.json` (config)
- `hedge_fund/pipeline/fixtures/record_before_intraday.json` (config)
- `hedge_fund/strategies/deep-value.yaml` (config)
- `hedge_fund/strategies/earnings-drift.yaml` (config)
- `hedge_fund/strategies/fundamental-ls.yaml` (config)
- `hedge_fund/strategies/inflections.yaml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `hedge_fund` — 139 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 2 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5c553b5222044f6a5527bd377b4104c50ee0ad28` is the revision these paths and observations refer to.
