# Project structure: listen1/listen1_desktop

**Analysed commit:** `bbc38654bd593d4ae70143230ea7814b34d09128`

**Commit reference:** [bbc38654bd593d4ae70143230ea7814b34d09128](https://github.com/listen1/listen1_desktop/commit/bbc38654bd593d4ae70143230ea7814b34d09128)

**Tree at this commit:** [listen1/listen1_desktop@bbc38654bd59](https://github.com/listen1/listen1_desktop/tree/bbc38654bd593d4ae70143230ea7814b34d09128)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | listen1/listen1_desktop |
| Description | one for all free music in china (Windows, Mac, Linux desktop) |
| Stars | 11452 |
| Forks | 1524 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `bbc38654bd593d4ae70143230ea7814b34d09128` |
| Retrieved at | 2026-11-14T19:12:18.487724+00:00 |
| Files in this snapshot | 12 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    release.yml
app/  (5 files)
  floatingWindow.html
  functions.js
  main.js
  package.json
  preload.js
.gitignore
.gitmodules
.prettierrc
LICENSE.md
README.md
package.json
```

## Entry points

- [app/main.js](https://github.com/listen1/listen1_desktop/blob/bbc38654bd593d4ae70143230ea7814b34d09128/app/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 3 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/release.yml` (ci)
- `app/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 6 analysed file(s)
- `app` — 5 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bbc38654bd593d4ae70143230ea7814b34d09128` is the revision these paths and observations refer to.
