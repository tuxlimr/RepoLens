# Project structure: yaronn/blessed-contrib

**Analysed commit:** `587d0efc4c63166a1cf3274f7bdc4dd8a8d9da1e`

**Commit reference:** [587d0efc4c63166a1cf3274f7bdc4dd8a8d9da1e](https://github.com/yaronn/blessed-contrib/commit/587d0efc4c63166a1cf3274f7bdc4dd8a8d9da1e)

**Tree at this commit:** [yaronn/blessed-contrib@587d0efc4c63](https://github.com/yaronn/blessed-contrib/tree/587d0efc4c63166a1cf3274f7bdc4dd8a8d9da1e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yaronn/blessed-contrib |
| Description | Build terminal dashboards using ascii/ansi art and javascript |
| Stars | 15772 |
| Forks | 832 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `587d0efc4c63166a1cf3274f7bdc4dd8a8d9da1e` |
| Retrieved at | 2026-11-14T19:11:35.955845+00:00 |
| Files in this snapshot | 65 |

## Directory tree

```text
examples/  (37 files)
  inline-data/  (10 files)
    bar.js
    donut.js
    gauge.js
    lcd.js
    map.js
    markdown.js
    multi-line-chart.js
    picture.js
    sparkline.js
    table.js
  bar.js
  carousel.js
  dashboard-random-colors.js
  dashboard.js
  donut.js
  explorer.js
  gauge-list.js
  gauge-stack.js
  gauge.js
  grid-no-border.js
  grid.js
  lcd.js
  line-abbreviate.js
  line-fraction.js
  line-random-colors.js
  line-start-above-zero.js
  line-zoomed-in.js
  log.js
  map.js
  markdown.js
  marked-terminal.js
  multi-line-chart.js
  picture.js
  sparkline.js
  … 3 more files
lib/  (19 files)
  layout/  (2 files)
    carousel.js
    grid.js
  widget/  (15 files)
    charts/  (3 files)
      … 3 files under this directory
    canvas.js
    donut.js
    gauge-list.js
    gauge.js
    lcd.js
    log.js
    map.js
    markdown.js
    picture.js
    sparkline.js
    table.js
    tree.js
  server-utils.js
  utils.js
test/  (1 files)
  prototype-pollution.js
.eslintrc.json
.gitignore
.npmignore
LICENSE.md
README.md
index.d.ts
index.js
package.json
```

## Entry points

- [index.js](https://github.com/yaronn/blessed-contrib/blob/587d0efc4c63166a1cf3274f7bdc4dd8a8d9da1e/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 19 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `package.json` (manifest)

## Top-level layout

- `examples` — 37 analysed file(s)
- `lib` — 19 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `test` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `587d0efc4c63166a1cf3274f7bdc4dd8a8d9da1e` is the revision these paths and observations refer to.
