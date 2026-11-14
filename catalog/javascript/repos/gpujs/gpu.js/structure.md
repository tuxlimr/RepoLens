# Project structure: gpujs/gpu.js

**Analysed commit:** `290711d0f8ff1af95b291489898f73a5c1b85a7a`

**Commit reference:** [290711d0f8ff1af95b291489898f73a5c1b85a7a](https://github.com/gpujs/gpu.js/commit/290711d0f8ff1af95b291489898f73a5c1b85a7a)

**Tree at this commit:** [gpujs/gpu.js@290711d0f8ff](https://github.com/gpujs/gpu.js/tree/290711d0f8ff1af95b291489898f73a5c1b85a7a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gpujs/gpu.js |
| Description | GPU Accelerated JavaScript |
| Stars | 15530 |
| Forks | 667 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `290711d0f8ff1af95b291489898f73a5c1b85a7a` |
| Retrieved at | 2026-11-14T19:11:37.858097+00:00 |
| Files in this snapshot | 521 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (2 files)
    browserstack.yml
    ci.yml
  compare-test-failures.js
  known-test-failures.txt
docs/  (1 files)
  design/  (1 files)
    pipeline-compilation.md
examples/  (15 files)
  cat-image/  (1 files)
    index.html
  raster-globe/  (1 files)
    index.html
  video/  (1 files)
    index.html
  advanced-typescript.ts
  fluid.html
  internal-variable-precision.html
  json-saving.js
  mandelbrot-set.html
  mandelbulb.html
  parallel-raytracer.html
  random.html
  raytracer.html
  simple-javascript.js
  simple-typescript.ts
  slow-fade.html
scripts/  (13 files)
  beautify.js
  benchmark-async.mjs
  benchmark-pipeline-webgpu.mjs
  benchmark-pipeline.mjs
  benchmark-webasm.mjs
  benchmark-webgpu.mjs
  build-tests.js
  build.js
  dev.js
  empty-module.js
  lib.js
  make.js
  minify.js
src/  (124 files)
  backend/  (111 files)
    cpu/  (3 files)
      … 3 files under this directory
    gl/  (22 files)
      … 22 files under this directory
    headless-gl/  (1 files)
      … 1 files under this directory
    web-assembly/  (5 files)
      … 5 files under this directory
    web-gl/  (35 files)
      … 35 files under this directory
    web-gl2/  (35 files)
      … 35 files under this directory
    web-gpu/  (5 files)
      … 5 files under this directory
    function-builder.js
    function-node.js
    function-tracer.js
    kernel-value.js
    kernel.js
  plugins/  (2 files)
    math-random-triangle-noise.js
    math-random-uniformly-distributed.js
  alias.js
  browser-header.txt
  browser.js
  gpu.js
  index.d.ts
  index.js
  input.js
  kernel-run-shortcut.js
  pipeline.js
  texture.js
  utils.js
test/  (355 files)
  browserstack/  (5 files)
    browsers.js
    context-probe.html
    run.js
    smoke.html
    visual.html
  features/  (195 files)
    pipeline/  (7 files)
      … 7 files under this directory
    to-string/  (95 files)
      … 95 files under this directory
    webasm/  (8 files)
      … 8 files under this directory
    webgpu/  (11 files)
      … 11 files under this directory
    add-custom-function.js
    add-custom-native-function.js
    add-typed-functions.js
    argument-array-types.js
    argument-array1d-types.js
    argument-array2d-types.js
    argument-array3d-types.js
    argument-type-changes.js
    arithmetic-operators.js
    assignment-operators.js
    async-mode.js
    basic-math.js
    bitwise-not-coverage.js
    bitwise-operators.js
    boolean-from-expression.js
    canvas.js
    clear-textures.js
    clone-textures.js
    combine-kernels.js
    constants-array.js
    constants-bool.js
    constants-canvas.js
    constants-float.js
    constants-image-array.js
    … 50 more files
  internal/  (80 files)
    backend/  (44 files)
      … 44 files under this directory
    argument-texture-switching.js
    boolean.js
    casting.js
    constants-texture-switching.js
    constructor-features.js
    context-inheritance.js
    deep-types.js
    deprecated.js
    destroy-releases-resources.js
    different-texture-cloning.js
    dynamic-output-texture-cache.js
    function-builder.js
    function-composition.js
    function-node.js
    function-return-type-detection.js
    function-tracer.js
    functions-as-strings.js
    gpu-methods.js
    hoisted-index-reads.js
    implied-else.js
    kernel-run-shortcut.js
    kernel.js
    loop-int.js
    loop-max.js
    … 12 more files
  issues/  (66 files)
    114-create-kernel-map-run-second-time.js
    116-multiple-kernels-run-again.js
    130-typed-array.js
    147-missing-constant.js
    152-for-vars.js
    159-3d.js
    174-webgl-context-warning.js
    195-read-from-texture2d.js
    207-same-function-reuse.js
    212-funky-function-support.js
    233-kernel-map-single-precision.js
    241-CPU-vs-GPU-maps-output-differently.js
    259-atan2.js
    263-to-string.js
    267-immutable-sub-kernels.js
    270-cache.js
    279-wrong-canvas-size.js
    300-nested-array-index.js
    31-nested-var-declare-test.js
    313-variable-lookup.js
    314-large-input-array-addressing.js
    335-missing-z-index-issue.js
    346-uint8array-converted.js
    349-division-by-factors-of-3.js
    … 42 more files
  playwright/  (2 files)
    modules.js
    qunit.spec.js
  all-template.html
  all.html
  benchmark-faster.js
  benchmark.js
  browser-test-utils.js
  index.js
  test-utils.js
.gitignore
CLAUDE.md
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
README.md
SECURITY.md
package.json
playwright.config.js
```

## Entry points

- [src/index.js](https://github.com/gpujs/gpu.js/blob/290711d0f8ff1af95b291489898f73a5c1b85a7a/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| alias.js package | library | Observed | Groups 1 file(s) under alias.js package (observed from repository paths and static analysis). |
| backend package | library | Observed | Groups 111 file(s) under backend package (observed from repository paths and static analysis). |
| browser.js package | library | Observed | Groups 1 file(s) under browser.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| gpu.js package | library | Observed | Groups 1 file(s) under gpu.js package (observed from repository paths and static analysis). |
| index.d.ts package | library | Observed | Groups 1 file(s) under index.d.ts package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| input.js package | library | Observed | Groups 1 file(s) under input.js package (observed from repository paths and static analysis). |
| kernel-run-shortcut.js package | library | Observed | Groups 1 file(s) under kernel-run-shortcut.js package (observed from repository paths and static analysis). |
| pipeline.js package | library | Observed | Groups 1 file(s) under pipeline.js package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 2 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 13 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 355 file(s) under tests (observed from repository paths and static analysis). |
| texture.js package | library | Observed | Groups 1 file(s) under texture.js package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/browserstack.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `test` — 355 analysed file(s)
- `src` — 124 analysed file(s)
- `examples` — 15 analysed file(s)
- `scripts` — 13 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 4 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `290711d0f8ff1af95b291489898f73a5c1b85a7a` is the revision these paths and observations refer to.
