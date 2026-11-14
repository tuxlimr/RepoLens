# Project structure: askmike/gekko

**Analysed commit:** `ff5698f1ae6329bab5729f145c35a74161e82bac`

**Commit reference:** [ff5698f1ae6329bab5729f145c35a74161e82bac](https://github.com/askmike/gekko/commit/ff5698f1ae6329bab5729f145c35a74161e82bac)

**Tree at this commit:** [askmike/gekko@ff5698f1ae63](https://github.com/askmike/gekko/tree/ff5698f1ae6329bab5729f145c35a74161e82bac)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | askmike/gekko |
| Description | A bitcoin trading bot written in node - https://gekko.wizb.it/ |
| Stars | 10177 |
| Forks | 3755 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `ff5698f1ae6329bab5729f145c35a74161e82bac` |
| Retrieved at | 2026-11-14T19:12:43.841578+00:00 |
| Files in this snapshot | 358 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  stale.yml
config/  (26 files)
  adapters/  (3 files)
    mongodb.toml
    postgresql.toml
    sqlite.toml
  plugins/  (6 files)
    candleWriter.toml
    paperTrader.toml
    performanceAnalyzer.toml
    pushbullet.toml
    trader.toml
    tradingAdvisor.toml
  strategies/  (15 files)
    CCI.toml
    DEMA.toml
    MACD.toml
    PPO.toml
    RSI.toml
    StochRSI.toml
    TMA.toml
    TSI.toml
    UO.toml
    custom.toml
    talib-macd.toml
    tulip-adx.toml
    tulip-macd.toml
    tulip-multi-strat.toml
    varPPO.toml
  backtest.toml
  general.toml
core/  (36 files)
  budfox/  (7 files)
    budfox.js
    candleCreator.js
    candleManager.js
    heart.js
    marketDataProvider.js
    marketFetcher.js
    tradeBatcher.js
  markets/  (4 files)
    backtest.js
    importer.js
    leech.js
    realtime.js
  tools/  (4 files)
    candleLoader.js
    configBuilder.js
    dataStitcher.js
    dateRangeScanner.js
  workers/  (10 files)
    datasetScan/  (1 files)
      … 1 files under this directory
    dateRangeScan/  (2 files)
      … 2 files under this directory
    loadCandles/  (2 files)
      … 2 files under this directory
    pipeline/  (5 files)
      … 5 files under this directory
  candleBatcher.js
  emitter.js
  gekkoStream.js
  log.js
  pipeline.js
  pluginUtil.js
  prepareDateRange.js
  stats.js
  talib.js
  tulind.js
  util.js
docs/  (39 files)
  commandline/  (5 files)
    Importing.md
    about_the_commandline.md
    backtesting.md
    plugins.md
    tradebot.md
  extending/  (3 files)
    add_a_plugin.md
    add_an_exchange.md
    other_software.md
  features/  (4 files)
    backtesting.md
    importing.md
    paper_trading.md
    trading_bot.md
  gekko-broker/  (3 files)
    introduction.md
    sticky_order.md
    wrapper_api.md
  installation/  (7 files)
    configuring_gekko_on_a_server.md
    installing_gekko.md
    installing_gekko_on_raspberry_pi_2_or_3.md
    installing_gekko_on_windows.md
    installing_gekko_on_windows_with_bash_on_windows_10.md
    installing_gekko_using_docker.md
    updating_gekko.md
  internals/  (6 files)
    architecture.md
    budfox.md
    events.md
    gekko_ui.md
    plugins.md
    server_api.md
  introduction/  (6 files)
    about_gekko.md
    getting_help.md
    roadmap.md
    scope.md
    supported_exchanges.md
    supporting_the_project.md
  strategies/  (5 files)
    creating_a_strategy.md
    gekko_indicators.md
    introduction.md
    talib_indicators.md
    tulip_indicators.md
exchange/  (58 files)
  orders/  (5 files)
    index.js
    limit.js
    order.js
    states.js
    sticky.js
  triggers/  (2 files)
    index.js
    trailingStop.js
  util/  (5 files)
    genMarketFiles/  (5 files)
      … 5 files under this directory
  wrappers/  (36 files)
    DEBUG_exchange-simulator.js
    binance-markets.json
    binance.js
    bitcoin-co-id.js.old
    bitfinex-markets.json
    bitfinex.js
    bitfinex_v2.js.prep
    bitstamp.js.old
    bittrex.js
    btc-markets.js.old
    btcc.js.old
    bx.in.th.js.old
    cexio.js.old
    coinbase-markets.json
    coinfalcon-markets.json
    coinfalcon.js
    coingi.js
    exmo-markets.json
    exmo.js
    gdax.js
    gemini.js.old
    kraken-markets.json
    kraken.js
    lakebtc.js
    … 12 more files
  .npmignore
  README.md
  dependencyCheck.js
  exchangeChecker.js
  exchangeErrors.js
  exchangeUtils.js
  gekkoBroker.js
  package.json
  portfolioManager.js
  trigger.js
importers/  (9 files)
  exchanges/  (9 files)
    binance.js
    bitfinex.js
    btcc.js
    coinfalcon.js
    gdax.js
    kraken.js
    luno.js
    poloniex.js
    therocktrading.js
logs/  (1 files)
  .gitignore
plugins/  (41 files)
  mongodb/  (5 files)
    handle.js
    reader.js
    scanner.js
    util.js
    writer.js
  paperTrader/  (1 files)
    paperTrader.js
  performanceAnalyzer/  (2 files)
    logger.js
    performanceAnalyzer.js
  postgresql/  (5 files)
    handle.js
    reader.js
    scanner.js
    util.js
    writer.js
  sqlite/  (5 files)
    handle.js
    reader.js
    scanner.js
    util.js
    writer.js
  trader/  (1 files)
    trader.js
  tradingAdvisor/  (3 files)
    asyncIndicatorRunner.js
    baseTradingMethod.js
    tradingAdvisor.js
  adviceLogger.js
  backtestResultExporter.js
  blotter.js
  campfire.js
  candleUploader.js
  childToParent.js
  eventLogger.js
  ifttt.js
  ircbot.js
  kodi.js
  mailer.js
  pushbullet.js
  pushover.js
  redisBeacon.js
  slack.js
  telegrambot.js
  twitter.js
  webserver.js
  xmppbot.js
strategies/  (29 files)
  indicators/  (11 files)
    CCI.js
    DEMA.js
    EMA.js
    LRC.js
    MACD.js
    PPO.js
    RSI.js
    SMA.js
    SMMA.js
    TSI.js
    UO.js
  CCI.js
  DEBUG_single-advice.js
  DEBUG_toggle-advice.js
  DEMA.js
  MACD.js
  PPO.js
  RSI.js
  StochRSI.js
  TMA.js
  TSI.js
  UO.js
  custom.js
  noop.js
  talib-macd.js
  tulip-adx.js
  tulip-macd.js
  tulip-multi-strat.js
  varPPO.js
test/  (17 files)
  exchanges/  (2 files)
    data/  (1 files)
      … 1 files under this directory
    bitstamp.js
  indicators/  (8 files)
    cci.js
    dema.js
    ema.js
    macd.js
    ppo.js
    rsi.js
    sma.js
    smma.js
  plugins/  (1 files)
    portfolioManager.js
  triggers/  (1 files)
    trailingStop.js
  _prepare.js
  candleBatcher.js
  marketFetcher.js
  test-config.json
  tradeBatcher.js
web/  (82 files)
  routes/  (15 files)
    apiKeys.js
    backtest.js
    baseConfig.js
    configPart.js
    deleteGekko.js
    exchanges.js
    getCandles.js
    import.js
    info.js
    list.js
    scanDatasets.js
    scanDateRange.js
    startGekko.js
    stopGekko.js
    strategies.js
  state/  (5 files)
    cache.js
    gekkoManager.js
    listManager.js
    logger.js
    reduceState.js
  vue/  (58 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (53 files)
      … 53 files under this directory
    babel.config.js
    package.json
    vue.config.js
  apiKeyManager.js
  baseUIconfig.js
  isWindows.js
  server.js
.dockerignore
.editorconfig
.gitignore
.prettierrc
.travis.yml
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
appveyor.yml
docker-compose.yml
docker-entrypoint.sh
gekko.js
package.json
plugins.js
sample-config.js
subscriptions.js
```

## Entry points

- [exchange/gekkoBroker.js](https://github.com/askmike/gekko/blob/ff5698f1ae6329bab5729f145c35a74161e82bac/exchange/gekkoBroker.js)
- [exchange/orders/index.js](https://github.com/askmike/gekko/blob/ff5698f1ae6329bab5729f145c35a74161e82bac/exchange/orders/index.js)
- [exchange/triggers/index.js](https://github.com/askmike/gekko/blob/ff5698f1ae6329bab5729f145c35a74161e82bac/exchange/triggers/index.js)
- [web/server.js](https://github.com/askmike/gekko/blob/ff5698f1ae6329bab5729f145c35a74161e82bac/web/server.js)
- [web/vue/src/main.js](https://github.com/askmike/gekko/blob/ff5698f1ae6329bab5729f145c35a74161e82bac/web/vue/src/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 15 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 45 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). |
| exchange package | library | Observed | Groups 32 file(s) under exchange package (observed from repository paths and static analysis). |
| importers package | library | Observed | Groups 9 file(s) under importers package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 41 file(s) under plugins package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 36 file(s) under service / domain layer (observed from repository paths and static analysis). |
| strategies package | library | Observed | Groups 29 file(s) under strategies package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). |
| web package | library | Observed | Groups 57 file(s) under web package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/stale.yml` (config)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `appveyor.yml` (config)
- `config/adapters/mongodb.toml` (config)
- `config/adapters/postgresql.toml` (config)
- `config/adapters/sqlite.toml` (config)
- `config/backtest.toml` (config)
- `config/general.toml` (config)
- `config/plugins/candleWriter.toml` (config)
- `config/plugins/paperTrader.toml` (config)
- `config/plugins/performanceAnalyzer.toml` (config)
- `config/plugins/pushbullet.toml` (config)
- `config/plugins/trader.toml` (config)
- `config/plugins/tradingAdvisor.toml` (config)
- `config/strategies/CCI.toml` (config)
- `config/strategies/DEMA.toml` (config)
- `config/strategies/MACD.toml` (config)
- `config/strategies/PPO.toml` (config)
- `config/strategies/RSI.toml` (config)
- `config/strategies/StochRSI.toml` (config)
- `config/strategies/TMA.toml` (config)
- `config/strategies/TSI.toml` (config)
- `config/strategies/UO.toml` (config)
- `config/strategies/custom.toml` (config)
- `config/strategies/talib-macd.toml` (config)
- `config/strategies/tulip-adx.toml` (config)
- `config/strategies/tulip-macd.toml` (config)
- `config/strategies/tulip-multi-strat.toml` (config)
- `config/strategies/varPPO.toml` (config)
- `docker-compose.yml` (container)
- `exchange/package.json` (manifest)
- `exchange/wrappers/binance-markets.json` (config)
- `exchange/wrappers/bitfinex-markets.json` (config)
- `exchange/wrappers/coinbase-markets.json` (config)
- `exchange/wrappers/coinfalcon-markets.json` (config)
- `exchange/wrappers/exmo-markets.json` (config)
- `exchange/wrappers/kraken-markets.json` (config)
- `exchange/wrappers/poloniex-markets.json` (config)
- `exchange/wrappers/quadriga-markets.json` (config)
- `exchange/wrappers/therocktrading-markets.json` (config)
- `package.json` (manifest)
- `web/vue/package.json` (manifest)

## Top-level layout

- `web` — 82 analysed file(s)
- `exchange` — 58 analysed file(s)
- `plugins` — 41 analysed file(s)
- `docs` — 39 analysed file(s)
- `core` — 36 analysed file(s)
- `strategies` — 29 analysed file(s)
- `config` — 26 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `test` — 17 analysed file(s)
- `importers` — 9 analysed file(s)
- `.github` — 3 analysed file(s)
- `logs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 15 file(s) were skipped during inventory (1 x likely secret file excluded; 2 x lockfile excluded; 12 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `ff5698f1ae6329bab5729f145c35a74161e82bac` is the revision these paths and observations refer to.
