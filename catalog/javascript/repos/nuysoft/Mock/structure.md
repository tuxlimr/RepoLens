# Project structure: nuysoft/Mock

**Analysed commit:** `00ce04b92eb464e664a4438430903f2de96efb47`

**Commit reference:** [00ce04b92eb464e664a4438430903f2de96efb47](https://github.com/nuysoft/Mock/commit/00ce04b92eb464e664a4438430903f2de96efb47)

**Tree at this commit:** [nuysoft/Mock@00ce04b92eb4](https://github.com/nuysoft/Mock/tree/00ce04b92eb464e664a4438430903f2de96efb47)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nuysoft/Mock |
| Description | A simulation data generator |
| Stars | 19546 |
| Forks | 2625 |
| Licence | Other |
| Language | JavaScript |
| Default branch | refactoring |
| Analysed commit | `00ce04b92eb464e664a4438430903f2de96efb47` |
| Retrieved at | 2026-11-14T19:11:17.477367+00:00 |
| Files in this snapshot | 56 |

## Directory tree

```text
bin/  (1 files)
  random
src/  (29 files)
  mock/  (28 files)
    random/  (14 files)
      … 14 files under this directory
    regexp/  (3 files)
      … 3 files under this directory
    schema/  (2 files)
      … 2 files under this directory
    valid/  (2 files)
      … 2 files under this directory
    xhr/  (2 files)
      … 2 files under this directory
    RE_KEY.svg
    constant.js
    handler.js
    parser.js
    util.js
  mock.js
test/  (14 files)
  materiels/  (2 files)
    noop.html
    noop.js
  bower.json
  package.json
  test.coveralls.js
  test.mock.html
  test.mock.mock.js
  test.mock.random.js
  test.mock.request.js
  test.mock.schema.js
  test.mock.spec.dpd.js
  test.mock.spec.dtd.js
  test.mock.valid.js
  valid.js
.editorconfig
.gitattributes
.gitignore
.jshintrc
.spmignore
.travis.yml
CHANGELOG.md
LICENSE
README.md
bower.json
gulpfile.js
package.json
```

## Entry points

- [bin/random](https://github.com/nuysoft/Mock/blob/00ce04b92eb464e664a4438430903f2de96efb47/bin/random)
- [src/mock/random/index.js](https://github.com/nuysoft/Mock/blob/00ce04b92eb464e664a4438430903f2de96efb47/src/mock/random/index.js)
- [src/mock/regexp/index.js](https://github.com/nuysoft/Mock/blob/00ce04b92eb464e664a4438430903f2de96efb47/src/mock/regexp/index.js)
- [src/mock/schema/index.js](https://github.com/nuysoft/Mock/blob/00ce04b92eb464e664a4438430903f2de96efb47/src/mock/schema/index.js)
- [src/mock/valid/index.js](https://github.com/nuysoft/Mock/blob/00ce04b92eb464e664a4438430903f2de96efb47/src/mock/valid/index.js)
- [src/mock/xhr/index.js](https://github.com/nuysoft/Mock/blob/00ce04b92eb464e664a4438430903f2de96efb47/src/mock/xhr/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| mock package | library | Observed | Groups 27 file(s) under mock package (observed from repository paths and static analysis). |
| mock.js package | library | Observed | Groups 1 file(s) under mock.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 29 analysed file(s)
- `test` — 14 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `00ce04b92eb464e664a4438430903f2de96efb47` is the revision these paths and observations refer to.
