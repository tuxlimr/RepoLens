# Project structure: aFarkas/html5shiv

**Analysed commit:** `daa5fd1169cf8c1b63b0659754b4d13b037c0e54`

**Commit reference:** [daa5fd1169cf8c1b63b0659754b4d13b037c0e54](https://github.com/aFarkas/html5shiv/commit/daa5fd1169cf8c1b63b0659754b4d13b037c0e54)

**Tree at this commit:** [aFarkas/html5shiv@daa5fd1169cf](https://github.com/aFarkas/html5shiv/tree/daa5fd1169cf8c1b63b0659754b4d13b037c0e54)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | aFarkas/html5shiv |
| Description | This script is the defacto way to enable use of HTML5 sectioning elements in legacy Internet Explorer. |
| Stars | 9839 |
| Forks | 2491 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `daa5fd1169cf8c1b63b0659754b4d13b037c0e54` |
| Retrieved at | 2026-11-14T19:12:49.208066+00:00 |
| Files in this snapshot | 45 |

## Directory tree

```text
src/  (2 files)
  html5shiv-printshiv.js
  html5shiv.js
test/  (35 files)
  data/  (7 files)
    iframed-tests.html
    inline-mixed-media.css
    inline-print-media.css
    no-print.css
    print-styles.css
    print.css
    screen.css
  highcharts/  (2 files)
    area-basic.html
    highcharts.js
  jquery-1.7.1/  (11 files)
    data/  (7 files)
      … 7 files under this directory
    unit/  (3 files)
      … 3 files under this directory
    index.html
  qunit/  (2 files)
    qunit.css
    qunit.js
  unit/  (1 files)
    tests.js
  html5shiv.html
  iframe.1-1.html
  iframe.1-2.html
  iframe.1.html
  index.html
  mixed-test.html
  object-test.html
  perf.1.html
  perf.2.html
  style.all.css
  style.css
  style.print.css
.gitattributes
.gitignore
Gruntfile.js
MIT and GPL2 licenses.md
bower.json
composer.json
package.json
readme.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| html5shiv.js package | library | Observed | Groups 1 file(s) under html5shiv.js package (observed from repository paths and static analysis). |
| html5shiv-printshiv.js package | library | Observed | Groups 1 file(s) under html5shiv-printshiv.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `bower.json` (config)
- `composer.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 35 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `src` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `daa5fd1169cf8c1b63b0659754b4d13b037c0e54` is the revision these paths and observations refer to.
