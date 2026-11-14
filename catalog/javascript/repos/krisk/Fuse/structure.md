# Project structure: krisk/Fuse

**Analysed commit:** `edf2fb608eca0461508d1d71317e6e58309ffada`

**Commit reference:** [edf2fb608eca0461508d1d71317e6e58309ffada](https://github.com/krisk/Fuse/commit/edf2fb608eca0461508d1d71317e6e58309ffada)

**Tree at this commit:** [krisk/Fuse@edf2fb608eca](https://github.com/krisk/Fuse/tree/edf2fb608eca0461508d1d71317e6e58309ffada)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | krisk/Fuse |
| Description | Lightweight fuzzy-search, in JavaScript |
| Stars | 20530 |
| Forks | 828 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `edf2fb608eca0461508d1d71317e6e58309ffada` |
| Retrieved at | 2026-11-14T19:11:13.399863+00:00 |
| Files in this snapshot | 154 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yml
    config.yml
    docs_bug.yml
    feature_request.yml
    support_request.yml
  workflows/  (2 files)
    deploy-docs.yml
    nodejs.yml
  FUNDING.yml
.husky/  (2 files)
  commit-msg
  pre-commit
bench/  (9 files)
  parallel-browser/  (2 files)
    index.html
    worker.js
  direction-a-parity-check.mjs
  extended.mjs
  index-creation.mjs
  inverted-index-shape.mjs
  parallel-workers.mjs
  search.mjs
  token-search.mjs
docs/  (46 files)
  .vitepress/  (20 files)
    theme/  (18 files)
      … 18 files under this directory
    config.ts
    env.d.ts
  articles/  (3 files)
    how-fuzzy-search-works.md
    using-fuse-with-react.md
    vs-semantic-search.md
  public/  (12 files)
    assets/  (6 files)
      … 6 files under this directory
    icons/  (1 files)
      … 1 files under this directory
    donate.html
    manifest.webmanifest
    robots.txt
    service-worker.js
    team-plans.html
  cloud.md
  demo.md
  extended-search.md
  fuzzy-search.md
  getting-started.md
  index.md
  logical-search.md
  performance.md
  sponsor.md
  token-search.md
  web-workers.md
scripts/  (3 files)
  bump-docs.cjs
  deploy-docs.sh
  release.sh
src/  (37 files)
  core/  (8 files)
    computeScore.ts
    config.ts
    errorMessages.ts
    format.ts
    formatMatches.ts
    index.ts
    queryParser.ts
    register.ts
  helpers/  (4 files)
    diacritics.ts
    get.ts
    mergeIndices.ts
    typeGuards.ts
  search/  (14 files)
    bitap/  (6 files)
      … 6 files under this directory
    extended/  (4 files)
      … 4 files under this directory
    token/  (3 files)
      … 3 files under this directory
    index.ts
  tools/  (4 files)
    FuseIndex.ts
    KeyStore.ts
    MaxHeap.ts
    fieldNorm.ts
  workers/  (3 files)
    FuseWorker.ts
    index.ts
    worker.ts
  entry.ts
  env.d.ts
  tsconfig.json
  types.ts
test/  (33 files)
  __snapshots__/  (3 files)
    extended-search.test.js.snap
    fuzzy-search.test.js.snap
    logical-search.test.js.snap
  fixtures/  (5 files)
    books.json
    pokedex.js
    pokedex.ts
    types.js
    types.ts
  cache-invalidation.test.js
  cjs-interop.test.js
  extended-search.test.js
  feature-flags.test.js
  fuse-worker.test.js
  fuzzy-search.test.js
  indexing.test.js
  internals.test.ts
  key-weight-normalization.test.js
  logical-search.test.js
  match.test.js
  object-query.test.js
  optimizations.test.js
  package-types.test.ts
  scoring.test.js
  token-search-and.test.js
  token-search-scenarios.test.js
  token-search-tokenizer.test.js
  token-search.test.js
  tsconfig.json
  typings.test.ts
  worker-entry-helper.mjs
  worker-thread-helper.mjs
  worker-url.test.js
  … 1 more files
.gitignore
.nvmrc
.prettierignore
.prettierrc.cjs
CHANGELOG.md
CONTRIBUTING.md
DEVELOPERS.md
LICENSE
README.md
SPONSOR.md
backers.md
eslint.config.mjs
package.json
tsconfig.base.json
tsdown.config.ts
vitest.config.ts
```

## Entry points

- [src/core/index.ts](https://github.com/krisk/Fuse/blob/edf2fb608eca0461508d1d71317e6e58309ffada/src/core/index.ts)
- [src/search/bitap/index.ts](https://github.com/krisk/Fuse/blob/edf2fb608eca0461508d1d71317e6e58309ffada/src/search/bitap/index.ts)
- [src/search/extended/index.ts](https://github.com/krisk/Fuse/blob/edf2fb608eca0461508d1d71317e6e58309ffada/src/search/extended/index.ts)
- [src/search/index.ts](https://github.com/krisk/Fuse/blob/edf2fb608eca0461508d1d71317e6e58309ffada/src/search/index.ts)
- [src/search/token/index.ts](https://github.com/krisk/Fuse/blob/edf2fb608eca0461508d1d71317e6e58309ffada/src/search/token/index.ts)
- [src/workers/index.ts](https://github.com/krisk/Fuse/blob/edf2fb608eca0461508d1d71317e6e58309ffada/src/workers/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bench package | library | Observed | Groups 8 file(s) under bench package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| entry.ts package | library | Observed | Groups 1 file(s) under entry.ts package (observed from repository paths and static analysis). |
| env.d.ts package | library | Observed | Groups 1 file(s) under env.d.ts package (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 4 file(s) under helpers package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| search package | library | Observed | Groups 14 file(s) under search package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 8 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 33 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 4 file(s) under tools package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| workers package | library | Observed | Groups 3 file(s) under workers package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/docs_bug.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/support_request.yml` (config)
- `.github/workflows/deploy-docs.yml` (ci)
- `.github/workflows/nodejs.yml` (ci)
- `package.json` (manifest)
- `src/tsconfig.json` (config)
- `tsconfig.base.json` (config)

## Top-level layout

- `docs` — 46 analysed file(s)
- `src` — 37 analysed file(s)
- `test` — 33 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `bench` — 9 analysed file(s)
- `.github` — 8 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 18 file(s) were skipped during inventory (1 x likely secret file excluded; 17 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `edf2fb608eca0461508d1d71317e6e58309ffada` is the revision these paths and observations refer to.
