# Project structure: AUTOMATIC1111/stable-diffusion-webui

**Analysed commit:** `82a973c04367123ae98bd9abdf80d9eda9b910e2`

**Commit reference:** [82a973c04367123ae98bd9abdf80d9eda9b910e2](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/82a973c04367123ae98bd9abdf80d9eda9b910e2)

**Tree at this commit:** [AUTOMATIC1111/stable-diffusion-webui@82a973c04367](https://github.com/AUTOMATIC1111/stable-diffusion-webui/tree/82a973c04367123ae98bd9abdf80d9eda9b910e2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | AUTOMATIC1111/stable-diffusion-webui |
| Description | Stable Diffusion web UI |
| Stars | 165313 |
| Forks | 31132 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `82a973c04367123ae98bd9abdf80d9eda9b910e2` |
| Retrieved at | 2026-11-14T19:06:01.982132+00:00 |
| Files in this snapshot | 305 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (3 files)
    on_pull_request.yaml
    run_tests.yaml
    warns_merge_master.yml
  pull_request_template.md
configs/  (7 files)
  alt-diffusion-inference.yaml
  alt-diffusion-m18-inference.yaml
  instruct-pix2pix.yaml
  sd3-inference.yaml
  sd_xl_inpaint.yaml
  v1-inference.yaml
  v1-inpainting-inference.yaml
embeddings/  (1 files)
  Place Textual Inversion embeddings here.txt
extensions/  (1 files)
  put extensions here.txt
extensions-builtin/  (43 files)
  LDSR/  (6 files)
    scripts/  (1 files)
      … 1 files under this directory
    ldsr_model_arch.py
    preload.py
    sd_hijack_autoencoder.py
    sd_hijack_ddpm_v1.py
    vqvae_quantize.py
  Lora/  (19 files)
    scripts/  (1 files)
      … 1 files under this directory
    extra_networks_lora.py
    lora.py
    lora_logger.py
    lora_patches.py
    lyco_helpers.py
    network.py
    network_full.py
    network_glora.py
    network_hada.py
    network_ia3.py
    network_lokr.py
    network_lora.py
    network_norm.py
    network_oft.py
    networks.py
    preload.py
    ui_edit_user_metadata.py
    ui_extra_networks_lora.py
  ScuNET/  (2 files)
    scripts/  (1 files)
      … 1 files under this directory
    preload.py
  SwinIR/  (2 files)
    scripts/  (1 files)
      … 1 files under this directory
    preload.py
  canvas-zoom-and-pan/  (3 files)
    javascript/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    style.css
  extra-options-section/  (1 files)
    scripts/  (1 files)
      … 1 files under this directory
  hypertile/  (2 files)
    scripts/  (1 files)
      … 1 files under this directory
    hypertile.py
  mobile/  (1 files)
    javascript/  (1 files)
      … 1 files under this directory
  postprocessing-for-training/  (5 files)
    scripts/  (5 files)
      … 5 files under this directory
  prompt-bracket-checker/  (1 files)
    javascript/  (1 files)
      … 1 files under this directory
  soft-inpainting/  (1 files)
    scripts/  (1 files)
      … 1 files under this directory
html/  (11 files)
  extra-networks-card.html
  extra-networks-copy-path-button.html
  extra-networks-edit-item-button.html
  extra-networks-metadata-button.html
  extra-networks-no-cards.html
  extra-networks-pane-dirs.html
  extra-networks-pane-tree.html
  extra-networks-pane.html
  extra-networks-tree-button.html
  footer.html
  licenses.html
javascript/  (25 files)
  aspectRatioOverlay.js
  contextMenus.js
  dragdrop.js
  edit-attention.js
  edit-order.js
  extensions.js
  extraNetworks.js
  generationParams.js
  hints.js
  hires_fix.js
  imageMaskFix.js
  imageviewer.js
  imageviewerGamepad.js
  inputAccordion.js
  localStorage.js
  localization.js
  notification.js
  profilerVisualization.js
  progressbar.js
  resizeHandle.js
  settings.js
  textualInversion.js
  token-counters.js
  ui.js
  … 1 more files
localizations/  (1 files)
  Put localization files here.txt
models/  (3 files)
  Stable-diffusion/  (1 files)
    Put Stable Diffusion checkpoints here.txt
  VAE/  (1 files)
    Put VAE here.txt
  deepbooru/  (1 files)
    Put your deepbooru release project folder here.txt
modules/  (152 files)
  api/  (2 files)
    api.py
    models.py
  hypernetworks/  (2 files)
    hypernetwork.py
    ui.py
  models/  (9 files)
    diffusion/  (4 files)
      … 4 files under this directory
    sd3/  (5 files)
      … 5 files under this directory
  processing_scripts/  (4 files)
    comments.py
    refiner.py
    sampler.py
    seed.py
  textual_inversion/  (7 files)
    autocrop.py
    dataset.py
    image_embedding.py
    learn_schedule.py
    saving_settings.py
    textual_inversion.py
    ui.py
  cache.py
  call_queue.py
  cmd_args.py
  codeformer_model.py
  config_states.py
  dat_model.py
  deepbooru.py
  deepbooru_model.py
  devices.py
  errors.py
  esrgan_model.py
  extensions.py
  extra_networks.py
  extra_networks_hypernet.py
  extras.py
  face_restoration.py
  face_restoration_utils.py
  fifo_lock.py
  gfpgan_model.py
  gitpython_hack.py
  gradio_extensons.py
  hashes.py
  hat_model.py
  images.py
  … 104 more files
scripts/  (12 files)
  custom_code.py
  img2imgalt.py
  loopback.py
  outpainting_mk_2.py
  poor_mans_outpainting.py
  postprocessing_codeformer.py
  postprocessing_gfpgan.py
  postprocessing_upscale.py
  prompt_matrix.py
  prompts_from_file.py
  sd_upscale.py
  xyz_grid.py
test/  (9 files)
  test_outputs/  (1 files)
    .gitkeep
  __init__.py
  conftest.py
  test_extras.py
  test_face_restorers.py
  test_img2img.py
  test_torch_utils.py
  test_txt2img.py
  test_utils.py
textual_inversion_templates/  (6 files)
  hypernetwork.txt
  none.txt
  style.txt
  style_filewords.txt
  subject.txt
  subject_filewords.txt
.eslintignore
.eslintrc.js
.git-blame-ignore-revs
.gitignore
.pylintrc
CHANGELOG.md
CITATION.cff
CODEOWNERS
LICENSE.txt
README.md
_typos.toml
environment-wsl2.yaml
launch.py
package.json
pyproject.toml
requirements-test.txt
requirements.txt
requirements_npu.txt
requirements_versions.txt
script.js
style.css
webui-macos-env.sh
webui-user.bat
webui-user.sh
… 3 more files
```

## Entry points

- [launch.py:47](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/82a973c04367123ae98bd9abdf80d9eda9b910e2/launch.py#L47)
- [modules/prompt_parser.py:460](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/82a973c04367123ae98bd9abdf80d9eda9b910e2/modules/prompt_parser.py#L460)
- [modules/textual_inversion/image_embedding.py:184](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/82a973c04367123ae98bd9abdf80d9eda9b910e2/modules/textual_inversion/image_embedding.py#L184)
- [webui.py:32](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/82a973c04367123ae98bd9abdf80d9eda9b910e2/webui.py#L32)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: Api, CreateResponse, EmbeddingItem, EmbeddingsResponse, ExtensionItem, ExtraBaseResponse. Observed top-l… |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 9 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AttnBlock, AutocastLinear, BaseModel, CFGDenoiser, CLIPAttention, CLIPEmbeddings. Observed top-level fu… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: ComposableScheduledPromptConditioning, Di… |
| extensions-builtin package | library | Observed | Groups 42 file(s) under extensions-builtin package (observed from repository paths and static analysis). Observed top-level classes: BundledTIHash, ColoredFormatter, DDPMV1, DiffusionWrapperV1, ExtraNetworkLora, ExtraNe… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| javascript package | library | Observed | Groups 25 file(s) under javascript package (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 139 file(s) under modules package (observed from repository paths and static analysis). Observed top-level classes: AfterCFGCallbackParams, AttnChunk, BatchLoader, BatchLoaderRandom, BeforeTokenCounterParams, Ber… |
| scripts package | library | Observed | Groups 12 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: AxisOption, AxisOptionImg2Img, AxisOptionTxt2Img, Script, ScriptPostprocessingCodeFormer, ScriptP… |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: file_to_base64, img2img_basic_image_base64, initialize, mask_basic_image_base64, pytest_configure, simple_… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/on_pull_request.yaml` (ci)
- `.github/workflows/run_tests.yaml` (ci)
- `.github/workflows/warns_merge_master.yml` (ci)
- `_typos.toml` (config)
- `configs/alt-diffusion-inference.yaml` (config)
- `configs/alt-diffusion-m18-inference.yaml` (config)
- `configs/instruct-pix2pix.yaml` (config)
- `configs/sd3-inference.yaml` (config)
- `configs/sd_xl_inpaint.yaml` (config)
- `configs/v1-inference.yaml` (config)
- `configs/v1-inpainting-inference.yaml` (config)
- `environment-wsl2.yaml` (config)
- `package.json` (manifest)
- `pyproject.toml` (manifest)
- `requirements-test.txt` (manifest)
- `requirements.txt` (manifest)
- `requirements_npu.txt` (manifest)
- `requirements_versions.txt` (manifest)

## Top-level layout

- `modules` — 152 analysed file(s)
- `extensions-builtin` — 43 analysed file(s)
- `(root files)` — 27 analysed file(s)
- `javascript` — 25 analysed file(s)
- `scripts` — 12 analysed file(s)
- `html` — 11 analysed file(s)
- `test` — 9 analysed file(s)
- `.github` — 7 analysed file(s)
- `configs` — 7 analysed file(s)
- `textual_inversion_templates` — 6 analysed file(s)
- `models` — 3 analysed file(s)
- `embeddings` — 1 analysed file(s)
- `extensions` — 1 analysed file(s)
- `localizations` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `82a973c04367123ae98bd9abdf80d9eda9b910e2` is the revision these paths and observations refer to.
