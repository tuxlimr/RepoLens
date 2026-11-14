# Project structure: jsx-eslint/eslint-plugin-react

**Analysed commit:** `61b91b612eed65386e1d2bda39b9afeb7c92c708`

**Commit reference:** [61b91b612eed65386e1d2bda39b9afeb7c92c708](https://github.com/jsx-eslint/eslint-plugin-react/commit/61b91b612eed65386e1d2bda39b9afeb7c92c708)

**Tree at this commit:** [jsx-eslint/eslint-plugin-react@61b91b612eed](https://github.com/jsx-eslint/eslint-plugin-react/tree/61b91b612eed65386e1d2bda39b9afeb7c92c708)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jsx-eslint/eslint-plugin-react |
| Description | React-specific linting rules for ESLint |
| Stars | 9291 |
| Forks | 2736 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `61b91b612eed65386e1d2bda39b9afeb7c92c708` |
| Retrieved at | 2026-11-14T19:13:34.659777+00:00 |
| Files in this snapshot | 412 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.yml
  workflows/  (10 files)
    eslint-8-.yml
    eslint-9+.yml
    node-minors.yml
    node-pretest.yml
    npm-publish.yml
    rebase.yml
    release.yml
    require-allow-edits.yml
    smoke-test.yml
    type-check.yml
  FUNDING.yml
configs/  (3 files)
  all.js
  jsx-runtime.js
  recommended.js
docs/  (104 files)
  rules/  (104 files)
    async-server-action.md
    boolean-prop-naming.md
    button-has-type.md
    checked-requires-onchange-or-readonly.md
    default-props-match-prop-types.md
    destructuring-assignment.md
    display-name.md
    forbid-component-props.md
    forbid-dom-props.md
    forbid-elements.md
    forbid-foreign-prop-types.md
    forbid-prop-types.md
    forward-ref-uses-ref.md
    function-component-definition.md
    hook-use-state.md
    iframe-missing-sandbox.md
    jsx-boolean-value.md
    jsx-child-element-spacing.md
    jsx-closing-bracket-location.md
    jsx-closing-tag-location.md
    jsx-curly-brace-presence.md
    jsx-curly-newline.md
    jsx-curly-spacing.md
    jsx-equals-spacing.md
    … 80 more files
lib/  (134 files)
  rules/  (105 files)
    async-server-action.js
    boolean-prop-naming.js
    button-has-type.js
    checked-requires-onchange-or-readonly.js
    default-props-match-prop-types.js
    destructuring-assignment.js
    display-name.js
    forbid-component-props.js
    forbid-dom-props.js
    forbid-elements.js
    forbid-foreign-prop-types.js
    forbid-prop-types.js
    forward-ref-uses-ref.js
    function-component-definition.js
    hook-use-state.js
    iframe-missing-sandbox.js
    index.js
    jsx-boolean-value.js
    jsx-child-element-spacing.js
    jsx-closing-bracket-location.js
    jsx-closing-tag-location.js
    jsx-curly-brace-presence.js
    jsx-curly-newline.js
    jsx-curly-spacing.js
    … 81 more files
  util/  (28 files)
    Components.js
    annotations.js
    ast.js
    componentUtil.js
    defaultProps.js
    docsUrl.js
    error.js
    eslint.js
    getTokenBeforeClosingBracket.js
    isCreateContext.js
    isCreateElement.js
    isDestructuredFromPragmaImport.js
    isFirstLetterCapitalized.js
    jsx.js
    lifecycleMethods.js
    linkComponents.js
    log.js
    makeNoMethodSetStateRule.js
    message.js
    pragma.js
    propTypes.js
    propTypesSort.js
    propWrapper.js
    props.js
    … 4 more files
  types.d.ts
test/  (2 files)
  eslint-remote-tester.config.js
  mocha.opts
test-published-types/  (3 files)
  index.js
  package.json
  tsconfig.json
tests/  (137 files)
  fixtures/  (18 files)
    flat-config/  (14 files)
      … 14 files under this directory
    version/  (4 files)
      … 4 files under this directory
  helpers/  (4 files)
    getESLintCoreRule.js
    getRuleDefiner.js
    parsers.js
    ruleTester.js
  lib/  (103 files)
    rules/  (103 files)
      … 103 files under this directory
  util/  (10 files)
    .eslintrc
    Components.js
    ast.js
    isFirstLetterCapitalized.js
    jsx.js
    linkComponents.js
    pragma.js
    propWrapper.js
    variable.js
    version.js
  flat-config.js
  index.js
types/  (3 files)
  rules/  (1 files)
    jsx-no-literals.d.ts
  string.prototype.repeat/  (1 files)
    index.d.ts
  eslint-core-augment.d.ts
.editorconfig
.eslint-doc-generatorrc.js
.eslintrc
.gitignore
.markdownlint.json
.markdownlintignore
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
build.tsconfig.json
index.js
package.json
tsconfig.json
```

## Entry points

- [index.js](https://github.com/jsx-eslint/eslint-plugin-react/blob/61b91b612eed65386e1d2bda39b9afeb7c92c708/index.js)
- [lib/rules/index.js](https://github.com/jsx-eslint/eslint-plugin-react/blob/61b91b612eed65386e1d2bda39b9afeb7c92c708/lib/rules/index.js)
- [test-published-types/index.js](https://github.com/jsx-eslint/eslint-plugin-react/blob/61b91b612eed65386e1d2bda39b9afeb7c92c708/test-published-types/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 134 file(s) under lib package (observed from repository paths and static analysis). |
| test-published-types package | library | Observed | Groups 1 file(s) under test-published-types package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 139 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 3 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/workflows/eslint-8-.yml` (ci)
- `.github/workflows/eslint-9+.yml` (ci)
- `.github/workflows/node-minors.yml` (ci)
- `.github/workflows/node-pretest.yml` (ci)
- `.github/workflows/npm-publish.yml` (ci)
- `.github/workflows/rebase.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/require-allow-edits.yml` (ci)
- `.github/workflows/smoke-test.yml` (ci)
- `.github/workflows/type-check.yml` (ci)
- `.markdownlint.json` (config)
- `build.tsconfig.json` (config)
- `package.json` (manifest)
- `test-published-types/package.json` (manifest)
- `test-published-types/tsconfig.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `tests` — 137 analysed file(s)
- `lib` — 134 analysed file(s)
- `docs` — 104 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 12 analysed file(s)
- `configs` — 3 analysed file(s)
- `test-published-types` — 3 analysed file(s)
- `types` — 3 analysed file(s)
- `test` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 13 file(s) were skipped during inventory (2 x likely secret file excluded; 11 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `61b91b612eed65386e1d2bda39b9afeb7c92c708` is the revision these paths and observations refer to.
