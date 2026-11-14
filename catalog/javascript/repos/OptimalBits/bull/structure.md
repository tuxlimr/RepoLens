# Project structure: OptimalBits/bull

**Analysed commit:** `73d065506931fc876c67c721bc424b2bd76b520b`

**Commit reference:** [73d065506931fc876c67c721bc424b2bd76b520b](https://github.com/OptimalBits/bull/commit/73d065506931fc876c67c721bc424b2bd76b520b)

**Tree at this commit:** [OptimalBits/bull@73d065506931](https://github.com/OptimalBits/bull/tree/73d065506931fc876c67c721bc424b2bd76b520b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | OptimalBits/bull |
| Description | Premium Queue package for handling distributed jobs and messages in NodeJS. |
| Stars | 16265 |
| Forks | 1391 |
| Licence | Other |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `73d065506931fc876c67c721bc424b2bd76b520b` |
| Retrieved at | 2026-11-14T19:11:33.573751+00:00 |
| Files in this snapshot | 108 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (3 files)
    codeql-analysis.yml
    node.js.yml
    release.yml
  issue_template.md
  stale.yml
docs/  (2 files)
  README.md
  _config.yml
lib/  (51 files)
  commands/  (36 files)
    includes/  (8 files)
      … 8 files under this directory
    addJob-6.lua
    addLog-2.lua
    cleanJobsInSet-3.lua
    extendLock-2.lua
    getCountsPerPriority-4.lua
    index.js
    isFinished-2.lua
    isJobInList-1.lua
    moveStalledJobsToWait-7.lua
    moveToActive-8.lua
    moveToDelayed-4.lua
    moveToFinished-9.lua
    obliterate-2.lua
    pause-5.lua
    promote-5.lua
    releaseLock-1.lua
    removeJob-11.lua
    removeJobs-8.lua
    removeRepeatable-2.lua
    reprocessJob-6.lua
    retryJob-7.lua
    retryJobs-5.lua
    saveStacktrace-1.lua
    script-loader.js
    … 4 more files
  process/  (4 files)
    child-pool.js
    master.js
    sandbox.js
    utils.js
  backoffs.js
  errors.js
  getters.js
  job.js
  p-timeout.js
  queue.js
  repeatable.js
  scripts.js
  timer-manager.js
  utils.js
  worker.js
support/  (1 files)
  logo.svg
test/  (29 files)
  fixtures/  (13 files)
    fixture_processor.js
    fixture_processor_bar.js
    fixture_processor_broken.js
    fixture_processor_callback.js
    fixture_processor_callback_fail.js
    fixture_processor_crash.js
    fixture_processor_data.js
    fixture_processor_discard.js
    fixture_processor_exit.js
    fixture_processor_fail.js
    fixture_processor_foo.js
    fixture_processor_progress.js
    fixture_processor_slow.js
  .eslintrc.yml
  test_child-pool.js
  test_connection.js
  test_events.js
  test_getters.js
  test_job.js
  test_metrics.js
  test_obliterate.js
  test_pause.js
  test_queue.js
  test_rate_limiter.js
  test_repeat.js
  test_sandboxed_process.js
  test_when_current_jobs_finished.js
  test_worker.js
  utils.js
.editorconfig
.eslintrc.yml
.gitignore
.mocharc.json
.npmignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
MIGRATION.md
PATTERNS.md
README.md
REFERENCE.md
commandTransform.js
commitlint.config.js
docker-compose.yml
generateRawScripts.js
index.d.ts
index.js
package.json
```

## Entry points

- [index.js](https://github.com/OptimalBits/bull/blob/73d065506931fc876c67c721bc424b2bd76b520b/index.js)
- [lib/commands/index.js](https://github.com/OptimalBits/bull/blob/73d065506931fc876c67c721bc424b2bd76b520b/lib/commands/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 17 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 29 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/node.js.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.mocharc.json` (config)
- `docker-compose.yml` (container)
- `docs/_config.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `lib` — 51 analysed file(s)
- `test` — 29 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 5 analysed file(s)
- `docs` — 2 analysed file(s)
- `support` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `73d065506931fc876c67c721bc424b2bd76b520b` is the revision these paths and observations refer to.
