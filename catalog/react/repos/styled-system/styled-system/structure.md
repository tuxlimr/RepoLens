# Project structure: styled-system/styled-system

**Analysed commit:** `6d822f27a486e5e2bc1cae1f44dd151ce874a863`

**Commit reference:** [6d822f27a486e5e2bc1cae1f44dd151ce874a863](https://github.com/styled-system/styled-system/commit/6d822f27a486e5e2bc1cae1f44dd151ce874a863)

**Tree at this commit:** [styled-system/styled-system@6d822f27a486](https://github.com/styled-system/styled-system/tree/6d822f27a486e5e2bc1cae1f44dd151ce874a863)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | styled-system/styled-system |
| Description | ⬢ Style props for rapid UI development |
| Stars | 7856 |
| Forks | 493 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `6d822f27a486e5e2bc1cae1f44dd151ce874a863` |
| Retrieved at | 2026-11-14T19:13:44.850428+00:00 |
| Files in this snapshot | 191 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (3 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    question.md
benchmarks/  (1 files)
  README.md
docs/  (63 files)
  guides/  (14 files)
    array-props.md
    array-scales.md
    build-a-box.md
    color-modes.md
    component-types.md
    default-values.md
    exceptions.md
    index.md
    migrating.md
    removing-props-from-html.md
    scale-aliases.md
    spacing.md
    theming.md
    why-powers-of-two.md
  src/  (26 files)
    gatsby-plugin-theme-ui/  (2 files)
      … 2 files under this directory
    logo/  (3 files)
      … 3 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    badges.md
    burger.js
    button.js
    doc.js
    edit-link.js
    example.mdx
    index.js
    layout.js
    link.js
    logos.mdx
    nav-grid.js
    nav-link.js
    note.js
    pagination.js
    sidebar.js
    sidebar.mdx
    toc-wrapper.js
  static/  (2 files)
    logo-white.svg
    logo.svg
  .gitignore
  api.md
  articles.md
  custom-props.md
  ecosystem.md
  gatsby-browser.js
  gatsby-config.js
  gatsby-node.js
  gatsby-ssr.js
  getting-started.md
  how-it-works.md
  package.json
  packages.md
  rationale.md
  responsive-styles.md
  showcase.md
  table.md
  testimonials.md
  theme-specification.md
  theming.md
  variants.md
examples/  (29 files)
  basic/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
  css/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
  emotion/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
  responsive-objects/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
  svelte/  (6 files)
    App.svelte
    README.md
    index.js
    package.json
    rollup.config.js
    theme.js
  theme-aliases/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
packages/  (82 files)
  background/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
  border/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
  color/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
  core/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (5 files)
      … 5 files under this directory
    package.json
  css/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .npmignore
    README.md
    package.json
  edit/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .gitignore
    .npmignore
    README.md
    package.json
  flexbox/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
  grid/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
  layout/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
  position/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
  prop-types/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .gitignore
    .npmignore
    README.md
    package.json
  props/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  shadow/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
  should-forward-prop/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  space/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
  styled-system/  (11 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (7 files)
      … 7 files under this directory
    .npmignore
    README.md
    package.json
  theme-get/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  typography/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    package.json
  variant/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    README.md
    package.json
.eslintignore
.gitignore
.npmignore
.prettierignore
.prettierrc
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
babel.config.js
lerna.json
package.json
```

## Entry points

- [packages/background/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/background/src/index.js)
- [packages/border/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/border/src/index.js)
- [packages/color/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/color/src/index.js)
- [packages/core/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/core/src/index.js)
- [packages/css/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/css/src/index.js)
- [packages/edit/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/edit/src/index.js)
- [packages/flexbox/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/flexbox/src/index.js)
- [packages/grid/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/grid/src/index.js)
- [packages/layout/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/layout/src/index.js)
- [packages/position/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/position/src/index.js)
- [packages/prop-types/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/prop-types/src/index.js)
- [packages/props/src/index.js](https://github.com/styled-system/styled-system/blob/6d822f27a486e5e2bc1cae1f44dd151ce874a863/packages/props/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 18 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 30 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `docs/package.json` (manifest)
- `examples/basic/package.json` (manifest)
- `examples/css/package.json` (manifest)
- `examples/emotion/package.json` (manifest)
- `examples/responsive-objects/package.json` (manifest)
- `examples/svelte/package.json` (manifest)
- `examples/theme-aliases/package.json` (manifest)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/background/package.json` (manifest)
- `packages/border/package.json` (manifest)
- `packages/color/package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/css/package.json` (manifest)
- `packages/edit/package.json` (manifest)
- `packages/flexbox/package.json` (manifest)
- `packages/grid/package.json` (manifest)
- `packages/layout/package.json` (manifest)
- `packages/position/package.json` (manifest)
- `packages/prop-types/package.json` (manifest)
- `packages/props/package.json` (manifest)
- `packages/shadow/package.json` (manifest)
- `packages/should-forward-prop/package.json` (manifest)
- `packages/space/package.json` (manifest)
- `packages/styled-system/package.json` (manifest)
- `packages/theme-get/package.json` (manifest)
- `packages/typography/package.json` (manifest)
- `packages/variant/package.json` (manifest)

## Top-level layout

- `packages` — 82 analysed file(s)
- `docs` — 63 analysed file(s)
- `examples` — 29 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 3 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `benchmarks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6d822f27a486e5e2bc1cae1f44dd151ce874a863` is the revision these paths and observations refer to.
