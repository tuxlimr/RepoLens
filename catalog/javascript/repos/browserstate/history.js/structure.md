# Project structure: browserstate/history.js

**Analysed commit:** `8e4c08323f4db50742a54cb276f6f377343dcdd2`

**Commit reference:** [8e4c08323f4db50742a54cb276f6f377343dcdd2](https://github.com/browserstate/history.js/commit/8e4c08323f4db50742a54cb276f6f377343dcdd2)

**Tree at this commit:** [browserstate/history.js@8e4c08323f4d](https://github.com/browserstate/history.js/tree/8e4c08323f4db50742a54cb276f6f377343dcdd2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | browserstate/history.js |
| Description | History.js gracefully supports the HTML5 History/State APIs (pushState, replaceState, onPopState) in all browsers. Including continued support for data, titles, replaceState. Supports jQuery, MooTools and Prototype.  For HTML5 browsers this means that you can modify the URL directly, without needin… |
| Stars | 10640 |
| Forks | 1295 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `8e4c08323f4db50742a54cb276f6f377343dcdd2` |
| Retrieved at | 2026-11-14T19:12:35.179064+00:00 |
| Files in this snapshot | 89 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
demo/  (9 files)
  bcherry-orig.html
  bcherry.html
  chrome.html
  index.html
  native-auto.html
  native.html
  navigator.html
  safari.html
  unicode.html
scripts/  (48 files)
  bundled/  (14 files)
    html4+html5/  (7 files)
      … 7 files under this directory
    html5/  (7 files)
      … 7 files under this directory
  bundled-uncompressed/  (14 files)
    html4+html5/  (7 files)
      … 7 files under this directory
    html5/  (7 files)
      … 7 files under this directory
  compressed/  (10 files)
    history.adapter.dojo.js
    history.adapter.extjs.js
    history.adapter.jquery.js
    history.adapter.mootools.js
    history.adapter.native.js
    history.adapter.right.js
    history.adapter.zepto.js
    history.html4.js
    history.js
    json2.js
  uncompressed/  (10 files)
    history.adapter.dojo.js
    history.adapter.extjs.js
    history.adapter.jquery.js
    history.adapter.mootools.js
    history.adapter.native.js
    history.adapter.right.js
    history.adapter.zepto.js
    history.html4.js
    history.js
    json2.js
tests/  (18 files)
  .htaccess
  html4+html5.dojo.html
  html4+html5.extjs.html
  html4+html5.jquery.html
  html4+html5.mootools.html
  html4+html5.native.html
  html4+html5.right.html
  html4+html5.zepto.html
  html5.dojo.html
  html5.extjs.html
  html5.jquery.html
  html5.mootools.html
  html5.native.html
  html5.right.html
  html5.zepto.html
  image.php
  index.html
  tests.js
tests.src/  (4 files)
  _header.php
  all.php
  each.php
  index.php
.gitignore
HISTORY.md
LICENSE.md
README.md
bower.json
buildr-uncompressed.coffee
buildr.coffee
component.json
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 48 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |
| tests.src package | library | Observed | Groups 4 file(s) under tests.src package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `bower.json` (config)
- `component.json` (config)
- `package.json` (manifest)

## Top-level layout

- `scripts` — 48 analysed file(s)
- `tests` — 18 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `demo` — 9 analysed file(s)
- `tests.src` — 4 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 26 file(s) were skipped during inventory (26 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8e4c08323f4db50742a54cb276f6f377343dcdd2` is the revision these paths and observations refer to.
