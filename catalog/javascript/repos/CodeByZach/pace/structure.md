# Project structure: CodeByZach/pace

**Analysed commit:** `eb7d40c547968c053db902b429aaf35de08d1181`

**Commit reference:** [eb7d40c547968c053db902b429aaf35de08d1181](https://github.com/CodeByZach/pace/commit/eb7d40c547968c053db902b429aaf35de08d1181)

**Tree at this commit:** [CodeByZach/pace@eb7d40c54796](https://github.com/CodeByZach/pace/tree/eb7d40c547968c053db902b429aaf35de08d1181)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | CodeByZach/pace |
| Description | Automatically add a progress bar to your site. |
| Stars | 15582 |
| Forks | 1831 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `eb7d40c547968c053db902b429aaf35de08d1181` |
| Retrieved at | 2026-11-14T19:11:36.588592+00:00 |
| Files in this snapshot | 192 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (4 files)
    actions.lock
    checks.yml
    deploy-site.yml
    publish-npm.yml
scripts/  (2 files)
  build.mjs
  color.mjs
site/  (4 files)
  assets/  (2 files)
    css/  (1 files)
      … 1 files under this directory
    js/  (1 files)
      … 1 files under this directory
  docs/  (1 files)
    index.html
  index.html
templates/  (15 files)
  pace-theme-barber-shop.tmpl.css
  pace-theme-big-counter.tmpl.css
  pace-theme-bounce.tmpl.css
  pace-theme-center-atom.tmpl.css
  pace-theme-center-circle.tmpl.css
  pace-theme-center-radar.tmpl.css
  pace-theme-center-simple.tmpl.css
  pace-theme-corner-indicator.tmpl.css
  pace-theme-fill-left.tmpl.css
  pace-theme-flash.tmpl.css
  pace-theme-flat-top.tmpl.css
  pace-theme-loading-bar.tmpl.css
  pace-theme-mac-osx.tmpl.css
  pace-theme-material.tmpl.css
  pace-theme-minimal.tmpl.css
tests/  (5 files)
  ajax.spec.mjs
  contract.spec.mjs
  fixtures.mjs
  navigation.spec.mjs
  security.spec.mjs
themes/  (150 files)
  black/  (15 files)
    pace-theme-barber-shop.css
    pace-theme-big-counter.css
    pace-theme-bounce.css
    pace-theme-center-atom.css
    pace-theme-center-circle.css
    pace-theme-center-radar.css
    pace-theme-center-simple.css
    pace-theme-corner-indicator.css
    pace-theme-fill-left.css
    pace-theme-flash.css
    pace-theme-flat-top.css
    pace-theme-loading-bar.css
    pace-theme-mac-osx.css
    pace-theme-material.css
    pace-theme-minimal.css
  blue/  (15 files)
    pace-theme-barber-shop.css
    pace-theme-big-counter.css
    pace-theme-bounce.css
    pace-theme-center-atom.css
    pace-theme-center-circle.css
    pace-theme-center-radar.css
    pace-theme-center-simple.css
    pace-theme-corner-indicator.css
    pace-theme-fill-left.css
    pace-theme-flash.css
    pace-theme-flat-top.css
    pace-theme-loading-bar.css
    pace-theme-mac-osx.css
    pace-theme-material.css
    pace-theme-minimal.css
  green/  (15 files)
    pace-theme-barber-shop.css
    pace-theme-big-counter.css
    pace-theme-bounce.css
    pace-theme-center-atom.css
    pace-theme-center-circle.css
    pace-theme-center-radar.css
    pace-theme-center-simple.css
    pace-theme-corner-indicator.css
    pace-theme-fill-left.css
    pace-theme-flash.css
    pace-theme-flat-top.css
    pace-theme-loading-bar.css
    pace-theme-mac-osx.css
    pace-theme-material.css
    pace-theme-minimal.css
  orange/  (15 files)
    pace-theme-barber-shop.css
    pace-theme-big-counter.css
    pace-theme-bounce.css
    pace-theme-center-atom.css
    pace-theme-center-circle.css
    pace-theme-center-radar.css
    pace-theme-center-simple.css
    pace-theme-corner-indicator.css
    pace-theme-fill-left.css
    pace-theme-flash.css
    pace-theme-flat-top.css
    pace-theme-loading-bar.css
    pace-theme-mac-osx.css
    pace-theme-material.css
    pace-theme-minimal.css
  pink/  (15 files)
    pace-theme-barber-shop.css
    pace-theme-big-counter.css
    pace-theme-bounce.css
    pace-theme-center-atom.css
    pace-theme-center-circle.css
    pace-theme-center-radar.css
    pace-theme-center-simple.css
    pace-theme-corner-indicator.css
    pace-theme-fill-left.css
    pace-theme-flash.css
    pace-theme-flat-top.css
    pace-theme-loading-bar.css
    pace-theme-mac-osx.css
    pace-theme-material.css
    pace-theme-minimal.css
  purple/  (15 files)
    pace-theme-barber-shop.css
    pace-theme-big-counter.css
    pace-theme-bounce.css
    pace-theme-center-atom.css
    pace-theme-center-circle.css
    pace-theme-center-radar.css
    pace-theme-center-simple.css
    pace-theme-corner-indicator.css
    pace-theme-fill-left.css
    pace-theme-flash.css
    pace-theme-flat-top.css
    pace-theme-loading-bar.css
    pace-theme-mac-osx.css
    pace-theme-material.css
    pace-theme-minimal.css
  red/  (15 files)
    pace-theme-barber-shop.css
    pace-theme-big-counter.css
    pace-theme-bounce.css
    pace-theme-center-atom.css
    pace-theme-center-circle.css
    pace-theme-center-radar.css
    pace-theme-center-simple.css
    pace-theme-corner-indicator.css
    pace-theme-fill-left.css
    pace-theme-flash.css
    pace-theme-flat-top.css
    pace-theme-loading-bar.css
    pace-theme-mac-osx.css
    pace-theme-material.css
    pace-theme-minimal.css
  silver/  (15 files)
    pace-theme-barber-shop.css
    pace-theme-big-counter.css
    pace-theme-bounce.css
    pace-theme-center-atom.css
    pace-theme-center-circle.css
    pace-theme-center-radar.css
    pace-theme-center-simple.css
    pace-theme-corner-indicator.css
    pace-theme-fill-left.css
    pace-theme-flash.css
    pace-theme-flat-top.css
    pace-theme-loading-bar.css
    pace-theme-mac-osx.css
    pace-theme-material.css
    pace-theme-minimal.css
  white/  (15 files)
    pace-theme-barber-shop.css
    pace-theme-big-counter.css
    pace-theme-bounce.css
    pace-theme-center-atom.css
    pace-theme-center-circle.css
    pace-theme-center-radar.css
    pace-theme-center-simple.css
    pace-theme-corner-indicator.css
    pace-theme-fill-left.css
    pace-theme-flash.css
    pace-theme-flat-top.css
    pace-theme-loading-bar.css
    pace-theme-mac-osx.css
    pace-theme-material.css
    pace-theme-minimal.css
  yellow/  (15 files)
    pace-theme-barber-shop.css
    pace-theme-big-counter.css
    pace-theme-bounce.css
    pace-theme-center-atom.css
    pace-theme-center-circle.css
    pace-theme-center-radar.css
    pace-theme-center-simple.css
    pace-theme-corner-indicator.css
    pace-theme-fill-left.css
    pace-theme-flash.css
    pace-theme-flat-top.css
    pace-theme-loading-bar.css
    pace-theme-mac-osx.css
    pace-theme-material.css
    pace-theme-minimal.css
.editorconfig
.git-blame-ignore-revs
.gitattributes
.gitignore
.tool-versions
LICENSE
README.md
SECURITY.md
pace-theme-default.css
pace.js
package.json
playwright.config.mjs
```

## Entry points

- [pace.js](https://github.com/CodeByZach/pace/blob/eb7d40c547968c053db902b429aaf35de08d1181/pace.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 1 file(s) under site package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/actions.lock` (ci)
- `.github/workflows/checks.yml` (ci)
- `.github/workflows/deploy-site.yml` (ci)
- `.github/workflows/publish-npm.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `themes` — 150 analysed file(s)
- `templates` — 15 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `tests` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `site` — 4 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x generated/minified file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `eb7d40c547968c053db902b429aaf35de08d1181` is the revision these paths and observations refer to.
