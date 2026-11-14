# Project structure: myhhub/stock

**Analysed commit:** `b6e0ca2268cfbadd02f5ed052159c187b6670231`

**Commit reference:** [b6e0ca2268cfbadd02f5ed052159c187b6670231](https://github.com/myhhub/stock/commit/b6e0ca2268cfbadd02f5ed052159c187b6670231)

**Tree at this commit:** [myhhub/stock@b6e0ca2268cf](https://github.com/myhhub/stock/tree/b6e0ca2268cfbadd02f5ed052159c187b6670231)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | myhhub/stock |
| Description | stock股票.获取股票数据,计算股票指标,筹码分布,识别股票形态,综合选股,选股策略,股票验证回测,股票自动交易,支持PC及移动设备。 |
| Stars | 15208 |
| Forks | 3112 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `b6e0ca2268cfbadd02f5ed052159c187b6670231` |
| Retrieved at | 2026-11-14T19:09:06.458612+00:00 |
| Files in this snapshot | 141 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    azure-container-webapp.yml
    docker-image.yml
cron/  (3 files)
  cron.hourly/  (1 files)
    run_hourly
  cron.monthly/  (1 files)
    run_monthly
  cron.workdayly/  (1 files)
    run_workdayly
docker/  (5 files)
  .dockerignore
  .gitignore
  Dockerfile
  build.sh
  docker-compose.yml
instock/  (126 files)
  bin/  (7 files)
    restart_web.sh
    run_cron.sh
    run_job.bat
    run_job.sh
    run_trade.bat
    run_web.bat
    run_web.sh
  config/  (4 files)
    .gitignore
    eastmoney_cookie.txt
    proxy.txt
    trade_client.json
  core/  (50 files)
    backtest/  (3 files)
      … 3 files under this directory
    crawling/  (13 files)
      … 13 files under this directory
    indicator/  (3 files)
      … 3 files under this directory
    kline/  (6 files)
      … 6 files under this directory
    pattern/  (3 files)
      … 3 files under this directory
    strategy/  (12 files)
      … 12 files under this directory
    .gitignore
    __init__.py
    eastmoney_fetcher.py
    singleton_proxy.py
    singleton_stock.py
    singleton_stock_web_module_data.py
    singleton_trade_date.py
    stockfetch.py
    tablestructure.py
    web_module_data.py
  job/  (12 files)
    .gitignore
    __init__.py
    backtest_data_daily_job.py
    basic_data_after_close_daily_job.py
    basic_data_daily_job.py
    basic_data_other_daily_job.py
    execute_daily_job.py
    indicators_data_daily_job.py
    init_job.py
    klinepattern_data_daily_job.py
    selection_data_daily_job.py
    strategy_data_daily_job.py
  lib/  (9 files)
    .gitignore
    __init__.py
    crypto_aes.py
    database.py
    run_template.py
    singleton_type.py
    torndb.py
    trade_time.py
    version.py
  trade/  (20 files)
    robot/  (12 files)
      … 12 files under this directory
    strategies/  (4 files)
      … 4 files under this directory
    .gitignore
    __init__.py
    trade_service.py
    usage.md
  web/  (22 files)
    static/  (5 files)
      … 5 files under this directory
    templates/  (11 files)
      … 11 files under this directory
    .gitignore
    __init__.py
    base.py
    dataIndicatorsHandler.py
    dataTableHandler.py
    web_service.py
  .gitignore
  __init__.py
supervisor/  (1 files)
  supervisord.conf
.gitignore
LICENSE
README.md
requirements.txt
```

## Entry points

- [instock/core/crawling/fund_etf_em.py:349](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/fund_etf_em.py#L349)
- [instock/core/crawling/stock_chip_race.py:152](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/stock_chip_race.py#L152)
- [instock/core/crawling/stock_cpbd.py:138](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/stock_cpbd.py#L138)
- [instock/core/crawling/stock_dzjy_em.py:537](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/stock_dzjy_em.py#L537)
- [instock/core/crawling/stock_fhps_em.py:149](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/stock_fhps_em.py#L149)
- [instock/core/crawling/stock_fund_em.py:435](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/stock_fund_em.py#L435)
- [instock/core/crawling/stock_hist_em.py:579](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/stock_hist_em.py#L579)
- [instock/core/crawling/stock_lhb_em.py:862](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/stock_lhb_em.py#L862)
- [instock/core/crawling/stock_lhb_sina.py:245](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/stock_lhb_sina.py#L245)
- [instock/core/crawling/stock_limitup_reason.py:121](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/stock_limitup_reason.py#L121)
- [instock/core/crawling/stock_selection.py:99](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/stock_selection.py#L99)
- [instock/core/crawling/trade_date_hist.py:330](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/core/crawling/trade_date_hist.py#L330)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: checkTableIsExist, engine, engine_to_db, executeSql, executeSqlCount, executeSqlFetch. |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 25 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AEScryptor, Application, HomeHandler, MData. Observed top-level functions: _find_last_pag… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| instock package | library | Observed | Groups 32 file(s) under instock package (observed from repository paths and static analysis). Observed top-level classes: BaseHandler, Clock, ClockEngine, ClockIntervalHandler, ClockMomentHandler, Connection. Observed t… |
| Service / domain layer | service | Observed | Groups 32 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: CYQCalculator, eastmoney_fetcher, proxys, stock_data, stock_hist_data, stock_trade_date. O… |

## Important files

- `.github/workflows/azure-container-webapp.yml` (ci)
- `.github/workflows/docker-image.yml` (ci)
- `docker/.dockerignore` (container)
- `docker/Dockerfile` (container)
- `docker/docker-compose.yml` (container)
- `instock/config/trade_client.json` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `instock` — 126 analysed file(s)
- `docker` — 5 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `cron` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `supervisor` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b6e0ca2268cfbadd02f5ed052159c187b6670231` is the revision these paths and observations refer to.
