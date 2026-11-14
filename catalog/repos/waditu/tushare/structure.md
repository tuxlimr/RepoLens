# Project structure: waditu/tushare

**Analysed commit:** `093856995af0811d3ebbe8c179b8febf4ae706f0`

**Commit reference:** [093856995af0811d3ebbe8c179b8febf4ae706f0](https://github.com/waditu/tushare/commit/093856995af0811d3ebbe8c179b8febf4ae706f0)

**Tree at this commit:** [waditu/tushare@093856995af0](https://github.com/waditu/tushare/tree/093856995af0811d3ebbe8c179b8febf4ae706f0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | waditu/tushare |
| Description | TuShare is a utility for crawling historical data of China stocks |
| Stars | 15493 |
| Forks | 4419 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `093856995af0811d3ebbe8c179b8febf4ae706f0` |
| Retrieved at | 2026-11-14T19:09:01.847535+00:00 |
| Files in this snapshot | 91 |

## Directory tree

```text
docs/  (14 files)
  billboard.rst
  boxoffice.rst
  classifying.rst
  datayes.rst
  donate.rst
  fundamental.rst
  index.rst
  macro.rst
  newsevent.rst
  preface.rst
  reference.rst
  shibor.rst
  storing.rst
  trading.rst
issues/  (2 files)
  from_email.txt
  from_sns.txt
test/  (14 files)
  __init__.py
  bar_test.py
  billboard_test.py
  classifying_test.py
  dateu_test.py
  fund_test.py
  indictor_test.py
  macro_test.py
  nav_test.py
  news_test.py
  ref_test.py
  shibor_test.py
  storing_test.py
  trading_test.py
tushare/  (52 files)
  bond/  (2 files)
    __init__.py
    bonds.py
  coins/  (2 files)
    __init__.py
    market.py
  data/  (1 files)
    __init__.py
  fund/  (3 files)
    __init__.py
    cons.py
    nav.py
  futures/  (5 files)
    __init__.py
    cons.py
    domestic.py
    domestic_cons.py
    intlfutures.py
  internet/  (4 files)
    __init__.py
    boxoffice.py
    caixinnews.py
    indexes.py
  pro/  (3 files)
    __init__.py
    client.py
    data_pro.py
  stock/  (16 files)
    __init__.py
    billboard.py
    classifying.py
    cons.py
    fundamental.py
    globals.py
    indictor.py
    macro.py
    macro_vars.py
    news_vars.py
    newsevent.py
    ref_vars.py
    reference.py
    shibor.py
    trading.py
    trendline.py
  trader/  (4 files)
    __init__.py
    trader.py
    utils.py
    vars.py
  util/  (10 files)
    __init__.py
    common.py
    conns.py
    dateu.py
    formula.py
    mailmerge.py
    netbase.py
    store.py
    upass.py
    vars.py
  VERSION.txt
  __init__.py
.gitignore
.travis.yml
LICENSE
MANIFEST
README.md
requirements.txt
setup.py
test_unittest.py
whats_new.md
```

## Entry points

- [test_unittest.py:23](https://github.com/waditu/tushare/blob/093856995af0811d3ebbe8c179b8febf4ae706f0/test_unittest.py#L23)
- [tushare/bond/bonds.py:16](https://github.com/waditu/tushare/blob/093856995af0811d3ebbe8c179b8febf4ae706f0/tushare/bond/bonds.py#L16)
- [tushare/pro/data_pro.py:143](https://github.com/waditu/tushare/blob/093856995af0811d3ebbe8c179b8febf4ae706f0/tushare/pro/data_pro.py#L143)
- [tushare/stock/trendline.py:981](https://github.com/waditu/tushare/blob/093856995af0811d3ebbe8c179b8febf4ae706f0/tushare/stock/trendline.py#L981)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: read, read_install_requires. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _ema, _ma, _md, adtm, arbr, asi. |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: DataApi. |
| Tests | test | Observed | Groups 15 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Test, TestTrading, Test_Is_holiday. Observed top-level functions: appends, csv, db, hdf, json, nosql. |
| tushare package | library | Observed | Groups 46 file(s) under tushare package (observed from repository paths and static analysis). Observed top-level classes: Client, MailMerge, NotLoginError, Store, TraderAPI. Observed top-level functions: ABS, ADTM, ATR,… |

## Important files

- `.travis.yml` (ci)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `tushare` — 52 analysed file(s)
- `docs` — 14 analysed file(s)
- `test` — 14 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `issues` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File tushare/internet/caixinnews.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `093856995af0811d3ebbe8c179b8febf4ae706f0` is the revision these paths and observations refer to.
