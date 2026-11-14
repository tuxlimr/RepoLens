# Project structure: karma-runner/karma

**Analysed commit:** `84f85e7016efc2266fa6b3465f494a3fa151c85c`

**Commit reference:** [84f85e7016efc2266fa6b3465f494a3fa151c85c](https://github.com/karma-runner/karma/commit/84f85e7016efc2266fa6b3465f494a3fa151c85c)

**Tree at this commit:** [karma-runner/karma@84f85e7016ef](https://github.com/karma-runner/karma/tree/84f85e7016efc2266fa6b3465f494a3fa151c85c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | karma-runner/karma |
| Description | Spectacular Test Runner for JavaScript |
| Stars | 11951 |
| Forks | 1703 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `84f85e7016efc2266fa6b3465f494a3fa151c85c` |
| Retrieved at | 2026-11-14T19:12:12.151544+00:00 |
| Files in this snapshot | 261 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (3 files)
    lint.yml
    release.yml
    test.yml
bin/  (1 files)
  karma
client/  (5 files)
  .eslintrc
  constants.js
  karma.js
  main.js
  updater.js
common/  (2 files)
  stringify.js
  util.js
context/  (2 files)
  karma.js
  main.js
docs/  (29 files)
  about/  (2 files)
    01-versioning.md
    03-migration.md
  config/  (5 files)
    01-configuration-file.md
    02-files.md
    03-browsers.md
    04-preprocessors.md
    05-plugins.md
  dev/  (6 files)
    01-contributing.md
    02-making-changes.md
    03-maintaining.md
    04-public-api.md
    05-plugins.md
    06-git-commit-msg.md
  intro/  (5 files)
    01-installation.md
    02-configuration.md
    03-how-it-works.md
    04-faq.md
    05-troubleshooting.md
  plus/  (10 files)
    01-requirejs.md
    02-travis.md
    03-jenkins.md
    04-semaphore.md
    05-cloud9.md
    06-angularjs.md
    07-yeoman.md
    08-emberjs.md
    09-codio.md
    10-teamcity.md
  index.md
lib/  (56 files)
  init/  (4 files)
    color_schemes.js
    formatters.js
    log-queue.js
    state_machine.js
  launchers/  (4 files)
    base.js
    capture_timeout.js
    process.js
    retry.js
  middleware/  (7 files)
    common.js
    karma.js
    proxy.js
    runner.js
    source_files.js
    stopper.js
    strip_host.js
  reporters/  (7 files)
    base.js
    base_color.js
    dots.js
    dots_color.js
    multi.js
    progress.js
    progress_color.js
  utils/  (6 files)
    crypto-utils.js
    dns-utils.js
    file-utils.js
    net-utils.js
    path-utils.js
    pattern-utils.js
  browser.js
  browser_collection.js
  browser_result.js
  cli.js
  completion.js
  config.js
  constants.js
  detached.js
  emitter_wrapper.js
  events.js
  executor.js
  file-list.js
  file.js
  helper.js
  index.js
  init.js
  launcher.js
  logger.js
  plugin.js
  preprocessor.js
  reporter.js
  runner.js
  server.js
  stopper.js
  … 4 more files
logo/  (1 files)
  logo.svg
scripts/  (3 files)
  client.js
  integration-tests.sh
  karma-completion.sh
static/  (7 files)
  client.html
  client_with_context.html
  context.html
  context.js
  debug.html
  debug.js
  karma.js
test/  (124 files)
  client/  (7 files)
    .eslintrc
    browser-exceptions.log
    karma.conf.js
    karma.spec.js
    mocks.js
    stringify.spec.js
    util.spec.js
  e2e/  (69 files)
    step_definitions/  (3 files)
      … 3 files under this directory
    support/  (41 files)
      … 41 files under this directory
    .eslintrc
    basic.feature
    browser_console.feature
    cli.feature
    custom-context.feature
    displayname.feature
    error.feature
    files.feature
    headers.feature
    helpful-logs.feature
    launcher-error.feature
    load.feature
    middleware.feature
    mocharepoter.feature
    module-types.feature
    pass-opts.feature
    proxy.feature
    reconnecting.feature
    reporting.feature
    restart-on-change.feature
    runInParent.feature
    stop.feature
    tag.feature
    timeout.feature
    … 1 more files
  unit/  (46 files)
    certificates/  (1 files)
      … 1 files under this directory
    fixtures/  (2 files)
      … 2 files under this directory
    init/  (2 files)
      … 2 files under this directory
    launchers/  (4 files)
      … 4 files under this directory
    middleware/  (5 files)
      … 5 files under this directory
    mocks/  (1 files)
      … 1 files under this directory
    reporters/  (2 files)
      … 2 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    browser.spec.js
    browser_collection.spec.js
    browser_result.spec.js
    cli.spec.js
    completion.spec.js
    config.spec.js
    emitter_wrapper.spec.js
    events.spec.js
    executor.spec.js
    file-list.spec.js
    file.spec.js
    helper.spec.js
    index.spec.js
    init.spec.js
    launcher.spec.js
    logger.spec.js
    mocha-globals.js
    plugin.spec.js
    preprocessor.spec.js
    reporter.spec.js
    runner.spec.js
    server.spec.js
    url.spec.js
    watcher.spec.js
    … 1 more files
  .eslintrc
  mocha.opts
tools/  (2 files)
  update-contributors.js
  update-docs.js
.codeclimate.yml
.eslintignore
.eslintrc.json
.gitattributes
.gitignore
.mailmap
.npmignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
README.md
SECURITY.md
commitlint.config.js
config.tpl.coffee
config.tpl.js
config.tpl.ls
config.tpl.ts
cucumber.js
package.json
release.config.js
requirejs.config.tpl.coffee
requirejs.config.tpl.js
… 1 more files
```

## Entry points

- [bin/karma](https://github.com/karma-runner/karma/blob/84f85e7016efc2266fa6b3465f494a3fa151c85c/bin/karma)
- [client/main.js](https://github.com/karma-runner/karma/blob/84f85e7016efc2266fa6b3465f494a3fa151c85c/client/main.js)
- [context/main.js](https://github.com/karma-runner/karma/blob/84f85e7016efc2266fa6b3465f494a3fa151c85c/context/main.js)
- [lib/index.js](https://github.com/karma-runner/karma/blob/84f85e7016efc2266fa6b3465f494a3fa151c85c/lib/index.js)
- [lib/server.js](https://github.com/karma-runner/karma/blob/84f85e7016efc2266fa6b3465f494a3fa151c85c/lib/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| common package | library | Observed | Groups 2 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| context package | library | Observed | Groups 2 file(s) under context package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 4 file(s) under external integrations (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 56 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| static package | library | Observed | Groups 3 file(s) under static package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 124 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 2 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.eslintrc.json` (config)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `test` — 124 analysed file(s)
- `lib` — 56 analysed file(s)
- `docs` — 29 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `static` — 7 analysed file(s)
- `client` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `scripts` — 3 analysed file(s)
- `common` — 2 analysed file(s)
- `context` — 2 analysed file(s)
- `tools` — 2 analysed file(s)
- `bin` — 1 analysed file(s)
- `logo` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `84f85e7016efc2266fa6b3465f494a3fa151c85c` is the revision these paths and observations refer to.
