# Project structure: GitSquared/edex-ui

**Analysed commit:** `04a00c4079908788b371c6ecdefff96d0d9950f8`

**Commit reference:** [04a00c4079908788b371c6ecdefff96d0d9950f8](https://github.com/GitSquared/edex-ui/commit/04a00c4079908788b371c6ecdefff96d0d9950f8)

**Tree at this commit:** [GitSquared/edex-ui@04a00c407990](https://github.com/GitSquared/edex-ui/tree/04a00c4079908788b371c6ecdefff96d0d9950f8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | GitSquared/edex-ui |
| Description | A cross-platform, customizable science fiction terminal emulator with advanced monitoring & touchscreen support. |
| Stars | 45041 |
| Forks | 3231 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `04a00c4079908788b371c6ecdefff96d0d9950f8` |
| Retrieved at | 2026-11-14T19:10:39.037549+00:00 |
| Files in this snapshot | 99 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    config.yml
    issue_template.md
  workflows/  (2 files)
    build-binaries.yaml
    codeql-analysis.yml
  FUNDING.yml
media/  (1 files)
  logo.svg
src/  (85 files)
  assets/  (62 files)
    css/  (20 files)
      … 20 files under this directory
    kb_layouts/  (19 files)
      … 19 files under this directory
    misc/  (2 files)
      … 2 files under this directory
    themes/  (21 files)
      … 21 files under this directory
  classes/  (18 files)
    audiofx.class.js
    clock.class.js
    conninfo.class.js
    cpuinfo.class.js
    docReader.class.js
    filesystem.class.js
    fuzzyFinder.class.js
    hardwareInspector.class.js
    keyboard.class.js
    locationGlobe.class.js
    mediaPlayer.class.js
    modal.class.js
    netstat.class.js
    ramwatcher.class.js
    sysinfo.class.js
    terminal.class.js
    toplist.class.js
    updateChecker.class.js
  _boot.js
  _multithread.js
  _renderer.js
  package.json
  ui.html
.gitignore
.gitmodules
LICENSE
README.md
SECURITY.md
file-icons-generator.js
package.json
prebuild-minify.js
```

## Entry points

- [src/_boot.js](https://github.com/GitSquared/edex-ui/blob/04a00c4079908788b371c6ecdefff96d0d9950f8/src/_boot.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| _boot.js package | library | Observed | Groups 1 file(s) under _boot.js package (observed from repository paths and static analysis). |
| classes package | library | Observed | Groups 18 file(s) under classes package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 42 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| _multithread.js package | library | Observed | Groups 1 file(s) under _multithread.js package (observed from repository paths and static analysis). |
| _renderer.js package | library | Observed | Groups 1 file(s) under _renderer.js package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/build-binaries.yaml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `package.json` (manifest)
- `src/assets/kb_layouts/da-DK.json` (config)
- `src/assets/kb_layouts/de-DE.json` (config)
- `src/assets/kb_layouts/en-COLEMAK.json` (config)
- `src/assets/kb_layouts/en-DVORAK.json` (config)
- `src/assets/kb_layouts/en-GB.json` (config)
- `src/assets/kb_layouts/en-NORMAN.json` (config)
- `src/assets/kb_layouts/en-US.json` (config)
- `src/assets/kb_layouts/en-WORKMAN.json` (config)
- `src/assets/kb_layouts/es-ES.json` (config)
- `src/assets/kb_layouts/es-LAT.json` (config)
- `src/assets/kb_layouts/fr-BEPO.json` (config)
- `src/assets/kb_layouts/fr-FR.json` (config)
- `src/assets/kb_layouts/hu-HU.json` (config)
- `src/assets/kb_layouts/it-IT.json` (config)
- `src/assets/kb_layouts/nl-BE.json` (config)
- `src/assets/kb_layouts/pt-BR.json` (config)
- `src/assets/kb_layouts/sv-SE.json` (config)
- `src/assets/kb_layouts/tr-TR-F.json` (config)
- `src/assets/kb_layouts/tr-TR-Q.json` (config)
- `src/assets/themes/apollo-notype.json` (config)
- `src/assets/themes/apollo.json` (config)
- `src/assets/themes/blade.json` (config)
- `src/assets/themes/chalkboard-ligatures.json` (config)
- `src/assets/themes/chalkboard-notype.json` (config)
- `src/assets/themes/chalkboard.json` (config)
- `src/assets/themes/cyborg-focus.json` (config)
- `src/assets/themes/cyborg.json` (config)
- `src/assets/themes/interstellar.json` (config)
- `src/assets/themes/matrix.json` (config)
- `src/assets/themes/navy-disrupted.json` (config)
- `src/assets/themes/navy-notype.json` (config)
- `src/assets/themes/navy.json` (config)
- `src/assets/themes/nord.json` (config)
- `src/assets/themes/red.json` (config)
- `src/assets/themes/tron-colorfilter.json` (config)
- `src/assets/themes/tron-disrupted.json` (config)
- `src/assets/themes/tron-fulltype.json` (config)
- `src/assets/themes/tron-notype.json` (config)
- `src/assets/themes/tron-typeleft.json` (config)
- `src/assets/themes/tron.json` (config)
- `src/package.json` (manifest)

## Top-level layout

- `src` — 85 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 5 analysed file(s)
- `media` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `04a00c4079908788b371c6ecdefff96d0d9950f8` is the revision these paths and observations refer to.
