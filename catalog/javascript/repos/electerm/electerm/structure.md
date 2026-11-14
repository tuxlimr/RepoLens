# Project structure: electerm/electerm

**Analysed commit:** `ee090c7cfa3d6bcbc8b9a3595839728323207347`

**Commit reference:** [ee090c7cfa3d6bcbc8b9a3595839728323207347](https://github.com/electerm/electerm/commit/ee090c7cfa3d6bcbc8b9a3595839728323207347)

**Tree at this commit:** [electerm/electerm@ee090c7cfa3d](https://github.com/electerm/electerm/tree/ee090c7cfa3d6bcbc8b9a3595839728323207347)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | electerm/electerm |
| Description | 📻Free and open-sourced terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice client(Linux, Mac, Windows, Android, HarmonyOS, iOS) |
| Stars | 15631 |
| Forks | 1264 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ee090c7cfa3d6bcbc8b9a3595839728323207347` |
| Retrieved at | 2026-11-14T19:11:36.874237+00:00 |
| Files in this snapshot | 732 |

## Directory tree

```text
.github/  (42 files)
  ISSUE_TEMPLATE/  (3 files)
    1-bug-report.yml
    2-proposal.yml
    config.yml
  workflows/  (33 files)
    build-homepage-trigger.yml
    electerm-react-publish.yml
    linux-arm-legacy.yml
    linux-arm.yml
    linux-deb-tar.yml
    linux-legacy.yml
    linux-loong64-legacy.yml
    linux-loong64.yml
    linux-riscv64.yml
    linux-rpm-snap.yml
    mac-10.yml
    mac-arm.yml
    mac-test-1.yml
    mac-test-2.yml
    mac-test-3.yml
    mac-test-4.yml
    mac.yml
    ms-store-upload.yml
    ppc64le.yml
    snap-store-upload.yml
    sync-atomgit-release.yml
    sync-gitee.yml
    trigger-npm-publish.yml
    upload-release-assets-r2.yml
    … 9 more files
  CONTRIBUTING.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  SECURITY.md
  code-of-conduct.md
  dependabot.yml
src/  (686 files)
  app/  (173 files)
    common/  (25 files)
      … 25 files under this directory
    lib/  (58 files)
      … 58 files under this directory
    mcp/  (3 files)
      … 3 files under this directory
    migrate/  (13 files)
      … 13 files under this directory
    preload/  (1 files)
      … 1 files under this directory
    server/  (50 files)
      … 50 files under this directory
    upgrade/  (7 files)
      … 7 files under this directory
    widgets/  (15 files)
      … 15 files under this directory
    app.js
  client/  (513 files)
    common/  (113 files)
      … 113 files under this directory
    components/  (400 files)
      … 400 files under this directory
.gitignore
LICENSE
README.md
package.json
```

## Entry points

- [src/app/app.js](https://github.com/electerm/electerm/blob/ee090c7cfa3d6bcbc8b9a3595839728323207347/src/app/app.js)
- [src/app/migrate/index.js](https://github.com/electerm/electerm/blob/ee090c7cfa3d6bcbc8b9a3595839728323207347/src/app/migrate/index.js)
- [src/app/server/server.js](https://github.com/electerm/electerm/blob/ee090c7cfa3d6bcbc8b9a3595839728323207347/src/app/server/server.js)
- [src/app/upgrade/index.js](https://github.com/electerm/electerm/blob/ee090c7cfa3d6bcbc8b9a3595839728323207347/src/app/upgrade/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 173 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 452 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/1-bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/2-proposal.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build-homepage-trigger.yml` (ci)
- `.github/workflows/electerm-react-publish.yml` (ci)
- `.github/workflows/linux-arm-legacy.yml` (ci)
- `.github/workflows/linux-arm.yml` (ci)
- `.github/workflows/linux-deb-tar.yml` (ci)
- `.github/workflows/linux-legacy.yml` (ci)
- `.github/workflows/linux-loong64-legacy.yml` (ci)
- `.github/workflows/linux-loong64.yml` (ci)
- `.github/workflows/linux-riscv64.yml` (ci)
- `.github/workflows/linux-rpm-snap.yml` (ci)
- `.github/workflows/mac-10.yml` (ci)
- `.github/workflows/mac-arm.yml` (ci)
- `.github/workflows/mac-test-1.yml` (ci)
- `.github/workflows/mac-test-2.yml` (ci)
- `.github/workflows/mac-test-3.yml` (ci)
- `.github/workflows/mac-test-4.yml` (ci)
- `.github/workflows/mac.yml` (ci)
- `.github/workflows/ms-store-upload.yml` (ci)
- `.github/workflows/ppc64le.yml` (ci)
- `.github/workflows/snap-store-upload.yml` (ci)
- `.github/workflows/sync-atomgit-release.yml` (ci)
- `.github/workflows/sync-gitee.yml` (ci)
- `.github/workflows/trigger-npm-publish.yml` (ci)
- `.github/workflows/upload-release-assets-r2.yml` (ci)
- `.github/workflows/win-appx.yml` (ci)
- `.github/workflows/win-arm.yml` (ci)
- `.github/workflows/win-loose.yml` (ci)
- `.github/workflows/win-nsis-arm.yml` (ci)
- `.github/workflows/win-nsis.yml` (ci)
- `.github/workflows/win-portable.yml` (ci)
- `.github/workflows/win-tar.yml` (ci)
- `.github/workflows/win7-tar.yml` (ci)
- `.github/workflows/winget.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 686 analysed file(s)
- `.github` — 42 analysed file(s)
- `(root files)` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 68 file(s) were skipped during inventory (68 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ee090c7cfa3d6bcbc8b9a3595839728323207347` is the revision these paths and observations refer to.
