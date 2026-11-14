# Project structure: mochajs/mocha

**Analysed commit:** `5b5afa7b12e3f76f4e0c6afa12e960c0b378358c`

**Commit reference:** [5b5afa7b12e3f76f4e0c6afa12e960c0b378358c](https://github.com/mochajs/mocha/commit/5b5afa7b12e3f76f4e0c6afa12e960c0b378358c)

**Tree at this commit:** [mochajs/mocha@5b5afa7b12e3](https://github.com/mochajs/mocha/tree/5b5afa7b12e3f76f4e0c6afa12e960c0b378358c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mochajs/mocha |
| Description | ☕️ Classic, reliable, trusted test framework for Node.js and the browser |
| Stars | 22912 |
| Forks | 3147 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `5b5afa7b12e3f76f4e0c6afa12e960c0b378358c` |
| Retrieved at | 2026-11-14T19:11:06.109220+00:00 |
| Files in this snapshot | 673 |

## Directory tree

```text
.github/  (32 files)
  ISSUE_TEMPLATE/  (6 files)
    01-bug.yml
    02-documentation.yml
    03-feature-request.yml
    04-performance.yml
    05-repository-tooling.yml
    config.yml
  release-please/  (2 files)
    config.json
    manifest.json
  workflows/  (17 files)
    add-to-project.yml
    auto-label.yml
    blocked-pr.yml
    cla.yml
    docs.yml
    format.yml
    mocha.yml
    nightly-site-deploy.yml
    npm-script.yml
    octoguide.yml
    protect-manifest.yml
    release-comment.yml
    release-please.yml
    remove-waiting-label.yml
    slop-detection.yml
    stale-branches.yml
    stale.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  DEVELOPMENT.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  copilot-instructions.md
  dependabot.yml
bin/  (1 files)
  mocha.js
docs/  (101 files)
  _data/  (2 files)
    blocklist.json
    supporters.cjs
  public/  (3 files)
    example/  (2 files)
      … 2 files under this directory
    favicon.svg
  src/  (87 files)
    components/  (14 files)
      … 14 files under this directory
    content/  (70 files)
      … 70 files under this directory
    style/  (1 files)
      … 1 files under this directory
    content.config.ts
    env.d.ts
  .gitignore
  .knip.jsonc
  .prettierrc.json
  README.md
  _redirects
  astro.config.ts
  netlify.toml
  package.json
  tsconfig.json
example/  (5 files)
  config/  (5 files)
    .mocharc.cjs
    .mocharc.json
    .mocharc.jsonc
    .mocharc.yml
    README.md
lib/  (66 files)
  browser/  (3 files)
    highlight-tags.js
    parse-query.js
    template.html
  cli/  (16 files)
    cli.js
    collect-files.cjs
    commands.js
    config.cjs
    index.cjs
    init.js
    lookup-files.js
    node-flags.cjs
    one-and-dones.js
    options.cjs
    parse-args.js
    run-helpers.cjs
    run-option-metadata.cjs
    run.cjs
    unparse-args.js
    watch-run.cjs
  interfaces/  (6 files)
    bdd.js
    common.js
    exports.js
    index.js
    qunit.js
    tdd.js
  nodejs/  (8 files)
    reporters/  (1 files)
      … 1 files under this directory
    buffered-worker-pool.js
    esm-utils.cjs
    file-unloader.js
    parallel-buffered-runner.js
    serializer.js
    worker-core.js
    worker.js
  reporters/  (17 files)
    base.js
    doc.js
    dot.js
    github-actions.js
    html.js
    index.cjs
    json-stream.js
    json.js
    landing.js
    list.js
    markdown.js
    min.js
    nyan.js
    progress.js
    spec.js
    tap.js
    xunit.js
  utils/  (1 files)
    regexp.js
  context.js
  error-constants.js
  errors.js
  hook.js
  mocha.cjs
  mocharc.json
  pending.js
  plugin-loader.js
  runnable.js
  runner.js
  stats-collector.js
  suite.js
  test.js
  types.d.ts
  utils.cjs
repro/  (5 files)
  test/  (1 files)
    hello.spec.js
  .gitignore
  .mocharc.yml
  README.md
  package.json
scripts/  (4 files)
  linkify-changelog.js
  merge-coverage.js
  pick-from-package-json.js
  update-authors.cjs
test/  (430 files)
  browser/  (4 files)
    config.js
    global-setup.js
    run.spec.js
    server.js
  browser-specific/  (5 files)
    fixtures/  (3 files)
      … 3 files under this directory
    esm.spec.js
    setup.cjs
  compiler/  (2 files)
    test.coffee
    test.foo
  compiler-cjs/  (4 files)
    test.js
    test.js.compiled
    test.ts
    test.ts.compiled
  compiler-esm/  (13 files)
    package.json
    test-tla.js
    test-tla.js.compiled
    test-tla.mjs
    test-tla.mjs.compiled
    test-tla.ts
    test-tla.ts.compiled
    test.js
    test.js.compiled
    test.mjs
    test.mjs.compiled
    test.ts
    test.ts.compiled
  compiler-fixtures/  (9 files)
    esm-only-loader/  (4 files)
      … 4 files under this directory
    esm-loader.fixture.js
    esm.fixture.cjs
    foo.fixture.cjs
    js.fixture.cjs
    ts.fixture.cjs
  integration/  (304 files)
    fixtures/  (236 files)
      … 236 files under this directory
    options/  (29 files)
      … 29 files under this directory
    plugins/  (2 files)
      … 2 files under this directory
    README.md
    color.spec.cjs
    common-js-require.spec.cjs
    compiler-cjs.spec.cjs
    compiler-esm-only-loader.spec.cjs
    compiler-esm.spec.cjs
    compiler-globbing.spec.cjs
    config.spec.cjs
    constants.js
    diffs.spec.cjs
    duplicate-arguments.spec.cjs
    esm.spec.cjs
    events.spec.cjs
    fifo.spec.cjs
    file-utils.spec.cjs
    glob.spec.cjs
    global-variable.spec.cjs
    help.spec.js
    helpers.cjs
    hook-err.spec.cjs
    hooks.spec.cjs
    init.spec.cjs
    invalid-arguments.spec.cjs
    multiple-done.spec.cjs
    … 13 more files
  interfaces/  (4 files)
    bdd.spec.js
    exports.spec.cjs
    qunit.spec.js
    tdd.spec.js
  jsapi/  (1 files)
    index.js
  node-unit/  (30 files)
    cli/  (11 files)
      … 11 files under this directory
    fixtures/  (9 files)
      … 9 files under this directory
    reporters/  (1 files)
      … 1 files under this directory
    buffered-worker-pool.spec.cjs
    esm-utils.spec.cjs
    merge-coverage.spec.cjs
    mocha.spec.cjs
    parallel-buffered-runner.spec.cjs
    serializer.spec.cjs
    stack-trace-filter.spec.cjs
    utils.spec.cjs
    worker.spec.cjs
  only/  (4 files)
    global/  (3 files)
      … 3 files under this directory
    bdd-require.spec.cjs
  reporters/  (16 files)
    base.spec.cjs
    doc.spec.cjs
    dot.spec.cjs
    github-actions.spec.cjs
    helpers.cjs
    json-stream.spec.cjs
    json.spec.js
    landing.spec.cjs
    list.spec.cjs
    markdown.spec.cjs
    min.spec.cjs
    nyan.spec.cjs
    progress.spec.cjs
    spec.spec.cjs
    tap.spec.cjs
    xunit.spec.cjs
  require/  (5 files)
    a.cjs
    b.coffee
    c.cjs
    d.coffee
    require.spec.cjs
  smoke/  (1 files)
    smoke.spec.cjs
  unit/  (25 files)
    interfaces/  (1 files)
      … 1 files under this directory
    reporters/  (1 files)
      … 1 files under this directory
    context.spec.cjs
    duration.spec.cjs
    errors.spec.cjs
    globals.spec.cjs
    grep.spec.cjs
    hook-async.spec.cjs
    hook-sync-nested.spec.cjs
    hook-sync.spec.cjs
    hook-timeout.spec.cjs
    hook.spec.cjs
    mocha.spec.cjs
    overspecified-async.spec.cjs
    parse-query.spec.cjs
    plugin-loader.spec.cjs
    required-tokens.spec.cjs
    root.spec.cjs
    runnable.spec.cjs
    runner.spec.cjs
    suite.spec.cjs
    test.spec.cjs
    throw.spec.cjs
    timeout.spec.cjs
    utils.spec.cjs
  README.md
  assertions.cjs
  setup.cjs
.browserslistrc
.gitattributes
.gitignore
.knip.jsonc
.mailmap
.mocharc.yml
.nycrc
.prettierignore
.wallaby.cjs
AGENTS.md
AUTHORS
CHANGELOG.md
FUNDING.md
LICENSE
MAINTAINERS.md
PROJECT_CHARTER.md
README.md
SECURITY.md
browser-entry.js
eslint.config.cjs
index.js
mocha.css
mocha.mjs
netlify.toml
… 5 more files
```

## Entry points

- [index.js](https://github.com/mochajs/mocha/blob/5b5afa7b12e3f76f4e0c6afa12e960c0b378358c/index.js)
- [bin/mocha.js](https://github.com/mochajs/mocha/blob/5b5afa7b12e3f76f4e0c6afa12e960c0b378358c/bin/mocha.js)
- [test/integration/fixtures/config/mocha-config/index.js](https://github.com/mochajs/mocha/blob/5b5afa7b12e3f76f4e0c6afa12e960c0b378358c/test/integration/fixtures/config/mocha-config/index.js)
- [lib/interfaces/index.js](https://github.com/mochajs/mocha/blob/5b5afa7b12e3f76f4e0c6afa12e960c0b378358c/lib/interfaces/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 64 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 431 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/01-bug.yml` (config)
- `.github/ISSUE_TEMPLATE/02-documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/03-feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/04-performance.yml` (config)
- `.github/ISSUE_TEMPLATE/05-repository-tooling.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/release-please/config.json` (config)
- `.github/release-please/manifest.json` (config)
- `.github/workflows/add-to-project.yml` (ci)
- `.github/workflows/auto-label.yml` (ci)
- `.github/workflows/blocked-pr.yml` (ci)
- `.github/workflows/cla.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/format.yml` (ci)
- `.github/workflows/mocha.yml` (ci)
- `.github/workflows/nightly-site-deploy.yml` (ci)
- `.github/workflows/npm-script.yml` (ci)
- `.github/workflows/octoguide.yml` (ci)
- `.github/workflows/protect-manifest.yml` (ci)
- `.github/workflows/release-comment.yml` (ci)
- `.github/workflows/release-please.yml` (ci)
- `.github/workflows/remove-waiting-label.yml` (ci)
- `.github/workflows/slop-detection.yml` (ci)
- `.github/workflows/stale-branches.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.mocharc.yml` (config)
- `docs/.prettierrc.json` (config)
- `docs/_data/blocklist.json` (config)
- `docs/netlify.toml` (config)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `example/config/.mocharc.json` (config)
- `example/config/.mocharc.yml` (config)
- `lib/mocharc.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `renovate.json` (config)
- `repro/.mocharc.yml` (config)
- `repro/package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 430 analysed file(s)
- `docs` — 101 analysed file(s)
- `lib` — 66 analysed file(s)
- `.github` — 32 analysed file(s)
- `(root files)` — 29 analysed file(s)
- `example` — 5 analysed file(s)
- `repro` — 5 analysed file(s)
- `scripts` — 4 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5b5afa7b12e3f76f4e0c6afa12e960c0b378358c` is the revision these paths and observations refer to.
