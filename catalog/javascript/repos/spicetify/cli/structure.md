# Project structure: spicetify/cli

**Analysed commit:** `867df4af012a07f0b9d5c6b4bc8d7c29badb8ca9`

**Commit reference:** [867df4af012a07f0b9d5c6b4bc8d7c29badb8ca9](https://github.com/spicetify/cli/commit/867df4af012a07f0b9d5c6b4bc8d7c29badb8ca9)

**Tree at this commit:** [spicetify/cli@867df4af012a](https://github.com/spicetify/cli/tree/867df4af012a07f0b9d5c6b4bc8d7c29badb8ca9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | spicetify/cli |
| Description | Command-line tool to customize Spotify client. Supports Windows, macOS, and Linux. |
| Stars | 25510 |
| Forks | 1010 |
| Licence | LGPL-2.1 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `867df4af012a07f0b9d5c6b4bc8d7c29badb8ca9` |
| Retrieved at | 2026-11-14T19:10:59.860003+00:00 |
| Files in this snapshot | 132 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (4 files)
    build.yml
    labeler.yml
    linter.yml
    lintpr.yml
  dependabot.yml
  labeler.yml
.vscode/  (2 files)
  extensions.json
  settings.json
CustomApps/  (32 files)
  lyrics-plus/  (17 files)
    Lyricsfile.js
    OptionsMenu.js
    Pages.js
    PlaybarButton.js
    ProviderGenius.js
    ProviderLRCLIB.js
    ProviderLRCRed.js
    ProviderNetease.js
    Providers.js
    README.md
    Settings.js
    TabBar.js
    Translator.js
    Utils.js
    index.js
    manifest.json
    style.css
  new-releases/  (6 files)
    Card.js
    Icons.js
    Settings.js
    index.js
    manifest.json
    style.css
  reddit/  (9 files)
    Card.js
    Icons.js
    OptionsMenu.js
    Settings.js
    SortBox.js
    TabBar.js
    index.js
    manifest.json
    style.css
Extensions/  (10 files)
  autoSkipExplicit.js
  autoSkipVideo.js
  bookmark.js
  fullAppDisplay.js
  keyboardShortcut.js
  loopyLoop.js
  popupLyrics.js
  shuffle+.js
  trashbin.js
  webnowplaying.js
Themes/  (2 files)
  SpicetifyDefault/  (2 files)
    color.ini
    user.css
jsHelper/  (3 files)
  expFeatures.js
  homeConfig.js
  sidebarConfig.js
scripts/  (2 files)
  build-wrapper.mjs
  update-cssmap.mjs
src/  (59 files)
  apply/  (1 files)
    apply.go
  backup/  (1 files)
    backup.go
  cmd/  (15 files)
    apply.go
    auto.go
    backup.go
    block-updates.go
    cmd.go
    color.go
    config-dir.go
    config.go
    devtools.go
    patch.go
    path.go
    permissions.go
    restart.go
    update.go
    watch.go
  jsHelper/  (27 files)
    spicetifyWrapper/  (27 files)
      … 27 files under this directory
  preprocess/  (1 files)
    preprocess.go
  status/  (2 files)
    backup/  (1 files)
      … 1 files under this directory
    spotify/  (1 files)
      … 1 files under this directory
  utils/  (12 files)
    isAdmin/  (2 files)
      … 2 files under this directory
    color.go
    config.go
    file-utils.go
    path-utils.go
    print.go
    scanner.go
    show-dir.go
    utils.go
    vcs.go
    watcher.go
.coderabbit.yaml
.gitignore
.oxfmtrc.json
.oxlintrc.json
CONTRIBUTING.md
LICENSE
README.md
globals.d.ts
go.mod
go.sum
install.ps1
install.sh
manifest.json
package.json
pnpm-workspace.yaml
spicetify.go
```

## Entry points

- [CustomApps/lyrics-plus/index.js](https://github.com/spicetify/cli/blob/867df4af012a07f0b9d5c6b4bc8d7c29badb8ca9/CustomApps/lyrics-plus/index.js)
- [CustomApps/new-releases/index.js](https://github.com/spicetify/cli/blob/867df4af012a07f0b9d5c6b4bc8d7c29badb8ca9/CustomApps/new-releases/index.js)
- [CustomApps/reddit/index.js](https://github.com/spicetify/cli/blob/867df4af012a07f0b9d5c6b4bc8d7c29badb8ca9/CustomApps/reddit/index.js)
- [src/jsHelper/spicetifyWrapper/index.js](https://github.com/spicetify/cli/blob/867df4af012a07f0b9d5c6b4bc8d7c29badb8ca9/src/jsHelper/spicetifyWrapper/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apply package | library | Observed | Groups 1 file(s) under apply package (observed from repository paths and static analysis). |
| backup package | library | Observed | Groups 1 file(s) under backup package (observed from repository paths and static analysis). |
| cmd package | library | Observed | Groups 15 file(s) under cmd package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| CustomApps package | library | Observed | Groups 25 file(s) under customapps package (observed from repository paths and static analysis). |
| Extensions package | library | Observed | Groups 10 file(s) under extensions package (observed from repository paths and static analysis). |
| jsHelper package | library | Observed | Groups 30 file(s) under jshelper package (observed from repository paths and static analysis). |
| preprocess package | library | Observed | Groups 1 file(s) under preprocess package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| status package | library | Observed | Groups 2 file(s) under status package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 12 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.coderabbit.yaml` (config)
- `.github/dependabot.yml` (config)
- `.github/labeler.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/labeler.yml` (ci)
- `.github/workflows/linter.yml` (ci)
- `.github/workflows/lintpr.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `CustomApps/lyrics-plus/manifest.json` (config)
- `CustomApps/new-releases/manifest.json` (config)
- `CustomApps/reddit/manifest.json` (config)
- `Themes/SpicetifyDefault/color.ini` (config)
- `go.mod` (manifest)
- `manifest.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)

## Top-level layout

- `src` — 59 analysed file(s)
- `CustomApps` — 32 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `Extensions` — 10 analysed file(s)
- `.github` — 6 analysed file(s)
- `jsHelper` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `Themes` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `867df4af012a07f0b9d5c6b4bc8d7c29badb8ca9` is the revision these paths and observations refer to.
