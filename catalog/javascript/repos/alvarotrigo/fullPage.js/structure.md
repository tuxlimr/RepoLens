# Project structure: alvarotrigo/fullPage.js

**Analysed commit:** `49f15effa7b195def295a36f872c28153cf9fb00`

**Commit reference:** [49f15effa7b195def295a36f872c28153cf9fb00](https://github.com/alvarotrigo/fullPage.js/commit/49f15effa7b195def295a36f872c28153cf9fb00)

**Tree at this commit:** [alvarotrigo/fullPage.js@49f15effa7b1](https://github.com/alvarotrigo/fullPage.js/tree/49f15effa7b195def295a36f872c28153cf9fb00)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alvarotrigo/fullPage.js |
| Description | fullPage plugin by Alvaro Trigo. Create full screen pages fast and simple |
| Stars | 35355 |
| Forks | 7055 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `49f15effa7b195def295a36f872c28153cf9fb00` |
| Retrieved at | 2026-11-14T19:10:43.004912+00:00 |
| Files in this snapshot | 257 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
examples/  (72 files)
  imgs/  (1 files)
    copyright.txt
  module_loaders/  (13 files)
    browserify-example/  (3 files)
      … 3 files under this directory
    requirejs-example/  (5 files)
      … 5 files under this directory
    webpack-example/  (5 files)
      … 5 files under this directory
  active-slide.html
  angular-fullpage.html
  auto-height.html
  autoplay-video-and-audio.html
  background-video.html
  backgrounds-fixed.html
  backgrounds.html
  callbacks.html
  cards.html
  cinematic.html
  continuous-horizontal.html
  continuous-vertical.html
  css3.html
  custom-arrows.html
  drag-and-move.html
  drop-effect.html
  easing-css3.html
  easing-js.html
  effects.html
  examples.css
  examples.js
  fading-effect.html
  fixed-headers.html
  gradient-backgrounds.html
  … 34 more files
gulp/  (1 files)
  build.js
lang/  (29 files)
  brazilian-portuguese/  (3 files)
    README.md
    how-to-activate-fullpage-extension.md
    parallax-extension.md
  chinese/  (3 files)
    README.md
    how-to-activate-fullpage-extension.md
    parallax-extensionmd.md
  french/  (3 files)
    README.md
    how-to-activate-fullpage-extension.md
    parallax-extension.md
  japanese/  (3 files)
    README.md
    how-to-activate-fullpage-extension.md
    parallax-extension.md
  korean/  (3 files)
    README.md
    how-to-activate-fullpage-extension.md
    parallax-extension.md
  russian/  (3 files)
    README.md
    how-to-activate-fullpage-extension.md
    parallax-extension.md
  spanish/  (3 files)
    README.md
    how-to-activate-fullpage-extension.md
    parallax-extension.md
  website/  (8 files)
    br.yml
    en.yml
    es.yml
    fr.yml
    ja.yml
    ko.yml
    ru.yml
    zh.yml
src/  (100 files)
  css/  (1 files)
    fullpage.css
  js/  (98 files)
    anchors/  (4 files)
      … 4 files under this directory
    beyondFullpage/  (4 files)
      … 4 files under this directory
    callbacks/  (4 files)
      … 4 files under this directory
    common/  (18 files)
      … 18 files under this directory
    dom/  (4 files)
      … 4 files under this directory
    infiniteScroll/  (3 files)
      … 3 files under this directory
    keyboard/  (2 files)
      … 2 files under this directory
    lazyLoad/  (2 files)
      … 2 files under this directory
    menu/  (3 files)
      … 3 files under this directory
    mixed/  (2 files)
      … 2 files under this directory
    mouse/  (2 files)
      … 2 files under this directory
    nav/  (4 files)
      … 4 files under this directory
    polyfills/  (6 files)
      … 6 files under this directory
    scroll/  (12 files)
      … 12 files under this directory
    slides/  (6 files)
      … 6 files under this directory
    app.js
    arrows.js
    autoScrolling.js
    bindings.js
    console.js
    dynamic.js
    easing.js
    fitToSection.js
    fullpage.js
    instance.js
    jquery-adaptor.js
    media.js
    normalScrollElements.js
    optionsDefault.js
    resize.js
    responsive.js
    scrolloverflow.js
    sections.js
    speed.js
    stateClasses.js
    stateUpdates.js
    touch.js
  jsconfig.json
tests/  (38 files)
  unit/  (36 files)
    arrows.js
    bigSectionsDestination.js
    callbacks.js
    callbacksV3.js
    continuousVertical.js
    destroy.js
    displayWarnings.js
    easingcss3.js
    fitToSection.js
    fixedElements.js
    keyboardScrolling.js
    lazyload.js
    lockAnchors.js
    loopBottom.js
    loopTop.js
    menu.js
    moveSectionDown.js
    moveSectionUp.js
    moveSlideLeft.js
    moveSlideRight.js
    moveTo.js
    nav.js
    normalScrollElements.js
    paddings.js
    … 12 more files
  index.html
  utils.js
types/  (1 files)
  index.d.ts
vendors/  (1 files)
  easings.js
. jshintrc
.gitattributes
.gitignore
BACKERS.md
CONTRIBUTING.md
FUNDING.yml
LICENSE
README.md
SECURITY.md
bower.json
gulpfile.js
package.json
rollup.config.js
```

## Entry points

- [src/js/anchors/index.js](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/src/js/anchors/index.js)
- [src/js/app.js](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/src/js/app.js)
- [src/js/beyondFullpage/index.js](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/src/js/beyondFullpage/index.js)
- [src/js/keyboard/index.js](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/src/js/keyboard/index.js)
- [src/js/menu/index.js](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/src/js/menu/index.js)
- [src/js/nav/index.js](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/src/js/nav/index.js)
- [src/js/polyfills/index.js](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/src/js/polyfills/index.js)
- [src/js/scroll/index.js](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/src/js/scroll/index.js)
- [src/js/slides/index.js](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/src/js/slides/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| gulp package | library | Observed | Groups 1 file(s) under gulp package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 98 file(s) under js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 38 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| vendors package | library | Observed | Groups 1 file(s) under vendors package (observed from repository paths and static analysis). |

## Important files

- `FUNDING.yml` (config)
- `bower.json` (config)
- `examples/module_loaders/browserify-example/package.json` (manifest)
- `examples/module_loaders/requirejs-example/package.json` (manifest)
- `examples/module_loaders/webpack-example/package.json` (manifest)
- `lang/website/br.yml` (config)
- `lang/website/en.yml` (config)
- `lang/website/es.yml` (config)
- `lang/website/fr.yml` (config)
- `lang/website/ja.yml` (config)
- `lang/website/ko.yml` (config)
- `lang/website/ru.yml` (config)
- `lang/website/zh.yml` (config)
- `package.json` (manifest)
- `src/jsconfig.json` (config)

## Top-level layout

- `src` — 100 analysed file(s)
- `examples` — 72 analysed file(s)
- `tests` — 38 analysed file(s)
- `lang` — 29 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 2 analysed file(s)
- `gulp` — 1 analysed file(s)
- `types` — 1 analysed file(s)
- `vendors` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (5 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `49f15effa7b195def295a36f872c28153cf9fb00` is the revision these paths and observations refer to.
