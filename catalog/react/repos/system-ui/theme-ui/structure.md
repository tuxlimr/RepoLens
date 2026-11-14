# Project structure: system-ui/theme-ui

**Analysed commit:** `bc87592449bdd43312b363753c077dcd8cb05b30`

**Commit reference:** [bc87592449bdd43312b363753c077dcd8cb05b30](https://github.com/system-ui/theme-ui/commit/bc87592449bdd43312b363753c077dcd8cb05b30)

**Tree at this commit:** [system-ui/theme-ui@bc87592449bd](https://github.com/system-ui/theme-ui/tree/bc87592449bdd43312b363753c077dcd8cb05b30)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | system-ui/theme-ui |
| Description | Build consistent, themeable React apps based on constraint-based design principles |
| Stars | 5410 |
| Forks | 649 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | develop |
| Analysed commit | `bc87592449bdd43312b363753c077dcd8cb05b30` |
| Retrieved at | 2026-11-14T19:14:19.987396+00:00 |
| Files in this snapshot | 576 |

## Directory tree

```text
.codesandbox/  (1 files)
  ci.json
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (3 files)
    ci.yml
    codeql-analysis.yml
    e2e.yml
  CODEOWNERS
  dependabot.yml
  validate-codeowners.sh
.husky/  (1 files)
  _/  (1 files)
    husky.sh
examples/  (35 files)
  gatsby/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    gatsby-browser.js
    gatsby-config.js
    gatsby-ssr.js
    package.json
    tsconfig.json
  gatsby-plugin/  (5 files)
    src/  (3 files)
      … 3 files under this directory
    gatsby-config.js
    package.json
  next/  (12 files)
    components/  (2 files)
      … 2 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    .gitignore
    next-env.d.ts
    next.config.js
    package.json
    tsconfig.json
  typography/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    gatsby-browser.js
    gatsby-config.js
    gatsby-ssr.js
    package.json
    tsconfig.json
packages/  (497 files)
  color/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  color-modes/  (8 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    README.md
    package.json
  components/  (55 files)
    src/  (39 files)
      … 39 files under this directory
    test/  (13 files)
      … 13 files under this directory
    CHANGELOG.md
    README.md
    package.json
  core/  (18 files)
    jsx-dev-runtime/  (1 files)
      … 1 files under this directory
    jsx-runtime/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    test/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    README.md
    package.json
  css/  (12 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (4 files)
      … 4 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  custom-properties/  (7 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
  docs/  (174 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (160 files)
      … 160 files under this directory
    static/  (2 files)
      … 2 files under this directory
    .babelrc
    .eslintignore
    .eslintrc.js
    .gitignore
    declarations.d.ts
    gatsby-browser.js
    gatsby-config.js
    gatsby-node.js
    gatsby-ssr.js
    package.json
    tsconfig.json
  e2e/  (8 files)
    integration/  (2 files)
      … 2 files under this directory
    .gitignore
    cypress.config.js
    package.json
    plugins.js
    support.ts
    tsconfig.json
  gatsby-plugin-theme-ui/  (13 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (1 files)
      … 1 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    gatsby-browser.js
    gatsby-node.js
    gatsby-ssr.js
    index.js
    package.json
  gatsby-theme-style-guide/  (12 files)
    src/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    README.md
    gatsby-config.js
    gatsby-node.js
    index.js
    package.json
  gatsby-theme-ui-layout/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    index.js
    package.json
  global/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    README.md
    package.json
  match-media/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    package.json
  mdx/  (13 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-base/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-bootstrap/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-bulma/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-dark/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-deep/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-funk/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-future/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-polaris/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-roboto/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-sketchy/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-swiss/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-system/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-tailwind/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  preset-tosh/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  presets/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
  prism/  (26 files)
    presets/  (19 files)
      … 19 files under this directory
    src/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    build-presets.js
    package.json
  style-guide/  (14 files)
    src/  (11 files)
      … 11 files under this directory
    CHANGELOG.md
    README.md
    package.json
  tachyons/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    types/  (1 files)
      … 1 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
  tailwind/  (10 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (4 files)
      … 4 files under this directory
    .gitignore
    .npmignore
    CHANGELOG.md
    README.md
    package.json
  test-utils/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    tsconfig.json
  theme-provider/  (6 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    CHANGELOG.md
    README.md
    package.json
  theme-ui/  (15 files)
    jsx-dev-runtime/  (1 files)
      … 1 files under this directory
    jsx-runtime/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    test/  (6 files)
      … 6 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
  typography/  (12 files)
    src/  (3 files)
      … 3 files under this directory
    test/  (4 files)
      … 4 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    declarations.d.ts
    package.json
scripts/  (8 files)
  typecheck-built-files/  (5 files)
    README.md
    imports.ts
    package.json
    pnpm-workspace.yaml
    tsconfig.json
  all-contributors-check.js
  publish-to-npm.mjs
  should-skip-deploy.sh
.all-contributorsrc
.eslintignore
.eslintrc.js
.gitignore
.nvmrc
.pnpmfile.cjs
.prettierignore
.size-limit.json
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
MIGRATING.md
auto.config.ts
babel.config.js
jest-preprocess.js
jest.config.ts
lint-staged.config.js
package.json
pnpm-workspace.yaml
prettier.config.js
tsconfig.json
tsconfig.options.json
tsconfig.test.json
… 1 more files
```

## Entry points

- [packages/color-modes/src/index.tsx](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/color-modes/src/index.tsx)
- [packages/color/src/index.ts](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/color/src/index.ts)
- [packages/components/src/index.ts](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/components/src/index.ts)
- [packages/core/src/index.ts](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/core/src/index.ts)
- [packages/css/src/index.ts](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/css/src/index.ts)
- [packages/custom-properties/src/index.ts](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/custom-properties/src/index.ts)
- [packages/gatsby-plugin-theme-ui/index.js](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/gatsby-plugin-theme-ui/index.js)
- [packages/gatsby-plugin-theme-ui/src/index.js](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/gatsby-plugin-theme-ui/src/index.js)
- [packages/gatsby-theme-style-guide/index.js](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/gatsby-theme-style-guide/index.js)
- [packages/gatsby-theme-style-guide/src/index.js](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/gatsby-theme-style-guide/src/index.js)
- [packages/gatsby-theme-ui-layout/index.js](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/gatsby-theme-ui-layout/index.js)
- [packages/gatsby-theme-ui-layout/src/index.js](https://github.com/system-ui/theme-ui/blob/bc87592449bdd43312b363753c077dcd8cb05b30/packages/gatsby-theme-ui-layout/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 72 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 119 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 60 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.codesandbox/ci.json` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/e2e.yml` (ci)
- `.size-limit.json` (config)
- `examples/gatsby-plugin/package.json` (manifest)
- `examples/gatsby/package.json` (manifest)
- `examples/gatsby/tsconfig.json` (config)
- `examples/next/package.json` (manifest)
- `examples/next/tsconfig.json` (config)
- `examples/typography/package.json` (manifest)
- `examples/typography/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/color-modes/package.json` (manifest)
- `packages/color/package.json` (manifest)
- `packages/components/package.json` (manifest)
- `packages/core/jsx-dev-runtime/package.json` (manifest)
- `packages/core/jsx-runtime/package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/css/package.json` (manifest)
- `packages/css/utils/package.json` (manifest)
- `packages/custom-properties/package.json` (manifest)
- `packages/docs/package.json` (manifest)
- `packages/docs/tsconfig.json` (config)
- `packages/e2e/package.json` (manifest)
- `packages/e2e/tsconfig.json` (config)
- `packages/gatsby-plugin-theme-ui/package.json` (manifest)
- `packages/gatsby-theme-style-guide/package.json` (manifest)
- `packages/gatsby-theme-ui-layout/package.json` (manifest)
- `packages/global/package.json` (manifest)
- `packages/match-media/package.json` (manifest)
- `packages/mdx/package.json` (manifest)
- `packages/preset-base/package.json` (manifest)
- `packages/preset-bootstrap/package.json` (manifest)
- `packages/preset-bulma/package.json` (manifest)
- `packages/preset-dark/package.json` (manifest)
- `packages/preset-deep/package.json` (manifest)
- `packages/preset-funk/package.json` (manifest)
- `packages/preset-future/package.json` (manifest)
- `packages/preset-polaris/package.json` (manifest)
- `packages/preset-roboto/package.json` (manifest)
- `packages/preset-sketchy/package.json` (manifest)
- `packages/preset-swiss/package.json` (manifest)
- `packages/preset-system/package.json` (manifest)
- `packages/preset-tailwind/package.json` (manifest)
- `packages/preset-tosh/package.json` (manifest)
- `packages/presets/package.json` (manifest)
- `packages/prism/package.json` (manifest)
- `packages/prism/presets/dracula.json` (config)
- `packages/prism/presets/duotone-dark.json` (config)
- `packages/prism/presets/duotone-light.json` (config)
- `packages/prism/presets/github.json` (config)
- `packages/prism/presets/night-owl-light.json` (config)
- `packages/prism/presets/night-owl.json` (config)
- `packages/prism/presets/oceanic-next.json` (config)
- `packages/prism/presets/prism-coy.json` (config)
- `packages/prism/presets/prism-dark.json` (config)
- `packages/prism/presets/prism-funky.json` (config)
- `packages/prism/presets/prism-okaidia.json` (config)
- `packages/prism/presets/prism-solarizedlight.json` (config)
- `packages/prism/presets/prism-tomorrow.json` (config)
- `packages/prism/presets/prism-twilight.json` (config)
- `packages/prism/presets/prism.json` (config)
- `packages/prism/presets/shades-of-purple.json` (config)
- `packages/prism/presets/ultramin.json` (config)
- `packages/prism/presets/vs-dark.json` (config)
- `packages/style-guide/package.json` (manifest)
- `packages/tachyons/package.json` (manifest)
- `packages/tailwind/package.json` (manifest)
- `packages/test-utils/package.json` (manifest)
- `packages/test-utils/tsconfig.json` (config)
- `packages/theme-provider/package.json` (manifest)
- `packages/theme-ui/jsx-dev-runtime/package.json` (manifest)
- `packages/theme-ui/jsx-runtime/package.json` (manifest)
- `packages/theme-ui/package.json` (manifest)
- `packages/typography/package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `scripts/typecheck-built-files/package.json` (manifest)
- `scripts/typecheck-built-files/pnpm-workspace.yaml` (config)
- `scripts/typecheck-built-files/tsconfig.json` (config)
- `tsconfig.json` (config)
- `tsconfig.options.json` (config)
- `tsconfig.test.json` (config)
- `vercel.json` (config)

## Top-level layout

- `packages` — 497 analysed file(s)
- `examples` — 35 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `.github` — 9 analysed file(s)
- `scripts` — 8 analysed file(s)
- `.codesandbox` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (2 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bc87592449bdd43312b363753c077dcd8cb05b30` is the revision these paths and observations refer to.
