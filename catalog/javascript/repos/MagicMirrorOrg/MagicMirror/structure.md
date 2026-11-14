# Project structure: MagicMirrorOrg/MagicMirror

**Analysed commit:** `f138f5b690ceab6450f55c852ac81d268363f563`

**Commit reference:** [f138f5b690ceab6450f55c852ac81d268363f563](https://github.com/MagicMirrorOrg/MagicMirror/commit/f138f5b690ceab6450f55c852ac81d268363f563)

**Tree at this commit:** [MagicMirrorOrg/MagicMirror@f138f5b690ce](https://github.com/MagicMirrorOrg/MagicMirror/tree/f138f5b690ceab6450f55c852ac81d268363f563)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | MagicMirrorOrg/MagicMirror |
| Description | MagicMirror² is an open source modular smart mirror platform. With a growing list of installable modules, the MagicMirror² allows you to convert your hallway or bathroom mirror into your personal assistant. |
| Stars | 24204 |
| Forks | 4576 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f138f5b690ceab6450f55c852ac81d268363f563` |
| Retrieved at | 2026-11-14T19:11:03.085962+00:00 |
| Files in this snapshot | 455 |

## Directory tree

```text
.github/  (18 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    change_request.yml
    config.yml
    feature_request.yml
  workflows/  (8 files)
    automated-tests.yaml
    codeql.yaml
    dep-review.yaml
    electron-rebuild.yaml
    enforce-pullrequest-rules.yaml
    release-notes.yaml
    spellcheck.yaml
    stale.yaml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yaml
  PULL_REQUEST_TEMPLATE.md
  SECURITY.md
  dependabot.yaml
.husky/  (1 files)
  pre-commit
clientonly/  (1 files)
  index.js
config/  (2 files)
  config.js.sample
  custom.css.sample
css/  (3 files)
  font-awesome.css
  main.css
  roboto.css
defaultmodules/  (80 files)
  alert/  (9 files)
    styles/  (4 files)
      … 4 files under this directory
    templates/  (2 files)
      … 2 files under this directory
    README.md
    alert.js
    notificationFx.mjs
  calendar/  (9 files)
    README.md
    calendar.css
    calendar.js
    calendarfetcher.js
    calendarfetcherutils.js
    calendarutils.js
    debug.js
    node_helper.js
    windowsZones.json
  clock/  (15 files)
    faces/  (12 files)
      … 12 files under this directory
    README.md
    clock.js
    clock_styles.css
  compliments/  (2 files)
    README.md
    compliments.js
  helloworld/  (3 files)
    README.md
    helloworld.js
    helloworld.njk
  newsfeed/  (8 files)
    README.md
    feeditem.js
    newsfeed.css
    newsfeed.js
    newsfeed.njk
    newsfeedfetcher.js
    node_helper.js
    oldconfig.njk
  updatenotification/  (7 files)
    README.md
    git_helper.js
    node_helper.js
    update_helper.js
    updatenotification.css
    updatenotification.js
    updatenotification.njk
  weather/  (25 files)
    providers/  (14 files)
      … 14 files under this directory
    README.md
    current.njk
    forecast.njk
    hourly.njk
    node_helper.js
    provider-utils.js
    weather.css
    weather.js
    weatherobject.js
    weatherprovider.js
    weatherutils.js
  defaultmodules.js
  utils.js
js/  (24 files)
  alias-resolver.js
  animateCSS.js
  app.js
  check_config.js
  defaults.js
  deprecated.js
  electron.js
  electron_helper.js
  http_fetcher.js
  ip_access_control.js
  loader.js
  logger.js
  main.js
  module.js
  node_helper.js
  releasenotes.js
  server.js
  server_functions.js
  socketclient.js
  suncalc-global.mjs
  systeminformation.js
  translator.js
  utils.js
  vendor.js
modules/  (1 files)
  .gitkeep
serveronly/  (2 files)
  index.js
  watcher.js
tests/  (257 files)
  configs/  (107 files)
    modules/  (98 files)
      … 98 files under this directory
    config_functions.js
    config_variables.env
    config_variables.js
    customregions.js
    default.js
    empty_ipWhiteList.js
    noIpWhiteList.js
    port_8090.js
    without_modules.js
  e2e/  (30 files)
    helpers/  (3 files)
      … 3 files under this directory
    modules/  (12 files)
      … 12 files under this directory
    animateCSS_spec.js
    clientonly_spec.js
    config_functions_spec.js
    config_variables_spec.js
    custom_module_regions_spec.js
    env_spec.js
    fonts_spec.js
    ipWhitelist_spec.js
    modules_display_spec.js
    modules_empty_spec.js
    modules_position_spec.js
    port_spec.js
    serveronly_spec.js
    translations_spec.js
    vendor_spec.js
  electron/  (6 files)
    helpers/  (2 files)
      … 2 files under this directory
    modules/  (3 files)
      … 3 files under this directory
    env_spec.js
  mocks/  (68 files)
    testNotification/  (1 files)
      … 1 files under this directory
    12_events.ics
    3_move_first_allday_repeating_event.ics
    RepeatingEvent.Oct21.ics
    bad_rrule.ics
    calendar_duplicates_1.ics
    calendar_duplicates_2.ics
    calendar_test.ics
    calendar_test_clone.ics
    calendar_test_empty_day.ics
    calendar_test_full_day_events.ics
    calendar_test_icons.ics
    calendar_test_multi_day_starting_today.ics
    calendar_test_recurring.ics
    calendar_test_slice_multiday_ends_midnight.ics
    calendar_test_slice_multiday_timed.ics
    chicago-nyedge.ics
    chicago_late_in_timezone.ics
    compliments_file.json
    compliments_test.json
    diff_tz_start_end.ics
    end_of_day_berlin_moved.ics
    event_with_time_over_multiple_days_non_repeating.ics
    event_with_time_over_multiple_days_yearly.ics
    event_with_time_same_day_yearly.ics
    … 43 more files
  unit/  (44 files)
    classes/  (5 files)
      … 5 files under this directory
    functions/  (8 files)
      … 8 files under this directory
    global_vars/  (2 files)
      … 2 files under this directory
    modules/  (29 files)
      … 29 files under this directory
  utils/  (2 files)
    translation_test_environment.js
    vitest-setup.js
translations/  (49 files)
  af.json
  ar.json
  az.json
  bg.json
  ca.json
  cs.json
  cv.json
  cy.json
  da.json
  de.json
  el.json
  en.json
  eo.json
  es.json
  et.json
  fi.json
  fr.json
  fy.json
  gl.json
  gu.json
  he.json
  hi.json
  hr.json
  hu.json
  … 25 more files
.editorconfig
.gitattributes
.gitignore
.prettierignore
CHANGELOG.md
Collaboration.md
LICENSE.md
README.md
cspell.config.json
eslint.config.mjs
favicon.svg
index.html
jsconfig.json
module-types.ts
package.json
prettier.config.mjs
vitest.config.mjs
```

## Entry points

- [js/electron.js](https://github.com/MagicMirrorOrg/MagicMirror/blob/f138f5b690ceab6450f55c852ac81d268363f563/js/electron.js)
- [clientonly/index.js](https://github.com/MagicMirrorOrg/MagicMirror/blob/f138f5b690ceab6450f55c852ac81d268363f563/clientonly/index.js)
- [js/app.js](https://github.com/MagicMirrorOrg/MagicMirror/blob/f138f5b690ceab6450f55c852ac81d268363f563/js/app.js)
- [js/main.js](https://github.com/MagicMirrorOrg/MagicMirror/blob/f138f5b690ceab6450f55c852ac81d268363f563/js/main.js)
- [js/server.js](https://github.com/MagicMirrorOrg/MagicMirror/blob/f138f5b690ceab6450f55c852ac81d268363f563/js/server.js)
- [serveronly/index.js](https://github.com/MagicMirrorOrg/MagicMirror/blob/f138f5b690ceab6450f55c852ac81d268363f563/serveronly/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| clientonly package | library | Observed | Groups 1 file(s) under clientonly package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 52 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| defaultmodules package | library | Observed | Groups 40 file(s) under defaultmodules package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 24 file(s) under js package (observed from repository paths and static analysis). |
| serveronly package | library | Observed | Groups 2 file(s) under serveronly package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 257 file(s) under tests (observed from repository paths and static analysis). |
| translations package | library | Observed | Groups 1 file(s) under translations package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yaml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/change_request.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yaml` (config)
- `.github/workflows/automated-tests.yaml` (ci)
- `.github/workflows/codeql.yaml` (ci)
- `.github/workflows/dep-review.yaml` (ci)
- `.github/workflows/electron-rebuild.yaml` (ci)
- `.github/workflows/enforce-pullrequest-rules.yaml` (ci)
- `.github/workflows/release-notes.yaml` (ci)
- `.github/workflows/spellcheck.yaml` (ci)
- `.github/workflows/stale.yaml` (ci)
- `cspell.config.json` (config)
- `defaultmodules/calendar/windowsZones.json` (config)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `translations/af.json` (config)
- `translations/ar.json` (config)
- `translations/az.json` (config)
- `translations/bg.json` (config)
- `translations/ca.json` (config)
- `translations/cs.json` (config)
- `translations/cv.json` (config)
- `translations/cy.json` (config)
- `translations/da.json` (config)
- `translations/de.json` (config)
- `translations/el.json` (config)
- `translations/en.json` (config)
- `translations/eo.json` (config)
- `translations/es.json` (config)
- `translations/et.json` (config)
- `translations/fi.json` (config)
- `translations/fr.json` (config)
- `translations/fy.json` (config)
- `translations/gl.json` (config)
- `translations/gu.json` (config)
- `translations/he.json` (config)
- `translations/hi.json` (config)
- `translations/hr.json` (config)
- `translations/hu.json` (config)
- `translations/id.json` (config)
- `translations/is.json` (config)
- `translations/it.json` (config)
- `translations/ja.json` (config)
- `translations/ko.json` (config)
- `translations/lt.json` (config)
- `translations/ms-my.json` (config)
- `translations/nb.json` (config)
- `translations/nl.json` (config)
- `translations/nn.json` (config)
- `translations/pl.json` (config)
- `translations/ps.json` (config)
- `translations/pt-br.json` (config)
- `translations/pt.json` (config)
- `translations/ro.json` (config)
- `translations/ru.json` (config)
- `translations/sk.json` (config)
- `translations/sv.json` (config)
- `translations/th.json` (config)
- `translations/tlh.json` (config)
- `translations/tr.json` (config)
- `translations/uk.json` (config)
- `translations/zh-cn.json` (config)
- `translations/zh-tw.json` (config)

## Top-level layout

- `tests` — 257 analysed file(s)
- `defaultmodules` — 80 analysed file(s)
- `translations` — 49 analysed file(s)
- `js` — 24 analysed file(s)
- `.github` — 18 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `css` — 3 analysed file(s)
- `config` — 2 analysed file(s)
- `serveronly` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `clientonly` — 1 analysed file(s)
- `modules` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f138f5b690ceab6450f55c852ac81d268363f563` is the revision these paths and observations refer to.
