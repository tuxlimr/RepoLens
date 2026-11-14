# Project structure: petkaantonov/bluebird

**Analysed commit:** `c220cfe480868e2f5c5de4fe8bb3b04b97588d7f`

**Commit reference:** [c220cfe480868e2f5c5de4fe8bb3b04b97588d7f](https://github.com/petkaantonov/bluebird/commit/c220cfe480868e2f5c5de4fe8bb3b04b97588d7f)

**Tree at this commit:** [petkaantonov/bluebird@c220cfe48086](https://github.com/petkaantonov/bluebird/tree/c220cfe480868e2f5c5de4fe8bb3b04b97588d7f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | petkaantonov/bluebird |
| Description | :bird: :zap: Bluebird is a full featured promise library with unmatched performance. |
| Stars | 20459 |
| Forks | 2301 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c220cfe480868e2f5c5de4fe8bb3b04b97588d7f` |
| Retrieved at | 2026-11-14T19:11:13.995510+00:00 |
| Files in this snapshot | 368 |

## Directory tree

```text
benchmark/  (79 files)
  analysis/  (2 files)
    promises-bluebird-parallel.js
    promises-bluebird.js
  doxbee-sequential/  (24 files)
    callbacks-baseline.js
    callbacks-caolan-async-waterfall.js
    callbacks-suguru03-neo-async-waterfall.js
    generators-tj-co.js
    observables-Reactive-Extensions-RxJS.js
    observables-baconjs-bacon.js.js
    observables-caolan-highland.js
    observables-pozadi-kefir.js
    promises-bluebird-generator.js
    promises-bluebird.js
    promises-calvinmetcalf-lie.js
    promises-cujojs-when.js
    promises-dfilatov-vow.js
    promises-ecmascript6-native.js
    promises-kriskowal-q.js
    promises-lvivski-davy.js
    promises-medikoo-deferred.js
    promises-native-async-await.js
    promises-obvious-kew.js
    promises-then-promise.js
    promises-tildeio-rsvp.js
    streamline-callbacks.js
    streamline-generators.js
    streamline._js
  doxbee-sequential-errors/  (17 files)
    callbacks-baseline.js
    callbacks-caolan-async-waterfall.js
    callbacks-suguru03-neo-async-waterfall.js
    promises-bluebird-generator.js
    promises-bluebird.js
    promises-calvinmetcalf-lie.js
    promises-cujojs-when.js
    promises-dfilatov-vow.js
    promises-kriskowal-q.js
    promises-lvivski-davy.js
    promises-medikoo-deferred.js
    promises-obvious-kew.js
    promises-then-promise.js
    promises-tildeio-rsvp.js
    streamline-callbacks.js
    streamline-generators.js
    streamline._js
  lib/  (14 files)
    catcher.js
    dummy.js
    fakemaker.js
    fakes-ctx.js
    fakes.js
    fakesC.js
    fakesO.js
    fakesObservable.js
    fakesP-ctx.js
    fakesP.js
    fakesSJS-dst.js
    fakesSJS-src.sjs
    promiseSupport.js
    timers-ctx.js
  madeup-parallel/  (19 files)
    callbacks-baseline.js
    callbacks-caolan-async-parallel.js
    callbacks-suguru03-neo-async-parallel.js
    generators-tj-co.js
    promises-bluebird-generator.js
    promises-bluebird.js
    promises-calvinmetcalf-lie.js
    promises-cujojs-when.js
    promises-dfilatov-vow.js
    promises-ecmascript6-native.js
    promises-lvivski-davy.js
    promises-medikoo-deferred.js
    promises-native-async-await.js
    promises-obvious-kew.js
    promises-then-promise.js
    promises-tildeio-rsvp.js
    streamline-callbacks.js
    streamline-generators.js
    streamline._js
  README.md
  package.json
  performance.js
docs/  (126 files)
  _layouts/  (3 files)
    api.html
    default.html
    page.html
  _plugins/  (2 files)
    mdate.rb
    plugin.rb
  css/  (2 files)
    main.css
    mono-blue.css
  docs/  (112 files)
    api/  (88 files)
      … 88 files under this directory
    anti-patterns.md
    api-reference.md
    async-dialogs.md
    beginners-guide.md
    benchmarks.md
    changelog.md
    coming-from-other-languages.md
    coming-from-other-libraries.md
    contribute.md
    deprecated-apis.md
    deprecated_apis.md
    download-api-reference.md
    error-explanations.md
    features.md
    getting-started.md
    install.md
    new-in-bluebird-3.md
    support.md
    warning-explanations.md
    what-about-generators.md
    why-bluebird.md
    why-performance.md
    why-promises.md
    working-with-callbacks.md
  img/  (1 files)
    README.txt
  .gitignore
  Gemfile
  README.md
  _config.yml
  helpers.rb
  index.html
src/  (38 files)
  any.js
  assert.js
  async.js
  bind.js
  bluebird.js
  call_get.js
  cancel.js
  catch_filter.js
  constants.js
  context.js
  debuggability.js
  direct_resolve.js
  each.js
  errors.js
  es5.js
  filter.js
  finally.js
  generators.js
  join.js
  map.js
  method.js
  nodeback.js
  nodeify.js
  promise.js
  … 14 more files
test/  (96 files)
  browser/  (12 files)
    es5-sham.js
    es5-shim.js
    have_getters.js
    index.html
    json.js
    main.js
    mocha.css
    mocha.js
    package.json
    promise_debug.js
    promise_instrumented.js
    worker.js
  mocha/  (84 files)
    helpers/  (7 files)
      … 7 files under this directory
    2.1.2.js
    2.1.3.js
    2.2.1.js
    2.2.2.js
    2.2.3.js
    2.2.4.js
    2.2.5.js
    2.2.6.js
    2.2.7.js
    2.3.1.js
    2.3.2.js
    2.3.3.js
    2.3.4.js
    3.2.1.js
    3.2.2.js
    3.2.3.js
    3.2.4.js
    3.2.5.js
    3.2.6.js
    any.js
    api_exceptions.js
    async.js
    async_hooks.js
    bind.js
    … 53 more files
tools/  (12 files)
  job-runner/  (1 files)
    job-runner.js
  README.md
  ast_passes.js
  browser_test_generator.js
  browser_test_runner.js
  build.js
  jshint.js
  jshintrc_generator.js
  mocha_runner.js
  saucelabs_runner.js
  test.js
  utils.js
.editorconfig
.gitignore
.istanbul.yml
.jshintignore
.jshintrc
.travis.yml
API.md
CONTRIBUTING.md
LICENSE
README.md
bench
bower.json
changelog.md
deprecated_apis.md
issue_template.md
package.json
tests
```

## Entry points

- [test/browser/index.html](https://github.com/petkaantonov/bluebird/blob/c220cfe480868e2f5c5de4fe8bb3b04b97588d7f/test/browser/index.html)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| any.js package | library | Observed | Groups 1 file(s) under any.js package (observed from repository paths and static analysis). |
| assert.js package | library | Observed | Groups 1 file(s) under assert.js package (observed from repository paths and static analysis). |
| async.js package | library | Observed | Groups 1 file(s) under async.js package (observed from repository paths and static analysis). |
| benchmark package | library | Observed | Groups 73 file(s) under benchmark package (observed from repository paths and static analysis). |
| bind.js package | library | Observed | Groups 1 file(s) under bind.js package (observed from repository paths and static analysis). |
| bluebird.js package | library | Observed | Groups 1 file(s) under bluebird.js package (observed from repository paths and static analysis). |
| call_get.js package | library | Observed | Groups 1 file(s) under call_get.js package (observed from repository paths and static analysis). |
| cancel.js package | library | Observed | Groups 1 file(s) under cancel.js package (observed from repository paths and static analysis). |
| catch_filter.js package | library | Observed | Groups 1 file(s) under catch_filter.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.js package | library | Observed | Groups 1 file(s) under constants.js package (observed from repository paths and static analysis). |
| context.js package | library | Observed | Groups 1 file(s) under context.js package (observed from repository paths and static analysis). |
| debuggability.js package | library | Observed | Groups 1 file(s) under debuggability.js package (observed from repository paths and static analysis). |
| direct_resolve.js package | library | Observed | Groups 1 file(s) under direct_resolve.js package (observed from repository paths and static analysis). |
| each.js package | library | Observed | Groups 1 file(s) under each.js package (observed from repository paths and static analysis). |
| errors.js package | library | Observed | Groups 1 file(s) under errors.js package (observed from repository paths and static analysis). |
| es5.js package | library | Observed | Groups 1 file(s) under es5.js package (observed from repository paths and static analysis). |
| filter.js package | library | Observed | Groups 1 file(s) under filter.js package (observed from repository paths and static analysis). |
| finally.js package | library | Observed | Groups 1 file(s) under finally.js package (observed from repository paths and static analysis). |
| generators.js package | library | Observed | Groups 1 file(s) under generators.js package (observed from repository paths and static analysis). |
| join.js package | library | Observed | Groups 1 file(s) under join.js package (observed from repository paths and static analysis). |
| map.js package | library | Observed | Groups 1 file(s) under map.js package (observed from repository paths and static analysis). |
| method.js package | library | Observed | Groups 1 file(s) under method.js package (observed from repository paths and static analysis). |
| nodeback.js package | library | Observed | Groups 1 file(s) under nodeback.js package (observed from repository paths and static analysis). |
| nodeify.js package | library | Observed | Groups 1 file(s) under nodeify.js package (observed from repository paths and static analysis). |
| promise_array.js package | library | Observed | Groups 1 file(s) under promise_array.js package (observed from repository paths and static analysis). |
| promise.js package | library | Observed | Groups 1 file(s) under promise.js package (observed from repository paths and static analysis). |
| promisify.js package | library | Observed | Groups 1 file(s) under promisify.js package (observed from repository paths and static analysis). |
| props.js package | library | Observed | Groups 1 file(s) under props.js package (observed from repository paths and static analysis). |
| queue.js package | library | Observed | Groups 1 file(s) under queue.js package (observed from repository paths and static analysis). |
| race.js package | library | Observed | Groups 1 file(s) under race.js package (observed from repository paths and static analysis). |
| reduce.js package | library | Observed | Groups 1 file(s) under reduce.js package (observed from repository paths and static analysis). |
| schedule.js package | library | Observed | Groups 1 file(s) under schedule.js package (observed from repository paths and static analysis). |
| settle.js package | library | Observed | Groups 1 file(s) under settle.js package (observed from repository paths and static analysis). |
| some.js package | library | Observed | Groups 1 file(s) under some.js package (observed from repository paths and static analysis). |
| synchronous_inspection.js package | library | Observed | Groups 1 file(s) under synchronous_inspection.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 97 file(s) under tests (observed from repository paths and static analysis). |
| thenables.js package | library | Observed | Groups 1 file(s) under thenables.js package (observed from repository paths and static analysis). |
| timers.js package | library | Observed | Groups 1 file(s) under timers.js package (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 11 file(s) under tools package (observed from repository paths and static analysis). |
| using.js package | library | Observed | Groups 1 file(s) under using.js package (observed from repository paths and static analysis). |
| util.js package | library | Observed | Groups 1 file(s) under util.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.istanbul.yml` (config)
- `.travis.yml` (ci)
- `benchmark/package.json` (manifest)
- `bower.json` (config)
- `docs/_config.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `docs` — 126 analysed file(s)
- `test` — 96 analysed file(s)
- `benchmark` — 79 analysed file(s)
- `src` — 38 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `tools` — 12 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (2 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c220cfe480868e2f5c5de4fe8bb3b04b97588d7f` is the revision these paths and observations refer to.
