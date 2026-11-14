# Project structure: dimsemenov/PhotoSwipe

**Analysed commit:** `cd41cb587a460634e4cae53134f3d01d06e284a6`

**Commit reference:** [cd41cb587a460634e4cae53134f3d01d06e284a6](https://github.com/dimsemenov/PhotoSwipe/commit/cd41cb587a460634e4cae53134f3d01d06e284a6)

**Tree at this commit:** [dimsemenov/PhotoSwipe@cd41cb587a46](https://github.com/dimsemenov/PhotoSwipe/tree/cd41cb587a460634e4cae53134f3d01d06e284a6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dimsemenov/PhotoSwipe |
| Description | JavaScript image gallery for mobile and desktop, modular, framework independent |
| Stars | 25302 |
| Forks | 3266 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `cd41cb587a460634e4cae53134f3d01d06e284a6` |
| Retrieved at | 2026-11-14T19:11:00.560308+00:00 |
| Files in this snapshot | 118 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    build.yml
  FUNDING.yml
demo-docs-website/  (53 files)
  src/  (43 files)
    components/  (12 files)
      … 12 files under this directory
    css/  (7 files)
      … 7 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    theme/  (20 files)
      … 20 files under this directory
  static/  (4 files)
    photoswipe/  (3 files)
      … 3 files under this directory
    .nojekyll
  .gitignore
  babel.config.js
  docusaurus.config.js
  package.json
  repo-data.json
  sidebars.js
docs/  (18 files)
  adding-ui-elements.md
  adjusting-zoom-level.md
  caption.md
  click-and-tap-actions.md
  custom-content.md
  data-sources.md
  events.md
  filters.md
  getting-started.md
  methods.md
  native-fullscreen-on-open.md
  opening-or-closing-transition.md
  options.md
  properties.md
  react-image-gallery.md
  styling.md
  svelte-image-gallery.md
  vue-image-gallery.md
src/  (35 files)
  js/  (34 files)
    core/  (2 files)
      … 2 files under this directory
    gestures/  (4 files)
      … 4 files under this directory
    lightbox/  (1 files)
      … 1 files under this directory
    slide/  (7 files)
      … 7 files under this directory
    ui/  (7 files)
      … 7 files under this directory
    util/  (7 files)
      … 7 files under this directory
    keyboard.js
    main-scroll.js
    opener.js
    photoswipe.js
    scroll-wheel.js
    types.ts
  photoswipe.css
.babelrc
.editorconfig
.eslintignore
.eslintrc.json
.gitignore
LICENSE
README.md
global.d.ts
package.json
tsconfig.json
```

## Entry points

- [demo-docs-website/src/pages/index.js](https://github.com/dimsemenov/PhotoSwipe/blob/cd41cb587a460634e4cae53134f3d01d06e284a6/demo-docs-website/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| demo-docs-website package | library | Observed | Groups 31 file(s) under demo-docs-website package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 32 file(s) under js package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 2 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/build.yml` (ci)
- `demo-docs-website/package.json` (manifest)
- `demo-docs-website/repo-data.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `demo-docs-website` — 53 analysed file(s)
- `src` — 35 analysed file(s)
- `docs` — 18 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 41 file(s) were skipped during inventory (41 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `cd41cb587a460634e4cae53134f3d01d06e284a6` is the revision these paths and observations refer to.
