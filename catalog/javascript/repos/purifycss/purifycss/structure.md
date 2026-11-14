# Project structure: purifycss/purifycss

**Analysed commit:** `be52c1c6b1b6e287b6989428c57f05a79aa135dc`

**Commit reference:** [be52c1c6b1b6e287b6989428c57f05a79aa135dc](https://github.com/purifycss/purifycss/commit/be52c1c6b1b6e287b6989428c57f05a79aa135dc)

**Tree at this commit:** [purifycss/purifycss@be52c1c6b1b6](https://github.com/purifycss/purifycss/tree/be52c1c6b1b6e287b6989428c57f05a79aa135dc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | purifycss/purifycss |
| Description | Remove unused CSS. Also works with single-page apps. |
| Stars | 9832 |
| Forks | 375 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `be52c1c6b1b6e287b6989428c57f05a79aa135dc` |
| Retrieved at | 2026-11-14T19:12:49.676362+00:00 |
| Files in this snapshot | 43 |

## Directory tree

```text
__tests__/  (26 files)
  test_examples/  (25 files)
    attribute_selector/  (2 files)
      … 2 files under this directory
    bootstrap/  (1 files)
      … 1 files under this directory
    camel_case/  (2 files)
      … 2 files under this directory
    combined/  (2 files)
      … 2 files under this directory
    delimited/  (2 files)
      … 2 files under this directory
    media_queries/  (2 files)
      … 2 files under this directory
    multiple_files/  (4 files)
      … 4 files under this directory
    pseudo_class/  (2 files)
      … 2 files under this directory
    remove_unused/  (2 files)
      … 2 files under this directory
    simple/  (2 files)
      … 2 files under this directory
    special_characters/  (2 files)
      … 2 files under this directory
    wildcard/  (2 files)
      … 2 files under this directory
  index.js
bin/  (1 files)
  purifycss
config/  (1 files)
  rollup.config.js
lib/  (2 files)
  purifycss.es.js
  purifycss.js
src/  (6 files)
  utils/  (3 files)
    ExtractWordsUtil.js
    FileUtil.js
    PrintUtil.js
  CssTreeWalker.js
  SelectorFilter.js
  purifycss.js
.eslintrc
.gitignore
.travis.yml
LICENSE
README.md
package.json
purified.css
```

## Entry points

- [lib/purifycss.js](https://github.com/purifycss/purifycss/blob/be52c1c6b1b6e287b6989428c57f05a79aa135dc/lib/purifycss.js)
- [bin/purifycss](https://github.com/purifycss/purifycss/blob/be52c1c6b1b6e287b6989428c57f05a79aa135dc/bin/purifycss)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| CssTreeWalker.js package | library | Observed | Groups 1 file(s) under csstreewalker.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 2 file(s) under lib package (observed from repository paths and static analysis). |
| purifycss.js package | library | Observed | Groups 1 file(s) under purifycss.js package (observed from repository paths and static analysis). |
| SelectorFilter.js package | library | Observed | Groups 1 file(s) under selectorfilter.js package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 8 file(s) under __tests__ package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `__tests__` — 26 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `src` — 6 analysed file(s)
- `lib` — 2 analysed file(s)
- `bin` — 1 analysed file(s)
- `config` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `be52c1c6b1b6e287b6989428c57f05a79aa135dc` is the revision these paths and observations refer to.
