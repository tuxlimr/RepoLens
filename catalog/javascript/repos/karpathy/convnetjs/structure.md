# Project structure: karpathy/convnetjs

**Analysed commit:** `4c3358a315b4d71f31a0d532eb5d1700e9e592ee`

**Commit reference:** [4c3358a315b4d71f31a0d532eb5d1700e9e592ee](https://github.com/karpathy/convnetjs/commit/4c3358a315b4d71f31a0d532eb5d1700e9e592ee)

**Tree at this commit:** [karpathy/convnetjs@4c3358a315b4](https://github.com/karpathy/convnetjs/tree/4c3358a315b4d71f31a0d532eb5d1700e9e592ee)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | karpathy/convnetjs |
| Description | Deep Learning in Javascript. Train Convolutional Neural Networks (or ordinary ones) in your browser. |
| Stars | 11217 |
| Forks | 2066 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `4c3358a315b4d71f31a0d532eb5d1700e9e592ee` |
| Retrieved at | 2026-11-14T19:12:23.870893+00:00 |
| Files in this snapshot | 50 |

## Directory tree

```text
compile/  (1 files)
  build.xml
demo/  (23 files)
  css/  (2 files)
    automatic.css
    style.css
  js/  (11 files)
    autoencoder.js
    automatic.js
    classify2d.js
    image-helpers.js
    image_regression.js
    images-demo.js
    npgmain.js
    pica.js
    regression.js
    rldemo.js
    trainers.js
  autoencoder.html
  automatic.html
  cifar10.html
  classify2d.html
  image_regression.html
  mnist.html
  regression.html
  rldemo.html
  speedtest.html
  trainers.html
src/  (15 files)
  convnet_export.js
  convnet_init.js
  convnet_layers_dotproducts.js
  convnet_layers_dropout.js
  convnet_layers_input.js
  convnet_layers_loss.js
  convnet_layers_nonlinearities.js
  convnet_layers_normalization.js
  convnet_layers_pool.js
  convnet_magicnet.js
  convnet_net.js
  convnet_trainers.js
  convnet_util.js
  convnet_vol.js
  convnet_vol_util.js
test/  (8 files)
  jasmine/  (8 files)
    lib/  (5 files)
      … 5 files under this directory
    spec/  (1 files)
      … 1 files under this directory
    MIT.LICENSE
    SpecRunner.html
LICENSE
Readme.md
bower.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| convnet_export.js package | library | Observed | Groups 1 file(s) under convnet_export.js package (observed from repository paths and static analysis). |
| convnet_init.js package | library | Observed | Groups 1 file(s) under convnet_init.js package (observed from repository paths and static analysis). |
| convnet_layers_dotproducts.js package | library | Observed | Groups 1 file(s) under convnet_layers_dotproducts.js package (observed from repository paths and static analysis). |
| convnet_layers_dropout.js package | library | Observed | Groups 1 file(s) under convnet_layers_dropout.js package (observed from repository paths and static analysis). |
| convnet_layers_input.js package | library | Observed | Groups 1 file(s) under convnet_layers_input.js package (observed from repository paths and static analysis). |
| convnet_layers_loss.js package | library | Observed | Groups 1 file(s) under convnet_layers_loss.js package (observed from repository paths and static analysis). |
| convnet_layers_nonlinearities.js package | library | Observed | Groups 1 file(s) under convnet_layers_nonlinearities.js package (observed from repository paths and static analysis). |
| convnet_layers_normalization.js package | library | Observed | Groups 1 file(s) under convnet_layers_normalization.js package (observed from repository paths and static analysis). |
| convnet_layers_pool.js package | library | Observed | Groups 1 file(s) under convnet_layers_pool.js package (observed from repository paths and static analysis). |
| convnet_magicnet.js package | library | Observed | Groups 1 file(s) under convnet_magicnet.js package (observed from repository paths and static analysis). |
| convnet_net.js package | library | Observed | Groups 1 file(s) under convnet_net.js package (observed from repository paths and static analysis). |
| convnet_trainers.js package | library | Observed | Groups 1 file(s) under convnet_trainers.js package (observed from repository paths and static analysis). |
| convnet_util.js package | library | Observed | Groups 1 file(s) under convnet_util.js package (observed from repository paths and static analysis). |
| convnet_vol.js package | library | Observed | Groups 1 file(s) under convnet_vol.js package (observed from repository paths and static analysis). |
| convnet_vol_util.js package | library | Observed | Groups 1 file(s) under convnet_vol_util.js package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 11 file(s) under demo package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `bower.json` (config)

## Top-level layout

- `demo` — 23 analysed file(s)
- `src` — 15 analysed file(s)
- `test` — 8 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `compile` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4c3358a315b4d71f31a0d532eb5d1700e9e592ee` is the revision these paths and observations refer to.
