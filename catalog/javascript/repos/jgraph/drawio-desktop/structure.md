# Project structure: jgraph/drawio-desktop

**Analysed commit:** `0623fb3c1523639b06600d5c33e3a127bf82aa1c`

**Commit reference:** [0623fb3c1523639b06600d5c33e3a127bf82aa1c](https://github.com/jgraph/drawio-desktop/commit/0623fb3c1523639b06600d5c33e3a127bf82aa1c)

**Tree at this commit:** [jgraph/drawio-desktop@0623fb3c1523](https://github.com/jgraph/drawio-desktop/tree/0623fb3c1523639b06600d5c33e3a127bf82aa1c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jgraph/drawio-desktop |
| Description | Official electron build of draw.io |
| Stars | 63996 |
| Forks | 5819 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | dev |
| Analysed commit | `0623fb3c1523639b06600d5c33e3a127bf82aa1c` |
| Retrieved at | 2026-11-14T19:10:35.288632+00:00 |
| Files in this snapshot | 66 |

## Directory tree

```text
.github/  (13 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (8 files)
    electron-builder-win.yml
    electron-builder.yml
    flathub-release.yml
    hash-gen.yml
    personal-build.yml
    prepare-release.yml
    stale.yml
    store-credentials-check.yml
  FUNDING.yml
  bug_report.md
  feature_request.md
doc/  (3 files)
  .gitignore
  BUILDING_FOR_PERSONAL_USE.md
  RELEASE_PROCESS.md
src/  (33 files)
  main/  (18 files)
    args.js
    backup-file.js
    config-paths.js
    disableUpdate.js
    electron-preload.js
    electron.js
    export-files.js
    file-watcher.js
    html-export.js
    pdf-xml.js
    png-xml.js
    print-options.js
    progress-bar.js
    system-path.js
    update-channel.js
    update-mode.js
    url-params.js
    window-bounds.js
  test/  (15 files)
    backup-file.test.js
    cli-args.test.js
    config-paths.test.js
    export-files.test.js
    file-watcher.test.js
    html-export.test.js
    msi-project-created.test.js
    pdf-xml.test.js
    png-xml.test.js
    print-options.test.js
    system-path.test.js
    update-channel.test.js
    update-mode.test.js
    url-params.test.js
    window-bounds.test.js
.gitignore
.gitmodules
.nvmrc
CLAUDE.md
CODE_OF_CONDUCT.md
DEVELOPMENT.md
LICENSE
README.md
SECURITY.md
electron-builder-appx.json
electron-builder-linux-mac.json
electron-builder-snap.json
electron-builder-win-arm64.json
electron-builder-win.json
package.json
preload.js
sync.cjs
```

## Entry points

- [src/main/electron.js](https://github.com/jgraph/drawio-desktop/blob/0623fb3c1523639b06600d5c33e3a127bf82aa1c/src/main/electron.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| main package | library | Observed | Groups 18 file(s) under main package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 15 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/electron-builder-win.yml` (ci)
- `.github/workflows/electron-builder.yml` (ci)
- `.github/workflows/flathub-release.yml` (ci)
- `.github/workflows/hash-gen.yml` (ci)
- `.github/workflows/personal-build.yml` (ci)
- `.github/workflows/prepare-release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/store-credentials-check.yml` (ci)
- `electron-builder-appx.json` (config)
- `electron-builder-linux-mac.json` (config)
- `electron-builder-snap.json` (config)
- `electron-builder-win-arm64.json` (config)
- `electron-builder-win.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 33 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 13 analysed file(s)
- `doc` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 12 file(s) were skipped during inventory (1 x lockfile excluded; 11 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0623fb3c1523639b06600d5c33e3a127bf82aa1c` is the revision these paths and observations refer to.
