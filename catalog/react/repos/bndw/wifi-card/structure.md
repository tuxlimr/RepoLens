# Project structure: bndw/wifi-card

**Analysed commit:** `7a990dd2411f6c8758ad696bf737b509f9672953`

**Commit reference:** [7a990dd2411f6c8758ad696bf737b509f9672953](https://github.com/bndw/wifi-card/commit/7a990dd2411f6c8758ad696bf737b509f9672953)

**Tree at this commit:** [bndw/wifi-card@7a990dd2411f](https://github.com/bndw/wifi-card/tree/7a990dd2411f6c8758ad696bf737b509f9672953)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bndw/wifi-card |
| Description | 📶 Print a QR code for connecting to your WiFi (wificard.io) |
| Stars | 7210 |
| Forks | 509 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `7a990dd2411f6c8758ad696bf737b509f9672953` |
| Retrieved at | 2026-11-14T19:13:58.747207+00:00 |
| Files in this snapshot | 25 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    master_push.yml
    pull_request.yml
.husky/  (1 files)
  pre-commit
public/  (2 files)
  manifest.json
  robots.txt
src/  (9 files)
  components/  (3 files)
    Settings.jsx
    WifiCard.jsx
    style.css
  App.jsx
  customStyles.js
  i18n.js
  index.jsx
  style.css
  translations.js
.dockerignore
.gitignore
.prettierrc.json
.yarnrc.yml
Dockerfile
LICENSE.md
Makefile
README.md
index.html
package.json
vite.config.js
```

## Entry points

- [src/App.jsx](https://github.com/bndw/wifi-card/blob/7a990dd2411f6c8758ad696bf737b509f9672953/src/App.jsx)
- [src/index.jsx](https://github.com/bndw/wifi-card/blob/7a990dd2411f6c8758ad696bf737b509f9672953/src/index.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.jsx package | library | Observed | Groups 1 file(s) under app.jsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 2 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| customStyles.js package | library | Observed | Groups 1 file(s) under customstyles.js package (observed from repository paths and static analysis). |
| i18n.js package | library | Observed | Groups 1 file(s) under i18n.js package (observed from repository paths and static analysis). |
| index.jsx package | library | Observed | Groups 1 file(s) under index.jsx package (observed from repository paths and static analysis). |
| translations.js package | library | Observed | Groups 1 file(s) under translations.js package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/workflows/master_push.yml` (ci)
- `.github/workflows/pull_request.yml` (ci)
- `.prettierrc.json` (config)
- `.yarnrc.yml` (config)
- `Dockerfile` (container)
- `package.json` (manifest)
- `public/manifest.json` (config)

## Top-level layout

- `(root files)` — 11 analysed file(s)
- `src` — 9 analysed file(s)
- `.github` — 2 analysed file(s)
- `public` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7a990dd2411f6c8758ad696bf737b509f9672953` is the revision these paths and observations refer to.
