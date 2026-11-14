# Project structure: XxHuberrr/Mineradio-paused

**Analysed commit:** `649c787d22fd283b5431899eca3ee6a509319247`

**Commit reference:** [649c787d22fd283b5431899eca3ee6a509319247](https://github.com/XxHuberrr/Mineradio-paused/commit/649c787d22fd283b5431899eca3ee6a509319247)

**Tree at this commit:** [XxHuberrr/Mineradio-paused@649c787d22fd](https://github.com/XxHuberrr/Mineradio-paused/tree/649c787d22fd283b5431899eca3ee6a509319247)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | XxHuberrr/Mineradio-paused |
| Description | Mineradio 官网：mineradio.cn ｜ 一款以电影镜头、粒子视觉和歌词舞台为核心的沉浸式音乐播放器。 |
| Stars | 11423 |
| Forks | 899 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `649c787d22fd283b5431899eca3ee6a509319247` |
| Retrieved at | 2026-11-14T19:12:19.165682+00:00 |
| Files in this snapshot | 254 |

## Directory tree

```text
cuefield/  (19 files)
  adapter-mineradio.js
  boundary-evidence.js
  bridge-planner.js
  cue-profile.js
  feedback-log.js
  lrc-anchors.js
  lyric-link.js
  mineradio-bridge.js
  musical-profile.js
  planner-contracts.js
  recipe-planner.js
  section-candidates.js
  shadow-diagnostics.js
  structure-map.js
  transition-artifact.js
  transition-evaluator.js
  transition-router.js
  transition-window-planner.js
  version.js
desktop/  (14 files)
  app-memory.js
  built-in-playlist-library.js
  desktop-icon-shape-runtime.js
  desktop-native-icon-layer-runtime.js
  full-desktop-mode-runtime.js
  local-music-library.js
  login-easter-egg-gate.js
  overlay-preload.js
  preload.js
  startup.html
  system-memory.js
  wallpaper-engine-library.js
  wallpaper-engine-runtime.js
  wallpaper-mode-runtime.js
docs/  (11 files)
  update/  (1 files)
    latest.yml
  3D_PLAYLIST_SHELF_MEMORY.md
  DESKTOP_LYRICS_VISUAL.md
  GLASS_SVG_TEXTURE.md
  INSTALLER_STYLE.md
  LOW_SPEC_OPTIMIZATION_DOCTRINE.md
  RELEASE_NOTES_v1.1.0.md
  RELEASE_NOTES_v2.2.0.md
  SUPPORT.md
  THIRD_PARTY_PORTS.md
  UPDATE_DELIVERY.md
public/  (110 files)
  js/  (105 files)
    modules/  (103 files)
      … 103 files under this directory
    index-loader.js
    preload-mode.js
  default-user-fx-archive.json
  desktop-lyrics.html
  index.html
  sonic-topography-preset.js
  sonic-workshop-preset.js
qishui-audio-decryptor/  (3 files)
  decrypt-utils.js
  mp4-box.js
  track-decryptor.js
qishui-auth-v6/  (5 files)
  react-dom.js
  react.js
  sdk-glue.js
  security_host.html
  security_seed.html
scripts/  (19 files)
  check-desktop-icon-lock-live.js
  check-desktop-keyboard-focus-live.js
  check-wallpaper-engine-audio-session.ps1
  check-wallpaper-engine-dwm-thumbnail.ps1
  check-wallpaper-engine-host-move-helper.js
  check-wallpaper-engine-library.js
  check-wallpaper-engine-lifecycle.js
  check-wallpaper-engine-live-scene.js
  check-wallpaper-engine-live-ui.js
  check-wallpaper-engine-normal-user.js
  check-wallpaper-engine-property-command.js
  check-wallpaper-engine-runtime.js
  check-wallpaper-engine-window-list.ps1
  check-wallpaper-mode-live.js
  check-wallpaper-mode-window-tree.ps1
  diagnose-wallpaper-engine-pointer-target.js
  list-wallpaper-engine-capture-sources.js
  read-wallpaper-engine-dwm-state.js
  sync-current-fx-default-archive.js
tests/  (53 files)
  fixtures/  (1 files)
    update-three-cloud-pages.json
  built-in-playlist-library.test.js
  cuefield-electron-smoke.js
  cuefield-mineradio-integration.test.js
  cuefield-transition-runtime.test.js
  curated-visual-presets.test.js
  desktop-icon-shape-runtime.test.js
  desktop-native-icon-layer-runtime.test.js
  external-update-page-bridge.test.js
  full-desktop-mode-runtime.test.js
  gesture-camera-permission.test.js
  gesture-player-actions.test.js
  gesture-runtime-lifecycle.test.js
  home-daily-recommendation-virtualization.test.js
  home-daily-recommendations-backend.test.js
  home-dashboard-update.test.js
  home-hero-mp4-platform-recommend.test.js
  kugou-api-resilience.test.js
  kugou-login-bridge.test.js
  kugou-vip-hardening.test.js
  local-music-library-persistence.test.js
  login-easter-egg-gate.test.js
  login-easter-egg-ime-focus.test.js
  lyric-active-line-viewport-fit.test.js
  main-window-runtime-recovery.test.js
  … 28 more files
.gitattributes
.gitignore
CHANGELOG.md
LICENSE
NOTICE.md
PRIVACY.md
README.md
RELEASE.md
SECURITY.md
dj-analyzer.js
electron-builder.internal-beta.json
kugou-api.js
package.json
qishui-api.js
qishui-auth-v6.js
qishui-qr-login.js
qq-vip-api.js
quick-check.bat
spotify-api.js
start-mineradio.bat
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| cuefield package | library | Observed | Groups 19 file(s) under cuefield package (observed from repository paths and static analysis). |
| desktop package | library | Observed | Groups 13 file(s) under desktop package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 107 file(s) under public package (observed from repository paths and static analysis). |
| qishui-audio-decryptor package | library | Observed | Groups 3 file(s) under qishui-audio-decryptor package (observed from repository paths and static analysis). |
| qishui-auth-v6 package | library | Observed | Groups 3 file(s) under qishui-auth-v6 package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 15 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 53 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `docs/update/latest.yml` (config)
- `electron-builder.internal-beta.json` (config)
- `package.json` (manifest)
- `public/default-user-fx-archive.json` (config)

## Top-level layout

- `public` — 110 analysed file(s)
- `tests` — 53 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `cuefield` — 19 analysed file(s)
- `scripts` — 19 analysed file(s)
- `desktop` — 14 analysed file(s)
- `docs` — 11 analysed file(s)
- `qishui-auth-v6` — 5 analysed file(s)
- `qishui-audio-decryptor` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 8 file(s) were skipped during inventory (1 x lockfile excluded; 7 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `649c787d22fd283b5431899eca3ee6a509319247` is the revision these paths and observations refer to.
