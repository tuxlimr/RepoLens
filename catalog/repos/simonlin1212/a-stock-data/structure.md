# Project structure: simonlin1212/a-stock-data

**Analysed commit:** `f21534946c42be3ad048ac938eecb1bad84cb8ab`

**Commit reference:** [f21534946c42be3ad048ac938eecb1bad84cb8ab](https://github.com/simonlin1212/a-stock-data/commit/f21534946c42be3ad048ac938eecb1bad84cb8ab)

**Tree at this commit:** [simonlin1212/a-stock-data@f21534946c42](https://github.com/simonlin1212/a-stock-data/tree/f21534946c42be3ad048ac938eecb1bad84cb8ab)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | simonlin1212/a-stock-data |
| Description | A股全栈数据工具包：行情K线·当日逐笔·研报·信号·资金面·新闻·财务·公告·打板·ETF期权·舆情·宏观利率·期货大宗(含大商所日K)·事件驱动·可转债 | 15层·87端点·34数据源·除iwencai外免Key | A-share data for AI agents: K-lines, ticks, reports, fund flow, news, financials, filings, options, macro, futures, events, convertibles | 15 layers·87 endpoints·34 sources |
| Stars | 11823 |
| Forks | 2142 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `f21534946c42be3ad048ac938eecb1bad84cb8ab` |
| Retrieved at | 2026-11-14T19:10:22.544223+00:00 |
| Files in this snapshot | 25 |

## Directory tree

```text
assets/  (1 files)
  .gitkeep
docs/  (2 files)
  source-integration-v3.8.0.md
  source-integration-v3.9.0.md
tests/  (17 files)
  fixtures/  (12 files)
    sina_adjust/  (12 files)
      … 12 files under this directory
  test_official_data.py
  test_v310_sources.py
  test_v37_adjust_factor.py
  test_v39_sources.py
  test_valuation.py
.gitignore
CHANGELOG.md
LICENSE
README.md
README_en.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CffexDailyWitnessTests, ChinaBondTests, ConvertibleBondTests, EastmoneyStrictTests, EquityPledgeTests, Erro… |

## Important files

No manifest, config, CI, or container files were observed in the analysed set.

## Top-level layout

- `tests` — 17 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `docs` — 2 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f21534946c42be3ad048ac938eecb1bad84cb8ab` is the revision these paths and observations refer to.
