# Project structure: ranaroussi/yfinance

**Analysed commit:** `2492a853aee975b4f39f230ad763298f039e37ae`

**Commit reference:** [2492a853aee975b4f39f230ad763298f039e37ae](https://github.com/ranaroussi/yfinance/commit/2492a853aee975b4f39f230ad763298f039e37ae)

**Tree at this commit:** [ranaroussi/yfinance@2492a853aee9](https://github.com/ranaroussi/yfinance/tree/2492a853aee975b4f39f230ad763298f039e37ae)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ranaroussi/yfinance |
| Description | Download market data from Yahoo! Finance's API |
| Stars | 25918 |
| Forks | 3494 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `2492a853aee975b4f39f230ad763298f039e37ae` |
| Retrieved at | 2026-11-14T19:07:28.218882+00:00 |
| Files in this snapshot | 218 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.yaml
  workflows/  (7 files)
    auto_close_default_issues.yml
    deploy_doc.yml
    pyright.yml
    pytest.yml.disabled
    python-publish.yml
    ruff.yml
    zizmor.yml
  FUNDING.yml
  dependabot.yml
doc/  (48 files)
  source/  (46 files)
    _static/  (1 files)
      … 1 files under this directory
    _templates/  (1 files)
      … 1 files under this directory
    advanced/  (8 files)
      … 8 files under this directory
    development/  (5 files)
      … 5 files under this directory
    reference/  (29 files)
      … 29 files under this directory
    conf.py
    index.rst
  Makefile
  make.bat
maintainer/  (2 files)
  prompts/  (1 files)
    update-github-actions.txt
  verify_github_actions.sh
tests/  (112 files)
  data/  (88 files)
    1398-HK-1d-bad-div-fixed.csv
    1398-HK-1d-bad-div.csv
    3988-HK-1d-bad-div-fixed.csv
    3988-HK-1d-bad-div.csv
    4063-T-1d-bad-div-fixed.csv
    4063-T-1d-bad-div.csv
    4063-T-1d-bad-stock-split-fixed.csv
    4063-T-1d-bad-stock-split.csv
    8TRA-DE-1d-missing-div-adjust-fixed.csv
    8TRA-DE-1d-missing-div-adjust.csv
    ABDP-L-1d-bad-div-fixed.csv
    ABDP-L-1d-bad-div.csv
    ADIG-L-1d-bad-div-fixed.csv
    ADIG-L-1d-bad-div.csv
    AET-L-1d-100x-error-fixed.csv
    AET-L-1d-100x-error.csv
    ALPHA-PA-1d-bad-stock-split-fixed.csv
    ALPHA-PA-1d-bad-stock-split.csv
    ASAI-L-1h-bad-unit-fixed.csv
    ASAI-L-1h-bad-unit.csv
    AV-L-1wk-bad-stock-split-fixed.csv
    AV-L-1wk-bad-stock-split.csv
    CALM-1d-no-bad-divs.csv
    CLC-L-1d-bad-div-fixed.csv
    … 64 more files
  __init__.py
  context.py
  test_auth.py
  test_cache.py
  test_cache_noperms.py
  test_calendars.py
  test_calendars_cache.py
  test_cookie_crumb_degradation.py
  test_data.py
  test_download_concurrency.py
  test_http.py
  test_live.py
  test_lookup.py
  test_market.py
  test_multi.py
  test_price_repair.py
  test_price_shift_detection.py
  test_prices.py
  test_screener.py
  test_search.py
  test_sector_region.py
  test_ticker.py
  test_ticker_locale.py
  test_utils.py
yfinance/  (35 files)
  domain/  (5 files)
    __init__.py
    domain.py
    industry.py
    market.py
    sector.py
  scrapers/  (7 files)
    __init__.py
    analysis.py
    fundamentals.py
    funds.py
    holders.py
    quote.py
    yahoo-keys.txt
  screener/  (3 files)
    __init__.py
    query.py
    screener.py
  __init__.py
  _http.py
  base.py
  cache.py
  calendars.py
  config.py
  const.py
  data.py
  exceptions.py
  live.py
  lookup.py
  multi.py
  pricing.proto
  pricing_pb2.py
  search.py
  shared.py
  ticker.py
  tickers.py
  utils.py
  version.py
.gitignore
.travis.yml
CHANGELOG.md
CHANGELOG.rst
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.txt
README.md
meta.yaml
pyproject.toml
ruff.toml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigMgr, NestedConfig. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| maintainer package | library | Observed | Groups 1 file(s) under maintainer package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: Domain, Industry, Market, MarketRegion, Sector. |
| Tests | test | Observed | Groups 112 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH yfinance.screener.screener.YfData.post, PATCH yfinance.data.YfData.post, PATCH yfinance.data.YfData.get, PATCH… |
| yfinance package | library | Observed | Groups 27 file(s) under yfinance package (observed from repository paths and static analysis). Observed top-level classes: Analysis, AsyncWebSocket, Auth, BaseWebSocket, CalendarQuery, Calendars. Observed top-level func… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/auto_close_default_issues.yml` (ci)
- `.github/workflows/deploy_doc.yml` (ci)
- `.github/workflows/pyright.yml` (ci)
- `.github/workflows/pytest.yml.disabled` (ci)
- `.github/workflows/python-publish.yml` (ci)
- `.github/workflows/ruff.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.travis.yml` (ci)
- `meta.yaml` (config)
- `pyproject.toml` (manifest)
- `ruff.toml` (config)

## Top-level layout

- `tests` — 112 analysed file(s)
- `doc` — 48 analysed file(s)
- `yfinance` — 35 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 10 analysed file(s)
- `maintainer` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2492a853aee975b4f39f230ad763298f039e37ae` is the revision these paths and observations refer to.
