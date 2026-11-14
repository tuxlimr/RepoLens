# Project structure: final-form/react-final-form

**Analysed commit:** `e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c`

**Commit reference:** [e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c](https://github.com/final-form/react-final-form/commit/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c)

**Tree at this commit:** [final-form/react-final-form@e09c3cf983bc](https://github.com/final-form/react-final-form/tree/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | final-form/react-final-form |
| Description | 🏁 High performance subscription-based form state management for React |
| Stars | 7435 |
| Forks | 492 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c` |
| Retrieved at | 2026-11-14T19:13:51.117605+00:00 |
| Files in this snapshot | 297 |

## Directory tree

```text
.github/  (9 files)
  workflows/  (3 files)
    ci.yml
    lock.yml
    publish.yml
  CODEOWNERS
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
docs/  (28 files)
  api/  (6 files)
    Field.md
    Form.md
    FormSpy.md
    useField.md
    useForm.md
    useFormState.md
  examples/  (7 files)
    chakra.md
    field-level-validation.md
    record-level-validation.md
    simple.md
    submission-errors.md
    subscriptions.md
    wizard.md
  migration/  (2 files)
    formik.md
    redux-form.md
  types/  (6 files)
    FieldProps.md
    FieldRenderProps.md
    FormProps.md
    FormRenderProps.md
    FormSpyProps.md
    FormSpyRenderProps.md
  api.md
  examples.md
  faq.md
  getting-started.md
  logo.svg
  philosophy.md
  sencha.svg
examples/  (203 files)
  async-field-level-validation/  (5 files)
    Spinner.js
    Styles.js
    index.js
    package.json
    readme.md
  async-redux-submission/  (7 files)
    Styles.js
    asyncSubmissionMiddleware.js
    index.js
    package.json
    readme.md
    registrationDuck.js
    store.js
  async-typeahead-redux/  (8 files)
    GithubUserTypeahead.jsx
    Styles.js
    actions.js
    index.js
    package.json
    readme.md
    store.js
    useKeyword.js
  auto-save-field-blur/  (5 files)
    AutoSave.js
    Styles.js
    index.js
    package.json
    readme.md
  auto-save-selective-debounce/  (5 files)
    AutoSave.js
    Styles.js
    index.js
    package.json
    readme.md
  auto-save-with-debounce/  (5 files)
    AutoSave.js
    Styles.js
    index.js
    package.json
    readme.md
  calculated-fields/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  chakra/  (4 files)
    index.js
    package.json
    readme.md
    validate.js
  conditional-fields/  (5 files)
    Styles.js
    index.js
    package.json
    pickupTimes.js
    readme.md
  credit-card/  (7 files)
    Card.js
    Styles.js
    cardUtils.js
    index.js
    package.json
    readme.md
    sandbox.config.json
  custom-validation-engine/  (5 files)
    OnBlurValidation.js
    Styles.js
    index.js
    package.json
    readme.md
  debounced-record-level-validation/  (5 files)
    ErrorWithDelay.js
    README.md
    Styles.js
    index.js
    package.json
  declarative-form-rules/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  downshift-typeahead/  (6 files)
    DownshiftInput.js
    Styles.js
    fruit.js
    index.js
    package.json
    readme.md
  external-submit/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  field-arrays/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  field-level-validation/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  field-warnings/  (5 files)
    Styles.js
    index.js
    package.json
    readme.md
    warning-engine.js
  fields-component/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  focus-first-error/  (5 files)
    Styles.js
    index.js
    package.json
    readme.md
    validate.js
  format-on-blur/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  format-string-by-pattern/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  hybrid-sync-async-record-level-validation/  (5 files)
    Spinner.js
    Styles.js
    index.js
    package.json
    readme.md
  independent-error-component-render-props/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  independent-error-component-with-hooks/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  listening-for-external-changes/  (6 files)
    BooleanDecay.js
    ExternalModificationDetector.js
    Styles.js
    index.js
    package.json
    readme.md
  loading-initializing-values/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  loading-saving-reinitializing/  (5 files)
    LoadSaveReinitializeForm.js
    Styles.js
    index.js
    package.json
    readme.md
  material-ui/  (4 files)
    .prettierrc
    index.js
    package.json
    readme.md
  parse-format/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  prefixed-fields/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  record-level-validation/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  redux/  (8 files)
    FormStateFromRedux.js
    FormStateToRedux.js
    Styles.js
    finalFormDuck.js
    index.js
    package.json
    readme.md
    store.js
  reusable-field-groups/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  simple/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  strongly-typed-values-typescript/  (11 files)
    components/  (8 files)
      … 8 files under this directory
    Styles.tsx
    index.tsx
    readme.md
  styling-with-smooth-ui/  (3 files)
    index.js
    package.json
    readme.md
  submission-errors/  (4 files)
    Styles.js
    index.js
    package.json
    readme.md
  subscriptions/  (5 files)
    RenderCount.js
    Styles.js
    index.js
    package.json
    readme.md
  third-party-components/  (5 files)
    Styles.js
    index.js
    package.json
    readme.md
    states.js
  wizard/  (5 files)
    Styles.js
    Wizard.js
    index.js
    package.json
    readme.md
  readme.md
src/  (34 files)
  Field.test.js
  Field.tsx
  FormSpy.test.js
  FormSpy.tsx
  ReactFinalForm.test.js
  ReactFinalForm.tsx
  context.test.js
  context.ts
  getValue.test.js
  getValue.ts
  getters.ts
  index.ts
  isReactNative.ts
  isSyntheticEvent.ts
  renderComponent.test.js
  renderComponent.ts
  shallowEqual.test.js
  shallowEqual.ts
  testUtils.ts
  types.ts
  useConstant.ts
  useConstantCallback.test.js
  useConstantCallback.ts
  useField.dynamic-name-869.test.js
  … 10 more files
typescript/  (7 files)
  Field.test.tsx
  FormSpy.test.tsx
  ReactFinalForm.test.tsx
  index.d.ts
  tsconfig.json
  useField.test.tsx
  useFormState.test.tsx
.babelrc.js
.flowconfig
.gitignore
.prettierignore
.prettierrc
.travis.yml
LICENSE
MIGRATION_V7.md
README.md
eslint.config.mjs
package-scripts.js
package.json
rollup.config.mjs
tsconfig.build.json
tsconfig.json
tslint.json
```

## Entry points

- [examples/async-field-level-validation/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/async-field-level-validation/index.js)
- [examples/async-typeahead-redux/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/async-typeahead-redux/index.js)
- [examples/auto-save-field-blur/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/auto-save-field-blur/index.js)
- [examples/auto-save-selective-debounce/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/auto-save-selective-debounce/index.js)
- [examples/auto-save-with-debounce/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/auto-save-with-debounce/index.js)
- [examples/calculated-fields/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/calculated-fields/index.js)
- [examples/chakra/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/chakra/index.js)
- [examples/custom-validation-engine/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/custom-validation-engine/index.js)
- [examples/external-submit/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/external-submit/index.js)
- [examples/field-arrays/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/field-arrays/index.js)
- [examples/field-level-validation/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/field-level-validation/index.js)
- [examples/field-warnings/index.js](https://github.com/final-form/react-final-form/blob/e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c/examples/field-warnings/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| context.test.js package | library | Observed | Groups 1 file(s) under context.test.js package (observed from repository paths and static analysis). |
| context.ts package | library | Observed | Groups 1 file(s) under context.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Field.test.js package | library | Observed | Groups 1 file(s) under field.test.js package (observed from repository paths and static analysis). |
| Field.tsx package | library | Observed | Groups 1 file(s) under field.tsx package (observed from repository paths and static analysis). |
| FormSpy.test.js package | library | Observed | Groups 1 file(s) under formspy.test.js package (observed from repository paths and static analysis). |
| FormSpy.tsx package | library | Observed | Groups 1 file(s) under formspy.tsx package (observed from repository paths and static analysis). |
| getters.ts package | library | Observed | Groups 1 file(s) under getters.ts package (observed from repository paths and static analysis). |
| getValue.test.js package | library | Observed | Groups 1 file(s) under getvalue.test.js package (observed from repository paths and static analysis). |
| getValue.ts package | library | Observed | Groups 1 file(s) under getvalue.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| isReactNative.ts package | library | Observed | Groups 1 file(s) under isreactnative.ts package (observed from repository paths and static analysis). |
| isSyntheticEvent.ts package | library | Observed | Groups 1 file(s) under issyntheticevent.ts package (observed from repository paths and static analysis). |
| ReactFinalForm.test.js package | library | Observed | Groups 1 file(s) under reactfinalform.test.js package (observed from repository paths and static analysis). |
| ReactFinalForm.tsx package | library | Observed | Groups 1 file(s) under reactfinalform.tsx package (observed from repository paths and static analysis). |
| renderComponent.test.js package | library | Observed | Groups 1 file(s) under rendercomponent.test.js package (observed from repository paths and static analysis). |
| renderComponent.ts package | library | Observed | Groups 1 file(s) under rendercomponent.ts package (observed from repository paths and static analysis). |
| shallowEqual.test.js package | library | Observed | Groups 1 file(s) under shallowequal.test.js package (observed from repository paths and static analysis). |
| shallowEqual.ts package | library | Observed | Groups 1 file(s) under shallowequal.ts package (observed from repository paths and static analysis). |
| testUtils.ts package | library | Observed | Groups 1 file(s) under testutils.ts package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| typescript package | library | Observed | Groups 6 file(s) under typescript package (observed from repository paths and static analysis). |
| useConstant.ts package | library | Observed | Groups 1 file(s) under useconstant.ts package (observed from repository paths and static analysis). |
| useConstantCallback.test.js package | library | Observed | Groups 1 file(s) under useconstantcallback.test.js package (observed from repository paths and static analysis). |
| useConstantCallback.ts package | library | Observed | Groups 1 file(s) under useconstantcallback.ts package (observed from repository paths and static analysis). |
| useField.dynamic-name-869.test.js package | library | Observed | Groups 1 file(s) under usefield.dynamic-name-869.test.js package (observed from repository paths and static analysis). |
| useField.initialValue-change.test.js package | library | Observed | Groups 1 file(s) under usefield.initialvalue-change.test.js package (observed from repository paths and static analysis). |
| useField.issue-984.test.js package | library | Observed | Groups 1 file(s) under usefield.issue-984.test.js package (observed from repository paths and static analysis). |
| useField.test.js package | library | Observed | Groups 1 file(s) under usefield.test.js package (observed from repository paths and static analysis). |
| useField.ts package | library | Observed | Groups 1 file(s) under usefield.ts package (observed from repository paths and static analysis). |
| useForm.test.js package | library | Observed | Groups 1 file(s) under useform.test.js package (observed from repository paths and static analysis). |
| useForm.ts package | library | Observed | Groups 1 file(s) under useform.ts package (observed from repository paths and static analysis). |
| useFormState.test.js package | library | Observed | Groups 1 file(s) under useformstate.test.js package (observed from repository paths and static analysis). |
| useFormState.ts package | library | Observed | Groups 1 file(s) under useformstate.ts package (observed from repository paths and static analysis). |
| useLatest.ts package | library | Observed | Groups 1 file(s) under uselatest.ts package (observed from repository paths and static analysis). |
| useWhenValueChanges.ts package | library | Observed | Groups 1 file(s) under usewhenvaluechanges.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/lock.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.travis.yml` (ci)
- `examples/async-field-level-validation/package.json` (manifest)
- `examples/async-redux-submission/package.json` (manifest)
- `examples/async-typeahead-redux/package.json` (manifest)
- `examples/auto-save-field-blur/package.json` (manifest)
- `examples/auto-save-selective-debounce/package.json` (manifest)
- `examples/auto-save-with-debounce/package.json` (manifest)
- `examples/calculated-fields/package.json` (manifest)
- `examples/chakra/package.json` (manifest)
- `examples/conditional-fields/package.json` (manifest)
- `examples/credit-card/package.json` (manifest)
- `examples/credit-card/sandbox.config.json` (config)
- `examples/custom-validation-engine/package.json` (manifest)
- `examples/debounced-record-level-validation/package.json` (manifest)
- `examples/declarative-form-rules/package.json` (manifest)
- `examples/downshift-typeahead/package.json` (manifest)
- `examples/external-submit/package.json` (manifest)
- `examples/field-arrays/package.json` (manifest)
- `examples/field-level-validation/package.json` (manifest)
- `examples/field-warnings/package.json` (manifest)
- `examples/fields-component/package.json` (manifest)
- `examples/focus-first-error/package.json` (manifest)
- `examples/format-on-blur/package.json` (manifest)
- `examples/format-string-by-pattern/package.json` (manifest)
- `examples/hybrid-sync-async-record-level-validation/package.json` (manifest)
- `examples/independent-error-component-render-props/package.json` (manifest)
- `examples/independent-error-component-with-hooks/package.json` (manifest)
- `examples/listening-for-external-changes/package.json` (manifest)
- `examples/loading-initializing-values/package.json` (manifest)
- `examples/loading-saving-reinitializing/package.json` (manifest)
- `examples/material-ui/package.json` (manifest)
- `examples/parse-format/package.json` (manifest)
- `examples/prefixed-fields/package.json` (manifest)
- `examples/record-level-validation/package.json` (manifest)
- `examples/redux/package.json` (manifest)
- `examples/reusable-field-groups/package.json` (manifest)
- `examples/simple/package.json` (manifest)
- `examples/styling-with-smooth-ui/package.json` (manifest)
- `examples/submission-errors/package.json` (manifest)
- `examples/subscriptions/package.json` (manifest)
- `examples/third-party-components/package.json` (manifest)
- `examples/wizard/package.json` (manifest)
- `package.json` (manifest)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)
- `tslint.json` (config)
- `typescript/tsconfig.json` (config)

## Top-level layout

- `examples` — 203 analysed file(s)
- `src` — 34 analysed file(s)
- `docs` — 28 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 9 analysed file(s)
- `typescript` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e09c3cf983bcce7721c6b9dfbbabee6fe62bf83c` is the revision these paths and observations refer to.
