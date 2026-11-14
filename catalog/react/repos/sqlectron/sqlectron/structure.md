# Project structure: sqlectron/sqlectron

**Analysed commit:** `b0f5e24015bca7974fbce6ab5e4ada69d51b48b3`

**Commit reference:** [b0f5e24015bca7974fbce6ab5e4ada69d51b48b3](https://github.com/sqlectron/sqlectron/commit/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3)

**Tree at this commit:** [sqlectron/sqlectron@b0f5e24015bc](https://github.com/sqlectron/sqlectron/tree/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sqlectron/sqlectron |
| Description | A simple and lightweight SQL client desktop with cross database and platform support. |
| Stars | 4757 |
| Forks | 524 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `b0f5e24015bca7974fbce6ab5e4ada69d51b48b3` |
| Retrieved at | 2026-11-14T19:14:36.538838+00:00 |
| Files in this snapshot | 187 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    publish.yml
    test.yml
.husky/  (2 files)
  .gitignore
  pre-commit
.storybook/  (2 files)
  main.js
  preview.js
docs/  (9 files)
  app/  (3 files)
    configuration-file.md
    keyboard-shortcuts.md
    logging.md
  development/  (6 files)
    README.md
    build-instructions.md
    docker-databases.md
    release.md
    run-from-source.md
    test-core-changes.md
scripts/  (3 files)
  dev-auto-restart.js
  link-sqlectron-db-core.sh
  start-test-integration-deps.sh
src/  (127 files)
  browser/  (22 files)
    core/  (9 files)
      … 9 files under this directory
    menu/  (4 files)
      … 4 files under this directory
    app.ts
    browser.ts
    config.ts
    ipcMain.ts
    logger.ts
    main.ts
    preload.ts
    update-checker.ts
    window.ts
  common/  (8 files)
    types/  (5 files)
      … 5 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    event.ts
  renderer/  (96 files)
    actions/  (13 files)
      … 13 files under this directory
    assets/  (7 files)
      … 7 files under this directory
    components/  (39 files)
      … 39 files under this directory
    containers/  (6 files)
      … 6 files under this directory
    hooks/  (4 files)
      … 4 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    reducers/  (15 files)
      … 15 files under this directory
    store/  (1 files)
      … 1 files under this directory
    utils/  (6 files)
      … 6 files under this directory
    api.ts
    entry.tsx
    index.html
    tailwind.css
  index.d.ts
stories/  (1 files)
  components/  (1 files)
    checkbox.stories.tsx
test/  (18 files)
  browser/  (5 files)
    validators/  (1 files)
      … 1 files under this directory
    config.test.ts
    servers.test.ts
    utils-stub.ts
    utils.test.ts
  common/  (1 files)
    utils/  (1 files)
      … 1 files under this directory
  e2e/  (4 files)
    helper.ts
    mainWindow.test.ts
    sqlite.test.ts
    ssh-mysql.test.ts
  fixtures/  (5 files)
    browser/  (2 files)
      … 2 files under this directory
    simple/  (1 files)
      … 1 files under this directory
    sqlite/  (1 files)
      … 1 files under this directory
    ssh-mysql/  (1 files)
      … 1 files under this directory
  renderer/  (2 files)
    components/  (1 files)
      … 1 files under this directory
    utils/  (1 files)
      … 1 files under this directory
  vitest.setup.ts
.dockerignore
.editorconfig
.gitattributes
.gitignore
.lintstagedrc.json
.prettierignore
.prettierrc.json
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
babel.config.js
docker-compose.yml
empty-shim.js
eslint.config.js
package.json
postcss.config.js
tailwind.config.js
tsconfig.build.json
tsconfig.json
vitest.config.mts
vitest.e2e.config.mts
webpack.config.js
```

## Entry points

- [.storybook/main.js](https://github.com/sqlectron/sqlectron/blob/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3/.storybook/main.js)
- [src/browser/app.ts](https://github.com/sqlectron/sqlectron/blob/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3/src/browser/app.ts)
- [src/browser/core/index.ts](https://github.com/sqlectron/sqlectron/blob/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3/src/browser/core/index.ts)
- [src/browser/main.ts](https://github.com/sqlectron/sqlectron/blob/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3/src/browser/main.ts)
- [src/browser/menu/index.ts](https://github.com/sqlectron/sqlectron/blob/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3/src/browser/menu/index.ts)
- [src/common/types/server.ts](https://github.com/sqlectron/sqlectron/blob/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3/src/common/types/server.ts)
- [src/renderer/containers/app.tsx](https://github.com/sqlectron/sqlectron/blob/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3/src/renderer/containers/app.tsx)
- [src/renderer/hooks/index.ts](https://github.com/sqlectron/sqlectron/blob/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3/src/renderer/hooks/index.ts)
- [src/renderer/reducers/index.ts](https://github.com/sqlectron/sqlectron/blob/b0f5e24015bca7974fbce6ab5e4ada69d51b48b3/src/renderer/reducers/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| browser package | library | Observed | Groups 13 file(s) under browser package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 8 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| renderer package | library | Observed | Groups 82 file(s) under renderer package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 9 file(s) under service / domain layer (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 1 file(s) under stories package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.lintstagedrc.json` (config)
- `.prettierrc.json` (config)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 127 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `test` — 18 analysed file(s)
- `docs` — 9 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.storybook` — 2 analysed file(s)
- `stories` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b0f5e24015bca7974fbce6ab5e4ada69d51b48b3` is the revision these paths and observations refer to.
