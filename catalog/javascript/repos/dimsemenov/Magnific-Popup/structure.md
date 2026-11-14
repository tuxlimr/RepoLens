# Project structure: dimsemenov/Magnific-Popup

**Analysed commit:** `45dd72ccd1a18f0626fb958f7c49e6313556d31f`

**Commit reference:** [45dd72ccd1a18f0626fb958f7c49e6313556d31f](https://github.com/dimsemenov/Magnific-Popup/commit/45dd72ccd1a18f0626fb958f7c49e6313556d31f)

**Tree at this commit:** [dimsemenov/Magnific-Popup@45dd72ccd1a1](https://github.com/dimsemenov/Magnific-Popup/tree/45dd72ccd1a18f0626fb958f7c49e6313556d31f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dimsemenov/Magnific-Popup |
| Description | Light and responsive lightbox script with focus on performance. |
| Stars | 11295 |
| Forks | 3333 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `45dd72ccd1a18f0626fb958f7c49e6313556d31f` |
| Retrieved at | 2026-11-14T19:12:19.914326+00:00 |
| Files in this snapshot | 36 |

## Directory tree

```text
libs/  (3 files)
  qunit/  (2 files)
    qunit.css
    qunit.js
  jquery-loader.js
src/  (10 files)
  css/  (2 files)
    _settings.scss
    main.scss
  js/  (8 files)
    ajax.js
    core.js
    gallery.js
    iframe.js
    image.js
    inline.js
    retina.js
    zoom.js
website/  (13 files)
  _includes/  (4 files)
    analytics.html
    examples.html
    logo.html
    signup.html
  _layouts/  (1 files)
    default.html
  site-assets/  (3 files)
    ajax/  (2 files)
      … 2 files under this directory
    site.css
  third-party-libs/  (2 files)
    uglify.js
    zepto.js
  documentation.md
  index.html
  wordpress.html
.gitignore
.jshintrc
.travis.yml
Gruntfile.js
LICENSE
README.md
bower.json
composer.json
magnific-popup.jquery.json
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 8 file(s) under js package (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 2 file(s) under libs package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 2 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `bower.json` (config)
- `composer.json` (config)
- `magnific-popup.jquery.json` (config)
- `package.json` (manifest)

## Top-level layout

- `website` — 13 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `src` — 10 analysed file(s)
- `libs` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `45dd72ccd1a18f0626fb958f7c49e6313556d31f` is the revision these paths and observations refer to.
