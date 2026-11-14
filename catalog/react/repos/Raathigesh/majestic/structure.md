# Project structure: Raathigesh/majestic

**Analysed commit:** `2bb0047188722610c7251e53717ce731bf5ec65e`

**Commit reference:** [2bb0047188722610c7251e53717ce731bf5ec65e](https://github.com/Raathigesh/majestic/commit/2bb0047188722610c7251e53717ce731bf5ec65e)

**Tree at this commit:** [Raathigesh/majestic@2bb004718872](https://github.com/Raathigesh/majestic/tree/2bb0047188722610c7251e53717ce731bf5ec65e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Raathigesh/majestic |
| Description | ⚡ Zero config GUI for Jest |
| Stars | 7437 |
| Forks | 169 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `2bb0047188722610c7251e53717ce731bf5ec65e` |
| Retrieved at | 2026-11-14T19:13:50.405389+00:00 |
| Files in this snapshot | 118 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    nodejs.yml
  issue_template.md
  stale.yml
.vscode/  (1 files)
  launch.json
integration/  (17 files)
  cypress/  (5 files)
    fixtures/  (1 files)
      … 1 files under this directory
    integration/  (1 files)
      … 1 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    support/  (2 files)
      … 2 files under this directory
  projects/  (9 files)
    basic/  (9 files)
      … 9 files under this directory
  cypress.json
  kill.js
  package.json
scripts/  (2 files)
  webpack.server.config.js
  webpack.ui.config.js
server/  (34 files)
  api/  (16 files)
    app/  (2 files)
      … 2 files under this directory
    runner/  (3 files)
      … 3 files under this directory
    workspace/  (10 files)
      … 10 files under this directory
    index.ts
  event-emitter/  (1 files)
    index.ts
  services/  (13 files)
    ast/  (2 files)
      … 2 files under this directory
    file-watcher/  (1 files)
      … 1 files under this directory
    jest-manager/  (4 files)
      … 4 files under this directory
    cli.ts
    config-resolver.ts
    project.ts
    result-handler-api.ts
    results.ts
    types.ts
  index.ts
  logger.ts
  static-files.ts
  typings.d.ts
ui/  (49 files)
  components/  (1 files)
    button.tsx
  coverage-panel/  (1 files)
    index.tsx
  hooks/  (1 files)
    use-keys.ts
  search/  (1 files)
    index.tsx
  sidebar/  (11 files)
    summary/  (1 files)
      … 1 files under this directory
    execution-indicator.tsx
    file-item.tsx
    index.tsx
    logo.tsx
    run.gql
    set-collect-coverage.gql
    set-watch-mode.gql
    should-collect-coverage.gql
    transformer.ts
    tree.tsx
  test-file/  (17 files)
    console-panel/  (1 files)
      … 1 files under this directory
    error-panel/  (1 files)
      … 1 files under this directory
    summary/  (3 files)
      … 3 files under this directory
    file-items-subscription.gql
    index.tsx
    open-failure.gql
    query.gql
    result.gql
    run-file.gql
    subscription.gql
    test-indicator.tsx
    test-item.tsx
    transformer.ts
    update-snapshot.gql
    use-subscription.tsx
  apollo-client.ts
  app.gql
  app.tsx
  container.tsx
  error.tsx
  index.tsx
  loading.tsx
  query.gql
  runner-status-query.gql
  runner-status-subs.gql
  set-selected-file.gql
  split-panel-style.ts
  stop-runner.gql
  summary-query.gql
  summary-subscription.gql
  theme.ts
  typings.d.ts
.all-contributorsrc
.babelrc
.gitignore
.prettierrc
CONTRIBUTING.MD
LICENSE
README.md
Troubleshooting.md
nodemon.json
package.json
tsconfig.json
tsconfig.server.json
```

## Entry points

- [integration/cypress/plugins/index.js](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/integration/cypress/plugins/index.js)
- [integration/cypress/support/index.js](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/integration/cypress/support/index.js)
- [integration/projects/basic/app.js](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/integration/projects/basic/app.js)
- [server/api/app/app.ts](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/server/api/app/app.ts)
- [server/api/index.ts](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/server/api/index.ts)
- [server/event-emitter/index.ts](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/server/event-emitter/index.ts)
- [server/index.ts](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/server/index.ts)
- [server/services/file-watcher/index.ts](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/server/services/file-watcher/index.ts)
- [server/services/jest-manager/index.ts](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/server/services/jest-manager/index.ts)
- [ui/app.tsx](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/ui/app.tsx)
- [ui/coverage-panel/index.tsx](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/ui/coverage-panel/index.tsx)
- [ui/index.tsx](https://github.com/Raathigesh/majestic/blob/2bb0047188722610c7251e53717ce731bf5ec65e/ui/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 16 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 12 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 5 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 13 file(s) under service / domain layer (observed from repository paths and static analysis). |
| ui package | library | Observed | Groups 28 file(s) under ui package (observed from repository paths and static analysis). |

## Important files

- `.github/stale.yml` (config)
- `.github/workflows/nodejs.yml` (ci)
- `.vscode/launch.json` (config)
- `integration/cypress.json` (config)
- `integration/cypress/fixtures/example.json` (config)
- `integration/package.json` (manifest)
- `integration/projects/basic/package.json` (manifest)
- `nodemon.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tsconfig.server.json` (config)

## Top-level layout

- `ui` — 49 analysed file(s)
- `server` — 34 analysed file(s)
- `integration` — 17 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 3 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2bb0047188722610c7251e53717ce731bf5ec65e` is the revision these paths and observations refer to.
