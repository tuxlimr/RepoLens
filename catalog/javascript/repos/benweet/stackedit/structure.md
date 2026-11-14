# Project structure: benweet/stackedit

**Analysed commit:** `6dce2a5e36b755a0c244522b48a06c91a2df0f59`

**Commit reference:** [6dce2a5e36b755a0c244522b48a06c91a2df0f59](https://github.com/benweet/stackedit/commit/6dce2a5e36b755a0c244522b48a06c91a2df0f59)

**Tree at this commit:** [benweet/stackedit@6dce2a5e36b7](https://github.com/benweet/stackedit/tree/6dce2a5e36b755a0c244522b48a06c91a2df0f59)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | benweet/stackedit |
| Description | In-browser Markdown editor |
| Stars | 23101 |
| Forks | 2812 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `6dce2a5e36b755a0c244522b48a06c91a2df0f59` |
| Retrieved at | 2026-11-14T19:11:05.555872+00:00 |
| Files in this snapshot | 332 |

## Directory tree

```text
chart/  (9 files)
  templates/  (6 files)
    tests/  (1 files)
      … 1 files under this directory
    NOTES.txt
    _helpers.tpl
    deployment.yaml
    ingress.yaml
    service.yaml
  .helmignore
  Chart.yaml
  values.yaml
chrome-app/  (1 files)
  manifest.json
config/  (3 files)
  dev.env.js
  index.js
  prod.env.js
server/  (6 files)
  conf.js
  github.js
  index.js
  pandoc.js
  pdf.js
  user.js
src/  (279 files)
  assets/  (12 files)
    iconBlogger.svg
    iconCouchdb.svg
    iconDropbox.svg
    iconGithub.svg
    iconGitlab.svg
    iconGoogle.svg
    iconGoogleDrive.svg
    iconGooglePhotos.svg
    iconStackedit.svg
    iconWordpress.svg
    iconZendesk.svg
    logo.svg
  components/  (84 files)
    common/  (3 files)
      … 3 files under this directory
    gutters/  (7 files)
      … 7 files under this directory
    menus/  (8 files)
      … 8 files under this directory
    modals/  (46 files)
      … 46 files under this directory
    App.vue
    ButtonBar.vue
    CodeEditor.vue
    ContextMenu.vue
    Editor.vue
    Explorer.vue
    ExplorerNode.vue
    FindReplace.vue
    Layout.vue
    Modal.vue
    NavigationBar.vue
    Notification.vue
    Preview.vue
    SideBar.vue
    SplashScreen.vue
    StatusBar.vue
    Toc.vue
    Tour.vue
    UserImage.vue
    UserName.vue
  data/  (25 files)
    defaults/  (4 files)
      … 4 files under this directory
    empties/  (9 files)
      … 9 files under this directory
    templates/  (4 files)
      … 4 files under this directory
    constants.js
    faq.md
    features.js
    markdownSample.md
    pagedownButtons.js
    presets.js
    simpleModals.js
    welcomeFile.md
  extensions/  (9 files)
    libs/  (3 files)
      … 3 files under this directory
    abcExtension.js
    emojiExtension.js
    index.js
    katexExtension.js
    markdownExtension.js
    mermaidExtension.js
  icons/  (58 files)
    Alert.vue
    ArrowLeft.vue
    CheckCircle.vue
    Close.vue
    CodeBraces.vue
    CodeTags.vue
    ContentCopy.vue
    ContentSave.vue
    Database.vue
    Delete.vue
    DotsHorizontal.vue
    Download.vue
    Eye.vue
    FileImage.vue
    FileMultiple.vue
    FilePlus.vue
    Folder.vue
    FolderMultiple.vue
    FolderPlus.vue
    FormatBold.vue
    FormatItalic.vue
    FormatListBulleted.vue
    FormatListChecks.vue
    FormatListNumbers.vue
    … 34 more files
  libs/  (3 files)
    clunderscore.js
    htmlSanitizer.js
    pagedown.js
  services/  (61 files)
    editor/  (12 files)
      … 12 files under this directory
    optional/  (5 files)
      … 5 files under this directory
    providers/  (23 files)
      … 23 files under this directory
    animationSvc.js
    backupSvc.js
    badgeSvc.js
    diffUtils.js
    editorSvc.js
    explorerSvc.js
    exportSvc.js
    extensionSvc.js
    gitWorkspaceSvc.js
    localDbSvc.js
    markdownConversionSvc.js
    markdownGrammarSvc.js
    networkSvc.js
    publishSvc.js
    syncSvc.js
    tempFileSvc.js
    templateWorker.js
    timeSvc.js
    userSvc.js
    utils.js
    workspaceSvc.js
  store/  (19 files)
    content.js
    contentState.js
    contextMenu.js
    data.js
    discussion.js
    explorer.js
    file.js
    findReplace.js
    folder.js
    index.js
    layout.js
    locationTemplate.js
    modal.js
    moduleTemplate.js
    notification.js
    queue.js
    syncedContent.js
    userInfo.js
    workspace.js
  styles/  (7 files)
    app.scss
    base.scss
    fonts.scss
    index.js
    markdownHighlighting.scss
    prism.scss
    variables.scss
  index.js
static/  (4 files)
  landing/  (2 files)
    index.html
    logo.svg
  oauth2/  (1 files)
    callback.html
  sitemap.xml
test/  (14 files)
  unit/  (14 files)
    mocks/  (4 files)
      … 4 files under this directory
    specs/  (7 files)
      … 7 files under this directory
    .eslintrc
    jest.conf.js
    setup.js
.babelrc
.dockerignore
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.postcssrc.js
.stylelintrc
.travis.yml
Dockerfile
LICENSE
README.md
gulpfile.js
index.html
index.js
package.json
```

## Entry points

- [index.js](https://github.com/benweet/stackedit/blob/6dce2a5e36b755a0c244522b48a06c91a2df0f59/index.js)
- [config/index.js](https://github.com/benweet/stackedit/blob/6dce2a5e36b755a0c244522b48a06c91a2df0f59/config/index.js)
- [server/index.js](https://github.com/benweet/stackedit/blob/6dce2a5e36b755a0c244522b48a06c91a2df0f59/server/index.js)
- [src/extensions/index.js](https://github.com/benweet/stackedit/blob/6dce2a5e36b755a0c244522b48a06c91a2df0f59/src/extensions/index.js)
- [src/icons/index.js](https://github.com/benweet/stackedit/blob/6dce2a5e36b755a0c244522b48a06c91a2df0f59/src/icons/index.js)
- [src/index.js](https://github.com/benweet/stackedit/blob/6dce2a5e36b755a0c244522b48a06c91a2df0f59/src/index.js)
- [src/services/optional/index.js](https://github.com/benweet/stackedit/blob/6dce2a5e36b755a0c244522b48a06c91a2df0f59/src/services/optional/index.js)
- [src/store/index.js](https://github.com/benweet/stackedit/blob/6dce2a5e36b755a0c244522b48a06c91a2df0f59/src/store/index.js)
- [src/styles/index.js](https://github.com/benweet/stackedit/blob/6dce2a5e36b755a0c244522b48a06c91a2df0f59/src/styles/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 84 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 16 file(s) under data layer (observed from repository paths and static analysis). |
| extensions package | library | Observed | Groups 9 file(s) under extensions package (observed from repository paths and static analysis). |
| icons package | library | Observed | Groups 58 file(s) under icons package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 3 file(s) under libs package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 6 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 61 file(s) under service / domain layer (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 19 file(s) under store package (observed from repository paths and static analysis). |
| styles package | library | Observed | Groups 1 file(s) under styles package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 15 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `chart/Chart.yaml` (config)
- `chart/templates/deployment.yaml` (config)
- `chart/templates/ingress.yaml` (config)
- `chart/templates/service.yaml` (config)
- `chart/values.yaml` (config)
- `chrome-app/manifest.json` (config)
- `package.json` (manifest)
- `src/data/defaults/defaultSettings.yml` (config)

## Top-level layout

- `src` — 279 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `test` — 14 analysed file(s)
- `chart` — 9 analysed file(s)
- `server` — 6 analysed file(s)
- `static` — 4 analysed file(s)
- `config` — 3 analysed file(s)
- `chrome-app` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 11 file(s) were skipped during inventory (11 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6dce2a5e36b755a0c244522b48a06c91a2df0f59` is the revision these paths and observations refer to.
