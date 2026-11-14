# Project structure: clauderic/react-infinite-calendar

**Analysed commit:** `d7a77fc1508cb4ded30e47baabb111a8d6461721`

**Commit reference:** [d7a77fc1508cb4ded30e47baabb111a8d6461721](https://github.com/clauderic/react-infinite-calendar/commit/d7a77fc1508cb4ded30e47baabb111a8d6461721)

**Tree at this commit:** [clauderic/react-infinite-calendar@d7a77fc1508c](https://github.com/clauderic/react-infinite-calendar/tree/d7a77fc1508cb4ded30e47baabb111a8d6461721)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | clauderic/react-infinite-calendar |
| Description | ✨ Infinite scrolling date-picker built with React, with localization, range selection, themes, keyboard support, and more. |
| Stars | 4018 |
| Forks | 394 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d7a77fc1508cb4ded30e47baabb111a8d6461721` |
| Retrieved at | 2026-11-14T19:14:56.219690+00:00 |
| Files in this snapshot | 55 |

## Directory tree

```text
.storybook/  (3 files)
  addons.js
  config.js
  webpack.config.js
demo/  (2 files)
  src/  (2 files)
    demo.css
    index.js
examples/  (5 files)
  basic-setup.js
  keyboard-support.js
  localization.js
  range-selection.js
  with-multiple-dates.js
src/  (36 files)
  .stories/  (2 files)
    index.js
    stories.scss
  Calendar/  (6 files)
    Container.scss
    index.js
    withDateSelection.js
    withKeyboardSupport.js
    withMultipleDates.js
    withRange.js
  Day/  (2 files)
    Day.scss
    index.js
  Header/  (9 files)
    Slider/  (3 files)
      … 3 files under this directory
    Animation.scss
    Header.scss
    defaultSelectionRenderer.js
    index.js
    withMultipleDates.js
    withRange.js
  Month/  (2 files)
    Month.scss
    index.js
  MonthList/  (2 files)
    MonthList.scss
    index.js
  Today/  (2 files)
    Today.scss
    index.js
  Weekdays/  (2 files)
    Weekdays.scss
    index.js
  Years/  (2 files)
    Years.scss
    index.js
  utils/  (5 files)
    animate.js
    defaultDisplayOptions.js
    defaultLocale.js
    defaultTheme.js
    index.js
  _variables.scss
  index.js
.eslintrc
.gitignore
CONTRIBUTING.md
LICENSE
README.md
nwb.config.js
package.json
preprocess-css.js
styles.css
```

## Entry points

- [demo/src/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/demo/src/index.js)
- [src/.stories/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/.stories/index.js)
- [src/Calendar/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/Calendar/index.js)
- [src/Day/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/Day/index.js)
- [src/Header/Slider/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/Header/Slider/index.js)
- [src/Header/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/Header/index.js)
- [src/Month/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/Month/index.js)
- [src/MonthList/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/MonthList/index.js)
- [src/Today/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/Today/index.js)
- [src/Weekdays/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/Weekdays/index.js)
- [src/Years/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/Years/index.js)
- [src/index.js](https://github.com/clauderic/react-infinite-calendar/blob/d7a77fc1508cb4ded30e47baabb111a8d6461721/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Calendar package | library | Observed | Groups 5 file(s) under calendar package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Day package | library | Observed | Groups 1 file(s) under day package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 1 file(s) under demo package (observed from repository paths and static analysis). |
| Header package | library | Observed | Groups 5 file(s) under header package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Month package | library | Observed | Groups 1 file(s) under month package (observed from repository paths and static analysis). |
| MonthList package | library | Observed | Groups 1 file(s) under monthlist package (observed from repository paths and static analysis). |
| .stories package | library | Observed | Groups 1 file(s) under .stories package (observed from repository paths and static analysis). |
| Today package | library | Observed | Groups 1 file(s) under today package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |
| Weekdays package | library | Observed | Groups 1 file(s) under weekdays package (observed from repository paths and static analysis). |
| Years package | library | Observed | Groups 1 file(s) under years package (observed from repository paths and static analysis). |

## Important files

- `package.json` (manifest)

## Top-level layout

- `src` — 36 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `examples` — 5 analysed file(s)
- `.storybook` — 3 analysed file(s)
- `demo` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d7a77fc1508cb4ded30e47baabb111a8d6461721` is the revision these paths and observations refer to.
