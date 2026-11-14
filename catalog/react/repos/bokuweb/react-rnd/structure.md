# Project structure: bokuweb/react-rnd

**Analysed commit:** `fec7303134ab0f0bbe83fdf975ddc15c340f7e5d`

**Commit reference:** [fec7303134ab0f0bbe83fdf975ddc15c340f7e5d](https://github.com/bokuweb/react-rnd/commit/fec7303134ab0f0bbe83fdf975ddc15c340f7e5d)

**Tree at this commit:** [bokuweb/react-rnd@fec7303134ab](https://github.com/bokuweb/react-rnd/tree/fec7303134ab0f0bbe83fdf975ddc15c340f7e5d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bokuweb/react-rnd |
| Description | 🖱  A resizable and draggable component for React. |
| Stars | 4326 |
| Forks | 327 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `fec7303134ab0f0bbe83fdf975ddc15c340f7e5d` |
| Retrieved at | 2026-11-14T19:14:48.887881+00:00 |
| Files in this snapshot | 86 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
.storybook/  (3 files)
  addons.js
  config.js
  webpack.config.js
docs/  (1 files)
  stories/  (1 files)
    _redirects
examples/  (16 files)
  vite/  (16 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .eslintrc.cjs
    .gitignore
    README.md
    index.html
    package.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
scripts/  (5 files)
  deploy-minor.sh
  deploy-patch.sh
  prod.common.js
  prod.es5.js
  prod.js
src/  (3 files)
  index.js.flow
  index.test.tsx
  index.tsx
stories/  (44 files)
  bare/  (1 files)
    bare.tsx
  basic/  (4 files)
    controlled.tsx
    multi-controlled.tsx
    multi-uncontrolled.tsx
    uncontrolled.tsx
  bounds/  (8 files)
    body-controlled.tsx
    element-controlled.tsx
    element-uncontrolled.tsx
    parent-controlled.tsx
    parent-uncontrolled.tsx
    selector-controlled.tsx
    selector-uncontrolled.tsx
    window-controlled.tsx
  callback/  (1 files)
    callbacks.tsx
  cancel/  (1 files)
    cancel.tsx
  customization/  (1 files)
    resizeHandleComponent.tsx
  dragAxis/  (3 files)
    dragAxisNone.tsx
    dragAxisX.tsx
    dragAxisY.tsx
  grid/  (3 files)
    both.tsx
    drag.tsx
    resize.tsx
  lock-aspect-ratio/  (1 files)
    basic.tsx
  min/  (1 files)
    uncontrolled.tsx
  sandbox/  (3 files)
    bodysize-to-maxwidth.tsx
    issue-#622.tsx
    lock-aspect-ratio-with-bounds.tsx
  scale/  (6 files)
    body-uncontrolled-x0-5.tsx
    body-uncontrolled-x1-5.tsx
    parent-uncontrolled.tsx
    selector-controlled.tsx
    selector-uncontrolled.tsx
    window-uncontrolled.tsx
  size/  (2 files)
    size-percent-controlled.tsx
    size-percent-uncontrolled.tsx
  bounds-and-offset.js
  index.tsx
  max-size-with-percent.js
  multiple.js
  sandbox.js
  size-and-position.js
  size-percentage.js
  styles.css
  styles.ts
.gitignore
.prettierrc
LICENSE
README.md
babel.config.js
fixture.html
package.json
renovate.json
tsconfig.json
tslint.json
```

## Entry points

- [src/index.tsx](https://github.com/bokuweb/react-rnd/blob/fec7303134ab0f0bbe83fdf975ddc15c340f7e5d/src/index.tsx)
- [stories/index.tsx](https://github.com/bokuweb/react-rnd/blob/fec7303134ab0f0bbe83fdf975ddc15c340f7e5d/stories/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.test.tsx package | library | Observed | Groups 1 file(s) under index.test.tsx package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 43 file(s) under stories package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `examples/vite/package.json` (manifest)
- `examples/vite/tsconfig.app.json` (config)
- `examples/vite/tsconfig.json` (config)
- `examples/vite/tsconfig.node.json` (config)
- `package.json` (manifest)
- `renovate.json` (config)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `stories` — 44 analysed file(s)
- `examples` — 16 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `.storybook` — 3 analysed file(s)
- `src` — 3 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `fec7303134ab0f0bbe83fdf975ddc15c340f7e5d` is the revision these paths and observations refer to.
