# Project structure: openai/openai-realtime-console

**Analysed commit:** `ab8b8f5852b47ec1b9ef73bf566851d0eeafddbb`

**Commit reference:** [ab8b8f5852b47ec1b9ef73bf566851d0eeafddbb](https://github.com/openai/openai-realtime-console/commit/ab8b8f5852b47ec1b9ef73bf566851d0eeafddbb)

**Tree at this commit:** [openai/openai-realtime-console@ab8b8f5852b4](https://github.com/openai/openai-realtime-console/tree/ab8b8f5852b47ec1b9ef73bf566851d0eeafddbb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/openai-realtime-console |
| Description | React app for inspecting, building and debugging with the Realtime API |
| Stars | 3620 |
| Forks | 1402 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `ab8b8f5852b47ec1b9ef73bf566851d0eeafddbb` |
| Retrieved at | 2026-11-14T19:15:11.648756+00:00 |
| Files in this snapshot | 22 |

## Directory tree

```text
client/  (12 files)
  assets/  (1 files)
    openai-logomark.svg
  components/  (5 files)
    App.jsx
    Button.jsx
    EventLog.jsx
    SessionControls.jsx
    ToolPanel.jsx
  pages/  (1 files)
    index.jsx
  base.css
  entry-client.jsx
  entry-server.jsx
  index.html
  index.js
.env.example
.gitignore
.prettierrc
LICENSE
README.md
package.json
postcss.config.cjs
server.js
tailwind.config.js
vite.config.js
```

## Entry points

- [client/components/App.jsx](https://github.com/openai/openai-realtime-console/blob/ab8b8f5852b47ec1b9ef73bf566851d0eeafddbb/client/components/App.jsx)
- [client/index.js](https://github.com/openai/openai-realtime-console/blob/ab8b8f5852b47ec1b9ef73bf566851d0eeafddbb/client/index.js)
- [client/pages/index.jsx](https://github.com/openai/openai-realtime-console/blob/ab8b8f5852b47ec1b9ef73bf566851d0eeafddbb/client/pages/index.jsx)
- [server.js](https://github.com/openai/openai-realtime-console/blob/ab8b8f5852b47ec1b9ef73bf566851d0eeafddbb/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 9 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `package.json` (manifest)

## Top-level layout

- `client` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ab8b8f5852b47ec1b9ef73bf566851d0eeafddbb` is the revision these paths and observations refer to.
