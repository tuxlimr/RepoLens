# Project structure: wheresryan22/anatomy

**Analysed commit:** `1482e8469b0a9e0d8cc18ea2740a01423d29ae80`

**Commit reference:** [1482e8469b0a9e0d8cc18ea2740a01423d29ae80](https://github.com/wheresryan22/anatomy/commit/1482e8469b0a9e0d8cc18ea2740a01423d29ae80)

**Tree at this commit:** [wheresryan22/anatomy@1482e8469b0a](https://github.com/wheresryan22/anatomy/tree/1482e8469b0a9e0d8cc18ea2740a01423d29ae80)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wheresryan22/anatomy |
| Description | An agent skill for creating detailed, interactive isometric illustrations of real-world machines and complex systems. Generates polished SVGs with optional WebGL shaders and 3D effects. |
| Stars | 27279 |
| Forks | 2308 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `1482e8469b0a9e0d8cc18ea2740a01423d29ae80` |
| Retrieved at | 2026-11-14T19:10:53.792763+00:00 |
| Files in this snapshot | 143 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    figure_request.yml
  workflows/  (1 files)
    ci.yml
  PULL_REQUEST_TEMPLATE.md
agents/  (1 files)
  openai.yaml
evals/  (1 files)
  evals.json
examples/  (42 files)
  arcade-cabinet/  (6 files)
    arcade-cabinet.css
    build.mjs
    live.js
    parts.mjs
    screen.mjs
    sheet.mjs
  desk-computer/  (1 files)
    build.mjs
  dial-indicator/  (3 files)
    build.mjs
    dial-indicator-light.html
    dial-indicator.html
  push-button/  (4 files)
    build.mjs
    push-button-light.html
    push-button.html
    sheet.mjs
  raptor-engine/  (4 files)
    build.mjs
    live.js
    raptor.css
    sheet.mjs
  ripple-tank/  (4 files)
    build.mjs
    live.js
    model.mjs
    ripple.css
  spot-plate/  (8 files)
    art.tsx
    drops.ts
    fan.ts
    figure.tsx
    geometry.ts
    live.tsx
    rig.ts
    spot-plate.css
  test-rig/  (8 files)
    art.tsx
    figure.tsx
    geometry.ts
    live.tsx
    pose.ts
    rig.ts
    stretch.css
    view.ts
  turning-dial/  (4 files)
    build.mjs
    dial.css
    live.js
    stress.mjs
kit/  (16 files)
  react/  (2 files)
    draw.tsx
    live.tsx
  audit.mjs
  canvas-painter.mjs
  gl-shared.mjs
  gl.mjs
  iso-kit.mjs
  iso-kit.ts
  iso.css
  lathe.mjs
  pdf-button.mjs
  tube.mjs
  turn-audit.mjs
  turn-build.mjs
  turn-fixed.mjs
  turn.mjs
references/  (10 files)
  3d.md
  craft.md
  kit.md
  motion.md
  print.md
  publish.md
  react.md
  verify.md
  walkthrough.md
  webgl.md
scripts/  (59 files)
  audit-affine-bounds.test.mjs
  audit-cache.test.mjs
  audit-clearance-envelope.test.mjs
  audit-empty-clipping.test.mjs
  audit-order-convergence.test.mjs
  audit-path-origin.test.mjs
  audit-profile.test.mjs
  audit-projection.test.mjs
  audit-slide-clearance.test.mjs
  audit-svg-attributes.test.mjs
  audit-taper.test.mjs
  audit-tube-support.test.mjs
  capture-current-geometry.test.mjs
  capture-selector.test.mjs
  capture.mjs
  capture.test.mjs
  chrome-port.mjs
  chrome-startup.test.mjs
  curve-density.test.mjs
  drive-actions.test.mjs
  drive-async-until.test.mjs
  drive-page-load.test.mjs
  drive-turn-controller.test.mjs
  drive.mjs
  … 35 more files
.gitattributes
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
SKILL.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| kit package | library | Observed | Groups 15 file(s) under kit package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 59 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/figure_request.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `agents/openai.yaml` (config)
- `evals/evals.json` (config)

## Top-level layout

- `scripts` — 59 analysed file(s)
- `examples` — 42 analysed file(s)
- `kit` — 16 analysed file(s)
- `references` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 5 analysed file(s)
- `agents` — 1 analysed file(s)
- `evals` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1482e8469b0a9e0d8cc18ea2740a01423d29ae80` is the revision these paths and observations refer to.
