# Project structure: oldboyxx/jira_clone

**Analysed commit:** `26a9e77b1789fef9cb43edb5d6018cf1663cf035`

**Commit reference:** [26a9e77b1789fef9cb43edb5d6018cf1663cf035](https://github.com/oldboyxx/jira_clone/commit/26a9e77b1789fef9cb43edb5d6018cf1663cf035)

**Tree at this commit:** [oldboyxx/jira_clone@26a9e77b1789](https://github.com/oldboyxx/jira_clone/tree/26a9e77b1789fef9cb43edb5d6018cf1663cf035)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | oldboyxx/jira_clone |
| Description | A simplified Jira clone built with React/Babel (Client), and Node/TypeScript (API). Auto formatted with Prettier, tested with Cypress. |
| Stars | 11061 |
| Forks | 2136 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `26a9e77b1789fef9cb43edb5d6018cf1663cf035` |
| Retrieved at | 2026-11-14T19:12:26.522997+00:00 |
| Files in this snapshot | 207 |

## Directory tree

```text
.vscode/  (1 files)
  settings.json
api/  (39 files)
  src/  (31 files)
    constants/  (2 files)
      … 2 files under this directory
    controllers/  (6 files)
      … 6 files under this directory
    database/  (4 files)
      … 4 files under this directory
    entities/  (5 files)
      … 5 files under this directory
    errors/  (3 files)
      … 3 files under this directory
    middleware/  (3 files)
      … 3 files under this directory
    serializers/  (1 files)
      … 1 files under this directory
    types/  (2 files)
      … 2 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    index.ts
    routes.ts
  .env.example
  .eslintignore
  .eslintrc.json
  .prettierrc
  README.md
  package.json
  tsconfig-paths.js
  tsconfig.json
client/  (162 files)
  cypress/  (12 files)
    integration/  (7 files)
      … 7 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    support/  (3 files)
      … 3 files under this directory
    .eslintrc.json
  jest/  (2 files)
    fileMock.js
    styleMock.js
  src/  (137 files)
    App/  (8 files)
      … 8 files under this directory
    Auth/  (1 files)
      … 1 files under this directory
    Project/  (56 files)
      … 56 files under this directory
    shared/  (69 files)
      … 69 files under this directory
    browserHistory.js
    index.html
    index.jsx
  .babelrc
  .eslintrc.json
  .prettierrc
  README.md
  cypress.json
  jest.config.js
  jsconfig.json
  package.json
  server.js
  webpack.config.js
  webpack.config.production.js
.gitignore
CONTRIBUTING.md
LICENSE
README.md
package.json
```

## Entry points

- [api/src/entities/index.ts](https://github.com/oldboyxx/jira_clone/blob/26a9e77b1789fef9cb43edb5d6018cf1663cf035/api/src/entities/index.ts)
- [api/src/errors/index.ts](https://github.com/oldboyxx/jira_clone/blob/26a9e77b1789fef9cb43edb5d6018cf1663cf035/api/src/errors/index.ts)
- [api/src/index.ts](https://github.com/oldboyxx/jira_clone/blob/26a9e77b1789fef9cb43edb5d6018cf1663cf035/api/src/index.ts)
- [client/cypress/plugins/index.js](https://github.com/oldboyxx/jira_clone/blob/26a9e77b1789fef9cb43edb5d6018cf1663cf035/client/cypress/plugins/index.js)
- [client/cypress/support/index.js](https://github.com/oldboyxx/jira_clone/blob/26a9e77b1789fef9cb43edb5d6018cf1663cf035/client/cypress/support/index.js)
- [client/server.js](https://github.com/oldboyxx/jira_clone/blob/26a9e77b1789fef9cb43edb5d6018cf1663cf035/client/server.js)
- [client/src/App/index.jsx](https://github.com/oldboyxx/jira_clone/blob/26a9e77b1789fef9cb43edb5d6018cf1663cf035/client/src/App/index.jsx)
- [client/src/Project/index.jsx](https://github.com/oldboyxx/jira_clone/blob/26a9e77b1789fef9cb43edb5d6018cf1663cf035/client/src/Project/index.jsx)
- [client/src/index.jsx](https://github.com/oldboyxx/jira_clone/blob/26a9e77b1789fef9cb43edb5d6018cf1663cf035/client/src/index.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 35 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 148 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.vscode/settings.json` (config)
- `api/.env.example` (config)
- `api/.eslintrc.json` (config)
- `api/package.json` (manifest)
- `api/tsconfig.json` (config)
- `client/.eslintrc.json` (config)
- `client/cypress.json` (config)
- `client/cypress/.eslintrc.json` (config)
- `client/jsconfig.json` (config)
- `client/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `client` — 162 analysed file(s)
- `api` — 39 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `26a9e77b1789fef9cb43edb5d6018cf1663cf035` is the revision these paths and observations refer to.
