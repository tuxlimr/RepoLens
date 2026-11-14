# Project structure: konstaui/konsta

**Analysed commit:** `5b8e54d35ba7ace274cca450f808af570d258f57`

**Commit reference:** [5b8e54d35ba7ace274cca450f808af570d258f57](https://github.com/konstaui/konsta/commit/5b8e54d35ba7ace274cca450f808af570d258f57)

**Tree at this commit:** [konstaui/konsta@5b8e54d35ba7](https://github.com/konstaui/konsta/tree/5b8e54d35ba7ace274cca450f808af570d258f57)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | konstaui/konsta |
| Description | Mobile UI components made with Tailwind CSS |
| Stars | 4289 |
| Forks | 159 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5b8e54d35ba7ace274cca450f808af570d258f57` |
| Retrieved at | 2026-11-14T19:14:49.940623+00:00 |
| Files in this snapshot | 699 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (5 files)
    config.yml
    feature-request.yml
    konsta_react_issue.yml
    konsta_svelte_issue.yml
    konsta_vue_issue.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
.vscode/  (1 files)
  settings.json
kitchen-sink/  (150 files)
  react/  (45 files)
    components/  (4 files)
      … 4 files under this directory
    pages/  (36 files)
      … 36 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    index.html
    index.js
    routes.js
    vite.config.js
  svelte/  (53 files)
    components/  (12 files)
      … 12 files under this directory
    pages/  (36 files)
      … 36 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    index.html
    index.js
    routes.js
    vite.config.js
  vue/  (52 files)
    components/  (11 files)
      … 11 files under this directory
    pages/  (36 files)
      … 36 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    index.html
    index.js
    routes.js
    vite.config.js
package/  (5 files)
  react/  (1 files)
    package.json
  svelte/  (1 files)
    package.json
  vue/  (1 files)
    package.json
  README.md
  package.json
scripts/  (17 files)
  banner.js
  build-copy.js
  build-export-classes.js
  build-export-colors.js
  build-export-shared.js
  build-react-types.js
  build-react.js
  build-shared.js
  build-sponsors.js
  build-svelte-types.js
  build-svelte.js
  build-vue-types.js
  build-vue.js
  build.js
  get-dirname.js
  release.js
  transform-vue-component.js
src/  (502 files)
  color-utils/  (48 files)
    material-color-utilities/  (45 files)
      … 45 files under this directory
    hex-to-rgb.js
    ios-colors.js
    md-colors.js
  react/  (90 files)
    components/  (74 files)
      … 74 files under this directory
    shared/  (11 files)
      … 11 files under this directory
    konsta-react.d.ts
    konsta-react.js
    package.json
    theme.css
    theme.css.d.ts
  shared/  (119 files)
    classes/  (56 files)
      … 56 files under this directory
    colors/  (57 files)
      … 57 files under this directory
    calc-popover-position.js
    cls.js
    filter-colors.js
    touch-ripple-class.js
    use-ios-highlight.js
    use-ios-tabbar-highlight.js
  styles/  (10 files)
    base.css
    colors.css
    glass.css
    hairlines.css
    ios-material.css
    no-scrollbar.css
    preloader.css
    range.css
    safe-areas.css
    touch-ripple.css
  svelte/  (85 files)
    components/  (71 files)
      … 71 files under this directory
    shared/  (9 files)
      … 9 files under this directory
    konsta-svelte.d.ts
    konsta-svelte.js
    package.json
    theme.css
    theme.css.d.ts
  types/  (62 files)
    Actions.d.ts
    ActionsButton.d.ts
    ActionsGroup.d.ts
    ActionsLabel.d.ts
    App.d.ts
    Badge.d.ts
    Block.d.ts
    BlockFooter.d.ts
    BlockHeader.d.ts
    BlockTitle.d.ts
    Breadcrumbs.d.ts
    BreadcrumbsCollapsed.d.ts
    BreadcrumbsItem.d.ts
    BreadcrumbsSeparator.d.ts
    Button.d.ts
    Card.d.ts
    Checkbox.d.ts
    Chip.d.ts
    Dialog.d.ts
    DialogButton.d.ts
    Fab.d.ts
    Glass.d.ts
    Icon.d.ts
    Link.d.ts
    … 38 more files
  vue/  (84 files)
    components/  (72 files)
      … 72 files under this directory
    shared/  (7 files)
      … 7 files under this directory
    konsta-vue.d.ts
    konsta-vue.js
    package.json
    theme.css
    theme.css.d.ts
  package.json
  plugin-colors.js
  theme.css
  theme.css.d.ts
.browserslistrc
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
babel.config.react.js
babel.config.vue.js
package.json
tailwind.config.js.old
```

## Entry points

- [kitchen-sink/react/components/App.jsx](https://github.com/konstaui/konsta/blob/5b8e54d35ba7ace274cca450f808af570d258f57/kitchen-sink/react/components/App.jsx)
- [kitchen-sink/react/components/Page.jsx](https://github.com/konstaui/konsta/blob/5b8e54d35ba7ace274cca450f808af570d258f57/kitchen-sink/react/components/Page.jsx)
- [kitchen-sink/react/index.js](https://github.com/konstaui/konsta/blob/5b8e54d35ba7ace274cca450f808af570d258f57/kitchen-sink/react/index.js)
- [kitchen-sink/svelte/index.js](https://github.com/konstaui/konsta/blob/5b8e54d35ba7ace274cca450f808af570d258f57/kitchen-sink/svelte/index.js)
- [kitchen-sink/vue/index.js](https://github.com/konstaui/konsta/blob/5b8e54d35ba7ace274cca450f808af570d258f57/kitchen-sink/vue/index.js)
- [src/color-utils/material-color-utilities/index.js](https://github.com/konstaui/konsta/blob/5b8e54d35ba7ace274cca450f808af570d258f57/src/color-utils/material-color-utilities/index.js)
- [src/react/components/App.jsx](https://github.com/konstaui/konsta/blob/5b8e54d35ba7ace274cca450f808af570d258f57/src/react/components/App.jsx)
- [src/react/components/Page.jsx](https://github.com/konstaui/konsta/blob/5b8e54d35ba7ace274cca450f808af570d258f57/src/react/components/Page.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| color-utils package | library | Observed | Groups 47 file(s) under color-utils package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| kitchen-sink package | library | Observed | Groups 144 file(s) under kitchen-sink package (observed from repository paths and static analysis). |
| plugin-colors.js package | library | Observed | Groups 1 file(s) under plugin-colors.js package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 88 file(s) under react package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 17 file(s) under scripts package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 119 file(s) under shared package (observed from repository paths and static analysis). |
| svelte package | library | Observed | Groups 83 file(s) under svelte package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| theme.css.d.ts package | library | Observed | Groups 1 file(s) under theme.css.d.ts package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 62 file(s) under types package (observed from repository paths and static analysis). |
| vue package | library | Observed | Groups 82 file(s) under vue package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/konsta_react_issue.yml` (config)
- `.github/ISSUE_TEMPLATE/konsta_svelte_issue.yml` (config)
- `.github/ISSUE_TEMPLATE/konsta_vue_issue.yml` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `package/package.json` (manifest)
- `package/react/package.json` (manifest)
- `package/svelte/package.json` (manifest)
- `package/vue/package.json` (manifest)
- `src/package.json` (manifest)
- `src/react/package.json` (manifest)
- `src/svelte/package.json` (manifest)
- `src/vue/package.json` (manifest)

## Top-level layout

- `src` — 502 analysed file(s)
- `kitchen-sink` — 150 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `scripts` — 17 analysed file(s)
- `.github` — 7 analysed file(s)
- `package` — 5 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5b8e54d35ba7ace274cca450f808af570d258f57` is the revision these paths and observations refer to.
