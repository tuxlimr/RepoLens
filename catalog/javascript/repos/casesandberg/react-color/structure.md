# Project structure: casesandberg/react-color

**Analysed commit:** `bc9a0e1dc5d11b06c511a8e02a95bd85c7129f4b`

**Commit reference:** [bc9a0e1dc5d11b06c511a8e02a95bd85c7129f4b](https://github.com/casesandberg/react-color/commit/bc9a0e1dc5d11b06c511a8e02a95bd85c7129f4b)

**Tree at this commit:** [casesandberg/react-color@bc9a0e1dc5d1](https://github.com/casesandberg/react-color/tree/bc9a0e1dc5d11b06c511a8e02a95bd85c7129f4b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | casesandberg/react-color |
| Description | :art: Color Pickers from Sketch, Photoshop, Chrome, Github, Twitter & more |
| Stars | 12332 |
| Forks | 917 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `bc9a0e1dc5d11b06c511a8e02a95bd85c7129f4b` |
| Retrieved at | 2026-11-14T19:12:06.138258+00:00 |
| Files in this snapshot | 197 |

## Directory tree

```text
.github/  (1 files)
  CONTRIBUTING.md
.storybook/  (4 files)
  SyncColorField.js
  addons.js
  config.js
  report.js
docs/  (21 files)
  components/  (3 files)
    home/  (3 files)
      … 3 files under this directory
  documentation/  (15 files)
    01-about.md
    02-getting-started.md
    02.01-install.md
    02.02-include.md
    03-api.md
    03.01-color.md
    03.02-onChange.md
    03.03-onChangeComplete.md
    03.04-individual.md
    03.05-customStyles.md
    04-create.md
    04.01-parent.md
    04.02-helpers.md
    05-examples.md
    index.js
  images/  (1 files)
    react-color.svg
  index.html
  index.js
examples/  (46 files)
  basic/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    package.json
  basic-positioning/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    package.json
  basic-toggle-open-closed/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    package.json
  basic-with-react-hooks/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    package.json
  custom-picker/  (6 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    package.json
  custom-pointer/  (7 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    package.json
  with-portals/  (7 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    package.json
  with-redux/  (6 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    package.json
scripts/  (4 files)
  docs-dist.js
  docs-server.js
  restore-original-babelrc.js
  use-module-babelrc.js
src/  (113 files)
  components/  (89 files)
    alpha/  (4 files)
      … 4 files under this directory
    block/  (5 files)
      … 5 files under this directory
    chrome/  (7 files)
      … 7 files under this directory
    circle/  (5 files)
      … 5 files under this directory
    common/  (11 files)
      … 11 files under this directory
    compact/  (6 files)
      … 6 files under this directory
    github/  (5 files)
      … 5 files under this directory
    google/  (7 files)
      … 7 files under this directory
    hue/  (4 files)
      … 4 files under this directory
    material/  (4 files)
      … 4 files under this directory
    photoshop/  (9 files)
      … 9 files under this directory
    sketch/  (6 files)
      … 6 files under this directory
    slider/  (6 files)
      … 6 files under this directory
    swatches/  (6 files)
      … 6 files under this directory
    twitter/  (4 files)
      … 4 files under this directory
  helpers/  (8 files)
    alpha.js
    checkboard.js
    color.js
    hue.js
    index.js
    interaction.js
    saturation.js
    spec.js
  Alpha.js
  Block.js
  Chrome.js
  Circle.js
  Compact.js
  Custom.js
  Github.js
  Google.js
  Hue.js
  Material.js
  Photoshop.js
  Sketch.js
  Slider.js
  Swatches.js
  Twitter.js
  index.js
.babelrc
.gitignore
.travis.yml
CODE_OF_CONDUCT.md
LICENSE
README.md
package.json
webpack.config.js
```

## Entry points

- [src/components/common/index.js](https://github.com/casesandberg/react-color/blob/bc9a0e1dc5d11b06c511a8e02a95bd85c7129f4b/src/components/common/index.js)
- [src/helpers/index.js](https://github.com/casesandberg/react-color/blob/bc9a0e1dc5d11b06c511a8e02a95bd85c7129f4b/src/helpers/index.js)
- [src/index.js](https://github.com/casesandberg/react-color/blob/bc9a0e1dc5d11b06c511a8e02a95bd85c7129f4b/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Alpha.js package | library | Observed | Groups 1 file(s) under alpha.js package (observed from repository paths and static analysis). |
| Block.js package | library | Observed | Groups 1 file(s) under block.js package (observed from repository paths and static analysis). |
| Chrome.js package | library | Observed | Groups 1 file(s) under chrome.js package (observed from repository paths and static analysis). |
| Circle.js package | library | Observed | Groups 1 file(s) under circle.js package (observed from repository paths and static analysis). |
| Compact.js package | library | Observed | Groups 1 file(s) under compact.js package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 74 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Custom.js package | library | Observed | Groups 1 file(s) under custom.js package (observed from repository paths and static analysis). |
| Github.js package | library | Observed | Groups 1 file(s) under github.js package (observed from repository paths and static analysis). |
| Google.js package | library | Observed | Groups 1 file(s) under google.js package (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 8 file(s) under helpers package (observed from repository paths and static analysis). |
| Hue.js package | library | Observed | Groups 1 file(s) under hue.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Material.js package | library | Observed | Groups 1 file(s) under material.js package (observed from repository paths and static analysis). |
| Photoshop.js package | library | Observed | Groups 1 file(s) under photoshop.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Sketch.js package | library | Observed | Groups 1 file(s) under sketch.js package (observed from repository paths and static analysis). |
| Slider.js package | library | Observed | Groups 1 file(s) under slider.js package (observed from repository paths and static analysis). |
| Swatches.js package | library | Observed | Groups 1 file(s) under swatches.js package (observed from repository paths and static analysis). |
| Twitter.js package | library | Observed | Groups 1 file(s) under twitter.js package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `examples/basic-positioning/package.json` (manifest)
- `examples/basic-toggle-open-closed/package.json` (manifest)
- `examples/basic-with-react-hooks/package.json` (manifest)
- `examples/basic/package.json` (manifest)
- `examples/custom-picker/package.json` (manifest)
- `examples/custom-pointer/package.json` (manifest)
- `examples/with-portals/package.json` (manifest)
- `examples/with-redux/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `src` — 113 analysed file(s)
- `examples` — 46 analysed file(s)
- `docs` — 21 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.storybook` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bc9a0e1dc5d11b06c511a8e02a95bd85c7129f4b` is the revision these paths and observations refer to.
