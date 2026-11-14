# Project structure: nolimits4web/atropos

**Analysed commit:** `eb4b4c5682117a53f60fccd459f64d06a99e9445`

**Commit reference:** [eb4b4c5682117a53f60fccd459f64d06a99e9445](https://github.com/nolimits4web/atropos/commit/eb4b4c5682117a53f60fccd459f64d06a99e9445)

**Tree at this commit:** [nolimits4web/atropos@eb4b4c568211](https://github.com/nolimits4web/atropos/tree/eb4b4c5682117a53f60fccd459f64d06a99e9445)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nolimits4web/atropos |
| Description | Stunning touch-friendly 3D parallax hover effects |
| Stars | 3614 |
| Forks | 108 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `eb4b4c5682117a53f60fccd459f64d06a99e9445` |
| Retrieved at | 2026-11-14T19:15:12.037871+00:00 |
| Files in this snapshot | 74 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (4 files)
    atropos_core_issue.yml
    atropos_react_issue.yml
    config.yml
    feature-request.yml
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
.vscode/  (1 files)
  settings.json
package/  (3 files)
  LICENSE
  README.md
  package.json
playground/  (24 files)
  core/  (7 files)
    i/  (5 files)
      … 5 files under this directory
    index.html
    main.css
  element/  (8 files)
    i/  (5 files)
      … 5 files under this directory
    index.html
    main.css
    main.js
  react/  (9 files)
    i/  (5 files)
      … 5 files under this directory
    App.jsx
    index.html
    main.css
    main.js
scripts/  (14 files)
  utils/  (4 files)
    autoprefixer.js
    clean-css.js
    fs-extra.js
    less.js
  banner.js
  build-element.js
  build-js.js
  build-react.js
  build-sponsors.mjs
  build-styles.js
  build-types.js
  build.js
  release.js
  watch.js
src/  (8 files)
  element/  (2 files)
    atropos-element.d.ts
    atropos-element.js
  react/  (2 files)
    atropos-react.d.ts
    atropos-react.js
  atropos.d.ts
  atropos.js
  atropos.less
  atropos.scss
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.prettierignore
.prettierrc
BACKERS.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
TODO.md
babel.config.js
babel.config.react.js
babel.config.vue.js
package.json
```

## Entry points

- [playground/element/main.js](https://github.com/nolimits4web/atropos/blob/eb4b4c5682117a53f60fccd459f64d06a99e9445/playground/element/main.js)
- [playground/react/App.jsx](https://github.com/nolimits4web/atropos/blob/eb4b4c5682117a53f60fccd459f64d06a99e9445/playground/react/App.jsx)
- [playground/react/main.js](https://github.com/nolimits4web/atropos/blob/eb4b4c5682117a53f60fccd459f64d06a99e9445/playground/react/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| atropos.d.ts package | library | Observed | Groups 1 file(s) under atropos.d.ts package (observed from repository paths and static analysis). |
| atropos.js package | library | Observed | Groups 1 file(s) under atropos.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| element package | library | Observed | Groups 2 file(s) under element package (observed from repository paths and static analysis). |
| playground package | library | Observed | Groups 3 file(s) under playground package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 2 file(s) under react package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 14 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/atropos_core_issue.yml` (config)
- `.github/ISSUE_TEMPLATE/atropos_react_issue.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `package/package.json` (manifest)

## Top-level layout

- `playground` — 24 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `scripts` — 14 analysed file(s)
- `src` — 8 analysed file(s)
- `.github` — 7 analysed file(s)
- `package` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `eb4b4c5682117a53f60fccd459f64d06a99e9445` is the revision these paths and observations refer to.
