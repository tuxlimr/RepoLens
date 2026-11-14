# Project structure: pinojs/pino

**Analysed commit:** `8d6927c29777882516339d9ccd509869ca3f295e`

**Commit reference:** [8d6927c29777882516339d9ccd509869ca3f295e](https://github.com/pinojs/pino/commit/8d6927c29777882516339d9ccd509869ca3f295e)

**Tree at this commit:** [pinojs/pino@8d6927c29777](https://github.com/pinojs/pino/tree/8d6927c29777882516339d9ccd509869ca3f295e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pinojs/pino |
| Description | 🌲 super fast, all natural json logger |
| Stars | 18301 |
| Forks | 1022 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `8d6927c29777882516339d9ccd509869ca3f295e` |
| Retrieved at | 2026-11-14T19:11:22.299723+00:00 |
| Files in this snapshot | 194 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (5 files)
    bench.yml
    ci.yml
    lock-threads.yml
    publish-release.yml
    target-main.yml
benchmarks/  (18 files)
  internal/  (5 files)
    custom-levels.js
    just-pino-heavy.bench.js
    just-pino.bench.js
    parent-vs-child.bench.js
    redact.bench.js
  utils/  (3 files)
    generate-benchmark-doc.js
    runbench.js
    wrap-log-level.js
  basic.bench.js
  child-child.bench.js
  child-creation.bench.js
  child.bench.js
  deep-object.bench.js
  formatters.bench.js
  long-string.bench.js
  multi-arg.bench.js
  multistream.js
  object.bench.js
docs/  (14 files)
  api.md
  asynchronous.md
  benchmarks.md
  browser.md
  bundling.md
  child-loggers.md
  diagnostics.md
  ecosystem.md
  help.md
  lts.md
  pretty.md
  redaction.md
  transports.md
  web.md
docsify/  (1 files)
  sidebar.md
examples/  (2 files)
  basic.js
  transport.js
lib/  (14 files)
  caller.js
  constants.js
  deprecations.js
  levels.js
  meta.js
  multistream.js
  proto.js
  redaction.js
  symbols.js
  time.js
  tools.js
  transport-stream.js
  transport.js
  worker.js
test/  (121 files)
  esm/  (3 files)
    esm.mjs
    index.test.js
    named-exports.mjs
  fixtures/  (49 files)
    broken-pipe/  (3 files)
      … 3 files under this directory
    eval/  (1 files)
      … 1 files under this directory
    pretty/  (1 files)
      … 1 files under this directory
    transport/  (2 files)
      … 2 files under this directory
    ts/  (10 files)
      … 10 files under this directory
    caller-loop.js
    console-transport.js
    crashing-transport.js
    default-exit.js
    destination-exit.js
    noop-transport.js
    stdout-hack-protection.js
    syncfalse-child.js
    syncfalse-exit.js
    syncfalse-flush-exit.js
    syncfalse.js
    syntax-error-esm.mjs
    to-file-transport-with-transform.js
    to-file-transport.js
    to-file-transport.mjs
    transport-exit-immediately-with-async-dest.js
    transport-exit-immediately.js
    transport-exit-on-ready.js
    transport-invalid-node-options.js
    transport-main.js
    transport-many-lines.js
    transport-preload-main.mjs
    transport-preload.mjs
    transport-string-stdout.js
    … 8 more files
  internals/  (1 files)
    version.test.js
  jest/  (1 files)
    basic.spec.js
  transport/  (16 files)
    big.test.js
    bundlers-support.test.js
    caller.test.js
    core.test.js
    core.transpiled.test.ts
    crash.test.js
    module-link.test.js
    native-type-stripping.test.mjs
    node-options.test.js
    pipeline.test.js
    preload.test.js
    repl.test.js
    sync-false.test.js
    sync-true.test.js
    targets.test.js
    uses-pino-config.test.js
  types/  (9 files)
    pino-import.tst.cts
    pino-import.tst.js
    pino-multistream.tst.ts
    pino-top-export.tst.ts
    pino-transport.tst.ts
    pino-type-only.tst.ts
    pino.ts
    pino.tst.ts
    tsconfig.json
  basic.test.js
  broken-pipe.test.js
  browser-bindings.test.js
  browser-child.test.js
  browser-disabled.test.js
  browser-early-console-freeze.test.js
  browser-is-level-enabled.test.js
  browser-levels.test.js
  browser-redaction.test.js
  browser-serializers.test.js
  browser-set-bindings.test.js
  browser-timestamp.test.js
  browser-transmit.test.js
  browser.test.js
  caller.test.js
  complex-objects.test.js
  crlf.test.js
  custom-levels.test.js
  diagnostics.test.js
  error-key.test.js
  error.test.js
  escaping.test.js
  exit.test.js
  formatters.test.js
  … 18 more files
.gitignore
.nojekyll
.npmignore
.prettierignore
CNAME
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
bin.js
browser.js
eslint.config.js
file.js
inc-version.sh
index.html
package.json
pino.d.ts
pino.js
tsconfig.json
```

## Entry points

- [pino.js](https://github.com/pinojs/pino/blob/8d6927c29777882516339d9ccd509869ca3f295e/pino.js)
- [bin.js](https://github.com/pinojs/pino/blob/8d6927c29777882516339d9ccd509869ca3f295e/bin.js)
- [test/fixtures/transport/index.js](https://github.com/pinojs/pino/blob/8d6927c29777882516339d9ccd509869ca3f295e/test/fixtures/transport/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 18 file(s) under benchmarks package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 14 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 121 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/bench.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/lock-threads.yml` (ci)
- `.github/workflows/publish-release.yml` (ci)
- `.github/workflows/target-main.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 121 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `benchmarks` — 18 analysed file(s)
- `docs` — 14 analysed file(s)
- `lib` — 14 analysed file(s)
- `.github` — 5 analysed file(s)
- `examples` — 2 analysed file(s)
- `docsify` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 18 file(s) were skipped during inventory (1 x likely secret file excluded; 17 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8d6927c29777882516339d9ccd509869ca3f295e` is the revision these paths and observations refer to.
