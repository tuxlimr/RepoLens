# Project structure: electron/minimal-repro

**Analysed commit:** `afcc34c164dbc24415221c158ed8151a54268523`

**Commit reference:** [afcc34c164dbc24415221c158ed8151a54268523](https://github.com/electron/minimal-repro/commit/afcc34c164dbc24415221c158ed8151a54268523)

**Tree at this commit:** [electron/minimal-repro@afcc34c164db](https://github.com/electron/minimal-repro/tree/afcc34c164dbc24415221c158ed8151a54268523)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | electron/minimal-repro |
| Description | Clone to try a simple Electron app |
| Stars | 11429 |
| Forks | 4854 |
| Licence | CC0-1.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `afcc34c164dbc24415221c158ed8151a54268523` |
| Retrieved at | 2026-11-14T19:12:18.583407+00:00 |
| Files in this snapshot | 12 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    add-to-project.yml
  CODEOWNERS
  dependabot.yml
.gitignore
LICENSE.md
README.md
index.html
main.js
package.json
preload.js
renderer.js
styles.css
```

## Entry points

- [main.js](https://github.com/electron/minimal-repro/blob/afcc34c164dbc24415221c158ed8151a54268523/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/add-to-project.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 9 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `afcc34c164dbc24415221c158ed8151a54268523` is the revision these paths and observations refer to.
