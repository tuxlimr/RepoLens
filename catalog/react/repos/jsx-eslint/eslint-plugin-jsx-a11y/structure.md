# Project structure: jsx-eslint/eslint-plugin-jsx-a11y

**Analysed commit:** `8f75961d965e47afb88854d324bd32fafde7acfe`

**Commit reference:** [8f75961d965e47afb88854d324bd32fafde7acfe](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/commit/8f75961d965e47afb88854d324bd32fafde7acfe)

**Tree at this commit:** [jsx-eslint/eslint-plugin-jsx-a11y@8f75961d965e](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/tree/8f75961d965e47afb88854d324bd32fafde7acfe)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jsx-eslint/eslint-plugin-jsx-a11y |
| Description | Static AST checker for a11y rules on JSX elements. |
| Stars | 3631 |
| Forks | 659 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `8f75961d965e47afb88854d324bd32fafde7acfe` |
| Retrieved at | 2026-11-14T19:15:11.355562+00:00 |
| Files in this snapshot | 274 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (5 files)
    node-4+.yml
    node-pretest.yml
    readme.yml
    rebase.yml
    require-allow-edits.yml
__mocks__/  (8 files)
  IdentifierMock.js
  JSXAttributeMock.js
  JSXElementMock.js
  JSXExpressionContainerMock.js
  JSXSpreadAttributeMock.js
  JSXTextMock.js
  LiteralMock.js
  genInteractives.js
__tests__/  (74 files)
  __util__/  (6 files)
    helpers/  (2 files)
      … 2 files under this directory
    RuleTester.js
    axeMapping.js
    parserOptionsMapper.js
    ruleOptionsMapperFactory.js
  src/  (67 files)
    rules/  (39 files)
      … 39 files under this directory
    util/  (28 files)
      … 28 files under this directory
  index-test.js
docs/  (39 files)
  rules/  (39 files)
    accessible-emoji.md
    alt-text.md
    anchor-ambiguous-text.md
    anchor-has-content.md
    anchor-is-valid.md
    aria-activedescendant-has-tabindex.md
    aria-props.md
    aria-proptypes.md
    aria-role.md
    aria-unsupported-elements.md
    autocomplete-valid.md
    click-events-have-key-events.md
    control-has-associated-label.md
    heading-has-content.md
    html-has-lang.md
    iframe-has-title.md
    img-redundant-alt.md
    interactive-supports-focus.md
    label-has-associated-control.md
    label-has-for.md
    lang.md
    media-has-caption.md
    mouse-events-have-key-events.md
    no-access-key.md
    … 15 more files
examples/  (27 files)
  flat-cjs/  (9 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    eslint.config.cjs
    index.html
    package.json
  flat-esm/  (9 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    eslint.config.js
    index.html
    package.json
  legacy/  (9 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .eslintrc.cjs
    index.html
    package.json
flow/  (2 files)
  eslint-jsx.js
  eslint.js
scripts/  (6 files)
  boilerplate/  (3 files)
    doc.js
    rule.js
    test.js
  addRuleToIndex.js
  create-rule.js
  create-rule.md
src/  (104 files)
  configs/  (2 files)
    flat-config-base.js
    legacy-config-base.js
  rules/  (39 files)
    accessible-emoji.js
    alt-text.js
    anchor-ambiguous-text.js
    anchor-has-content.js
    anchor-is-valid.js
    aria-activedescendant-has-tabindex.js
    aria-props.js
    aria-proptypes.js
    aria-role.js
    aria-unsupported-elements.js
    autocomplete-valid.js
    click-events-have-key-events.js
    control-has-associated-label.js
    heading-has-content.js
    html-has-lang.js
    iframe-has-title.js
    img-redundant-alt.js
    interactive-supports-focus.js
    label-has-associated-control.js
    label-has-for.js
    lang.js
    media-has-caption.js
    mouse-events-have-key-events.js
    no-access-key.js
    … 15 more files
  util/  (62 files)
    implicitRoles/  (37 files)
      … 37 files under this directory
    attributesComparator.js
    getAccessibleChildText.js
    getComputedRole.js
    getElementType.js
    getExplicitRole.js
    getImplicitRole.js
    getSuggestion.js
    getTabIndex.js
    hasAccessibleChild.js
    isAbstractRole.js
    isContentEditable.js
    isDOMElement.js
    isDisabledElement.js
    isFocusable.js
    isHiddenFromScreenReader.js
    isInteractiveElement.js
    isInteractiveRole.js
    isNonInteractiveElement.js
    isNonInteractiveRole.js
    isNonLiteralProperty.js
    isPresentationRole.js
    isSemanticRoleElement.js
    mayContainChildComponent.js
    mayHaveAccessibleLabel.js
    … 1 more files
  index.js
.babelrc
.eslintrc
.flowconfig
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE.md
README.md
package.json
```

## Entry points

- [src/index.js](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/8f75961d965e47afb88854d324bd32fafde7acfe/src/index.js)
- [src/util/implicitRoles/index.js](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/8f75961d965e47afb88854d324bd32fafde7acfe/src/util/implicitRoles/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| flow package | library | Observed | Groups 2 file(s) under flow package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 8 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| rules package | library | Observed | Groups 39 file(s) under rules package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 74 file(s) under __tests__ package (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 62 file(s) under util package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/node-4+.yml` (ci)
- `.github/workflows/node-pretest.yml` (ci)
- `.github/workflows/readme.yml` (ci)
- `.github/workflows/rebase.yml` (ci)
- `.github/workflows/require-allow-edits.yml` (ci)
- `examples/flat-cjs/package.json` (manifest)
- `examples/flat-esm/package.json` (manifest)
- `examples/legacy/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `src` — 104 analysed file(s)
- `__tests__` — 74 analysed file(s)
- `docs` — 39 analysed file(s)
- `examples` — 27 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `__mocks__` — 8 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `flow` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8f75961d965e47afb88854d324bd32fafde7acfe` is the revision these paths and observations refer to.
