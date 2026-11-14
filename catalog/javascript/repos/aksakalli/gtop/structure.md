# Project structure: aksakalli/gtop

**Analysed commit:** `ac6c2e11a683d41ae25c41912646d6b320285f8b`

**Commit reference:** [ac6c2e11a683d41ae25c41912646d6b320285f8b](https://github.com/aksakalli/gtop/commit/ac6c2e11a683d41ae25c41912646d6b320285f8b)

**Tree at this commit:** [aksakalli/gtop@ac6c2e11a683](https://github.com/aksakalli/gtop/tree/ac6c2e11a683d41ae25c41912646d6b320285f8b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | aksakalli/gtop |
| Description | System monitoring dashboard for terminal |
| Stars | 9936 |
| Forks | 339 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ac6c2e11a683d41ae25c41912646d6b320285f8b` |
| Retrieved at | 2026-11-14T19:12:46.929603+00:00 |
| Files in this snapshot | 23 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (2 files)
    ci.yml
    release.yml
  CONTRIBUTING.md
  ISSUE_TEMPLATE.md
bin/  (1 files)
  gtop
lib/  (8 files)
  monitor/  (6 files)
    cpu.js
    disk.js
    index.js
    mem.js
    net.js
    proc.js
  gtop.js
  utils.js
snap/  (1 files)
  snapcraft.yaml
.editorconfig
.gitignore
.npmignore
CLI.md
Dockerfile
LICENSE
README.md
index.js
package.json
```

## Entry points

- [index.js](https://github.com/aksakalli/gtop/blob/ac6c2e11a683d41ae25c41912646d6b320285f8b/index.js)
- [bin/gtop](https://github.com/aksakalli/gtop/blob/ac6c2e11a683d41ae25c41912646d6b320285f8b/bin/gtop)
- [lib/monitor/index.js](https://github.com/aksakalli/gtop/blob/ac6c2e11a683d41ae25c41912646d6b320285f8b/lib/monitor/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 8 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `Dockerfile` (container)
- `package.json` (manifest)
- `snap/snapcraft.yaml` (config)

## Top-level layout

- `(root files)` — 9 analysed file(s)
- `lib` — 8 analysed file(s)
- `.github` — 4 analysed file(s)
- `bin` — 1 analysed file(s)
- `snap` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ac6c2e11a683d41ae25c41912646d6b320285f8b` is the revision these paths and observations refer to.
