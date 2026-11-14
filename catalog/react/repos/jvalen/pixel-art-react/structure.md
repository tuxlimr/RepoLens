# Project structure: jvalen/pixel-art-react

**Analysed commit:** `73b57b6b2305146b5a9f94ec9786ea701749c356`

**Commit reference:** [73b57b6b2305146b5a9f94ec9786ea701749c356](https://github.com/jvalen/pixel-art-react/commit/73b57b6b2305146b5a9f94ec9786ea701749c356)

**Tree at this commit:** [jvalen/pixel-art-react@73b57b6b2305](https://github.com/jvalen/pixel-art-react/tree/73b57b6b2305146b5a9f94ec9786ea701749c356)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jvalen/pixel-art-react |
| Description | Pixel art animation and drawing web app powered by React |
| Stars | 6062 |
| Forks | 333 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `73b57b6b2305146b5a9f94ec9786ea701749c356` |
| Retrieved at | 2026-11-14T19:14:10.130180+00:00 |
| Files in this snapshot | 155 |

## Directory tree

```text
examples/  (2 files)
  import-export/  (2 files)
    cat.txt
    json-cat.js
public/  (3 files)
  _redirects
  index.dev.html
  index.html
src/  (123 files)
  components/  (50 files)
    About/  (1 files)
      … 1 files under this directory
    Mentions/  (1 files)
      … 1 files under this directory
    common/  (1 files)
      … 1 files under this directory
    loadFromFile/  (5 files)
      … 5 files under this directory
    Animation.jsx
    App.jsx
    Bucket.jsx
    CellSize.jsx
    CellsInfo.jsx
    Checkbox.jsx
    ColorPicker.jsx
    Cookies.jsx
    CopyCSS.jsx
    CssDisplay.jsx
    Dimensions.jsx
    DownloadDrawing.jsx
    Duration.jsx
    Eraser.jsx
    Eyedropper.jsx
    Frame.jsx
    FramesHandler.jsx
    GridWrapper.jsx
    KeyBindings.jsx
    KeyBindingsLegend.jsx
    LoadDrawing.jsx
    Modal.jsx
    Move.jsx
    NewProject.jsx
    … 18 more files
  css/  (49 files)
    components/  (32 files)
      … 32 files under this directory
    fonts/  (3 files)
      … 3 files under this directory
    input/  (2 files)
      … 2 files under this directory
    layout/  (4 files)
      … 4 files under this directory
    views/  (3 files)
      … 3 files under this directory
    _base.css
    _normalize.css
    _utils.css
    _variables.css
    imports.css
  store/  (9 files)
    actions/  (2 files)
      … 2 files under this directory
    reducers/  (6 files)
      … 6 files under this directory
    configureStore.js
  utils/  (14 files)
    ImageToCanvas.js
    breakpoints.js
    canvasGIF.js
    color.js
    cssParse.js
    drawHandlersProvider.js
    intervals.js
    loadFromCanvas.js
    outputParse.js
    polyfills.js
    random.js
    startup.js
    storage.js
    throttle.js
  index.jsx
test/  (10 files)
  utils/  (4 files)
    color.test.js
    intervals.test.js
    loadFromCanvas.test.js
    outputParse.test.js
  actions.test.js
  activeFrameReducer.test.js
  drawingToolReducer.test.js
  framesReducer.test.js
  paletteReducer.test.js
  reducer.test.js
.babelrc
.browserslistrc
.eslintignore
.eslintrc
.gitignore
.huskyrc
.lintstagedrc
.prettierignore
.prettierrc
.stylelintrc
.travis.yml
LICENSE.md
README.md
package.json
postcss.config.js
webpack.config.js
webpack.production.config.js
```

## Entry points

- [src/components/App.jsx](https://github.com/jvalen/pixel-art-react/blob/73b57b6b2305146b5a9f94ec9786ea701749c356/src/components/App.jsx)
- [src/components/loadFromFile/index.jsx](https://github.com/jvalen/pixel-art-react/blob/73b57b6b2305146b5a9f94ec9786ea701749c356/src/components/loadFromFile/index.jsx)
- [src/index.jsx](https://github.com/jvalen/pixel-art-react/blob/73b57b6b2305146b5a9f94ec9786ea701749c356/src/index.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 50 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| index.jsx package | library | Observed | Groups 1 file(s) under index.jsx package (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 9 file(s) under store package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 14 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 123 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `test` — 10 analysed file(s)
- `public` — 3 analysed file(s)
- `examples` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `73b57b6b2305146b5a9f94ec9786ea701749c356` is the revision these paths and observations refer to.
