# Project structure: paperswithbacktest/awesome-systematic-trading

**Analysed commit:** `ddfee8bb548bd6914191cb8fdb695d533ae16b0d`

**Commit reference:** [ddfee8bb548bd6914191cb8fdb695d533ae16b0d](https://github.com/paperswithbacktest/awesome-systematic-trading/commit/ddfee8bb548bd6914191cb8fdb695d533ae16b0d)

**Tree at this commit:** [paperswithbacktest/awesome-systematic-trading@ddfee8bb548b](https://github.com/paperswithbacktest/awesome-systematic-trading/tree/ddfee8bb548bd6914191cb8fdb695d533ae16b0d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | paperswithbacktest/awesome-systematic-trading |
| Description | A curated list of awesome libraries, packages, strategies, books, blogs, tutorials for systematic trading. |
| Stars | 15359 |
| Forks | 1865 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `ddfee8bb548bd6914191cb8fdb695d533ae16b0d` |
| Retrieved at | 2026-11-14T19:09:03.735066+00:00 |
| Files in this snapshot | 71 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    link-check.yml
.vscode/  (2 files)
  launch.json
  settings.json
scripts/  (3 files)
  build_strategies_table.py
  check_links.py
  update_counts.py
static/  (61 files)
  strategies/  (61 files)
    12-month-cycle-in-cross-section-of-stocks-returns.py
    52-weeks-high-effect-in-stocks.py
    accrual-anomaly.py
    asset-class-momentum-rotational-system.py
    asset-class-trend-following.py
    asset-growth-effect.py
    betting-against-beta-factor-in-country-equity-indexes.py
    betting-against-beta-factor-in-stocks.py
    combining-fundamental-fscore-and-equity-short-term-reversals.py
    combining-smart-factors-momentum-and-market-portfolio.py
    consistent-momentum-strategy.py
    crude-oil-predicts-equity-returns.py
    currency-momentum-factor.py
    currency-value-factor-ppp-strategy.py
    dispersion-trading.py
    dollar-carry-trade.py
    earnings-announcement-premium.py
    earnings-announcements-combined-with-stock-repurchases.py
    earnings-quality-factor.py
    esg-factor-momentum-strategy.py
    fed-model.py
    fx-carry-trade.py
    how-to-use-lexical-density-of-company-filings.py
    intraday-seasonality-in-bitcoin.py
    … 37 more files
.gitignore
README.md
README_ja.md
README_zh.md
```

## Entry points

- [scripts/build_strategies_table.py:234](https://github.com/paperswithbacktest/awesome-systematic-trading/blob/ddfee8bb548bd6914191cb8fdb695d533ae16b0d/scripts/build_strategies_table.py#L234)
- [scripts/check_links.py:96](https://github.com/paperswithbacktest/awesome-systematic-trading/blob/ddfee8bb548bd6914191cb8fdb695d533ae16b0d/scripts/check_links.py#L96)
- [scripts/update_counts.py:139](https://github.com/paperswithbacktest/awesome-systematic-trading/blob/ddfee8bb548bd6914191cb8fdb695d533ae16b0d/scripts/update_counts.py#L139)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: active_window, asset_bucket, classify, clean_title, count, fetch. |
| static package | library | Observed | Groups 60 file(s) under static package (observed from repository paths and static analysis). Observed top-level classes: AccrualAnomaly, AccrualsData, AcrrualsData, AssetClassTrendFollowing, AssetGrowthEffect, BettingAg… |

## Important files

- `.github/workflows/link-check.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)

## Top-level layout

- `static` — 61 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ddfee8bb548bd6914191cb8fdb695d533ae16b0d` is the revision these paths and observations refer to.
