# Project structure: Automattic/node-canvas

**Analysed commit:** `efd824343c84071e26b0a132a6c6c2fcb88399fb`

**Commit reference:** [efd824343c84071e26b0a132a6c6c2fcb88399fb](https://github.com/Automattic/node-canvas/commit/efd824343c84071e26b0a132a6c6c2fcb88399fb)

**Tree at this commit:** [Automattic/node-canvas@efd824343c84](https://github.com/Automattic/node-canvas/tree/efd824343c84071e26b0a132a6c6c2fcb88399fb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Automattic/node-canvas |
| Description | Node canvas is a Cairo backed Canvas implementation for NodeJS. |
| Stars | 10696 |
| Forks | 1197 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `efd824343c84071e26b0a132a6c6c2fcb88399fb` |
| Retrieved at | 2026-11-14T19:12:34.245184+00:00 |
| Files in this snapshot | 181 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug.yml
    feat.yml
  workflows/  (2 files)
    ci.yaml
    publish.yaml
  PULL_REQUEST_TEMPLATE.md
benchmarks/  (1 files)
  run.js
examples/  (33 files)
  images/  (2 files)
    badge.svg
    small-svg.svg
  pfennigFont/  (2 files)
    FONTLOG.txt
    OFL.txt
  clock.js
  crop.js
  fill-evenodd.js
  font.js
  globalAlpha.js
  gradients.js
  grayscale-image.js
  image-caption-overlay.js
  image-src-svg.js
  image-src-url.js
  image-src.js
  indexed-png-alpha.js
  indexed-png-image-data.js
  kraken.js
  live-clock.js
  multi-page-pdf.js
  pango-glyphs.js
  pdf-images.js
  pdf-link.js
  ray.js
  resize.js
  rhill-voronoi-core-min.js
  small-pdf.js
  small-svg.js
  … 5 more files
lib/  (9 files)
  DOMMatrix.js
  bindings.js
  canvas.js
  context2d.js
  image.js
  jpegstream.js
  pattern.js
  pdfstream.js
  pngstream.js
npm/  (13 files)
  darwin-arm64/  (1 files)
    package.json
  darwin-x64/  (1 files)
    package.json
  linux-arm-gnueabihf/  (1 files)
    package.json
  linux-arm64-gnu/  (1 files)
    package.json
  linux-arm64-musl/  (1 files)
    package.json
  linux-riscv64-gnu/  (1 files)
    package.json
  linux-x64-gnu/  (1 files)
    package.json
  linux-x64-musl/  (1 files)
    package.json
  linux-x86-gnu/  (1 files)
    package.json
  linux-x86-musl/  (1 files)
    package.json
  win32-arm64/  (1 files)
    package.json
  win32-x64/  (1 files)
    package.json
  win32-x86/  (1 files)
    package.json
pkg/  (22 files)
  cairo/  (3 files)
    build.zig
    build.zig.zon
    sources.zig
  freetype/  (2 files)
    build.zig
    build.zig.zon
  giflib/  (2 files)
    build.zig
    build.zig.zon
  harfbuzz/  (2 files)
    build.zig
    build.zig.zon
  libpng/  (4 files)
    LICENSE
    build.zig
    build.zig.zon
    pnglibconf.h
  lunasvg/  (2 files)
    build.zig
    build.zig.zon
  pixman/  (2 files)
    build.zig
    build.zig.zon
  sheenbidi/  (2 files)
    build.zig
    build.zig.zon
  zlib/  (3 files)
    LICENSE
    build.zig
    build.zig.zon
scripts/  (1 files)
  version.js
src/  (49 files)
  bmp/  (3 files)
    BMPParser.cc
    BMPParser.h
    LICENSE.md
  Backends.h
  Canvas.cc
  Canvas.h
  CanvasError.h
  CanvasGradient.cc
  CanvasGradient.h
  CanvasPattern.cc
  CanvasPattern.h
  CanvasRenderingContext2d.cc
  CanvasRenderingContext2d.h
  CharData.h
  Font.h
  FontFace.cc
  FontFace.h
  FontFaceSet.cc
  FontFaceSet.h
  FontLayout.cc
  FontLayout.h
  FontManager.cc
  FontManager.h
  FontManagerLinux.cc
  FontManagerLinux.h
  FontManagerMacos.cc
  FontManagerMacos.h
  … 22 more files
test/  (35 files)
  fixtures/  (3 files)
    Arimo-Regular-License.txt
    embedded-jpeg.svg
    tree.svg
  public/  (4 files)
    app.html
    app.js
    style.css
    tests.js
  wpt/  (22 files)
    generated/  (10 files)
      … 10 files under this directory
    drawing-text-to-the-canvas.yaml
    fill-and-stroke-styles.yaml
    generate.js
    line-styles.yaml
    meta.yaml
    path-objects.yaml
    pixel-manipulation.yaml
    shadows.yaml
    text-styles.yaml
    the-canvas-element.yaml
    the-canvas-state.yaml
    transformations.yaml
  canvas.test.js
  dommatrix.test.js
  fontParser.test.js
  image.test.js
  imageData.test.js
  server.js
util/  (2 files)
  has_lib.js
  win_jpeg_lookup.js
.gitignore
CHANGELOG.md
README.md
SECURITY.md
browser.js
build.zig
build.zig.zon
index.d.ts
index.js
index.test-d.ts
package.json
```

## Entry points

- [index.js](https://github.com/Automattic/node-canvas/blob/efd824343c84071e26b0a132a6c6c2fcb88399fb/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Backends.h package | library | Observed | Groups 1 file(s) under backends.h package (observed from repository paths and static analysis). |
| benchmarks package | library | Observed | Groups 1 file(s) under benchmarks package (observed from repository paths and static analysis). |
| bmp package | library | Observed | Groups 1 file(s) under bmp package (observed from repository paths and static analysis). |
| Canvas.h package | library | Observed | Groups 1 file(s) under canvas.h package (observed from repository paths and static analysis). |
| CanvasError.h package | library | Observed | Groups 1 file(s) under canvaserror.h package (observed from repository paths and static analysis). |
| CanvasGradient.h package | library | Observed | Groups 1 file(s) under canvasgradient.h package (observed from repository paths and static analysis). |
| CanvasPattern.h package | library | Observed | Groups 1 file(s) under canvaspattern.h package (observed from repository paths and static analysis). |
| CanvasRenderingContext2d.h package | library | Observed | Groups 1 file(s) under canvasrenderingcontext2d.h package (observed from repository paths and static analysis). |
| CharData.h package | library | Observed | Groups 1 file(s) under chardata.h package (observed from repository paths and static analysis). |
| closure.h package | library | Observed | Groups 1 file(s) under closure.h package (observed from repository paths and static analysis). |
| color.h package | library | Observed | Groups 1 file(s) under color.h package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Font.h package | library | Observed | Groups 1 file(s) under font.h package (observed from repository paths and static analysis). |
| FontFace.h package | library | Observed | Groups 1 file(s) under fontface.h package (observed from repository paths and static analysis). |
| FontFaceSet.h package | library | Observed | Groups 1 file(s) under fontfaceset.h package (observed from repository paths and static analysis). |
| FontLayout.h package | library | Observed | Groups 1 file(s) under fontlayout.h package (observed from repository paths and static analysis). |
| FontManager.h package | library | Observed | Groups 1 file(s) under fontmanager.h package (observed from repository paths and static analysis). |
| FontManagerLinux.h package | library | Observed | Groups 1 file(s) under fontmanagerlinux.h package (observed from repository paths and static analysis). |
| FontManagerMacos.h package | library | Observed | Groups 1 file(s) under fontmanagermacos.h package (observed from repository paths and static analysis). |
| FontManagerWindows.h package | library | Observed | Groups 1 file(s) under fontmanagerwindows.h package (observed from repository paths and static analysis). |
| FontParser.h package | library | Observed | Groups 1 file(s) under fontparser.h package (observed from repository paths and static analysis). |
| Image.h package | library | Observed | Groups 1 file(s) under image.h package (observed from repository paths and static analysis). |
| ImageData.h package | library | Observed | Groups 1 file(s) under imagedata.h package (observed from repository paths and static analysis). |
| InstanceData.h package | library | Observed | Groups 1 file(s) under instancedata.h package (observed from repository paths and static analysis). |
| itemize.h package | library | Observed | Groups 1 file(s) under itemize.h package (observed from repository paths and static analysis). |
| JPEGStream.h package | library | Observed | Groups 1 file(s) under jpegstream.h package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 9 file(s) under lib package (observed from repository paths and static analysis). |
| pkg package | library | Observed | Groups 1 file(s) under pkg package (observed from repository paths and static analysis). |
| PNG.h package | library | Observed | Groups 1 file(s) under png.h package (observed from repository paths and static analysis). |
| Point.h package | library | Observed | Groups 1 file(s) under point.h package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). |
| unicode.h package | library | Observed | Groups 1 file(s) under unicode.h package (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 2 file(s) under util package (observed from repository paths and static analysis). |
| Util.h package | library | Observed | Groups 1 file(s) under util.h package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/feat.yml` (config)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/publish.yaml` (ci)
- `npm/darwin-arm64/package.json` (manifest)
- `npm/darwin-x64/package.json` (manifest)
- `npm/linux-arm-gnueabihf/package.json` (manifest)
- `npm/linux-arm64-gnu/package.json` (manifest)
- `npm/linux-arm64-musl/package.json` (manifest)
- `npm/linux-riscv64-gnu/package.json` (manifest)
- `npm/linux-x64-gnu/package.json` (manifest)
- `npm/linux-x64-musl/package.json` (manifest)
- `npm/linux-x86-gnu/package.json` (manifest)
- `npm/linux-x86-musl/package.json` (manifest)
- `npm/win32-arm64/package.json` (manifest)
- `npm/win32-x64/package.json` (manifest)
- `npm/win32-x86/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `src` — 49 analysed file(s)
- `test` — 35 analysed file(s)
- `examples` — 33 analysed file(s)
- `pkg` — 22 analysed file(s)
- `npm` — 13 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `lib` — 9 analysed file(s)
- `.github` — 5 analysed file(s)
- `util` — 2 analysed file(s)
- `benchmarks` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `efd824343c84071e26b0a132a6c6c2fcb88399fb` is the revision these paths and observations refer to.
