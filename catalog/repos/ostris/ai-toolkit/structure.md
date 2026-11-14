# Project structure: ostris/ai-toolkit

**Analysed commit:** `d6a18ad72da9abca3ffb67ea8e42c25764eee61a`

**Commit reference:** [d6a18ad72da9abca3ffb67ea8e42c25764eee61a](https://github.com/ostris/ai-toolkit/commit/d6a18ad72da9abca3ffb67ea8e42c25764eee61a)

**Tree at this commit:** [ostris/ai-toolkit@d6a18ad72da9](https://github.com/ostris/ai-toolkit/tree/d6a18ad72da9abca3ffb67ea8e42c25764eee61a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ostris/ai-toolkit |
| Description | The ultimate training toolkit for finetuning diffusion models |
| Stars | 12629 |
| Forks | 1621 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `d6a18ad72da9abca3ffb67ea8e42c25764eee61a` |
| Retrieved at | 2026-11-14T19:10:05.656413+00:00 |
| Files in this snapshot | 688 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (1 files)
    stale-issues.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
.vscode/  (1 files)
  launch.json
assets/  (1 files)
  glif.svg
config/  (25 files)
  examples/  (25 files)
    modal/  (2 files)
      … 2 files under this directory
    extract.example.yml
    generate.example.yaml
    mod_lora_scale.yaml
    train_flex_redux.yaml
    train_full_fine_tune_flex.yaml
    train_full_fine_tune_lumina.yaml
    train_lora_chroma_24gb.yaml
    train_lora_flex2_24gb.yaml
    train_lora_flex_24gb.yaml
    train_lora_flux_24gb.yaml
    train_lora_flux_kontext_24gb.yaml
    train_lora_flux_schnell_24gb.yaml
    train_lora_hidream_48.yaml
    train_lora_lumina.yaml
    train_lora_omnigen2_24gb.yaml
    train_lora_qwen_image_24gb.yaml
    train_lora_qwen_image_edit_2509_32gb.yaml
    train_lora_qwen_image_edit_32gb.yaml
    train_lora_sd35_large_24gb.yaml
    train_lora_wan21_14b_24gb.yaml
    train_lora_wan21_1b_24gb.yaml
    train_lora_wan22_14b_24gb.yaml
    train_slider.example.yml
docker/  (2 files)
  Dockerfile
  start.sh
extensions/  (3 files)
  example/  (3 files)
    config/  (1 files)
      … 1 files under this directory
    ExampleMergeModels.py
    __init__.py
extensions_built_in/  (286 files)
  advanced_generator/  (5 files)
    config/  (1 files)
      … 1 files under this directory
    Img2ImgGenerator.py
    PureLoraGenerator.py
    ReferenceGenerator.py
    __init__.py
  audio_models/  (21 files)
    ace_step/  (5 files)
      … 5 files under this directory
    yue2/  (13 files)
      … 13 files under this directory
    __init__.py
    base_audio_model.py
    ui.tsx
  captioner/  (14 files)
    prompts/  (4 files)
      … 4 files under this directory
    AceStepCaptioner.py
    BaseCaptioner.py
    Ideogram4Captioner.py
    MossMusicCaptioner.py
    Qwen25OmniCaptioner.py
    Qwen32Captioner.py
    Qwen38Captioner.py
    Qwen3OmniCaptioner.py
    Qwen3VLCaptioner.py
    __init__.py
  concept_replacer/  (3 files)
    config/  (1 files)
      … 1 files under this directory
    ConceptReplacer.py
    __init__.py
  concept_slider/  (2 files)
    ConceptSliderTrainer.py
    __init__.py
  dataset_tools/  (10 files)
    tools/  (6 files)
      … 6 files under this directory
    DatasetTools.py
    SuperTagger.py
    SyncFromCollection.py
    __init__.py
  diffusion_models/  (198 files)
    anima/  (2 files)
      … 2 files under this directory
    boogu_image/  (10 files)
      … 10 files under this directory
    chroma/  (9 files)
      … 9 files under this directory
    ernie_image/  (3 files)
      … 3 files under this directory
    example_model/  (6 files)
      … 6 files under this directory
    f_light/  (5 files)
      … 5 files under this directory
    fibo2/  (8 files)
      … 8 files under this directory
    flux2/  (7 files)
      … 7 files under this directory
    flux3/  (9 files)
      … 9 files under this directory
    flux_kontext/  (2 files)
      … 2 files under this directory
    hidream/  (19 files)
      … 19 files under this directory
    ideogram4/  (6 files)
      … 6 files under this directory
    iris3b/  (7 files)
      … 7 files under this directory
    krea2/  (6 files)
      … 6 files under this directory
    ltx2/  (3 files)
      … 3 files under this directory
    mageflow/  (8 files)
      … 8 files under this directory
    ming_image/  (10 files)
      … 10 files under this directory
    minimax_h3/  (15 files)
      … 15 files under this directory
    moss_image/  (6 files)
      … 6 files under this directory
    nucleus_image/  (2 files)
      … 2 files under this directory
    omnigen2/  (23 files)
      … 23 files under this directory
    prx_pixel_t2i/  (6 files)
      … 6 files under this directory
    qwen_image/  (5 files)
      … 5 files under this directory
    qwen_image_2/  (7 files)
      … 7 files under this directory
    wan22/  (5 files)
      … 5 files under this directory
    z_image/  (3 files)
      … 3 files under this directory
    zeta_chroma/  (4 files)
      … 4 files under this directory
    __init__.py
    ui.tsx
  flex2/  (4 files)
    __init__.py
    flex2.py
    pipeline.py
    ui.tsx
  image_reference_slider_trainer/  (3 files)
    config/  (1 files)
      … 1 files under this directory
    ImageReferenceSliderTrainerProcess.py
    __init__.py
  inference_engine/  (9 files)
    InferenceEngine.py
    PLANNING.md
    README.md
    __init__.py
    engine.py
    latent_format_tables.py
    latent_preview.py
    protocol.py
    server.py
  llm_models/  (9 files)
    src/  (5 files)
      … 5 files under this directory
    __init__.py
    qwen25_omni.py
    qwen38.py
    ui.tsx
  sd_trainer/  (5 files)
    config/  (1 files)
      … 1 files under this directory
    DiffusionTrainer.py
    SDTrainer.py
    UITrainer.py
    __init__.py
  ultimate_slider_trainer/  (3 files)
    config/  (1 files)
      … 1 files under this directory
    UltimateSliderTrainerProcess.py
    __init__.py
jobs/  (28 files)
  process/  (20 files)
    models/  (2 files)
      … 2 files under this directory
    BaseExtensionProcess.py
    BaseExtractProcess.py
    BaseMergeProcess.py
    BaseProcess.py
    BaseSDTrainProcess.py
    BaseTrainProcess.py
    ExtractLoconProcess.py
    ExtractLoraProcess.py
    GenerateProcess.py
    MergeLoconProcess.py
    ModRescaleLoraProcess.py
    TrainESRGANProcess.py
    TrainFineTuneProcess.py
    TrainSDRescaleProcess.py
    TrainSliderProcess.py
    TrainSliderProcessOld.py
    TrainVAEProcess.py
    __init__.py
  BaseJob.py
  ExtensionJob.py
  ExtractJob.py
  GenerateJob.py
  MergeJob.py
  ModJob.py
  TrainJob.py
  __init__.py
manager/  (16 files)
  README.md
  __init__.py
  __main__.py
  detect.py
  doctor.py
  env.py
  ffmpeg.py
  gitops.py
  gitwin.py
  launch.py
  migrations.py
  nodejs.py
  sparkdeps.py
  spec.py
  util.py
  uvbin.py
notebooks/  (3 files)
  FLUX_1_dev_LoRA_Training.ipynb
  FLUX_1_schnell_LoRA_Training.ipynb
  SliderTraining.ipynb
output/  (1 files)
  .gitkeep
scripts/  (17 files)
  add_mask_dataset.py
  calculate_timestep_weighing_flex.py
  caption_audio_dataset.py
  convert_cog.py
  convert_diffusers_to_comfy.py
  convert_diffusers_to_comfy_transformer_only.py
  convert_lora_to_peft_format.py
  convert_melbandroformer.py
  convert_vllm_to_comfy.py
  extract_lora_from_flex.py
  generate_sampler_step_scales.py
  make_diffusers_model.py
  make_lcm_sdxl_model.py
  patch_te_adapter.py
  repair_dataset_folder.py
  test_quantizations.py
  update_sponsors.py
testing/  (18 files)
  compare_keys.py
  generate_lora_mapping.py
  generate_weight_mappings.py
  merge_in_text_encoder_adapter.py
  shrink_pixart.py
  shrink_pixart2.py
  shrink_pixart_sm.py
  shrink_pixart_sm2.py
  shrink_pixart_sm3.py
  stage_profiler.py
  test_bucket_dataloader.py
  test_inference_engine.py
  test_lora_compile_scalars.py
  test_ltx_dataloader.py
  test_model_load_save.py
  test_model_loading.py
  test_vae.py
  test_vae_cycle.py
toolkit/  (216 files)
  audio/  (14 files)
    melbandroformer/  (6 files)
      … 6 files under this directory
    moss_music/  (5 files)
      … 5 files under this directory
    album_artwork.py
    make_video.py
    preserve_pitch.py
  data_transfer_object/  (1 files)
    data_loader.py
  keymaps/  (6 files)
    stable_diffusion_refiner_unmatched.json
    stable_diffusion_sd1.json
    stable_diffusion_sd2.json
    stable_diffusion_sd2_unmatched.json
    stable_diffusion_sdxl_unmatched.json
    stable_diffusion_ssd_unmatched.json
  memory_management/  (4 files)
    __init__.py
    manager.py
    manager_modules.py
    test_memory_manager.py
  models/  (85 files)
    loaders/  (2 files)
      … 2 files under this directory
    v2/  (41 files)
      … 41 files under this directory
    wan21/  (7 files)
      … 7 files under this directory
    DoRA.py
    FakeVAE.py
    LoRAFormer.py
    RRDB.py
    auraflow.py
    autoencoder_tiny_with_pooled_exits.py
    base_model.py
    block.py
    clip_fusion.py
    clip_pre_processor.py
    cogview4.py
    control_lora_adapter.py
    decorator.py
    diffusion_feature_extraction.py
    flux.py
    flux_sage_attn.py
    i2v_adapter.py
    ilora.py
    ilora2.py
    llm_adapter.py
    lokr.py
    mean_flow_adapter.py
    pixtral_vision.py
    redux.py
    … 11 more files
  optimizers/  (11 files)
    adafactor.py
    adam8bit.py
    adamconvrot.py
    automagic.py
    automagic2.py
    automagic3.py
    automagic4.py
    automagicEXPERIMENT.py
    optimizer_utils.py
    prodigy_8bit.py
    test_optimizers.py
  orig_configs/  (1 files)
    sd_xl_refiner.yaml
  samplers/  (3 files)
    custom_flowmatch_sampler.py
    custom_lcm_scheduler.py
    mean_flow_scheduler.py
  timestep_weighing/  (2 files)
    __init__.py
    default_weighing_scheme.py
  util/  (24 files)
    band_loss.svg
    blended_blur_noise.py
    comfy_quant_export.py
    comfy_quant_import.py
    convrot_quant.py
    convrot_w4a8_quant.py
    float8_quant.py
    get_model.py
    inverse_cfg.py
    ip_adapter_utils.py
    losses.py
    mask.py
    mixed_precision.py
    nvfp4_quant.py
    orbit_quant.py
    orbit_vq_quant.py
    ostris_quant.py
    quantize.py
    qwen_vae_gradient_checkpointing.py
    shuffle.py
    streamed_safetensors.py
    uintx_quant.py
    unified_memory.py
    vae.py
  __init__.py
  accelerator.py
  advanced_prompt_embeds.py
  assistant_lora.py
  basic.py
  buckets.py
  civitai.py
  clip_vision_adapter.py
  config.py
  config_modules.py
  control_generator.py
  cuda_malloc.py
  custom_adapter.py
  data_loader.py
  dataloader_mixins.py
  dequantize.py
  dto.py
  ema.py
  embedding.py
  esrgan_utils.py
  extension.py
  guidance.py
  ideogram_caption.py
  image_utils.py
  … 41 more files
ui/  (47 files)
  cron/  (7 files)
    actions/  (2 files)
      … 2 files under this directory
    fileServer.ts
    paths.ts
    prisma.ts
    pythonPath.ts
    worker.ts
  prisma/  (1 files)
    schema.prisma
  public/  (5 files)
    file.svg
    globe.svg
    next.svg
    vercel.svg
    window.svg
  src/  (29 files)
    app/  (29 files)
      … 29 files under this directory
  .gitignore
  README.md
  next.config.ts
  package.json
  postcss.config.mjs
.gitignore
.gitmodules
FAQ.md
LICENSE
README.md
build_and_push_docker
build_and_push_docker_dev
docker-compose.yml
flux_train_ui.py
info.py
requirements.txt
requirements_base.txt
run.py
run_linux.sh
run_mac.zsh
run_modal.py
run_windows.bat
spark_requirements.txt
tsconfig.json
```

## Entry points

- [extensions_built_in/audio_models/ace_step/src/model.py:1584](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/extensions_built_in/audio_models/ace_step/src/model.py#L1584)
- [extensions_built_in/diffusion_models/f_light/src/model.py:445](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/extensions_built_in/diffusion_models/f_light/src/model.py#L445)
- [extensions_built_in/inference_engine/server.py:25](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/extensions_built_in/inference_engine/server.py#L25)
- [flux_train_ui.py:413](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/flux_train_ui.py#L413)
- [manager/__main__.py:248](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/manager/__main__.py#L248)
- [run.py:150](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/run.py#L150)
- [run_modal.py:144](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/run_modal.py#L144)
- [scripts/add_mask_dataset.py:255](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/scripts/add_mask_dataset.py#L255)
- [scripts/caption_audio_dataset.py:308](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/scripts/caption_audio_dataset.py#L308)
- [scripts/convert_cog.py:93](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/scripts/convert_cog.py#L93)
- [scripts/convert_melbandroformer.py:126](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/scripts/convert_melbandroformer.py#L126)
- [scripts/convert_vllm_to_comfy.py:343](https://github.com/ostris/ai-toolkit/blob/d6a18ad72da9abca3ffb67ea8e42c25764eee61a/scripts/convert_vllm_to_comfy.py#L343)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 28 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 45 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: get_config, get_cwd_abs_path, preprocess_config, replace_env_vars_in_string. |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 104 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AggressiveWanI2VUnloadPipeline, AggressiveWanUnloadPipeline, AnimaTextConditioner, Attention, Attenti… |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 24 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: AceStep15, ArchHandler, Attention, Autoe… |
| extensions package | library | Observed | Groups 2 file(s) under extensions package (observed from repository paths and static analysis). Observed top-level classes: ExampleMergeExtension, ExampleMergeModels, ModelInputConfig. Observed top-level functions: flus… |
| extensions_built_in package | library | Observed | Groups 256 file(s) under extensions_built_in package (observed from repository paths and static analysis). Observed top-level classes: AMPBlock, APGConfig, ARDecodeGraph, AbcRepairError, AceStep15Model, AceStep15Pipelin… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| jobs package | library | Observed | Groups 26 file(s) under jobs package (observed from repository paths and static analysis). Observed top-level classes: ACTION_TYPES_SLIDER, BaseExtensionProcess, BaseExtractProcess, BaseJob, BaseMergeProcess, BaseProces… |
| manager package | library | Observed | Groups 14 file(s) under manager package (observed from repository paths and static analysis). Observed top-level classes: EnvSpec. Observed top-level functions: _asset, _build_spec, _check, _cuda_flavor, _cuda_spec, _di… |
| scripts package | library | Observed | Groups 10 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: extract_diff, flush, is_in_diffusers_map, scale_weights_to_8bit, stochastic_round_to, swap_scal… |
| testing package | library | Observed | Groups 10 file(s) under testing package (observed from repository paths and static analysis). Observed top-level classes: StageProfiler, _Sampler. Observed top-level functions: export_state_dict, flush, get_reduced_shap… |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AdapterScaleTest, Client, FakeAdapter, FakeSD, RamMonitor, Transformer. Observed top-level functions: _fini… |
| toolkit package | library | Observed | Groups 105 file(s) under toolkit package (observed from repository paths and static analysis). Observed top-level classes: ACTION_TYPES_SLIDER, Adafactor, Adam8bit, AdamConvRot, AdapterConfig, AdvancedPromptEmbeds. Obse… |
| ui package | library | Observed | Groups 10 file(s) under ui package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/stale-issues.yml` (ci)
- `.vscode/launch.json` (config)
- `config/examples/extract.example.yml` (config)
- `config/examples/generate.example.yaml` (config)
- `config/examples/mod_lora_scale.yaml` (config)
- `config/examples/modal/modal_train_lora_flux_24gb.yaml` (config)
- `config/examples/modal/modal_train_lora_flux_schnell_24gb.yaml` (config)
- `config/examples/train_flex_redux.yaml` (config)
- `config/examples/train_full_fine_tune_flex.yaml` (config)
- `config/examples/train_full_fine_tune_lumina.yaml` (config)
- `config/examples/train_lora_chroma_24gb.yaml` (config)
- `config/examples/train_lora_flex2_24gb.yaml` (config)
- `config/examples/train_lora_flex_24gb.yaml` (config)
- `config/examples/train_lora_flux_24gb.yaml` (config)
- `config/examples/train_lora_flux_kontext_24gb.yaml` (config)
- `config/examples/train_lora_flux_schnell_24gb.yaml` (config)
- `config/examples/train_lora_hidream_48.yaml` (config)
- `config/examples/train_lora_lumina.yaml` (config)
- `config/examples/train_lora_omnigen2_24gb.yaml` (config)
- `config/examples/train_lora_qwen_image_24gb.yaml` (config)
- `config/examples/train_lora_qwen_image_edit_2509_32gb.yaml` (config)
- `config/examples/train_lora_qwen_image_edit_32gb.yaml` (config)
- `config/examples/train_lora_sd35_large_24gb.yaml` (config)
- `config/examples/train_lora_wan21_14b_24gb.yaml` (config)
- `config/examples/train_lora_wan21_1b_24gb.yaml` (config)
- `config/examples/train_lora_wan22_14b_24gb.yaml` (config)
- `config/examples/train_slider.example.yml` (config)
- `docker-compose.yml` (container)
- `docker/Dockerfile` (container)
- `extensions/example/config/config.example.yaml` (config)
- `extensions_built_in/advanced_generator/config/train.example.yaml` (config)
- `extensions_built_in/concept_replacer/config/train.example.yaml` (config)
- `extensions_built_in/image_reference_slider_trainer/config/train.example.yaml` (config)
- `extensions_built_in/sd_trainer/config/train.example.yaml` (config)
- `extensions_built_in/ultimate_slider_trainer/config/train.example.yaml` (config)
- `requirements.txt` (manifest)
- `requirements_base.txt` (manifest)
- `toolkit/keymaps/stable_diffusion_refiner_unmatched.json` (config)
- `toolkit/keymaps/stable_diffusion_sd1.json` (config)
- `toolkit/keymaps/stable_diffusion_sd2.json` (config)
- `toolkit/keymaps/stable_diffusion_sd2_unmatched.json` (config)
- `toolkit/keymaps/stable_diffusion_sdxl_unmatched.json` (config)
- `toolkit/keymaps/stable_diffusion_ssd_unmatched.json` (config)
- `toolkit/orig_configs/sd_xl_refiner.yaml` (config)
- `tsconfig.json` (config)
- `ui/package.json` (manifest)

## Top-level layout

- `extensions_built_in` — 286 analysed file(s)
- `toolkit` — 216 analysed file(s)
- `ui` — 47 analysed file(s)
- `jobs` — 28 analysed file(s)
- `config` — 25 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `testing` — 18 analysed file(s)
- `scripts` — 17 analysed file(s)
- `manager` — 16 analysed file(s)
- `.github` — 5 analysed file(s)
- `extensions` — 3 analysed file(s)
- `notebooks` — 3 analysed file(s)
- `docker` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `assets` — 1 analysed file(s)
- `output` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d6a18ad72da9abca3ffb67ea8e42c25764eee61a` is the revision these paths and observations refer to.
