# Project structure: akfamily/akshare

**Analysed commit:** `f43ea5f1175021eea742638354bcaa7de9ecaf99`

**Commit reference:** [f43ea5f1175021eea742638354bcaa7de9ecaf99](https://github.com/akfamily/akshare/commit/f43ea5f1175021eea742638354bcaa7de9ecaf99)

**Tree at this commit:** [akfamily/akshare@f43ea5f11750](https://github.com/akfamily/akshare/tree/f43ea5f1175021eea742638354bcaa7de9ecaf99)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | akfamily/akshare |
| Description | AKShare is an elegant and simple financial data interface library for Python, built for human beings! 开源财经数据接口库 |
| Stars | 23340 |
| Forks | 3576 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `f43ea5f1175021eea742638354bcaa7de9ecaf99` |
| Retrieved at | 2026-11-14T19:07:47.581879+00:00 |
| Files in this snapshot | 493 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    akshare_enhancement.yml
    akshare_report.yml
    config.yml
  workflows/  (2 files)
    main_dev_check.yml
    release_and_deploy.yml
  dependabot.yml
akshare/  (386 files)
  alternative/  (18 files)
    __init__.py
    alternative_air_hebei.py
    alternative_air_zhenqi.py
    alternative_bank_cons.py
    alternative_bank_nfra.py
    alternative_car_cpca.py
    alternative_fortune_500.py
    alternative_fortune_bloomberg.py
    alternative_fortune_forbes_500.py
    alternative_fortune_hurun.py
    alternative_migration_baidu.py
    alternative_migration_cons.py
    alternative_movie_yien.py
    alternative_news_cctv.py
    alternative_nlp.py
    alternative_sunrise_tad.py
    alternative_taptap.py
    alternative_weibo_nlp.py
  bond/  (17 files)
    __init__.py
    bond_buy_back_em.py
    bond_cb_sina.py
    bond_cb_ths.py
    bond_cbond.py
    bond_china.py
    bond_china_money.py
    bond_convert.py
    bond_em.py
    bond_gb_sina.py
    bond_info_cm.py
    bond_issue_cninfo.py
    bond_nafmii.py
    bond_summary.py
    bond_zh_cov.py
    bond_zh_sina.py
    cons.py
  calendar/  (2 files)
    __init__.py
    calendar_trade_date_hist.py
  crypto/  (4 files)
    __init__.py
    crypto_bitcoin_cme.py
    crypto_hold.py
    crypto_js_spot.py
  data/  (7 files)
    __init__.py
    calendar.json
    crypto.js
    jm.js
    outcrypto.js
    renames.json
    ths.js
  energy/  (3 files)
    __init__.py
    energy_carbon.py
    energy_oil_em.py
  fund/  (31 files)
    __init__.py
    fund_amac.py
    fund_announcement_em.py
    fund_aum_em.py
    fund_em.py
    fund_etf_em.py
    fund_etf_holding_js.py
    fund_etf_pcf.py
    fund_etf_sina.py
    fund_etf_sse.py
    fund_etf_szse.py
    fund_etf_ths.py
    fund_fee_em.py
    fund_fhsp_em.py
    fund_info_ths.py
    fund_init_em.py
    fund_init_ths.py
    fund_lof_em.py
    fund_manager.py
    fund_overview_em.py
    fund_portfolio_em.py
    fund_position_lg.py
    fund_qdii_jsl.py
    fund_rank_em.py
    … 7 more files
  futures/  (41 files)
    __init__.py
    cons.py
    futures_basis.py
    futures_cftc_js.py
    futures_comex_em.py
    futures_comm_ctp.py
    futures_comm_js.py
    futures_comm_qihuo.py
    futures_contract_detail.py
    futures_contract_info_cffex.py
    futures_contract_info_czce.py
    futures_contract_info_dce.py
    futures_contract_info_gfex.py
    futures_contract_info_ine.py
    futures_contract_info_shfe.py
    futures_cot.py
    futures_cot_sina.py
    futures_daily_bar.py
    futures_foreign.py
    futures_hf_em.py
    futures_hist_em.py
    futures_hog.py
    futures_hog_index.py
    futures_hq_sina.py
    … 17 more files
  fx/  (11 files)
    __init__.py
    cons.py
    cons_forex.py
    fx_c_swap_cm.py
    fx_china_bank_sina.py
    fx_currency_investing.py
    fx_forex_em.py
    fx_quote.py
    fx_quote_baidu.py
    fx_safe.py
    fx_sentiment_jin10.py
  index/  (23 files)
    __init__.py
    cons.py
    index_cflp.py
    index_cni.py
    index_cons.py
    index_csindex.py
    index_drewry.py
    index_global_em.py
    index_global_sina.py
    index_kq_ss.py
    index_option_qvix.py
    index_research_fund_sw.py
    index_research_sw.py
    index_sox_em.py
    index_sp500_min.py
    index_spot.py
    index_stock_hk.py
    index_stock_us_sina.py
    index_stock_zh.py
    index_stock_zh_csindex.py
    index_sugar.py
    index_sw.py
    index_zh_em.py
  interest_rate/  (6 files)
    __init__.py
    interest_rate_ibor_js.py
    interest_rate_interbank_em.py
    interest_rate_lpr_em.py
    interest_rate_repo.py
    interest_rate_swap_cm.py
  macro/  (17 files)
    __init__.py
    cons.py
    macro_australia.py
    macro_canada.py
    macro_china.py
    macro_china_cx.py
    macro_china_hk.py
    macro_china_nbs.py
    macro_cnbs.py
    macro_finance_ths.py
    macro_germany.py
    macro_info_ws.py
    macro_japan.py
    macro_news_baidu.py
    macro_swiss.py
    macro_uk.py
    macro_usa.py
  option/  (19 files)
    __init__.py
    cons.py
    option_comm_qihuo.py
    option_commodity.py
    option_commodity_sina.py
    option_contract_info_ctp.py
    option_current_sse.py
    option_current_szse.py
    option_czce.py
    option_daily_stats_sse_szse.py
    option_em.py
    option_finance.py
    option_finance_sina.py
    option_lhb_em.py
    option_margin.py
    option_premium_analysis_em.py
    option_risk_analysis_em.py
    option_risk_indicator_sse.py
    option_value_analysis_em.py
  research/  (7 files)
    __init__.py
    cons.py
    research_epu_index.py
    research_ff_factor.py
    research_fred_md.py
    research_risk_rv.py
    research_rv.py
  spot/  (5 files)
    __init__.py
    spot_hog_soozhu.py
    spot_price_qh.py
    spot_sge.py
    spot_sge_js.py
  stock/  (158 files)
    board/  (17 files)
      … 17 files under this directory
    finance/  (19 files)
      … 19 files under this directory
    flow/  (17 files)
      … 17 files under this directory
    holder/  (10 files)
      … 10 files under this directory
    issue/  (19 files)
      … 19 files under this directory
    other/  (4 files)
      … 4 files under this directory
    quote/  (28 files)
      … 28 files under this directory
    research/  (25 files)
      … 25 files under this directory
    valuation/  (17 files)
      … 17 files under this directory
    __init__.py
    cons.py
  utils/  (11 files)
    __init__.py
    baidu_finance.py
    cons.py
    context.py
    func.py
    http.py
    jsonish.py
    multi_decrypt.py
    params.py
    request.py
    tqdm.py
  __init__.py
  _version.py
  datasets.py
  exceptions.py
  registry.py
  request.py
docs/  (52 files)
  _static/  (1 files)
    custom.css
  _templates/  (2 files)
    ak-navbar.html
    wechat.html
  data/  (27 files)
    alternative/  (1 files)
      … 1 files under this directory
    bond/  (1 files)
      … 1 files under this directory
    calendar/  (1 files)
      … 1 files under this directory
    crypto/  (1 files)
      … 1 files under this directory
    energy/  (1 files)
      … 1 files under this directory
    fund/  (1 files)
      … 1 files under this directory
    fx/  (1 files)
      … 1 files under this directory
    index/  (1 files)
      … 1 files under this directory
    interest_rate/  (1 files)
      … 1 files under this directory
    macro/  (5 files)
      … 5 files under this directory
    option/  (1 files)
      … 1 files under this directory
    research/  (1 files)
      … 1 files under this directory
    spot/  (1 files)
      … 1 files under this directory
    stock/  (9 files)
      … 9 files under this directory
    index.rst
  README.rst
  acknowledgements.md
  aktools.md
  articles.md
  backtest.md
  changelog.md
  changelog_archive.md
  conf.py
  contributing.md
  faq.md
  index.rst
  indicator.md
  installation.md
  introduction.md
  mcp.md
  migration.md
  quant_platforms.md
  requirements.txt
  search.md
  trade.md
  tutorial.md
  uv.md
scripts/  (6 files)
  build_registry.py
  check_punctuation.py
  check_release.py
  registry_alternatives.json
  registry_baseline.json
  registry_removed.json
tests/  (33 files)
  __init__.py
  conftest.py
  naming_baseline.json
  positional_columns_baseline.json
  test_bond_info_cm.py
  test_build_registry.py
  test_check_release.py
  test_ffill_to_index.py
  test_fred_md.py
  test_func.py
  test_fund_etf_pcf.py
  test_futures_comm_qihuo.py
  test_futures_main_contract.py
  test_http.py
  test_http_retry.py
  test_index_stock_zh.py
  test_index_sugar.py
  test_iteration_order.py
  test_js_engine.py
  test_jsonish.py
  test_legu_csrf.py
  test_naming.py
  test_news_cctv.py
  test_params.py
  … 9 more files
.gitignore
.pre-commit-config.yaml
.python-version
.readthedocs.yaml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
llms.txt
pyproject.toml
```

## Entry points

- [akshare/alternative/alternative_air_hebei.py:106](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_air_hebei.py#L106)
- [akshare/alternative/alternative_air_zhenqi.py:299](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_air_zhenqi.py#L299)
- [akshare/alternative/alternative_bank_nfra.py:190](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_bank_nfra.py#L190)
- [akshare/alternative/alternative_car_cpca.py:264](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_car_cpca.py#L264)
- [akshare/alternative/alternative_fortune_500.py:155](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_fortune_500.py#L155)
- [akshare/alternative/alternative_fortune_bloomberg.py:71](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_fortune_bloomberg.py#L71)
- [akshare/alternative/alternative_fortune_forbes_500.py:47](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_fortune_forbes_500.py#L47)
- [akshare/alternative/alternative_fortune_hurun.py:308](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_fortune_hurun.py#L308)
- [akshare/alternative/alternative_migration_baidu.py:110](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_migration_baidu.py#L110)
- [akshare/alternative/alternative_movie_yien.py:676](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_movie_yien.py#L676)
- [akshare/alternative/alternative_news_cctv.py:187](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_news_cctv.py#L187)
- [akshare/alternative/alternative_nlp.py:29](https://github.com/akfamily/akshare/blob/f43ea5f1175021eea742638354bcaa7de9ecaf99/akshare/alternative/alternative_nlp.py#L29)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| akshare package | library | Observed | Groups 51 file(s) under akshare package (observed from repository paths and static analysis). Observed top-level classes: APIError, AkshareConfig, AkshareException, CurlSession, DataParsingError, DceBlockedError. Observ… |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 331 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ModuleIndex, TLSAdapter, _LegacySSLAdapter. Observed top-level functions: __bond_registe… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 33 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeResponse, _Racer, _Resp, _Response. Observed top-level functions: _count, _daily_row, _dates, _fail_on_… |

## Important files

- `.github/ISSUE_TEMPLATE/akshare_enhancement.yml` (config)
- `.github/ISSUE_TEMPLATE/akshare_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/main_dev_check.yml` (ci)
- `.github/workflows/release_and_deploy.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `akshare/data/calendar.json` (config)
- `akshare/data/renames.json` (config)
- `docs/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `scripts/registry_alternatives.json` (config)
- `scripts/registry_baseline.json` (config)
- `scripts/registry_removed.json` (config)

## Top-level layout

- `akshare` — 386 analysed file(s)
- `docs` — 52 analysed file(s)
- `tests` — 33 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 6 analysed file(s)
- `scripts` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f43ea5f1175021eea742638354bcaa7de9ecaf99` is the revision these paths and observations refer to.
