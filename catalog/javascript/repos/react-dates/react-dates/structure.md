# Project structure: react-dates/react-dates

**Analysed commit:** `b7bad38dcff024d374ee98f972b55b3de9e61289`

**Commit reference:** [b7bad38dcff024d374ee98f972b55b3de9e61289](https://github.com/react-dates/react-dates/commit/b7bad38dcff024d374ee98f972b55b3de9e61289)

**Tree at this commit:** [react-dates/react-dates@b7bad38dcff0](https://github.com/react-dates/react-dates/tree/b7bad38dcff024d374ee98f972b55b3de9e61289)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-dates/react-dates |
| Description | An easily internationalizable, mobile-friendly datepicker library for the web |
| Stars | 12160 |
| Forks | 1662 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b7bad38dcff024d374ee98f972b55b3de9e61289` |
| Retrieved at | 2026-11-14T19:12:08.915307+00:00 |
| Files in this snapshot | 198 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (4 files)
    node-pretest.yml
    node.yml
    rebase.yml
    require-allow-edits.yml
.storybook/  (4 files)
  .eslintrc
  addons.js
  config.js
  webpack.config.js
.storybook-css/  (4 files)
  .eslintrc
  addons.js
  config.js
  webpack.config.js
css/  (1 files)
  storybook.scss
examples/  (6 files)
  .eslintrc
  DateRangePickerWrapper.jsx
  DayPickerRangeControllerWrapper.jsx
  DayPickerSingleDateControllerWrapper.jsx
  PresetDateRangePicker.jsx
  SingleDatePickerWrapper.jsx
scripts/  (4 files)
  .eslintrc
  buildCSS.js
  pure-component-fallback.js
  renderAllComponents.jsx
src/  (85 files)
  components/  (24 files)
    CalendarDay.jsx
    CalendarIcon.jsx
    CalendarMonth.jsx
    CalendarMonthGrid.jsx
    CalendarWeek.jsx
    ChevronDown.jsx
    ChevronUp.jsx
    CloseButton.jsx
    CustomizableCalendarDay.jsx
    DateInput.jsx
    DateRangePicker.jsx
    DateRangePickerInput.jsx
    DateRangePickerInputController.jsx
    DayPicker.jsx
    DayPickerKeyboardShortcuts.jsx
    DayPickerNavigation.jsx
    DayPickerRangeController.jsx
    DayPickerSingleDateController.jsx
    KeyboardShortcutRow.jsx
    LeftArrow.jsx
    RightArrow.jsx
    SingleDatePicker.jsx
    SingleDatePickerInput.jsx
    SingleDatePickerInputController.jsx
  shapes/  (13 files)
    AnchorDirectionShape.js
    CalendarInfoPositionShape.js
    DateRangePickerShape.js
    DayOfWeekShape.js
    DisabledShape.js
    FocusedInputShape.js
    IconPositionShape.js
    ModifiersShape.js
    NavPositionShape.js
    OpenDirectionShape.js
    OrientationShape.js
    ScrollableOrientationShape.js
    SingleDatePickerShape.js
  svg/  (6 files)
    arrow-left.svg
    arrow-right.svg
    calendar.svg
    chevron-down.svg
    chevron-up.svg
    close.svg
  theme/  (1 files)
    DefaultTheme.js
  utils/  (37 files)
    calculateDimension.js
    disableScroll.js
    getActiveElement.js
    getCalendarDaySettings.js
    getCalendarMonthWeeks.js
    getCalendarMonthWidth.js
    getDetachedContainerStyles.js
    getInputHeight.js
    getNumberOfCalendarMonthWeeks.js
    getPhrase.jsx
    getPhrasePropTypes.js
    getPooledMoment.js
    getPreviousMonthMemoLast.js
    getResponsiveContainerStyles.js
    getSelectedDateOffset.js
    getTransformStyles.js
    getVisibleDays.js
    isAfterDay.js
    isBeforeDay.js
    isDayVisible.js
    isInclusivelyAfterDay.js
    isInclusivelyBeforeDay.js
    isNextDay.js
    isNextMonth.js
    … 13 more files
  constants.js
  defaultPhrases.js
  index.js
  initialize.js
stories/  (15 files)
  .eslintrc
  DateRangePicker.js
  DateRangePicker_calendar.js
  DateRangePicker_day.js
  DateRangePicker_input.js
  DayPicker.js
  DayPickerRangeController.js
  DayPickerSingleDateController.js
  InfoPanelDecorator.js
  PresetDateRangePicker.js
  SingleDatePicker.js
  SingleDatePicker_calendar.js
  SingleDatePicker_day.js
  SingleDatePicker_input.js
  withStyles.js
test/  (57 files)
  _helpers/  (5 files)
    describeIfWindow.js
    enzymeSetup.js
    registerReactWithStylesInterface.js
    restoreSinonStubs.js
    withTouchSupport.js
  components/  (17 files)
    CalendarDay_spec.jsx
    CalendarMonthGrid_spec.jsx
    CalendarMonth_spec.jsx
    CalendarWeek_spec.jsx
    CustomizableCalendarDay_spec.jsx
    DateInput_spec.jsx
    DateRangePickerInputController_spec.jsx
    DateRangePickerInput_spec.jsx
    DateRangePicker_spec.jsx
    DayPickerKeyboardShortcuts_spec.jsx
    DayPickerNavigation_spec.jsx
    DayPickerSingleDateController_spec.jsx
    DayPicker_spec.jsx
    KeyboardShortcutRow_spec.jsx
    SingleDatePickerInputController_spec.jsx
    SingleDatePickerInput_spec.jsx
    SingleDatePicker_spec.jsx
  utils/  (33 files)
    calculateDimension_spec.js
    disableScroll_spec.js
    getActiveElement_spec.js
    getCalendarDaySettings_spec.js
    getCalendarMonthWeeks_spec.js
    getCalendarMonthWidth_spec.js
    getDetachedContainerStyles_spec.js
    getInputHeight_spec.js
    getNumberOfCalendarMonthWeeks_spec.js
    getPhrasePropTypes_spec.js
    getPhrase_spec.js
    getPooledMoment_spec.js
    getResponsiveContainerStyles_spec.js
    getSelectedDateOffset_spec.js
    getTransformStyles_spec.js
    getVisibleDays_spec.js
    isAfterDay_spec.js
    isBeforeDay_spec.js
    isDayVisible_spec.js
    isInclusivelyAfterDay_spec.js
    isInclusivelyBeforeDay_spec.js
    isNextDay_spec.js
    isNextMonth_spec.js
    isPrevMonth_spec.js
    … 9 more files
  browser-main.js
  mocha.opts
.babelrc
.eslintrc
.gitignore
.lgtm
.npmignore
.nycrc
.travis.yml
CHANGELOG.md
INTHEWILD.md
LICENSE
MAINTAINERS
README.md
constants.js
index.js
initialize.js
karma.conf.js
package.json
```

## Entry points

- [index.js](https://github.com/react-dates/react-dates/blob/b7bad38dcff024d374ee98f972b55b3de9e61289/index.js)
- [src/index.js](https://github.com/react-dates/react-dates/blob/b7bad38dcff024d374ee98f972b55b3de9e61289/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 24 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| defaultPhrases.js package | library | Observed | Groups 1 file(s) under defaultphrases.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| initialize.js package | library | Observed | Groups 1 file(s) under initialize.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| shapes package | library | Observed | Groups 13 file(s) under shapes package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 14 file(s) under stories package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 57 file(s) under tests (observed from repository paths and static analysis). |
| theme package | library | Observed | Groups 1 file(s) under theme package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 37 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/node-pretest.yml` (ci)
- `.github/workflows/node.yml` (ci)
- `.github/workflows/rebase.yml` (ci)
- `.github/workflows/require-allow-edits.yml` (ci)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 85 analysed file(s)
- `test` — 57 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `stories` — 15 analysed file(s)
- `examples` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `.storybook` — 4 analysed file(s)
- `.storybook-css` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `css` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b7bad38dcff024d374ee98f972b55b3de9e61289` is the revision these paths and observations refer to.
