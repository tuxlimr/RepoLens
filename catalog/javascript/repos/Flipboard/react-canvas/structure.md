# Project structure: Flipboard/react-canvas

**Analysed commit:** `0b71180b4061a55410efb4578df2b65c1bf00a8e`

**Commit reference:** [0b71180b4061a55410efb4578df2b65c1bf00a8e](https://github.com/Flipboard/react-canvas/commit/0b71180b4061a55410efb4578df2b65c1bf00a8e)

**Tree at this commit:** [Flipboard/react-canvas@0b71180b4061](https://github.com/Flipboard/react-canvas/tree/0b71180b4061a55410efb4578df2b65c1bf00a8e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Flipboard/react-canvas |
| Description | High performance <canvas> rendering for React components |
| Stars | 13190 |
| Forks | 910 |
| Licence | BSD-3-Clause |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `0b71180b4061a55410efb4578df2b65c1bf00a8e` |
| Retrieved at | 2026-11-14T19:11:59.424299+00:00 |
| Files in this snapshot | 47 |

## Directory tree

```text
examples/  (13 files)
  common/  (3 files)
    data.js
    examples.css
    touch-emulator.js
  css-layout/  (2 files)
    app.js
    index.html
  gradient/  (2 files)
    app.js
    index.html
  listview/  (3 files)
    components/  (1 files)
      … 1 files under this directory
    app.js
    index.html
  timeline/  (3 files)
    components/  (1 files)
      … 1 files under this directory
    app.js
    index.html
lib/  (27 files)
  __tests__/  (1 files)
    clamp-test.js
  Canvas.js
  CanvasUtils.js
  ContainerMixin.js
  DrawingUtils.js
  Easing.js
  EventTypes.js
  FontFace.js
  FontUtils.js
  FrameUtils.js
  Gradient.js
  Group.js
  Image.js
  ImageCache.js
  Layer.js
  LayerMixin.js
  Layout.js
  ListView.js
  ReactCanvas.js
  RenderLayer.js
  Surface.js
  Text.js
  clamp.js
  createComponent.js
  hitTest.js
  … 2 more files
.babelrc
.gitignore
LICENSE
README.md
gulpfile.js
package.json
webpack.config.js
```

## Entry points

- [lib/ReactCanvas.js](https://github.com/Flipboard/react-canvas/blob/0b71180b4061a55410efb4578df2b65c1bf00a8e/lib/ReactCanvas.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 27 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `package.json` (manifest)

## Top-level layout

- `lib` — 27 analysed file(s)
- `examples` — 13 analysed file(s)
- `(root files)` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0b71180b4061a55410efb4578df2b65c1bf00a8e` is the revision these paths and observations refer to.
