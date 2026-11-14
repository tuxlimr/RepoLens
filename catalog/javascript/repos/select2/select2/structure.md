# Project structure: select2/select2

**Analysed commit:** `79811ace45f09e199fc6b92f5f1ea8334746df8f`

**Commit reference:** [79811ace45f09e199fc6b92f5f1ea8334746df8f](https://github.com/select2/select2/commit/79811ace45f09e199fc6b92f5f1ea8334746df8f)

**Tree at this commit:** [select2/select2@79811ace45f0](https://github.com/select2/select2/tree/79811ace45f09e199fc6b92f5f1ea8334746df8f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | select2/select2 |
| Description | Select2 is a jQuery based replacement for select boxes. It supports searching, remote data sets, and infinite scrolling of results. |
| Stars | 25907 |
| Forks | 6116 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `79811ace45f09e199fc6b92f5f1ea8334746df8f` |
| Retrieved at | 2026-11-14T19:10:56.443092+00:00 |
| Files in this snapshot | 235 |

## Directory tree

```text
.github/  (9 files)
  workflows/  (3 files)
    docs-deploy.yml
    main.yml
    package-deploy.yml
  CONTRIBUTING.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  stale.yml
docs/  (35 files)
  advanced/  (7 files)
    default-adapters/  (6 files)
      … 6 files under this directory
    adapters-and-decorators.md
  configuration/  (3 files)
    data-attributes.md
    defaults.md
    options-api.md
  data-sources/  (3 files)
    ajax.md
    arrays.md
    formats.md
  getting-started/  (3 files)
    basic-usage.md
    builds-and-modules.md
    installation.md
  overrides/  (2 files)
    custom.css
    main.html
  programmatic-control/  (4 files)
    add-select-clear-items.md
    events.md
    methods.md
    retrieving-selections.md
  troubleshooting/  (2 files)
    common-problems.md
    getting-help.md
  upgrading/  (2 files)
    migrating-from-35.md
    new-in-40.md
  README.md
  appearance.md
  dropdown.md
  i18n.md
  options.md
  placeholders.md
  searching.md
  selections.md
  tagging.md
src/  (123 files)
  js/  (111 files)
    select2/  (104 files)
      … 104 files under this directory
    banner.end.js
    banner.start.js
    jquery.mousewheel.shim.js
    jquery.select2.js
    jquery.shim.js
    wrapper.end.js
    wrapper.start.js
  scss/  (12 files)
    mixins/  (1 files)
      … 1 files under this directory
    theme/  (7 files)
      … 7 files under this directory
    _dropdown.scss
    _multiple.scss
    _single.scss
    core.scss
tests/  (51 files)
  a11y/  (1 files)
    selection-tests.js
  data/  (8 files)
    array-tests.js
    base-tests.js
    maximumInputLength-tests.js
    maximumSelectionLength-tests.js
    minimumInputLength-tests.js
    select-tests.js
    tags-tests.js
    tokenizer-tests.js
  dropdown/  (7 files)
    dropdownCss-tests.js
    dropdownParent-tests.js
    positioning-tests.js
    search-a11y-tests.js
    search-tests.js
    selectOnClose-tests.js
    stopPropagation-tests.js
  integration/  (3 files)
    dom-changes.js
    jquery-calls.js
    select2-methods.js
  options/  (5 files)
    ajax-tests.js
    data-tests.js
    element-tests.js
    translation-tests.js
    width-tests.js
  results/  (4 files)
    a11y-tests.js
    focusing-tests.js
    infiniteScroll-tests.js
    option-tests.js
  selection/  (11 files)
    allowClear-tests.js
    focusing-tests.js
    multiple-tests.js
    openOnKeyDown-tests.js
    placeholder-tests.js
    search-a11y-tests.js
    search-placeholder-tests.js
    search-tests.js
    selectionCss-tests.js
    single-tests.js
    stopPropagation-tests.js
  utils/  (3 files)
    data-tests.js
    decorator-tests.js
    escapeMarkup-tests.js
  helpers.js
  integration-jq1.html
  integration-jq2.html
  integration-jq3.html
  integration-jq4.html
  unit-jq1.html
  unit-jq2.html
  unit-jq3.html
  unit-jq4.html
.biome.json
.editorconfig
.gitignore
.jshintignore
.jshintrc
.nvmrc
.pre-commit-config.yaml
CHANGELOG.md
Gruntfile.js
LICENSE.md
README.md
bower.json
component.json
composer.json
mkdocs.yml
package.json
pyproject.toml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 9 file(s) under data layer (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 102 file(s) under js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 51 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.biome.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/docs-deploy.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/package-deploy.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `bower.json` (config)
- `component.json` (config)
- `composer.json` (config)
- `mkdocs.yml` (config)
- `package.json` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `src` — 123 analysed file(s)
- `tests` — 51 analysed file(s)
- `docs` — 35 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 73 file(s) were skipped during inventory (2 x lockfile excluded; 71 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `79811ace45f09e199fc6b92f5f1ea8334746df8f` is the revision these paths and observations refer to.
