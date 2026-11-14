# Project structure: visgl/react-map-gl

**Analysed commit:** `1afe1a98580680c870eeb1139c40a94835333705`

**Commit reference:** [1afe1a98580680c870eeb1139c40a94835333705](https://github.com/visgl/react-map-gl/commit/1afe1a98580680c870eeb1139c40a94835333705)

**Tree at this commit:** [visgl/react-map-gl@1afe1a985806](https://github.com/visgl/react-map-gl/tree/1afe1a98580680c870eeb1139c40a94835333705)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | visgl/react-map-gl |
| Description | React friendly API wrapper around MapboxGL JS |
| Stars | 8515 |
| Forks | 1345 |
| Licence | Other |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `1afe1a98580680c870eeb1139c40a94835333705` |
| Retrieved at | 2026-11-14T19:13:41.622840+00:00 |
| Files in this snapshot | 586 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.yml
    config.yml
    feature-request.yml
  workflows/  (3 files)
    release.yml
    test.yml
    website.yml
  SECURITY.md
docs/  (41 files)
  api-reference/  (31 files)
    mapbox/  (14 files)
      … 14 files under this directory
    maplibre/  (17 files)
      … 17 files under this directory
  get-started/  (5 files)
    adding-custom-data.md
    get-started.md
    mapbox-tokens.md
    state-management.md
    tips-and-tricks.md
  .gitignore
  README.md
  table-of-contents.json
  upgrade-guide.md
  whats-new.md
examples/  (303 files)
  .data/  (3 files)
    bart-station.json
    cities.json
    feature-example-sf.json
  get-started/  (36 files)
    basic/  (5 files)
      … 5 files under this directory
    controlled/  (5 files)
      … 5 files under this directory
    hook/  (8 files)
      … 8 files under this directory
    maplibre/  (4 files)
      … 4 files under this directory
    nextjs/  (6 files)
      … 6 files under this directory
    redux/  (8 files)
      … 8 files under this directory
  mapbox/  (137 files)
    clusters/  (8 files)
      … 8 files under this directory
    controls/  (8 files)
      … 8 files under this directory
    custom-cursor/  (7 files)
      … 7 files under this directory
    custom-overlay/  (8 files)
      … 8 files under this directory
    deckgl-overlay/  (6 files)
      … 6 files under this directory
    draggable-markers/  (8 files)
      … 8 files under this directory
    draw-polygon/  (8 files)
      … 8 files under this directory
    filter/  (8 files)
      … 8 files under this directory
    geocoder/  (8 files)
      … 8 files under this directory
    geojson/  (9 files)
      … 9 files under this directory
    geojson-animation/  (7 files)
      … 7 files under this directory
    heatmap/  (8 files)
      … 8 files under this directory
    interaction/  (7 files)
      … 7 files under this directory
    layers/  (7 files)
      … 7 files under this directory
    side-by-side/  (7 files)
      … 7 files under this directory
    terrain/  (7 files)
      … 7 files under this directory
    viewport-animation/  (7 files)
      … 7 files under this directory
    zoom-to-bounds/  (8 files)
      … 8 files under this directory
    map-style-basic-v8.json
  maplibre/  (125 files)
    clusters/  (7 files)
      … 7 files under this directory
    controls/  (7 files)
      … 7 files under this directory
    custom-cursor/  (6 files)
      … 6 files under this directory
    custom-overlay/  (7 files)
      … 7 files under this directory
    deckgl-overlay/  (5 files)
      … 5 files under this directory
    draggable-markers/  (7 files)
      … 7 files under this directory
    draw-polygon/  (7 files)
      … 7 files under this directory
    filter/  (7 files)
      … 7 files under this directory
    geocoder/  (7 files)
      … 7 files under this directory
    geojson/  (8 files)
      … 8 files under this directory
    geojson-animation/  (6 files)
      … 6 files under this directory
    globe/  (6 files)
      … 6 files under this directory
    heatmap/  (7 files)
      … 7 files under this directory
    interaction/  (6 files)
      … 6 files under this directory
    layers/  (6 files)
      … 6 files under this directory
    side-by-side/  (6 files)
      … 6 files under this directory
    terrain/  (6 files)
      … 6 files under this directory
    viewport-animation/  (6 files)
      … 6 files under this directory
    zoom-to-bounds/  (7 files)
      … 7 files under this directory
    map-style-basic-v8.json
  .eslintrc
  vite.config.local.js
modules/  (153 files)
  main/  (50 files)
    src/  (29 files)
      … 29 files under this directory
    test/  (19 files)
      … 19 files under this directory
    package.json
    tsconfig.json
  react-mapbox/  (54 files)
    src/  (30 files)
      … 30 files under this directory
    test/  (22 files)
      … 22 files under this directory
    package.json
    tsconfig.json
  react-maplibre/  (49 files)
    src/  (31 files)
      … 31 files under this directory
    test/  (16 files)
      … 16 files under this directory
    package.json
    tsconfig.json
scripts/  (1 files)
  update-release-branch.sh
test/  (16 files)
  apps/  (5 files)
    reuse-maps/  (5 files)
      … 5 files under this directory
  data/  (1 files)
    style.json
  render/  (2 files)
    index.jsx
    test-cases.jsx
  size/  (3 files)
    mapbox-legacy.js
    mapbox.js
    maplibre.js
  src/  (1 files)
    exports.ts
  .eslintrc
  browser-test-setup.ts
  node.js
  test-utils.js
website/  (48 files)
  src/  (39 files)
    examples/  (34 files)
      … 34 files under this directory
    pages/  (1 files)
      … 1 files under this directory
    mapbox-gl.css
    maplibre-gl.css
    maplibre-worker.js
    styles.css
  static/  (3 files)
    images/  (3 files)
      … 3 files under this directory
  .eslintignore
  .gitignore
  .yarnrc.yml
  babel.config.js
  docusaurus.config.js
  package.json
.gitignore
.nvmrc
.ocularrc.js
.prettierrc
.yarnrc.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
TESTING.md
biome.jsonc
index.html
lerna.json
package.json
tsconfig.json
vitest.config.ts
```

## Entry points

- [modules/react-mapbox/src/index.ts](https://github.com/visgl/react-map-gl/blob/1afe1a98580680c870eeb1139c40a94835333705/modules/react-mapbox/src/index.ts)
- [modules/react-maplibre/src/index.ts](https://github.com/visgl/react-map-gl/blob/1afe1a98580680c870eeb1139c40a94835333705/modules/react-maplibre/src/index.ts)
- [website/src/pages/index.jsx](https://github.com/visgl/react-map-gl/blob/1afe1a98580680c870eeb1139c40a94835333705/website/src/pages/index.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 90 file(s) under modules package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 73 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 4 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/website.yml` (ci)
- `.yarnrc.yml` (config)
- `docs/table-of-contents.json` (config)
- `examples/.data/bart-station.json` (config)
- `examples/.data/cities.json` (config)
- `examples/.data/feature-example-sf.json` (config)
- `examples/get-started/basic/package.json` (manifest)
- `examples/get-started/controlled/package.json` (manifest)
- `examples/get-started/hook/package.json` (manifest)
- `examples/get-started/maplibre/package.json` (manifest)
- `examples/get-started/nextjs/package.json` (manifest)
- `examples/get-started/redux/package.json` (manifest)
- `examples/mapbox/clusters/package.json` (manifest)
- `examples/mapbox/clusters/tsconfig.json` (config)
- `examples/mapbox/controls/package.json` (manifest)
- `examples/mapbox/controls/tsconfig.json` (config)
- `examples/mapbox/custom-cursor/package.json` (manifest)
- `examples/mapbox/custom-cursor/tsconfig.json` (config)
- `examples/mapbox/custom-overlay/package.json` (manifest)
- `examples/mapbox/custom-overlay/tsconfig.json` (config)
- `examples/mapbox/deckgl-overlay/package.json` (manifest)
- `examples/mapbox/deckgl-overlay/tsconfig.json` (config)
- `examples/mapbox/draggable-markers/package.json` (manifest)
- `examples/mapbox/draggable-markers/tsconfig.json` (config)
- `examples/mapbox/draw-polygon/package.json` (manifest)
- `examples/mapbox/draw-polygon/tsconfig.json` (config)
- `examples/mapbox/filter/package.json` (manifest)
- `examples/mapbox/filter/tsconfig.json` (config)
- `examples/mapbox/geocoder/package.json` (manifest)
- `examples/mapbox/geocoder/tsconfig.json` (config)
- `examples/mapbox/geojson-animation/package.json` (manifest)
- `examples/mapbox/geojson-animation/tsconfig.json` (config)
- `examples/mapbox/geojson/package.json` (manifest)
- `examples/mapbox/geojson/tsconfig.json` (config)
- `examples/mapbox/heatmap/package.json` (manifest)
- `examples/mapbox/heatmap/tsconfig.json` (config)
- `examples/mapbox/interaction/package.json` (manifest)
- `examples/mapbox/interaction/tsconfig.json` (config)
- `examples/mapbox/layers/package.json` (manifest)
- `examples/mapbox/layers/tsconfig.json` (config)
- `examples/mapbox/map-style-basic-v8.json` (config)
- `examples/mapbox/side-by-side/package.json` (manifest)
- `examples/mapbox/side-by-side/tsconfig.json` (config)
- `examples/mapbox/terrain/package.json` (manifest)
- `examples/mapbox/terrain/tsconfig.json` (config)
- `examples/mapbox/viewport-animation/package.json` (manifest)
- `examples/mapbox/viewport-animation/tsconfig.json` (config)
- `examples/mapbox/zoom-to-bounds/package.json` (manifest)
- `examples/mapbox/zoom-to-bounds/tsconfig.json` (config)
- `examples/maplibre/clusters/package.json` (manifest)
- `examples/maplibre/clusters/tsconfig.json` (config)
- `examples/maplibre/controls/package.json` (manifest)
- `examples/maplibre/controls/tsconfig.json` (config)
- `examples/maplibre/custom-cursor/package.json` (manifest)
- `examples/maplibre/custom-cursor/tsconfig.json` (config)
- `examples/maplibre/custom-overlay/package.json` (manifest)
- `examples/maplibre/custom-overlay/tsconfig.json` (config)
- `examples/maplibre/deckgl-overlay/package.json` (manifest)
- `examples/maplibre/deckgl-overlay/tsconfig.json` (config)
- `examples/maplibre/draggable-markers/package.json` (manifest)
- `examples/maplibre/draggable-markers/tsconfig.json` (config)
- `examples/maplibre/draw-polygon/package.json` (manifest)
- `examples/maplibre/draw-polygon/tsconfig.json` (config)
- `examples/maplibre/filter/package.json` (manifest)
- `examples/maplibre/filter/tsconfig.json` (config)
- `examples/maplibre/geocoder/package.json` (manifest)
- `examples/maplibre/geocoder/tsconfig.json` (config)
- `examples/maplibre/geojson-animation/package.json` (manifest)
- `examples/maplibre/geojson-animation/tsconfig.json` (config)
- `examples/maplibre/geojson/package.json` (manifest)
- `examples/maplibre/geojson/tsconfig.json` (config)
- `examples/maplibre/globe/package.json` (manifest)
- `examples/maplibre/globe/tsconfig.json` (config)
- `examples/maplibre/heatmap/package.json` (manifest)
- `examples/maplibre/heatmap/tsconfig.json` (config)
- `examples/maplibre/interaction/package.json` (manifest)
- `examples/maplibre/interaction/tsconfig.json` (config)
- `examples/maplibre/layers/package.json` (manifest)
- `examples/maplibre/layers/tsconfig.json` (config)
- `examples/maplibre/map-style-basic-v8.json` (config)
- `examples/maplibre/side-by-side/package.json` (manifest)
- `examples/maplibre/side-by-side/tsconfig.json` (config)
- `examples/maplibre/terrain/package.json` (manifest)
- `examples/maplibre/terrain/tsconfig.json` (config)
- `examples/maplibre/viewport-animation/package.json` (manifest)
- `examples/maplibre/viewport-animation/tsconfig.json` (config)
- `examples/maplibre/zoom-to-bounds/package.json` (manifest)
- `examples/maplibre/zoom-to-bounds/tsconfig.json` (config)
- `lerna.json` (config)
- `modules/main/package.json` (manifest)
- `modules/main/tsconfig.json` (config)
- `modules/react-mapbox/package.json` (manifest)
- `modules/react-mapbox/tsconfig.json` (config)
- `modules/react-maplibre/package.json` (manifest)
- `modules/react-maplibre/tsconfig.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `website/.yarnrc.yml` (config)
- `website/package.json` (manifest)
- `website/src/examples/table-of-contents.json` (config)

## Top-level layout

- `examples` — 303 analysed file(s)
- `modules` — 153 analysed file(s)
- `website` — 48 analysed file(s)
- `docs` — 41 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `test` — 16 analysed file(s)
- `.github` — 7 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1afe1a98580680c870eeb1139c40a94835333705` is the revision these paths and observations refer to.
