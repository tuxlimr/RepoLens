# Project structure: DavidHDev/canvas-ui

**Analysed commit:** `a0be3b7e1f42d0d1bafde470b6794b39f6729502`

**Commit reference:** [a0be3b7e1f42d0d1bafde470b6794b39f6729502](https://github.com/DavidHDev/canvas-ui/commit/a0be3b7e1f42d0d1bafde470b6794b39f6729502)

**Tree at this commit:** [DavidHDev/canvas-ui@a0be3b7e1f42](https://github.com/DavidHDev/canvas-ui/tree/a0be3b7e1f42d0d1bafde470b6794b39f6729502)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | DavidHDev/canvas-ui |
| Description | A library of creative canvas components. Real HTML with WebGL effects running over it. React, Vue, Svelte, vanilla. |
| Stars | 5417 |
| Forks | 280 |
| Licence | Other |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `a0be3b7e1f42d0d1bafde470b6794b39f6729502` |
| Retrieved at | 2026-11-14T19:14:20.138504+00:00 |
| Files in this snapshot | 508 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (1 files)
    ci.yml
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
public/  (9 files)
  assets/  (3 files)
    models/  (2 files)
      … 2 files under this directory
    bolt-mark.svg
  _headers
  favicon.svg
  llms.txt
  logo-icon.svg
  logo.svg
  site.webmanifest
scripts/  (12 files)
  build-live-wrappers.mts
  build-registry.mts
  preflight-deploy.mts
  test-android-fallback.mjs
  test-bounded-inputs.mjs
  test-canvas-viewport.mjs
  test-flame-wrap-vanilla.mjs
  test-html-in-canvas.mjs
  test-particle-scroll-fallback.mjs
  test-playground-controls.mjs
  test-subscribe-rate-limits.mjs
  test-webgpu-resize.mjs
src/  (468 files)
  app/  (51 files)
    (shell)/  (41 files)
      … 41 files under this directory
    celebrate/  (1 files)
      … 1 files under this directory
    playground/  (1 files)
      … 1 files under this directory
    privacy/  (1 files)
      … 1 files under this directory
    globals.css
    layout.tsx
    not-found.tsx
    page.tsx
    robots.ts
    sitemap.ts
    typeset.css
  components/  (123 files)
    celebrate/  (3 files)
      … 3 files under this directory
    common/  (16 files)
      … 16 files under this directory
    demos/  (4 files)
      … 4 files under this directory
    docs/  (53 files)
      … 53 files under this directory
    landing/  (19 files)
      … 19 files under this directory
    playground/  (17 files)
      … 17 files under this directory
    ui/  (11 files)
      … 11 files under this directory
  data/  (1 files)
    components.ts
  demos/  (36 files)
    ascii-object-demo.tsx
    ascii-sweep-demo.tsx
    asciify-demo.tsx
    bend-demo.tsx
    blaze-demo.tsx
    bubble-demo.tsx
    canvas-demo.tsx
    cloth-demo.tsx
    clouds-demo.tsx
    decrypt-reveal-demo.tsx
    demo-image-cycler.tsx
    displacement-demo.tsx
    dithered-object-demo.tsx
    droplets-demo.tsx
    flame-wrap-demo.tsx
    force-field-demo.tsx
    frost-demo.tsx
    glass-demo.tsx
    glass-object-demo.tsx
    glitch-demo.tsx
    glyph-rain-demo.tsx
    grid-demo.tsx
    hex-float-demo.tsx
    ink-object-demo.tsx
    … 12 more files
  hooks/  (4 files)
    use-demo-controls.ts
    use-preference.ts
    use-theme-toggle.ts
    use-turnstile.ts
  lib/  (252 files)
    AsciiObject/  (7 files)
      … 7 files under this directory
    AsciiSweep/  (7 files)
      … 7 files under this directory
    Asciify/  (7 files)
      … 7 files under this directory
    Bend/  (7 files)
      … 7 files under this directory
    Blaze/  (7 files)
      … 7 files under this directory
    Bubble/  (7 files)
      … 7 files under this directory
    Canvas/  (7 files)
      … 7 files under this directory
    Cloth/  (7 files)
      … 7 files under this directory
    Clouds/  (7 files)
      … 7 files under this directory
    DecryptReveal/  (7 files)
      … 7 files under this directory
    Displacement/  (7 files)
      … 7 files under this directory
    DitheredObject/  (7 files)
      … 7 files under this directory
    Droplets/  (7 files)
      … 7 files under this directory
    FlameWrap/  (7 files)
      … 7 files under this directory
    ForceField/  (7 files)
      … 7 files under this directory
    Frost/  (7 files)
      … 7 files under this directory
    Glass/  (7 files)
      … 7 files under this directory
    GlassObject/  (7 files)
      … 7 files under this directory
    Glitch/  (7 files)
      … 7 files under this directory
    GlyphRain/  (7 files)
      … 7 files under this directory
    Grid/  (7 files)
      … 7 files under this directory
    HexFloat/  (7 files)
      … 7 files under this directory
    InkObject/  (7 files)
      … 7 files under this directory
    Laser/  (7 files)
      … 7 files under this directory
    Liquid/  (7 files)
      … 7 files under this directory
    LiquidObject/  (7 files)
      … 7 files under this directory
    Magnify/  (7 files)
      … 7 files under this directory
    ParticleObject/  (7 files)
      … 7 files under this directory
    ParticleReveal/  (7 files)
      … 7 files under this directory
    ParticleScroll/  (7 files)
      … 7 files under this directory
    Peel/  (7 files)
      … 7 files under this directory
    RetroDither/  (7 files)
      … 7 files under this directory
    Ripple/  (7 files)
      … 7 files under this directory
    Shatter/  (7 files)
      … 7 files under this directory
    VHS/  (7 files)
      … 7 files under this directory
    canvas-viewport.ts
    celebrate.ts
    github.ts
    html-in-canvas.ts
    rect-cache.ts
    registry.ts
    utils.ts
  webgpu-env.d.ts
worker/  (2 files)
  domains.ts
  index.ts
.env.example
.gitignore
LICENSE.md
README.md
components.json
eslint.config.mjs
next.config.ts
package.json
postcss.config.mjs
tsconfig.json
wrangler.jsonc
```

## Entry points

- [src/app/celebrate/page.tsx](https://github.com/DavidHDev/canvas-ui/blob/a0be3b7e1f42d0d1bafde470b6794b39f6729502/src/app/celebrate/page.tsx)
- [src/app/page.tsx](https://github.com/DavidHDev/canvas-ui/blob/a0be3b7e1f42d0d1bafde470b6794b39f6729502/src/app/page.tsx)
- [src/app/playground/page.tsx](https://github.com/DavidHDev/canvas-ui/blob/a0be3b7e1f42d0d1bafde470b6794b39f6729502/src/app/playground/page.tsx)
- [src/app/privacy/page.tsx](https://github.com/DavidHDev/canvas-ui/blob/a0be3b7e1f42d0d1bafde470b6794b39f6729502/src/app/privacy/page.tsx)
- [worker/index.ts](https://github.com/DavidHDev/canvas-ui/blob/a0be3b7e1f42d0d1bafde470b6794b39f6729502/worker/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 10 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 70 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 36 file(s) under demos package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 4 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 252 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 9 file(s) under scripts package (observed from repository paths and static analysis). |
| webgpu-env.d.ts package | library | Observed | Groups 1 file(s) under webgpu-env.d.ts package (observed from repository paths and static analysis). |
| worker package | library | Observed | Groups 2 file(s) under worker package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `components.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 468 analysed file(s)
- `scripts` — 12 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `public` — 9 analysed file(s)
- `.github` — 6 analysed file(s)
- `worker` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a0be3b7e1f42d0d1bafde470b6794b39f6729502` is the revision these paths and observations refer to.
