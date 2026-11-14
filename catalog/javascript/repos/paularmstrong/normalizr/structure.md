# Project structure: paularmstrong/normalizr

**Analysed commit:** `c2ab080641c7ebc6f5dc085a4ac074947f48ca58`

**Commit reference:** [c2ab080641c7ebc6f5dc085a4ac074947f48ca58](https://github.com/paularmstrong/normalizr/commit/c2ab080641c7ebc6f5dc085a4ac074947f48ca58)

**Tree at this commit:** [paularmstrong/normalizr@c2ab080641c7](https://github.com/paularmstrong/normalizr/tree/c2ab080641c7ebc6f5dc085a4ac074947f48ca58)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | paularmstrong/normalizr |
| Description | Normalizes nested JSON according to a schema |
| Stars | 20778 |
| Forks | 851 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c2ab080641c7ebc6f5dc085a4ac074947f48ca58` |
| Retrieved at | 2026-11-14T19:11:12.318178+00:00 |
| Files in this snapshot | 86 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.md
    feature_request.md
    support_question.md
  workflows/  (1 files)
    close-pull-request.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  lock.yml
docs/  (6 files)
  README.md
  api.md
  faqs.md
  introduction.md
  jsonapi.md
  quickstart.md
examples/  (28 files)
  github/  (4 files)
    README.md
    index.js
    output.json
    schema.js
  redux/  (18 files)
    src/  (13 files)
      … 13 files under this directory
    .babelrc
    .gitignore
    README.md
    index.js
    package.json
  relationships/  (5 files)
    README.md
    index.js
    input.json
    output.json
    schema.js
  .eslintrc
src/  (20 files)
  __tests__/  (2 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    index.test.js
  schemas/  (17 files)
    __tests__/  (10 files)
      … 10 files under this directory
    Array.js
    Entity.js
    ImmutableUtils.js
    Object.js
    Polymorphic.js
    Union.js
    Values.js
  index.js
typescript-tests/  (8 files)
  array.ts
  array_schema.ts
  entity.ts
  github.ts
  object.ts
  relationships.ts
  union.ts
  values.ts
.babelrc.js
.eslintignore
.eslintrc.js
.flowconfig
.gitignore
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
husky.config.js
index.d.ts
jest.config.js
lint-staged.config.js
package.json
prettier.config.js
rollup.config.js
```

## Entry points

- [examples/redux/index.js](https://github.com/paularmstrong/normalizr/blob/c2ab080641c7ebc6f5dc085a4ac074947f48ca58/examples/redux/index.js)
- [src/index.js](https://github.com/paularmstrong/normalizr/blob/c2ab080641c7ebc6f5dc085a4ac074947f48ca58/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| schemas package | library | Observed | Groups 12 file(s) under schemas package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 1 file(s) under __tests__ package (observed from repository paths and static analysis). |
| typescript-tests package | library | Observed | Groups 8 file(s) under typescript-tests package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/lock.yml` (config)
- `.github/workflows/close-pull-request.yml` (ci)
- `.travis.yml` (ci)
- `examples/github/output.json` (config)
- `examples/redux/package.json` (manifest)
- `examples/relationships/input.json` (config)
- `examples/relationships/output.json` (config)
- `package.json` (manifest)

## Top-level layout

- `examples` — 28 analysed file(s)
- `src` — 20 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `typescript-tests` — 8 analysed file(s)
- `.github` — 7 analysed file(s)
- `docs` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `c2ab080641c7ebc6f5dc085a4ac074947f48ca58` is the revision these paths and observations refer to.
