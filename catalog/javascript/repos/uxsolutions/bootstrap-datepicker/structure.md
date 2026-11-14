# Project structure: uxsolutions/bootstrap-datepicker

**Analysed commit:** `722dc29432e89e048e5677b51fb4cfd8bbdab13c`

**Commit reference:** [722dc29432e89e048e5677b51fb4cfd8bbdab13c](https://github.com/uxsolutions/bootstrap-datepicker/commit/722dc29432e89e048e5677b51fb4cfd8bbdab13c)

**Tree at this commit:** [uxsolutions/bootstrap-datepicker@722dc29432e8](https://github.com/uxsolutions/bootstrap-datepicker/tree/722dc29432e89e048e5677b51fb4cfd8bbdab13c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | uxsolutions/bootstrap-datepicker |
| Description | A datepicker for twitter bootstrap (@twbs) |
| Stars | 12629 |
| Forks | 5837 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `722dc29432e89e048e5677b51fb4cfd8bbdab13c` |
| Retrieved at | 2026-11-14T19:12:04.608867+00:00 |
| Files in this snapshot | 165 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    ci.yaml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
docs/  (31 files)
  _screenshots/  (18 files)
    assets/  (2 files)
      … 2 files under this directory
    demo_head.html
    markup_component.html
    markup_daterange.html
    markup_inline.html
    markup_input.html
    option_calendarweeks.html
    option_clearbtn.html
    option_daysofweekdisabled.html
    option_enddate.html
    option_language.html
    option_multidate.html
    option_showweekdays.html
    option_startdate.html
    option_todaybtn.html
    option_todayhighlight.html
    option_weekstart.html
  Makefile
  README.md
  conf.py
  events.rst
  i18n.rst
  index.rst
  keyboard.rst
  make.bat
  markup.rst
  methods.rst
  options.rst
  requirements.txt
  screenshots.js
grunt/  (1 files)
  .jshintrc
js/  (89 files)
  locales/  (86 files)
    bootstrap-datepicker-en-CA.js
    bootstrap-datepicker.ar-DZ.js
    bootstrap-datepicker.ar-tn.js
    bootstrap-datepicker.ar.js
    bootstrap-datepicker.az.js
    bootstrap-datepicker.bg.js
    bootstrap-datepicker.bm.js
    bootstrap-datepicker.bn.js
    bootstrap-datepicker.br.js
    bootstrap-datepicker.bs.js
    bootstrap-datepicker.ca.js
    bootstrap-datepicker.cs.js
    bootstrap-datepicker.cy.js
    bootstrap-datepicker.da.js
    bootstrap-datepicker.de.js
    bootstrap-datepicker.el.js
    bootstrap-datepicker.en-AU.js
    bootstrap-datepicker.en-CA.js
    bootstrap-datepicker.en-GB.js
    bootstrap-datepicker.en-IE.js
    bootstrap-datepicker.en-NZ.js
    bootstrap-datepicker.en-US.js
    bootstrap-datepicker.en-ZA.js
    bootstrap-datepicker.eo.js
    … 62 more files
  .jscsrc
  .jshintrc
  bootstrap-datepicker.js
less/  (3 files)
  .csslintrc
  datepicker.less
  datepicker3.less
tests/  (27 files)
  assets/  (6 files)
    coverage.js
    mock.js
    qunit-logging.js
    qunit.css
    qunit.js
    utils.js
  suites/  (18 files)
    keyboard_navigation/  (3 files)
      … 3 files under this directory
    mouse_navigation/  (3 files)
      … 3 files under this directory
    touch_navigation/  (1 files)
      … 1 files under this directory
    calendar-weeks.js
    component.js
    data-api.js
    events.js
    formats.js
    inline.js
    methods.js
    methods_jquery.js
    noconflict.js
    options.js
    timezone.js
  README.md
  tests.html
  timezone.html
.editorconfig
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Gruntfile.js
LICENSE
README.md
bower.json
composer.json
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 87 file(s) under js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 27 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yaml` (ci)
- `bower.json` (config)
- `composer.json` (config)
- `docs/requirements.txt` (manifest)
- `package.json` (manifest)

## Top-level layout

- `js` — 89 analysed file(s)
- `docs` — 31 analysed file(s)
- `tests` — 27 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 3 analysed file(s)
- `less` — 3 analysed file(s)
- `grunt` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 14 file(s) were skipped during inventory (1 x lockfile excluded; 13 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `722dc29432e89e048e5677b51fb4cfd8bbdab13c` is the revision these paths and observations refer to.
