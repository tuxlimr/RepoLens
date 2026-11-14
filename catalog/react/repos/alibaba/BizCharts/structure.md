# Project structure: alibaba/BizCharts

**Analysed commit:** `0be043c2fe36dd1ef56fa252e7a075a0a31115b5`

**Commit reference:** [0be043c2fe36dd1ef56fa252e7a075a0a31115b5](https://github.com/alibaba/BizCharts/commit/0be043c2fe36dd1ef56fa252e7a075a0a31115b5)

**Tree at this commit:** [alibaba/BizCharts@0be043c2fe36](https://github.com/alibaba/BizCharts/tree/0be043c2fe36dd1ef56fa252e7a075a0a31115b5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alibaba/BizCharts |
| Description | Powerful data visualization library based on G2 and React. |
| Stars | 6181 |
| Forks | 657 |
| Licence | Not detected |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `0be043c2fe36dd1ef56fa252e7a075a0a31115b5` |
| Retrieved at | 2026-11-14T19:14:09.246840+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE.md
.storybook/  (4 files)
  .eslintrc
  main.js
  preview.js
  webpack.config.js
__stories__/  (21 files)
  plots/  (1 files)
    area.stories.tsx
  area.stories.tsx
  base.stories.tsx
  box.stories.tsx
  bugs.stories.tsx
  candle.stories.tsx
  dashboard.stories.tsx
  feature.stories.tsx
  funnel.stories.tsx
  g.stories.tsx
  geometry.stories.tsx
  heatMap.stories.tsx
  interval.stories.tsx
  line.stories.tsx
  path.stories.tsx
  pie.stories.tsx
  plot.stories.tsx
  point.stories.tsx
  radar.stories.tsx
  temp.stories.tsx
  theme.stories.tsx
demos/  (83 files)
  adepter/  (2 files)
    coord.jsx
    geom-label.jsx
  area/  (7 files)
    areaWithNull.jsx
    basicArea.jsx
    basicAreaWithNegativeValues.jsx
    colorBlock.jsx
    intervalArea.jsx
    percentStackingArea.jsx
    stackingArea.jsx
  box/  (1 files)
    basicBox.jsx
  bugs/  (2 files)
    plot-bar.jsx
    view-changeData.jsx
  candle/  (2 files)
    data.js
    stock.jsx
  components/  (7 files)
    annotation-text.js
    annotation.jsx
    autoFit.jsx
    axis.jsx
    coordinate.jsx
    facet.jsx
    view.jsx
  dashboard/  (1 files)
    basicDashboard.jsx
  external/  (1 files)
    index.html
  features/  (14 files)
    JsxTooltip.jsx
    changeData.jsx
    chartManager.jsx
    effects.jsx
    facet.jsx
    fiber-reconciler.jsx
    filter.jsx
    interaction.jsx
    pure.jsx
    resize.jsx
    selected.jsx
    slider.jsx
    tooltip-linkage.jsx
    transform.jsx
  funnel/  (1 files)
    basicFunnel.jsx
  g-components/  (1 files)
    basic.tsx
  geom/  (6 files)
    LineAdvance.jsx
    area.jsx
    interval-group.jsx
    interval.jsx
    line.jsx
    path.jsx
  heatMap/  (2 files)
    calendar.jsx
    heatMap.jsx
  interval/  (16 files)
    basicBar.tsx
    basicColumn.jsx
    bezier.jsx
    colorGroupedStackedColumns.jsx
    comparedBar.jsx
    gradientBar.jsx
    groupedBar.jsx
    groupedColumns.jsx
    groupedStackedColumns.jsx
    histogram.jsx
    intervalColumn.jsx
    percentStackedColumn.jsx
    polarCoordinate.jsx
    roundedColumn.jsx
    stackedBars.jsx
    stackedColumn.jsx
  line/  (4 files)
    gradientPolyline.jsx
    ordinaryCurve.jsx
    ordinaryPolyline.jsx
    stepPolyline.jsx
  pie/  (7 files)
    RoseChart-limitedAngleRange.jsx
    basicPie.jsx
    multicolorNightingaleRoseillustration.jsx
    nestedPie.jsx
    nightingaleRoseIllustration.jsx
    nightingaleRosette.jsx
    visualizationOfDailyWork.jsx
  plot/  (4 files)
    gauge.jsx
    line.jsx
    plots.jsx
    ring.jsx
  point/  (3 files)
    basicPoint.jsx
    bubble.jsx
    multiShapeScatter.jsx
  radar/  (1 files)
    radar.jsx
  theme/  (1 files)
    index.jsx
docs/  (530 files)
  BizCharts/  (252 files)
    API文档/  (21 files)
      … 21 files under this directory
    Demo/  (214 files)
      … 214 files under this directory
    使用指南/  (15 files)
      … 15 files under this directory
    实战/  (2 files)
      … 2 files under this directory
  BizCharts@4.x/  (246 files)
    API文档/  (37 files)
      … 37 files under this directory
    Demo/  (161 files)
      … 161 files under this directory
    Plots/  (34 files)
      … 34 files under this directory
    使用指南/  (14 files)
      … 14 files under this directory
  BizGoblin/  (30 files)
    API文档/  (7 files)
      … 7 files under this directory
    Demo/  (20 files)
      … 20 files under this directory
    使用指南/  (3 files)
      … 3 files under this directory
  常见问题/  (1 files)
    faq.md
  category_list.json
src/  (149 files)
  adapter/  (2 files)
    Guide.tsx
    paddingCheck.ts
  boundary/  (2 files)
    ErrorBoundary.tsx
    withContainer.tsx
  components/  (33 files)
    Annotation/  (13 files)
      … 13 files under this directory
    Axis/  (1 files)
      … 1 files under this directory
    Chart/  (3 files)
      … 3 files under this directory
    Coordinate/  (2 files)
      … 2 files under this directory
    Effects/  (1 files)
      … 1 files under this directory
    Facet/  (1 files)
      … 1 files under this directory
    Interaction/  (2 files)
      … 2 files under this directory
    Legend/  (2 files)
      … 2 files under this directory
    Slider/  (1 files)
      … 1 files under this directory
    Tooltip/  (5 files)
      … 5 files under this directory
    View/  (2 files)
      … 2 files under this directory
  connector/  (1 files)
    createTooltipConnector.ts
  context/  (4 files)
    canvas.tsx
    group.tsx
    root.tsx
    view.tsx
  extend/  (2 files)
    scale/  (2 files)
      … 2 files under this directory
  g-components/  (17 files)
    Base/  (3 files)
      … 3 files under this directory
    reconciler/  (1 files)
      … 1 files under this directory
    Canvas.tsx
    Circle.tsx
    Ellipse.tsx
    Group.tsx
    Image.tsx
    Line.tsx
    Marker.tsx
    Path.tsx
    Polygon.tsx
    Polyline.tsx
    Rect.tsx
    Text.tsx
    index.ts
  geometry/  (14 files)
    Area.tsx
    Base.tsx
    Edge.tsx
    Heatmap.tsx
    Interval.tsx
    Label.tsx
    Line.tsx
    LineAdvance.tsx
    Path.tsx
    Point.tsx
    Polygon.tsx
    Schema.tsx
    actions.ts
    index.tsx
  hooks/  (3 files)
    useChartInstance.tsx
    useChartView.tsx
    useTheme.ts
  plots/  (47 files)
    core/  (3 files)
      … 3 files under this directory
    AreaChart.tsx
    BarChart.tsx
    BubbleChart.tsx
    BulletChart.tsx
    CalendarChart.tsx
    ColumnChart.tsx
    DensityHeatmapChart.tsx
    DonutChart.tsx
    DualAxesChart.tsx
    FunnelChart.tsx
    GaugeChart.tsx
    GroupedBarChart.tsx
    GroupedColumnChart.tsx
    GroupedRoseChart.tsx
    HeatmapChart.tsx
    HistogramChart.tsx
    LineChart.tsx
    LiquidChart.tsx
    PercentStackedAreaChart.tsx
    PercentStackedBarChart.tsx
    PercentStackedColumnChart.tsx
    PieChart.tsx
    PlotAdapter.tsx
    ProgressChart.tsx
    … 20 more files
  theme/  (1 files)
    index.tsx
  utils/  (16 files)
    data-transform/  (7 files)
      … 7 files under this directory
    cloneDeep.ts
    compareProps.ts
    constant.ts
    getElementSize.ts
    index.ts
    isEqual.ts
    pickWithout.ts
    plotTools.ts
    shallowEqual.ts
  animations.ts
  core.ts
  createPlot.tsx
  g2-all.ts
  global.d.ts
  index.tsx
  interface.ts
.babelrc
.eslintignore
.eslintrc.js
.fatherrc.js
.gitignore
.prettierrc.js
CHANGELOG.md
README.md
SECURITY.md
gulpfile.js
manifest.json
package.json
```

## Entry points

- [.storybook/main.js](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/.storybook/main.js)
- [demos/theme/index.jsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/demos/theme/index.jsx)
- [src/components/Annotation/index.tsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/src/components/Annotation/index.tsx)
- [src/components/Axis/index.tsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/src/components/Axis/index.tsx)
- [src/components/Chart/index.tsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/src/components/Chart/index.tsx)
- [src/components/Coordinate/index.tsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/src/components/Coordinate/index.tsx)
- [src/components/Effects/index.tsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/src/components/Effects/index.tsx)
- [src/components/Facet/index.tsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/src/components/Facet/index.tsx)
- [src/components/Interaction/index.tsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/src/components/Interaction/index.tsx)
- [src/components/Legend/index.tsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/src/components/Legend/index.tsx)
- [src/components/Slider/index.tsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/src/components/Slider/index.tsx)
- [src/components/Tooltip/index.tsx](https://github.com/alibaba/BizCharts/blob/0be043c2fe36dd1ef56fa252e7a075a0a31115b5/src/components/Tooltip/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| adapter package | library | Observed | Groups 2 file(s) under adapter package (observed from repository paths and static analysis). |
| animations.ts package | library | Observed | Groups 1 file(s) under animations.ts package (observed from repository paths and static analysis). |
| boundary package | library | Observed | Groups 2 file(s) under boundary package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 32 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| connector package | library | Observed | Groups 1 file(s) under connector package (observed from repository paths and static analysis). |
| context package | library | Observed | Groups 4 file(s) under context package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| core.ts package | library | Observed | Groups 1 file(s) under core.ts package (observed from repository paths and static analysis). |
| createPlot.tsx package | library | Observed | Groups 1 file(s) under createplot.tsx package (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 82 file(s) under demos package (observed from repository paths and static analysis). |
| extend package | library | Observed | Groups 2 file(s) under extend package (observed from repository paths and static analysis). |
| g2-all.ts package | library | Observed | Groups 1 file(s) under g2-all.ts package (observed from repository paths and static analysis). |
| g-components package | library | Observed | Groups 17 file(s) under g-components package (observed from repository paths and static analysis). |
| geometry package | library | Observed | Groups 14 file(s) under geometry package (observed from repository paths and static analysis). |
| global.d.ts package | library | Observed | Groups 1 file(s) under global.d.ts package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 3 file(s) under hooks package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| interface.ts package | library | Observed | Groups 1 file(s) under interface.ts package (observed from repository paths and static analysis). |
| plots package | library | Observed | Groups 44 file(s) under plots package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 3 file(s) under service / domain layer (observed from repository paths and static analysis). |
| __stories__ package | library | Observed | Groups 21 file(s) under __stories__ package (observed from repository paths and static analysis). |
| theme package | library | Observed | Groups 1 file(s) under theme package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 16 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `docs/BizCharts/API文档/data.json` (config)
- `docs/BizCharts/使用指南/data.json` (config)
- `docs/BizCharts/实战/data.json` (config)
- `docs/BizCharts@4.x/使用指南/data.json` (config)
- `docs/category_list.json` (config)
- `manifest.json` (config)
- `package.json` (manifest)

## Top-level layout

- `docs` — 530 analysed file(s)
- `src` — 149 analysed file(s)
- `demos` — 83 analysed file(s)
- `__stories__` — 21 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.storybook` — 4 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0be043c2fe36dd1ef56fa252e7a075a0a31115b5` is the revision these paths and observations refer to.
