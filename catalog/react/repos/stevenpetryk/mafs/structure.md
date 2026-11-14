# Project structure: stevenpetryk/mafs

**Analysed commit:** `e74a3ef465f4ddc98704814d2ae18b73a6cd9dae`

**Commit reference:** [e74a3ef465f4ddc98704814d2ae18b73a6cd9dae](https://github.com/stevenpetryk/mafs/commit/e74a3ef465f4ddc98704814d2ae18b73a6cd9dae)

**Tree at this commit:** [stevenpetryk/mafs@e74a3ef465f4](https://github.com/stevenpetryk/mafs/tree/e74a3ef465f4ddc98704814d2ae18b73a6cd9dae)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | stevenpetryk/mafs |
| Description | React components for interactive math |
| Stars | 3450 |
| Forks | 100 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `e74a3ef465f4ddc98704814d2ae18b73a6cd9dae` |
| Retrieved at | 2026-11-14T19:15:18.940160+00:00 |
| Files in this snapshot | 217 |

## Directory tree

```text
.api-report/  (1 files)
  mafs.api.md
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
docs/  (106 files)
  app/  (38 files)
    guides/  (32 files)
      … 32 files under this directory
    globals.css
    layout.tsx
    mafs-usage.css
    page.module.css
    page.tsx
    syntax-highlighting.css
  components/  (58 files)
    guide-examples/  (47 files)
      … 47 files under this directory
    Advanced.tsx
    Code.tsx
    CodeAndExample.tsx
    Experimental.tsx
    MafsLogo.tsx
    PropTable.tsx
    RiemannHomepage.tsx
    ScrollTop.tsx
    WIP.tsx
    analytics.tsx
    icons.tsx
  helpers/  (1 files)
    fancyFx.tsx
  public/  (1 files)
    favicon.svg
  .gitignore
  guide-example-loader.mjs
  next.config.js
  package.json
  postcss.config.js
  raw.d.ts
  tailwind.config.js
  tsconfig.json
e2e/  (4 files)
  components/  (1 files)
    MafsDragging.tsx
  generated-vrt.spec.tsx
  mafs-panning.spec.tsx
  movable-point.spec.tsx
playwright/  (2 files)
  index.html
  index.ts
scripts/  (6 files)
  build.ts
  dev.ts
  docgen-cli.ts
  docgen.ts
  publish-branch.ts
  testgen.ts
src/  (52 files)
  animation/  (1 files)
    useStopwatch.ts
  context/  (5 files)
    CoordinateContext.tsx
    PaneContext.tsx
    SpanContext.tsx
    TestContext.tsx
    TransformContext.tsx
  debug/  (3 files)
    TransformWidget.tsx
    ViewportInfo.tsx
    index.tsx
  display/  (31 files)
    Coordinates/  (4 files)
      … 4 files under this directory
    Line/  (4 files)
      … 4 files under this directory
    Plot/  (7 files)
      … 7 files under this directory
    Circle.tsx
    Ellipse.tsx
    Image.tsx
    LaTeX.tsx
    Line.tsx
    MovablePointDisplay.test.ts
    MovablePointDisplay.tsx
    Plot.tsx
    Point.tsx
    PolyBase.tsx
    Polygon.tsx
    Polyline.tsx
    Text.tsx
    Theme.ts
    Transform.tsx
    Vector.tsx
  gestures/  (2 files)
    useCamera.tsx
    useWheelEnabler.tsx
  interaction/  (4 files)
    MovablePoint.test.ts
    MovablePoint.tsx
    useMovable.tsx
    useMovablePoint.tsx
  typings/  (1 files)
    env.d.ts
  view/  (1 files)
    Mafs.tsx
  index.tsx
  math.test.ts
  math.ts
  vec.ts
tests/  (23 files)
  frameworks/  (23 files)
    nextjs/  (7 files)
      … 7 files under this directory
    vite/  (13 files)
      … 13 files under this directory
    frameworks.spec.tsx
    pnpm-workspace.yaml
    setup.ts
.browserslistrc
.envrc
.eslintignore
.eslintrc.json
.gitignore
.nvmrc
.prettierignore
.prettierrc.json
CHANGELOG.md
LICENSE
README.md
api-extractor.json
core.css
flake.lock
flake.nix
font.css
package.json
playwright.config.ts
pnpm-workspace.yaml
tsconfig.json
vercel.json
vitest.config.ts
```

## Entry points

- [playwright/index.ts](https://github.com/stevenpetryk/mafs/blob/e74a3ef465f4ddc98704814d2ae18b73a6cd9dae/playwright/index.ts)
- [src/debug/index.tsx](https://github.com/stevenpetryk/mafs/blob/e74a3ef465f4ddc98704814d2ae18b73a6cd9dae/src/debug/index.tsx)
- [src/display/Coordinates/index.tsx](https://github.com/stevenpetryk/mafs/blob/e74a3ef465f4ddc98704814d2ae18b73a6cd9dae/src/display/Coordinates/index.tsx)
- [src/index.tsx](https://github.com/stevenpetryk/mafs/blob/e74a3ef465f4ddc98704814d2ae18b73a6cd9dae/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| animation package | library | Observed | Groups 1 file(s) under animation package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| context package | library | Observed | Groups 5 file(s) under context package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| debug package | library | Observed | Groups 3 file(s) under debug package (observed from repository paths and static analysis). |
| display package | library | Observed | Groups 31 file(s) under display package (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 4 file(s) under e2e package (observed from repository paths and static analysis). |
| gestures package | library | Observed | Groups 2 file(s) under gestures package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| interaction package | library | Observed | Groups 4 file(s) under interaction package (observed from repository paths and static analysis). |
| math.test.ts package | library | Observed | Groups 1 file(s) under math.test.ts package (observed from repository paths and static analysis). |
| math.ts package | library | Observed | Groups 1 file(s) under math.ts package (observed from repository paths and static analysis). |
| playwright package | library | Observed | Groups 1 file(s) under playwright package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 23 file(s) under tests (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 1 file(s) under typings package (observed from repository paths and static analysis). |
| vec.ts package | library | Observed | Groups 1 file(s) under vec.ts package (observed from repository paths and static analysis). |
| view package | library | Observed | Groups 1 file(s) under view package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/workflows/ci.yml` (ci)
- `.prettierrc.json` (config)
- `api-extractor.json` (config)
- `docs/components/guide-examples/.prettierrc.json` (config)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `docs` — 106 analysed file(s)
- `src` — 52 analysed file(s)
- `tests` — 23 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `scripts` — 6 analysed file(s)
- `e2e` — 4 analysed file(s)
- `playwright` — 2 analysed file(s)
- `.api-report` — 1 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e74a3ef465f4ddc98704814d2ae18b73a6cd9dae` is the revision these paths and observations refer to.
