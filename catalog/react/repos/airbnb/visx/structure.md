# Project structure: airbnb/visx

**Analysed commit:** `485c0359664ee8e612992defb16e1f035ed40b23`

**Commit reference:** [485c0359664ee8e612992defb16e1f035ed40b23](https://github.com/airbnb/visx/commit/485c0359664ee8e612992defb16e1f035ed40b23)

**Tree at this commit:** [airbnb/visx@485c0359664e](https://github.com/airbnb/visx/tree/485c0359664ee8e612992defb16e1f035ed40b23)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | airbnb/visx |
| Description | 🐯 visx | visualization components |
| Stars | 21109 |
| Forks | 776 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `485c0359664ee8e612992defb16e1f035ed40b23` |
| Retrieved at | 2026-11-14T19:13:10.375616+00:00 |
| Files in this snapshot | 779 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    pull_request.yml
    push.yml
assets/  (1 files)
  happo-wordmark.svg
config-eslint/  (4 files)
  base.js
  next.js
  prettier.js
  typescript.js
packages/  (754 files)
  visx-a11y/  (26 files)
    src/  (15 files)
      … 15 files under this directory
    test/  (7 files)
      … 7 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-annotation/  (24 files)
    src/  (11 files)
      … 11 files under this directory
    test/  (9 files)
      … 9 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-axis/  (34 files)
    src/  (17 files)
      … 17 files under this directory
    test/  (13 files)
      … 13 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-bounds/  (8 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (2 files)
      … 2 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-brush/  (16 files)
    src/  (9 files)
      … 9 files under this directory
    test/  (3 files)
      … 3 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-chart/  (15 files)
    src/  (6 files)
      … 6 files under this directory
    test/  (5 files)
      … 5 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-chord/  (10 files)
    src/  (3 files)
      … 3 files under this directory
    test/  (3 files)
      … 3 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-clip-path/  (10 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (2 files)
      … 2 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-curve/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-delaunay/  (12 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (4 files)
      … 4 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-demo/  (405 files)
    public/  (7 files)
      … 7 files under this directory
    src/  (391 files)
      … 391 files under this directory
    .gitignore
    Readme.md
    next-env.d.ts
    next.config.js
    package.json
    tsconfig.json
    vercel.json
  visx-drag/  (18 files)
    src/  (9 files)
      … 9 files under this directory
    test/  (5 files)
      … 5 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-event/  (14 files)
    src/  (7 files)
      … 7 files under this directory
    test/  (3 files)
      … 3 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-geo/  (24 files)
    src/  (11 files)
      … 11 files under this directory
    test/  (9 files)
      … 9 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-glyph/  (24 files)
    src/  (10 files)
      … 10 files under this directory
    test/  (10 files)
      … 10 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-gradient/  (21 files)
    src/  (13 files)
      … 13 files under this directory
    test/  (4 files)
      … 4 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-grid/  (22 files)
    src/  (10 files)
      … 10 files under this directory
    test/  (8 files)
      … 8 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-group/  (8 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (2 files)
      … 2 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-heatmap/  (11 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (3 files)
      … 3 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-hierarchy/  (19 files)
    src/  (11 files)
      … 11 files under this directory
    test/  (4 files)
      … 4 files under this directory
    Readme.md
    package.json
    tsconfig.json
    vitest.config.ts
  visx-kernel/  (25 files)
    src/  (12 files)
      … 12 files under this directory
    test/  (11 files)
      … 11 files under this directory
    Readme.md
    package.json
  sizes.json
.eslintignore
.eslintrc.js
.gitignore
.npmignore
.nvmrc
.prettierignore
.yarnrc.yml
ATTRIBUTION.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MIGRATION.md
PULL_REQUEST_TEMPLATE.md
README.md
babel.config.js
lerna.json
package.json
```

## Entry points

- [packages/visx-demo/src/sandboxes/template/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/template/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-annotation/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-annotation/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-area/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-area/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-axis/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-axis/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-bargroup-horizontal/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-bargroup-horizontal/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-bargroup/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-bargroup/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-bars/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-bars/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-barstack-horizontal/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-barstack-horizontal/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-barstack/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-barstack/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-brush/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-brush/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-chord/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-chord/index.tsx)
- [packages/visx-demo/src/sandboxes/visx-curve/index.tsx](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/packages/visx-demo/src/sandboxes/visx-curve/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 95 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config-eslint package | library | Observed | Groups 4 file(s) under config-eslint package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 431 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 109 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/pull_request.yml` (ci)
- `.github/workflows/push.yml` (ci)
- `.yarnrc.yml` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/sizes.json` (config)
- `packages/visx-a11y/package.json` (manifest)
- `packages/visx-a11y/tsconfig.json` (config)
- `packages/visx-annotation/package.json` (manifest)
- `packages/visx-annotation/tsconfig.json` (config)
- `packages/visx-axis/package.json` (manifest)
- `packages/visx-axis/tsconfig.json` (config)
- `packages/visx-bounds/package.json` (manifest)
- `packages/visx-bounds/tsconfig.json` (config)
- `packages/visx-brush/package.json` (manifest)
- `packages/visx-brush/tsconfig.json` (config)
- `packages/visx-chart/package.json` (manifest)
- `packages/visx-chart/tsconfig.json` (config)
- `packages/visx-chord/package.json` (manifest)
- `packages/visx-chord/tsconfig.json` (config)
- `packages/visx-clip-path/package.json` (manifest)
- `packages/visx-clip-path/tsconfig.json` (config)
- `packages/visx-curve/package.json` (manifest)
- `packages/visx-curve/tsconfig.json` (config)
- `packages/visx-delaunay/package.json` (manifest)
- `packages/visx-delaunay/tsconfig.json` (config)
- `packages/visx-demo/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/template/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-annotation/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-area/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-axis/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-bargroup-horizontal/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-bargroup/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-bars/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-barstack-horizontal/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-barstack/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-brush/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-chord/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-curve/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-delaunay-triangulation/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-delaunay-voronoi/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-dendrogram/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-dots/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-drag-i/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-drag-ii/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-geo-albers-usa/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-geo-albers-usa/us-abbr.json` (config)
- `packages/visx-demo/src/sandboxes/visx-geo-custom/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-geo-mercator/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-glyph/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-gradient/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-heatmap/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-legend/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-linktypes/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-network/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-pack/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-pattern/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-polygons/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-radar/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-radial-bars/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-responsive/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-sankey/energy.json` (config)
- `packages/visx-demo/src/sandboxes/visx-sankey/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-shape-line-radial/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-shape-pie/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-shape-splitlinepath/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-stacked-areas/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-stats/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-streamgraph/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-threshold/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-tooltip/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-tree/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-treemap/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-voronoi/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-wordcloud/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-xychart/package.json` (manifest)
- `packages/visx-demo/src/sandboxes/visx-zoom-i/package.json` (manifest)
- `packages/visx-demo/tsconfig.json` (config)
- `packages/visx-demo/vercel.json` (config)
- `packages/visx-drag/package.json` (manifest)
- `packages/visx-drag/tsconfig.json` (config)
- `packages/visx-event/package.json` (manifest)
- `packages/visx-event/tsconfig.json` (config)
- `packages/visx-geo/package.json` (manifest)
- `packages/visx-geo/tsconfig.json` (config)
- `packages/visx-glyph/package.json` (manifest)
- `packages/visx-glyph/tsconfig.json` (config)
- `packages/visx-gradient/package.json` (manifest)
- `packages/visx-gradient/tsconfig.json` (config)
- `packages/visx-grid/package.json` (manifest)
- `packages/visx-grid/tsconfig.json` (config)
- `packages/visx-group/package.json` (manifest)
- `packages/visx-group/tsconfig.json` (config)
- `packages/visx-heatmap/package.json` (manifest)
- `packages/visx-heatmap/tsconfig.json` (config)
- `packages/visx-hierarchy/package.json` (manifest)
- `packages/visx-hierarchy/tsconfig.json` (config)
- `packages/visx-kernel/package.json` (manifest)

## Top-level layout

- `packages` — 754 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `config-eslint` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 21 file(s) were skipped during inventory (21 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `485c0359664ee8e612992defb16e1f035ed40b23` is the revision these paths and observations refer to.
