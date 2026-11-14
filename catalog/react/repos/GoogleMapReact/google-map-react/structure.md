# Project structure: GoogleMapReact/google-map-react

**Analysed commit:** `ba0ef4df4351c511e3dce67d0214f4c5270dcf52`

**Commit reference:** [ba0ef4df4351c511e3dce67d0214f4c5270dcf52](https://github.com/GoogleMapReact/google-map-react/commit/ba0ef4df4351c511e3dce67d0214f4c5270dcf52)

**Tree at this commit:** [GoogleMapReact/google-map-react@ba0ef4df4351](https://github.com/GoogleMapReact/google-map-react/tree/ba0ef4df4351c511e3dce67d0214f4c5270dcf52)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | GoogleMapReact/google-map-react |
| Description | Google map library for react that allows rendering components as markers :tada: |
| Stars | 6480 |
| Forks | 843 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ba0ef4df4351c511e3dce67d0214f4c5270dcf52` |
| Retrieved at | 2026-11-14T19:14:04.981903+00:00 |
| Files in this snapshot | 56 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    BUG_REPORT.md
    FEATURE_REQUEST.md
  workflows/  (1 files)
    npm-publish.yml
  lock.yml
example/  (11 files)
  public/  (3 files)
    index.html
    manifest.json
    places.json
  src/  (6 files)
    components/  (1 files)
      … 1 files under this directory
    const/  (1 files)
      … 1 files under this directory
    App.js
    App.test.js
    index.css
    index.js
  README.md
  package.json
src/  (30 files)
  lib/  (8 files)
    geo/  (7 files)
      … 7 files under this directory
    index.js
  loaders/  (1 files)
    google_map_loader.js
  test/  (1 files)
    components/  (1 files)
      … 1 files under this directory
  utils/  (12 files)
    detect.js
    detectElementResize.js
    isArraysEqualEps.js
    isEmpty.js
    isNumber.js
    isPlainObject.js
    log2.js
    omit.js
    passiveEvents.js
    pick.js
    raf.js
    shallowEqual.js
  google_heatmap.js
  google_map.js
  google_map_map.js
  google_map_markers.js
  google_map_markers_prerender.js
  index.cjs.js
  index.js
  marker_dispatcher.js
.eslintignore
.eslintrc
.gitignore
.prettierrc
.travis.yml
API.md
CHANGELOG.md
DOC.md
LICENSE.md
README.md
package.json
```

## Entry points

- [src/index.js](https://github.com/GoogleMapReact/google-map-react/blob/ba0ef4df4351c511e3dce67d0214f4c5270dcf52/src/index.js)
- [src/lib/geo/index.js](https://github.com/GoogleMapReact/google-map-react/blob/ba0ef4df4351c511e3dce67d0214f4c5270dcf52/src/lib/geo/index.js)
- [src/lib/index.js](https://github.com/GoogleMapReact/google-map-react/blob/ba0ef4df4351c511e3dce67d0214f4c5270dcf52/src/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| google_heatmap.js package | library | Observed | Groups 1 file(s) under google_heatmap.js package (observed from repository paths and static analysis). |
| google_map.js package | library | Observed | Groups 1 file(s) under google_map.js package (observed from repository paths and static analysis). |
| google_map_map.js package | library | Observed | Groups 1 file(s) under google_map_map.js package (observed from repository paths and static analysis). |
| google_map_markers.js package | library | Observed | Groups 1 file(s) under google_map_markers.js package (observed from repository paths and static analysis). |
| google_map_markers_prerender.js package | library | Observed | Groups 1 file(s) under google_map_markers_prerender.js package (observed from repository paths and static analysis). |
| index.cjs.js package | library | Observed | Groups 1 file(s) under index.cjs.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 6 file(s) under lib package (observed from repository paths and static analysis). |
| loaders package | library | Observed | Groups 1 file(s) under loaders package (observed from repository paths and static analysis). |
| marker_dispatcher.js package | library | Observed | Groups 1 file(s) under marker_dispatcher.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 12 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/lock.yml` (config)
- `.github/workflows/npm-publish.yml` (ci)
- `.travis.yml` (ci)
- `example/package.json` (manifest)
- `example/public/manifest.json` (config)
- `example/public/places.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 30 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `example` — 11 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ba0ef4df4351c511e3dce67d0214f4c5270dcf52` is the revision these paths and observations refer to.
