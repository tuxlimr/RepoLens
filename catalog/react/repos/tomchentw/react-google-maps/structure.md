# Project structure: tomchentw/react-google-maps

**Analysed commit:** `ca5c5c6f5346fb3ee0037893fbca488a408c9938`

**Commit reference:** [ca5c5c6f5346fb3ee0037893fbca488a408c9938](https://github.com/tomchentw/react-google-maps/commit/ca5c5c6f5346fb3ee0037893fbca488a408c9938)

**Tree at this commit:** [tomchentw/react-google-maps@ca5c5c6f5346](https://github.com/tomchentw/react-google-maps/tree/ca5c5c6f5346fb3ee0037893fbca488a408c9938)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tomchentw/react-google-maps |
| Description | React.js Google Maps integration component |
| Stars | 4625 |
| Forks | 917 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ca5c5c6f5346fb3ee0037893fbca488a408c9938` |
| Retrieved at | 2026-11-14T19:14:41.168383+00:00 |
| Files in this snapshot | 124 |

## Directory tree

```text
docs/  (1 files)
  index.html
lib/  (28 files)
  components/  (22 files)
    addons/  (3 files)
      … 3 files under this directory
    drawing/  (1 files)
      … 1 files under this directory
    places/  (2 files)
      … 2 files under this directory
    visualization/  (1 files)
      … 1 files under this directory
    BicyclingLayer.js
    Circle.js
    DirectionsRenderer.js
    FusionTablesLayer.js
    GoogleMap.js
    GroundOverlay.js
    InfoWindow.js
    KmlLayer.js
    Marker.js
    OverlayView.js
    Polygon.js
    Polyline.js
    Rectangle.js
    StreetViewPanorama.js
    TrafficLayer.js
  utils/  (2 files)
    MapChildHelper.js
    OverlayViewHelper.js
  constants.js
  index.js
  withGoogleMap.js
  withScriptjs.js
src/  (80 files)
  __tests__/  (1 files)
    index.spec.js
  components/  (45 files)
    addons/  (9 files)
      … 9 files under this directory
    drawing/  (3 files)
      … 3 files under this directory
    places/  (5 files)
      … 5 files under this directory
    visualization/  (2 files)
      … 2 files under this directory
    BicyclingLayer.jsx
    BicyclingLayer.md
    Circle.jsx
    DirectionsRenderer.jsx
    DirectionsRenderer.md
    FusionTablesLayer.jsx
    FusionTablesLayer.md
    GoogleMap.jsx
    GoogleMap.md
    GroundOverlay.jsx
    GroundOverlay.md
    InfoWindow.jsx
    InfoWindow.md
    KmlLayer.jsx
    KmlLayer.md
    Marker.jsx
    Marker.md
    OverlayView.jsx
    OverlayView.md
    Polygon.jsx
    Polyline.jsx
    Rectangle.jsx
    StreetViewPanorama.jsx
    StreetViewPanorama.md
    … 2 more files
  docs/  (3 files)
    configuration.md
    installation.md
    introduction.md
  macros/  (20 files)
    addons/  (1 files)
      … 1 files under this directory
    drawing/  (1 files)
      … 1 files under this directory
    places/  (2 files)
      … 2 files under this directory
    visualization/  (1 files)
      … 1 files under this directory
    BicyclingLayer.jsx
    Circle.jsx
    DirectionsRenderer.jsx
    FusionTablesLayer.jsx
    GoogleMap.jsx
    GroundOverlay.jsx
    InfoWindow.jsx
    KmlLayer.jsx
    Marker.jsx
    OverlayView.jsx
    Polygon.jsx
    Polyline.jsx
    Rectangle.jsx
    StreetViewPanorama.jsx
    TrafficLayer.jsx
  tx/  (3 files)
    ClassDefinition.js
    MapChild.js
    jscodeshift.js
  utils/  (2 files)
    MapChildHelper.js
    OverlayViewHelper.js
  constants.js
  index.js
  withGoogleMap.jsx
  withGoogleMap.md
  withScriptjs.jsx
  withScriptjs.md
types/  (3 files)
  index.d.ts
  tsconfig.json
  tslint.json
.codeclimate.yml
.editorconfig
.gitignore
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
PULL_REQUEST_TEMPLATE.md
README.md
package.json
styleguide.config.js
```

## Entry points

- [lib/index.js](https://github.com/tomchentw/react-google-maps/blob/ca5c5c6f5346fb3ee0037893fbca488a408c9938/lib/index.js)
- [src/index.js](https://github.com/tomchentw/react-google-maps/blob/ca5c5c6f5346fb3ee0037893fbca488a408c9938/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 27 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 28 file(s) under lib package (observed from repository paths and static analysis). |
| macros package | library | Observed | Groups 20 file(s) under macros package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 1 file(s) under __tests__ package (observed from repository paths and static analysis). |
| tx package | library | Observed | Groups 3 file(s) under tx package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 2 file(s) under utils package (observed from repository paths and static analysis). |
| withGoogleMap.jsx package | library | Observed | Groups 1 file(s) under withgooglemap.jsx package (observed from repository paths and static analysis). |
| withScriptjs.jsx package | library | Observed | Groups 1 file(s) under withscriptjs.jsx package (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.editorconfig` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)
- `src/components/addons/demoFancyMapStyles.json` (config)
- `types/tsconfig.json` (config)
- `types/tslint.json` (config)

## Top-level layout

- `src` — 80 analysed file(s)
- `lib` — 28 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `types` — 3 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ca5c5c6f5346fb3ee0037893fbca488a408c9938` is the revision these paths and observations refer to.
