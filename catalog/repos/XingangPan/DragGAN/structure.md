# Project structure: XingangPan/DragGAN

**Analysed commit:** `336f120ce126aca6f55dc58537e76c10d19eabd0`

**Commit reference:** [336f120ce126aca6f55dc58537e76c10d19eabd0](https://github.com/XingangPan/DragGAN/commit/336f120ce126aca6f55dc58537e76c10d19eabd0)

**Tree at this commit:** [XingangPan/DragGAN@336f120ce126](https://github.com/XingangPan/DragGAN/tree/336f120ce126aca6f55dc58537e76c10d19eabd0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | XingangPan/DragGAN |
| Description | Official Code for DragGAN (SIGGRAPH 2023) |
| Stars | 35696 |
| Forks | 3381 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `336f120ce126aca6f55dc58537e76c10d19eabd0` |
| Retrieved at | 2026-11-14T19:06:58.290540+00:00 |
| Files in this snapshot | 190 |

## Directory tree

```text
dnnlib/  (2 files)
  __init__.py
  util.py
gradio_utils/  (2 files)
  __init__.py
  utils.py
gui_utils/  (6 files)
  __init__.py
  gl_utils.py
  glfw_window.py
  imgui_utils.py
  imgui_window.py
  text_utils.py
scripts/  (4 files)
  download_model.py
  download_models.json
  gui.bat
  gui.sh
stylegan_human/  (128 files)
  PP_HumanSeg/  (3 files)
    deploy/  (1 files)
      … 1 files under this directory
    export_model/  (1 files)
      … 1 files under this directory
    pretrained_model/  (1 files)
      … 1 files under this directory
  dnnlib/  (13 files)
    tflib/  (11 files)
      … 11 files under this directory
    __init__.py
    util.py
  docs/  (1 files)
    Dataset.md
  edit/  (3 files)
    __init__.py
    edit_config.py
    edit_helper.py
  latent_direction/  (4 files)
    ss_statics/  (4 files)
      … 4 files under this directory
  openpose/  (5 files)
    model/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
  pti/  (30 files)
    pti_configs/  (4 files)
      … 4 files under this directory
    pti_models/  (17 files)
      … 17 files under this directory
    training/  (9 files)
      … 9 files under this directory
  torch_utils/  (34 files)
    op_edit/  (7 files)
      … 7 files under this directory
    ops/  (20 files)
      … 20 files under this directory
    __init__.py
    custom_ops.py
    misc.py
    models.py
    models_face.py
    persistence.py
    training_stats.py
  training/  (7 files)
    __init__.py
    augment.py
    dataset.py
    loss.py
    networks_stylegan2.py
    networks_stylegan3.py
    training_loop.py
  training_scripts/  (7 files)
    sg2/  (3 files)
      … 3 files under this directory
    sg3/  (4 files)
      … 4 files under this directory
  utils/  (7 files)
    ImagesDataset.py
    __init__.py
    data_utils.py
    face_alignment.py
    log_utils.py
    models_utils.py
    util.py
  .gitignore
  README.md
  __init__.py
  alignment.py
  bg_white.py
  edit.py
  environment.yml
  generate.py
  insetgan.py
  interpolation.py
  legacy.py
  run_pti.py
  style_mixing.py
  stylemixing_video.py
torch_utils/  (25 files)
  ops/  (20 files)
    __init__.py
    bias_act.cpp
    bias_act.cu
    bias_act.h
    bias_act.py
    conv2d_gradfix.py
    conv2d_resample.py
    filtered_lrelu.cpp
    filtered_lrelu.cu
    filtered_lrelu.h
    filtered_lrelu.py
    filtered_lrelu_ns.cu
    filtered_lrelu_rd.cu
    filtered_lrelu_wr.cu
    fma.py
    grid_sample_gradfix.py
    upfirdn2d.cpp
    upfirdn2d.cu
    upfirdn2d.h
    upfirdn2d.py
  __init__.py
  custom_ops.py
  misc.py
  persistence.py
  training_stats.py
training/  (7 files)
  __init__.py
  augment.py
  dataset.py
  loss.py
  networks_stylegan2.py
  networks_stylegan3.py
  training_loop.py
viz/  (6 files)
  __init__.py
  capture_widget.py
  drag_widget.py
  latent_widget.py
  pickle_widget.py
  renderer.py
.gitignore
Dockerfile
LICENSE.txt
README.md
environment.yml
gen_images.py
legacy.py
requirements.txt
visualizer_drag.py
visualizer_drag_gradio.py
```

## Entry points

- [stylegan_human/openpose/src/body.py:209](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/stylegan_human/openpose/src/body.py#L209)
- [gen_images.py:80](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/gen_images.py#L80)
- [legacy.py:297](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/legacy.py#L297)
- [scripts/download_model.py:77](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/scripts/download_model.py#L77)
- [stylegan_human/PP_HumanSeg/export_model/download_export_model.py:36](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/stylegan_human/PP_HumanSeg/export_model/download_export_model.py#L36)
- [stylegan_human/PP_HumanSeg/pretrained_model/download_pretrained_model.py:36](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/stylegan_human/PP_HumanSeg/pretrained_model/download_pretrained_model.py#L36)
- [stylegan_human/alignment.py:206](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/stylegan_human/alignment.py#L206)
- [stylegan_human/bg_white.py:40](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/stylegan_human/bg_white.py#L40)
- [stylegan_human/edit.py:55](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/stylegan_human/edit.py#L55)
- [stylegan_human/generate.py:48](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/stylegan_human/generate.py#L48)
- [stylegan_human/insetgan.py:347](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/stylegan_human/insetgan.py#L347)
- [stylegan_human/interpolation.py:106](https://github.com/XingangPan/DragGAN/blob/336f120ce126aca6f55dc58537e76c10d19eabd0/stylegan_human/interpolation.py#L106)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: clear_state, init_images, preprocess_mask_info, reverse_point_pairs, update_image_draw. |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Blur, ConstantInput, ConvLayer, Discriminator, Downsample, EqualConv2d. Observed top-level functions: k… |
| dnnlib package | library | Observed | Groups 2 file(s) under dnnlib package (observed from repository paths and static analysis). Observed top-level classes: EasyDict, Logger. Observed top-level functions: ask_yes_no, call_func_by_name, construct_class_by_n… |
| Application entry point | entrypoint | Observed | Groups 18 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AsyncRenderer, Body, CommaSeparatedList, InsetGAN, UserError, Visualizer. Observed top-le… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| gradio_utils package | library | Observed | Groups 2 file(s) under gradio_utils package (observed from repository paths and static analysis). Observed top-level classes: ImageMask. Observed top-level functions: draw_mask_on_image, draw_points_on_image, get_latest… |
| gui_utils package | library | Observed | Groups 6 file(s) under gui_utils package (observed from repository paths and static analysis). Observed top-level classes: Framebuffer, GlfwWindow, ImguiWindow, Texture, _GlfwRenderer. Observed top-level functions: _get… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| stylegan_human package | library | Observed | Groups 90 file(s) under stylegan_human package (observed from repository paths and static analysis). Observed top-level classes: AugmentPipe, Backbone, BaseCoach, Blur, Bottleneck, Collector. Observed top-level function… |
| torch_utils package | library | Observed | Groups 19 file(s) under torch_utils package (observed from repository paths and static analysis). Observed top-level classes: Collector, InfiniteSampler, _FusedMultiplyAdd, _GridSample2dBackward, _GridSample2dForward. O… |
| training package | library | Observed | Groups 7 file(s) under training package (observed from repository paths and static analysis). Observed top-level classes: AugmentPipe, Conv2dLayer, Dataset, Discriminator, DiscriminatorBlock, DiscriminatorEpilogue. Obse… |
| viz package | library | Observed | Groups 6 file(s) under viz package (observed from repository paths and static analysis). Observed top-level classes: CaptureSuccess, CaptureWidget, CapturedException, DragWidget, LatentWidget, PickleWidget. Observed top… |

## Important files

- `Dockerfile` (container)
- `environment.yml` (manifest)
- `requirements.txt` (manifest)
- `scripts/download_models.json` (config)
- `stylegan_human/environment.yml` (manifest)

## Top-level layout

- `stylegan_human` — 128 analysed file(s)
- `torch_utils` — 25 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `training` — 7 analysed file(s)
- `gui_utils` — 6 analysed file(s)
- `viz` — 6 analysed file(s)
- `scripts` — 4 analysed file(s)
- `dnnlib` — 2 analysed file(s)
- `gradio_utils` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File stylegan_human/dnnlib/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File stylegan_human/dnnlib/util.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File stylegan_human/legacy.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File stylegan_human/torch_utils/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File stylegan_human/torch_utils/misc.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File stylegan_human/torch_utils/ops/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File stylegan_human/torch_utils/persistence.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File stylegan_human/training_scripts/sg2/training/dataset.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File stylegan_human/training_scripts/sg2/training/networks.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `336f120ce126aca6f55dc58537e76c10d19eabd0` is the revision these paths and observations refer to.
