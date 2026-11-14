# Project structure: evolus/pencil

**Analysed commit:** `3fc5856b60415068259a8916d17a14adcd6ecc7a`

**Commit reference:** [3fc5856b60415068259a8916d17a14adcd6ecc7a](https://github.com/evolus/pencil/commit/3fc5856b60415068259a8916d17a14adcd6ecc7a)

**Tree at this commit:** [evolus/pencil@3fc5856b6041](https://github.com/evolus/pencil/tree/3fc5856b60415068259a8916d17a14adcd6ecc7a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | evolus/pencil |
| Description | The Pencil Project's unique mission is to build a free and opensource tool for making diagrams and GUI prototyping that everyone can use.  |
| Stars | 9914 |
| Forks | 795 |
| Licence | GPL-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `3fc5856b60415068259a8916d17a14adcd6ecc7a` |
| Retrieved at | 2026-11-14T19:12:48.388021+00:00 |
| Files in this snapshot | 633 |

## Directory tree

```text
RELEASE/  (3 files)
  RELEASE-NOTE-310.md
  RELEASE-NOTE-311.md
  RELEASE-NOTE-400.md
app/  (617 files)
  archive/  (84 files)
    bindings/  (31 files)
      … 31 files under this directory
    stencil/  (9 files)
      … 9 files under this directory
    aboutDialog.js
    aboutDialog.xul
    androidSupportOverlay.xul
    borderToolOverlay.xul
    clipartBrowser.xul
    colorToolOverlay.xul
    exportWizard.js
    exportWizard.xul
    firefoxOverlay.js
    firefoxOverlay.xul
    innershadow.patch
    installRemoteCollectionsDialog.js
    installRemoteCollectionsDialog.xul
    main.js
    mainWindow.js
    mainWindow.xul
    mainWindow_old.js
    messageDialog.js
    messageDialog.xul
    pageDetailDialog.js
    pageDetailDialog.xul
    pageNoteDialog.js
    pageNoteDialog.xul
    port.xhtml
    … 20 more files
  css/  (15 files)
    bootstrap-fix.less
    bootstrap-wrapper.css
    bootstrap-wrapper.less
    canvas.css
    common.less
    dialog.less
    form.less
    layout.less
    less-watch.sh
    material-icons.css
    pencil.css
    pencil.less
    theme.css
    theme.less
    variables.less
  fonts/  (1 files)
    core/  (1 files)
      … 1 files under this directory
  lib/  (125 files)
    bootstrap/  (73 files)
      … 73 files under this directory
    codemirror/  (4 files)
      … 4 files under this directory
    font-awesome-4.4.0/  (28 files)
      … 28 files under this directory
    widget/  (18 files)
      … 18 files under this directory
    common-dom.js
    loader.js
  pencil-core/  (149 files)
    behavior/  (3 files)
      … 3 files under this directory
    canvasHelper/  (7 files)
      … 7 files under this directory
    clipartBrowser/  (5 files)
      … 5 files under this directory
    common/  (45 files)
      … 45 files under this directory
    definition/  (9 files)
      … 9 files under this directory
    document/  (4 files)
      … 4 files under this directory
    editor/  (14 files)
      … 14 files under this directory
    exporter/  (10 files)
      … 10 files under this directory
    n-patch/  (3 files)
      … 3 files under this directory
    privateCollection/  (4 files)
      … 4 files under this directory
    propertyType/  (18 files)
      … 18 files under this directory
    templates/  (19 files)
      … 19 files under this directory
    xferHelper/  (6 files)
      … 6 files under this directory
    blank.html
    editor-blank.html
  stencils/  (12 files)
    Annotation/  (2 files)
      … 2 files under this directory
    BasicWebElements/  (2 files)
      … 2 files under this directory
    Common/  (1 files)
      … 1 files under this directory
    ExtJSKitchenSink_Neptune/  (1 files)
      … 1 files under this directory
    Gtk.GUI/  (1 files)
      … 1 files under this directory
    Prototype_GUI/  (1 files)
      … 1 files under this directory
    SketchyGUI/  (1 files)
      … 1 files under this directory
    TemplateDesign/  (1 files)
      … 1 files under this directory
    WindowsXP-GUI/  (1 files)
      … 1 files under this directory
    out.txt
  theme/  (1 files)
    default/  (1 files)
      … 1 files under this directory
  tools/  (33 files)
    mcp/  (26 files)
      … 26 files under this directory
    api-server.js
    capture-services.js
    color-picker-window.js
    color-picker-window.xhtml
    global-shortcut-main.js
    global-shortcut.js
    screenshot-renderer.js
  views/  (184 files)
    collections/  (27 files)
      … 27 files under this directory
    common/  (35 files)
      … 35 files under this directory
    editors/  (61 files)
      … 61 files under this directory
    menus/  (6 files)
      … 6 files under this directory
    toolbars/  (13 files)
      … 13 files under this directory
    tools/  (30 files)
      … 30 files under this directory
    AboutDialog.js
    AboutDialog.xhtml
    ApplicationPane.js
    ApplicationPane.xhtml
    EditPageNoteDialog.js
    EditPageNoteDialog.xhtml
    ExportDialog.js
    ExportDialog.xhtml
    PageDetailDialog.js
    PageDetailDialog.xhtml
    StartUpDocumentView.js
    StartUpDocumentView.xhtml
  app.js
  app.xhtml
  app_.xhtml
  blank.xhtml
  desktop.js
  dnd.html
  index.js
  license.txt
  package.json
  renderer.xhtml
  screenshot.xhtml
  test.xhtml
  updater.js
.buildignore
.editorconfig
.gitattributes
.gitignore
.gitlab-ci.yml
.project
.travis.yml
ISSUE_TEMPLATE.md
LICENSE.md
README.md
appveyor.yml
package.json
version.json
```

## Entry points

- [app/index.js](https://github.com/evolus/pencil/blob/3fc5856b60415068259a8916d17a14adcd6ecc7a/app/index.js)
- [app/app.js](https://github.com/evolus/pencil/blob/3fc5856b60415068259a8916d17a14adcd6ecc7a/app/app.js)
- [app/archive/main.js](https://github.com/evolus/pencil/blob/3fc5856b60415068259a8916d17a14adcd6ecc7a/app/archive/main.js)
- [app/tools/mcp/index.js](https://github.com/evolus/pencil/blob/3fc5856b60415068259a8916d17a14adcd6ecc7a/app/tools/mcp/index.js)
- [app/tools/mcp/server.js](https://github.com/evolus/pencil/blob/3fc5856b60415068259a8916d17a14adcd6ecc7a/app/tools/mcp/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 102 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 194 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.gitlab-ci.yml` (ci)
- `.travis.yml` (ci)
- `app/lib/bootstrap/.csscomb.json` (config)
- `app/package.json` (manifest)
- `app/tools/mcp/kb/pencil/package.json` (manifest)
- `appveyor.yml` (config)
- `package.json` (manifest)
- `version.json` (config)

## Top-level layout

- `app` — 617 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `RELEASE` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (3 x generated/minified file excluded; 2 x lockfile excluded; 4 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3fc5856b60415068259a8916d17a14adcd6ecc7a` is the revision these paths and observations refer to.
