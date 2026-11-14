# Project structure: liabru/matter-js

**Analysed commit:** `b8ee71cd7f9b49f53639ddaedd6254f1929bcbe5`

**Commit reference:** [b8ee71cd7f9b49f53639ddaedd6254f1929bcbe5](https://github.com/liabru/matter-js/commit/b8ee71cd7f9b49f53639ddaedd6254f1929bcbe5)

**Tree at this commit:** [liabru/matter-js@b8ee71cd7f9b](https://github.com/liabru/matter-js/tree/b8ee71cd7f9b49f53639ddaedd6254f1929bcbe5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | liabru/matter-js |
| Description | a 2D rigid body physics engine for the web ▲● ■ |
| Stars | 18629 |
| Forks | 1999 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b8ee71cd7f9b49f53639ddaedd6254f1929bcbe5` |
| Retrieved at | 2026-11-14T19:11:21.067003+00:00 |
| Files in this snapshot | 110 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
demo/  (13 files)
  src/  (5 files)
    Compare.js
    Demo.js
    Multi.js
    index.ejs
    index.js
  svg/  (7 files)
    iconmonstr-check-mark-8-icon.svg
    iconmonstr-direction-4-icon.svg
    iconmonstr-paperclip-2-icon.svg
    iconmonstr-puzzle-icon.svg
    iconmonstr-user-icon.svg
    svg.svg
    terrain.svg
  index.html
examples/  (49 files)
  airFriction.js
  avalanche.js
  ballPool.js
  bridge.js
  car.js
  catapult.js
  chains.js
  circleStack.js
  cloth.js
  collisionFiltering.js
  compositeManipulation.js
  compound.js
  compoundStack.js
  concave.js
  constraints.js
  doublePendulum.js
  events.js
  friction.js
  gravity.js
  gyro.js
  index.js
  manipulation.js
  mixed.js
  newtonsCradle.js
  … 25 more files
src/  (32 files)
  body/  (3 files)
    Body.js
    Composite.js
    World.js
  collision/  (9 files)
    Collision.js
    Contact.js
    Detector.js
    Grid.js
    Pair.js
    Pairs.js
    Query.js
    Resolver.js
    SAT.js
  constraint/  (2 files)
    Constraint.js
    MouseConstraint.js
  core/  (8 files)
    Common.js
    Engine.js
    Events.js
    Matter.js
    Mouse.js
    Plugin.js
    Runner.js
    Sleeping.js
  factory/  (2 files)
    Bodies.js
    Composites.js
  geometry/  (5 files)
    Axes.js
    Bounds.js
    Svg.js
    Vector.js
    Vertices.js
  module/  (2 files)
    license.js
    main.js
  render/  (1 files)
    Render.js
test/  (3 files)
  ExampleWorker.js
  Examples.spec.js
  TestTools.js
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
RELEASE.md
eslint.config.mjs
package.json
pnpm-workspace.yaml
rollup.config.demo.mjs
rollup.config.mjs
yuidoc.json
```

## Entry points

- [demo/src/index.js](https://github.com/liabru/matter-js/blob/b8ee71cd7f9b49f53639ddaedd6254f1929bcbe5/demo/src/index.js)
- [src/module/main.js](https://github.com/liabru/matter-js/blob/b8ee71cd7f9b49f53639ddaedd6254f1929bcbe5/src/module/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| body package | library | Observed | Groups 3 file(s) under body package (observed from repository paths and static analysis). |
| collision package | library | Observed | Groups 9 file(s) under collision package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constraint package | library | Observed | Groups 2 file(s) under constraint package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 4 file(s) under demo package (observed from repository paths and static analysis). |
| factory package | library | Observed | Groups 2 file(s) under factory package (observed from repository paths and static analysis). |
| geometry package | library | Observed | Groups 5 file(s) under geometry package (observed from repository paths and static analysis). |
| module package | library | Observed | Groups 2 file(s) under module package (observed from repository paths and static analysis). |
| render package | library | Observed | Groups 1 file(s) under render package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 8 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `yuidoc.json` (config)

## Top-level layout

- `examples` — 49 analysed file(s)
- `src` — 32 analysed file(s)
- `demo` — 13 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `test` — 3 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b8ee71cd7f9b49f53639ddaedd6254f1929bcbe5` is the revision these paths and observations refer to.
