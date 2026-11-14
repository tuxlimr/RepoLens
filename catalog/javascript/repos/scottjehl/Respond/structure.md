# Project structure: scottjehl/Respond

**Analysed commit:** `9d91fd47eb59c11a80d570d4ea0beaa59cfc71bf`

**Commit reference:** [9d91fd47eb59c11a80d570d4ea0beaa59cfc71bf](https://github.com/scottjehl/Respond/commit/9d91fd47eb59c11a80d570d4ea0beaa59cfc71bf)

**Tree at this commit:** [scottjehl/Respond@9d91fd47eb59](https://github.com/scottjehl/Respond/tree/9d91fd47eb59c11a80d570d4ea0beaa59cfc71bf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | scottjehl/Respond |
| Description | A fast & lightweight polyfill for min/max-width CSS3 Media Queries (for IE 6-8, and more) |
| Stars | 11180 |
| Forks | 3241 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9d91fd47eb59c11a80d570d4ea0beaa59cfc71bf` |
| Retrieved at | 2026-11-14T19:12:24.873046+00:00 |
| Files in this snapshot | 28 |

## Directory tree

```text
cross-domain/  (4 files)
  example-base.html
  example.html
  respond-proxy.html
  respond.proxy.js
dest/  (2 files)
  respond.matchmedia.addListener.src.js
  respond.src.js
src/  (3 files)
  matchmedia.addListener.js
  matchmedia.polyfill.js
  respond.js
test/  (13 files)
  unit/  (10 files)
    qunit/  (2 files)
      … 2 files under this directory
    index.html
    test-with-comment.css
    test-with-dpr.css
    test-with-keyframe.css
    test.css
    test2.css
    test3.css
    tests.js
  test.css
  test.html
  test2.css
.gitignore
Gruntfile.js
LICENSE-MIT
README.md
bower.json
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| cross-domain package | library | Observed | Groups 1 file(s) under cross-domain package (observed from repository paths and static analysis). |
| dest package | library | Observed | Groups 2 file(s) under dest package (observed from repository paths and static analysis). |
| matchmedia.addListener.js package | library | Observed | Groups 1 file(s) under matchmedia.addlistener.js package (observed from repository paths and static analysis). |
| matchmedia.polyfill.js package | library | Observed | Groups 1 file(s) under matchmedia.polyfill.js package (observed from repository paths and static analysis). |
| respond.js package | library | Observed | Groups 1 file(s) under respond.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 13 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 13 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `cross-domain` — 4 analysed file(s)
- `src` — 3 analysed file(s)
- `dest` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `9d91fd47eb59c11a80d570d4ea0beaa59cfc71bf` is the revision these paths and observations refer to.
