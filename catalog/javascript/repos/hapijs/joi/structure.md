# Project structure: hapijs/joi

**Analysed commit:** `7cfb3ce20017a4289f7efdcd8803625d4be889df`

**Commit reference:** [7cfb3ce20017a4289f7efdcd8803625d4be889df](https://github.com/hapijs/joi/commit/7cfb3ce20017a4289f7efdcd8803625d4be889df)

**Tree at this commit:** [hapijs/joi@7cfb3ce20017](https://github.com/hapijs/joi/tree/7cfb3ce20017a4289f7efdcd8803625d4be889df)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hapijs/joi |
| Description | The most powerful data validation library for JS |
| Stars | 21168 |
| Forks | 1529 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `7cfb3ce20017a4289f7efdcd8803625d4be889df` |
| Retrieved at | 2026-11-14T19:11:11.215442+00:00 |
| Files in this snapshot | 80 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci-module.yml
benchmarks/  (5 files)
  .gitignore
  README.md
  bench.js
  package.json
  suite.js
browser/  (7 files)
  lib/  (1 files)
    version-loader.js
  tests/  (1 files)
    index.js
  .gitignore
  karma.conf.js
  package.json
  webpack.config.js
  webpack.mocha.js
lib/  (32 files)
  types/  (13 files)
    alternatives.js
    any.js
    array.js
    binary.js
    boolean.js
    date.js
    function.js
    keys.js
    link.js
    number.js
    object.js
    string.js
    symbol.js
  annotate.js
  base.js
  cache.js
  common.js
  compile.js
  errors.js
  extend.js
  index.d.ts
  index.js
  manifest.js
  messages.js
  modify.js
  ref.js
  schemas.js
  state.js
  template.js
  trace.js
  validator.js
  values.js
test/  (29 files)
  types/  (11 files)
    alternatives.js
    any.js
    array.js
    binary.js
    boolean.js
    date.js
    function.js
    link.js
    number.js
    object.js
    symbol.js
  base.js
  cache.js
  common.js
  compile.js
  errors.js
  extend.js
  helper.js
  index.js
  index.ts
  isAsync.js
  json-schema.js
  manifest.js
  modify.js
  ref.js
  template.js
  trace.js
  validator.js
  values.js
.gitignore
API.md
LICENSE.md
README.md
eslint.config.js
package.json
```

## Entry points

- [lib/index.js](https://github.com/hapijs/joi/blob/7cfb3ce20017a4289f7efdcd8803625d4be889df/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 2 file(s) under benchmarks package (observed from repository paths and static analysis). |
| browser package | library | Observed | Groups 4 file(s) under browser package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 32 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 30 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci-module.yml` (ci)
- `benchmarks/package.json` (manifest)
- `browser/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `lib` — 32 analysed file(s)
- `test` — 29 analysed file(s)
- `browser` — 7 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `benchmarks` — 5 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7cfb3ce20017a4289f7efdcd8803625d4be889df` is the revision these paths and observations refer to.
