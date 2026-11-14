# Project structure: mementum/backtrader

**Analysed commit:** `b853d7c90b6721476eb5a5ea3135224e33db1f14`

**Commit reference:** [b853d7c90b6721476eb5a5ea3135224e33db1f14](https://github.com/mementum/backtrader/commit/b853d7c90b6721476eb5a5ea3135224e33db1f14)

**Tree at this commit:** [mementum/backtrader@b853d7c90b67](https://github.com/mementum/backtrader/tree/b853d7c90b6721476eb5a5ea3135224e33db1f14)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mementum/backtrader |
| Description | Python Backtesting library for trading strategies |
| Stars | 23740 |
| Forks | 5327 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `b853d7c90b6721476eb5a5ea3135224e33db1f14` |
| Retrieved at | 2026-11-14T19:07:47.204502+00:00 |
| Files in this snapshot | 372 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
backtrader/  (171 files)
  analyzers/  (16 files)
    __init__.py
    annualreturn.py
    calmar.py
    drawdown.py
    leverage.py
    logreturnsrolling.py
    periodstats.py
    positions.py
    pyfolio.py
    returns.py
    sharpe.py
    sqn.py
    timereturn.py
    tradeanalyzer.py
    transactions.py
    vwr.py
  brokers/  (5 files)
    __init__.py
    bbroker.py
    ibbroker.py
    oandabroker.py
    vcbroker.py
  btrun/  (2 files)
    __init__.py
    btrun.py
  commissions/  (1 files)
    __init__.py
  feeds/  (18 files)
    __init__.py
    blaze.py
    btcsv.py
    chainer.py
    csvgeneric.py
    ibdata.py
    influxfeed.py
    mt4csv.py
    oanda.py
    pandafeed.py
    quandl.py
    rollover.py
    sierrachart.py
    vcdata.py
    vchart.py
    vchartcsv.py
    vchartfile.py
    yahoo.py
  filters/  (9 files)
    __init__.py
    bsplitter.py
    calendardays.py
    datafiller.py
    datafilter.py
    daysteps.py
    heikinashi.py
    renko.py
    session.py
  indicators/  (51 files)
    contrib/  (2 files)
      … 2 files under this directory
    __init__.py
    accdecoscillator.py
    aroon.py
    atr.py
    awesomeoscillator.py
    basicops.py
    bollinger.py
    cci.py
    crossover.py
    dema.py
    deviation.py
    directionalmove.py
    dma.py
    dpo.py
    dv2.py
    ema.py
    envelope.py
    hadelta.py
    heikinashi.py
    hma.py
    hurst.py
    ichimoku.py
    kama.py
    kst.py
    … 25 more files
  observers/  (8 files)
    __init__.py
    benchmark.py
    broker.py
    buysell.py
    drawdown.py
    logreturns.py
    timereturn.py
    trades.py
  plot/  (8 files)
    __init__.py
    finance.py
    formatters.py
    locator.py
    multicursor.py
    plot.py
    scheme.py
    utils.py
  signals/  (1 files)
    __init__.py
  sizers/  (3 files)
    __init__.py
    fixedsize.py
    percents_sizer.py
  stores/  (5 files)
    __init__.py
    ibstore.py
    oandastore.py
    vchartfile.py
    vcstore.py
  strategies/  (2 files)
    __init__.py
    sma_crossover.py
  studies/  (3 files)
    contrib/  (2 files)
      … 2 files under this directory
    __init__.py
  utils/  (7 files)
    __init__.py
    autodict.py
    date.py
    dateintern.py
    flushfile.py
    ordereddefaultdict.py
    py3.py
  __init__.py
  analyzer.py
  broker.py
  cerebro.py
  comminfo.py
  dataseries.py
  errors.py
  feed.py
  fillers.py
  flt.py
  functions.py
  indicator.py
  linebuffer.py
  lineiterator.py
  lineroot.py
  lineseries.py
  mathsupport.py
  metabase.py
  observer.py
  order.py
  position.py
  resamplerfilter.py
  signal.py
  sizer.py
  … 8 more files
contrib/  (5 files)
  datas/  (2 files)
    daily-KO.csv
    daily-PEP.csv
  samples/  (1 files)
    pair-trading/  (1 files)
      … 1 files under this directory
  utils/  (2 files)
    influxdb-import.py
    iqfeed-to-influxdb.py
datas/  (17 files)
  2005-2006-day-001.txt
  2006-day-001-optix.txt
  2006-day-001.txt
  2006-day-002.txt
  2006-min-005.txt
  2006-month-001.txt
  2006-volume-day-001.txt
  2006-week-001.txt
  2006-week-002.txt
  bidask.csv
  bidask2.csv
  nvda-2014.txt
  orcl-2003-2005.txt
  orcl-2014.txt
  ticksample.csv
  yhoo-2003-2005.txt
  yhoo-2014.txt
samples/  (85 files)
  analyzer-annualreturn/  (1 files)
    analyzer-annualreturn.py
  bidask-to-ohlc/  (1 files)
    bidask-to-ohlc.py
  bracket/  (1 files)
    bracket.py
  btfd/  (1 files)
    btfd.py
  calendar-days/  (1 files)
    calendar-days.py
  calmar/  (1 files)
    calmar-test.py
  cheat-on-open/  (1 files)
    cheat-on-open.py
  commission-schemes/  (1 files)
    commission-schemes.py
  credit-interest/  (1 files)
    credit-interest.py
  data-bid-ask/  (1 files)
    bidask.py
  data-filler/  (2 files)
    data-filler.py
    relativevolume.py
  data-multitimeframe/  (1 files)
    data-multitimeframe.py
  data-pandas/  (2 files)
    data-pandas-optix.py
    data-pandas.py
  data-replay/  (1 files)
    data-replay.py
  data-resample/  (1 files)
    data-resample.py
  daysteps/  (1 files)
    daysteps.py
  future-spot/  (1 files)
    future-spot.py
  gold-vs-sp500/  (1 files)
    gold-vs-sp500.py
  ib-cash-bid-ask/  (1 files)
    ib-cash-bid-ask.py
  ibtest/  (1 files)
    ibtest.py
  kselrsi/  (1 files)
    ksignal.py
  lineplotter/  (1 files)
    lineplotter.py
  lrsi/  (1 files)
    lrsi-test.py
  macd-settings/  (1 files)
    macd-settings.py
  memory-savings/  (1 files)
    memory-savings.py
  mixing-timeframes/  (1 files)
    mixing-timeframes.py
  multi-copy/  (1 files)
    multi-copy.py
  multi-example/  (1 files)
    mult-values.py
  multidata-strategy/  (2 files)
    multidata-strategy-unaligned.py
    multidata-strategy.py
  multitrades/  (2 files)
    mtradeobserver.py
    multitrades.py
  oandatest/  (1 files)
    oandatest.py
  observer-benchmark/  (1 files)
    observer-benchmark.py
  observers/  (4 files)
    observers-default-drawdown.py
    observers-default.py
    observers-orderobserver.py
    orderobserver.py
  oco/  (1 files)
    oco.py
  optimization/  (1 files)
    optimization.py
  order-close/  (2 files)
    close-daily.py
    close-minute.py
  order-execution/  (1 files)
    order-execution.py
  order-history/  (1 files)
    order-history.py
  order_target/  (1 files)
    order_target.py
  partial-plot/  (1 files)
    partial-plot.py
  pinkfish-challenge/  (1 files)
    pinkfish-challenge.py
  pivot-point/  (2 files)
    pivotpoint.py
    ppsample.py
  plot-same-axis/  (1 files)
    plot-same-axis.py
  psar/  (2 files)
    psar-intraday.py
    psar.py
  pyfolio2/  (2 files)
    backtrader-pyfolio.ipynb
    pyfoliotest.py
  pyfoliotest/  (1 files)
    pyfoliotest.py
  relative-volume/  (2 files)
    relative-volume.py
    relvolbybar.py
  renko/  (1 files)
    renko.py
  resample-tickdata/  (1 files)
    resample-tickdata.py
  rollover/  (1 files)
    rollover.py
  sharpe-timereturn/  (1 files)
    sharpe-timereturn.py
  signals-strategy/  (1 files)
    signals-strategy.py
  sigsmacross/  (2 files)
    sigsmacross.py
    sigsmacross2.py
  sizertest/  (1 files)
    sizertest.py
  slippage/  (1 files)
    slippage.py
  sratio/  (1 files)
    sratio.py
  stop-trading/  (1 files)
    stop-loss-approaches.py
  stoptrail/  (1 files)
    trail.py
  strategy-selection/  (1 files)
    strategy-selection.py
  talib/  (2 files)
    tablibsartest.py
    talibtest.py
  timers/  (2 files)
    scheduled-min.py
    scheduled.py
  tradingcalendar/  (2 files)
    tcal-intra.py
    tcal.py
  vctest/  (1 files)
    vctest.py
  volumefilling/  (1 files)
    volumefilling.py
  vwr/  (1 files)
    vwr.py
  weekdays-filler/  (2 files)
    weekdaysaligner.py
    weekdaysfiller.py
  writer-test/  (1 files)
    writer-test.py
  yahoo-test/  (1 files)
    yahoo-test.py
tests/  (83 files)
  test_analyzer-sqn.py
  test_analyzer-timereturn.py
  test_comminfo.py
  test_data_multiframe.py
  test_data_replay.py
  test_data_resample.py
  test_ind_accdecosc.py
  test_ind_aroonoscillator.py
  test_ind_aroonupdown.py
  test_ind_atr.py
  test_ind_awesomeoscillator.py
  test_ind_bbands.py
  test_ind_cci.py
  test_ind_dema.py
  test_ind_demaenvelope.py
  test_ind_demaosc.py
  test_ind_dm.py
  test_ind_dma.py
  test_ind_downmove.py
  test_ind_dpo.py
  test_ind_dv2.py
  test_ind_ema.py
  test_ind_emaenvelope.py
  test_ind_emaosc.py
  … 59 more files
tools/  (3 files)
  bt-run.py
  rewrite-data.py
  yahoodownload.py
.gitignore
.travis.yml
LICENSE
README.rst
changelog.txt
pypi.sh
setup.py
```

## Entry points

- [backtrader/btrun/__init__.py](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/btrun/__init__.py)
- [backtrader/btrun/btrun.py:742](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/btrun/btrun.py#L742)
- [contrib/samples/pair-trading/pair-trading.py:261](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/contrib/samples/pair-trading/pair-trading.py#L261)
- [contrib/utils/influxdb-import.py:63](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/contrib/utils/influxdb-import.py#L63)
- [contrib/utils/iqfeed-to-influxdb.py:156](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/contrib/utils/iqfeed-to-influxdb.py#L156)
- [samples/analyzer-annualreturn/analyzer-annualreturn.py:240](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/samples/analyzer-annualreturn/analyzer-annualreturn.py#L240)
- [samples/bidask-to-ohlc/bidask-to-ohlc.py:88](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/samples/bidask-to-ohlc/bidask-to-ohlc.py#L88)
- [samples/bracket/bracket.py:198](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/samples/bracket/bracket.py#L198)
- [samples/btfd/btfd.py:232](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/samples/btfd/btfd.py#L232)
- [samples/calendar-days/calendar-days.py:129](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/samples/calendar-days/calendar-days.py#L129)
- [samples/calmar/calmar-test.py:120](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/samples/calmar/calmar-test.py#L120)
- [samples/cheat-on-open/cheat-on-open.py:153](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/samples/cheat-on-open/cheat-on-open.py#L153)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| backtrader package | library | Observed | Groups 170 file(s) under backtrader package (observed from repository paths and static analysis). Observed top-level classes: API, AbstractDataBase, AccelerationDecelerationOscillator, Accum, AdaptiveMovingAverage, All.… |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 84 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AutoStopOrStopTrail, BaseStrategy, BidAskCSV, BuySellArrows, CloseSMA, DayStepsCloseFilte… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| samples package | library | Observed | Groups 7 file(s) under samples package (observed from repository paths and static analysis). Observed top-level classes: MTradeObserver, OrderObserver, PivotPoint, PivotPoint1, RelativeVolume, RelativeVolumeByBar. |
| Tests | test | Observed | Groups 83 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeCommInfo, FakeData, SampleParamsHolder, TS2, TestFrompackages, TestStrategy. Observed top-level functio… |

## Important files

- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `setup.py` (manifest)

## Top-level layout

- `backtrader` — 171 analysed file(s)
- `samples` — 85 analysed file(s)
- `tests` — 83 analysed file(s)
- `datas` — 17 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `contrib` — 5 analysed file(s)
- `tools` — 3 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b853d7c90b6721476eb5a5ea3135224e33db1f14` is the revision these paths and observations refer to.
