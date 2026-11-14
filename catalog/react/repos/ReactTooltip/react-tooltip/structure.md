# Project structure: ReactTooltip/react-tooltip

**Analysed commit:** `c58434e175078b2c36dbd17162a06a1971238831`

**Commit reference:** [c58434e175078b2c36dbd17162a06a1971238831](https://github.com/ReactTooltip/react-tooltip/commit/c58434e175078b2c36dbd17162a06a1971238831)

**Tree at this commit:** [ReactTooltip/react-tooltip@c58434e17507](https://github.com/ReactTooltip/react-tooltip/tree/c58434e175078b2c36dbd17162a06a1971238831)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ReactTooltip/react-tooltip |
| Description | React Tooltip Component |
| Stars | 3826 |
| Forks | 529 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c58434e175078b2c36dbd17162a06a1971238831` |
| Retrieved at | 2026-11-14T19:15:04.168718+00:00 |
| Files in this snapshot | 213 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    question.yml
  workflows/  (4 files)
    beta-release.yaml
    lint.yaml
    pull-request.yaml
    stale.yml
  FUNDING.yml
.husky/  (2 files)
  .gitignore
  pre-commit
benchmarks/  (6 files)
  fixture/  (2 files)
    app.tsx
    index.html
  README.md
  aggregate-benchmarks.mjs
  run-benchmark.mjs
  run-scaling-series.mjs
docs/  (100 files)
  docs/  (26 files)
    examples/  (18 files)
      … 18 files under this directory
    upgrade-guide/  (4 files)
      … 4 files under this directory
    accessibility.mdx
    getting-started.mdx
    options.mdx
    troubleshooting.mdx
  scripts/  (1 files)
    generate-tooltip-style-sources.mjs
  src/  (22 files)
    components/  (10 files)
      … 10 files under this directory
    css/  (1 files)
      … 1 files under this directory
    data/  (1 files)
      … 1 files under this directory
    generated/  (2 files)
      … 2 files under this directory
    pages/  (5 files)
      … 5 files under this directory
    theme/  (3 files)
      … 3 files under this directory
  static/  (17 files)
    img/  (12 files)
      … 12 files under this directory
    js/  (2 files)
      … 2 files under this directory
    .nojekyll
    ads.txt
    robots.txt
  versioned_docs/  (24 files)
    version-5.x/  (24 files)
      … 24 files under this directory
  versioned_sidebars/  (1 files)
    version-5.x-sidebars.json
  .gitignore
  README.md
  babel.config.js
  docusaurus.config.js
  package.json
  react-app-env.d.ts
  sidebars.js
  tsconfig.json
  versions.json
example/  (8 files)
  public/  (2 files)
    index.html
    manifest.json
  src/  (4 files)
    App.js
    index.css
    index.js
    index.scss
  .gitignore
  package.json
public/  (2 files)
  index-rollup.html
  index.html
rollup-plugins/  (1 files)
  replace-before-save-file.js
scripts/  (2 files)
  configure-react-version.mjs
  dev-port.mjs
src/  (55 files)
  components/  (15 files)
    Tooltip/  (11 files)
      … 11 files under this directory
    TooltipController/  (4 files)
      … 4 files under this directory
  test/  (23 files)
    __snapshots__/  (3 files)
      … 3 files under this directory
    anchor-registry.spec.js
    escaped-anchor-selectors.spec.js
    jest-setup.js
    mutation-observer-test-utils.js
    test-utils.js
    tooltip-advanced.spec.js
    tooltip-anchor-selection.spec.js
    tooltip-attributes.spec.js
    tooltip-close-and-delay-behavior.spec.js
    tooltip-controlled-and-ref.spec.js
    tooltip-edge-cases.spec.js
    tooltip-focus-visible.spec.js
    tooltip-imperative.spec.js
    tooltip-interaction-behavior.spec.js
    tooltip-interactions.spec.js
    tooltip-observers.spec.js
    tooltip-props.spec.js
    tooltip-removal.spec.js
    tooltip-styling.spec.js
    utils.spec.js
  utils/  (12 files)
    clear-timeout-ref.ts
    compute-tooltip-position-types.d.ts
    compute-tooltip-position.ts
    css-time-to-ms.ts
    debounce.ts
    deep-equal.ts
    get-scroll-parent.ts
    handle-style.ts
    index.ts
    parse-data-tooltip-id-selector.ts
    resolve-data-tooltip-anchor.ts
    use-isomorphic-layout-effect.ts
  App.tsx
  index-dev.tsx
  index.tsx
  styles.module.css
  tokens.css
.editorconfig
.eslintrc.json
.gitattributes
.gitignore
.npmignore
.prettierrc.json
.stylelintrc.json
.travis.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
beta-release.js
bower.json
bundlesize.config.json
esbuild.config.dev.mjs
esbuild.config.prod.mjs
eslint.config.js
global.d.ts
jest.config.mjs
package.json
prebuild.js
rollup.config.dev.mjs
… 4 more files
```

## Entry points

- [benchmarks/fixture/app.tsx](https://github.com/ReactTooltip/react-tooltip/blob/c58434e175078b2c36dbd17162a06a1971238831/benchmarks/fixture/app.tsx)
- [src/App.tsx](https://github.com/ReactTooltip/react-tooltip/blob/c58434e175078b2c36dbd17162a06a1971238831/src/App.tsx)
- [src/components/Tooltip/index.ts](https://github.com/ReactTooltip/react-tooltip/blob/c58434e175078b2c36dbd17162a06a1971238831/src/components/Tooltip/index.ts)
- [src/components/TooltipController/index.ts](https://github.com/ReactTooltip/react-tooltip/blob/c58434e175078b2c36dbd17162a06a1971238831/src/components/TooltipController/index.ts)
- [src/index.tsx](https://github.com/ReactTooltip/react-tooltip/blob/c58434e175078b2c36dbd17162a06a1971238831/src/index.tsx)
- [src/utils/index.ts](https://github.com/ReactTooltip/react-tooltip/blob/c58434e175078b2c36dbd17162a06a1971238831/src/utils/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| benchmarks package | library | Observed | Groups 4 file(s) under benchmarks package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 13 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 10 file(s) under core modules (observed from repository paths and static analysis). |
| index-dev.tsx package | library | Observed | Groups 1 file(s) under index-dev.tsx package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| rollup-plugins package | library | Observed | Groups 1 file(s) under rollup-plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 23 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 12 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/workflows/beta-release.yaml` (ci)
- `.github/workflows/lint.yaml` (ci)
- `.github/workflows/pull-request.yaml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.prettierrc.json` (config)
- `.stylelintrc.json` (config)
- `.travis.yml` (ci)
- `bower.json` (config)
- `bundlesize.config.json` (config)
- `docs/docs/examples/_category_.json` (config)
- `docs/docs/upgrade-guide/_category_.json` (config)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `docs/versioned_docs/version-5.x/examples/_category_.json` (config)
- `docs/versioned_docs/version-5.x/upgrade-guide/_category_.json` (config)
- `docs/versioned_sidebars/version-5.x-sidebars.json` (config)
- `docs/versions.json` (config)
- `example/package.json` (manifest)
- `example/public/manifest.json` (config)
- `package.json` (manifest)
- `tsconfig.jest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `docs` — 100 analysed file(s)
- `src` — 55 analysed file(s)
- `(root files)` — 28 analysed file(s)
- `.github` — 9 analysed file(s)
- `example` — 8 analysed file(s)
- `benchmarks` — 6 analysed file(s)
- `.husky` — 2 analysed file(s)
- `public` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `rollup-plugins` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (5 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c58434e175078b2c36dbd17162a06a1971238831` is the revision these paths and observations refer to.
