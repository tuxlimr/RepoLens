# Project structure: gommzystudio/device-activity-tracker

**Analysed commit:** `a6e90350fefca2e5bc2190b530be8d6a48399ecf`

**Commit reference:** [a6e90350fefca2e5bc2190b530be8d6a48399ecf](https://github.com/gommzystudio/device-activity-tracker/commit/a6e90350fefca2e5bc2190b530be8d6a48399ecf)

**Tree at this commit:** [gommzystudio/device-activity-tracker@a6e90350fefc](https://github.com/gommzystudio/device-activity-tracker/tree/a6e90350fefca2e5bc2190b530be8d6a48399ecf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gommzystudio/device-activity-tracker |
| Description | A phone number can reveal whether a device is active, in standby or offline (and more). This PoC demonstrates how delivery receipts + RTT timing leak sensitive device-activity patterns. (WhatsApp / Signal) |
| Stars | 5241 |
| Forks | 711 |
| Licence | Other |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `a6e90350fefca2e5bc2190b530be8d6a48399ecf` |
| Retrieved at | 2026-11-14T19:14:24.486731+00:00 |
| Files in this snapshot | 38 |

## Directory tree

```text
client/  (23 files)
  public/  (3 files)
    index.html
    manifest.json
    robots.txt
  src/  (12 files)
    components/  (3 files)
      … 3 files under this directory
    App.css
    App.test.tsx
    App.tsx
    index.css
    index.tsx
    logo.svg
    react-app-env.d.ts
    reportWebVitals.ts
    setupTests.ts
  .dockerignore
  .gitignore
  Dockerfile
  nginx.conf
  package.json
  postcss.config.js
  tailwind.config.js
  tsconfig.json
src/  (5 files)
  scripts/  (1 files)
    init-signal.ts
  index.ts
  server.ts
  signal-tracker.ts
  tracker.ts
.dockerignore
.env.example
.gitignore
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
docker-compose.yml
package.json
tsconfig.json
```

## Entry points

- [client/src/App.tsx](https://github.com/gommzystudio/device-activity-tracker/blob/a6e90350fefca2e5bc2190b530be8d6a48399ecf/client/src/App.tsx)
- [client/src/index.tsx](https://github.com/gommzystudio/device-activity-tracker/blob/a6e90350fefca2e5bc2190b530be8d6a48399ecf/client/src/index.tsx)
- [src/index.ts](https://github.com/gommzystudio/device-activity-tracker/blob/a6e90350fefca2e5bc2190b530be8d6a48399ecf/src/index.ts)
- [src/server.ts](https://github.com/gommzystudio/device-activity-tracker/blob/a6e90350fefca2e5bc2190b530be8d6a48399ecf/src/server.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 11 file(s) under external integrations (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| server.ts package | library | Observed | Groups 1 file(s) under server.ts package (observed from repository paths and static analysis). |
| signal-tracker.ts package | library | Observed | Groups 1 file(s) under signal-tracker.ts package (observed from repository paths and static analysis). |
| tracker.ts package | library | Observed | Groups 1 file(s) under tracker.ts package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `Dockerfile` (container)
- `client/.dockerignore` (container)
- `client/Dockerfile` (container)
- `client/package.json` (manifest)
- `client/public/manifest.json` (config)
- `client/tsconfig.json` (config)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `client` — 23 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `src` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a6e90350fefca2e5bc2190b530be8d6a48399ecf` is the revision these paths and observations refer to.
