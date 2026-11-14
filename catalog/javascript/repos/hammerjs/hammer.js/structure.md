# Project structure: hammerjs/hammer.js

**Analysed commit:** `ff687ea0daa3c806b9accd2ecb1a46165ea3c00a`

**Commit reference:** [ff687ea0daa3c806b9accd2ecb1a46165ea3c00a](https://github.com/hammerjs/hammer.js/commit/ff687ea0daa3c806b9accd2ecb1a46165ea3c00a)

**Tree at this commit:** [hammerjs/hammer.js@ff687ea0daa3](https://github.com/hammerjs/hammer.js/tree/ff687ea0daa3c806b9accd2ecb1a46165ea3c00a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hammerjs/hammer.js |
| Description | A javascript library for multi-touch gestures :// You can touch this |
| Stars | 24316 |
| Forks | 2546 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ff687ea0daa3c806b9accd2ecb1a46165ea3c00a` |
| Retrieved at | 2026-11-14T19:11:02.542932+00:00 |
| Files in this snapshot | 107 |

## Directory tree

```text
src/  (63 files)
  input/  (5 files)
    mouse.js
    pointerevent.js
    singletouch.js
    touch.js
    touchmouse.js
  inputjs/  (15 files)
    compute-delta-xy.js
    compute-input-data.js
    compute-interval-input-data.js
    create-input-instance.js
    get-angle.js
    get-center.js
    get-direction.js
    get-distance.js
    get-rotation.js
    get-scale.js
    get-velocity.js
    input-constructor.js
    input-consts.js
    input-handler.js
    simple-clone-input-data.js
  recognizerjs/  (5 files)
    direction-str.js
    get-recognizer-by-name-if-manager.js
    recognizer-constructor.js
    recognizer-consts.js
    state-str.js
  recognizers/  (7 files)
    attribute.js
    pan.js
    pinch.js
    press.js
    rotate.js
    swipe.js
    tap.js
  touchactionjs/  (4 files)
    clean-touch-actions.js
    get-touchaction-props.js
    touchaction-Consts.js
    touchaction-constructor.js
  utils/  (23 files)
    add-event-listeners.js
    assign.js
    bind-fn.js
    bool-or-fn.js
    deprecate.js
    each.js
    extend.js
    get-window-for-element.js
    has-parent.js
    if-undefined.js
    in-array.js
    in-str.js
    inherit.js
    invoke-array-arg.js
    merge.js
    prefixed.js
    remove-event-listeners.js
    set-timeout-context.js
    split-str.js
    to-array.js
    unique-array.js
    unique-id.js
    utils-consts.js
  .babelrc
  hammer.js
  main.js
  manager.js
tests/  (26 files)
  manual/  (10 files)
    assets/  (1 files)
      … 1 files under this directory
    compute_touch_action.html
    input.html
    log.html
    multiple.html
    nested.html
    simulator-googlemaps.html
    simulator.html
    touchaction.html
    visual.html
  unit/  (16 files)
    assets/  (1 files)
      … 1 files under this directory
    gestures/  (3 files)
      … 3 files under this directory
    index.html
    test_enable.js
    test_events.js
    test_gestures.js
    test_hammer.js
    test_jquery_plugin.js
    test_multiple_taps.js
    test_nested_gesture_recognizers.js
    test_propagation_bubble.js
    test_require_failure.js
    test_simultaneous_recognition.js
    test_utils.js
.bowerrc
.editorconfig
.gitignore
.jscsrc
.jshintrc
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
LICENSE.md
README.md
banner.ejs
bower.json
changelog.js
component.json
hammer.js
package.json
rollup.config.js
string-replace.js
```

## Entry points

- [hammer.js](https://github.com/hammerjs/hammer.js/blob/ff687ea0daa3c806b9accd2ecb1a46165ea3c00a/hammer.js)
- [src/main.js](https://github.com/hammerjs/hammer.js/blob/ff687ea0daa3c806b9accd2ecb1a46165ea3c00a/src/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| hammer.js package | library | Observed | Groups 1 file(s) under hammer.js package (observed from repository paths and static analysis). |
| input package | library | Observed | Groups 5 file(s) under input package (observed from repository paths and static analysis). |
| inputjs package | library | Observed | Groups 15 file(s) under inputjs package (observed from repository paths and static analysis). |
| main.js package | library | Observed | Groups 1 file(s) under main.js package (observed from repository paths and static analysis). |
| manager.js package | library | Observed | Groups 1 file(s) under manager.js package (observed from repository paths and static analysis). |
| recognizerjs package | library | Observed | Groups 5 file(s) under recognizerjs package (observed from repository paths and static analysis). |
| recognizers package | library | Observed | Groups 7 file(s) under recognizers package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 26 file(s) under tests (observed from repository paths and static analysis). |
| touchactionjs package | library | Observed | Groups 4 file(s) under touchactionjs package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 23 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `bower.json` (config)
- `component.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 63 analysed file(s)
- `tests` — 26 analysed file(s)
- `(root files)` — 18 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ff687ea0daa3c806b9accd2ecb1a46165ea3c00a` is the revision these paths and observations refer to.
