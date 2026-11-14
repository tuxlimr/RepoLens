# Project structure: leeoniya/uPlot

**Analysed commit:** `6f32019905014d952f9f013a101efaac7182f5f8`

**Commit reference:** [6f32019905014d952f9f013a101efaac7182f5f8](https://github.com/leeoniya/uPlot/commit/6f32019905014d952f9f013a101efaac7182f5f8)

**Tree at this commit:** [leeoniya/uPlot@6f3201990501](https://github.com/leeoniya/uPlot/tree/6f32019905014d952f9f013a101efaac7182f5f8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | leeoniya/uPlot |
| Description | 📈 A small, fast chart for time series, lines, areas, ohlc & bars |
| Stars | 10639 |
| Forks | 471 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `6f32019905014d952f9f013a101efaac7182f5f8` |
| Retrieved at | 2026-11-14T19:12:36.058873+00:00 |
| Files in this snapshot | 788 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
bench/  (222 files)
  dashboard/  (102 files)
    README.md
    agcharts.html
    agcharts.mjs
    amcharts-sampled.html
    amcharts-sampled.mjs
    amcharts.html
    amcharts.mjs
    anychart-sampled.html
    anychart-sampled.mjs
    anychart.html
    anychart.mjs
    apexcharts-sampled.html
    apexcharts-sampled.mjs
    apexcharts.html
    apexcharts.mjs
    billboard.html
    billboard.mjs
    bokeh-canvas.html
    bokeh-canvas.mjs
    bokeh.html
    bokeh.mjs
    browser.mjs
    canvasjs.html
    canvasjs.mjs
    … 78 more files
  AGCharts.html
  AnyChart-Sampled.html
  AnyChart.html
  ApexCharts-Sampled.html
  ApexCharts.html
  Billboard.html
  Bokeh-Canvas.html
  Bokeh.html
  CanvasJS.html
  Chart.js4-sine-stream.html
  Chart.js4.html
  ChartGPU.html
  D3-SVG.html
  D3-sine-stream.html
  D3.html
  DevExtreme-Sampled.html
  DevExtreme.html
  ECharts5-sine-stream.html
  ECharts5.html
  Flot.html
  FusionTime-Sampled.html
  FusionTime.html
  G2-WebGL.html
  G2.html
  … 96 more files
demos/  (196 files)
  data/  (15 files)
    AAPL.csv
    AMD.csv
    AMZN.csv
    CSCO.csv
    FB.csv
    MSFT.csv
    QCOM.csv
    SBUX.csv
    TSLA.csv
    ZNGA.csv
    log-scales.js
    rustc-perf.json
    sparse.json
    taxi-trips.json
    traffic.json
  issues/  (8 files)
    issue-1133-dynamic-backend-range.html
    issue-20-export-pxratio.html
    issue-648-auto-reset-vs-zoom.html
    issue-650-candidate-range.html
    issue-655-fixed-auto-false.html
    issue-808-static-range-scan.html
    issue-823-full-domain-scan.html
    issue-915-static-range-reset.html
  lib/  (26 files)
    ASAP-optimized.js
    ASAP-simple.js
    barChartPlugin.js
    barChartPlugin.md
    barControls.js
    barHover.js
    barTotals.js
    barValues.js
    d3CanvasAligned.js
    dbscan1d.js
    distr.js
    double-mad.js
    flatbush.LICENSE
    flatbush.js
    heatmapCellsData.js
    heatmapCellsData.md
    heatmapColorLut.js
    heatmapPlugin.js
    quadtree.js
    rand.js
    randomWalk.js
    scatterPlugin.js
    scatterPlugin.md
    sgg.js
    … 2 more files
  add-del-series.html
  align-data.html
  annotations.html
  annotations.js
  arcsinh-scales.html
  arcsinh-scales.js
  area-fill.html
  area-fill.js
  axis-autosize.html
  axis-control.html
  axis-control.js
  axis-indicators.html
  axis-label-rotation-chartjs.html
  axis-label-rotation-echarts.html
  axis-label-rotation.html
  axis-label-rotation.js
  axis-range-aligned.html
  axis-range-aligned.js
  axis-range-policies.html
  axis-range-policies.js
  bars-grouped-stacked.html
  bars-grouped-stacked.js
  bars-values-autosize.html
  box-whisker.html
  … 123 more files
docs/  (67 files)
  investigations/  (61 files)
    adaptive-asinh-scan-simplification.md
    band-rendering-performance.md
    band-scale-plan.md
    bar-chart-demo-recommendations.md
    benchmark-d3-memory-rerun-results.json
    benchmark-d3-memory-rerun.md
    benchmark-d3-memory-rerun.mjs
    benchmark-d3-residual-memory.md
    benchmark-d3-residual-probe.mjs
    benchmark-d3-residual-rerun.mjs
    benchmark-d3-retention-probe.mjs
    benchmark-d3-retention-results.json
    benchmark-d3-retention.md
    benchmark-d3-shared-probe.mjs
    benchmark-gc-cold-warm.md
    benchmark-library-expansion.md
    benchmark-update-references.md
    coverage-gaps.md
    disp-core-capabilities-review.md
    disp-semantics-plan.md
    drag-range-refinement.md
    faceted-mode-migration.md
    grafana-bar-chart-replacement-results.json
    grafana-bar-chart-replacement.md
    … 37 more files
  README.md
  data-modes.md
  legend-dom-prototype.md
  manual-profile.md
  paths-disp.md
  tooltip.md
scripts/  (63 files)
  analyze-benchmarks-process-memory.mjs
  analyze-benchmarks-raf.mjs
  analyze-benchmarks-trace.mjs
  audit-grafana-scales.mjs
  bench-asinh-scan.mjs
  bench-axis-overflow.mjs
  bench-browser-process.mjs
  bench-canvas-sprites.mjs
  bench-demo-sources.mjs
  bench-fixed-dec.mjs
  bench-heatmap-asinh.mjs
  bench-heatmap-color-blocks.mjs
  bench-heatmap-color-precompute.mjs
  bench-heatmap-grid-browser.mjs
  bench-heatmap-grid.mjs
  bench-heatmap-log-blocks.mjs
  bench-heatmap-lookup.mjs
  bench-heatmap-minmax.mjs
  bench-hover-browser.mjs
  bench-hover.mjs
  bench-instrument.mjs
  bench-join.mjs
  bench-legend-browser.js
  bench-legend.mjs
  … 39 more files
src/  (26 files)
  paths/  (9 files)
    bars.js
    catmullRomCentrip.js
    disp.js
    linear.js
    monotoneCubic.js
    points.js
    spline.js
    stepped.js
    utils.js
  axis.js
  dom.js
  domClasses.js
  feats.js
  fmtDate.js
  h.js
  keyed-list.js
  legend-dom-template.js
  legend-dom.js
  opts.js
  rangeY.js
  strings.js
  sync.js
  tooltip.js
  uPlot.css
  uPlot.js
  utils.js
test/  (204 files)
  demos/  (180 files)
    annotations/  (1 files)
      … 1 files under this directory
    arcsinh-scales/  (2 files)
      … 2 files under this directory
    area-fill/  (1 files)
      … 1 files under this directory
    axis-control/  (3 files)
      … 3 files under this directory
    bars-grouped-stacked/  (10 files)
      … 10 files under this directory
    box-whisker/  (17 files)
      … 17 files under this directory
    candlestick-ohlc/  (1 files)
      … 1 files under this directory
    custom-scales/  (3 files)
      … 3 files under this directory
    decimation/  (3 files)
      … 3 files under this directory
    dependent-scale/  (1 files)
      … 1 files under this directory
    gradients/  (5 files)
      … 5 files under this directory
    grid-over-series/  (1 files)
      … 1 files under this directory
    high-low-bands/  (13 files)
      … 13 files under this directory
    line-paths/  (8 files)
      … 8 files under this directory
    log-scales2/  (12 files)
      … 12 files under this directory
    missing-data/  (2 files)
      … 2 files under this directory
    months/  (2 files)
      … 2 files under this directory
    months-ru/  (1 files)
      … 1 files under this directory
    multi-bars/  (4 files)
      … 4 files under this directory
    nearest-non-null/  (5 files)
      … 5 files under this directory
    no-data/  (35 files)
      … 35 files under this directory
    path-gap-clip/  (17 files)
      … 17 files under this directory
    points/  (4 files)
      … 4 files under this directory
    scale-padding/  (1 files)
      … 1 files under this directory
    scales-dir-ori/  (16 files)
      … 16 files under this directory
    soft-minmax/  (8 files)
      … 8 files under this directory
    sparklines-bars/  (2 files)
      … 2 files under this directory
    stacked-series/  (2 files)
      … 2 files under this directory
  integration/  (1 files)
    demo-steps.mjs
  plugins/  (1 files)
    test.mjs
  README.md
  asinh-scan-utils.mjs
  asinh-scan.mjs
  asinh.mjs
  axis-autosize.mjs
  axis-range-demo.mjs
  axis-range-policy-demo.mjs
  axis-value-precision.mjs
  band-drawing.mjs
  bar-gap.mjs
  bar-radii.mjs
  cache.mjs
  context-attributes.mjs
  cursor-drag.mjs
  cursor-focus.mjs
  cursor-points.mjs
  data-cache.mjs
  dbscan1d.mjs
  decimation.mjs
  demo-extractions.mjs
  demo-migrations.mjs
  demos.mjs
.editorconfig
.gitignore
LICENSE
README.md
bun.lock
bunfig.toml
jsconfig.json
package.json
rolldown.config.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| axis.js package | library | Observed | Groups 1 file(s) under axis.js package (observed from repository paths and static analysis). |
| bench package | library | Observed | Groups 115 file(s) under bench package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 75 file(s) under demos package (observed from repository paths and static analysis). |
| dom.js package | library | Observed | Groups 1 file(s) under dom.js package (observed from repository paths and static analysis). |
| domClasses.js package | library | Observed | Groups 1 file(s) under domclasses.js package (observed from repository paths and static analysis). |
| feats.js package | library | Observed | Groups 1 file(s) under feats.js package (observed from repository paths and static analysis). |
| fmtDate.js package | library | Observed | Groups 1 file(s) under fmtdate.js package (observed from repository paths and static analysis). |
| h.js package | library | Observed | Groups 1 file(s) under h.js package (observed from repository paths and static analysis). |
| keyed-list.js package | library | Observed | Groups 1 file(s) under keyed-list.js package (observed from repository paths and static analysis). |
| legend-dom.js package | library | Observed | Groups 1 file(s) under legend-dom.js package (observed from repository paths and static analysis). |
| legend-dom-template.js package | library | Observed | Groups 1 file(s) under legend-dom-template.js package (observed from repository paths and static analysis). |
| opts.js package | library | Observed | Groups 1 file(s) under opts.js package (observed from repository paths and static analysis). |
| paths package | library | Observed | Groups 9 file(s) under paths package (observed from repository paths and static analysis). |
| rangeY.js package | library | Observed | Groups 1 file(s) under rangey.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 62 file(s) under scripts package (observed from repository paths and static analysis). |
| strings.js package | library | Observed | Groups 1 file(s) under strings.js package (observed from repository paths and static analysis). |
| sync.js package | library | Observed | Groups 1 file(s) under sync.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 204 file(s) under tests (observed from repository paths and static analysis). |
| tooltip.js package | library | Observed | Groups 1 file(s) under tooltip.js package (observed from repository paths and static analysis). |
| uPlot.js package | library | Observed | Groups 1 file(s) under uplot.js package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `bench/results.json` (config)
- `bunfig.toml` (config)
- `demos/data/rustc-perf.json` (config)
- `demos/data/sparse.json` (config)
- `demos/data/taxi-trips.json` (config)
- `demos/data/traffic.json` (config)
- `docs/investigations/benchmark-d3-memory-rerun-results.json` (config)
- `docs/investigations/benchmark-d3-retention-results.json` (config)
- `docs/investigations/grafana-bar-chart-replacement-results.json` (config)
- `docs/investigations/grafana-bar-chart-size-results.json` (config)
- `docs/investigations/number-format-decimal-results.json` (config)
- `docs/investigations/number-format-iteration-results.json` (config)
- `docs/investigations/number-format-results.json` (config)
- `docs/investigations/number-format-structural-results.json` (config)
- `docs/investigations/sine-stream-bundle-size-results.json` (config)
- `jsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `bench` — 222 analysed file(s)
- `test` — 204 analysed file(s)
- `demos` — 196 analysed file(s)
- `docs` — 67 analysed file(s)
- `scripts` — 63 analysed file(s)
- `src` — 26 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 11 file(s) were skipped during inventory (1 x lockfile excluded; 10 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6f32019905014d952f9f013a101efaac7182f5f8` is the revision these paths and observations refer to.
