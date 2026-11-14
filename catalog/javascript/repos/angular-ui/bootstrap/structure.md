# Project structure: angular-ui/bootstrap

**Analysed commit:** `baf0a567f9f4641848a9a4699695f9cde5f28f70`

**Commit reference:** [baf0a567f9f4641848a9a4699695f9cde5f28f70](https://github.com/angular-ui/bootstrap/commit/baf0a567f9f4641848a9a4699695f9cde5f28f70)

**Tree at this commit:** [angular-ui/bootstrap@baf0a567f9f4](https://github.com/angular-ui/bootstrap/tree/baf0a567f9f4641848a9a4699695f9cde5f28f70)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | angular-ui/bootstrap |
| Description | PLEASE READ THE PROJECT STATUS BELOW.  Native AngularJS (Angular) directives for Bootstrap. Smaller footprint (20kB gzipped), no 3rd party JS dependencies (jQuery, bootstrap JS) required. Please read the README.md file before submitting an issue! |
| Stars | 14122 |
| Forks | 6527 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `baf0a567f9f4641848a9a4699695f9cde5f28f70` |
| Retrieved at | 2026-11-14T19:11:46.435625+00:00 |
| Files in this snapshot | 226 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
misc/  (15 files)
  demo/  (11 files)
    assets/  (10 files)
      … 10 files under this directory
    index.html
  test-lib/  (1 files)
    helpers.js
  changelog.tpl.md
  raw-files-generator.js
  validate-commit-msg.js
src/  (165 files)
  accordion/  (6 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    accordion.js
    index.js
  alert/  (6 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    alert.js
    index.js
  buttons/  (6 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    buttons.js
    index.js
  carousel/  (8 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    carousel.css
    carousel.js
    index-nocss.js
    index.js
  collapse/  (7 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (2 files)
      … 2 files under this directory
    collapse.js
    index.js
  dateparser/  (6 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    dateparser.js
    index.js
  datepicker/  (8 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    datepicker.css
    datepicker.js
    index-nocss.js
    index.js
  datepickerPopup/  (8 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index-nocss.js
    index.js
    popup.css
    popup.js
  debounce/  (3 files)
    test/  (1 files)
      … 1 files under this directory
    debounce.js
    index.js
  dropdown/  (7 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    dropdown.js
    index-nocss.js
    index.js
  isClass/  (3 files)
    test/  (1 files)
      … 1 files under this directory
    index.js
    isClass.js
  modal/  (7 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index-nocss.js
    index.js
    modal.js
  multiMap/  (3 files)
    test/  (1 files)
      … 1 files under this directory
    index.js
    multiMap.js
  pager/  (6 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    pager.js
  pagination/  (6 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    pagination.js
  paging/  (3 files)
    test/  (1 files)
      … 1 files under this directory
    index.js
    paging.js
  popover/  (9 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (3 files)
      … 3 files under this directory
    index-nocss.js
    index.js
    popover.js
  position/  (9 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (2 files)
      … 2 files under this directory
    index-nocss.js
    index.js
    position.css
    position.js
  progressbar/  (6 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    progressbar.js
  rating/  (6 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    rating.js
  stackedMap/  (3 files)
    test/  (1 files)
      … 1 files under this directory
    index.js
    stackedMap.js
  tabindex/  (3 files)
    test/  (1 files)
      … 1 files under this directory
    index.js
    tabindex.js
  tabs/  (6 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    tabs.js
  timepicker/  (8 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index-nocss.js
    index.js
    timepicker.css
    timepicker.js
  tooltip/  (10 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (3 files)
      … 3 files under this directory
    index-nocss.js
    index.js
    tooltip.css
    tooltip.js
  typeahead/  (12 files)
    docs/  (3 files)
      … 3 files under this directory
    test/  (5 files)
      … 5 files under this directory
    index-nocss.js
    index.js
    typeahead.css
    typeahead.js
template/  (28 files)
  accordion/  (2 files)
    accordion-group.html
    accordion.html
  alert/  (1 files)
    alert.html
  carousel/  (2 files)
    carousel.html
    slide.html
  datepicker/  (4 files)
    datepicker.html
    day.html
    month.html
    year.html
  datepickerPopup/  (1 files)
    popup.html
  modal/  (1 files)
    window.html
  pager/  (1 files)
    pager.html
  pagination/  (1 files)
    pagination.html
  popover/  (3 files)
    popover-html.html
    popover-template.html
    popover.html
  progressbar/  (3 files)
    bar.html
    progress.html
    progressbar.html
  rating/  (1 files)
    rating.html
  tabs/  (2 files)
    tab.html
    tabset.html
  timepicker/  (1 files)
    timepicker.html
  tooltip/  (3 files)
    tooltip-html-popup.html
    tooltip-popup.html
    tooltip-template-popup.html
  typeahead/  (2 files)
    typeahead-match.html
    typeahead-popup.html
.editorconfig
.eslintrc
.gitattributes
.gitignore
.jshintrc
.npmignore
.travis.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Gruntfile.js
LICENSE
README.md
index.js
karma.conf.js
package.json
```

## Entry points

- [index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/index.js)
- [misc/demo/assets/app.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/misc/demo/assets/app.js)
- [src/accordion/index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/src/accordion/index.js)
- [src/alert/index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/src/alert/index.js)
- [src/buttons/index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/src/buttons/index.js)
- [src/carousel/index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/src/carousel/index.js)
- [src/collapse/index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/src/collapse/index.js)
- [src/dateparser/index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/src/dateparser/index.js)
- [src/datepicker/index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/src/datepicker/index.js)
- [src/datepickerPopup/index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/src/datepickerPopup/index.js)
- [src/debounce/index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/src/debounce/index.js)
- [src/dropdown/index.js](https://github.com/angular-ui/bootstrap/blob/baf0a567f9f4641848a9a4699695f9cde5f28f70/src/dropdown/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| accordion package | library | Observed | Groups 2 file(s) under accordion package (observed from repository paths and static analysis). |
| alert package | library | Observed | Groups 2 file(s) under alert package (observed from repository paths and static analysis). |
| buttons package | library | Observed | Groups 2 file(s) under buttons package (observed from repository paths and static analysis). |
| carousel package | library | Observed | Groups 3 file(s) under carousel package (observed from repository paths and static analysis). |
| collapse package | library | Observed | Groups 2 file(s) under collapse package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| dateparser package | library | Observed | Groups 2 file(s) under dateparser package (observed from repository paths and static analysis). |
| datepicker package | library | Observed | Groups 3 file(s) under datepicker package (observed from repository paths and static analysis). |
| datepickerPopup package | library | Observed | Groups 3 file(s) under datepickerpopup package (observed from repository paths and static analysis). |
| debounce package | library | Observed | Groups 2 file(s) under debounce package (observed from repository paths and static analysis). |
| dropdown package | library | Observed | Groups 3 file(s) under dropdown package (observed from repository paths and static analysis). |
| isClass package | library | Observed | Groups 2 file(s) under isclass package (observed from repository paths and static analysis). |
| misc package | library | Observed | Groups 11 file(s) under misc package (observed from repository paths and static analysis). |
| modal package | library | Observed | Groups 3 file(s) under modal package (observed from repository paths and static analysis). |
| multiMap package | library | Observed | Groups 2 file(s) under multimap package (observed from repository paths and static analysis). |
| pager package | library | Observed | Groups 2 file(s) under pager package (observed from repository paths and static analysis). |
| pagination package | library | Observed | Groups 2 file(s) under pagination package (observed from repository paths and static analysis). |
| paging package | library | Observed | Groups 2 file(s) under paging package (observed from repository paths and static analysis). |
| popover package | library | Observed | Groups 3 file(s) under popover package (observed from repository paths and static analysis). |
| position package | library | Observed | Groups 3 file(s) under position package (observed from repository paths and static analysis). |
| progressbar package | library | Observed | Groups 2 file(s) under progressbar package (observed from repository paths and static analysis). |
| rating package | library | Observed | Groups 2 file(s) under rating package (observed from repository paths and static analysis). |
| stackedMap package | library | Observed | Groups 2 file(s) under stackedmap package (observed from repository paths and static analysis). |
| tabindex package | library | Observed | Groups 2 file(s) under tabindex package (observed from repository paths and static analysis). |
| tabs package | library | Observed | Groups 2 file(s) under tabs package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 36 file(s) under tests (observed from repository paths and static analysis). |
| timepicker package | library | Observed | Groups 3 file(s) under timepicker package (observed from repository paths and static analysis). |
| tooltip package | library | Observed | Groups 3 file(s) under tooltip package (observed from repository paths and static analysis). |
| typeahead package | library | Observed | Groups 3 file(s) under typeahead package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 165 analysed file(s)
- `template` — 28 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `misc` — 15 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `baf0a567f9f4641848a9a4699695f9cde5f28f70` is the revision these paths and observations refer to.
