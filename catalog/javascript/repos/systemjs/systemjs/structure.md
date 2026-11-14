# Project structure: systemjs/systemjs

**Analysed commit:** `9647576d43294e938ddae8fe231beb62255f4e46`

**Commit reference:** [9647576d43294e938ddae8fe231beb62255f4e46](https://github.com/systemjs/systemjs/commit/9647576d43294e938ddae8fe231beb62255f4e46)

**Tree at this commit:** [systemjs/systemjs@9647576d4329](https://github.com/systemjs/systemjs/tree/9647576d43294e938ddae8fe231beb62255f4e46)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | systemjs/systemjs |
| Description | Dynamic ES module loader |
| Stars | 13083 |
| Forks | 1089 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `9647576d43294e938ddae8fe231beb62255f4e46` |
| Retrieved at | 2026-11-14T19:12:00.910353+00:00 |
| Files in this snapshot | 238 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.md
    feature-request.md
    question.md
  workflows/  (3 files)
    size-impact/  (1 files)
      … 1 files under this directory
    size-impact.yml
    test.yml
  FUNDING.yml
docs/  (7 files)
  api.md
  errors.md
  hooks.md
  import-maps.md
  module-types.md
  nodejs.md
  system-register.md
examples/  (1 files)
  README.md
src/  (23 files)
  extras/  (8 files)
    amd.js
    dynamic-import-maps.js
    global.js
    module-types.js
    named-exports.js
    named-register.js
    transform.js
    use-default.js
  features/  (8 files)
    depcache.js
    fetch-load.js
    import-maps.js
    node-fetch.js
    registry.js
    resolve.js
    script-load.js
    worker-load.js
  common.js
  err-msg.js
  package.json
  s.js
  system-core.js
  system-node.js
  system.js
test/  (192 files)
  browser/  (8 files)
    amd.js
    base-href.js
    core.js
    dynamic-import-maps.js
    named-exports.js
    named-register.js
    transform.js
    worker.js
  fixtures/  (176 files)
    browser/  (87 files)
      … 87 files under this directory
    css-modules/  (5 files)
      … 5 files under this directory
    es-modules/  (38 files)
      … 38 files under this directory
    register-modules/  (38 files)
      … 38 files under this directory
    tla/  (7 files)
      … 7 files under this directory
    url-resolution-cases.json
  import-map.mjs
  mocha-setup.js
  server.mjs
  system-core.mjs
  system-node.mjs
  test-base-href.html
  test.html
  url-resolution.mjs
.agignore
.gitignore
CHANGELOG.md
LICENSE
README.md
chompfile.toml
package.json
terser.js
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| common.js package | library | Observed | Groups 1 file(s) under common.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| err-msg.js package | library | Observed | Groups 1 file(s) under err-msg.js package (observed from repository paths and static analysis). |
| extras package | library | Observed | Groups 8 file(s) under extras package (observed from repository paths and static analysis). |
| features package | library | Observed | Groups 8 file(s) under features package (observed from repository paths and static analysis). |
| s.js package | library | Observed | Groups 1 file(s) under s.js package (observed from repository paths and static analysis). |
| system-core.js package | library | Observed | Groups 1 file(s) under system-core.js package (observed from repository paths and static analysis). |
| system.js package | library | Observed | Groups 1 file(s) under system.js package (observed from repository paths and static analysis). |
| system-node.js package | library | Observed | Groups 1 file(s) under system-node.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 192 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/size-impact.yml` (ci)
- `.github/workflows/size-impact/report-size-impact.mjs` (ci)
- `.github/workflows/test.yml` (ci)
- `chompfile.toml` (config)
- `package.json` (manifest)
- `src/package.json` (manifest)

## Top-level layout

- `test` — 192 analysed file(s)
- `src` — 23 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 7 analysed file(s)
- `docs` — 7 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 10 file(s) were skipped during inventory (10 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9647576d43294e938ddae8fe231beb62255f4e46` is the revision these paths and observations refer to.
