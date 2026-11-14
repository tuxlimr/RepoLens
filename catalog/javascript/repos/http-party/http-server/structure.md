# Project structure: http-party/http-server

**Analysed commit:** `0d3b7bb5b6e8a59fd450ae2dca65870009cfcd8b`

**Commit reference:** [0d3b7bb5b6e8a59fd450ae2dca65870009cfcd8b](https://github.com/http-party/http-server/commit/0d3b7bb5b6e8a59fd450ae2dca65870009cfcd8b)

**Tree at this commit:** [http-party/http-server@0d3b7bb5b6e8](https://github.com/http-party/http-server/tree/0d3b7bb5b6e8a59fd450ae2dca65870009cfcd8b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | http-party/http-server |
| Description | A simple, zero-configuration, command-line http server |
| Stars | 14239 |
| Forks | 1558 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `0d3b7bb5b6e8a59fd450ae2dca65870009cfcd8b` |
| Retrieved at | 2026-11-14T19:11:46.126385+00:00 |
| Files in this snapshot | 121 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    feature-request.md
  workflows/  (3 files)
    node.js.yml
    release-drafter.yml
    stale.yml
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  release-drafter.yml
bin/  (1 files)
  http-server
doc/  (1 files)
  http-server.1
lib/  (14 files)
  core/  (12 files)
    show-dir/  (7 files)
      … 7 files under this directory
    aliases.json
    etag.js
    index.js
    opts.js
    status-handlers.js
  shims/  (1 files)
    https-server-shim.js
  http-server.js
public/  (2 files)
  404.html
  index.html
test/  (85 files)
  fixtures/  (10 files)
    proxy-all-local/  (2 files)
      … 2 files under this directory
    root/  (5 files)
      … 5 files under this directory
    common-cases-error.js
    common-cases.js
    custom_mime_type.types
  public/  (32 files)
    another-subdir/  (1 files)
      … 1 files under this directory
    brotli/  (6 files)
      … 6 files under this directory
    charset/  (2 files)
      … 2 files under this directory
    compress/  (2 files)
      … 2 files under this directory
    curimit@gmail.com (40%)/  (1 files)
      … 1 files under this directory
    dir-overrides-404/  (2 files)
      … 2 files under this directory
    gzip/  (3 files)
      … 3 files under this directory
    show-dir$$href_encoding$$/  (1 files)
      … 1 files under this directory
    subdir/  (2 files)
      … 2 files under this directory
    subdir_with space/  (2 files)
      … 2 files under this directory
    中文/  (1 files)
      … 1 files under this directory
    404.html
    a.txt
    b.txt
    c.js
    custom_mime_type.opml
    custom_mime_type.types
    d.js
    e.js
    f_f
  304.test.js
  accept-encoding.test.js
  allowed-hosts.test.js
  cache.test.js
  check-headers.js
  cli.test.js
  compression.test.js
  content-type.test.js
  coop.test.js
  core-error.test.js
  core.test.js
  cors.test.js
  custom-content-type-file-secret.test.js
  custom-content-type-file.test.js
  custom-content-type.test.js
  default-default-ext.test.js
  dir-overrides-404.test.js
  enotdir.test.js
  escaping.test.js
  express-error.test.js
  express.test.js
  force-content-encoding.test.js
  headers.test.js
  illegal-access-date.test.js
  … 19 more files
.dockerignore
.eslintrc.json
.gitignore
CODE_OF_CONDUCT.md
Dockerfile
LICENSE
README.md
SECURITY.md
package.json
```

## Entry points

- [bin/http-server](https://github.com/http-party/http-server/blob/0d3b7bb5b6e8a59fd450ae2dca65870009cfcd8b/bin/http-server)
- [lib/core/index.js](https://github.com/http-party/http-server/blob/0d3b7bb5b6e8a59fd450ae2dca65870009cfcd8b/lib/core/index.js)
- [lib/core/show-dir/index.js](https://github.com/http-party/http-server/blob/0d3b7bb5b6e8a59fd450ae2dca65870009cfcd8b/lib/core/show-dir/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 2 file(s) under lib package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 10 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 85 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/release-drafter.yml` (config)
- `.github/workflows/node.js.yml` (ci)
- `.github/workflows/release-drafter.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `Dockerfile` (container)
- `lib/core/aliases.json` (config)
- `lib/core/show-dir/icons.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 85 analysed file(s)
- `lib` — 14 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 9 analysed file(s)
- `public` — 2 analysed file(s)
- `bin` — 1 analysed file(s)
- `doc` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0d3b7bb5b6e8a59fd450ae2dca65870009cfcd8b` is the revision these paths and observations refer to.
