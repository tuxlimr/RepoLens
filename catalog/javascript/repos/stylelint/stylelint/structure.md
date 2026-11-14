# Project structure: stylelint/stylelint

**Analysed commit:** `ee4f118acae33876a93ced5866872328e36660c2`

**Commit reference:** [ee4f118acae33876a93ced5866872328e36660c2](https://github.com/stylelint/stylelint/commit/ee4f118acae33876a93ced5866872328e36660c2)

**Tree at this commit:** [stylelint/stylelint@ee4f118acae3](https://github.com/stylelint/stylelint/tree/ee4f118acae33876a93ced5866872328e36660c2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | stylelint/stylelint |
| Description | A mighty CSS linter that helps you avoid errors and enforce conventions. |
| Stars | 11550 |
| Forks | 1029 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `ee4f118acae33876a93ced5866872328e36660c2` |
| Retrieved at | 2026-11-14T19:12:16.643862+00:00 |
| Files in this snapshot | 797 |

## Directory tree

```text
.changeset/  (15 files)
  README.md
  better-years-greet.md
  changelog-stylelint.mjs
  changelog-stylelint.test.mjs
  config.json
  early-moments-attend.md
  fair-seals-camp.md
  full-taxis-grow.md
  gentle-lizards-crash.md
  get-github-info.mock.mjs
  legal-colts-attend.md
  puny-monkeys-draw.md
  rewrite-changelog.mjs
  smart-jars-decide.md
  twenty-flowers-retire.md
.githooks/  (1 files)
  pre-commit
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    REPORT_A_BUG.yml
    REPORT_A_DOCS_ISSUE.yml
    REQUEST_A_FEATURE.yml
  workflows/  (7 files)
    ci.yml
    close-unknown-effort-prs.yml
    comment-on-old-issues.yml
    publish-to-pkg.pr.new.yml
    release-pr.yml
    release.yml
    update-pkg.pr.new-comment.yml
  CODEOWNERS
  dependabot.yml
bin/  (1 files)
  stylelint.mjs
docs/  (29 files)
  about/  (3 files)
    governance.md
    semantic-versioning.md
    vision.md
  contributor-guide/  (4 files)
    benchmarks.md
    glossary.md
    rules.md
    system-tests.md
  developer-guide/  (3 files)
    formatters.md
    plugins.md
    syntaxes.md
  maintainer-guide/  (3 files)
    issues.md
    pull-requests.md
    releases.md
  migration-guide/  (5 files)
    to-14.md
    to-15.md
    to-16.md
    to-17.md
    to-18.md
  user-guide/  (11 files)
    cli.md
    configure.md
    customize.md
    errors.md
    get-started.md
    ignore-code.md
    node-api.md
    options.md
    postcss-plugin.md
    rules.md
    suppressions.md
identity/  (6 files)
  credits.md
  stylelint-icon-and-text-white-square.svg
  stylelint-icon-black.svg
  stylelint-icon-white.svg
  stylelint-text-black.svg
  stylelint-text-white.svg
lib/  (721 files)
  __tests__/  (208 files)
    fixtures/  (142 files)
      … 142 files under this directory
    standalone-glob-parent-test/  (4 files)
      … 4 files under this directory
    stylelintignore-test/  (9 files)
      … 9 files under this directory
    .stylelintignore
    applyOverrides.test.mjs
    cli-suppressions.test.mjs
    cli.test.mjs
    cli.test.mjs.snapshot
    constants.test.mjs
    defaultSeverity.test.mjs
    descriptionlessDisables.test.mjs
    disableRanges-integration.test.mjs
    disableRanges.test.mjs
    extends.test.mjs
    formatters.test.mjs
    getConfigForFile.test.mjs
    getPostcssResult.test.mjs
    ignore.test.mjs
    ignoreDisables.test.mjs
    integration.test.mjs
    invalidScopeDisables.test.mjs
    isPathIgnored.test.mjs
    languageOptions.test.mjs
    message.test.mjs
    needlessDisables.test.mjs
    normalizeRuleSettings-integration.test.mjs
    normalizeRuleSettings.test.mjs
    … 29 more files
  formatters/  (19 files)
    __tests__/  (8 files)
      … 8 files under this directory
    calcSeverityCounts.mjs
    compactFormatter.mjs
    index.mjs
    jsonFormatter.mjs
    preprocessWarnings.mjs
    stringFormatter.mjs
    tapFormatter.mjs
    terminalLink.mjs
    unixFormatter.mjs
    verboseFormatter.mjs
    wrapText.mjs
  reference/  (10 files)
    __tests__/  (1 files)
      … 1 files under this directory
    atKeywords.mjs
    functions.mjs
    keywords.mjs
    mediaFeatures.mjs
    mediaTypes.mjs
    prefixes.mjs
    properties.mjs
    selectors.mjs
    units.mjs
  rules/  (460 files)
    __tests__/  (1 files)
      … 1 files under this directory
    alpha-value-notation/  (3 files)
      … 3 files under this directory
    annotation-no-unknown/  (3 files)
      … 3 files under this directory
    at-charset-rule-no-invalid/  (3 files)
      … 3 files under this directory
    at-rule-allowed-list/  (3 files)
      … 3 files under this directory
    at-rule-descriptor-no-unknown/  (3 files)
      … 3 files under this directory
    at-rule-descriptor-value-no-unknown/  (3 files)
      … 3 files under this directory
    at-rule-disallowed-list/  (3 files)
      … 3 files under this directory
    at-rule-empty-line-before/  (3 files)
      … 3 files under this directory
    at-rule-no-deprecated/  (3 files)
      … 3 files under this directory
    at-rule-no-unknown/  (3 files)
      … 3 files under this directory
    at-rule-no-vendor-prefix/  (3 files)
      … 3 files under this directory
    at-rule-prelude-no-invalid/  (3 files)
      … 3 files under this directory
    at-rule-property-required-list/  (3 files)
      … 3 files under this directory
    block-no-empty/  (3 files)
      … 3 files under this directory
    block-no-redundant-nested-style-rules/  (3 files)
      … 3 files under this directory
    color-function-alias-notation/  (3 files)
      … 3 files under this directory
    color-function-notation/  (3 files)
      … 3 files under this directory
    color-hex-alpha/  (3 files)
      … 3 files under this directory
    color-hex-length/  (3 files)
      … 3 files under this directory
    color-named/  (5 files)
      … 5 files under this directory
    color-no-hex/  (3 files)
      … 3 files under this directory
    color-no-invalid-hex/  (3 files)
      … 3 files under this directory
    comment-empty-line-before/  (3 files)
      … 3 files under this directory
    comment-no-empty/  (3 files)
      … 3 files under this directory
    comment-pattern/  (3 files)
      … 3 files under this directory
    comment-whitespace-inside/  (3 files)
      … 3 files under this directory
    comment-word-disallowed-list/  (3 files)
      … 3 files under this directory
    container-name-pattern/  (3 files)
      … 3 files under this directory
    custom-media-pattern/  (3 files)
      … 3 files under this directory
    custom-property-empty-line-before/  (3 files)
      … 3 files under this directory
    custom-property-no-missing-var-function/  (3 files)
      … 3 files under this directory
    custom-property-pattern/  (3 files)
      … 3 files under this directory
    declaration-block-no-duplicate-custom-properties/  (3 files)
      … 3 files under this directory
    declaration-block-no-duplicate-properties/  (3 files)
      … 3 files under this directory
    declaration-block-no-redundant-longhand-properties/  (3 files)
      … 3 files under this directory
    declaration-block-no-shorthand-property-overrides/  (3 files)
      … 3 files under this directory
    declaration-empty-line-before/  (3 files)
      … 3 files under this directory
    declaration-no-important/  (3 files)
      … 3 files under this directory
    declaration-property-custom-property-allowed-list/  (3 files)
      … 3 files under this directory
    declaration-property-max-values/  (3 files)
      … 3 files under this directory
    declaration-property-unit-allowed-list/  (3 files)
      … 3 files under this directory
    declaration-property-unit-disallowed-list/  (3 files)
      … 3 files under this directory
    declaration-property-value-allowed-list/  (3 files)
      … 3 files under this directory
    declaration-property-value-disallowed-list/  (3 files)
      … 3 files under this directory
    declaration-property-value-keyword-no-deprecated/  (3 files)
      … 3 files under this directory
    declaration-property-value-no-unknown/  (3 files)
      … 3 files under this directory
    display-notation/  (3 files)
      … 3 files under this directory
    font-family-name-quotes/  (3 files)
      … 3 files under this directory
    font-family-no-duplicate-names/  (3 files)
      … 3 files under this directory
    font-family-no-missing-generic-family-keyword/  (3 files)
      … 3 files under this directory
    font-weight-notation/  (3 files)
      … 3 files under this directory
    function-allowed-list/  (3 files)
      … 3 files under this directory
    function-calc-no-unspaced-operator/  (3 files)
      … 3 files under this directory
    function-disallowed-list/  (3 files)
      … 3 files under this directory
    function-linear-gradient-no-nonstandard-direction/  (3 files)
      … 3 files under this directory
    function-name-case/  (3 files)
      … 3 files under this directory
    function-no-unknown/  (3 files)
      … 3 files under this directory
    function-url-no-scheme-relative/  (3 files)
      … 3 files under this directory
    function-url-quotes/  (3 files)
      … 3 files under this directory
    function-url-scheme-allowed-list/  (3 files)
      … 3 files under this directory
    function-url-scheme-disallowed-list/  (3 files)
      … 3 files under this directory
    hue-degree-notation/  (3 files)
      … 3 files under this directory
    import-notation/  (3 files)
      … 3 files under this directory
    keyframe-block-no-duplicate-selectors/  (3 files)
      … 3 files under this directory
    keyframe-declaration-no-important/  (3 files)
      … 3 files under this directory
    keyframe-selector-notation/  (3 files)
      … 3 files under this directory
    keyframes-name-pattern/  (3 files)
      … 3 files under this directory
    layer-name-pattern/  (3 files)
      … 3 files under this directory
    length-zero-no-unit/  (3 files)
      … 3 files under this directory
    lightness-notation/  (3 files)
      … 3 files under this directory
    max-nesting-depth/  (3 files)
      … 3 files under this directory
    media-feature-name-allowed-list/  (3 files)
      … 3 files under this directory
    media-feature-name-disallowed-list/  (3 files)
      … 3 files under this directory
    media-feature-name-no-unknown/  (3 files)
      … 3 files under this directory
    media-feature-name-no-vendor-prefix/  (3 files)
      … 3 files under this directory
    media-feature-name-unit-allowed-list/  (3 files)
      … 3 files under this directory
    media-feature-name-value-allowed-list/  (3 files)
      … 3 files under this directory
    media-feature-name-value-no-unknown/  (3 files)
      … 3 files under this directory
    media-feature-range-notation/  (3 files)
      … 3 files under this directory
    media-query-no-invalid/  (3 files)
      … 3 files under this directory
    media-type-no-deprecated/  (3 files)
      … 3 files under this directory
    named-grid-areas-no-invalid/  (5 files)
      … 5 files under this directory
    nesting-selector-no-missing-scoping-root/  (3 files)
      … 3 files under this directory
    no-descending-specificity/  (3 files)
      … 3 files under this directory
    no-duplicate-at-import-rules/  (3 files)
      … 3 files under this directory
    no-duplicate-selectors/  (6 files)
      … 6 files under this directory
    no-empty-source/  (3 files)
      … 3 files under this directory
    no-invalid-double-slash-comments/  (3 files)
      … 3 files under this directory
    no-invalid-position-at-import-rule/  (3 files)
      … 3 files under this directory
    no-invalid-position-declaration/  (3 files)
      … 3 files under this directory
    no-irregular-whitespace/  (3 files)
      … 3 files under this directory
    no-unknown-animations/  (3 files)
      … 3 files under this directory
    no-unknown-custom-media/  (3 files)
      … 3 files under this directory
    no-unknown-custom-properties/  (3 files)
      … 3 files under this directory
    number-max-precision/  (3 files)
      … 3 files under this directory
    property-allowed-list/  (3 files)
      … 3 files under this directory
    property-disallowed-list/  (3 files)
      … 3 files under this directory
    property-layout-mappings/  (3 files)
      … 3 files under this directory
    property-no-deprecated/  (3 files)
      … 3 files under this directory
    property-no-unknown/  (3 files)
      … 3 files under this directory
    property-no-vendor-prefix/  (3 files)
      … 3 files under this directory
    relative-selector-nesting-notation/  (3 files)
      … 3 files under this directory
    rule-empty-line-before/  (3 files)
      … 3 files under this directory
    rule-nesting-at-rule-required-list/  (3 files)
      … 3 files under this directory
    rule-selector-property-disallowed-list/  (3 files)
      … 3 files under this directory
    selector-anb-no-unmatchable/  (3 files)
      … 3 files under this directory
    selector-attribute-name-disallowed-list/  (3 files)
      … 3 files under this directory
    selector-attribute-operator-allowed-list/  (3 files)
      … 3 files under this directory
    selector-attribute-operator-disallowed-list/  (3 files)
      … 3 files under this directory
    selector-attribute-quotes/  (3 files)
      … 3 files under this directory
    selector-class-pattern/  (3 files)
      … 3 files under this directory
    selector-combinator-allowed-list/  (3 files)
      … 3 files under this directory
    selector-combinator-disallowed-list/  (3 files)
      … 3 files under this directory
    selector-disallowed-list/  (3 files)
      … 3 files under this directory
    selector-id-pattern/  (3 files)
      … 3 files under this directory
    selector-max-attribute/  (3 files)
      … 3 files under this directory
    selector-max-class/  (3 files)
      … 3 files under this directory
    selector-max-combinators/  (3 files)
      … 3 files under this directory
    selector-max-compound-selectors/  (3 files)
      … 3 files under this directory
    selector-max-id/  (3 files)
      … 3 files under this directory
    selector-max-pseudo-class/  (3 files)
      … 3 files under this directory
    selector-max-specificity/  (3 files)
      … 3 files under this directory
    selector-max-type/  (3 files)
      … 3 files under this directory
    selector-max-universal/  (3 files)
      … 3 files under this directory
    selector-nested-pattern/  (3 files)
      … 3 files under this directory
    selector-no-deprecated/  (3 files)
      … 3 files under this directory
    selector-no-invalid/  (3 files)
      … 3 files under this directory
    selector-no-qualifying-type/  (3 files)
      … 3 files under this directory
    selector-no-unmatchable/  (3 files)
      … 3 files under this directory
    selector-no-vendor-prefix/  (3 files)
      … 3 files under this directory
    selector-not-notation/  (3 files)
      … 3 files under this directory
    selector-pseudo-class-allowed-list/  (3 files)
      … 3 files under this directory
    selector-pseudo-class-disallowed-list/  (3 files)
      … 3 files under this directory
    selector-pseudo-class-no-unknown/  (3 files)
      … 3 files under this directory
    selector-pseudo-element-allowed-list/  (3 files)
      … 3 files under this directory
    selector-pseudo-element-colon-notation/  (3 files)
      … 3 files under this directory
    selector-pseudo-element-disallowed-list/  (3 files)
      … 3 files under this directory
    selector-pseudo-element-no-unknown/  (3 files)
      … 3 files under this directory
    selector-type-case/  (3 files)
      … 3 files under this directory
    selector-type-no-unknown/  (3 files)
      … 3 files under this directory
    shorthand-property-no-redundant-values/  (3 files)
      … 3 files under this directory
    string-no-newline/  (3 files)
      … 3 files under this directory
    syntax-string-no-invalid/  (3 files)
      … 3 files under this directory
    time-min-milliseconds/  (3 files)
      … 3 files under this directory
    unit-allowed-list/  (3 files)
      … 3 files under this directory
    unit-disallowed-list/  (3 files)
      … 3 files under this directory
    unit-layout-mappings/  (3 files)
      … 3 files under this directory
    unit-no-unknown/  (3 files)
      … 3 files under this directory
    value-keyword-case/  (3 files)
      … 3 files under this directory
    value-keyword-layout-mappings/  (3 files)
      … 3 files under this directory
    value-no-invalid/  (1 files)
      … 1 files under this directory
    index.mjs
  assignDisabledRanges.mjs
  augmentConfig.mjs
  cli.mjs
  constants.mjs
  createPartialStylelintResult.mjs
  createPlugin.mjs
  createStylelint.mjs
  descriptionlessDisables.mjs
  getConfigForFile.mjs
  getPostcssResult.mjs
  index.mjs
  invalidScopeDisables.mjs
  isPathIgnored.mjs
  lintPostcssResult.mjs
  lintSource.mjs
  needlessDisables.mjs
  normalizeAllRuleSettings.mjs
  normalizeRuleSettings.mjs
  postcssPlugin.mjs
  prepareReturnValue.mjs
  printConfig.mjs
  reportDisables.mjs
  reportUnknownRuleNames.mjs
  resolveConfig.mjs
.codespellrc
.editorconfig
.gitattributes
.gitignore
.prettierignore
.remarkignore
CONTRIBUTING.md
LICENSE
README.md
SUPPORT.md
codecov.yml
eslint.config.mjs
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 43 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 445 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/REPORT_A_BUG.yml` (config)
- `.github/ISSUE_TEMPLATE/REPORT_A_DOCS_ISSUE.yml` (config)
- `.github/ISSUE_TEMPLATE/REQUEST_A_FEATURE.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/close-unknown-effort-prs.yml` (ci)
- `.github/workflows/comment-on-old-issues.yml` (ci)
- `.github/workflows/publish-to-pkg.pr.new.yml` (ci)
- `.github/workflows/release-pr.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/update-pkg.pr.new-comment.yml` (ci)
- `codecov.yml` (config)
- `lib/__tests__/fixtures/config-allow-empty-input.json` (config)
- `lib/__tests__/fixtures/config-at-rule-empty-line-before.json` (config)
- `lib/__tests__/fixtures/config-block-empty-ok.json` (config)
- `lib/__tests__/fixtures/config-block-no-empty-and-color-hex-length-short.json` (config)
- `lib/__tests__/fixtures/config-block-no-empty-report-disables.json` (config)
- `lib/__tests__/fixtures/config-block-no-empty.json` (config)
- `lib/__tests__/fixtures/config-color-named-custom-message.yaml` (config)
- `lib/__tests__/fixtures/config-color-no-invalid-hex.json` (config)
- `lib/__tests__/fixtures/config-extending-and-ignoring.json` (config)
- `lib/__tests__/fixtures/config-extending-another-extend.json` (config)
- `lib/__tests__/fixtures/config-extending-one.json` (config)
- `lib/__tests__/fixtures/config-extending-three-with-override.json` (config)
- `lib/__tests__/fixtures/config-extending-two.json` (config)
- `lib/__tests__/fixtures/config-extending-with-plugin.json` (config)
- `lib/__tests__/fixtures/config-language-options.json` (config)
- `lib/__tests__/fixtures/config-length-zero-no-unit-true.json` (config)
- `lib/__tests__/fixtures/config-no-empty-source.json` (config)
- `lib/__tests__/fixtures/config-no-pixels.json` (config)
- `lib/__tests__/fixtures/config-overrides/at-rule-no-unknown.json` (config)
- `lib/__tests__/fixtures/config-overrides/extending-plugin-and-one-rule.json` (config)
- `lib/__tests__/fixtures/config-overrides/extending-simple-rule.json` (config)
- `lib/__tests__/fixtures/config-overrides/extends-in-overrides.json` (config)
- `lib/__tests__/fixtures/config-overrides/number-max-precision-4.json` (config)
- `lib/__tests__/fixtures/config-overrides/number-max-precision-8.json` (config)
- `lib/__tests__/fixtures/config-overrides/plugin-and-one-rule.json` (config)
- `lib/__tests__/fixtures/config-overrides/scss.json` (config)
- `lib/__tests__/fixtures/config-overrides/simple-rule.json` (config)
- `lib/__tests__/fixtures/config-plugin-extending-with-plugin.json` (config)
- `lib/__tests__/fixtures/config-relative-plugin-nested.json` (config)
- `lib/__tests__/fixtures/config-relative-plugin.json` (config)
- `lib/__tests__/fixtures/config-with-undefined-rule.json` (config)
- `lib/__tests__/fixtures/config-without-rules.json` (config)
- `lib/__tests__/fixtures/default-severity-warning.json` (config)
- `lib/__tests__/fixtures/disableOptions/file-config/.stylelintrc.json` (config)
- `lib/__tests__/fixtures/quiet-deprecation-warnings/config.json` (config)
- `lib/__tests__/fixtures/suppressions/config-block-color-length-invalid-option.json` (config)
- `lib/__tests__/fixtures/suppressions/config-block-color-length.json` (config)
- `lib/__tests__/fixtures/suppressions/config-block-no-empty_and_color-invalid.json` (config)
- `lib/__tests__/fixtures/suppressions/config-length-zero-no-unit.json` (config)
- `lib/__tests__/fixtures/suppressions/existing-suppressions.json` (config)
- `lib/__tests__/stylelintignore-test/fixtures/config-block-no-empty.json` (config)
- `lib/__tests__/stylelintignore-test/fixtures/config-color-no-invalid-hex.json` (config)

## Top-level layout

- `lib` — 721 analysed file(s)
- `docs` — 29 analysed file(s)
- `.changeset` — 15 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 12 analysed file(s)
- `identity` — 6 analysed file(s)
- `.githooks` — 1 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (1 x likely secret file excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ee4f118acae33876a93ced5866872328e36660c2` is the revision these paths and observations refer to.
