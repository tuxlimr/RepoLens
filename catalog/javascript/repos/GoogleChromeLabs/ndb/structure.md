# Project structure: GoogleChromeLabs/ndb

**Analysed commit:** `ade2052ad27f3c90cfd97c6aa87465c179572f8a`

**Commit reference:** [ade2052ad27f3c90cfd97c6aa87465c179572f8a](https://github.com/GoogleChromeLabs/ndb/commit/ade2052ad27f3c90cfd97c6aa87465c179572f8a)

**Tree at this commit:** [GoogleChromeLabs/ndb@ade2052ad27f](https://github.com/GoogleChromeLabs/ndb/tree/ade2052ad27f3c90cfd97c6aa87465c179572f8a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | GoogleChromeLabs/ndb |
| Description | ndb is an improved debugging experience for Node.js, enabled by Chrome DevTools |
| Stars | 10857 |
| Forks | 241 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ade2052ad27f3c90cfd97c6aa87465c179572f8a` |
| Retrieved at | 2026-11-14T19:12:30.241401+00:00 |
| Files in this snapshot | 61 |

## Directory tree

```text
docs/  (1 files)
  issue_template.md
front_end/  (18 files)
  ndb/  (5 files)
    Connection.js
    FileSystem.js
    InspectorFrontendHostOverrides.js
    NdbMain.js
    module.json
  ndb_sdk/  (3 files)
    NodeRuntime.js
    NodeWorker.js
    module.json
  ndb_ui/  (6 files)
    NodeProcesses.js
    RunConfiguration.js
    Terminal.js
    module.json
    nodeProcesses.css
    runConfiguration.css
  xterm/  (1 files)
    module.json
  ndb.html
  ndb.js
  ndb.json
lib/  (5 files)
  preload/  (1 files)
    ndb/  (1 files)
      … 1 files under this directory
  backend.js
  filepath_to_url.js
  launcher.js
  process_utility.js
scripts/  (1 files)
  builder.js
services/  (5 files)
  file_system.js
  file_system_io.js
  ndd_service.js
  search.js
  terminal.js
test/  (6 files)
  assets/  (3 files)
    test-project/  (3 files)
      … 3 files under this directory
  basic.spec.js
  integration.js
  platform.spec.js
utils/  (11 files)
  testrunner/  (11 files)
    examples/  (5 files)
      … 5 files under this directory
    Matchers.js
    Multimap.js
    README.md
    Reporter.js
    TestRunner.js
    index.js
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.npmignore
.travis.yml
CONTRIBUTING.md
LICENSE
README.md
build.js
debug.js
ndb.js
package.json
version.js
```

## Entry points

- [ndb.js](https://github.com/GoogleChromeLabs/ndb/blob/ade2052ad27f3c90cfd97c6aa87465c179572f8a/ndb.js)
- [test/assets/test-project/index.js](https://github.com/GoogleChromeLabs/ndb/blob/ade2052ad27f3c90cfd97c6aa87465c179572f8a/test/assets/test-project/index.js)
- [utils/testrunner/index.js](https://github.com/GoogleChromeLabs/ndb/blob/ade2052ad27f3c90cfd97c6aa87465c179572f8a/utils/testrunner/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| front_end package | library | Observed | Groups 10 file(s) under front_end package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 5 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 10 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `front_end/ndb.json` (config)
- `front_end/ndb/module.json` (config)
- `front_end/ndb_sdk/module.json` (config)
- `front_end/ndb_ui/module.json` (config)
- `front_end/xterm/module.json` (config)
- `package.json` (manifest)

## Top-level layout

- `front_end` — 18 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `utils` — 11 analysed file(s)
- `test` — 6 analysed file(s)
- `lib` — 5 analysed file(s)
- `services` — 5 analysed file(s)
- `docs` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `ade2052ad27f3c90cfd97c6aa87465c179572f8a` is the revision these paths and observations refer to.
