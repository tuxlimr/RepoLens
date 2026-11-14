# Project structure: gregberge/svgr

**Analysed commit:** `975215efe85805cecafc920c103a827d864d2580`

**Commit reference:** [975215efe85805cecafc920c103a827d864d2580](https://github.com/gregberge/svgr/commit/975215efe85805cecafc920c103a827d864d2580)

**Tree at this commit:** [gregberge/svgr@975215efe858](https://github.com/gregberge/svgr/tree/975215efe85805cecafc920c103a827d864d2580)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gregberge/svgr |
| Description | Transform SVGs into React components 🦁 |
| Stars | 11061 |
| Forks | 440 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `975215efe85805cecafc920c103a827d864d2580` |
| Retrieved at | 2026-11-14T19:13:26.896340+00:00 |
| Files in this snapshot | 290 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (4 files)
    bug.md
    feature.md
    question.md
    regression.md
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  SUPPORT.md
  opencollective.yml
  stale.yml
__fixtures__/  (26 files)
  cased/  (4 files)
    PascalCase.svg
    camelCase.svg
    kebab-case.svg
    multiple---dashes.svg
  complex/  (2 files)
    skype.svg
    telegram.svg
  nesting/  (3 files)
    a/  (2 files)
      … 2 files under this directory
    one.svg
  numeric/  (2 files)
    2.file.svg
    file.svg
  simple/  (1 files)
    file.svg
  simple-existing/  (3 files)
    File..js
    File.js
    index..js
  withPrettierRc/  (2 files)
    .prettierrc
    file.svg
  withSvgoConfig/  (3 files)
    file.svg
    svgo.config.cjs
    svgo.config.js
  withSvgrRc/  (2 files)
    .svgrrc
    file.svg
  custom-index-template.js
  custom-index.config.js
  overrides.config.js
  template.js
api/  (4 files)
  api/  (1 files)
    svgr.js
  package.json
  pnpm-workspace.yaml
  vercel.json
deprecated-packages/  (2 files)
  svgr/  (2 files)
    message.js
    package.json
examples/  (14 files)
  mocha-esm/  (7 files)
    __mocks__/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    example.js
    example.test.js
    icon.svg
    mock-loader.js
    package.json
  webpack/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    CHANGELOG.md
    package.json
    webpack.config.js
packages/  (158 files)
  babel-plugin-add-jsx-attribute/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  babel-plugin-remove-jsx-attribute/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  babel-plugin-remove-jsx-empty-expression/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  babel-plugin-replace-jsx-attribute-value/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  babel-plugin-svg-dynamic-title/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  babel-plugin-svg-em-dimensions/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  babel-plugin-transform-react-native-svg/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  babel-plugin-transform-svg-component/  (11 files)
    src/  (6 files)
      … 6 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  babel-preset/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  cli/  (14 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (8 files)
      … 8 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  core/  (20 files)
    src/  (15 files)
      … 15 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  hast-util-to-babel-ast/  (16 files)
    src/  (11 files)
      … 11 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  plugin-jsx/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  plugin-prettier/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  plugin-svgo/  (10 files)
    src/  (5 files)
      … 5 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  rollup/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  webpack/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    .npmignore
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
public/  (1 files)
  .exists
website/  (56 files)
  images/  (2 files)
    logo-nav-dark.svg
    logo-nav-light.svg
  pages/  (21 files)
    docs/  (19 files)
      … 19 files under this directory
    index.mdx
    playground.mdx
  src/  (24 files)
    components/  (23 files)
      … 23 files under this directory
    smooth-doc/  (1 files)
      … 1 files under this directory
  .eslintignore
  .eslintrc.js
  .gitignore
  .nvmrc
  README.md
  _redirects
  gatsby-config.js
  netlify.toml
  package.json
.eslintignore
.eslintrc.json
.gitignore
.nvmrc
.prettierignore
.prettierrc
BACKERS.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
babel.config.js
jest.config.js
lerna.json
package.json
pnpm-workspace.yaml
tsconfig.json
```

## Entry points

- [packages/cli/bin/svgr](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/cli/bin/svgr)
- [packages/babel-plugin-add-jsx-attribute/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/babel-plugin-add-jsx-attribute/src/index.ts)
- [packages/babel-plugin-remove-jsx-attribute/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/babel-plugin-remove-jsx-attribute/src/index.ts)
- [packages/babel-plugin-remove-jsx-empty-expression/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/babel-plugin-remove-jsx-empty-expression/src/index.ts)
- [packages/babel-plugin-replace-jsx-attribute-value/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/babel-plugin-replace-jsx-attribute-value/src/index.ts)
- [packages/babel-plugin-svg-dynamic-title/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/babel-plugin-svg-dynamic-title/src/index.ts)
- [packages/babel-plugin-svg-em-dimensions/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/babel-plugin-svg-em-dimensions/src/index.ts)
- [packages/babel-plugin-transform-react-native-svg/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/babel-plugin-transform-react-native-svg/src/index.ts)
- [packages/babel-plugin-transform-svg-component/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/babel-plugin-transform-svg-component/src/index.ts)
- [packages/babel-preset/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/babel-preset/src/index.ts)
- [packages/cli/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/cli/src/index.ts)
- [packages/core/src/index.ts](https://github.com/gregberge/svgr/blob/975215efe85805cecafc920c103a827d864d2580/packages/core/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 45 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| deprecated-packages package | library | Observed | Groups 1 file(s) under deprecated-packages package (observed from repository paths and static analysis). |
| __fixtures__ package | library | Observed | Groups 9 file(s) under __fixtures__ package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 49 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 10 file(s) under service / domain layer (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 25 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/opencollective.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `api/package.json` (manifest)
- `api/pnpm-workspace.yaml` (config)
- `api/vercel.json` (config)
- `deprecated-packages/svgr/package.json` (manifest)
- `examples/mocha-esm/package.json` (manifest)
- `examples/webpack/package.json` (manifest)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/babel-plugin-add-jsx-attribute/package.json` (manifest)
- `packages/babel-plugin-add-jsx-attribute/tsconfig.json` (config)
- `packages/babel-plugin-remove-jsx-attribute/package.json` (manifest)
- `packages/babel-plugin-remove-jsx-attribute/tsconfig.json` (config)
- `packages/babel-plugin-remove-jsx-empty-expression/package.json` (manifest)
- `packages/babel-plugin-remove-jsx-empty-expression/tsconfig.json` (config)
- `packages/babel-plugin-replace-jsx-attribute-value/package.json` (manifest)
- `packages/babel-plugin-replace-jsx-attribute-value/tsconfig.json` (config)
- `packages/babel-plugin-svg-dynamic-title/package.json` (manifest)
- `packages/babel-plugin-svg-dynamic-title/tsconfig.json` (config)
- `packages/babel-plugin-svg-em-dimensions/package.json` (manifest)
- `packages/babel-plugin-svg-em-dimensions/tsconfig.json` (config)
- `packages/babel-plugin-transform-react-native-svg/package.json` (manifest)
- `packages/babel-plugin-transform-react-native-svg/tsconfig.json` (config)
- `packages/babel-plugin-transform-svg-component/package.json` (manifest)
- `packages/babel-plugin-transform-svg-component/tsconfig.json` (config)
- `packages/babel-preset/package.json` (manifest)
- `packages/babel-preset/tsconfig.json` (config)
- `packages/cli/package.json` (manifest)
- `packages/cli/tsconfig.json` (config)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/hast-util-to-babel-ast/package.json` (manifest)
- `packages/hast-util-to-babel-ast/tsconfig.json` (config)
- `packages/plugin-jsx/package.json` (manifest)
- `packages/plugin-jsx/tsconfig.json` (config)
- `packages/plugin-prettier/package.json` (manifest)
- `packages/plugin-prettier/tsconfig.json` (config)
- `packages/plugin-svgo/package.json` (manifest)
- `packages/plugin-svgo/tsconfig.json` (config)
- `packages/rollup/package.json` (manifest)
- `packages/rollup/tsconfig.json` (config)
- `packages/webpack/package.json` (manifest)
- `packages/webpack/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `website/netlify.toml` (config)
- `website/package.json` (manifest)

## Top-level layout

- `packages` — 158 analysed file(s)
- `website` — 56 analysed file(s)
- `__fixtures__` — 26 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `examples` — 14 analysed file(s)
- `.github` — 11 analysed file(s)
- `api` — 4 analysed file(s)
- `deprecated-packages` — 2 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (1 x likely secret file excluded; 2 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `975215efe85805cecafc920c103a827d864d2580` is the revision these paths and observations refer to.
