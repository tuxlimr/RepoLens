# Project structure: adrianhajdin/project_chat_application

**Analysed commit:** `c0b49d1e66cbe78d238419ed2746259ec84be8e8`

**Commit reference:** [c0b49d1e66cbe78d238419ed2746259ec84be8e8](https://github.com/adrianhajdin/project_chat_application/commit/c0b49d1e66cbe78d238419ed2746259ec84be8e8)

**Tree at this commit:** [adrianhajdin/project_chat_application@c0b49d1e66cb](https://github.com/adrianhajdin/project_chat_application/tree/c0b49d1e66cbe78d238419ed2746259ec84be8e8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | adrianhajdin/project_chat_application |
| Description | This is a code repository for the corresponding YouTube video. In this tutorial we are going to build and deploy a real time chat application. Covered topics: React.js, Node.js, Express.js, and Socket.io. |
| Stars | 4132 |
| Forks | 1849 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c0b49d1e66cbe78d238419ed2746259ec84be8e8` |
| Retrieved at | 2026-11-14T19:14:52.337002+00:00 |
| Files in this snapshot | 31 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
.netlify/  (1 files)
  state.json
client/  (21 files)
  public/  (1 files)
    index.html
  src/  (16 files)
    components/  (14 files)
      … 14 files under this directory
    App.js
    index.js
  .eslintrc.js
  .gitignore
  README.md
  package.json
server/  (6 files)
  .gitignore
  Procfile
  index.js
  package.json
  router.js
  users.js
.gitignore
README.md
```

## Entry points

- [server/index.js](https://github.com/adrianhajdin/project_chat_application/blob/c0b49d1e66cbe78d238419ed2746259ec84be8e8/server/index.js)
- [client/src/App.js](https://github.com/adrianhajdin/project_chat_application/blob/c0b49d1e66cbe78d238419ed2746259ec84be8e8/client/src/App.js)
- [client/src/index.js](https://github.com/adrianhajdin/project_chat_application/blob/c0b49d1e66cbe78d238419ed2746259ec84be8e8/client/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 10 file(s) under external integrations (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 3 file(s) under server package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.netlify/state.json` (config)
- `client/package.json` (manifest)
- `server/package.json` (manifest)

## Top-level layout

- `client` — 21 analysed file(s)
- `server` — 6 analysed file(s)
- `(root files)` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `.netlify` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c0b49d1e66cbe78d238419ed2746259ec84be8e8` is the revision these paths and observations refer to.
