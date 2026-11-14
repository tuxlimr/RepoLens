# Project structure: modelscope/DiffSynth-Studio

**Analysed commit:** `28638042df62d206486a8bcff3ef22973c84e414`

**Commit reference:** [28638042df62d206486a8bcff3ef22973c84e414](https://github.com/modelscope/DiffSynth-Studio/commit/28638042df62d206486a8bcff3ef22973c84e414)

**Tree at this commit:** [modelscope/DiffSynth-Studio@28638042df62](https://github.com/modelscope/DiffSynth-Studio/tree/28638042df62d206486a8bcff3ef22973c84e414)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | modelscope/DiffSynth-Studio |
| Description | Enjoy the magic of Diffusion models! |
| Stars | 13367 |
| Forks | 1335 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `28638042df62d206486a8bcff3ef22973c84e414` |
| Retrieved at | 2026-11-14T19:09:51.220533+00:00 |
| Files in this snapshot | 666 |

## Directory tree

```text
.agents/  (63 files)
  skills/  (63 files)
    diffsynth-analyze-target/  (3 files)
      … 3 files under this directory
    diffsynth-docs/  (2 files)
      … 2 files under this directory
    diffsynth-environment/  (2 files)
      … 2 files under this directory
    diffsynth-integrator/  (8 files)
      … 8 files under this directory
    diffsynth-model-code/  (11 files)
      … 11 files under this directory
    diffsynth-pipeline/  (5 files)
      … 5 files under this directory
    diffsynth-pipeline-lowvram/  (1 files)
      … 1 files under this directory
    diffsynth-pipeline-training/  (5 files)
      … 5 files under this directory
    diffsynth-pr/  (2 files)
      … 2 files under this directory
    diffsynth-pr-review/  (1 files)
      … 1 files under this directory
    diffsynth-style/  (1 files)
      … 1 files under this directory
    diffsynth-testing/  (2 files)
      … 2 files under this directory
    diffsynth-user-dataset/  (2 files)
      … 2 files under this directory
    diffsynth-user-evaluation/  (1 files)
      … 1 files under this directory
    diffsynth-user-inference/  (4 files)
      … 4 files under this directory
    diffsynth-user-research/  (7 files)
      … 7 files under this directory
    diffsynth-user-setup/  (2 files)
      … 2 files under this directory
    diffsynth-user-training/  (4 files)
      … 4 files under this directory
.github/  (1 files)
  workflows/  (1 files)
    publish.yaml
diffsynth/  (315 files)
  configs/  (3 files)
    __init__.py
    model_configs.py
    vram_management_module_maps.py
  core/  (39 files)
    attention/  (9 files)
      … 9 files under this directory
    data/  (3 files)
      … 3 files under this directory
    device/  (2 files)
      … 2 files under this directory
    gradient/  (2 files)
      … 2 files under this directory
    loader/  (4 files)
      … 4 files under this directory
    npu_patch/  (1 files)
      … 1 files under this directory
    offload_training/  (4 files)
      … 4 files under this directory
    quant/  (9 files)
      … 9 files under this directory
    vram/  (4 files)
      … 4 files under this directory
    __init__.py
  diffusion/  (11 files)
    __init__.py
    base_pipeline.py
    ddim_scheduler.py
    dmd2.py
    flow_match.py
    logger.py
    loss.py
    parsers.py
    runner.py
    template.py
    training_module.py
  metrics/  (14 files)
    __init__.py
    aesthetic.py
    base.py
    bioclip.py
    clip.py
    fid.py
    hpsv2.py
    hpsv3.py
    image_reward.py
    lpips.py
    pickscore.py
    qwen_image_bench.py
    unified_reward_2.py
    unified_reward_edit.py
  models/  (127 files)
    ace_step_conditioner.py
    ace_step_dit.py
    ace_step_residual_fsq.py
    ace_step_text_encoder.py
    ace_step_tokenizer.py
    ace_step_vae.py
    aesthetic.py
    anima_dit.py
    bioclip.py
    boogu_image_dit.py
    clip.py
    demucs.py
    diffsynth_music_dit.py
    dinov3_image_encoder.py
    ernie_image_dit.py
    ernie_image_text_encoder.py
    fibo_dit.py
    fid.py
    flux2_dit.py
    flux2_text_encoder.py
    flux2_vae.py
    flux3_dit.py
    flux_controlnet.py
    flux_dit.py
    … 103 more files
  pipelines/  (29 files)
    ace_step.py
    anima_image.py
    boogu_image.py
    diffsynth_music.py
    ernie_image.py
    fibo.py
    flux2_image.py
    flux3_image.py
    flux_image.py
    hidream_o1_image.py
    ideogram4.py
    joyai_image.py
    krea2.py
    lingbot_video.py
    ltx2_audio_video.py
    minimax_h3_audio_video.py
    minimax_h3_image.py
    minimax_music3.py
    moss_image.py
    mova_audio_video.py
    qwen_image.py
    qwen_image_21.py
    qwen_video_edit.py
    sensenova_u1_image.py
    … 5 more files
  utils/  (90 files)
    controlnet/  (3 files)
      … 3 files under this directory
    data/  (5 files)
      … 5 files under this directory
    demucs/  (1 files)
      … 1 files under this directory
    dequantizer/  (1 files)
      … 1 files under this directory
    lora/  (9 files)
      … 9 files under this directory
    music_tools/  (3 files)
      … 3 files under this directory
    quant/  (1 files)
      … 1 files under this directory
    ses/  (3 files)
      … 3 files under this directory
    state_dict_converters/  (60 files)
      … 60 files under this directory
    tile/  (2 files)
      … 2 files under this directory
    xfuser/  (2 files)
      … 2 files under this directory
  __init__.py
  version.py
docs/  (148 files)
  en/  (73 files)
    API_Reference/  (6 files)
      … 6 files under this directory
    Developer_Guide/  (5 files)
      … 5 files under this directory
    Diffusion_Templates/  (4 files)
      … 4 files under this directory
    Model_Details/  (29 files)
      … 29 files under this directory
    Pipeline_Usage/  (9 files)
      … 9 files under this directory
    Research_Tutorial/  (5 files)
      … 5 files under this directory
    Training/  (9 files)
      … 9 files under this directory
    .readthedocs.yaml
    Makefile
    QA.md
    README.md
    conf.py
    index.rst
  zh/  (74 files)
    API_Reference/  (6 files)
      … 6 files under this directory
    Developer_Guide/  (5 files)
      … 5 files under this directory
    Diffusion_Templates/  (4 files)
      … 4 files under this directory
    Model_Details/  (29 files)
      … 29 files under this directory
    Pipeline_Usage/  (9 files)
      … 9 files under this directory
    Research_Tutorial/  (6 files)
      … 6 files under this directory
    Training/  (9 files)
      … 9 files under this directory
    .readthedocs.yaml
    Makefile
    QA.md
    README.md
    conf.py
    index.rst
  requirements.txt
examples/  (135 files)
  ace_step/  (65 files)
    model_inference/  (12 files)
      … 12 files under this directory
    model_inference_low_vram/  (12 files)
      … 12 files under this directory
    model_training/  (41 files)
      … 41 files under this directory
  anima/  (10 files)
    model_inference/  (1 files)
      … 1 files under this directory
    model_inference_low_vram/  (1 files)
      … 1 files under this directory
    model_training/  (7 files)
      … 7 files under this directory
    README.md
  boogu_image/  (21 files)
    model_inference/  (3 files)
      … 3 files under this directory
    model_inference_low_vram/  (3 files)
      … 3 files under this directory
    model_training/  (15 files)
      … 15 files under this directory
  dev_tools/  (4 files)
    compute_dmd2_sigmas.py
    unit_test.py
    webui.py
    webui_train.py
  diffsynth_music/  (5 files)
    model_inference/  (1 files)
      … 1 files under this directory
    model_inference_low_vram/  (1 files)
      … 1 files under this directory
    model_training/  (3 files)
      … 3 files under this directory
  ernie_image/  (12 files)
    model_inference/  (2 files)
      … 2 files under this directory
    model_inference_low_vram/  (2 files)
      … 2 files under this directory
    model_training/  (8 files)
      … 8 files under this directory
  fibo/  (15 files)
    model_inference/  (2 files)
      … 2 files under this directory
    model_inference_low_vram/  (2 files)
      … 2 files under this directory
    model_training/  (10 files)
      … 10 files under this directory
    README.md
  flux/  (3 files)
    model_inference/  (2 files)
      … 2 files under this directory
    README.md
.gitignore
LICENSE
README.md
README_zh.md
```

## Entry points

- [.agents/skills/diffsynth-user-dataset/scripts/check_dataset.py:391](https://github.com/modelscope/DiffSynth-Studio/blob/28638042df62d206486a8bcff3ef22973c84e414/.agents/skills/diffsynth-user-dataset/scripts/check_dataset.py#L391)
- [.agents/skills/diffsynth-user-inference/scripts/probe_environment.py:652](https://github.com/modelscope/DiffSynth-Studio/blob/28638042df62d206486a8bcff3ef22973c84e414/.agents/skills/diffsynth-user-inference/scripts/probe_environment.py#L652)
- [.agents/skills/diffsynth-user-inference/scripts/validate_outputs.py:145](https://github.com/modelscope/DiffSynth-Studio/blob/28638042df62d206486a8bcff3ef22973c84e414/.agents/skills/diffsynth-user-inference/scripts/validate_outputs.py#L145)
- [.agents/skills/diffsynth-user-setup/scripts/probe_environment.py:652](https://github.com/modelscope/DiffSynth-Studio/blob/28638042df62d206486a8bcff3ef22973c84e414/.agents/skills/diffsynth-user-setup/scripts/probe_environment.py#L652)
- [.agents/skills/diffsynth-user-training/scripts/probe_environment.py:652](https://github.com/modelscope/DiffSynth-Studio/blob/28638042df62d206486a8bcff3ef22973c84e414/.agents/skills/diffsynth-user-training/scripts/probe_environment.py#L652)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: MixedQuantizeConfig, ModelConfig, QuantMethodSpec, QuantizeConfig. Observed top-level… |
| Data layer | data | Observed | Groups 136 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AMPBlock1, AbstractDistribution, AceStepAttention, AceStepAudioTokenizer, AceStepConditionEncoder, Ac… |
| diffsynth package | library | Observed | Groups 140 file(s) under diffsynth package (observed from repository paths and static analysis). Observed top-level classes: AceStepPipeline, AceStepUnit_ConditionEmbedder, AceStepUnit_ContextLatentBuilder, AceStepUnit_… |
| Service / domain layer | service | Observed | Groups 33 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AlwaysOnGPUParamOffloader, AttentionBackend, AutoTorchModule, AutoWrappedLinear, AutoWrapp… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: filter_unprocessed_tasks, move_files, run_inference, run_tasks_on_single_GPU, run_train_multi_GPU, run_tra… |

## Important files

- `.agents/skills/diffsynth-integrator/config.yaml` (config)
- `.github/workflows/publish.yaml` (ci)
- `docs/en/.readthedocs.yaml` (config)
- `docs/requirements.txt` (manifest)
- `docs/zh/.readthedocs.yaml` (config)
- `examples/ernie_image/model_training/full/accelerate_config_zero3.yaml` (config)
- `examples/fibo/model_training/full/accelerate_config.yaml` (config)

## Top-level layout

- `diffsynth` — 315 analysed file(s)
- `docs` — 148 analysed file(s)
- `examples` — 135 analysed file(s)
- `.agents` — 63 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `28638042df62d206486a8bcff3ef22973c84e414` is the revision these paths and observations refer to.
