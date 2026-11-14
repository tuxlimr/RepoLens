# Project structure: metafizzy/zdog

**Analysed commit:** `dde8684be686bc6d3cbedb6be49875c0a03a14c0`

**Commit reference:** [dde8684be686bc6d3cbedb6be49875c0a03a14c0](https://github.com/metafizzy/zdog/commit/dde8684be686bc6d3cbedb6be49875c0a03a14c0)

**Tree at this commit:** [metafizzy/zdog@dde8684be686](https://github.com/metafizzy/zdog/tree/dde8684be686bc6d3cbedb6be49875c0a03a14c0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | metafizzy/zdog |
| Description | Flat, round, designer-friendly pseudo-3D engine for canvas & SVG |
| Stars | 10698 |
| Forks | 412 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `dde8684be686bc6d3cbedb6be49875c0a03a14c0` |
| Retrieved at | 2026-11-14T19:12:33.438786+00:00 |
| Files in this snapshot | 66 |

## Directory tree

```text
.github/  (2 files)
  contributing.md
  issue_template.md
demos/  (37 files)
  box-cross/  (2 files)
    box-cross.js
    index.html
  dot-cube/  (2 files)
    dot-cube.js
    index.html
  fullscreen/  (2 files)
    fullscreen.js
    index.html
  hello-world-canvas/  (2 files)
    hello-world-canvas.js
    index.html
  hello-world-svg/  (2 files)
    hello-world-svg.js
    index.html
  hemisphere-cone-ball/  (2 files)
    hemisphere-cone-ball.js
    index.html
  houses/  (2 files)
    houses.js
    index.html
  kid-kit/  (2 files)
    index.html
    kid-kit.js
  kirby-parasol/  (2 files)
    index.html
    kirby-parasol.js
  no-illo-canvas/  (2 files)
    index.html
    no-illo-canvas.js
  no-illo-svg/  (2 files)
    index.html
    no-illo-svg.js
  path-commands/  (2 files)
    index.html
    path-commands.js
  resize/  (2 files)
    index.html
    resize.js
  shade-and-shades/  (2 files)
    index.html
    shade-and-shades.js
  shapes/  (2 files)
    index.html
    shapes.js
  solids/  (2 files)
    index.html
    solids.js
  strutter/  (2 files)
    index.html
    strutter.js
  zdog-logo/  (2 files)
    index.html
    zdog-logo.js
  .eslintrc.js
js/  (19 files)
  anchor.js
  boilerplate.js
  box.js
  canvas-renderer.js
  cone.js
  cylinder.js
  dragger.js
  ellipse.js
  group.js
  hemisphere.js
  illustration.js
  index.js
  path-command.js
  polygon.js
  rect.js
  rounded-rect.js
  shape.js
  svg-renderer.js
  vector.js
tasks/  (3 files)
  .eslintrc.js
  bundle.js
  version.js
.eslintrc.js
.gitignore
README.md
bower.json
package.json
```

## Entry points

- [js/index.js](https://github.com/metafizzy/zdog/blob/dde8684be686bc6d3cbedb6be49875c0a03a14c0/js/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 19 file(s) under demos package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 19 file(s) under js package (observed from repository paths and static analysis). |
| tasks package | library | Observed | Groups 3 file(s) under tasks package (observed from repository paths and static analysis). |

## Important files

- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `demos` — 37 analysed file(s)
- `js` — 19 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `tasks` — 3 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dde8684be686bc6d3cbedb6be49875c0a03a14c0` is the revision these paths and observations refer to.
