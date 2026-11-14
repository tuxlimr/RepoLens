# Project structure: KlingAIResearch/LivePortrait

**Analysed commit:** `9b294b3d0536135442ea73cb01e6cb3ca7029dd3`

**Commit reference:** [9b294b3d0536135442ea73cb01e6cb3ca7029dd3](https://github.com/KlingAIResearch/LivePortrait/commit/9b294b3d0536135442ea73cb01e6cb3ca7029dd3)

**Tree at this commit:** [KlingAIResearch/LivePortrait@9b294b3d0536](https://github.com/KlingAIResearch/LivePortrait/tree/9b294b3d0536135442ea73cb01e6cb3ca7029dd3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | KlingAIResearch/LivePortrait |
| Description | Bring portraits to life! |
| Stars | 19478 |
| Forks | 2032 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `9b294b3d0536135442ea73cb01e6cb3ca7029dd3` |
| Retrieved at | 2026-11-14T19:08:13.412049+00:00 |
| Files in this snapshot | 129 |

## Directory tree

```text
.vscode/  (1 files)
  settings.json
assets/  (19 files)
  docs/  (11 files)
    changelog/  (8 files)
      … 8 files under this directory
    directory-structure.md
    how-to-install-ffmpeg.md
    speed.md
  gradio/  (7 files)
    gradio_description_animate_clear.md
    gradio_description_animation.md
    gradio_description_retargeting.md
    gradio_description_retargeting_video.md
    gradio_description_upload.md
    gradio_description_upload_animal.md
    gradio_title.md
  .gitignore
pretrained_weights/  (1 files)
  .gitkeep
src/  (96 files)
  config/  (6 files)
    __init__.py
    argument_config.py
    base_config.py
    crop_config.py
    inference_config.py
    models.yaml
  modules/  (9 files)
    __init__.py
    appearance_feature_extractor.py
    convnextv2.py
    dense_motion.py
    motion_extractor.py
    spade_generator.py
    stitching_retargeting_network.py
    util.py
    warping_network.py
  utils/  (77 files)
    dependencies/  (61 files)
      … 61 files under this directory
    __init__.py
    animal_landmark_runner.py
    camera.py
    check_windows_port.py
    crop.py
    cropper.py
    face_analysis_diy.py
    filter.py
    helper.py
    human_landmark_runner.py
    io.py
    retargeting_utils.py
    rprint.py
    timer.py
    video.py
    viz.py
  gradio_pipeline.py
  live_portrait_pipeline.py
  live_portrait_pipeline_animal.py
  live_portrait_wrapper.py
.gitignore
LICENSE
app.py
app_animals.py
inference.py
inference_animals.py
readme.md
readme_zh_cn.md
requirements.txt
requirements_base.txt
requirements_macOS.txt
speed.py
```

## Entry points

- [src/utils/dependencies/XPose/models/UniPose/ops/test.py:81](https://github.com/KlingAIResearch/LivePortrait/blob/9b294b3d0536135442ea73cb01e6cb3ca7029dd3/src/utils/dependencies/XPose/models/UniPose/ops/test.py#L81)
- [src/utils/dependencies/XPose/models/UniPose/swin_transformer.py:695](https://github.com/KlingAIResearch/LivePortrait/blob/9b294b3d0536135442ea73cb01e6cb3ca7029dd3/src/utils/dependencies/XPose/models/UniPose/swin_transformer.py#L695)
- [src/utils/dependencies/XPose/util/box_ops.py:135](https://github.com/KlingAIResearch/LivePortrait/blob/9b294b3d0536135442ea73cb01e6cb3ca7029dd3/src/utils/dependencies/XPose/util/box_ops.py#L135)
- [src/utils/dependencies/insightface/model_zoo/scrfd.py:319](https://github.com/KlingAIResearch/LivePortrait/blob/9b294b3d0536135442ea73cb01e6cb3ca7029dd3/src/utils/dependencies/insightface/model_zoo/scrfd.py#L319)
- [inference.py:65](https://github.com/KlingAIResearch/LivePortrait/blob/9b294b3d0536135442ea73cb01e6cb3ca7029dd3/inference.py#L65)
- [inference_animals.py:65](https://github.com/KlingAIResearch/LivePortrait/blob/9b294b3d0536135442ea73cb01e6cb3ca7029dd3/inference_animals.py#L65)
- [speed.py:194](https://github.com/KlingAIResearch/LivePortrait/blob/9b294b3d0536135442ea73cb01e6cb3ca7029dd3/speed.py#L194)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ArgumentConfig, Config, ConfigDict, CropConfig, DictAction, InferenceConfig. Observe… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: fast_check_ffmpeg, gpu_wrapped_execute_video, partial_fields. |
| Data layer | data | Observed | Groups 27 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Backbone, BackboneBase, BiAttentionBlock, BiMultiHeadAttention, ContrastiveAssign, DeformableTransform… |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BasicLayer, Mlp, PatchEmbed, PatchMerging, SCRFD, SwinTransformer. Observed top-level func… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| gradio_pipeline.py package | library | Observed | Groups 1 file(s) under gradio_pipeline.py package (observed from repository paths and static analysis). Observed top-level classes: GradioPipeline, GradioPipelineAnimal. Observed top-level functions: update_args. |
| live_portrait_pipeline_animal.py package | library | Observed | Groups 1 file(s) under live_portrait_pipeline_animal.py package (observed from repository paths and static analysis). Observed top-level classes: LivePortraitPipelineAnimal. Observed top-level functions: make_abs_path. |
| live_portrait_pipeline.py package | library | Observed | Groups 1 file(s) under live_portrait_pipeline.py package (observed from repository paths and static analysis). Observed top-level classes: LivePortraitPipeline. Observed top-level functions: make_abs_path. |
| live_portrait_wrapper.py package | library | Observed | Groups 1 file(s) under live_portrait_wrapper.py package (observed from repository paths and static analysis). Observed top-level classes: LivePortraitWrapper, LivePortraitWrapperAnimal. |
| modules package | library | Observed | Groups 9 file(s) under modules package (observed from repository paths and static analysis). Observed top-level classes: AppearanceFeatureExtractor, Block, ConvNeXtV2, ConvT2d, Decoder, DenseMotionNetwork. Observed top-… |
| utils package | library | Observed | Groups 42 file(s) under utils package (observed from repository paths and static analysis). Observed top-level classes: ArcFaceONNX, Attribute, CenterCrop, Compose, Cropper, Dict. Observed top-level functions: P2sRt, _e… |

## Important files

- `.vscode/settings.json` (config)
- `requirements.txt` (manifest)
- `requirements_base.txt` (manifest)
- `requirements_macOS.txt` (manifest)
- `src/config/models.yaml` (config)
- `src/utils/dependencies/XPose/models/UniPose/ops/setup.py` (manifest)

## Top-level layout

- `src` — 96 analysed file(s)
- `assets` — 19 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `pretrained_weights` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9b294b3d0536135442ea73cb01e6cb3ca7029dd3` is the revision these paths and observations refer to.
