# Project structure: js-cookie/js-cookie

**Analysed commit:** `e9a4b83402a9d09065831f0e02820478a569253e`

**Commit reference:** [e9a4b83402a9d09065831f0e02820478a569253e](https://github.com/js-cookie/js-cookie/commit/e9a4b83402a9d09065831f0e02820478a569253e)

**Tree at this commit:** [js-cookie/js-cookie@e9a4b83402a9](https://github.com/js-cookie/js-cookie/tree/e9a4b83402a9d09065831f0e02820478a569253e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | js-cookie/js-cookie |
| Description | A simple, lightweight JavaScript API for handling cookies, client-side. |
| Stars | 22562 |
| Forks | 2042 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `e9a4b83402a9d09065831f0e02820478a569253e` |
| Retrieved at | 2026-11-14T19:11:07.852972+00:00 |
| Files in this snapshot | 47 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (4 files)
    ci.yml
    release.yml
    stale-bot.yml
    zizmor.yml
  dependabot.yml
.vscode/  (1 files)
  extensions.json
examples/  (6 files)
  es-module/  (2 files)
    src/  (1 files)
      … 1 files under this directory
    package.json
  webpack/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    package.json
    server.js
src/  (3 files)
  api.mjs
  assign.mjs
  converter.mjs
test/  (12 files)
  browserstack/  (1 files)
    runner.js
  sub/  (2 files)
    index.html
    tests.js
  encoding.html
  encoding.js
  index.html
  missing_semicolon.html
  module.html
  module.mjs
  node.js
  tests.js
  utils.js
.gitignore
.nano-staged.mjs
.prettierignore
.release-it.json
.simple-git-hooks.json
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Gruntfile.js
LICENSE
README.md
SECURITY.md
SERVER_SIDE.md
browserstack.yml
eslint.config.mjs
index.js
package.json
prettier.config.mjs
rollup.config.mjs
```

## Entry points

- [index.js](https://github.com/js-cookie/js-cookie/blob/e9a4b83402a9d09065831f0e02820478a569253e/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| api.mjs package | library | Observed | Groups 1 file(s) under api.mjs package (observed from repository paths and static analysis). |
| assign.mjs package | library | Observed | Groups 1 file(s) under assign.mjs package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| converter.mjs package | library | Observed | Groups 1 file(s) under converter.mjs package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/stale-bot.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.release-it.json` (config)
- `.simple-git-hooks.json` (config)
- `.vscode/extensions.json` (config)
- `browserstack.yml` (config)
- `examples/es-module/package.json` (manifest)
- `examples/webpack/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 18 analysed file(s)
- `test` — 12 analysed file(s)
- `.github` — 7 analysed file(s)
- `examples` — 6 analysed file(s)
- `src` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e9a4b83402a9d09065831f0e02820478a569253e` is the revision these paths and observations refer to.
