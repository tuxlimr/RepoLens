# Project structure: expressjs/multer

**Analysed commit:** `2c380d06cdaacc68bbef8b36244493a3d33d6b88`

**Commit reference:** [2c380d06cdaacc68bbef8b36244493a3d33d6b88](https://github.com/expressjs/multer/commit/2c380d06cdaacc68bbef8b36244493a3d33d6b88)

**Tree at this commit:** [expressjs/multer@2c380d06cdaa](https://github.com/expressjs/multer/tree/2c380d06cdaacc68bbef8b36244493a3d33d6b88)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | expressjs/multer |
| Description | Node.js middleware for handling `multipart/form-data`. |
| Stars | 12086 |
| Forks | 1149 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `2c380d06cdaacc68bbef8b36244493a3d33d6b88` |
| Retrieved at | 2026-11-14T19:12:10.890905+00:00 |
| Files in this snapshot | 69 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (4 files)
    ci.yml
    codeql.yml
    npm-publish.yml
    scorecard.yml
  dependabot.yml
examples/  (10 files)
  FormDataBlob/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    index.js
    package.json
  FormDataImage/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    index.js
    package.json
lib/  (6 files)
  counter.js
  file-appender.js
  make-middleware.js
  multer-error.js
  remove-uploaded-files.js
  validate-limits.js
storage/  (2 files)
  disk.js
  memory.js
test/  (38 files)
  _util.js
  abort-destroyed-stream-callback.js
  abort-fd-leak.js
  abort-flush-fd-race.js
  abort-storage-error-cleanup.js
  abort-unlink-after-close.js
  array-index-limit.js
  async-file-filter-file-size.js
  async-file-filter-orphan.js
  async-file-filter-teardown-crash.js
  busboy-options.js
  crafted-field-names.js
  def-param-charset.js
  disk-storage.js
  error-handling.js
  expected-files.js
  express-integration.js
  fieldname-decoding.js
  fields.js
  file-filter.js
  file-ordering.js
  filename-decoding.js
  functionality.js
  issue-232.js
  … 14 more files
.gitattributes
.gitignore
CHANGELOG.md
LICENSE
README.md
StorageEngine.md
index.js
package.json
```

## Entry points

- [examples/FormDataBlob/index.js](https://github.com/expressjs/multer/blob/2c380d06cdaacc68bbef8b36244493a3d33d6b88/examples/FormDataBlob/index.js)
- [examples/FormDataImage/index.js](https://github.com/expressjs/multer/blob/2c380d06cdaacc68bbef8b36244493a3d33d6b88/examples/FormDataImage/index.js)
- [index.js](https://github.com/expressjs/multer/blob/2c380d06cdaacc68bbef8b36244493a3d33d6b88/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 6 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 38 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/npm-publish.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `examples/FormDataBlob/package.json` (manifest)
- `examples/FormDataImage/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `test` — 38 analysed file(s)
- `examples` — 10 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `lib` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `storage` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2c380d06cdaacc68bbef8b36244493a3d33d6b88` is the revision these paths and observations refer to.
