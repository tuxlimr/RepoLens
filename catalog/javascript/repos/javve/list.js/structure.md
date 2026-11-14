# Project structure: javve/list.js

**Analysed commit:** `44ae2396072a617f6a418b5d10c5adbcbc34842f`

**Commit reference:** [44ae2396072a617f6a418b5d10c5adbcbc34842f](https://github.com/javve/list.js/commit/44ae2396072a617f6a418b5d10c5adbcbc34842f)

**Tree at this commit:** [javve/list.js@44ae2396072a](https://github.com/javve/list.js/tree/44ae2396072a617f6a418b5d10c5adbcbc34842f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | javve/list.js |
| Description | The perfect library for adding search, sort, filters and flexibility to tables, lists and various HTML elements. Built to be invisible and work on existing HTML. |
| Stars | 11201 |
| Forks | 875 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `44ae2396072a617f6a418b5d10c5adbcbc34842f` |
| Retrieved at | 2026-11-14T19:12:24.395242+00:00 |
| Files in this snapshot | 112 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
__test__/  (28 files)
  usage/  (6 files)
    amd.html
    classic.html
    fuzzy-search-pagination.html
    main.js
    require.js
    style.css
  add-get-remove.test.js
  buttons.test.js
  create.test.js
  defaults.test.js
  filter.test.js
  fixtures-fuzzysearch.js
  fixtures-pagination.js
  fixtures.js
  fuzzysearch.test.js
  item.test.js
  off.test.js
  on.test.js
  pagination.test.js
  parse.test.js
  re-index.test.js
  search-filter.test.js
  search.test.js
  show.test.js
  sort.test.js
  trigger.test.js
  utils.classes.test.js
  utils.get-by-class.test.js
docs/  (48 files)
  .bundle/  (1 files)
    config
  _data/  (1 files)
    pkg.json
  _examples/  (8 files)
    add-get-remove.html
    data-attributes-custom-attributes.html
    existing-list-add.html
    existing-list.html
    fuzzy-search.html
    new-list.html
    pagination.html
    table.html
  _includes/  (5 files)
    examples/  (1 files)
      … 1 files under this directory
    author.html
    carbon.html
    codepen.html
    menu.html
  _layouts/  (1 files)
    default.html
  _sass/  (6 files)
    _base.scss
    _carbonads.scss
    _docs.scss
    _menu.scss
    _mixins.scss
    _normalize.scss
  assets/  (2 files)
    css/  (1 files)
      … 1 files under this directory
    javascripts/  (1 files)
      … 1 files under this directory
  docs/  (9 files)
    plugins/  (4 files)
      … 4 files under this directory
    fuzzysearch.html
    index.html
    item-api.html
    pagination.html
    search-sort.html
  overview/  (5 files)
    changelog.html
    contribute.html
    download.html
    index.html
    press.html
  .ruby-version
  CNAME
  Gemfile
  Gemfile.lock
  README.md
  _config.yml
  api.html
  faq.html
  feed.xml
  index.html
src/  (19 files)
  utils/  (9 files)
    classes.js
    events.js
    extend.js
    fuzzy.js
    get-attribute.js
    get-by-class.js
    index-of.js
    to-array.js
    to-string.js
  add-async.js
  filter.js
  fuzzy-search.js
  index.js
  item.js
  pagination.js
  parse.js
  search.js
  sort.js
  templater.js
.browserslistrc
.codecov.yml
.gitignore
.npmignore
.nvmrc
.prettierignore
CHANGELOG.md
LICENSE
README.md
Release.md
WISHLIST.md
bower.json
package.json
prettier.config.js
webpack.config.js
```

## Entry points

- [__test__/usage/main.js](https://github.com/javve/list.js/blob/44ae2396072a617f6a418b5d10c5adbcbc34842f/__test__/usage/main.js)
- [src/index.js](https://github.com/javve/list.js/blob/44ae2396072a617f6a418b5d10c5adbcbc34842f/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| add-async.js package | library | Observed | Groups 1 file(s) under add-async.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| filter.js package | library | Observed | Groups 1 file(s) under filter.js package (observed from repository paths and static analysis). |
| fuzzy-search.js package | library | Observed | Groups 1 file(s) under fuzzy-search.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| item.js package | library | Observed | Groups 1 file(s) under item.js package (observed from repository paths and static analysis). |
| pagination.js package | library | Observed | Groups 1 file(s) under pagination.js package (observed from repository paths and static analysis). |
| parse.js package | library | Observed | Groups 1 file(s) under parse.js package (observed from repository paths and static analysis). |
| search.js package | library | Observed | Groups 1 file(s) under search.js package (observed from repository paths and static analysis). |
| sort.js package | library | Observed | Groups 1 file(s) under sort.js package (observed from repository paths and static analysis). |
| templater.js package | library | Observed | Groups 1 file(s) under templater.js package (observed from repository paths and static analysis). |
| __test__ package | library | Observed | Groups 24 file(s) under __test__ package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 9 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.codecov.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `bower.json` (config)
- `docs/_config.yml` (config)
- `docs/_data/pkg.json` (config)
- `package.json` (manifest)

## Top-level layout

- `docs` — 48 analysed file(s)
- `__test__` — 28 analysed file(s)
- `src` — 19 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (6 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `44ae2396072a617f6a418b5d10c5adbcbc34842f` is the revision these paths and observations refer to.
