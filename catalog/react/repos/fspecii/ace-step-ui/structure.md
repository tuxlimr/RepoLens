# Project structure: fspecii/ace-step-ui

**Analysed commit:** `a1fdf91829ec6f7b98844f80e323529cd155dbf2`

**Commit reference:** [a1fdf91829ec6f7b98844f80e323529cd155dbf2](https://github.com/fspecii/ace-step-ui/commit/a1fdf91829ec6f7b98844f80e323529cd155dbf2)

**Tree at this commit:** [fspecii/ace-step-ui@a1fdf91829ec](https://github.com/fspecii/ace-step-ui/tree/a1fdf91829ec6f7b98844f80e323529cd155dbf2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fspecii/ace-step-ui |
| Description | 🎵 The Ultimate Open Source Suno Alternative - Professional UI for ACE-Step 1.5 AI Music Generation. Free, local, unlimited. Stop paying for Suno! |
| Stars | 5218 |
| Forks | 802 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `a1fdf91829ec6f7b98844f80e323529cd155dbf2` |
| Retrieved at | 2026-11-14T19:14:24.839729+00:00 |
| Files in this snapshot | 166 |

## Directory tree

```text
audiomass-editor/  (36 files)
  src/  (35 files)
    fonts/  (1 files)
      … 1 files under this directory
    about.html
    actions.js
    app.js
    audiomass-server.go
    audiomass-server.py
    audiomass-url-patch.js
    audiomass.appcache
    contextmenu.js
    drag.js
    engine.js
    eq.html
    flac.js
    fx-auto.js
    fx-pg-eq.js
    id3.js
    index-cache.html
    index.html
    keys.js
    local.js
    lz4-block-codec-wasm.js
    lzma.js
    main.css
    manifest.json
    modal.js
    … 10 more files
  README.md
components/  (24 files)
  AlbumCover.tsx
  ConfirmDialog.tsx
  CreatePanel.tsx
  EditProfileModal.tsx
  EditableSlider.tsx
  LibraryView.tsx
  MobileDrawer.tsx
  NewsPage.tsx
  Player.tsx
  PlaylistDetail.tsx
  PlaylistModals.tsx
  RightSidebar.tsx
  SearchPage.tsx
  SettingsModal.tsx
  ShareModal.tsx
  Sidebar.tsx
  SongDropdownMenu.tsx
  SongList.tsx
  SongProfile.tsx
  Toast.tsx
  TrainingPanel.tsx
  UserProfile.tsx
  UsernameModal.tsx
  VideoGeneratorModal.tsx
context/  (3 files)
  AuthContext.tsx
  I18nContext.tsx
  ResponsiveContext.tsx
data/  (4 files)
  all_style.txt
  genres.ts
  main_style.txt
  news.json
i18n/  (1 files)
  translations.ts
server/  (75 files)
  audio-editor/  (35 files)
    fonts/  (1 files)
      … 1 files under this directory
    about.html
    actions.js
    app.js
    audiomass-server.go
    audiomass-server.py
    audiomass-url-patch.js
    audiomass.appcache
    contextmenu.js
    drag.js
    engine.js
    eq.html
    flac.js
    fx-auto.js
    fx-pg-eq.js
    id3.js
    index-cache.html
    index.html
    keys.js
    local.js
    lz4-block-codec-wasm.js
    lzma.js
    main.css
    manifest.json
    modal.js
    … 10 more files
  data/  (1 files)
    .gitkeep
  public/  (7 files)
    audio/  (1 files)
      … 1 files under this directory
    demucs-web/  (6 files)
      … 6 files under this directory
  scripts/  (4 files)
    format_sample.py
    get_limits.py
    preprocess_dataset.py
    simple_generate.py
  src/  (24 files)
    config/  (1 files)
      … 1 files under this directory
    db/  (3 files)
      … 3 files under this directory
    middleware/  (1 files)
      … 1 files under this directory
    routes/  (9 files)
      … 9 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    services/  (7 files)
      … 7 files under this directory
    index.ts
  .env.example
  .gitignore
  package.json
  tsconfig.json
services/  (2 files)
  api.ts
  geminiService.ts
.env.example
.gitignore
App.tsx
I18N_USAGE.md
README.md
global.d.ts
index.html
index.tsx
metadata.json
package.json
setup.bat
setup.sh
start-all.bat
start-all.sh
start.bat
start.sh
stop-all.sh
tsconfig.json
types.ts
vite-env.d.ts
vite.config.ts
```

## Entry points

- [server/scripts/format_sample.py:172](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/server/scripts/format_sample.py#L172)
- [server/scripts/get_limits.py:24](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/server/scripts/get_limits.py#L24)
- [server/scripts/preprocess_dataset.py:139](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/server/scripts/preprocess_dataset.py#L139)
- [server/scripts/simple_generate.py:290](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/server/scripts/simple_generate.py#L290)
- [App.tsx](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/App.tsx)
- [audiomass-editor/src/app.js](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/audiomass-editor/src/app.js)
- [index.tsx](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/index.tsx)
- [server/audio-editor/app.js](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/server/audio-editor/app.js)
- [server/public/demucs-web/app.js](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/server/public/demucs-web/app.js)
- [server/src/config/index.ts](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/server/src/config/index.ts)
- [server/src/index.ts](https://github.com/fspecii/ace-step-ui/blob/a1fdf91829ec6f7b98844f80e323529cd155dbf2/server/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). |
| audiomass-editor package | library | Observed | Groups 26 file(s) under audiomass-editor package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 24 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| context package | library | Observed | Groups 3 file(s) under context package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 10 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 7 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: format_input, generate, get_handlers, get_llm_handler, main. |
| i18n package | library | Observed | Groups 1 file(s) under i18n package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 35 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `audiomass-editor/src/manifest.json` (config)
- `data/news.json` (config)
- `metadata.json` (config)
- `package.json` (manifest)
- `server/.env.example` (config)
- `server/audio-editor/manifest.json` (config)
- `server/package.json` (manifest)
- `server/tsconfig.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `server` — 75 analysed file(s)
- `audiomass-editor` — 36 analysed file(s)
- `components` — 24 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `data` — 4 analysed file(s)
- `context` — 3 analysed file(s)
- `services` — 2 analysed file(s)
- `i18n` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (2 x lockfile excluded; 1 x vendored/generated directory excluded).
- File audiomass-editor/src/audiomass-server.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File server/audio-editor/audiomass-server.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a1fdf91829ec6f7b98844f80e323529cd155dbf2` is the revision these paths and observations refer to.
