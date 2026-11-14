# Project structure: anvaka/city-roads

**Analysed commit:** `4677b4e146190697c8d96d6ab901c7ac90fc633a`

**Commit reference:** [4677b4e146190697c8d96d6ab901c7ac90fc633a](https://github.com/anvaka/city-roads/commit/4677b4e146190697c8d96d6ab901c7ac90fc633a)

**Tree at this commit:** [anvaka/city-roads@4677b4e14619](https://github.com/anvaka/city-roads/tree/4677b4e146190697c8d96d6ab901c7ac90fc633a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | anvaka/city-roads |
| Description | Visualization of all roads within any city |
| Stars | 9821 |
| Forks | 761 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `4677b4e146190697c8d96d6ab901c7ac90fc633a` |
| Retrieved at | 2026-11-14T19:12:52.559615+00:00 |
| Files in this snapshot | 54 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
src/  (40 files)
  components/  (13 files)
    vue3-color/  (8 files)
      … 8 files under this directory
    ColorPicker.vue
    EditableLabel.vue
    FindPlace.vue
    LoadingIcon.vue
    clickOutside.js
  lib/  (17 files)
    BoundingBox.js
    Grid.js
    GridLayer.js
    LoadOptions.js
    Progress.js
    Query.js
    appState.js
    bus.js
    canvas2BlobPolyfill.js
    createScene.js
    findBoundaryByName.js
    getZazzleLink.js
    postData.js
    protobufExport.js
    request.js
    saveFile.js
    svgExport.js
  proto/  (4 files)
    decode.js
    encode.js
    place.js
    place.proto
  App.vue
  NoWebGL.vue
  config.js
  createOverlayManager.js
  main.js
  vars.styl
static/  (1 files)
  .gitkeep
.editorconfig
.eslintignore
.eslintrc.cjs
.gitignore
API.md
LICENSE
README.md
babel.config.js
deploy.sh
index.html
package.json
vite.config.js
```

## Entry points

- [src/main.js](https://github.com/anvaka/city-roads/blob/4677b4e146190697c8d96d6ab901c7ac90fc633a/src/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.vue package | library | Observed | Groups 1 file(s) under app.vue package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 12 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| createOverlayManager.js package | library | Observed | Groups 1 file(s) under createoverlaymanager.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 17 file(s) under lib package (observed from repository paths and static analysis). |
| main.js package | library | Observed | Groups 1 file(s) under main.js package (observed from repository paths and static analysis). |
| NoWebGL.vue package | library | Observed | Groups 1 file(s) under nowebgl.vue package (observed from repository paths and static analysis). |
| proto package | library | Observed | Groups 3 file(s) under proto package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 40 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 1 analysed file(s)
- `static` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4677b4e146190697c8d96d6ab901c7ac90fc633a` is the revision these paths and observations refer to.
