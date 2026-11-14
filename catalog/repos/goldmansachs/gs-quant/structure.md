# Project structure: goldmansachs/gs-quant

**Analysed commit:** `8725ddf2ce4b925a7ce68ba90eca353455ac34b5`

**Commit reference:** [8725ddf2ce4b925a7ce68ba90eca353455ac34b5](https://github.com/goldmansachs/gs-quant/commit/8725ddf2ce4b925a7ce68ba90eca353455ac34b5)

**Tree at this commit:** [goldmansachs/gs-quant@8725ddf2ce4b](https://github.com/goldmansachs/gs-quant/tree/8725ddf2ce4b925a7ce68ba90eca353455ac34b5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | goldmansachs/gs-quant |
| Description | Python toolkit for quantitative finance |
| Stars | 14123 |
| Forks | 1958 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `8725ddf2ce4b925a7ce68ba90eca353455ac34b5` |
| Retrieved at | 2026-11-14T19:09:32.370986+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.claude/  (1 files)
  skills/  (1 files)
    README.md
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    python-publish.yml
dco/  (4 files)
  Bryan Galindo.dco
  Grant McGovern.dco
  Maverick Lin.dco
  Scott Weinstein.dco
docs/  (664 files)
  _build/  (325 files)
    html/  (323 files)
      … 323 files under this directory
    search/  (2 files)
      … 2 files under this directory
  _templates/  (7 files)
    contexts.rst
    instruments.rst
    models_class.rst
    portfolio_manager.rst
    processors.rst
    report.rst
    timeseries_class.rst
  _themes/  (16 files)
    gs/  (16 files)
      … 16 files under this directory
  classes/  (123 files)
    gs_quant.analytics.datagrid.datagrid.DataGrid.rst
    gs_quant.analytics.processors.AdditionProcessor.rst
    gs_quant.analytics.processors.AppendProcessor.rst
    gs_quant.analytics.processors.ChangeProcessor.rst
    gs_quant.analytics.processors.CoordinateProcessor.rst
    gs_quant.analytics.processors.CorrelationProcessor.rst
    gs_quant.analytics.processors.DivisionProcessor.rst
    gs_quant.analytics.processors.EntityProcessor.rst
    gs_quant.analytics.processors.LastProcessor.rst
    gs_quant.analytics.processors.MultiplicationProcessor.rst
    gs_quant.analytics.processors.PercentilesProcessor.rst
    gs_quant.analytics.processors.ReturnsProcessor.rst
    gs_quant.analytics.processors.SharpeRatioProcessor.rst
    gs_quant.analytics.processors.SubtractionProcessor.rst
    gs_quant.analytics.processors.VolatilityProcessor.rst
    gs_quant.analytics.workspaces.Component.rst
    gs_quant.analytics.workspaces.Workspace.rst
    gs_quant.base.Priceable.rst
    gs_quant.data.DataContext.rst
    gs_quant.data.Dataset.rst
    gs_quant.data.Fields.rst
    gs_quant.data.core.DataContext.rst
    gs_quant.data.dataset.Dataset.rst
    gs_quant.data.fields.Fields.rst
    … 99 more files
  functions/  (171 files)
    gs_quant.datetime.date.business_day_count.rst
    gs_quant.datetime.date.business_day_offset.rst
    gs_quant.datetime.date.date_range.rst
    gs_quant.datetime.date.is_business_day.rst
    gs_quant.datetime.date.prev_business_date.rst
    gs_quant.datetime.point.point_sort_order.rst
    gs_quant.markets.baskets.Basket.add_factor_risk_report.rst
    gs_quant.markets.baskets.Basket.cancel_rebalance.rst
    gs_quant.markets.baskets.Basket.clone.rst
    gs_quant.markets.baskets.Basket.create.rst
    gs_quant.markets.baskets.Basket.delete_factor_risk_report.rst
    gs_quant.markets.baskets.Basket.entity_type.rst
    gs_quant.markets.baskets.Basket.get.rst
    gs_quant.markets.baskets.Basket.get_close_price_for_date.rst
    gs_quant.markets.baskets.Basket.get_close_prices.rst
    gs_quant.markets.baskets.Basket.get_corporate_actions.rst
    gs_quant.markets.baskets.Basket.get_data_coordinate.rst
    gs_quant.markets.baskets.Basket.get_data_series.rst
    gs_quant.markets.baskets.Basket.get_details.rst
    gs_quant.markets.baskets.Basket.get_entity.rst
    gs_quant.markets.baskets.Basket.get_fundamentals.rst
    gs_quant.markets.baskets.Basket.get_identifier.rst
    gs_quant.markets.baskets.Basket.get_identifiers.rst
    gs_quant.markets.baskets.Basket.get_latest_close_price.rst
    … 147 more files
  html/  (5 files)
    .doctrees/  (2 files)
      … 2 files under this directory
    _sources/  (1 files)
      … 1 files under this directory
    objects.inv
    searchindex.js
  module/  (1 files)
    models.rst
  modules/  (1 files)
    gs_quant.markets.indices_utils.rst
  searchdataext/  (1 files)
    __init__.py
  Makefile
  README.md
  analytics.rst
  conf.py
  data.rst
  datetime.rst
  entities.rst
  index.rst
  instrument.rst
  make.bat
  markets.rst
  models.rst
  risk.rst
  timeseries.rst
gs_quant/  (115 files)
  analytics/  (26 files)
    common/  (4 files)
      … 4 files under this directory
    core/  (4 files)
      … 4 files under this directory
    datagrid/  (7 files)
      … 7 files under this directory
    processors/  (7 files)
      … 7 files under this directory
    workspaces/  (3 files)
      … 3 files under this directory
    __init__.py
  api/  (59 files)
    fred/  (3 files)
      … 3 files under this directory
    gs/  (50 files)
      … 50 files under this directory
    __init__.py
    api_cache.py
    api_session.py
    data.py
    risk.py
    utils.py
  backtests/  (20 files)
    __init__.py
    action_handler.py
    actions.py
    backtest_engine.py
    backtest_objects.py
    backtest_utils.py
    core.py
    data_handler.py
    data_sources.py
    decorator.py
    equity_vol_engine.py
    event.py
    execution_engine.py
    generic_engine.py
    generic_engine_action_impls.py
    order.py
    predefined_asset_engine.py
    strategy.py
    strategy_systematic.py
    triggers.py
  config/  (3 files)
    __init__.py
    options.py
    utils.py
  content/  (2 files)
    Contents.ipynb
    Index.ipynb
  __init__.py
  _version.py
  base.py
  common.py
  config.ini
.gitattributes
.gitignore
.gitlab-ci.yml
.gs-project.yml
.pre-commit-config.yaml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
NOTICE
NOTICE.txt
README.md
conftest.py
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 58 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: AdditionalResults, AggregateCostModel, ApiRequestCache, ApiWithCustomSession, AssetCache, BacktestRespo… |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: DisplayOptions. Observed top-level functions: _env_var_or_cwd, expand_string_with_var… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| gs_quant package | library | Observed | Groups 46 file(s) under gs_quant package (observed from repository paths and static analysis). Observed top-level classes: Action, ActionHandler, ActionHandlerBaseFactory, AddScaledTradeAction, AddScaledTradeActionImpl,… |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: BaseProcessor, DataQueryInfo, MeasureQueryInfo, ProcessorResult. Observed top-level functio… |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: test_transaction_cost_config_encoding. |

## Important files

- `.github/workflows/python-publish.yml` (ci)
- `.gitlab-ci.yml` (ci)
- `.gs-project.yml` (config)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `docs/_build/search/search-index.json` (config)
- `docs/_build/search/searchdata.json` (config)
- `gs_quant/config.ini` (config)

## Top-level layout

- `docs` — 664 analysed file(s)
- `gs_quant` — 115 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `dco` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `.claude` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8725ddf2ce4b925a7ce68ba90eca353455ac34b5` is the revision these paths and observations refer to.
