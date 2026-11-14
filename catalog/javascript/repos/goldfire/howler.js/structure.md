# Project structure: goldfire/howler.js

**Analysed commit:** `1d3053576a860e9854645493ad6c4a72c6cc6e45`

**Commit reference:** [1d3053576a860e9854645493ad6c4a72c6cc6e45](https://github.com/goldfire/howler.js/commit/1d3053576a860e9854645493ad6c4a72c6cc6e45)

**Tree at this commit:** [goldfire/howler.js@1d3053576a86](https://github.com/goldfire/howler.js/tree/1d3053576a860e9854645493ad6c4a72c6cc6e45)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | goldfire/howler.js |
| Description | Javascript audio library for the modern web. |
| Stars | 25445 |
| Forks | 2281 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `1d3053576a860e9854645493ad6c4a72c6cc6e45` |
| Retrieved at | 2026-11-14T19:11:02.019128+00:00 |
| Files in this snapshot | 46 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (4 files)
    bug.yml
    config.yml
    docs.yml
    feature.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
examples/  (24 files)
  3d/  (10 files)
    js/  (7 files)
      … 7 files under this directory
    README.md
    index.html
    styles.css
  player/  (5 files)
    README.md
    index.html
    player.js
    siriwave.js
    styles.css
  radio/  (4 files)
    README.md
    index.html
    radio.js
    styles.css
  sprite/  (4 files)
    README.md
    index.html
    sprite.js
    styles.css
  README.md
src/  (2 files)
  plugins/  (1 files)
    howler.spatial.js
  howler.core.js
tests/  (8 files)
  css/  (1 files)
    styles.css
  js/  (3 files)
    core.html5audio.js
    core.webaudio.js
    spatial.js
  core.html5audio.html
  core.webaudio.html
  index.html
  spatial.html
BACKERS.md
CHANGELOG.md
LICENSE.md
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
| howler.core.js package | library | Observed | Groups 1 file(s) under howler.core.js package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 1 file(s) under plugins package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/docs.yml` (config)
- `.github/ISSUE_TEMPLATE/feature.yml` (config)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `examples` — 24 analysed file(s)
- `tests` — 8 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 6 analysed file(s)
- `src` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1d3053576a860e9854645493ad6c4a72c6cc6e45` is the revision these paths and observations refer to.
