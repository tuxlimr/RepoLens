# Project structure: paypal/glamorous

**Analysed commit:** `031484cd5eff92ff135038200ba49a300859a335`

**Commit reference:** [031484cd5eff92ff135038200ba49a300859a335](https://github.com/paypal/glamorous/commit/031484cd5eff92ff135038200ba49a300859a335)

**Tree at this commit:** [paypal/glamorous@031484cd5eff](https://github.com/paypal/glamorous/tree/031484cd5eff92ff135038200ba49a300859a335)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | paypal/glamorous |
| Description | DEPRECATED: 💄 Maintainable CSS with React |
| Stars | 3613 |
| Forks | 204 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `031484cd5eff92ff135038200ba49a300859a335` |
| Retrieved at | 2026-11-14T19:15:11.946466+00:00 |
| Files in this snapshot | 113 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
examples/  (8 files)
  with-jest/  (7 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    .babelrc
    README.md
    index.js
    index.test.js
    package.json
    testSetup.js
  README.md
other/  (19 files)
  __tests__/  (3 files)
    helpers/  (1 files)
      … 1 files under this directory
    dist-preact.js
    dist-react.js
  codemods/  (5 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    theme-move.js
    theme-move.test.js
  logo/  (2 files)
    compact.ai
    full.ai
  EMOTION_MIGRATION.md
  FAQ.md
  MAINTAINING.md
  USERS.md
  get-exports-code.js
  jest.config.js
  manual-releases.md
  patch-preact-package-json.js
  setup-tests.js
src/  (39 files)
  __mocks__/  (1 files)
    constants.js
  __tests__/  (23 files)
    __snapshots__/  (8 files)
      … 8 files under this directory
    .eslintrc
    create-glamorous.with-component.js
    dev.js
    index.filter-props.js
    index.js
    index.should-class-name-update.js
    index.with-config.js
    index.with-props.js
    preact.js
    refs.js
    should-forward-property.js
    theme-provider.js
    tiny.js
    typescript.js
    with-theme.js
  .eslintrc
  cjs-entry.js
  constants.js
  create-glamorous.js
  dom-elements.js
  get-glamor-classname.js
  index.js
  react-compat.js
  react-props.js
  should-forward-property.js
  split-props.js
  theme-provider.js
  tiny.js
  umd-entry.js
  with-theme.js
test/  (5 files)
  preact/  (2 files)
    glamorous.test.tsx
    should-fail.test.tsx
  glamorous-exports.test.ts
  glamorous.test.tsx
  should-fail.test.tsx
typings/  (22 files)
  preact/  (11 files)
    built-in-component-factories.d.ts
    built-in-glamorous-components.d.ts
    component-factory.d.ts
    css-properties.d.ts
    dom-tag-component-factory.d.ts
    glamorous-component.d.ts
    glamorous.d.ts
    helpers.d.ts
    named-built-in-glamorous-components.d.ts
    style-arguments.d.ts
    svg-properties.d.ts
  built-in-component-factories.d.ts
  built-in-glamorous-components.d.ts
  component-factory.d.ts
  css-properties.d.ts
  dom-tag-component-factory.d.ts
  glamorous-component.d.ts
  glamorous.d.ts
  helpers.d.ts
  named-built-in-glamorous-components.d.ts
  style-arguments.d.ts
  svg-properties.d.ts
.all-contributorsrc
.eslintignore
.gitattributes
.gitignore
.travis.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
jest.config.js
package.json
rollup.config.js
tsconfig.base.json
tsconfig.json
tsconfig.preact.json
tsconfig.react.json
tslint.json
```

## Entry points

- [examples/with-jest/index.js](https://github.com/paypal/glamorous/blob/031484cd5eff92ff135038200ba49a300859a335/examples/with-jest/index.js)
- [src/index.js](https://github.com/paypal/glamorous/blob/031484cd5eff92ff135038200ba49a300859a335/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cjs-entry.js package | library | Observed | Groups 1 file(s) under cjs-entry.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| create-glamorous.js package | library | Observed | Groups 1 file(s) under create-glamorous.js package (observed from repository paths and static analysis). |
| dom-elements.js package | library | Observed | Groups 1 file(s) under dom-elements.js package (observed from repository paths and static analysis). |
| get-glamor-classname.js package | library | Observed | Groups 1 file(s) under get-glamor-classname.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| other package | library | Observed | Groups 9 file(s) under other package (observed from repository paths and static analysis). |
| react-compat.js package | library | Observed | Groups 1 file(s) under react-compat.js package (observed from repository paths and static analysis). |
| react-props.js package | library | Observed | Groups 1 file(s) under react-props.js package (observed from repository paths and static analysis). |
| should-forward-property.js package | library | Observed | Groups 1 file(s) under should-forward-property.js package (observed from repository paths and static analysis). |
| split-props.js package | library | Observed | Groups 1 file(s) under split-props.js package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 19 file(s) under __tests__ package (observed from repository paths and static analysis). |
| theme-provider.js package | library | Observed | Groups 1 file(s) under theme-provider.js package (observed from repository paths and static analysis). |
| tiny.js package | library | Observed | Groups 1 file(s) under tiny.js package (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 22 file(s) under typings package (observed from repository paths and static analysis). |
| umd-entry.js package | library | Observed | Groups 1 file(s) under umd-entry.js package (observed from repository paths and static analysis). |
| with-theme.js package | library | Observed | Groups 1 file(s) under with-theme.js package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `examples/with-jest/package.json` (manifest)
- `other/codemods/package.json` (manifest)
- `package.json` (manifest)
- `tsconfig.base.json` (config)
- `tsconfig.json` (config)
- `tsconfig.preact.json` (config)
- `tsconfig.react.json` (config)
- `tslint.json` (config)

## Top-level layout

- `src` — 39 analysed file(s)
- `typings` — 22 analysed file(s)
- `other` — 19 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `examples` — 8 analysed file(s)
- `test` — 5 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `031484cd5eff92ff135038200ba49a300859a335` is the revision these paths and observations refer to.
