# Project structure: julianshapiro/velocity

**Analysed commit:** `767e35cac12120be526eef330e4d988b2c3cfc3c`

**Commit reference:** [767e35cac12120be526eef330e4d988b2c3cfc3c](https://github.com/julianshapiro/velocity/commit/767e35cac12120be526eef330e4d988b2c3cfc3c)

**Tree at this commit:** [julianshapiro/velocity@767e35cac121](https://github.com/julianshapiro/velocity/tree/767e35cac12120be526eef330e4d988b2c3cfc3c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | julianshapiro/velocity |
| Description | Accelerated JavaScript animation. |
| Stars | 17190 |
| Forks | 1510 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `767e35cac12120be526eef330e4d988b2c3cfc3c` |
| Retrieved at | 2026-11-14T19:11:28.636442+00:00 |
| Files in this snapshot | 254 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
gsap/  (16 files)
  GreenSock Animation Platform (GSAP) Speed Test_files/  (15 files)
    CSSPlugin.js.download
    CSSPlugin.min.js.download
    Ease.js.download
    TweenLite.min.js.download
    anime.min.js.download
    css
    dojo.js.download
    easeljs-0.4.2.min.js.download
    easing.js.download
    jquery-3.0.0.min.js.download
    jquery.gsap.min.js.download
    mootools-core-1.4.5-full-compat-yc.js.download
    tweenjs-0.2.0.min.js.download
    web-animations-basic.min.js.download
    zepto.min.js.download
  GreenSock Animation Platform (GSAP) Speed Test.html
legacy/  (6 files)
  README.md
  blur.ts
  borderColor.ts
  clip.ts
  normalisations.ts
  opacity.ts
src/  (64 files)
  Velocity/  (56 files)
    actions/  (11 files)
      … 11 files under this directory
    css/  (8 files)
      … 8 files under this directory
    easing/  (10 files)
      … 10 files under this directory
    normalizations/  (13 files)
      … 13 files under this directory
    _all.ts
    camelCase.ts
    complete.ts
    data.ts
    defaults.ts
    index.ts
    options.ts
    patch.ts
    queue.ts
    sequences.ts
    sequencesObject.ts
    state.ts
    tick.ts
    tweens.ts
  constants.ts
  fakeClass.js
  fakeClass.ts
  tsconfig.json
  types.ts
  utility.ts
  velocity.ts
  velocityFn.ts
src-ui/  (93 files)
  attention_seekers/  (11 files)
    _all.ts
    bounce.ts
    flash.ts
    headShake.ts
    jello.ts
    pulse.ts
    rubberBand.ts
    shake.ts
    swing.ts
    tada.ts
    wobble.ts
  bouncing_entrances/  (6 files)
    _all.ts
    bounceIn.ts
    bounceInDown.ts
    bounceInLeft.ts
    bounceInRight.ts
    bounceInUp.ts
  bouncing_exits/  (6 files)
    _all.ts
    bounceOut.ts
    bounceOutDown.ts
    bounceOutLeft.ts
    bounceOutRight.ts
    bounceOutUp.ts
  fading_entrances/  (10 files)
    _all.ts
    fadeIn.ts
    fadeInDown.ts
    fadeInDownBig.ts
    fadeInLeft.ts
    fadeInLeftBig.ts
    fadeInRight.ts
    fadeInRightBig.ts
    fadeInUp.ts
    fadeInUpBig.ts
  fading_exits/  (10 files)
    _all.ts
    fadeOut.ts
    fadeOutDown.ts
    fadeOutDownBig.ts
    fadeOutLeft.ts
    fadeOutLeftBig.ts
    fadeOutRight.ts
    fadeOutRightBig.ts
    fadeOutUp.ts
    fadeOutUpBig.ts
  flippers/  (6 files)
    _all.ts
    flip.ts
    flipInX.ts
    flipInY.ts
    flipOutX.ts
    flipOutY.ts
  lightspeed/  (3 files)
    _all.ts
    lightSpeedIn.ts
    lightSpeedOut.ts
  rotating_entrances/  (6 files)
    _all.ts
    rotateIn.ts
    rotateInDownLeft.ts
    rotateInDownRight.ts
    rotateInUpLeft.ts
    rotateInUpRight.ts
  rotating_exits/  (6 files)
    _all.ts
    rotateOut.ts
    rotateOutDownLeft.ts
    rotateOutDownRight.ts
    rotateOutUpLeft.ts
    rotateOutUpRight.ts
  sliding_entrances/  (5 files)
    _all.ts
    slideInDown.ts
    slideInLeft.ts
    slideInRight.ts
    slideInUp.ts
  sliding_exits/  (5 files)
    _all.ts
    slideOutDown.ts
    slideOutLeft.ts
    slideOutRight.ts
    slideOutUp.ts
  specials/  (5 files)
    _all.ts
    hinge.ts
    jackInTheBox.ts
    rollIn.ts
    rollOut.ts
  zooming_entrances/  (6 files)
    _all.ts
    zoomIn.ts
    zoomInDown.ts
    zoomInLeft.ts
    zoomInRight.ts
    zoomInUp.ts
  zooming_exits/  (6 files)
    _all.ts
    zoomOut.ts
    zoomOutDown.ts
    zoomOutLeft.ts
    zoomOutRight.ts
    zoomOutUp.ts
  tsconfig.json
  velocity.ui.ts
test/  (52 files)
  src/  (47 files)
    1_Core/  (6 files)
      … 6 files under this directory
    2_Option/  (13 files)
      … 13 files under this directory
    3_Command/  (7 files)
      … 7 files under this directory
    4_Feature/  (7 files)
      … 7 files under this directory
    5_UIPack/  (7 files)
      … 7 files under this directory
    6_Properties/  (4 files)
      … 4 files under this directory
    test.ts
    tsconfig.json
    utilities.ts
  index.html
  qunit-2.5.0.css
  qunit-2.5.0.js
  qunit-assert-close.js
  test.js
.babelrc
.editorconfig
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
README.md
V2_CHANGES.md
babel.config.js
bower.json
docs.ts
package.json
rollup.config.js
tsconfig.json
tslint.json
velocity.d.ts
velocity.es5.js
velocity.js
velocity.ui.js
version.ts
```

## Entry points

- [src/Velocity/actions/index.ts](https://github.com/julianshapiro/velocity/blob/767e35cac12120be526eef330e4d988b2c3cfc3c/src/Velocity/actions/index.ts)
- [src/Velocity/css/index.ts](https://github.com/julianshapiro/velocity/blob/767e35cac12120be526eef330e4d988b2c3cfc3c/src/Velocity/css/index.ts)
- [src/Velocity/easing/index.ts](https://github.com/julianshapiro/velocity/blob/767e35cac12120be526eef330e4d988b2c3cfc3c/src/Velocity/easing/index.ts)
- [src/Velocity/index.ts](https://github.com/julianshapiro/velocity/blob/767e35cac12120be526eef330e4d988b2c3cfc3c/src/Velocity/index.ts)
- [src/Velocity/normalizations/index.ts](https://github.com/julianshapiro/velocity/blob/767e35cac12120be526eef330e4d988b2c3cfc3c/src/Velocity/normalizations/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.ts package | library | Observed | Groups 1 file(s) under constants.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| fakeClass.js package | library | Observed | Groups 1 file(s) under fakeclass.js package (observed from repository paths and static analysis). |
| fakeClass.ts package | library | Observed | Groups 1 file(s) under fakeclass.ts package (observed from repository paths and static analysis). |
| legacy package | library | Observed | Groups 5 file(s) under legacy package (observed from repository paths and static analysis). |
| src-ui package | library | Observed | Groups 92 file(s) under src-ui package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 52 file(s) under tests (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| utility.ts package | library | Observed | Groups 1 file(s) under utility.ts package (observed from repository paths and static analysis). |
| Velocity package | library | Observed | Groups 56 file(s) under velocity package (observed from repository paths and static analysis). |
| velocity.ts package | library | Observed | Groups 1 file(s) under velocity.ts package (observed from repository paths and static analysis). |
| velocityFn.ts package | library | Observed | Groups 1 file(s) under velocityfn.ts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `bower.json` (config)
- `package.json` (manifest)
- `src-ui/tsconfig.json` (config)
- `src/tsconfig.json` (config)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `src-ui` — 93 analysed file(s)
- `src` — 64 analysed file(s)
- `test` — 52 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `gsap` — 16 analysed file(s)
- `legacy` — 6 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `767e35cac12120be526eef330e4d988b2c3cfc3c` is the revision these paths and observations refer to.
