# Project structure: localtunnel/localtunnel

**Analysed commit:** `decafd5c0fce195e7901b159d22e3e4a447958c7`

**Commit reference:** [decafd5c0fce195e7901b159d22e3e4a447958c7](https://github.com/localtunnel/localtunnel/commit/decafd5c0fce195e7901b159d22e3e4a447958c7)

**Tree at this commit:** [localtunnel/localtunnel@decafd5c0fce](https://github.com/localtunnel/localtunnel/tree/decafd5c0fce195e7901b159d22e3e4a447958c7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | localtunnel/localtunnel |
| Description | expose yourself |
| Stars | 22501 |
| Forks | 1566 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `decafd5c0fce195e7901b159d22e3e4a447958c7` |
| Retrieved at | 2026-11-14T19:11:08.349621+00:00 |
| Files in this snapshot | 13 |

## Directory tree

```text
bin/  (1 files)
  lt.js
lib/  (3 files)
  HeaderHostTransformer.js
  Tunnel.js
  TunnelCluster.js
.eslintrc.js
.gitignore
.travis.yml
CHANGELOG.md
LICENSE
README.md
localtunnel.js
localtunnel.spec.js
package.json
```

## Entry points

- [localtunnel.js](https://github.com/localtunnel/localtunnel/blob/decafd5c0fce195e7901b159d22e3e4a447958c7/localtunnel.js)
- [bin/lt.js](https://github.com/localtunnel/localtunnel/blob/decafd5c0fce195e7901b159d22e3e4a447958c7/bin/lt.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 3 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 9 analysed file(s)
- `lib` — 3 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `decafd5c0fce195e7901b159d22e3e4a447958c7` is the revision these paths and observations refer to.
