# Project structure: chartjs/Chart.js

**Analysed commit:** `71d44219e79e3ac41e6f9dc907022eebf574868d`

**Commit reference:** [71d44219e79e3ac41e6f9dc907022eebf574868d](https://github.com/chartjs/Chart.js/commit/71d44219e79e3ac41e6f9dc907022eebf574868d)

**Tree at this commit:** [chartjs/Chart.js@71d44219e79e](https://github.com/chartjs/Chart.js/tree/71d44219e79e3ac41e6f9dc907022eebf574868d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chartjs/Chart.js |
| Description | Simple HTML5 Charts using the <canvas> tag |
| Stars | 67793 |
| Forks | 11970 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `71d44219e79e3ac41e6f9dc907022eebf574868d` |
| Retrieved at | 2026-11-14T19:10:35.467987+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (13 files)
  ISSUE_TEMPLATE/  (4 files)
    bug.yml
    config.yml
    docs.yml
    feature.yml
  workflows/  (5 files)
    ci.yml
    compressed-size.yml
    deploy-docs.yml
    release-drafter.yml
    release.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  release-drafter.yml
auto/  (4 files)
  auto.cjs
  auto.d.ts
  auto.js
  package.json
docs/  (152 files)
  .vuepress/  (4 files)
    public/  (1 files)
      … 1 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    config.ts
    redirects
  axes/  (15 files)
    cartesian/  (8 files)
      … 8 files under this directory
    radial/  (2 files)
      … 2 files under this directory
    _common.md
    _common_ticks.md
    index.md
    labelling.md
    styling.md
  charts/  (9 files)
    area.md
    bar.md
    bubble.md
    doughnut.md
    line.md
    mixed.md
    polar.md
    radar.md
    scatter.md
  configuration/  (14 files)
    animations.md
    canvas-background.md
    decimation.md
    device-pixel-ratio.md
    elements.md
    index.md
    interactions.md
    layout.md
    legend.md
    locale.md
    responsive.md
    subtitle.md
    title.md
    tooltip.md
  developers/  (9 files)
    api.md
    axes.md
    charts.md
    contributing.md
    index.md
    plugin_flowcharts.drawio
    plugins.md
    publishing.md
    updates.md
  general/  (7 files)
    accessibility.md
    colors.md
    data-structures.md
    fonts.md
    options.md
    padding.md
    performance.md
  getting-started/  (5 files)
    index.md
    installation.md
    integration.md
    usage.md
    using-from-node-js.md
  migration/  (2 files)
    v3-migration.md
    v4-migration.md
  samples/  (78 files)
    advanced/  (7 files)
      … 7 files under this directory
    animations/  (5 files)
      … 5 files under this directory
    area/  (5 files)
      … 5 files under this directory
    bar/  (6 files)
      … 6 files under this directory
    legend/  (5 files)
      … 5 files under this directory
    line/  (7 files)
      … 7 files under this directory
    other-charts/  (12 files)
      … 12 files under this directory
    plugins/  (3 files)
      … 3 files under this directory
    scale-options/  (4 files)
      … 4 files under this directory
    scales/  (8 files)
      … 8 files under this directory
    scriptable/  (6 files)
      … 6 files under this directory
    subtitle/  (1 files)
      … 1 files under this directory
    title/  (1 files)
      … 1 files under this directory
    tooltip/  (5 files)
      … 5 files under this directory
    .eslintrc.yml
    information.md
    utils.md
  scripts/  (7 files)
    analyzer.js
    components.js
    derived-bubble.js
    helpers.js
    log2.js
    register.js
    utils.js
  index.md
  package.json
helpers/  (4 files)
  helpers.cjs
  helpers.d.ts
  helpers.js
  package.json
scripts/  (5 files)
  deploy-docs.sh
  docs-config.sh
  publish.sh
  sample-redirect-template.html
  utils.sh
src/  (90 files)
  controllers/  (9 files)
    controller.bar.js
    controller.bubble.js
    controller.doughnut.js
    controller.line.js
    controller.pie.js
    controller.polarArea.js
    controller.radar.js
    controller.scatter.js
    index.js
  core/  (21 files)
    core.adapters.ts
    core.animation.js
    core.animations.defaults.js
    core.animations.js
    core.animator.js
    core.config.js
    core.controller.js
    core.datasetController.js
    core.defaults.js
    core.element.ts
    core.interaction.js
    core.layouts.defaults.js
    core.layouts.js
    core.plugins.js
    core.registry.js
    core.scale.autoskip.js
    core.scale.defaults.js
    core.scale.js
    core.ticks.js
    core.typedRegistry.js
    index.ts
  elements/  (5 files)
    element.arc.ts
    element.bar.js
    element.line.js
    element.point.ts
    index.js
  helpers/  (18 files)
    helpers.canvas.ts
    helpers.collection.ts
    helpers.color.ts
    helpers.config.ts
    helpers.config.types.ts
    helpers.core.ts
    helpers.curve.ts
    helpers.dataset.ts
    helpers.dom.ts
    helpers.easing.ts
    helpers.extras.ts
    helpers.interpolation.ts
    helpers.intl.ts
    helpers.math.ts
    helpers.options.ts
    helpers.rtl.ts
    helpers.segment.js
    index.ts
  platform/  (4 files)
    index.js
    platform.base.js
    platform.basic.js
    platform.dom.js
  plugins/  (15 files)
    plugin.filler/  (8 files)
      … 8 files under this directory
    index.js
    plugin.colors.ts
    plugin.decimation.js
    plugin.legend.js
    plugin.subtitle.js
    plugin.title.js
    plugin.tooltip.js
  scales/  (8 files)
    index.js
    scale.category.js
    scale.linear.js
    scale.linearbase.js
    scale.logarithmic.js
    scale.radialLinear.js
    scale.time.js
    scale.timeseries.js
  types/  (7 files)
    animation.d.ts
    basic.d.ts
    color.d.ts
    geometric.d.ts
    index.d.ts
    layout.d.ts
    utils.d.ts
  index.ts
  index.umd.ts
  types.ts
test/  (517 files)
  fixtures/  (515 files)
    controller.bar/  (87 files)
      … 87 files under this directory
    controller.bubble/  (8 files)
      … 8 files under this directory
    controller.doughnut/  (57 files)
      … 57 files under this directory
    controller.line/  (68 files)
      … 68 files under this directory
    controller.polarArea/  (54 files)
      … 54 files under this directory
    controller.radar/  (45 files)
      … 45 files under this directory
    controller.scatter/  (3 files)
      … 3 files under this directory
    core.datasetController/  (1 files)
      … 1 files under this directory
    core.interaction/  (3 files)
      … 3 files under this directory
    core.layouts/  (11 files)
      … 11 files under this directory
    core.scale/  (62 files)
      … 62 files under this directory
    element.line/  (17 files)
      … 17 files under this directory
    element.point/  (12 files)
      … 12 files under this directory
    mixed/  (2 files)
      … 2 files under this directory
    plugin.colors/  (12 files)
      … 12 files under this directory
    plugin.filler/  (64 files)
      … 64 files under this directory
    plugin.legend/  (9 files)
      … 9 files under this directory
  .eslintrc.yml
  BasicChartWebWorker.js
.browserslistrc
.codeclimate.yml
.editorconfig
.eslintignore
.eslintrc.yml
.gitignore
.htmllintrc
LICENSE.md
MAINTAINING.md
README.md
composer.json
karma.conf.cjs
package.json
pnpm-workspace.yaml
rollup.config.js
```

## Entry points

- [auto/auto.cjs](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/auto/auto.cjs)
- [helpers/helpers.cjs](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/helpers/helpers.cjs)
- [src/controllers/index.js](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/src/controllers/index.js)
- [src/core/index.ts](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/src/core/index.ts)
- [src/elements/index.js](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/src/elements/index.js)
- [src/helpers/index.ts](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/src/helpers/index.ts)
- [src/index.ts](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/src/index.ts)
- [src/platform/index.js](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/src/platform/index.js)
- [src/plugins/index.js](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/src/plugins/index.js)
- [src/plugins/plugin.filler/index.js](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/src/plugins/plugin.filler/index.js)
- [src/scales/index.js](https://github.com/chartjs/Chart.js/blob/71d44219e79e3ac41e6f9dc907022eebf574868d/src/scales/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). |
| auto package | library | Observed | Groups 3 file(s) under auto package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| elements package | library | Observed | Groups 5 file(s) under elements package (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 21 file(s) under helpers package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| index.umd.ts package | library | Observed | Groups 1 file(s) under index.umd.ts package (observed from repository paths and static analysis). |
| platform package | library | Observed | Groups 4 file(s) under platform package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 15 file(s) under plugins package (observed from repository paths and static analysis). |
| scales package | library | Observed | Groups 8 file(s) under scales package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 21 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 517 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 7 file(s) under types package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.editorconfig` (config)
- `.eslintrc.yml` (config)
- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/docs.yml` (config)
- `.github/ISSUE_TEMPLATE/feature.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/release-drafter.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/compressed-size.yml` (ci)
- `.github/workflows/deploy-docs.yml` (ci)
- `.github/workflows/release-drafter.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `auto/package.json` (manifest)
- `composer.json` (config)
- `docs/package.json` (manifest)
- `docs/samples/.eslintrc.yml` (config)
- `helpers/package.json` (manifest)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)

## Top-level layout

- `test` — 517 analysed file(s)
- `docs` — 152 analysed file(s)
- `src` — 90 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 13 analysed file(s)
- `scripts` — 5 analysed file(s)
- `auto` — 4 analysed file(s)
- `helpers` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `71d44219e79e3ac41e6f9dc907022eebf574868d` is the revision these paths and observations refer to.
