# Project structure: unbug/codelf

**Analysed commit:** `0bfb88a8d297ca0f65abbf8f83f7826311df42a3`

**Commit reference:** [0bfb88a8d297ca0f65abbf8f83f7826311df42a3](https://github.com/unbug/codelf/commit/0bfb88a8d297ca0f65abbf8f83f7826311df42a3)

**Tree at this commit:** [unbug/codelf@0bfb88a8d297](https://github.com/unbug/codelf/tree/0bfb88a8d297ca0f65abbf8f83f7826311df42a3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | unbug/codelf |
| Description | A search tool helps dev to solve the naming things problem. |
| Stars | 14120 |
| Forks | 955 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `0bfb88a8d297ca0f65abbf8f83f7826311df42a3` |
| Retrieved at | 2026-11-14T19:11:47.057353+00:00 |
| Files in this snapshot | 116 |

## Directory tree

```text
__static/  (37 files)
  app/  (37 files)
    html/  (7 files)
      … 7 files under this directory
    resources/  (3 files)
      … 3 files under this directory
    scss/  (8 files)
      … 8 files under this directory
    src/  (15 files)
      … 15 files under this directory
    cache.manifest
    ddms_frame_callback.html
    index.html
    sw.js
app/  (3 files)
  ddms_frame_callback.html
  index.html
  opensearch.xml
assets/  (1 files)
  fonts/  (1 files)
    Dressedless_Three.svg
build-system/  (7 files)
  build.js
  clean.js
  default.js
  dist.js
  lint.js
  server.js
  util.js
src/  (42 files)
  components/  (13 files)
    hooks/  (1 files)
      … 1 files under this directory
    Bookmark.js
    Copybook.js
    Donate.js
    Doodle.js
    Loading.js
    SearchBar.js
    SearchError.js
    SourceCode.js
    Suggestion.js
    TitleLogo.js
    VariableItem.js
    VariableList.js
  constants/  (1 files)
    Configs.js
  containers/  (4 files)
    CopybookContainer.js
    MainContainer.js
    NavBarContainer.js
    NoticeContainer.js
  models/  (12 files)
    metadata/  (5 files)
      … 5 files under this directory
    AppModel.js
    BaseModel.js
    CopybookModel.js
    DDMSModel.js
    ErrorModel.js
    SearchCodeModel.js
    Store.js
  utils/  (8 files)
    FormHandler.js
    HashHandler.js
    JSONP.js
    LocalStorage.js
    Navigator.js
    Param.js
    Tools.js
    TranslateHandler.js
  vendors/  (2 files)
    prettify.css
    prettify.js
  App.js
  sw.js
styles/  (15 files)
  _animation.scss
  _common.scss
  _components.scss
  _constants.scss
  _containers.scss
  _copybook-container.scss
  _donate.scss
  _doodle.scss
  _logo.scss
  _main-container.scss
  _nav-bar-container.scss
  _notice-container.scss
  _source-code.scss
  _utils.scss
  app.scss
.editorconfig
.eslintrc.js
.gitattributes
.gitignore
LICENSE
README.md
babel.config.js
gulpfile.js
lib.config.js
package.json
webpack.config.js
```

## Entry points

- [__static/app/src/App.js](https://github.com/unbug/codelf/blob/0bfb88a8d297ca0f65abbf8f83f7826311df42a3/__static/app/src/App.js)
- [build-system/server.js](https://github.com/unbug/codelf/blob/0bfb88a8d297ca0f65abbf8f83f7826311df42a3/build-system/server.js)
- [src/App.js](https://github.com/unbug/codelf/blob/0bfb88a8d297ca0f65abbf8f83f7826311df42a3/src/App.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| build-system package | library | Observed | Groups 7 file(s) under build-system package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 13 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants package | library | Observed | Groups 1 file(s) under constants package (observed from repository paths and static analysis). |
| containers package | library | Observed | Groups 4 file(s) under containers package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). |
| __static package | library | Observed | Groups 16 file(s) under __static package (observed from repository paths and static analysis). |
| sw.js package | library | Observed | Groups 1 file(s) under sw.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 8 file(s) under utils package (observed from repository paths and static analysis). |
| vendors package | library | Observed | Groups 1 file(s) under vendors package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 42 analysed file(s)
- `__static` — 37 analysed file(s)
- `styles` — 15 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `build-system` — 7 analysed file(s)
- `app` — 3 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 11 file(s) were skipped during inventory (2 x generated/minified file excluded; 9 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0bfb88a8d297ca0f65abbf8f83f7826311df42a3` is the revision these paths and observations refer to.
