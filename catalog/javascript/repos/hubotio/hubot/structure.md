# Project structure: hubotio/hubot

**Analysed commit:** `1e66cb44b0b7fcea686f0018d2d3fb41cd1194ca`

**Commit reference:** [1e66cb44b0b7fcea686f0018d2d3fb41cd1194ca](https://github.com/hubotio/hubot/commit/1e66cb44b0b7fcea686f0018d2d3fb41cd1194ca)

**Tree at this commit:** [hubotio/hubot@1e66cb44b0b7](https://github.com/hubotio/hubot/tree/1e66cb44b0b7fcea686f0018d2d3fb41cd1194ca)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hubotio/hubot |
| Description | A customizable life embetterment robot. |
| Stars | 16796 |
| Forks | 3706 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `1e66cb44b0b7fcea686f0018d2d3fb41cd1194ca` |
| Retrieved at | 2026-11-14T19:11:30.454295+00:00 |
| Files in this snapshot | 101 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (5 files)
    nodejs-macos.yml
    nodejs-ubuntu.yml
    nodejs-windows.yml
    pipeline.yml
    sfab-gh-pages.yml
  stale.yml
bin/  (3 files)
  Hubot.mjs
  e2e-test.sh
  hubot
configuration/  (1 files)
  Config.mjs
docs/  (29 files)
  adapters/  (3 files)
    campfire.md
    development.md
    shell.md
  assets/  (12 files)
    fonts/  (10 files)
      … 10 files under this directory
    images/  (1 files)
      … 1 files under this directory
    stylesheets/  (1 files)
      … 1 files under this directory
  deploying/  (4 files)
    azure.md
    bluemix.md
    unix.md
    windows.md
  designs/  (1 files)
    commands.md
  layouts/  (2 files)
    docs.html
    main.html
  adapters.md
  deploying.md
  docs.md
  implementation.md
  index.html
  patterns.md
  scripting.md
examples/  (2 files)
  hubot-start.ps1
  hubot.service
script/  (6 files)
  bootstrap
  release
  server
  simple-lint.mjs
  smoke-test
  test
sfab-hooks/  (1 files)
  SfabHook.mjs
src/  (16 files)
  adapters/  (2 files)
    Campfire.mjs
    Shell.mjs
  datastores/  (1 files)
    Memory.mjs
  Adapter.mjs
  Brain.mjs
  CommandBus.mjs
  DataStore.mjs
  GenHubot.mjs
  HttpClient.mjs
  Listener.mjs
  Message.mjs
  Middleware.mjs
  OptParse.mjs
  Response.mjs
  Robot.mjs
  User.mjs
test/  (28 files)
  doubles/  (1 files)
    DummyAdapter.mjs
  fixtures/  (6 files)
    MockAdapter.mjs
    TestScript.js
    TestScript.mjs
    TestScript.ts
    TestScriptIncorrectApi.js
    TestScriptIncorrectApi.mjs
  ordered-scripts/  (3 files)
    01-PFirst.mjs
    02-SetupBotConfig.mjs
    WebSetup.mjs
  scripts/  (1 files)
    Xample.mjs
  AdapterName_test.mjs
  Adapter_test.mjs
  Brain_test.mjs
  CommandBus_test.mjs
  Configuration_test.mjs
  DataStore_test.mjs
  GenHubot_test.mjs
  Hubot_test.mjs
  Listener_test.mjs
  Message_test.mjs
  Middleware_test.mjs
  OptParse-test.mjs
  Robot_test.mjs
  Shell_test.mjs
  User_test.mjs
  XampleTest.mjs
  index_test.mjs
.editorconfig
.gitignore
.npmignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
README.md
index.mjs
package.json
```

## Entry points

- [index.mjs](https://github.com/hubotio/hubot/blob/1e66cb44b0b7fcea686f0018d2d3fb41cd1194ca/index.mjs)
- [bin/hubot](https://github.com/hubotio/hubot/blob/1e66cb44b0b7fcea686f0018d2d3fb41cd1194ca/bin/hubot)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Adapter.mjs package | library | Observed | Groups 1 file(s) under adapter.mjs package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| Brain.mjs package | library | Observed | Groups 1 file(s) under brain.mjs package (observed from repository paths and static analysis). |
| CommandBus.mjs package | library | Observed | Groups 1 file(s) under commandbus.mjs package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| configuration package | library | Observed | Groups 1 file(s) under configuration package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| DataStore.mjs package | library | Observed | Groups 1 file(s) under datastore.mjs package (observed from repository paths and static analysis). |
| datastores package | library | Observed | Groups 1 file(s) under datastores package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). |
| GenHubot.mjs package | library | Observed | Groups 1 file(s) under genhubot.mjs package (observed from repository paths and static analysis). |
| HttpClient.mjs package | library | Observed | Groups 1 file(s) under httpclient.mjs package (observed from repository paths and static analysis). |
| Listener.mjs package | library | Observed | Groups 1 file(s) under listener.mjs package (observed from repository paths and static analysis). |
| Message.mjs package | library | Observed | Groups 1 file(s) under message.mjs package (observed from repository paths and static analysis). |
| Middleware.mjs package | library | Observed | Groups 1 file(s) under middleware.mjs package (observed from repository paths and static analysis). |
| OptParse.mjs package | library | Observed | Groups 1 file(s) under optparse.mjs package (observed from repository paths and static analysis). |
| Response.mjs package | library | Observed | Groups 1 file(s) under response.mjs package (observed from repository paths and static analysis). |
| Robot.mjs package | library | Observed | Groups 1 file(s) under robot.mjs package (observed from repository paths and static analysis). |
| script package | library | Observed | Groups 1 file(s) under script package (observed from repository paths and static analysis). |
| sfab-hooks package | library | Observed | Groups 1 file(s) under sfab-hooks package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 29 file(s) under tests (observed from repository paths and static analysis). |
| User.mjs package | library | Observed | Groups 1 file(s) under user.mjs package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/stale.yml` (config)
- `.github/workflows/nodejs-macos.yml` (ci)
- `.github/workflows/nodejs-ubuntu.yml` (ci)
- `.github/workflows/nodejs-windows.yml` (ci)
- `.github/workflows/pipeline.yml` (ci)
- `.github/workflows/sfab-gh-pages.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `docs` — 29 analysed file(s)
- `test` — 28 analysed file(s)
- `src` — 16 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 6 analysed file(s)
- `script` — 6 analysed file(s)
- `bin` — 3 analysed file(s)
- `examples` — 2 analysed file(s)
- `configuration` — 1 analysed file(s)
- `sfab-hooks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1e66cb44b0b7fcea686f0018d2d3fb41cd1194ca` is the revision these paths and observations refer to.
