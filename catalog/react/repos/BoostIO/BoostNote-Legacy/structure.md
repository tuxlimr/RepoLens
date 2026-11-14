# Project structure: BoostIO/BoostNote-Legacy

**Analysed commit:** `789926bc760628ecedbd0051ca96d190a2be234f`

**Commit reference:** [789926bc760628ecedbd0051ca96d190a2be234f](https://github.com/BoostIO/BoostNote-Legacy/commit/789926bc760628ecedbd0051ca96d190a2be234f)

**Tree at this commit:** [BoostIO/BoostNote-Legacy@789926bc7606](https://github.com/BoostIO/BoostNote-Legacy/tree/789926bc760628ecedbd0051ca96d190a2be234f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BoostIO/BoostNote-Legacy |
| Description | This repository is outdated and new Boost Note app is available! We've launched a new Boost Note app which supports real-time collaborative writing. https://github.com/BoostIO/BoostNote-App |
| Stars | 16867 |
| Forks | 1439 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `789926bc760628ecedbd0051ca96d190a2be234f` |
| Retrieved at | 2026-11-14T19:13:13.910966+00:00 |
| Files in this snapshot | 408 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
.vscode/  (2 files)
  launch.json
  tasks.json
__mocks__/  (1 files)
  electron.js
browser/  (224 files)
  components/  (35 files)
    render/  (1 files)
      … 1 files under this directory
    CodeEditor.js
    CodeEditor.styl
    ColorPicker.js
    ColorPicker.styl
    MarkdownEditor.js
    MarkdownEditor.styl
    MarkdownPreview.js
    MarkdownSplitEditor.js
    MarkdownSplitEditor.styl
    ModalEscButton.js
    ModalEscButton.styl
    NavToggleButton.js
    NavToggleButton.styl
    NoteItem.js
    NoteItem.styl
    NoteItemSimple.js
    NoteItemSimple.styl
    RealtimeNotification.js
    RealtimeNotification.styl
    SideNavFilter.js
    SideNavFilter.styl
    SnippetTab.js
    SnippetTab.styl
    StorageItem.js
    … 10 more files
  lib/  (37 files)
    CMLanguageList.js
    CSSModules.js
    Languages.js
    Mutable.js
    RcParser.js
    SnippetManager.js
    TextEditorInterface.js
    confirmDeleteNote.js
    consts.js
    context.js
    contextMenuBuilder.js
    convertModeName.js
    customMeta.js
    date-formatter.js
    findNoteTitle.js
    findStorage.js
    getTodoStatus.js
    htmlTextHelper.js
    i18n.js
    keygen.js
    markdown-it-deflist.js
    markdown-it-fence.js
    markdown-it-frontmatter.js
    markdown-it-sanitize-html.js
    … 13 more files
  main/  (139 files)
    Detail/  (32 files)
      … 32 files under this directory
    DevTools/  (3 files)
      … 3 files under this directory
    NewNoteButton/  (2 files)
      … 2 files under this directory
    NoteList/  (2 files)
      … 2 files under this directory
    SideNav/  (11 files)
      … 11 files under this directory
    StatusBar/  (2 files)
      … 2 files under this directory
    TopBar/  (2 files)
      … 2 files under this directory
    lib/  (46 files)
      … 46 files under this directory
    modals/  (34 files)
      … 34 files under this directory
    Main.js
    Main.styl
    global.styl
    index.js
    store.js
  styles/  (13 files)
    Detail/  (1 files)
      … 1 files under this directory
    mixins/  (8 files)
      … 8 files under this directory
    shared/  (1 files)
      … 1 files under this directory
    theme/  (1 files)
      … 1 files under this directory
    index.styl
    vars.styl
dev-scripts/  (1 files)
  dev.js
dictionaries/  (4 files)
  de_DE/  (2 files)
    LICENSE
    de_DE.aff
  en_GB/  (2 files)
    LICENSE
    en_GB.aff
docs/  (18 files)
  de/  (2 files)
    build.md
    debug.md
  fr/  (2 files)
    build.md
    debug.md
  jp/  (2 files)
    build.md
    debug.md
  ko/  (2 files)
    build.md
    debug.md
  pt_BR/  (2 files)
    build.md
    debug.md
  ru/  (2 files)
    build.md
    debug.md
  zh_CN/  (2 files)
    build.md
    debug.md
  zh_TW/  (1 files)
    build.md
  build.md
  code_style.md
  debug.md
extra_scripts/  (7 files)
  boost/  (1 files)
    boostNewLineIndentContinueMarkdownList.js
  codemirror/  (6 files)
    addon/  (2 files)
      … 2 files under this directory
    mode/  (3 files)
      … 3 files under this directory
    theme/  (1 files)
      … 1 files under this directory
lib/  (7 files)
  ipcServer.js
  main-app.js
  main-menu.js
  main-window.js
  main.development.html
  main.production.html
  touchbar-menu.js
locales/  (21 files)
  cs.json
  da.json
  de.json
  en.json
  es-ES.json
  fa.json
  fr.json
  hu.json
  it.json
  ja.json
  ko.json
  no.json
  pl.json
  pt-BR.json
  pt-PT.json
  ru.json
  sq.json
  th.json
  tr.json
  zh-CN.json
  zh-TW.json
resources/  (46 files)
  icon/  (46 files)
    icon-all-active.svg
    icon-all.svg
    icon-code-off.svg
    icon-code-on.svg
    icon-column-list.svg
    icon-column.svg
    icon-down.svg
    icon-edit-lock.svg
    icon-edit.svg
    icon-external.svg
    icon-full.svg
    icon-info.svg
    icon-left-to-right.svg
    icon-list-active.svg
    icon-list.svg
    icon-lock.svg
    icon-mode-markdown-off-active.svg
    icon-mode-markdown-off.svg
    icon-mode-split-on-active.svg
    icon-mode-split-on.svg
    icon-newnote.svg
    icon-note-code.svg
    icon-note-text.svg
    icon-plus.svg
    … 22 more files
snap/  (2 files)
  gui/  (1 files)
    boostnote.desktop
  snapcraft.yaml
tests/  (52 files)
  components/  (2 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    TagListItem.snapshot.test.js
  dataApi/  (22 files)
    addStorage.js
    attachmentManagement.test.js
    copyFile.test.js
    createFolder.test.js
    createNote.test.js
    createNoteFromUrl.test.js
    createSnippet.test.js
    deleteFolder.test.js
    deleteNote-test.js
    deleteSnippet-test.js
    exportFolder-test.js
    exportStorage-test.js
    init.js
    migrateFromV6Storage-test.js
    moveNote-test.js
    removeStorage-test.js
    renameStorage-test.js
    reorderFolder-test.js
    toggleStorage-test.js
    updateFolder-test.js
    updateNote-test.js
    updateSnippet-test.js
  fixtures/  (2 files)
    TestDummy.js
    markdowns.js
  helpers/  (2 files)
    setup-browser-env.js
    setup-electron-mock.js
  lib/  (21 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    boostnoterc/  (3 files)
      … 3 files under this directory
    snapshots/  (1 files)
      … 1 files under this directory
    contextMenuBuilder.test.js
    escapeHtmlCharacters.test.js
    find-storage.test.js
    find-title.test.js
    get-todo-status.test.js
    html-text-helper.test.js
    markdown-text-helper.test.js
    markdown-toc-generator.test.js
    markdown.test.js
    normalize-editor-font-family.test.js
    rc-parser.test.js
    search.test.js
    slugify.test.js
    spellcheck.test.js
    themeManager.test.js
    utils.test.js
  .gitignore
  date-formatter-test.js
  jest.js
.babelrc
.boostnoterc.sample
.editorconfig
.eslintignore
.eslintrc
.gitignore
.prettierrc
.travis.yml
FAQ.md
ISSUE_TEMPLATE.md
LICENSE
PULL_REQUEST_TEMPLATE.md
appdmg.json
contributing.md
gruntfile.js
index.js
package.json
prettier.config
readme.md
webpack-production.config.js
webpack-skeleton.js
webpack.config.js
```

## Entry points

- [index.js](https://github.com/BoostIO/BoostNote-Legacy/blob/789926bc760628ecedbd0051ca96d190a2be234f/index.js)
- [browser/main/Detail/index.js](https://github.com/BoostIO/BoostNote-Legacy/blob/789926bc760628ecedbd0051ca96d190a2be234f/browser/main/Detail/index.js)
- [browser/main/DevTools/index.js](https://github.com/BoostIO/BoostNote-Legacy/blob/789926bc760628ecedbd0051ca96d190a2be234f/browser/main/DevTools/index.js)
- [browser/main/Main.js](https://github.com/BoostIO/BoostNote-Legacy/blob/789926bc760628ecedbd0051ca96d190a2be234f/browser/main/Main.js)
- [browser/main/NewNoteButton/index.js](https://github.com/BoostIO/BoostNote-Legacy/blob/789926bc760628ecedbd0051ca96d190a2be234f/browser/main/NewNoteButton/index.js)
- [browser/main/NoteList/index.js](https://github.com/BoostIO/BoostNote-Legacy/blob/789926bc760628ecedbd0051ca96d190a2be234f/browser/main/NoteList/index.js)
- [browser/main/SideNav/index.js](https://github.com/BoostIO/BoostNote-Legacy/blob/789926bc760628ecedbd0051ca96d190a2be234f/browser/main/SideNav/index.js)
- [browser/main/StatusBar/index.js](https://github.com/BoostIO/BoostNote-Legacy/blob/789926bc760628ecedbd0051ca96d190a2be234f/browser/main/StatusBar/index.js)
- [browser/main/TopBar/index.js](https://github.com/BoostIO/BoostNote-Legacy/blob/789926bc760628ecedbd0051ca96d190a2be234f/browser/main/TopBar/index.js)
- [browser/main/index.js](https://github.com/BoostIO/BoostNote-Legacy/blob/789926bc760628ecedbd0051ca96d190a2be234f/browser/main/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| browser package | library | Observed | Groups 153 file(s) under browser package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 24 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| dev-scripts package | library | Observed | Groups 1 file(s) under dev-scripts package (observed from repository paths and static analysis). |
| extra_scripts package | library | Observed | Groups 5 file(s) under extra_scripts package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 5 file(s) under lib package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 52 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/tasks.json` (config)
- `appdmg.json` (config)
- `locales/cs.json` (config)
- `locales/da.json` (config)
- `locales/de.json` (config)
- `locales/en.json` (config)
- `locales/es-ES.json` (config)
- `locales/fa.json` (config)
- `locales/fr.json` (config)
- `locales/hu.json` (config)
- `locales/it.json` (config)
- `locales/ja.json` (config)
- `locales/ko.json` (config)
- `locales/no.json` (config)
- `locales/pl.json` (config)
- `locales/pt-BR.json` (config)
- `locales/pt-PT.json` (config)
- `locales/ru.json` (config)
- `locales/sq.json` (config)
- `locales/th.json` (config)
- `locales/tr.json` (config)
- `locales/zh-CN.json` (config)
- `locales/zh-TW.json` (config)
- `package.json` (manifest)
- `snap/snapcraft.yaml` (config)

## Top-level layout

- `browser` — 224 analysed file(s)
- `tests` — 52 analysed file(s)
- `resources` — 46 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `locales` — 21 analysed file(s)
- `docs` — 18 analysed file(s)
- `extra_scripts` — 7 analysed file(s)
- `lib` — 7 analysed file(s)
- `dictionaries` — 4 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `snap` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `__mocks__` — 1 analysed file(s)
- `dev-scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `789926bc760628ecedbd0051ca96d190a2be234f` is the revision these paths and observations refer to.
