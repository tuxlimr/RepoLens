# Project structure: imakewebthings/waypoints

**Analysed commit:** `34d9f6d77016cb9ed7884963c522e140fb8f8dc3`

**Commit reference:** [34d9f6d77016cb9ed7884963c522e140fb8f8dc3](https://github.com/imakewebthings/waypoints/commit/34d9f6d77016cb9ed7884963c522e140fb8f8dc3)

**Tree at this commit:** [imakewebthings/waypoints@34d9f6d77016](https://github.com/imakewebthings/waypoints/tree/34d9f6d77016cb9ed7884963c522e140fb8f8dc3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | imakewebthings/waypoints |
| Description | Waypoints is a library that makes it easy to execute a function whenever you scroll to an element. |
| Stars | 10294 |
| Forks | 1282 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `34d9f6d77016cb9ed7884963c522e140fb8f8dc3` |
| Retrieved at | 2026-11-14T19:12:41.961104+00:00 |
| Files in this snapshot | 48 |

## Directory tree

```text
lib/  (7 files)
  shortcuts/  (3 files)
    infinite.js
    inview.js
    sticky.js
  jquery.waypoints.js
  noframework.waypoints.js
  waypoints.debug.js
  zepto.waypoints.js
src/  (11 files)
  adapters/  (4 files)
    jquery-zepto-fn-extension.js
    jquery.js
    noframework.js
    zepto.js
  shortcuts/  (3 files)
    infinite.js
    inview.js
    sticky.js
  context.js
  debug.js
  group.js
  waypoint.js
test/  (19 files)
  fixtures/  (3 files)
    infinite.html
    standard.html
    sticky.html
  lib/  (7 files)
    coffee-script.js
    jasmine-html.js
    jasmine-jquery.js
    jasmine.css
    jasmine.js
    require.js
    testloader.js
  adapter-fn-spec.js
  context-spec.js
  debug-spec.js
  group-spec.js
  infinite-spec.js
  inview-spec.js
  settings.js
  sticky-spec.js
  waypoint-spec.js
.eslintrc
.gitignore
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
README.md
bower.json
gulpfile.js
licenses.txt
package.json
testem.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| context.js package | library | Observed | Groups 1 file(s) under context.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| debug.js package | library | Observed | Groups 1 file(s) under debug.js package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 4 file(s) under external integrations (observed from repository paths and static analysis). |
| group.js package | library | Observed | Groups 1 file(s) under group.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 7 file(s) under lib package (observed from repository paths and static analysis). |
| shortcuts package | library | Observed | Groups 3 file(s) under shortcuts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 19 file(s) under tests (observed from repository paths and static analysis). |
| waypoint.js package | library | Observed | Groups 1 file(s) under waypoint.js package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)
- `testem.json` (config)

## Top-level layout

- `test` — 19 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `src` — 11 analysed file(s)
- `lib` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `34d9f6d77016cb9ed7884963c522e140fb8f8dc3` is the revision these paths and observations refer to.
