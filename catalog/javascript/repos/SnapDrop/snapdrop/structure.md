# Project structure: SnapDrop/snapdrop

**Analysed commit:** `b8b78cc22a672fd7c442f5a4866a8d9b0c05362e`

**Commit reference:** [b8b78cc22a672fd7c442f5a4866a8d9b0c05362e](https://github.com/SnapDrop/snapdrop/commit/b8b78cc22a672fd7c442f5a4866a8d9b0c05362e)

**Tree at this commit:** [SnapDrop/snapdrop@b8b78cc22a67](https://github.com/SnapDrop/snapdrop/tree/b8b78cc22a672fd7c442f5a4866a8d9b0c05362e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | SnapDrop/snapdrop |
| Description | A Progressive Web App for local file sharing  |
| Stars | 19711 |
| Forks | 1864 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b8b78cc22a672fd7c442f5a4866a8d9b0c05362e` |
| Retrieved at | 2026-11-14T19:11:17.014965+00:00 |
| Files in this snapshot | 23 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
client/  (8 files)
  images/  (1 files)
    safari-pinned-tab.svg
  scripts/  (3 files)
    clipboard.js
    network.js
    ui.js
  index.html
  manifest.json
  service-worker.js
  styles.css
docker/  (6 files)
  nginx/  (1 files)
    default.conf
  openssl/  (3 files)
    create.sh
    snapdropCA.cnf
    snapdropCert.cnf
  fqdn.env
  nginx-with-openssl.Dockerfile
docs/  (2 files)
  faq.md
  local-dev.md
server/  (2 files)
  index.js
  package.json
.gitignore
LICENSE
README.md
docker-compose.yml
```

## Entry points

- [server/index.js](https://github.com/SnapDrop/snapdrop/blob/b8b78cc22a672fd7c442f5a4866a8d9b0c05362e/server/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 4 file(s) under external integrations (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 1 file(s) under server package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `client/manifest.json` (config)
- `docker-compose.yml` (container)
- `server/package.json` (manifest)

## Top-level layout

- `client` — 8 analysed file(s)
- `docker` — 6 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `docs` — 2 analysed file(s)
- `server` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b8b78cc22a672fd7c442f5a4866a8d9b0c05362e` is the revision these paths and observations refer to.
