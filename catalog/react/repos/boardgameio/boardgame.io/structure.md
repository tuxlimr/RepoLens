# Project structure: boardgameio/boardgame.io

**Analysed commit:** `47adef2b46e375999931209ba7b41e9654c506e1`

**Commit reference:** [47adef2b46e375999931209ba7b41e9654c506e1](https://github.com/boardgameio/boardgame.io/commit/47adef2b46e375999931209ba7b41e9654c506e1)

**Tree at this commit:** [boardgameio/boardgame.io@47adef2b46e3](https://github.com/boardgameio/boardgame.io/tree/47adef2b46e375999931209ba7b41e9654c506e1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | boardgameio/boardgame.io |
| Description | State Management and Multiplayer Networking for Turn-Based Games |
| Stars | 12491 |
| Forks | 833 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `47adef2b46e375999931209ba7b41e9654c506e1` |
| Retrieved at | 2026-11-14T19:13:20.470476+00:00 |
| Files in this snapshot | 343 |

## Directory tree

```text
.devcontainer/  (2 files)
  Dockerfile
  devcontainer.json
.github/  (5 files)
  workflows/  (2 files)
    ci.yml
    npm-publish.yml
  FUNDING.yml
  dependabot.yml
  pull_request_template.md
.husky/  (2 files)
  pre-commit
  pre-push
benchmark/  (1 files)
  index.js
docs/  (43 files)
  documentation/  (38 files)
    api/  (4 files)
      … 4 files under this directory
    snippets/  (10 files)
      … 10 files under this directory
    .nojekyll
    CHANGELOG.md
    chat.md
    concepts.md
    debugging.md
    deployment.md
    events.md
    immutability.md
    index.html
    multiplayer.md
    notable_projects.md
    phases.md
    plugins.md
    random.md
    secret-state.md
    sidebar.md
    stages.md
    storage.md
    testing.md
    theme.css
    turn-order.md
    tutorial.md
    typescript.md
    undo.md
  CNAME
  index.css
  index.html
  logo-optimized.svg
  logo.svg
examples/  (102 files)
  react-native/  (9 files)
    .gitignore
    .watchmanconfig
    App.js
    README.md
    app.json
    board.js
    game.js
    package.json
    rn-cli.config.js
  react-web/  (66 files)
    src/  (63 files)
      … 63 files under this directory
    .gitignore
    package.json
    server.js
  snippets/  (27 files)
    src/  (23 files)
      … 23 files under this directory
    .gitignore
    README.md
    install.sh
    package.json
integration/  (17 files)
  node-smoke/  (2 files)
    cjs-test.cjs
    esm-test.mjs
  src/  (8 files)
    App.css
    App.jsx
    App.test.jsx
    board.css
    board.jsx
    game.js
    index.css
    index.jsx
  type-tests/  (2 files)
    server-custom-plugin.ts
    tsconfig.json
  .gitignore
  README.md
  index.html
  package.json
  vite.config.js
packages/  (13 files)
  ai.ts
  client.ts
  core.ts
  debug.ts
  internal.ts
  main.js
  master.ts
  multiplayer.ts
  plugins.ts
  react-native.ts
  react.ts
  server.ts
  testing.ts
python/  (4 files)
  examples/  (1 files)
    tic-tac-toe/  (1 files)
      … 1 files under this directory
  .gitignore
  boardgameio.py
  test_boardgameio.py
scripts/  (7 files)
  changelog.js
  clean.js
  dev-client.js
  install-examples.js
  integration.js
  proxy-dirs.js
  rollup-filesize.js
src/  (125 files)
  ai/  (5 files)
    ai.test.ts
    ai.ts
    bot.ts
    mcts-bot.ts
    random-bot.ts
  client/  (42 files)
    debug/  (27 files)
      … 27 files under this directory
    transport/  (7 files)
      … 7 files under this directory
    client.test.ts
    client.ts
    manager.ts
    react-native.js
    react-native.test.js
    react.ssr.test.tsx
    react.test.tsx
    react.tsx
  core/  (19 files)
    action-creators.ts
    action-types.ts
    backwards-compatibility.ts
    constants.ts
    errors.ts
    flow.test.ts
    flow.ts
    game-methods.ts
    game.test.ts
    game.ts
    initialize.ts
    logger.test.js
    logger.ts
    player-view.test.ts
    player-view.ts
    reducer.test.ts
    reducer.ts
    turn-order.test.ts
    turn-order.ts
  lobby/  (10 files)
    client.test.ts
    client.ts
    connection.test.ts
    connection.ts
    create-match-form.tsx
    login-form.tsx
    match-instance.tsx
    react.ssr.test.tsx
    react.test.tsx
    react.tsx
  master/  (4 files)
    filter-player-view.test.ts
    filter-player-view.ts
    master.test.ts
    master.ts
  plugins/  (17 files)
    events/  (2 files)
      … 2 files under this directory
    random/  (3 files)
      … 3 files under this directory
    main.test.ts
    main.ts
    plugin-events.ts
    plugin-immer.test.ts
    plugin-immer.ts
    plugin-log.test.ts
    plugin-log.ts
    plugin-player.test.ts
    plugin-player.ts
    plugin-random.ts
    plugin-serializable.test.ts
    plugin-serializable.ts
  server/  (25 files)
    db/  (9 files)
      … 9 files under this directory
    transport/  (7 files)
      … 7 files under this directory
    api.test.ts
    api.ts
    auth.test.ts
    auth.ts
    cors.test.ts
    cors.ts
    index.test.ts
    index.ts
    util.ts
  testing/  (2 files)
    mock-random.test.ts
    mock-random.ts
  types.ts
.empty_module.js
.gitignore
.lintstagedrc
.prettierignore
.prettierrc
AGENTS.md
AUTHORS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
babel.config.js
babel.config.test.js
eslint.config.js
jest-svelte-transformer.cjs
jest.setup.js
package.json
pnpm-workspace.yaml
roadmap.md
rollup.config.js
subpackages.js
tsconfig.json
```

## Entry points

- [benchmark/index.js](https://github.com/boardgameio/boardgame.io/blob/47adef2b46e375999931209ba7b41e9654c506e1/benchmark/index.js)
- [integration/src/App.jsx](https://github.com/boardgameio/boardgame.io/blob/47adef2b46e375999931209ba7b41e9654c506e1/integration/src/App.jsx)
- [integration/src/index.jsx](https://github.com/boardgameio/boardgame.io/blob/47adef2b46e375999931209ba7b41e9654c506e1/integration/src/index.jsx)
- [packages/main.js](https://github.com/boardgameio/boardgame.io/blob/47adef2b46e375999931209ba7b41e9654c506e1/packages/main.js)
- [packages/server.ts](https://github.com/boardgameio/boardgame.io/blob/47adef2b46e375999931209ba7b41e9654c506e1/packages/server.ts)
- [src/plugins/main.ts](https://github.com/boardgameio/boardgame.io/blob/47adef2b46e375999931209ba7b41e9654c506e1/src/plugins/main.ts)
- [src/server/db/index.ts](https://github.com/boardgameio/boardgame.io/blob/47adef2b46e375999931209ba7b41e9654c506e1/src/server/db/index.ts)
- [src/server/index.ts](https://github.com/boardgameio/boardgame.io/blob/47adef2b46e375999931209ba7b41e9654c506e1/src/server/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ai package | library | Observed | Groups 5 file(s) under ai package (observed from repository paths and static analysis). |
| benchmark package | library | Observed | Groups 1 file(s) under benchmark package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 9 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: TicTacToeBot. Observed top-level functions: main, stop. |
| External integrations | external | Observed | Groups 49 file(s) under external integrations (observed from repository paths and static analysis). |
| lobby package | library | Observed | Groups 10 file(s) under lobby package (observed from repository paths and static analysis). |
| master package | library | Observed | Groups 4 file(s) under master package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 13 file(s) under packages package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 17 file(s) under plugins package (observed from repository paths and static analysis). |
| python package | library | Observed | Groups 1 file(s) under python package (observed from repository paths and static analysis). Observed top-level classes: Bot, Namespace. |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 16 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 19 file(s) under service / domain layer (observed from repository paths and static analysis). |
| testing package | library | Observed | Groups 2 file(s) under testing package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestBot, TestNamespace. |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/npm-publish.yml` (ci)
- `examples/react-native/app.json` (config)
- `examples/react-native/package.json` (manifest)
- `examples/react-web/package.json` (manifest)
- `examples/snippets/package.json` (manifest)
- `integration/package.json` (manifest)
- `integration/type-tests/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 125 analysed file(s)
- `examples` — 102 analysed file(s)
- `docs` — 43 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `integration` — 17 analysed file(s)
- `packages` — 13 analysed file(s)
- `scripts` — 7 analysed file(s)
- `.github` — 5 analysed file(s)
- `python` — 4 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)
- `benchmark` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `47adef2b46e375999931209ba7b41e9654c506e1` is the revision these paths and observations refer to.
