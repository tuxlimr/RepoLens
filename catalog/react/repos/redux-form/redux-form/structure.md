# Project structure: redux-form/redux-form

**Analysed commit:** `88866f08120c1297daf54a5b887b90708e7f35e9`

**Commit reference:** [88866f08120c1297daf54a5b887b90708e7f35e9](https://github.com/redux-form/redux-form/commit/88866f08120c1297daf54a5b887b90708e7f35e9)

**Tree at this commit:** [redux-form/redux-form@88866f08120c](https://github.com/redux-form/redux-form/tree/88866f08120c1297daf54a5b887b90708e7f35e9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | redux-form/redux-form |
| Description | A Higher Order Component using react-redux to keep form state in a Redux store |
| Stars | 12473 |
| Forks | 1613 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `88866f08120c1297daf54a5b887b90708e7f35e9` |
| Retrieved at | 2026-11-14T19:13:20.228232+00:00 |
| Files in this snapshot | 330 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    1-bug.md
    2-feature.md
    config.yml
  funding.yml
  lock.yml
  pull-request-template.md
  security.md
  stale.yml
  support.md
docs/  (35 files)
  api/  (17 files)
    ActionCreators.md
    Field.md
    FieldArray.md
    Fields.md
    Form.md
    FormName.md
    FormSection.md
    FormValueSelector.md
    FormValues.md
    Props.md
    README.md
    Reducer.md
    ReducerPlugin.md
    ReduxForm.md
    ReduxFormContext.md
    Selectors.md
    SubmissionError.md
  faq/  (12 files)
    BundleSize.md
    ButtonType.md
    CustomComponent.md
    EnterToSubmit.md
    HandleVsOn.md
    HowToClear.md
    HowToConnect.md
    ImmutableJs.md
    README.md
    ReactNative.md
    SubmitFunction.md
    WebsocketSubmit.md
  DocumentationVersions.md
  Flow.md
  GettingStarted.md
  MigrationGuide.md
  ValueLifecycle.md
  sponsor.json
flow-typed/  (3 files)
  npm/  (3 files)
    jest_v25.x.x.js
    lodash_v4.x.x.js
    redux_v4.x.x.js
scripts/  (1 files)
  patch-immutable-flow-error.js
src/  (260 files)
  __tests__/  (63 files)
    helpers/  (36 files)
      … 36 files under this directory
    Field.spec.js
    FieldArray.spec.js
    Fields.spec.js
    Form.spec.js
    FormName.spec.js
    FormSection.spec.js
    SubmissionError.spec.js
    actions.spec.js
    asyncValidation.spec.js
    createFieldArrayProps.spec.js
    createFieldProps.spec.js
    defaultShouldAsyncValidate.spec.js
    defaultShouldError.spec.js
    defaultShouldValidate.spec.js
    defaultShouldWarn.spec.js
    deleteInWithCleanUp.spec.js
    formValueSelector.spec.js
    formValues.spec.js
    generateValidator.spec.js
    handleSubmit.spec.js
    hasError.spec.js
    immutable.spec.js
    index.spec.js
    reducer.spec.js
    … 3 more files
  events/  (10 files)
    __tests__/  (5 files)
      … 5 files under this directory
    getValue.js
    isEvent.js
    onChangeValue.js
    silenceEvent.js
    silenceEvents.js
  immutable/  (25 files)
    Field.js
    FieldArray.js
    Fields.js
    formValueSelector.js
    formValues.js
    getFormAsyncErrors.js
    getFormError.js
    getFormInitialValues.js
    getFormMeta.js
    getFormNames.js
    getFormSubmitErrors.js
    getFormSyncErrors.js
    getFormSyncWarnings.js
    getFormValues.js
    hasSubmitFailed.js
    hasSubmitSucceeded.js
    isAsyncValidating.js
    isDirty.js
    isInvalid.js
    isPristine.js
    isSubmitting.js
    isValid.js
    reducer.js
    reduxForm.js
    … 1 more files
  selectors/  (51 files)
    __tests__/  (17 files)
      … 17 files under this directory
    getFormAsyncErrors.js
    getFormAsyncErrors.types.js.flow
    getFormError.js
    getFormError.types.js.flow
    getFormInitialValues.js
    getFormInitialValues.types.js.flow
    getFormMeta.js
    getFormMeta.types.js.flow
    getFormNames.js
    getFormNames.types.js.flow
    getFormSubmitErrors.js
    getFormSubmitErrors.types.js.flow
    getFormSyncErrors.js
    getFormSyncErrors.types.js.flow
    getFormSyncWarnings.js
    getFormSyncWarnings.types.js.flow
    getFormValues.js
    getFormValues.types.js.flow
    hasSubmitFailed.js
    hasSubmitFailed.types.js.flow
    hasSubmitSucceeded.js
    hasSubmitSucceeded.types.js.flow
    isAsyncValidating.js
    isAsyncValidating.types.js.flow
    … 10 more files
  structure/  (24 files)
    immutable/  (10 files)
      … 10 files under this directory
    plain/  (14 files)
      … 14 files under this directory
  util/  (12 files)
    __tests__/  (4 files)
      … 4 files under this directory
    FormNameProps.types.js.flow.js
    eventConsts.js
    eventMocks.js
    getDisplayName.js
    isHotReloading.js
    prefixName.js
    shallowCompare.js
    validateComponentProp.js
  ConnectedField.js
  ConnectedField.types.js.flow
  ConnectedFieldArray.js
  ConnectedFieldArray.types.js.flow
  ConnectedFields.js
  ConnectedFields.types.js.flow
  Field.js
  FieldArray.js
  FieldArrayProps.types.js.flow
  FieldProps.types.js.flow
  Fields.js
  FieldsProps.types.js.flow
  Form.js
  FormName.js
  FormNameProps.types.js.flow
  FormSection.js
  ReduxFormContext.js
  SubmissionError.js
  actionTypes.js
  actionTypes.types.js.flow
  actions.js
  actions.types.js.flow
  asyncValidation.js
  createField.js
  … 51 more files
.babelrc.js
.codeclimate.yml
.editorconfig
.eslintignore
.eslintrc
.flowconfig
.gitignore
.npmignore
.nvmrc
.prettierignore
.prettierrc
.size-limit.json
.travis.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
immutable.js
package.json
tools.md
webpack.config.js
```

## Entry points

- [src/index.js](https://github.com/redux-form/redux-form/blob/88866f08120c1297daf54a5b887b90708e7f35e9/src/index.js)
- [src/structure/immutable/index.js](https://github.com/redux-form/redux-form/blob/88866f08120c1297daf54a5b887b90708e7f35e9/src/structure/immutable/index.js)
- [src/structure/plain/index.js](https://github.com/redux-form/redux-form/blob/88866f08120c1297daf54a5b887b90708e7f35e9/src/structure/plain/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| actions.js package | library | Observed | Groups 1 file(s) under actions.js package (observed from repository paths and static analysis). |
| actionTypes.js package | library | Observed | Groups 1 file(s) under actiontypes.js package (observed from repository paths and static analysis). |
| asyncValidation.js package | library | Observed | Groups 1 file(s) under asyncvalidation.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| ConnectedField.js package | library | Observed | Groups 1 file(s) under connectedfield.js package (observed from repository paths and static analysis). |
| ConnectedFieldArray.js package | library | Observed | Groups 1 file(s) under connectedfieldarray.js package (observed from repository paths and static analysis). |
| ConnectedFields.js package | library | Observed | Groups 1 file(s) under connectedfields.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| createField.js package | library | Observed | Groups 1 file(s) under createfield.js package (observed from repository paths and static analysis). |
| createFieldArray.js package | library | Observed | Groups 1 file(s) under createfieldarray.js package (observed from repository paths and static analysis). |
| createFieldArrayProps.js package | library | Observed | Groups 1 file(s) under createfieldarrayprops.js package (observed from repository paths and static analysis). |
| createFieldProps.js package | library | Observed | Groups 1 file(s) under createfieldprops.js package (observed from repository paths and static analysis). |
| createFields.js package | library | Observed | Groups 1 file(s) under createfields.js package (observed from repository paths and static analysis). |
| createFormValues.js package | library | Observed | Groups 1 file(s) under createformvalues.js package (observed from repository paths and static analysis). |
| createFormValueSelector.js package | library | Observed | Groups 1 file(s) under createformvalueselector.js package (observed from repository paths and static analysis). |
| createReducer.js package | library | Observed | Groups 1 file(s) under createreducer.js package (observed from repository paths and static analysis). |
| createReduxForm.js package | library | Observed | Groups 1 file(s) under createreduxform.js package (observed from repository paths and static analysis). |
| createValues.js package | library | Observed | Groups 1 file(s) under createvalues.js package (observed from repository paths and static analysis). |
| defaultShouldAsyncValidate.js package | library | Observed | Groups 1 file(s) under defaultshouldasyncvalidate.js package (observed from repository paths and static analysis). |
| defaultShouldError.js package | library | Observed | Groups 1 file(s) under defaultshoulderror.js package (observed from repository paths and static analysis). |
| defaultShouldValidate.js package | library | Observed | Groups 1 file(s) under defaultshouldvalidate.js package (observed from repository paths and static analysis). |
| defaultShouldWarn.js package | library | Observed | Groups 1 file(s) under defaultshouldwarn.js package (observed from repository paths and static analysis). |
| deleteInWithCleanUp.js package | library | Observed | Groups 1 file(s) under deleteinwithcleanup.js package (observed from repository paths and static analysis). |
| events package | library | Observed | Groups 10 file(s) under events package (observed from repository paths and static analysis). |
| Field.js package | library | Observed | Groups 1 file(s) under field.js package (observed from repository paths and static analysis). |
| FieldArray.js package | library | Observed | Groups 1 file(s) under fieldarray.js package (observed from repository paths and static analysis). |
| fieldKeys.js package | library | Observed | Groups 1 file(s) under fieldkeys.js package (observed from repository paths and static analysis). |
| Fields.js package | library | Observed | Groups 1 file(s) under fields.js package (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 3 file(s) under flow-typed package (observed from repository paths and static analysis). |
| Form.js package | library | Observed | Groups 1 file(s) under form.js package (observed from repository paths and static analysis). |
| FormName.js package | library | Observed | Groups 1 file(s) under formname.js package (observed from repository paths and static analysis). |
| FormSection.js package | library | Observed | Groups 1 file(s) under formsection.js package (observed from repository paths and static analysis). |
| formValues.js package | library | Observed | Groups 1 file(s) under formvalues.js package (observed from repository paths and static analysis). |
| formValueSelector.js package | library | Observed | Groups 1 file(s) under formvalueselector.js package (observed from repository paths and static analysis). |
| generateFields.js package | library | Observed | Groups 1 file(s) under generatefields.js package (observed from repository paths and static analysis). |
| generateValidator.js package | library | Observed | Groups 1 file(s) under generatevalidator.js package (observed from repository paths and static analysis). |
| getFormAsyncErrors.js package | library | Observed | Groups 1 file(s) under getformasyncerrors.js package (observed from repository paths and static analysis). |
| getFormError.js package | library | Observed | Groups 1 file(s) under getformerror.js package (observed from repository paths and static analysis). |
| getFormInitialValues.js package | library | Observed | Groups 1 file(s) under getforminitialvalues.js package (observed from repository paths and static analysis). |
| getFormMeta.js package | library | Observed | Groups 1 file(s) under getformmeta.js package (observed from repository paths and static analysis). |
| getFormNames.js package | library | Observed | Groups 1 file(s) under getformnames.js package (observed from repository paths and static analysis). |
| getFormSubmitErrors.js package | library | Observed | Groups 1 file(s) under getformsubmiterrors.js package (observed from repository paths and static analysis). |
| getFormSyncErrors.js package | library | Observed | Groups 1 file(s) under getformsyncerrors.js package (observed from repository paths and static analysis). |
| getFormSyncWarnings.js package | library | Observed | Groups 1 file(s) under getformsyncwarnings.js package (observed from repository paths and static analysis). |
| getFormValues.js package | library | Observed | Groups 1 file(s) under getformvalues.js package (observed from repository paths and static analysis). |
| handleSubmit.js package | library | Observed | Groups 1 file(s) under handlesubmit.js package (observed from repository paths and static analysis). |
| hasError.js package | library | Observed | Groups 1 file(s) under haserror.js package (observed from repository paths and static analysis). |
| hasSubmitFailed.js package | library | Observed | Groups 1 file(s) under hassubmitfailed.js package (observed from repository paths and static analysis). |
| hasSubmitSucceeded.js package | library | Observed | Groups 1 file(s) under hassubmitsucceeded.js package (observed from repository paths and static analysis). |
| immutable package | library | Observed | Groups 25 file(s) under immutable package (observed from repository paths and static analysis). |
| immutable.js package | library | Observed | Groups 1 file(s) under immutable.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| isAsyncValidating.js package | library | Observed | Groups 1 file(s) under isasyncvalidating.js package (observed from repository paths and static analysis). |
| isDirty.js package | library | Observed | Groups 1 file(s) under isdirty.js package (observed from repository paths and static analysis). |
| isInvalid.js package | library | Observed | Groups 1 file(s) under isinvalid.js package (observed from repository paths and static analysis). |
| isPristine.js package | library | Observed | Groups 1 file(s) under ispristine.js package (observed from repository paths and static analysis). |
| isReactNative.js package | library | Observed | Groups 1 file(s) under isreactnative.js package (observed from repository paths and static analysis). |
| isSubmitting.js package | library | Observed | Groups 1 file(s) under issubmitting.js package (observed from repository paths and static analysis). |
| isValid.js package | library | Observed | Groups 1 file(s) under isvalid.js package (observed from repository paths and static analysis). |
| propTypes.js package | library | Observed | Groups 1 file(s) under proptypes.js package (observed from repository paths and static analysis). |
| reducer.js package | library | Observed | Groups 1 file(s) under reducer.js package (observed from repository paths and static analysis). |
| reduxForm.js package | library | Observed | Groups 1 file(s) under reduxform.js package (observed from repository paths and static analysis). |
| ReduxFormContext.js package | library | Observed | Groups 1 file(s) under reduxformcontext.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| selectors package | library | Observed | Groups 34 file(s) under selectors package (observed from repository paths and static analysis). |
| structure package | library | Observed | Groups 24 file(s) under structure package (observed from repository paths and static analysis). |
| SubmissionError.js package | library | Observed | Groups 1 file(s) under submissionerror.js package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 63 file(s) under __tests__ package (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 12 file(s) under util package (observed from repository paths and static analysis). |
| values.js package | library | Observed | Groups 1 file(s) under values.js package (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/funding.yml` (config)
- `.github/lock.yml` (config)
- `.github/stale.yml` (config)
- `.size-limit.json` (config)
- `.travis.yml` (ci)
- `docs/sponsor.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 260 analysed file(s)
- `docs` — 35 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `.github` — 9 analysed file(s)
- `flow-typed` — 3 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `88866f08120c1297daf54a5b887b90708e7f35e9` is the revision these paths and observations refer to.
