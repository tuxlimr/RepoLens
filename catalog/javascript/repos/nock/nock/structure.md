# Project structure: nock/nock

**Analysed commit:** `3e817ab5415606cc44eab247691d4035c037c322`

**Commit reference:** [3e817ab5415606cc44eab247691d4035c037c322](https://github.com/nock/nock/commit/3e817ab5415606cc44eab247691d4035c037c322)

**Tree at this commit:** [nock/nock@3e817ab54156](https://github.com/nock/nock/tree/3e817ab5415606cc44eab247691d4035c037c322)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nock/nock |
| Description | HTTP server mocking and expectations library for Node.js |
| Stars | 13141 |
| Forks | 793 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `3e817ab5415606cc44eab247691d4035c037c322` |
| Retrieved at | 2026-11-14T19:11:59.970155+00:00 |
| Files in this snapshot | 121 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    01_bug_report.yml
    02_feature_request.yml
    config.yml
  workflows/  (3 files)
    continuous-delivery.yaml
    continuous-integration.yaml
    fix-formatting.yaml
  dependabot.yml
  lock.yml
  stale.yml
  toc.yml
examples/  (10 files)
  .eslintrc.yml
  _log.js
  binary-reply.js
  delay-response.js
  net-connect-default-no-mock.js
  net-connect-default-other-mock.js
  net-connect-disabled-different-host.js
  net-connect-mock-same-host-different-path.js
  socket-delay-abort.js
  socket-delay-no-abort.js
lib/  (14 files)
  interceptors/  (1 files)
    builtin.ts
  utils/  (1 files)
    node/  (1 files)
      … 1 files under this directory
  back.ts
  common.ts
  debug.ts
  global_emitter.ts
  handle-request.ts
  intercept.ts
  interceptor.ts
  match_body.ts
  playback_interceptor.ts
  recorder.ts
  scope.ts
  stringify.ts
migration_guides/  (5 files)
  migrating_to_10.md
  migrating_to_11.md
  migrating_to_12.md
  migrating_to_13.md
  migrating_to_15.md
rfcs/  (1 files)
  rfc-001.md
scripts/  (3 files)
  build.js
  test-build.js
  test-leak.js
tests/  (60 files)
  assets/  (1 files)
    reply_file_1.txt
  fixtures/  (3 files)
    content_length_test.json
    good_request.json
    wrong_uri.json
  got/  (38 files)
    fixtures/  (1 files)
      … 1 files under this directory
    got_client.js
    test_allow_unmocked.js
    test_allow_unmocked_https.js
    test_back_filters.js
    test_basic_auth.js
    test_body_match.js
    test_content_encoding.js
    test_default_reply_headers.js
    test_define.js
    test_delay.js
    test_dynamic_mock.js
    test_events.js
    test_fake_timer.js
    test_header_matching.js
    test_intercept.js
    test_intercept_parallel.js
    test_logging.js
    test_net_connect.js
    test_nock_lifecycle.js
    test_nock_off.js
    test_passthrough.js
    test_persist_optionally.js
    test_query.js
    test_query_complex.js
    … 13 more files
  servers/  (3 files)
    ca.crt
    index.js
    localhost.crt
  setup.js
  test_abort.js
  test_abort_signal.js
  test_back.js
  test_client_request.js
  test_common.js
  test_destroy.js
  test_fetch.js
  test_gzip_request.js
  test_ipv6.js
  test_reply_with_error.js
  test_socket.js
  test_stringify.js
  test_undici.js
  test_unix_socket.js
.all-contributorsrc
.gitignore
.mocharc.json
.npmignore
.nycrc.yml
.prettierignore
.prettierrc.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTORS.md
LICENSE
README.md
eslint.config.mjs
index.ts
package.json
tsconfig.build.json
tsconfig.json
```

## Entry points

- [index.ts](https://github.com/nock/nock/blob/3e817ab5415606cc44eab247691d4035c037c322/index.ts)
- [lib/utils/node/index.ts](https://github.com/nock/nock/blob/3e817ab5415606cc44eab247691d4035c037c322/lib/utils/node/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 14 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 60 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/01_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/02_feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/lock.yml` (config)
- `.github/stale.yml` (config)
- `.github/toc.yml` (config)
- `.github/workflows/continuous-delivery.yaml` (ci)
- `.github/workflows/continuous-integration.yaml` (ci)
- `.github/workflows/fix-formatting.yaml` (ci)
- `.mocharc.json` (config)
- `.nycrc.yml` (config)
- `.prettierrc.yml` (config)
- `examples/.eslintrc.yml` (config)
- `package.json` (manifest)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `tests` — 60 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `lib` — 14 analysed file(s)
- `.github` — 10 analysed file(s)
- `examples` — 10 analysed file(s)
- `migration_guides` — 5 analysed file(s)
- `scripts` — 3 analysed file(s)
- `rfcs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3e817ab5415606cc44eab247691d4035c037c322` is the revision these paths and observations refer to.
