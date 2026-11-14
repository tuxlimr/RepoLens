# Project structure: akiran/react-slick

**Analysed commit:** `97442318e9a442bd4a84eb25133ef62087f98232`

**Commit reference:** [97442318e9a442bd4a84eb25133ef62087f98232](https://github.com/akiran/react-slick/commit/97442318e9a442bd4a84eb25133ef62087f98232)

**Tree at this commit:** [akiran/react-slick@97442318e9a4](https://github.com/akiran/react-slick/tree/97442318e9a442bd4a84eb25133ef62087f98232)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | akiran/react-slick |
| Description | React carousel component  |
| Stars | 11908 |
| Forks | 2065 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `97442318e9a442bd4a84eb25133ef62087f98232` |
| Retrieved at | 2026-11-14T19:12:13.198148+00:00 |
| Files in this snapshot | 101 |

## Directory tree

```text
.github/  (2 files)
  FUNDING.yml
  ISSUE_TEMPLATE.md
__tests__/  (14 files)
  regression/  (4 files)
    fix-1813.test.js
    fix-1874.test.js
    fix-2315.test.js
    fix-2414.test.js
  utils/  (1 files)
    filterSettings.test.js
  SimpleSlider.test.js
  TestComponents.js
  afterChange.test.js
  arrows.js
  beforeChange.test.js
  lazyLoad.test.js
  observations.json
  sliderStyles.test.js
  testUtils.js
docs/  (13 files)
  scripts/  (2 files)
    generateExampleConfigs.js
    generateExamples.js
  api.md
  common.md
  demos.js
  docs.css
  docs.js
  index.html
  index.js
  routes.js
  single-demo.js
  slick-theme.css
  slick.css
examples/  (37 files)
  __tests__/  (7 files)
    CentreMode.test.js
    Fade.js
    FocusOnSelect.test.js
    MultipleItems.test.js
    SimpleSlider.test.js
    SlickGoTo.test.js
    UnevenSets.test.js
  AdaptiveHeight.js
  AppendDots.js
  AsNavFor.js
  AutoPlay.js
  AutoPlayMethods.js
  CenterMode.js
  CustomArrows.js
  CustomPaging.js
  CustomSlides.js
  DynamicSlides.js
  Fade.js
  FocusOnSelect.js
  LazyLoad.js
  MultipleItems.js
  MultipleRows.js
  PauseOnHover.js
  PreviousNextMethods.js
  Resizable.js
  Responsive.js
  Rtl.js
  SimpleSlider.js
  SlickGoTo.js
  SlideChangeHooks.js
  SwipeToSlide.js
  … 6 more files
playwright/  (2 files)
  index.html
  index.jsx
playwright-tests/  (6 files)
  features/  (2 files)
    responsive/  (2 files)
      … 2 files under this directory
  regression/  (2 files)
    fix-1930/  (2 files)
      … 2 files under this directory
  sample/  (2 files)
    sample.spec.tsx
    sample.story.tsx
src/  (9 files)
  utils/  (1 files)
    innerSliderUtils.js
  arrows.js
  default-props.js
  dots.js
  index.js
  initial-state.js
  inner-slider.js
  slider.js
  track.js
.babelrc
.eslintrc
.gitignore
.npmignore
.prettierrc
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
gulpfile.js
jest.config.js
package.json
playwright-ct.config.js
test-setup.js
test-utils.js
webpack.config.dist.js
webpack.config.js
```

## Entry points

- [playwright/index.jsx](https://github.com/akiran/react-slick/blob/97442318e9a442bd4a84eb25133ef62087f98232/playwright/index.jsx)
- [src/index.js](https://github.com/akiran/react-slick/blob/97442318e9a442bd4a84eb25133ef62087f98232/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| arrows.js package | library | Observed | Groups 1 file(s) under arrows.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| default-props.js package | library | Observed | Groups 1 file(s) under default-props.js package (observed from repository paths and static analysis). |
| dots.js package | library | Observed | Groups 1 file(s) under dots.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| initial-state.js package | library | Observed | Groups 1 file(s) under initial-state.js package (observed from repository paths and static analysis). |
| inner-slider.js package | library | Observed | Groups 1 file(s) under inner-slider.js package (observed from repository paths and static analysis). |
| playwright package | library | Observed | Groups 1 file(s) under playwright package (observed from repository paths and static analysis). |
| playwright-tests package | library | Observed | Groups 6 file(s) under playwright-tests package (observed from repository paths and static analysis). |
| slider.js package | library | Observed | Groups 1 file(s) under slider.js package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 13 file(s) under __tests__ package (observed from repository paths and static analysis). |
| track.js package | library | Observed | Groups 1 file(s) under track.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `__tests__/observations.json` (config)
- `package.json` (manifest)

## Top-level layout

- `examples` — 37 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `__tests__` — 14 analysed file(s)
- `docs` — 13 analysed file(s)
- `src` — 9 analysed file(s)
- `playwright-tests` — 6 analysed file(s)
- `.github` — 2 analysed file(s)
- `playwright` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `97442318e9a442bd4a84eb25133ef62087f98232` is the revision these paths and observations refer to.
