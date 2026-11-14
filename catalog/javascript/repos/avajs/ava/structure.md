# Project structure: avajs/ava

**Analysed commit:** `a4fb2094052078faca5094fbe8cab7cbf18c785b`

**Commit reference:** [a4fb2094052078faca5094fbe8cab7cbf18c785b](https://github.com/avajs/ava/commit/a4fb2094052078faca5094fbe8cab7cbf18c785b)

**Tree at this commit:** [avajs/ava@a4fb20940520](https://github.com/avajs/ava/tree/a4fb2094052078faca5094fbe8cab7cbf18c785b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | avajs/ava |
| Description | Node.js test runner that lets you develop with confidence 🚀 |
| Stars | 20829 |
| Forks | 1468 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `a4fb2094052078faca5094fbe8cab7cbf18c785b` |
| Retrieved at | 2026-11-14T19:11:11.971852+00:00 |
| Files in this snapshot | 792 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.md
    config.yml
    feature.md
  workflows/  (2 files)
    ci.yml
    release.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
docs/  (28 files)
  recipes/  (19 files)
    babel.md
    browser-testing.md
    code-coverage.md
    debugging-with-chrome-devtools.md
    debugging-with-vscode.md
    debugging-with-webstorm.md
    endpoint-testing-with-mongoose.md
    endpoint-testing.md
    isolated-mongodb-integration-tests.md
    passing-arguments-to-your-test-files.md
    puppeteer.md
    shared-workers.md
    splitting-tests-ci.md
    test-setup.md
    testing-with-selenium-webdriverjs.md
    typescript.md
    vue.md
    watch-mode.md
    when-to-use-plan.md
  01-writing-tests.md
  02-execution-context.md
  03-assertions.md
  04-snapshot-testing.md
  05-command-line.md
  06-configuration.md
  07-test-timeouts.md
  08-common-pitfalls.md
  support-statement.md
entrypoints/  (7 files)
  cli.js
  eslint-plugin-helper.js
  internal.d.ts
  main.d.ts
  main.js
  plugin.d.ts
  plugin.js
examples/  (47 files)
  endpoint-testing/  (4 files)
    app.js
    package.json
    readme.md
    test.js
  macros/  (4 files)
    index.js
    package.json
    readme.md
    test.js
  matching-titles/  (3 files)
    package.json
    readme.md
    test.js
  specific-line-numbers/  (3 files)
    package.json
    readme.md
    test.js
  tap-reporter/  (3 files)
    package.json
    readme.md
    test.js
  timeouts/  (4 files)
    index.js
    package.json
    readme.md
    test.js
  typescript-build/  (7 files)
    source/  (2 files)
      … 2 files under this directory
    .gitignore
    ava.config.js
    package.json
    readme.md
    tsconfig.json
  typescript-context/  (7 files)
    source/  (2 files)
      … 2 files under this directory
    .gitignore
    ava.config.js
    package.json
    readme.md
    tsconfig.json
  typescript-loader/  (6 files)
    source/  (2 files)
      … 2 files under this directory
    ava.config.js
    package.json
    readme.md
    tsconfig.json
  typescript-native/  (6 files)
    source/  (2 files)
      … 2 files under this directory
    ava.config.js
    package.json
    readme.md
    tsconfig.json
lib/  (53 files)
  plugin-support/  (2 files)
    shared-worker-loader.js
    shared-workers.js
  reporters/  (7 files)
    beautify-stack.js
    colors.js
    default.js
    format-serialized-error.js
    improper-usage-messages.js
    prefix-title.js
    tap.js
  worker/  (10 files)
    base.js
    channel.js
    completion-handlers.js
    guard-environment.js
    line-numbers.js
    main.js
    options.js
    plugin.js
    state.js
    utils.js
  api-event-iterator.js
  api.js
  assert.js
  assertion-error.js
  chalk.js
  cli.js
  code-excerpt.js
  concordance-options.js
  concordance.js
  context-ref.js
  create-chain.js
  environment-variables.js
  eslint-plugin-helper-worker.js
  extensions.js
  fork.js
  glob-helpers.js
  globs.js
  ipc-flow-control.js
  is-ci.js
  like-selector.js
  line-numbers.js
  load-config.js
  node-arguments.js
  now-and-timers.js
  … 10 more files
media/  (11 files)
  screenshot-fixtures/  (9 files)
    magic-assert-buffers.js
    magic-assert-exceptions.js
    magic-assert-objects.js
    magic-assert-strings.js
    mini-reporter.md
    package.json
    snapshot-testing.md
    tap-reporter.js
    verbose-reporter.js
  logo.ai
  logo.svg
scripts/  (2 files)
  ci.sh
  test.sh
test/  (309 files)
  assertions/  (9 files)
    fixtures/  (7 files)
      … 7 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    test.js
  builtin-nodejs-assert/  (3 files)
    fixtures/  (2 files)
      … 2 files under this directory
    test.js
  child-process/  (3 files)
    fixtures/  (2 files)
      … 2 files under this directory
    test.js
  completion-handlers/  (5 files)
    fixtures/  (4 files)
      … 4 files under this directory
    test.js
  concurrency/  (4 files)
    fixtures/  (2 files)
      … 2 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    test.js
  config/  (41 files)
    fixtures/  (35 files)
      … 35 files under this directory
    snapshots/  (3 files)
      … 3 files under this directory
    integration.js
    loader.js
    next-gen.js
  config-require/  (22 files)
    fixtures/  (21 files)
      … 21 files under this directory
    test.js
  create-chain/  (1 files)
    test.js
  environment-variables/  (6 files)
    fixtures/  (4 files)
      … 4 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    test.js
  extensions/  (6 files)
    fixtures/  (4 files)
      … 4 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    test.js
  external-assertions/  (5 files)
    fixtures/  (3 files)
      … 3 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    test.js
  globs/  (12 files)
    fixtures/  (10 files)
      … 10 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    test.js
  helpers/  (3 files)
    exec.js
    simulate-tty.js
    with-temporary-fixture.js
  hook-restrictions/  (5 files)
    fixtures/  (3 files)
      … 3 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    test.js
  idle-timeouts/  (3 files)
    fixtures/  (2 files)
      … 2 files under this directory
    test.js
  internal-events/  (5 files)
    fixtures/  (4 files)
      … 4 files under this directory
    test.js
  line-numbers/  (6 files)
    fixtures/  (4 files)
      … 4 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    test.js
  macros/  (3 files)
    fixtures/  (2 files)
      … 2 files under this directory
    test.js
  meta/  (4 files)
    fixtures/  (3 files)
      … 3 files under this directory
    test.js
  multiple-implementations/  (4 files)
    fixtures/  (3 files)
      … 3 files under this directory
    test.js
  node-arguments/  (11 files)
    fixtures/  (9 files)
      … 9 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    test.js
  scheduler/  (5 files)
    fixtures/  (4 files)
      … 4 files under this directory
    test.js
  shared-workers/  (57 files)
    cannot-publish-before-available/  (5 files)
      … 5 files under this directory
    lifecycle/  (5 files)
      … 5 files under this directory
    multiple-workers-are-loaded/  (4 files)
      … 4 files under this directory
    restricted-to-worker-threads/  (4 files)
      … 4 files under this directory
    timeout/  (4 files)
      … 4 files under this directory
    unsupported-protocol/  (6 files)
      … 6 files under this directory
    worker-execution-crash/  (6 files)
      … 6 files under this directory
    worker-protocol/  (8 files)
      … 8 files under this directory
    worker-startup-crashes/  (9 files)
      … 9 files under this directory
    workers-are-loaded-once/  (6 files)
      … 6 files under this directory
  snapshot-order/  (13 files)
    fixtures/  (8 files)
      … 8 files under this directory
    helpers/  (1 files)
      … 1 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    intertest-order.js
    randomness.js
    report-declaration-order.js
  snapshot-regenerate-report/  (3 files)
    fixtures/  (2 files)
      … 2 files under this directory
    test.js
  snapshot-removal/  (29 files)
    fixtures/  (26 files)
      … 26 files under this directory
    helpers/  (1 files)
      … 1 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    test.js
  snapshot-tests/  (19 files)
    fixtures/  (12 files)
      … 12 files under this directory
    snapshots/  (3 files)
      … 3 files under this directory
    code-block.js
    corrupt.js
    formatting.js
    large.js
  snapshot-workflow/  (20 files)
    fixtures/  (17 files)
      … 17 files under this directory
    README.md
    adding.js
    changing-label.js
  .fake-root
  README.md
test-tap/  (300 files)
  fixture/  (216 files)
    ava-paths/  (1 files)
      … 1 files under this directory
    caching/  (2 files)
      … 2 files under this directory
    eslint-plugin-helper/  (4 files)
      … 4 files under this directory
    esm/  (1 files)
      … 1 files under this directory
    extensions/  (2 files)
      … 2 files under this directory
    fail-fast/  (11 files)
      … 11 files under this directory
    globs/  (30 files)
      … 30 files under this directory
    ignored-dirs/  (2 files)
      … 2 files under this directory
    load-config/  (28 files)
      … 28 files under this directory
    package-config/  (2 files)
      … 2 files under this directory
    parallel-runs/  (24 files)
      … 24 files under this directory
    pkg-type-module/  (2 files)
      … 2 files under this directory
    report/  (36 files)
      … 36 files under this directory
    reset-cache/  (2 files)
      … 2 files under this directory
    snapshots/  (25 files)
      … 25 files under this directory
    sort-tests/  (5 files)
      … 5 files under this directory
    stalled-tests/  (2 files)
      … 2 files under this directory
    symlinkdir/  (1 files)
      … 1 files under this directory
    tap/  (2 files)
      … 2 files under this directory
    with-dependencies/  (7 files)
      … 7 files under this directory
    .fake-root
    assert.js.md
    error-in-anonymous-function.js
    es2015.js
    formatting-color.js
    hooks-skipped.js
    infinity-stack-trace.js
    js.js
    long-running.js
    match-no-match-2.js
    match-no-match.js
    matcher-skip.js
    mjs.mjs
    no-tests.js
    node-env-foo.js
    node-env-test.js
    package.json
    process-cwd-default.js
    process-cwd-pkgdir.js
    serial.js
    skip-only.js
    target-symlink.js
    test-count-2.js
    test-count-3.js
    … 3 more files
  helper/  (8 files)
    ava-test.js
    chalk0.js
    cli.js
    fix-reporter-env.js
    replay-report.js
    report-worker.js
    report.js
    tty-stream.js
  integration/  (7 files)
    assorted.js
    debug.js
    parallel-runs.js
    repl.js
    snapshots.js
    stack-traces.js
    stalled.js
  reporters/  (53 files)
    default.edgecases.v22.log
    default.edgecases.v24.log
    default.edgecases.v26.log
    default.failfast.v22.log
    default.failfast.v24.log
    default.failfast.v26.log
    default.failfast2.v22.log
    default.failfast2.v24.log
    default.failfast2.v26.log
    default.js
    default.only.v22.log
    default.only.v24.log
    default.only.v26.log
    default.regular.v22.log
    default.regular.v24.log
    default.regular.v26.log
    default.timeoutcontextlogs.v22.log
    default.timeoutcontextlogs.v24.log
    default.timeoutcontextlogs.v26.log
    default.timeoutinmultiplefiles.v22.log
    default.timeoutinmultiplefiles.v24.log
    default.timeoutinmultiplefiles.v26.log
    default.timeoutinsinglefile.v22.log
    default.timeoutinsinglefile.v24.log
    … 29 more files
  api.js
  assert.js
  chalk.js
  code-excerpt.js
  eslint-plugin-helper.js
  globs.js
  hooks.js
  line-numbers.js
  node-arguments.js
  promise.js
  run-status.js
  runner.js
  test-try-commit.js
  test.js
  try-snapshot.js
  tsconfig.json
test-types/  (14 files)
  module/  (13 files)
    assertions-as-type-guards.ts
    conditional-chains.ts
    context.ts
    deep-equal.ts
    implementation-result.ts
    like.ts
    macros.ts
    plugin.ts
    snapshot.ts
    teardown.ts
    throws.ts
    timeout.ts
    try-commit.ts
  .gitignore
.c8rc.json
.editorconfig
.gitattributes
.gitignore
.taprc
ava.config.js
index.d.ts
license
maintaining.md
mise.toml
package.json
plugin.d.ts
pnpm-workspace.yaml
readme.md
```

## Entry points

- [media/screenshot-fixtures/magic-assert-buffers.js](https://github.com/avajs/ava/blob/a4fb2094052078faca5094fbe8cab7cbf18c785b/media/screenshot-fixtures/magic-assert-buffers.js)
- [entrypoints/cli.js](https://github.com/avajs/ava/blob/a4fb2094052078faca5094fbe8cab7cbf18c785b/entrypoints/cli.js)
- [entrypoints/main.js](https://github.com/avajs/ava/blob/a4fb2094052078faca5094fbe8cab7cbf18c785b/entrypoints/main.js)
- [lib/worker/main.js](https://github.com/avajs/ava/blob/a4fb2094052078faca5094fbe8cab7cbf18c785b/lib/worker/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 54 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| entrypoints package | library | Observed | Groups 7 file(s) under entrypoints package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 7 file(s) under external integrations (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 53 file(s) under lib package (observed from repository paths and static analysis). |
| media package | library | Observed | Groups 6 file(s) under media package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| test-tap package | library | Observed | Groups 161 file(s) under test-tap package (observed from repository paths and static analysis). |
| test-types package | library | Observed | Groups 13 file(s) under test-types package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 332 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.c8rc.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `examples/endpoint-testing/package.json` (manifest)
- `examples/macros/package.json` (manifest)
- `examples/matching-titles/package.json` (manifest)
- `examples/specific-line-numbers/package.json` (manifest)
- `examples/tap-reporter/package.json` (manifest)
- `examples/timeouts/package.json` (manifest)
- `examples/typescript-build/package.json` (manifest)
- `examples/typescript-build/tsconfig.json` (config)
- `examples/typescript-context/package.json` (manifest)
- `examples/typescript-context/tsconfig.json` (config)
- `examples/typescript-loader/package.json` (manifest)
- `examples/typescript-loader/tsconfig.json` (config)
- `examples/typescript-native/package.json` (manifest)
- `examples/typescript-native/tsconfig.json` (config)
- `media/screenshot-fixtures/package.json` (manifest)
- `mise.toml` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `test-tap/fixture/caching/package.json` (manifest)
- `test-tap/fixture/eslint-plugin-helper/for-overriding/package.json` (manifest)
- `test-tap/fixture/eslint-plugin-helper/package.json` (manifest)
- `test-tap/fixture/esm/package.json` (manifest)
- `test-tap/fixture/extensions/package.json` (manifest)
- `test-tap/fixture/globs/no-files/package.json` (manifest)
- `test-tap/fixture/load-config/contains-ava-property/package.json` (manifest)
- `test-tap/fixture/load-config/explicit-bad-extension/package.json` (manifest)
- `test-tap/fixture/load-config/factory-no-plain-return/package.json` (manifest)
- `test-tap/fixture/load-config/no-default-export/package.json` (manifest)
- `test-tap/fixture/load-config/no-plain-config/package.json` (manifest)
- `test-tap/fixture/load-config/non-function/package.json` (manifest)
- `test-tap/fixture/load-config/non-object-experiments/package.json` (manifest)
- `test-tap/fixture/load-config/package-no-file-yes-factory/package.json` (manifest)
- `test-tap/fixture/load-config/package-no-file-yes/package.json` (manifest)
- `test-tap/fixture/load-config/package-only/package.json` (manifest)
- `test-tap/fixture/load-config/package-yes-explicit-yes/package.json` (manifest)
- `test-tap/fixture/load-config/package-yes-file-yes/package.json` (manifest)
- `test-tap/fixture/load-config/throws/package.json` (manifest)
- `test-tap/fixture/load-config/unsupported-experiments/package.json` (manifest)
- `test-tap/fixture/package-config/fail-without-assertions/package.json` (manifest)
- `test-tap/fixture/package.json` (manifest)
- `test-tap/fixture/parallel-runs/custom-comparator/package.json` (manifest)
- `test-tap/fixture/parallel-runs/less-files-than-ci-total/package.json` (manifest)
- `test-tap/fixture/parallel-runs/more-files-than-ci-total/package.json` (manifest)
- `test-tap/fixture/parallel-runs/no-files/package.json` (manifest)
- `test-tap/fixture/pkg-type-module/package.json` (manifest)
- `test-tap/fixture/report/failfast/package.json` (manifest)
- `test-tap/fixture/report/failfast2/package.json` (manifest)
- `test-tap/fixture/report/only/package.json` (manifest)
- `test-tap/fixture/report/regular/package.json` (manifest)
- `test-tap/fixture/report/timeoutcontextlogs/package.json` (manifest)
- `test-tap/fixture/report/timeoutinmultiplefiles/package.json` (manifest)
- `test-tap/fixture/report/timeoutinsinglefile/package.json` (manifest)
- `test-tap/fixture/report/timeoutwithmatch/package.json` (manifest)
- `test-tap/fixture/report/watch/package.json` (manifest)
- `test-tap/fixture/reset-cache/package.json` (manifest)
- `test-tap/fixture/snapshots/__tests__-dir/package.json` (manifest)
- `test-tap/fixture/snapshots/package.json` (manifest)
- `test-tap/fixture/snapshots/test-content/package.json` (manifest)
- `test-tap/fixture/snapshots/test-dir/package.json` (manifest)
- `test-tap/fixture/snapshots/test-snapshot-location/package.json` (manifest)
- `test-tap/fixture/snapshots/test-sourcemaps/package.json` (manifest)
- `test-tap/fixture/snapshots/test-sourcemaps/tsconfig.json` (config)
- `test-tap/fixture/snapshots/tests-dir/package.json` (manifest)
- `test-tap/fixture/snapshots/watcher-rerun-unlink/package.json` (manifest)
- `test-tap/fixture/snapshots/watcher-rerun/package.json` (manifest)
- `test-tap/fixture/sort-tests/package.json` (manifest)
- `test-tap/fixture/tap/package.json` (manifest)
- `test-tap/tsconfig.json` (config)

## Top-level layout

- `test` — 309 analysed file(s)
- `test-tap` — 300 analysed file(s)
- `lib` — 53 analysed file(s)
- `examples` — 47 analysed file(s)
- `docs` — 28 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `test-types` — 14 analysed file(s)
- `media` — 11 analysed file(s)
- `.github` — 7 analysed file(s)
- `entrypoints` — 7 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 8 file(s) were skipped during inventory (1 x likely secret file excluded; 7 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a4fb2094052078faca5094fbe8cab7cbf18c785b` is the revision these paths and observations refer to.
