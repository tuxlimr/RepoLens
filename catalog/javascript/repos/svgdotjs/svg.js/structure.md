# Project structure: svgdotjs/svg.js

**Analysed commit:** `4b8809b1554c44a84f8992cdbda60480336cc040`

**Commit reference:** [4b8809b1554c44a84f8992cdbda60480336cc040](https://github.com/svgdotjs/svg.js/commit/4b8809b1554c44a84f8992cdbda60480336cc040)

**Tree at this commit:** [svgdotjs/svg.js@4b8809b1554c](https://github.com/svgdotjs/svg.js/tree/4b8809b1554c44a84f8992cdbda60480336cc040)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | svgdotjs/svg.js |
| Description | The lightweight library for manipulating and animating SVG |
| Stars | 11924 |
| Forks | 1094 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `4b8809b1554c44a84f8992cdbda60480336cc040` |
| Retrieved at | 2026-11-14T19:12:12.921590+00:00 |
| Files in this snapshot | 209 |

## Directory tree

```text
.config/  (7 files)
  karma.conf.cjs
  karma.conf.common.cjs
  polyfillListIE.js
  pretest.js
  rolldown.config.js
  rolldown.polyfills.js
  rolldown.tests.js
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    feature-request.md
    other.md
  CONTRIBUTING.md
  FUNDING.yml
bench/  (13 files)
  tests/  (11 files)
    10000-accesses.js
    10000-boxes.js
    10000-circles.js
    10000-each.js
    10000-pathArray-bbox.js
    10000-pathArrays.js
    10000-paths.js
    10000-pointArray-bbox.js
    10000-rects.js
    10000-textContent.js
    10000-transform.js
  runner.html
  svg.bench.js
playgrounds/  (11 files)
  colors/  (3 files)
    index.html
    main.js
    style.css
  matrix/  (4 files)
    drag.js
    index.html
    matrix.js
    style.css
  transforms/  (3 files)
    index.html
    style.css
    transforms.js
  webpack.config.js
spec/  (85 files)
  fixtures/  (2 files)
    fixture.css
    fixture.svg
  package/  (5 files)
    fixtures/  (4 files)
      … 4 files under this directory
    package-contract.mjs
  spec/  (71 files)
    animation/  (6 files)
      … 6 files under this directory
    elements/  (30 files)
      … 30 files under this directory
    modules/  (18 files)
      … 18 files under this directory
    polyfills/  (1 files)
      … 1 files under this directory
    types/  (11 files)
      … 11 files under this directory
    utils/  (5 files)
      … 5 files under this directory
  RAFPlugin.js
  SpecRunner.html
  SpecRunnerEs6.html
  helpers.js
  runSVGDomTest.js
  setupBrowser.js
  setupSVGDom.js
src/  (77 files)
  animation/  (6 files)
    Animator.js
    Controller.js
    Morphable.js
    Queue.js
    Runner.js
    Timeline.js
  elements/  (30 files)
    A.js
    Circle.js
    ClipPath.js
    Container.js
    Defs.js
    Dom.js
    Element.js
    Ellipse.js
    ForeignObject.js
    Fragment.js
    G.js
    Gradient.js
    Image.js
    Line.js
    Marker.js
    Mask.js
    Path.js
    Pattern.js
    Polygon.js
    Polyline.js
    Rect.js
    Shape.js
    Stop.js
    Style.js
    … 6 more files
  modules/  (21 files)
    core/  (14 files)
      … 14 files under this directory
    optional/  (7 files)
      … 7 files under this directory
  polyfills/  (2 files)
    children.js
    innerHTML.js
  types/  (11 files)
    Base.js
    Box.js
    Color.js
    EventTarget.js
    List.js
    Matrix.js
    PathArray.js
    Point.js
    PointArray.js
    SVGArray.js
    SVGNumber.js
  utils/  (5 files)
    adopter.js
    methods.js
    pathParser.js
    utils.js
    window.js
  main.js
  svg.js
.gitignore
.oxfmtrc.json
.oxlintrc.json
.travis.yml
CHANGELOG.md
LICENSE.txt
README.md
package.json
pnpm-workspace.yaml
svg.js.d.ts
tsconfig.json
```

## Entry points

- [playgrounds/colors/main.js](https://github.com/svgdotjs/svg.js/blob/4b8809b1554c44a84f8992cdbda60480336cc040/playgrounds/colors/main.js)
- [src/main.js](https://github.com/svgdotjs/svg.js/blob/4b8809b1554c44a84f8992cdbda60480336cc040/src/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| animation package | library | Observed | Groups 6 file(s) under animation package (observed from repository paths and static analysis). |
| bench package | library | Observed | Groups 1 file(s) under bench package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| elements package | library | Observed | Groups 30 file(s) under elements package (observed from repository paths and static analysis). |
| main.js package | library | Observed | Groups 1 file(s) under main.js package (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 7 file(s) under modules package (observed from repository paths and static analysis). |
| playgrounds package | library | Observed | Groups 5 file(s) under playgrounds package (observed from repository paths and static analysis). |
| polyfills package | library | Observed | Groups 2 file(s) under polyfills package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 25 file(s) under service / domain layer (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 69 file(s) under spec package (observed from repository paths and static analysis). |
| svg.js package | library | Observed | Groups 1 file(s) under svg.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 11 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `spec` — 85 analysed file(s)
- `src` — 77 analysed file(s)
- `bench` — 13 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `playgrounds` — 11 analysed file(s)
- `.config` — 7 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4b8809b1554c44a84f8992cdbda60480336cc040` is the revision these paths and observations refer to.
