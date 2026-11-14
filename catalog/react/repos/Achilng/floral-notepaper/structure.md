# Project structure: Achilng/floral-notepaper

**Analysed commit:** `8b624e0b1dc38ea66d0fcea83fd4e3117d63d8c3`

**Commit reference:** [8b624e0b1dc38ea66d0fcea83fd4e3117d63d8c3](https://github.com/Achilng/floral-notepaper/commit/8b624e0b1dc38ea66d0fcea83fd4e3117d63d8c3)

**Tree at this commit:** [Achilng/floral-notepaper@8b624e0b1dc3](https://github.com/Achilng/floral-notepaper/tree/8b624e0b1dc38ea66d0fcea83fd4e3117d63d8c3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Achilng/floral-notepaper |
| Description | 花笺，轻量优雅的跨平台桌面便签工具，支持 Markdown 编辑与预览 |
| Stars | 5623 |
| Forks | 334 |
| Licence | MIT |
| Language | Rust |
| Default branch | main |
| Analysed commit | `8b624e0b1dc38ea66d0fcea83fd4e3117d63d8c3` |
| Retrieved at | 2026-11-14T19:14:17.496874+00:00 |
| Files in this snapshot | 172 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (3 files)
    bug.yml
    config.yml
    enhancement.yml
  workflows/  (7 files)
    build-artifacts.yml
    issue-platform-label.yml
    mirrorchyan_release.yml
    mirrorchyan_release_note.yml
    pulls.yml
    rebuild-release.yml
    release.yml
  pull_request_template.md
.husky/  (1 files)
  pre-commit
Docs/  (7 files)
  release-note/  (2 files)
    1.1.0.md
    1.2.0.md
  CONTRIBUTING_en-US.md
  CONTRIBUTING_zh-HK.md
  MSSTORE_PUBLISH.md
  RELEASE_WORKFLOW.md
  signpath-configurations.md
scripts/  (11 files)
  assert-pe-version.ps1
  build-msix.ps1
  build-msixupload.ps1
  build-windows-local.ps1
  fetch-contributors.mjs
  prepare-nsis-toolchain.ps1
  set-version.mjs
  sign-msix-self-signed.ps1
  verify-authenticode.ps1
  verify-msix-package.ps1
  verify-release-tag.sh
src/  (86 files)
  assets/  (2 files)
    fonts/  (2 files)
      … 2 files under this directory
  components/  (14 files)
    AboutPanel.test.tsx
    AboutPanel.tsx
    BackgroundLayer.tsx
    ContextMenu.tsx
    MainWindow.tsx
    NotePad.tsx
    NotepadOpenPanel.tsx
    SettingsPanel.tsx
    SlidingButtonGroup.tsx
    Tile.tsx
    TileShowcase.tsx
    Toast.tsx
    popupPosition.test.ts
    popupPosition.ts
  features/  (52 files)
    images/  (3 files)
      … 3 files under this directory
    importExport/  (2 files)
      … 2 files under this directory
    markdown/  (9 files)
      … 9 files under this directory
    notes/  (6 files)
      … 6 files under this directory
    settings/  (9 files)
      … 9 files under this directory
    update/  (9 files)
      … 9 files under this directory
    windows/  (14 files)
      … 14 files under this directory
  locales/  (14 files)
    en-US/  (2 files)
      … 2 files under this directory
    zh-CN/  (2 files)
      … 2 files under this directory
    zh-HK/  (2 files)
      … 2 files under this directory
    i18next.d.ts
    index.ts
    locale-whitelist.test.ts
    locale-whitelist.ts
    resources.test.ts
    resources.ts
    test-setup.ts
    tips.ts
  App.css
  App.tsx
  main.tsx
  vite-env.d.ts
src-tauri/  (39 files)
  capabilities/  (1 files)
    default.json
  icons/  (2 files)
    android/  (2 files)
      … 2 files under this directory
  msix/  (4 files)
    lang-en-US/  (1 files)
      … 1 files under this directory
    lang-zh-CN/  (1 files)
      … 1 files under this directory
    lang-zh-HK/  (1 files)
      … 1 files under this directory
    AppxManifest.template.xml
  src/  (24 files)
    services/  (2 files)
      … 2 files under this directory
    updater/  (17 files)
      … 17 files under this directory
    desktop.rs
    json_io.rs
    lib.rs
    locales.rs
    main.rs
  .gitignore
  Cargo.toml
  build.rs
  linux-desktop-template.hbs
  nsis-hooks.nsh
  tauri.conf.json
  tauri.linux.conf.json
  tauri.macos.conf.json
tests/  (1 files)
  AppCss.test.ts
.gitattributes
.gitignore
.oxfmtrc.json
.prettierignore
CONTRIBUTING.md
LICENSE
PRIVACY
README.md
README_en-US.md
README_zh-HK.md
THIRD_PARTY_NOTICES.md
index.html
package.json
tsconfig.json
tsconfig.node.json
vite.config.ts
```

## Entry points

- [src/App.tsx](https://github.com/Achilng/floral-notepaper/blob/8b624e0b1dc38ea66d0fcea83fd4e3117d63d8c3/src/App.tsx)
- [src/locales/index.ts](https://github.com/Achilng/floral-notepaper/blob/8b624e0b1dc38ea66d0fcea83fd4e3117d63d8c3/src/locales/index.ts)
- [src/main.tsx](https://github.com/Achilng/floral-notepaper/blob/8b624e0b1dc38ea66d0fcea83fd4e3117d63d8c3/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 14 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 24 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| features package | library | Observed | Groups 43 file(s) under features package (observed from repository paths and static analysis). |
| locales package | library | Observed | Groups 8 file(s) under locales package (observed from repository paths and static analysis). |
| main.tsx package | library | Observed | Groups 1 file(s) under main.tsx package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 2 file(s) under service / domain layer (observed from repository paths and static analysis). |
| src-tauri package | library | Observed | Groups 22 file(s) under src-tauri package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| vite-env.d.ts package | library | Observed | Groups 1 file(s) under vite-env.d.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/enhancement.yml` (config)
- `.github/workflows/build-artifacts.yml` (ci)
- `.github/workflows/issue-platform-label.yml` (ci)
- `.github/workflows/mirrorchyan_release.yml` (ci)
- `.github/workflows/mirrorchyan_release_note.yml` (ci)
- `.github/workflows/pulls.yml` (ci)
- `.github/workflows/rebuild-release.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.oxfmtrc.json` (config)
- `package.json` (manifest)
- `src-tauri/Cargo.toml` (manifest)
- `src-tauri/capabilities/default.json` (config)
- `src-tauri/src/updater/fixtures/update-manifest.valid.json` (config)
- `src-tauri/tauri.conf.json` (config)
- `src-tauri/tauri.linux.conf.json` (config)
- `src-tauri/tauri.macos.conf.json` (config)
- `src/locales/en-US/tips.json` (config)
- `src/locales/en-US/translation.json` (config)
- `src/locales/zh-CN/tips.json` (config)
- `src/locales/zh-CN/translation.json` (config)
- `src/locales/zh-HK/tips.json` (config)
- `src/locales/zh-HK/translation.json` (config)
- `tsconfig.json` (config)
- `tsconfig.node.json` (config)

## Top-level layout

- `src` — 86 analysed file(s)
- `src-tauri` — 39 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 11 analysed file(s)
- `scripts` — 11 analysed file(s)
- `Docs` — 7 analysed file(s)
- `.husky` — 1 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8b624e0b1dc38ea66d0fcea83fd4e3117d63d8c3` is the revision these paths and observations refer to.
