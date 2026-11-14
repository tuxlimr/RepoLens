# Project structure: piskelapp/piskel

**Analysed commit:** `e394f4fd3b382a0412aab078d1b88b2899d3b8ea`

**Commit reference:** [e394f4fd3b382a0412aab078d1b88b2899d3b8ea](https://github.com/piskelapp/piskel/commit/e394f4fd3b382a0412aab078d1b88b2899d3b8ea)

**Tree at this commit:** [piskelapp/piskel@e394f4fd3b38](https://github.com/piskelapp/piskel/tree/e394f4fd3b382a0412aab078d1b88b2899d3b8ea)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | piskelapp/piskel |
| Description | A simple web-based tool for Spriting and Pixel art. |
| Stars | 12987 |
| Forks | 937 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e394f4fd3b382a0412aab078d1b88b2899d3b8ea` |
| Retrieved at | 2026-11-14T19:12:02.212777+00:00 |
| Files in this snapshot | 547 |

## Directory tree

```text
.claude/  (1 files)
  skills/  (1 files)
    e2e-tests/  (1 files)
      … 1 files under this directory
.github/  (3 files)
  workflows/  (2 files)
    ci.yml
    update-visual-baselines.yml
  ISSUE_TEMPLATE
.husky/  (1 files)
  pre-commit
TODO/  (2 files)
  clarify-layer-opacity-preference.md
  fix-clock-going-backwards.md
bin/  (2 files)
  copy-to-piskel-web.js
  copy-to-piskel-website.js
cli/  (4 files)
  README.md
  export-png.js
  index.js
  piskel-export.js
docs/  (18 files)
  specs/  (17 files)
    README.md
    canvas.md
    colors-and-palettes.md
    drawing-tools.md
    editor.md
    export.md
    frames.md
    import.md
    keyboard-shortcuts.md
    layers.md
    preview.md
    save-and-storage.md
    selection.md
    settings.md
    transformations.md
    undo-redo.md
    untested.txt
  known-issues.md
misc/  (79 files)
  desktop/  (1 files)
    Info.plist
  gif-tests/  (4 files)
    low-colors-no-transparency.piskel
    low-colors-with-transparency.piskel
    too-many-colors-no-transparency.piskel
    too-many-colors-with-transparency.piskel
  icons/  (63 files)
    SVG/  (8 files)
      … 8 files under this directory
    cleaned_svg/  (16 files)
      … 16 files under this directory
    noun-project/  (4 files)
      … 4 files under this directory
    source/  (35 files)
      … 35 files under this directory
  proto-ui-1/  (3 files)
    index.html
    main.css
    main.js
  scripts/  (4 files)
    build-mac-application.txt
    package-mac-application.cmd
    package-windows-executable.cmd
    piskel-root
  selenium-ide/  (4 files)
    change-colors.html
    change-size.html
    select-tools.html
    user-preferences.html
scripts/  (6 files)
  desktop.js
  partials.js
  serve.js
  spec-check.js
  sprite.js
  visual-storyboard.js
src/  (280 files)
  css/  (43 files)
    bootstrap/  (3 files)
      … 3 files under this directory
    fonts/  (2 files)
      … 2 files under this directory
    spectrum/  (2 files)
      … 2 files under this directory
    animations.css
    color-picker-slider.css
    dialogs-browse-backups.css
    dialogs-browse-local.css
    dialogs-cheatsheet.css
    dialogs-create-palette.css
    dialogs-import.css
    dialogs-performance-info.css
    dialogs-unsupported-browser.css
    dialogs.css
    font-icon.css
    forms.css
    frames-list.css
    layout.css
    minimap.css
    notifications.css
    reset.css
    settings-application.css
    settings-export.css
    settings-import.css
    settings-resize.css
    settings-save.css
    settings.css
    style.css
    … 12 more files
  js/  (203 files)
    controller/  (52 files)
      … 52 files under this directory
    database/  (3 files)
      … 3 files under this directory
    lib/  (9 files)
      … 9 files under this directory
    model/  (8 files)
      … 8 files under this directory
    rendering/  (11 files)
      … 11 files under this directory
    selection/  (5 files)
      … 5 files under this directory
    service/  (33 files)
      … 33 files under this directory
    tools/  (29 files)
      … 29 files under this directory
    utils/  (35 files)
      … 35 files under this directory
    widgets/  (9 files)
      … 9 files under this directory
    worker/  (6 files)
      … 6 files under this directory
    Constants.js
    Events.js
    app.js
  templates/  (30 files)
    dialogs/  (7 files)
      … 7 files under this directory
    settings/  (12 files)
      … 12 files under this directory
    data-uri-export.html
    debug-header.html
    drawing-tools.html
    frames-list.html
    layers-list.html
    misc-templates.html
    palettes-list.html
    popup-preview.html
    preview.html
    settings.html
    transformations.html
  index.html
  piskel-boot.js
  piskel-script-list.js
  piskel-style-list.js
tests/  (137 files)
  e2e/  (105 files)
    playwright/  (105 files)
      … 105 files under this directory
  unit-tests/  (32 files)
    database/  (2 files)
      … 2 files under this directory
    model/  (2 files)
      … 2 files under this directory
    rendering/  (4 files)
      … 4 files under this directory
    selection/  (1 files)
      … 1 files under this directory
    service/  (7 files)
      … 7 files under this directory
    testutils/  (1 files)
      … 1 files under this directory
    tools/  (1 files)
      … 1 files under this directory
    utils/  (14 files)
      … 14 files under this directory
vite-plugins/  (3 files)
  concat-scripts.js
  css-replace.js
  html-include.js
.gitignore
.npmignore
LICENSE
README.md
biome.jsonc
global.d.ts
karma.conf.js
package.json
playwright.config.ts
run-test-ci.sh
vite.config.js
```

## Entry points

- [misc/scripts/piskel-root](https://github.com/piskelapp/piskel/blob/e394f4fd3b382a0412aab078d1b88b2899d3b8ea/misc/scripts/piskel-root)
- [cli/index.js](https://github.com/piskelapp/piskel/blob/e394f4fd3b382a0412aab078d1b88b2899d3b8ea/cli/index.js)
- [misc/proto-ui-1/main.js](https://github.com/piskelapp/piskel/blob/e394f4fd3b382a0412aab078d1b88b2899d3b8ea/misc/proto-ui-1/main.js)
- [src/js/app.js](https://github.com/piskelapp/piskel/blob/e394f4fd3b382a0412aab078d1b88b2899d3b8ea/src/js/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 3 file(s) under cli package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 8 file(s) under data layer (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 151 file(s) under js package (observed from repository paths and static analysis). |
| misc package | library | Observed | Groups 1 file(s) under misc package (observed from repository paths and static analysis). |
| piskel-boot.js package | library | Observed | Groups 1 file(s) under piskel-boot.js package (observed from repository paths and static analysis). |
| piskel-script-list.js package | library | Observed | Groups 1 file(s) under piskel-script-list.js package (observed from repository paths and static analysis). |
| piskel-style-list.js package | library | Observed | Groups 1 file(s) under piskel-style-list.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 28 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 137 file(s) under tests (observed from repository paths and static analysis). |
| vite-plugins package | library | Observed | Groups 3 file(s) under vite-plugins package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci.yml` (ci)
- `.github/workflows/update-visual-baselines.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 280 analysed file(s)
- `tests` — 137 analysed file(s)
- `misc` — 79 analysed file(s)
- `docs` — 18 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `scripts` — 6 analysed file(s)
- `cli` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `vite-plugins` — 3 analysed file(s)
- `TODO` — 2 analysed file(s)
- `bin` — 2 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e394f4fd3b382a0412aab078d1b88b2899d3b8ea` is the revision these paths and observations refer to.
