# Project structure: request/request

**Analysed commit:** `3c0cddc7c8eb60b470e9519da85896ed7ee0081e`

**Commit reference:** [3c0cddc7c8eb60b470e9519da85896ed7ee0081e](https://github.com/request/request/commit/3c0cddc7c8eb60b470e9519da85896ed7ee0081e)

**Tree at this commit:** [request/request@3c0cddc7c8eb](https://github.com/request/request/tree/3c0cddc7c8eb60b470e9519da85896ed7ee0081e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | request/request |
| Description | 🏊🏾 Simplified HTTP request client. |
| Stars | 25477 |
| Forks | 3132 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `3c0cddc7c8eb60b470e9519da85896ed7ee0081e` |
| Retrieved at | 2026-11-14T19:11:00.413628+00:00 |
| Files in this snapshot | 113 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  stale.yml
examples/  (1 files)
  README.md
lib/  (11 files)
  auth.js
  cookies.js
  getProxyFromURI.js
  har.js
  hawk.js
  helpers.js
  multipart.js
  oauth.js
  querystring.js
  redirect.js
  tunnel.js
tests/  (86 files)
  browser/  (5 files)
    ssl/  (2 files)
      … 2 files under this directory
    karma.conf.js
    start.js
    test.js
  fixtures/  (1 files)
    har.json
  ssl/  (23 files)
    ca/  (21 files)
      … 21 files under this directory
    npm-ca.crt
    test.crt
  server.js
  squid.conf
  test-agent.js
  test-agentOptions.js
  test-api.js
  test-aws.js
  test-baseUrl.js
  test-basic-auth.js
  test-bearer-auth.js
  test-body.js
  test-cookies.js
  test-defaults.js
  test-digest-auth.js
  test-emptyBody.js
  test-errors.js
  test-event-forwarding.js
  test-follow-all-303.js
  test-follow-all.js
  test-form-data-error.js
  test-form-data.js
  test-form-urlencoded.js
  test-form.js
  test-gzip.js
  test-har.js
  … 33 more files
.gitignore
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
codecov.yml
disabled.appveyor.yml
index.js
package.json
release.sh
request.js
```

## Entry points

- [index.js](https://github.com/request/request/blob/3c0cddc7c8eb60b470e9519da85896ed7ee0081e/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 11 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 86 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/stale.yml` (config)
- `.travis.yml` (ci)
- `codecov.yml` (config)
- `disabled.appveyor.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `tests` — 86 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `lib` — 11 analysed file(s)
- `.github` — 3 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (7 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3c0cddc7c8eb60b470e9519da85896ed7ee0081e` is the revision these paths and observations refer to.
