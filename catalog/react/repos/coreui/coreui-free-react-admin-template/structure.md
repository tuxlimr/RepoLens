# Project structure: coreui/coreui-free-react-admin-template

**Analysed commit:** `2609f5995035973e00c16ec723165a5fff87cceb`

**Commit reference:** [2609f5995035973e00c16ec723165a5fff87cceb](https://github.com/coreui/coreui-free-react-admin-template/commit/2609f5995035973e00c16ec723165a5fff87cceb)

**Tree at this commit:** [coreui/coreui-free-react-admin-template@2609f5995035](https://github.com/coreui/coreui-free-react-admin-template/tree/2609f5995035973e00c16ec723165a5fff87cceb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | coreui/coreui-free-react-admin-template |
| Description | Free React Admin & Dashboard Template Built for AI-Assisted Development |
| Stars | 4970 |
| Forks | 2552 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `2609f5995035973e00c16ec723165a5fff87cceb` |
| Retrieved at | 2026-11-14T19:14:32.908654+00:00 |
| Files in this snapshot | 108 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    npm.yml
    stale.yml
  CODE_OF_CONDUCT.md
  COMMIT_CONVENTION.md
  CONTRIBUTING.md
  FUNDING.yml
  SUPPORT.md
public/  (1 files)
  manifest.json
src/  (83 files)
  assets/  (8 files)
    brand/  (7 files)
      … 7 files under this directory
    icons/  (1 files)
      … 1 files under this directory
  components/  (13 files)
    header/  (2 files)
      … 2 files under this directory
    AppBreadcrumb.jsx
    AppContent.jsx
    AppFooter.jsx
    AppHeader.jsx
    AppSidebar.jsx
    AppSidebarNav.jsx
    DocsComponents.jsx
    DocsExample.jsx
    DocsIcons.jsx
    DocsLink.jsx
    index.js
  layout/  (1 files)
    DefaultLayout.jsx
  scss/  (3 files)
    vendors/  (1 files)
      … 1 files under this directory
    examples.scss
    style.scss
  views/  (53 files)
    authentication/  (6 files)
      … 6 files under this directory
    charts/  (1 files)
      … 1 files under this directory
    components/  (25 files)
      … 25 files under this directory
    dashboard/  (3 files)
      … 3 files under this directory
    error-pages/  (2 files)
      … 2 files under this directory
    forms/  (9 files)
      … 9 files under this directory
    icons/  (4 files)
      … 4 files under this directory
    widgets/  (3 files)
      … 3 files under this directory
  App.jsx
  _nav.jsx
  index.jsx
  routes.js
  store.js
.browserslistrc
.cursorrules
.editorconfig
.gitattributes
.gitignore
.prettierignore
.prettierrc.js
ARCHITECTURE.md
DEVELOPMENT.md
LICENSE
README.md
eslint.config.mjs
index.html
package.json
vite.config.mjs
```

## Entry points

- [src/App.jsx](https://github.com/coreui/coreui-free-react-admin-template/blob/2609f5995035973e00c16ec723165a5fff87cceb/src/App.jsx)
- [src/components/header/index.js](https://github.com/coreui/coreui-free-react-admin-template/blob/2609f5995035973e00c16ec723165a5fff87cceb/src/components/header/index.js)
- [src/components/index.js](https://github.com/coreui/coreui-free-react-admin-template/blob/2609f5995035973e00c16ec723165a5fff87cceb/src/components/index.js)
- [src/index.jsx](https://github.com/coreui/coreui-free-react-admin-template/blob/2609f5995035973e00c16ec723165a5fff87cceb/src/index.jsx)
- [src/views/icons/index.js](https://github.com/coreui/coreui-free-react-admin-template/blob/2609f5995035973e00c16ec723165a5fff87cceb/src/views/icons/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 53 file(s) under api layer (observed from repository paths and static analysis). |
| App.jsx package | library | Observed | Groups 1 file(s) under app.jsx package (observed from repository paths and static analysis). |
| assets package | library | Observed | Groups 8 file(s) under assets package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 13 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| index.jsx package | library | Observed | Groups 1 file(s) under index.jsx package (observed from repository paths and static analysis). |
| layout package | library | Observed | Groups 1 file(s) under layout package (observed from repository paths and static analysis). |
| _nav.jsx package | library | Observed | Groups 1 file(s) under _nav.jsx package (observed from repository paths and static analysis). |
| routes.js package | library | Observed | Groups 1 file(s) under routes.js package (observed from repository paths and static analysis). |
| store.js package | library | Observed | Groups 1 file(s) under store.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/npm.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `package.json` (manifest)
- `public/manifest.json` (config)

## Top-level layout

- `src` — 83 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 9 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2609f5995035973e00c16ec723165a5fff87cceb` is the revision these paths and observations refer to.
