# Project structure: tsayen/dom-to-image

**Analysed commit:** `fae625bce0970b3a039671ea7f338d05ecb3d0e8`

**Commit reference:** [fae625bce0970b3a039671ea7f338d05ecb3d0e8](https://github.com/tsayen/dom-to-image/commit/fae625bce0970b3a039671ea7f338d05ecb3d0e8)

**Tree at this commit:** [tsayen/dom-to-image@fae625bce097](https://github.com/tsayen/dom-to-image/tree/fae625bce0970b3a039671ea7f338d05ecb3d0e8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tsayen/dom-to-image |
| Description | Generates an image from a DOM node using HTML5 canvas |
| Stars | 10768 |
| Forks | 1670 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `fae625bce0970b3a039671ea7f338d05ecb3d0e8` |
| Retrieved at | 2026-11-14T19:12:32.906706+00:00 |
| Files in this snapshot | 220 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE.md
bower_components/  (208 files)
  fontawesome/  (32 files)
    css/  (1 files)
      … 1 files under this directory
    less/  (13 files)
      … 13 files under this directory
    scss/  (13 files)
      … 13 files under this directory
    .bower.json
    .gitignore
    .npmignore
    HELP-US-OUT.txt
    bower.json
  jquery/  (84 files)
    src/  (81 files)
      … 81 files under this directory
    .bower.json
    MIT-LICENSE.txt
    bower.json
  js-imagediff/  (21 files)
    bin/  (1 files)
      … 1 files under this directory
    browser/  (1 files)
      … 1 files under this directory
    examples/  (2 files)
      … 2 files under this directory
    js/  (2 files)
      … 2 files under this directory
    lib/  (4 files)
      … 4 files under this directory
    make/  (1 files)
      … 1 files under this directory
    spec/  (3 files)
      … 3 files under this directory
    .bower.json
    LICENSE
    Makefile
    README.md
    bower.json
    imagediff.js
    package.json
  ocrad-bower/  (71 files)
    examples/  (3 files)
      … 3 files under this directory
    ocrad-0.23-pre1/  (59 files)
      … 59 files under this directory
    .bower.json
    README.md
    bower.json
    build.sh
    demo.html
    diff.patch
    post.js
    pre.js
    worker.js
.gitattributes
.gitignore
.jsbeautifyrc
.jshintrc
.stylelintrc
.travis.yml
Gruntfile.js
LICENSE
README.md
bower.json
karma.conf.js
```

## Entry points

- [bower_components/js-imagediff/imagediff.js](https://github.com/tsayen/dom-to-image/blob/fae625bce0970b3a039671ea7f338d05ecb3d0e8/bower_components/js-imagediff/imagediff.js)
- [bower_components/js-imagediff/bin/imagediff](https://github.com/tsayen/dom-to-image/blob/fae625bce0970b3a039671ea7f338d05ecb3d0e8/bower_components/js-imagediff/bin/imagediff)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bower_components package | library | Observed | Groups 102 file(s) under bower_components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `bower.json` (config)
- `bower_components/fontawesome/.bower.json` (config)
- `bower_components/fontawesome/bower.json` (config)
- `bower_components/jquery/.bower.json` (config)
- `bower_components/jquery/bower.json` (config)
- `bower_components/js-imagediff/.bower.json` (config)
- `bower_components/js-imagediff/bower.json` (config)
- `bower_components/js-imagediff/make/build.json` (config)
- `bower_components/js-imagediff/package.json` (manifest)
- `bower_components/js-imagediff/spec/jasmine.yml` (config)
- `bower_components/ocrad-bower/.bower.json` (config)
- `bower_components/ocrad-bower/bower.json` (config)

## Top-level layout

- `bower_components` — 208 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 580 file(s) were skipped during inventory (1 x generated/minified file excluded; 579 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `fae625bce0970b3a039671ea7f338d05ecb3d0e8` is the revision these paths and observations refer to.
