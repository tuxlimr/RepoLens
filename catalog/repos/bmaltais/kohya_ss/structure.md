# Project structure: bmaltais/kohya_ss

**Analysed commit:** `45088f04af78e11cec5407ff4652ea3ed2c14422`

**Commit reference:** [45088f04af78e11cec5407ff4652ea3ed2c14422](https://github.com/bmaltais/kohya_ss/commit/45088f04af78e11cec5407ff4652ea3ed2c14422)

**Tree at this commit:** [bmaltais/kohya_ss@45088f04af78](https://github.com/bmaltais/kohya_ss/tree/45088f04af78e11cec5407ff4652ea3ed2c14422)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bmaltais/kohya_ss |
| Description | Not provided |
| Stars | 12666 |
| Forks | 1605 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `45088f04af78e11cec5407ff4652ea3ed2c14422` |
| Retrieved at | 2026-11-14T19:10:02.893970+00:00 |
| Files in this snapshot | 343 |

## Directory tree

```text
.cache/  (5 files)
  config/  (1 files)
    .gitkeep
  keras/  (1 files)
    .gitkeep
  nv/  (1 files)
    .gitkeep
  triton/  (1 files)
    .gitkeep
  user/  (1 files)
    .gitkeep
.github/  (4 files)
  workflows/  (2 files)
    docker_publish.yml
    typos.yaml
  FUNDING.yml
  dependabot.yml
.out-of-scope/  (2 files)
  README.md
  musubi-tuner-models.md
.vscode/  (1 files)
  settings.json
assets/  (5 files)
  js/  (4 files)
    icon_button_titles.js
    info_tooltip.js
    localization.js
    script.js
  style.css
config_files/  (2 files)
  accelerate/  (2 files)
    default_config.yaml
    runpod.yaml
dataset/  (4 files)
  images/  (1 files)
    .gitkeep
  logs/  (1 files)
    .gitkeep
  outputs/  (1 files)
    .gitkeep
  regularization/  (1 files)
    .gitkeep
docs/  (26 files)
  Finetuning/  (1 files)
    top_level.md
  Installation/  (4 files)
    pip_linux.md
    pip_windows.md
    uv_linux.md
    uv_windows.md
  LoRA/  (2 files)
    options.md
    top_level.md
  AGENTS.md
  config_README-ja.md
  fine_tune_README_ja.md
  gen_img_README-ja.md
  image_folder_structure.md
  installation_docker.md
  installation_novita.md
  installation_runpod.md
  train_README-ja.md
  train_README-zh.md
  train_README.md
  train_db_README-ja.md
  train_db_README-zh.md
  train_lllite_README-ja.md
  train_lllite_README.md
  train_network_README-ja.md
  train_network_README-zh.md
  train_ti_README-ja.md
  troubleshooting_tesla_v100.md
examples/  (14 files)
  stable_cascade/  (1 files)
    test.toml
  LoRA based finetuning 2 phase.ps1
  caption.ps1
  caption_subfolders.ps1
  finetune_latent.ps1
  kohya-1-folders.ps1
  kohya-3-folders.ps1
  kohya.ps1
  kohya_finetune.ps1
  kohya_new-v3.ps1
  kohya_train_db_fixed_with-reg_SDv2 512 base.ps1
  lucoris extract examples.txt
  pull kohya_ss sd-scripts updates in.md
  word_frequency.ps1
kohya_gui/  (57 files)
  AGENTS.md
  __init__.py
  anima_lllite_gui.py
  basic_caption_gui.py
  blip2_caption_gui.py
  blip_caption_gui.py
  class_accelerate_launch.py
  class_advanced_training.py
  class_anima.py
  class_basic_training.py
  class_command_executor.py
  class_configuration_file.py
  class_flux1.py
  class_folders.py
  class_gui_config.py
  class_huggingface.py
  class_hunyuan_image.py
  class_lora_tab.py
  class_lumina.py
  class_metadata.py
  class_sample_images.py
  class_sd3.py
  class_sdxl_parameters.py
  class_source_model.py
  … 33 more files
localizations/  (5 files)
  Put localization files here.txt
  chinese-sample.json
  en-GB.json
  zh-CN.json
  zh-TW.json
models/  (1 files)
  .keep
presets/  (41 files)
  dreambooth/  (2 files)
    sd3_bdsqlsz_v1.json
    sd3_bdsqlsz_v2.json
  finetune/  (6 files)
    user_presets/  (1 files)
      … 1 files under this directory
    SDXL - AI_Now PagedAdamW8bit v1.0.json
    SDXL - Essenz series by AI_Characters_Training v1.0.json
    adafactor.json
    lion.json
    prepare_presets.md
  lora/  (33 files)
    user_presets/  (1 files)
      … 1 files under this directory
    SDXL - 1 image LoRA v1.0.json
    SDXL - LoHA AI_Characters v1.0.json
    SDXL - LoKR v1.0.json
    SDXL - LoRA AI_Now ADamW v1.0.json
    SDXL - LoRA AI_Now prodigy v1.0.json
    SDXL - LoRA AI_characters standard v1.0.json
    SDXL - LoRA AI_characters standard v1.1.json
    SDXL - LoRA adafactor v1.0.json
    SDXL - LoRA aitrepreneur clothing v1.0.json
    SDXL - LoRA by malcolmrey training v1.0.json
    SDXL - LoRA face dogu_cat v1.0.json
    SDXL - LoRA finetuning phase 1_v1.1.json
    SDXL - LoRA finetuning phase 2_v1.1.json
    SDXL - LoRA kudou-reira dadaptadam v1.0.json
    SDXL - LoRA kudou-reira dadaptadam v1.1.json
    SDXL - LoRA kudou-reira prodigy v4.0.json
    SDXL - edgLoRAXL AI_Now.json
    SDXL - edgLoRAXL.json
    flux1D - adamw8bit fp8.json
    iA3-Prodigy-sd15.json
    ia3-sd15.json
    locon-dadaptation-sdxl.json
    loha-sd15.json
    lokr-sd15.json
    … 8 more files
setup/  (11 files)
  check_local_modules.py
  create_user_files.py
  debug_info.py
  docker_setup.py
  setup_common.py
  setup_linux.py
  setup_runpod.py
  setup_windows.py
  tkinter_preflight.sh
  update_bitsandbytes.py
  validate_requirements.py
test/  (58 files)
  config/  (37 files)
    Diag-OFT-AdamW8bit-toml.json
    DyLoRA-Adafactor-toml.json
    LoKR-AdamW8bit-toml.json
    SDXL-Standard-Adafactor.json
    SDXL-Standard-AdamW.json
    SDXL-Standard-AdamW8bit.json
    Standard-AdamW.json
    Standard-AdamW8bit.json
    TI-AdamW8bit-SDXL.json
    TI-AdamW8bit-toml.json
    TI-AdamW8bit.json
    dataset-finetune.toml
    dataset-masked_loss.toml
    dataset-multires.toml
    dataset.toml
    dreambooth-Adafactor.json
    dreambooth-AdamW.json
    dreambooth-AdamW8bit-masked_loss-toml.json
    dreambooth-AdamW8bit-toml.json
    dreambooth-AdamW8bit.json
    dreambooth-DAdaptAdam.json
    dreambooth-Prodigy-SDXL.json
    dreambooth-Prodigy.json
    dreambooth.json
    … 13 more files
  ft/  (1 files)
    .keep
  img/  (8 files)
    10_darius kawasaki person/  (8 files)
      … 8 files under this directory
  img with spaces/  (8 files)
    10_darius kawasaki person/  (8 files)
      … 8 files under this directory
  log/  (1 files)
    .keep
  logs/  (1 files)
    .keep
  AGENTS.md
  test_allowed_paths.py
tests/  (39 files)
  AGENTS.md
  conftest.py
  test_anima_finetune_gui.py
  test_anima_lllite_gui.py
  test_anima_lora_gui.py
  test_blip2_caption_gui.py
  test_check_torch_native_xpu.py
  test_command_executor.py
  test_configure_accelerate_hf_home.py
  test_dreambooth_folder_creation_gui.py
  test_dreambooth_gui.py
  test_finetune_gui.py
  test_get_executable_path.py
  test_gradio_pin_policy.py
  test_headless_recommendation.py
  test_hunyuan_image_lora_gui.py
  test_info_tooltip_gradio6.py
  test_install_requirements_failure.py
  test_leco_gui.py
  test_loha_lokr_gui.py
  test_lora_gui.py
  test_lora_regularizer_controls.py
  test_lr_warmup_resolve.py
  test_lumina_finetune_gui.py
  … 15 more files
tools/  (28 files)
  AGENTS.md
  analyse_loha.py
  caption.py
  caption_from_filename.py
  cleanup_captions.py
  convert_html_to_md.py
  convert_images_to_hq_jpg.py
  convert_images_to_webp.py
  create_txt_from_images.py
  crop_images_to_n_buckets.py
  dummy_loha.py
  extract loha and lora examples.txt
  extract_locon.py
  extract_loha.ps1
  extract_loha_from_model.py
  extract_lora_from_models-new.py
  extract_model_difference.py
  gradio_theme_builder.py
  group_images.py
  group_images_recommended_size.py
  lcm_convert.py
  lycoris_locon_extract.py
  lycoris_utils.py
  merge_lycoris.py
  … 4 more files
.augmentignore
.dockerignore
.gitattributes
.gitignore
.gitmodules
.hadolint.yml
.python-version
.release
AGENTS.md
Dockerfile
LICENSE.md
README.md
SECURITY.md
_typos.toml
config example.toml
docker-compose.yaml
gui-uv.bat
gui-uv.sh
gui.bat
gui.ps1
gui.sh
kohya_gui.py
kohya_ss_colab.ipynb
local_train.py
… 16 more files
```

## Entry points

- [kohya_gui.py:266](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/kohya_gui.py#L266)
- [local_train.py:90](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/local_train.py#L90)
- [setup/setup_linux.py:45](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/setup/setup_linux.py#L45)
- [setup/setup_runpod.py:78](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/setup/setup_runpod.py#L78)
- [setup/setup_windows.py:270](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/setup/setup_windows.py#L270)
- [setup/update_bitsandbytes.py:48](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/setup/update_bitsandbytes.py#L48)
- [setup/validate_requirements.py:227](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/setup/validate_requirements.py#L227)
- [tools/analyse_loha.py:149](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/tools/analyse_loha.py#L149)
- [tools/caption.py:59](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/tools/caption.py#L59)
- [tools/caption_from_filename.py:79](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/tools/caption_from_filename.py#L79)
- [tools/cleanup_captions.py:38](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/tools/cleanup_captions.py#L38)
- [tools/convert_html_to_md.py:58](https://github.com/bmaltais/kohya_ss/blob/45088f04af78e11cec5407ff4652ea3ed2c14422/tools/convert_html_to_md.py#L58)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 4 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 58 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 28 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ImageProcessor, LocalLoRAModulePlaceholder, LogType, Logger. Observed top-level functions… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| kohya_gui package | library | Observed | Groups 56 file(s) under kohya_gui package (observed from repository paths and static analysis). Observed top-level classes: AccelerateLaunch, AdvancedTraining, BasicTraining, CommandExecutor, ConfigurationFile, Folders.… |
| setup package | library | Observed | Groups 6 file(s) under setup package (observed from repository paths and static analysis). Observed top-level functions: _check_amd_toolkit, _check_hardware_toolkit, _check_intel_oneapi_toolkit, _check_nvidia_toolkit, _… |
| Tests | test | Observed | Groups 97 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH shutil.which, PATCH cpuinfo.get_cpu_info, PATCH shutil.which, PATCH cpuinfo.get_cpu_info, PATCH shutil.which. Ob… |
| tools package | library | Observed | Groups 4 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: cp_weight, cp_weight_from_conv, extract_conv, extract_diff, extract_linear, get_module. |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/docker_publish.yml` (ci)
- `.github/workflows/typos.yaml` (ci)
- `.hadolint.yml` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `_typos.toml` (config)
- `config example.toml` (config)
- `config_files/accelerate/default_config.yaml` (config)
- `config_files/accelerate/runpod.yaml` (config)
- `docker-compose.yaml` (container)
- `examples/stable_cascade/test.toml` (config)
- `localizations/chinese-sample.json` (config)
- `localizations/en-GB.json` (config)
- `localizations/zh-CN.json` (config)
- `localizations/zh-TW.json` (config)
- `presets/dreambooth/sd3_bdsqlsz_v1.json` (config)
- `presets/dreambooth/sd3_bdsqlsz_v2.json` (config)
- `presets/finetune/SDXL - AI_Now PagedAdamW8bit v1.0.json` (config)
- `presets/finetune/SDXL - Essenz series by AI_Characters_Training v1.0.json` (config)
- `presets/finetune/adafactor.json` (config)
- `presets/finetune/lion.json` (config)
- `presets/lora/SDXL - 1 image LoRA v1.0.json` (config)
- `presets/lora/SDXL - LoHA AI_Characters v1.0.json` (config)
- `presets/lora/SDXL - LoKR v1.0.json` (config)
- `presets/lora/SDXL - LoRA AI_Now ADamW v1.0.json` (config)
- `presets/lora/SDXL - LoRA AI_Now prodigy v1.0.json` (config)
- `presets/lora/SDXL - LoRA AI_characters standard v1.0.json` (config)
- `presets/lora/SDXL - LoRA AI_characters standard v1.1.json` (config)
- `presets/lora/SDXL - LoRA adafactor v1.0.json` (config)
- `presets/lora/SDXL - LoRA aitrepreneur clothing v1.0.json` (config)
- `presets/lora/SDXL - LoRA by malcolmrey training v1.0.json` (config)
- `presets/lora/SDXL - LoRA face dogu_cat v1.0.json` (config)
- `presets/lora/SDXL - LoRA finetuning phase 1_v1.1.json` (config)
- `presets/lora/SDXL - LoRA finetuning phase 2_v1.1.json` (config)
- `presets/lora/SDXL - LoRA kudou-reira dadaptadam v1.0.json` (config)
- `presets/lora/SDXL - LoRA kudou-reira dadaptadam v1.1.json` (config)
- `presets/lora/SDXL - LoRA kudou-reira prodigy v4.0.json` (config)
- `presets/lora/SDXL - edgLoRAXL AI_Now.json` (config)
- `presets/lora/SDXL - edgLoRAXL.json` (config)
- `presets/lora/flux1D - adamw8bit fp8.json` (config)
- `presets/lora/iA3-Prodigy-sd15.json` (config)
- `presets/lora/ia3-sd15.json` (config)
- `presets/lora/locon-dadaptation-sdxl.json` (config)
- `presets/lora/loha-sd15.json` (config)
- `presets/lora/lokr-sd15.json` (config)
- `presets/lora/sd15 - EDG_LoConOptiSettings.json` (config)
- `presets/lora/sd15 - EDG_LoHaOptiSettings.json` (config)
- `presets/lora/sd15 - EDG_LoraOptiSettings.json` (config)
- `presets/lora/sd15 - GLoRA v1.0.json` (config)
- `presets/lora/sd15 - LoKR v1.0.json` (config)
- `presets/lora/sd15 - LoKr v1.1.json` (config)
- `presets/lora/sd15 - LoKr v2.0.json` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `requirements_ipex_xpu.txt` (manifest)
- `requirements_linux.txt` (manifest)
- `requirements_linux_ipex.txt` (manifest)
- `requirements_linux_rocm.txt` (manifest)
- `requirements_macos_amd64.txt` (manifest)
- `requirements_macos_arm64.txt` (manifest)
- `requirements_pytorch_windows.txt` (manifest)
- `requirements_runpod.txt` (manifest)
- `requirements_windows.txt` (manifest)

## Top-level layout

- `test` — 58 analysed file(s)
- `kohya_gui` — 57 analysed file(s)
- `presets` — 41 analysed file(s)
- `(root files)` — 40 analysed file(s)
- `tests` — 39 analysed file(s)
- `tools` — 28 analysed file(s)
- `docs` — 26 analysed file(s)
- `examples` — 14 analysed file(s)
- `setup` — 11 analysed file(s)
- `.cache` — 5 analysed file(s)
- `assets` — 5 analysed file(s)
- `localizations` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `dataset` — 4 analysed file(s)
- `.out-of-scope` — 2 analysed file(s)
- `config_files` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `models` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `45088f04af78e11cec5407ff4652ea3ed2c14422` is the revision these paths and observations refer to.
