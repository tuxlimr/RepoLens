# Project structure: downshift-js/downshift

**Analysed commit:** `5c968318273c0a3b54e00a586f622aedc1fffffb`

**Commit reference:** [5c968318273c0a3b54e00a586f622aedc1fffffb](https://github.com/downshift-js/downshift/commit/5c968318273c0a3b54e00a586f622aedc1fffffb)

**Tree at this commit:** [downshift-js/downshift@5c968318273c](https://github.com/downshift-js/downshift/tree/5c968318273c0a3b54e00a586f622aedc1fffffb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | downshift-js/downshift |
| Description | 🏎 A set of primitives to build simple, flexible, WAI-ARIA compliant React autocomplete, combobox or select dropdown components. |
| Stars | 12301 |
| Forks | 931 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5c968318273c0a3b54e00a586f622aedc1fffffb` |
| Retrieved at | 2026-11-14T19:12:06.704971+00:00 |
| Files in this snapshot | 290 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    validate.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
docusaurus/  (14 files)
  pages/  (11 files)
    combobox.tsx
    index.tsx
    shared.css
    useCombobox.tsx
    useCombobox_compiled.jsx
    useMultipleCombobox.tsx
    useMultipleSelect.tsx
    useSelect.tsx
    useTagGroup.tsx
    useTagGroupCombobox.css
    useTagGroupCombobox.tsx
  plugins/  (1 files)
    webpack5polyfills.js
  tsconfig.json
  utils.ts
e2e/  (7 files)
  combobox.spec.ts
  tsconfig.json
  useCombobox.spec.ts
  useMultipleCombobox.spec.ts
  useMultipleSelect.spec.ts
  useSelect.spec.ts
  useTagGroup.spec.ts
flow-typed/  (1 files)
  npm/  (1 files)
    downshift_v2.x.x.js.flow
other/  (16 files)
  misc-tests/  (3 files)
    __tests__/  (2 files)
      … 2 files under this directory
    jest.config.js
  public/  (1 files)
    logo/  (1 files)
      … 1 files under this directory
  react-native/  (6 files)
    __tests__/  (4 files)
      … 4 files under this directory
    .babelrc
    jest.config.js
  ssr/  (2 files)
    __tests__/  (1 files)
      … 1 files under this directory
    jest.config.js
  MAINTAINING.md
  TYPESCRIPT_USAGE.md
  USERS.md
  manual-releases.md
src/  (216 files)
  __mocks__/  (2 files)
    set-a11y-status.js
    utils.js
  __tests__/  (29 files)
    __snapshots__/  (6 files)
      … 6 files under this directory
    .eslintrc
    downshift.aria.js
    downshift.focus-restoration.js
    downshift.get-button-props.js
    downshift.get-input-props.js
    downshift.get-item-props.js
    downshift.get-label-props.js
    downshift.get-menu-props.js
    downshift.get-root-props.js
    downshift.lifecycle.js
    downshift.misc-with-utils-mocked.js
    downshift.misc.js
    downshift.props.js
    portal-support.js
    set-a11y-status.js
    utils.call-all-event-handlers.js
    utils.get-a11y-status-message.js
    utils.get-highlighted-index.js
    utils.handle-refs.js
    utils.pick-state.js
    utils.reset-id-counter.js
    utils.reset-id-counter.r18.js
    utils.scroll-into-view.js
  hooks/  (144 files)
    testUtils/  (5 files)
      … 5 files under this directory
    useCombobox/  (25 files)
      … 25 files under this directory
    useMultipleSelection/  (14 files)
      … 14 files under this directory
    useSelect/  (23 files)
      … 23 files under this directory
    useTagGroup/  (26 files)
      … 26 files under this directory
    utils/  (46 files)
      … 46 files under this directory
    MIGRATION_V7.md
    MIGRATION_V8.md
    MIGRATION_V9.md
    README.md
    index.ts
  utils/  (32 files)
    __tests__/  (15 files)
      … 15 files under this directory
    callAllEventHandlers.ts
    debounce.ts
    generateId.ts
    getHighlightedIndex.ts
    getNonDisabledIndex.ts
    getState.ts
    handleRefs.ts
    index.ts
    noop.ts
    normalizeArrowKey.ts
    scrollIntoView.ts
    setA11yStatus.ts
    targetWithinDownshift.ts
    useIsomorphicLayoutEffect.ts
    useLatestRef.ts
    validateControlledUnchanged.ts
    validatePropTypes.ts
  downshift.js
  downshift.types.ts
  index.ts
  is.macro.d.ts
  is.macro.js
  productionEnum.macro.d.ts
  productionEnum.macro.js
  stateChangeTypes.js
  utils.legacy.js
test/  (11 files)
  basic.test.js
  basic.test.tsx
  custom.test.js
  custom.test.tsx
  downshift.test.tsx
  setup.ts
  tsconfig.json
  useCombobox.test.tsx
  useMultipleSelect.test.tsx
  useSelect.test.tsx
  useTagGroup.test.tsx
typings/  (1 files)
  index.d.ts
.all-contributorsrc
.flowconfig
.gitattributes
.gitignore
.nvmrc
.prettierignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
babel.config.js
docusaurus.config.js
jest.config.js
netlify.toml
package.json
playwright.config.ts
prettier.config.js
rollup.config.js
tsconfig.json
tsconfig.preact.json
```

## Entry points

- [docusaurus/pages/index.tsx](https://github.com/downshift-js/downshift/blob/5c968318273c0a3b54e00a586f622aedc1fffffb/docusaurus/pages/index.tsx)
- [src/hooks/index.ts](https://github.com/downshift-js/downshift/blob/5c968318273c0a3b54e00a586f622aedc1fffffb/src/hooks/index.ts)
- [src/hooks/testUtils/index.ts](https://github.com/downshift-js/downshift/blob/5c968318273c0a3b54e00a586f622aedc1fffffb/src/hooks/testUtils/index.ts)
- [src/hooks/useCombobox/index.ts](https://github.com/downshift-js/downshift/blob/5c968318273c0a3b54e00a586f622aedc1fffffb/src/hooks/useCombobox/index.ts)
- [src/hooks/useMultipleSelection/index.js](https://github.com/downshift-js/downshift/blob/5c968318273c0a3b54e00a586f622aedc1fffffb/src/hooks/useMultipleSelection/index.js)
- [src/hooks/useSelect/index.ts](https://github.com/downshift-js/downshift/blob/5c968318273c0a3b54e00a586f622aedc1fffffb/src/hooks/useSelect/index.ts)
- [src/hooks/useTagGroup/index.ts](https://github.com/downshift-js/downshift/blob/5c968318273c0a3b54e00a586f622aedc1fffffb/src/hooks/useTagGroup/index.ts)
- [src/hooks/utils/index.ts](https://github.com/downshift-js/downshift/blob/5c968318273c0a3b54e00a586f622aedc1fffffb/src/hooks/utils/index.ts)
- [src/index.ts](https://github.com/downshift-js/downshift/blob/5c968318273c0a3b54e00a586f622aedc1fffffb/src/index.ts)
- [src/utils/index.ts](https://github.com/downshift-js/downshift/blob/5c968318273c0a3b54e00a586f622aedc1fffffb/src/utils/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| docusaurus package | library | Observed | Groups 11 file(s) under docusaurus package (observed from repository paths and static analysis). |
| downshift.js package | library | Observed | Groups 1 file(s) under downshift.js package (observed from repository paths and static analysis). |
| downshift.types.ts package | library | Observed | Groups 1 file(s) under downshift.types.ts package (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 6 file(s) under e2e package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 133 file(s) under hooks package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| is.macro.d.ts package | library | Observed | Groups 1 file(s) under is.macro.d.ts package (observed from repository paths and static analysis). |
| is.macro.js package | library | Observed | Groups 1 file(s) under is.macro.js package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 2 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| other package | library | Observed | Groups 9 file(s) under other package (observed from repository paths and static analysis). |
| productionEnum.macro.d.ts package | library | Observed | Groups 1 file(s) under productionenum.macro.d.ts package (observed from repository paths and static analysis). |
| productionEnum.macro.js package | library | Observed | Groups 1 file(s) under productionenum.macro.js package (observed from repository paths and static analysis). |
| stateChangeTypes.js package | library | Observed | Groups 1 file(s) under statechangetypes.js package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 33 file(s) under __tests__ package (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 1 file(s) under typings package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 32 file(s) under utils package (observed from repository paths and static analysis). |
| utils.legacy.js package | library | Observed | Groups 1 file(s) under utils.legacy.js package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/validate.yml` (ci)
- `docusaurus/tsconfig.json` (config)
- `e2e/tsconfig.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tsconfig.preact.json` (config)

## Top-level layout

- `src` — 216 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `other` — 16 analysed file(s)
- `docusaurus` — 14 analysed file(s)
- `test` — 11 analysed file(s)
- `e2e` — 7 analysed file(s)
- `.github` — 3 analysed file(s)
- `flow-typed` — 1 analysed file(s)
- `typings` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5c968318273c0a3b54e00a586f622aedc1fffffb` is the revision these paths and observations refer to.
