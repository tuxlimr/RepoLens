# Project structure: Sanster/IOPaint

**Analysed commit:** `61a759fb3f332bacdce8b2813f4837495c9b86e0`

**Commit reference:** [61a759fb3f332bacdce8b2813f4837495c9b86e0](https://github.com/Sanster/IOPaint/commit/61a759fb3f332bacdce8b2813f4837495c9b86e0)

**Tree at this commit:** [Sanster/IOPaint@61a759fb3f33](https://github.com/Sanster/IOPaint/tree/61a759fb3f332bacdce8b2813f4837495c9b86e0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Sanster/IOPaint |
| Description | Image inpainting tool powered by SOTA AI Model. Remove any unwanted object, defect, people from your pictures or erase and replace(powered by stable diffusion) any thing on your pictures. |
| Stars | 23286 |
| Forks | 2566 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `61a759fb3f332bacdce8b2813f4837495c9b86e0` |
| Retrieved at | 2026-11-14T19:07:48.713977+00:00 |
| Files in this snapshot | 302 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    config.yml
    🐛-bug-report.md
    🚀-feature-request.md
  FUNDING.yml
docker/  (2 files)
  CPUDockerfile
  GPUDockerfile
iopaint/  (204 files)
  file_manager/  (4 files)
    __init__.py
    file_manager.py
    storage_backends.py
    utils.py
  model/  (92 files)
    anytext/  (46 files)
      … 46 files under this directory
    brushnet/  (8 files)
      … 8 files under this directory
    helper/  (4 files)
      … 4 files under this directory
    original_sd_configs/  (5 files)
      … 5 files under this directory
    power_paint/  (10 files)
      … 10 files under this directory
    __init__.py
    base.py
    controlnet.py
    ddim_sampler.py
    fcf.py
    instruct_pix2pix.py
    kandinsky.py
    lama.py
    ldm.py
    manga.py
    mat.py
    mi_gan.py
    opencv2.py
    paint_by_example.py
    plms_sampler.py
    sd.py
    sdxl.py
    utils.py
    zits.py
  plugins/  (73 files)
    basicsr/  (5 files)
      … 5 files under this directory
    facexlib/  (16 files)
      … 16 files under this directory
    gfpgan/  (5 files)
      … 5 files under this directory
    segment_anything/  (16 files)
      … 16 files under this directory
    segment_anything2/  (20 files)
      … 20 files under this directory
    __init__.py
    anime_seg.py
    base_plugin.py
    briarmbg.py
    briarmbg2.py
    gfpgan_plugin.py
    gfpganer.py
    interactive_seg.py
    realesrgan.py
    remove_bg.py
    restoreformer.py
  tests/  (21 files)
    .gitignore
    __init__.py
    test_adjust_mask.py
    test_anytext.py
    test_brushnet.py
    test_controlnet.py
    test_instruct_pix2pix.py
    test_load_img.py
    test_low_mem.py
    test_match_histograms.py
    test_model.py
    test_model_md5.py
    test_model_switch.py
    test_outpainting.py
    test_paint_by_example.py
    test_plugins.py
    test_save_exif.py
    test_save_quality.py
    test_sd_model.py
    test_sdxl.py
    utils.py
  __init__.py
  __main__.py
  api.py
  batch_processing.py
  benchmark.py
  cli.py
  const.py
  download.py
  helper.py
  installer.py
  model_manager.py
  runtime.py
  schema.py
  web_config.py
scripts/  (13 files)
  user_scripts/  (6 files)
    win_config.bat
    win_setup.bat
    win_setup_cn.bat
    win_start.bat
    win_start_cn.bat
    win_update.bat
  .gitignore
  README.md
  convert_vae_pt_to_diffusers.py
  environment.yaml
  pack.bat
  pack.sh
  tool.py
web_app/  (70 files)
  src/  (59 files)
    components/  (45 files)
      … 45 files under this directory
    hooks/  (5 files)
      … 5 files under this directory
    lib/  (5 files)
      … 5 files under this directory
    App.tsx
    globals.css
    main.tsx
    vite-env.d.ts
  .eslintrc.cjs
  .gitignore
  README.md
  components.json
  index.html
  package.json
  postcss.config.js
  tailwind.config.js
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
.gitignore
LICENSE
README.md
build_docker.sh
main.py
publish.sh
requirements-dev.txt
requirements.txt
setup.py
```

## Entry points

- [iopaint/__init__.py](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/iopaint/__init__.py)
- [iopaint/__main__.py:3](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/iopaint/__main__.py#L3)
- [iopaint/benchmark.py:100](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/iopaint/benchmark.py#L100)
- [iopaint/cli.py:16](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/iopaint/cli.py#L16)
- [iopaint/model/anytext/cldm/recognizer.py:299](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/iopaint/model/anytext/cldm/recognizer.py#L299)
- [iopaint/model/anytext/ocr_recog/RNN.py:208](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/iopaint/model/anytext/ocr_recog/RNN.py#L208)
- [iopaint/model/anytext/ocr_recog/RecSVTR.py:585](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/iopaint/model/anytext/ocr_recog/RecSVTR.py#L585)
- [iopaint/model/brushnet/brushnet.py:929](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/iopaint/model/brushnet/brushnet.py#L929)
- [iopaint/model/helper/g_diffuser_bot.py:42](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/iopaint/model/helper/g_diffuser_bot.py#L42)
- [iopaint/plugins/facexlib/detection/matlab_cp2tform.py:235](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/iopaint/plugins/facexlib/detection/matlab_cp2tform.py#L235)
- [main.py:3](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/main.py#L3)
- [scripts/convert_vae_pt_to_diffusers.py:213](https://github.com/Sanster/IOPaint/blob/61a759fb3f332bacdce8b2813f4837495c9b86e0/scripts/convert_vae_pt_to_diffusers.py#L213)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: load_requirements. |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AttnBlock, AttnBlock2_0, AutoencoderKL, DDIMSampler, DDPM, DPMSolverSampler. Observed top-level functi… |
| Application entry point | entrypoint | Observed | Groups 12 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Typer. Observed top-level classes: Attention, Block, BrushNetModel,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| iopaint package | library | Observed | Groups 152 file(s) under iopaint package (observed from repository paths and static analysis). Observed top-level classes: ASPP, ASPPDeformable, AbstractDistribution, AbstractEncoder, AbstractLowScaleModel, Activation.… |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: CheckpointMergerPipeline. |
| Tests | test | Observed | Groups 21 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: _save, assert_equal, assert_keys, check_device, convert_controlnet_method_name, extra_info. |
| web_app package | library | Observed | Groups 62 file(s) under web_app package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `iopaint/model/anytext/anytext_sd15.yaml` (config)
- `iopaint/model/original_sd_configs/sd_xl_base.yaml` (config)
- `iopaint/model/original_sd_configs/sd_xl_refiner.yaml` (config)
- `iopaint/model/original_sd_configs/v1-inference.yaml` (config)
- `iopaint/model/original_sd_configs/v2-inference-v.yaml` (config)
- `requirements-dev.txt` (manifest)
- `requirements.txt` (manifest)
- `scripts/environment.yaml` (config)
- `setup.py` (manifest)
- `web_app/components.json` (config)
- `web_app/package.json` (manifest)
- `web_app/tsconfig.json` (config)
- `web_app/tsconfig.node.json` (config)

## Top-level layout

- `iopaint` — 204 analysed file(s)
- `web_app` — 70 analysed file(s)
- `scripts` — 13 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 4 analysed file(s)
- `docker` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `61a759fb3f332bacdce8b2813f4837495c9b86e0` is the revision these paths and observations refer to.
