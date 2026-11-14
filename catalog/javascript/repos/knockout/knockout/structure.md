# Project structure: knockout/knockout

**Analysed commit:** `ab1f4b0e25c93ca2027bca84437ba5ec5e410b18`

**Commit reference:** [ab1f4b0e25c93ca2027bca84437ba5ec5e410b18](https://github.com/knockout/knockout/commit/ab1f4b0e25c93ca2027bca84437ba5ec5e410b18)

**Tree at this commit:** [knockout/knockout@ab1f4b0e25c9](https://github.com/knockout/knockout/tree/ab1f4b0e25c93ca2027bca84437ba5ec5e410b18)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | knockout/knockout |
| Description | Knockout makes it easier to create rich, responsive UIs with JavaScript |
| Stars | 10566 |
| Forks | 1482 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ab1f4b0e25c93ca2027bca84437ba5ec5e410b18` |
| Retrieved at | 2026-11-14T19:12:37.235977+00:00 |
| Files in this snapshot | 145 |

## Directory tree

```text
spec/  (80 files)
  components/  (4 files)
    componentBindingBehaviors.js
    customElementBehaviors.js
    defaultLoaderBehaviors.js
    loaderRegistryBehaviors.js
  defaultBindings/  (23 files)
    attrBehaviors.js
    checkedBehaviors.js
    clickBehaviors.js
    cssBehaviors.js
    enableDisableBehaviors.js
    eventBehaviors.js
    foreachBehaviors.js
    hasfocusBehaviors.js
    htmlBehaviors.js
    ifBehaviors.js
    ifnotBehaviors.js
    letBehaviors.js
    optionsBehaviors.js
    selectedOptionsBehaviors.js
    styleBehaviors.js
    submitBehaviors.js
    textBehaviors.js
    textInputBehaviors.js
    uniqueNameBehaviors.js
    usingBehaviors.js
    valueBehaviors.js
    visibleHiddenBehaviors.js
    withBehaviors.js
  lib/  (11 files)
    jasmine-1.2.0/  (5 files)
      … 5 files under this directory
    innershiv.js
    jasmine-results.js
    jasmine.extensions.css
    jasmine.extensions.js
    json2.js
    loadDependencies.js
  types/  (6 files)
    global/  (3 files)
      … 3 files under this directory
    module/  (3 files)
      … 3 files under this directory
  arrayEditDetectionBehaviors.js
  arrayToDomEditDetectionBehaviors.js
  asyncBehaviors.js
  asyncBindingBehaviors.js
  bindingAttributeBehaviors.js
  bindingDependencyBehaviors.js
  bindingPreprocessingBehaviors.js
  blank.html
  crossWindowBehaviors.js
  dependentObservableBehaviors.js
  dependentObservableDomBehaviors.js
  domNodeDisposalBehaviors.js
  e2e-tests.html
  expressionRewritingBehaviors.js
  extenderBehaviors.js
  jsonPostingBehaviors.js
  mappingHelperBehaviors.js
  memoizationBehaviors.js
  nativeTemplateEngineBehaviors.js
  nodePreprocessingBehaviors.js
  observableArrayBehaviors.js
  observableArrayChangeTrackingBehaviors.js
  observableBehaviors.js
  observableUtilsBehaviors.js
  … 12 more files
src/  (57 files)
  binding/  (27 files)
    defaultBindings/  (21 files)
      … 21 files under this directory
    editDetection/  (2 files)
      … 2 files under this directory
    bindingAttributeSyntax.js
    bindingProvider.js
    expressionRewriting.js
    selectExtensions.js
  components/  (4 files)
    componentBinding.js
    customElements.js
    defaultLoader.js
    loaderRegistry.js
  subscribables/  (9 files)
    dependencyDetection.js
    dependentObservable.js
    extenders.js
    mappingHelpers.js
    observable.js
    observableArray.changeTracking.js
    observableArray.js
    observableUtils.js
    subscribable.js
  templating/  (6 files)
    jquery.tmpl/  (1 files)
      … 1 files under this directory
    native/  (1 files)
      … 1 files under this directory
    templateEngine.js
    templateRewriting.js
    templateSources.js
    templating.js
  google-closure-compiler-utils.js
  memoization.js
  namespace.js
  options.js
  tasks.js
  utils.domData.js
  utils.domManipulation.js
  utils.domNodeDisposal.js
  utils.js
  version.js
  virtualElements.js
.gitignore
.npmignore
.travis.yml
Gruntfile.js
LICENSE
README.md
bower.json
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| binding package | library | Observed | Groups 27 file(s) under binding package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 4 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| google-closure-compiler-utils.js package | library | Observed | Groups 1 file(s) under google-closure-compiler-utils.js package (observed from repository paths and static analysis). |
| memoization.js package | library | Observed | Groups 1 file(s) under memoization.js package (observed from repository paths and static analysis). |
| namespace.js package | library | Observed | Groups 1 file(s) under namespace.js package (observed from repository paths and static analysis). |
| options.js package | library | Observed | Groups 1 file(s) under options.js package (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 72 file(s) under spec package (observed from repository paths and static analysis). |
| subscribables package | library | Observed | Groups 9 file(s) under subscribables package (observed from repository paths and static analysis). |
| tasks.js package | library | Observed | Groups 1 file(s) under tasks.js package (observed from repository paths and static analysis). |
| templating package | library | Observed | Groups 6 file(s) under templating package (observed from repository paths and static analysis). |
| utils.domData.js package | library | Observed | Groups 1 file(s) under utils.domdata.js package (observed from repository paths and static analysis). |
| utils.domManipulation.js package | library | Observed | Groups 1 file(s) under utils.dommanipulation.js package (observed from repository paths and static analysis). |
| utils.domNodeDisposal.js package | library | Observed | Groups 1 file(s) under utils.domnodedisposal.js package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| version.js package | library | Observed | Groups 1 file(s) under version.js package (observed from repository paths and static analysis). |
| virtualElements.js package | library | Observed | Groups 1 file(s) under virtualelements.js package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)
- `spec/types/global/tsconfig.json` (config)
- `spec/types/module/tsconfig.json` (config)

## Top-level layout

- `spec` — 80 analysed file(s)
- `src` — 57 analysed file(s)
- `(root files)` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 11 file(s) were skipped during inventory (1 x lockfile excluded; 10 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ab1f4b0e25c93ca2027bca84437ba5ec5e410b18` is the revision these paths and observations refer to.
