# Project structure: lllyasviel/Fooocus

**Analysed commit:** `ae05379cc97bc4361ec8b4ec90193dab21be763f`

**Commit reference:** [ae05379cc97bc4361ec8b4ec90193dab21be763f](https://github.com/lllyasviel/Fooocus/commit/ae05379cc97bc4361ec8b4ec90193dab21be763f)

**Tree at this commit:** [lllyasviel/Fooocus@ae05379cc97b](https://github.com/lllyasviel/Fooocus/tree/ae05379cc97bc4361ec8b4ec90193dab21be763f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lllyasviel/Fooocus |
| Description | Focus on prompting and generating |
| Stars | 53929 |
| Forks | 8624 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `ae05379cc97bc4361ec8b4ec90193dab21be763f` |
| Retrieved at | 2026-11-14T19:06:30.278647+00:00 |
| Files in this snapshot | 324 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (1 files)
    build_container.yml
  CODEOWNERS
  dependabot.yml
css/  (1 files)
  style.css
extras/  (51 files)
  BLIP/  (21 files)
    configs/  (10 files)
      … 10 files under this directory
    models/  (11 files)
      … 11 files under this directory
  GroundingDINO/  (2 files)
    config/  (1 files)
      … 1 files under this directory
    util/  (1 files)
      … 1 files under this directory
  facexlib/  (14 files)
    detection/  (6 files)
      … 6 files under this directory
    parsing/  (4 files)
      … 4 files under this directory
    utils/  (4 files)
      … 4 files under this directory
  safety_checker/  (3 files)
    configs/  (2 files)
      … 2 files under this directory
    models/  (1 files)
      … 1 files under this directory
  sam/  (1 files)
    predictor.py
  censor.py
  expansion.py
  face_crop.py
  inpaint_mask.py
  interrogate.py
  ip_adapter.py
  preprocessors.py
  resampler.py
  vae_interpose.py
  wd14tagger.py
javascript/  (7 files)
  contextMenus.js
  edit-attention.js
  imageviewer.js
  localization.js
  script.js
  viewer.js
  zoom.js
language/  (2 files)
  en.json
  example.json
ldm_patched/  (141 files)
  contrib/  (25 files)
    external.py
    external_align_your_steps.py
    external_canny.py
    external_clip_sdxl.py
    external_compositing.py
    external_custom_sampler.py
    external_freelunch.py
    external_hypernetwork.py
    external_hypertile.py
    external_images.py
    external_latent.py
    external_mask.py
    external_model_advanced.py
    external_model_downscale.py
    external_model_merging.py
    external_perpneg.py
    external_photomaker.py
    external_post_processing.py
    external_rebatch.py
    external_sag.py
    external_sdupscale.py
    external_stable3d.py
    external_tomesd.py
    external_upscale_model.py
    … 1 more files
  controlnet/  (1 files)
    cldm.py
  k_diffusion/  (2 files)
    sampling.py
    utils.py
  ldm/  (15 files)
    models/  (1 files)
      … 1 files under this directory
    modules/  (13 files)
      … 13 files under this directory
    util.py
  licenses-3rd/  (7 files)
    chainer
    comfyui
    diffusers
    kdiffusion
    ldm
    taesd
    transformers
  modules/  (35 files)
    sd1_tokenizer/  (2 files)
      … 2 files under this directory
    args_parser.py
    checkpoint_pickle.py
    clip_config_bigg.json
    clip_model.py
    clip_vision.py
    clip_vision_config_g.json
    clip_vision_config_h.json
    clip_vision_config_vitl.json
    conds.py
    controlnet.py
    diffusers_convert.py
    diffusers_load.py
    gligen.py
    latent_formats.py
    lora.py
    model_base.py
    model_detection.py
    model_management.py
    model_patcher.py
    model_sampling.py
    ops.py
    options.py
    sample.py
    samplers.py
    … 9 more files
  pfn/  (51 files)
    architecture/  (48 files)
      … 48 files under this directory
    __init__.py
    model_loading.py
    types.py
  t2ia/  (1 files)
    adapter.py
  taesd/  (1 files)
    taesd.py
  unipc/  (1 files)
    uni_pc.py
  utils/  (2 files)
    latent_visualization.py
    path_utils.py
models/  (32 files)
  checkpoints/  (1 files)
    put_checkpoints_here
  clip/  (1 files)
    put_clip_or_text_encoder_models_here
  clip_vision/  (1 files)
    put_clip_vision_models_here
  configs/  (11 files)
    anything_v3.yaml
    v1-inference.yaml
    v1-inference_clip_skip_2.yaml
    v1-inference_clip_skip_2_fp16.yaml
    v1-inference_fp16.yaml
    v1-inpainting-inference.yaml
    v2-inference-v.yaml
    v2-inference-v_fp32.yaml
    v2-inference.yaml
    v2-inference_fp32.yaml
    v2-inpainting-inference.yaml
  controlnet/  (1 files)
    put_controlnets_and_t2i_here
  diffusers/  (1 files)
    put_diffusers_models_here
  embeddings/  (1 files)
    put_embeddings_or_textual_inversion_concepts_here
  gligen/  (1 files)
    put_gligen_models_here
  hypernetworks/  (1 files)
    put_hypernetworks_here
  inpaint/  (1 files)
    put_inpaint_here
  loras/  (1 files)
    put_loras_here
  prompt_expansion/  (5 files)
    fooocus_expansion/  (4 files)
      … 4 files under this directory
    put_prompt_expansion_here
  safety_checker/  (1 files)
    put_safety_checker_models_here
  style_models/  (1 files)
    put_t2i_style_model_here
  unet/  (1 files)
    put_unet_files_here
  upscale_models/  (1 files)
    put_esrgan_and_other_upscale_models_here
  vae/  (1 files)
    put_vae_here
  vae_approx/  (1 files)
    put_taesd_encoder_pth_and_taesd_decoder_pth_here
modules/  (30 files)
  __init__.py
  anisotropic.py
  async_worker.py
  auth.py
  config.py
  constants.py
  core.py
  default_pipeline.py
  extra_utils.py
  flags.py
  gradio_hijack.py
  hash_cache.py
  html.py
  inpaint_worker.py
  launch_util.py
  localization.py
  lora.py
  meta_parser.py
  model_loader.py
  ops.py
  patch.py
  patch_clip.py
  patch_precision.py
  private_logger.py
  … 6 more files
presets/  (9 files)
  .gitignore
  anime.json
  default.json
  lcm.json
  lightning.json
  playground_v2.5.json
  pony_v6.json
  realistic.json
  sai.json
sdxl_styles/  (6 files)
  sdxl_styles_diva.json
  sdxl_styles_fooocus.json
  sdxl_styles_marc_k3nt3l.json
  sdxl_styles_mre.json
  sdxl_styles_sai.json
  sdxl_styles_twri.json
tests/  (3 files)
  __init__.py
  test_extra_utils.py
  test_utils.py
wildcards/  (8 files)
  .gitignore
  animal.txt
  artist.txt
  color.txt
  color_flower.txt
  extended-color.txt
  flower.txt
  nationality.txt
.dockerignore
.gitattributes
.gitignore
Dockerfile
LICENSE
args_manager.py
auth-example.json
build_launcher.py
development.md
docker-compose.yml
docker.md
entry_with_update.py
entrypoint.sh
environment.yaml
experiments_expansion.py
experiments_face.py
experiments_interrogate.py
experiments_mask_generation.py
fooocus_colab.ipynb
fooocus_version.py
launch.py
readme.md
requirements_docker.txt
requirements_versions.txt
… 4 more files
```

## Entry points

- [extras/facexlib/detection/matlab_cp2tform.py:235](https://github.com/lllyasviel/Fooocus/blob/ae05379cc97bc4361ec8b4ec90193dab21be763f/extras/facexlib/detection/matlab_cp2tform.py#L235)
- [extras/facexlib/utils/face_utils.py:211](https://github.com/lllyasviel/Fooocus/blob/ae05379cc97bc4361ec8b4ec90193dab21be763f/extras/facexlib/utils/face_utils.py#L211)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 60 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: add_ratio, download_sam_model, downloading_controlnet_canny, downloading_controlne… |
| Core modules | core | Observed | Groups 12 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: build_launcher, download_models, dump_default_english_config, generate_clicked, get_task, ini_args. |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AbstractAutoencoder, Attention, AttnBlock, AutoencoderKL, AutoencodingEngine, AutoencodingEngineLegacy… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: MatlabCp2tormException. Observed top-level functions: align_crop_face_landmarks, compute_i… |
| extras package | library | Observed | Groups 24 file(s) under extras package (observed from repository paths and static analysis). Observed top-level classes: AttentionRefinementModule, BasicBlock, BboxHead, BiSeNet, BiSeNetOutput, Censor. Observed top-leve… |
| javascript package | library | Observed | Groups 7 file(s) under javascript package (observed from repository paths and static analysis). |
| ldm_patched package | library | Observed | Groups 109 file(s) under ldm_patched package (observed from repository paths and static analysis). Observed top-level classes: AE3DConv, AbstractDistribution, AbstractLowScaleModel, AdaConvGuidedFilter, AdaGuidedFilter,… |
| modules package | library | Observed | Groups 29 file(s) under modules package (observed from repository paths and static analysis). Observed top-level classes: A1111MetadataParser, AsyncTask, BilateralBlur, BrownianTreeNoiseSamplerPatched, EarlyReturnExcept… |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestUtils. |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build_container.yml` (ci)
- `Dockerfile` (container)
- `auth-example.json` (config)
- `docker-compose.yml` (container)
- `environment.yaml` (config)
- `extras/BLIP/configs/bert_config.json` (config)
- `extras/BLIP/configs/caption_coco.yaml` (config)
- `extras/BLIP/configs/med_config.json` (config)
- `extras/BLIP/configs/nlvr.yaml` (config)
- `extras/BLIP/configs/nocaps.yaml` (config)
- `extras/BLIP/configs/pretrain.yaml` (config)
- `extras/BLIP/configs/retrieval_coco.yaml` (config)
- `extras/BLIP/configs/retrieval_flickr.yaml` (config)
- `extras/BLIP/configs/retrieval_msrvtt.yaml` (config)
- `extras/BLIP/configs/vqa.yaml` (config)
- `extras/BLIP/models/bert_tokenizer/config.json` (config)
- `extras/BLIP/models/bert_tokenizer/tokenizer_config.json` (config)
- `extras/safety_checker/configs/config.json` (config)
- `extras/safety_checker/configs/preprocessor_config.json` (config)
- `language/en.json` (config)
- `language/example.json` (config)
- `ldm_patched/modules/clip_config_bigg.json` (config)
- `ldm_patched/modules/clip_vision_config_g.json` (config)
- `ldm_patched/modules/clip_vision_config_h.json` (config)
- `ldm_patched/modules/clip_vision_config_vitl.json` (config)
- `ldm_patched/modules/sd1_clip_config.json` (config)
- `ldm_patched/modules/sd1_tokenizer/special_tokens_map.json` (config)
- `ldm_patched/modules/sd1_tokenizer/tokenizer_config.json` (config)
- `ldm_patched/modules/sd2_clip_config.json` (config)
- `models/configs/anything_v3.yaml` (config)
- `models/configs/v1-inference.yaml` (config)
- `models/configs/v1-inference_clip_skip_2.yaml` (config)
- `models/configs/v1-inference_clip_skip_2_fp16.yaml` (config)
- `models/configs/v1-inference_fp16.yaml` (config)
- `models/configs/v1-inpainting-inference.yaml` (config)
- `models/configs/v2-inference-v.yaml` (config)
- `models/configs/v2-inference-v_fp32.yaml` (config)
- `models/configs/v2-inference.yaml` (config)
- `models/configs/v2-inference_fp32.yaml` (config)
- `models/configs/v2-inpainting-inference.yaml` (config)
- `models/prompt_expansion/fooocus_expansion/config.json` (config)
- `models/prompt_expansion/fooocus_expansion/special_tokens_map.json` (config)
- `models/prompt_expansion/fooocus_expansion/tokenizer_config.json` (config)
- `presets/anime.json` (config)
- `presets/default.json` (config)
- `presets/lcm.json` (config)
- `presets/lightning.json` (config)
- `presets/playground_v2.5.json` (config)
- `presets/pony_v6.json` (config)
- `presets/realistic.json` (config)
- `presets/sai.json` (config)
- `requirements_docker.txt` (manifest)
- `requirements_versions.txt` (manifest)
- `sdxl_styles/sdxl_styles_diva.json` (config)
- `sdxl_styles/sdxl_styles_fooocus.json` (config)
- `sdxl_styles/sdxl_styles_marc_k3nt3l.json` (config)
- `sdxl_styles/sdxl_styles_mre.json` (config)
- `sdxl_styles/sdxl_styles_sai.json` (config)
- `sdxl_styles/sdxl_styles_twri.json` (config)

## Top-level layout

- `ldm_patched` — 141 analysed file(s)
- `extras` — 51 analysed file(s)
- `models` — 32 analysed file(s)
- `modules` — 30 analysed file(s)
- `(root files)` — 28 analysed file(s)
- `presets` — 9 analysed file(s)
- `wildcards` — 8 analysed file(s)
- `javascript` — 7 analysed file(s)
- `.github` — 6 analysed file(s)
- `sdxl_styles` — 6 analysed file(s)
- `tests` — 3 analysed file(s)
- `language` — 2 analysed file(s)
- `css` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ae05379cc97bc4361ec8b4ec90193dab21be763f` is the revision these paths and observations refer to.
