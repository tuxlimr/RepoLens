# Project structure: RVC-Boss/GPT-SoVITS

**Analysed commit:** `6d51ffceafbf240145619af4c92408a6e54b7924`

**Commit reference:** [6d51ffceafbf240145619af4c92408a6e54b7924](https://github.com/RVC-Boss/GPT-SoVITS/commit/6d51ffceafbf240145619af4c92408a6e54b7924)

**Tree at this commit:** [RVC-Boss/GPT-SoVITS@6d51ffceafbf](https://github.com/RVC-Boss/GPT-SoVITS/tree/6d51ffceafbf240145619af4c92408a6e54b7924)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | RVC-Boss/GPT-SoVITS |
| Description | 1 min voice data can also be used to train a good TTS model! (few shot voice cloning) |
| Stars | 65051 |
| Forks | 6802 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `6d51ffceafbf240145619af4c92408a6e54b7924` |
| Retrieved at | 2026-11-14T19:06:21.715107+00:00 |
| Files in this snapshot | 274 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    build_windows_packages.yaml
    docker-publish.yaml
  build_windows_packages.ps1
Docker/  (2 files)
  install_wrapper.sh
  miniforge_install.sh
GPT_SoVITS/  (177 files)
  AR/  (32 files)
    data/  (4 files)
      … 4 files under this directory
    models/  (9 files)
      … 9 files under this directory
    modules/  (12 files)
      … 12 files under this directory
    text_processing/  (3 files)
      … 3 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    __init__.py
  Accel/  (27 files)
    MLX/  (9 files)
      … 9 files under this directory
    PyTorch/  (13 files)
      … 13 files under this directory
    README.md
    __init__.py
    adapter.py
    logger.py
    runtime.py
  BigVGAN/  (18 files)
    alias_free_activation/  (4 files)
      … 4 files under this directory
    incl_licenses/  (8 files)
      … 8 files under this directory
    LICENSE
    README.md
    activations.py
    bigvgan.py
    env.py
    utils0.py
  TTS_infer_pack/  (5 files)
    TTS.py
    TextPreprocessor.py
    __init__.py
    streaming.py
    text_segmentation_method.py
  configs/  (12 files)
    .gitignore
    s1.yaml
    s1big.yaml
    s1big2.yaml
    s1longer-v2.yaml
    s1longer.yaml
    s1mq.yaml
    s2.json
    s2v2Pro.json
    s2v2ProPlus.json
    train.yaml
    tts_infer.yaml
  eres2net/  (4 files)
    ERes2NetV2.py
    fusion.py
    kaldi.py
    pooling_layers.py
  f5_tts/  (4 files)
    model/  (4 files)
      … 4 files under this directory
  feature_extractor/  (3 files)
    __init__.py
    cnhubert.py
    whisper_enc.py
  module/  (18 files)
    __init__.py
    attentions.py
    attentions_onnx.py
    cache_dit.py
    commons.py
    core_vq.py
    data_utils.py
    ddp_utils.py
    distrib.py
    losses.py
    mel_processing.py
    models.py
    models_onnx.py
    models_v5.py
    modules.py
    mrte_model.py
    quantize.py
    transforms.py
  prepare_datasets/  (4 files)
    1-get-text.py
    2-get-hubert-wav32k.py
    2-get-sv.py
    3-get-semantic.py
  pretrained_models/  (1 files)
    .gitignore
  text/  (33 files)
    LangSegmenter/  (2 files)
      … 2 files under this directory
    en_normalization/  (1 files)
      … 1 files under this directory
    g2pw/  (7 files)
      … 7 files under this directory
    zh_normalization/  (9 files)
      … 9 files under this directory
    .gitignore
    __init__.py
    cantonese.py
    chinese.py
    chinese2.py
    cleaner.py
    engdict-hot.rep
    english.py
    japanese.py
    korean.py
    opencpop-strict.txt
    symbols.py
    symbols2.py
    tone_sandhi.py
  download.py
  export_torch_script.py
  export_torch_script_v3v4.py
  inference_cli.py
  inference_gui.py
  inference_webui.py
  inference_webui_fast.py
  onnx_export.py
  process_ckpt.py
  s1_train.py
  s2_train.py
  s2_train_v3.py
  s2_train_v3_lora.py
  stream_v2pro.py
  sv.py
  utils.py
docs/  (10 files)
  cn/  (2 files)
    Changelog_CN.md
    README.md
  en/  (2 files)
    Changelog_EN.md
    semantic_streaming.md
  ja/  (2 files)
    Changelog_JA.md
    README.md
  ko/  (2 files)
    Changelog_KO.md
    README.md
  tr/  (2 files)
    Changelog_TR.md
    README.md
requirements-py312-win-flash_attention/  (4 files)
  requirements_py312_win_cu118_china.txt
  requirements_py312_win_cu118_overseas.txt
  requirements_py312_win_cu128_china.txt
  requirements_py312_win_cu128_overseas.txt
tools/  (56 files)
  AP_BWE_main/  (8 files)
    24kto48k/  (2 files)
      … 2 files under this directory
    datasets1/  (2 files)
      … 2 files under this directory
    models/  (2 files)
      … 2 files under this directory
    LICENSE
    README.md
  asr/  (4 files)
    models/  (1 files)
      … 1 files under this directory
    config.py
    fasterwhisper_asr.py
    funasr_asr.py
  denoise-model/  (1 files)
    .gitignore
  i18n/  (15 files)
    locale/  (13 files)
      … 13 files under this directory
    i18n.py
    scan_i18n.py
  uvr5/  (18 files)
    bs_roformer/  (4 files)
      … 4 files under this directory
    lib/  (9 files)
      … 9 files under this directory
    uvr5_weights/  (1 files)
      … 1 files under this directory
    bsroformer.py
    mdxnet.py
    vr.py
    webui.py
  __init__.py
  acceleration.py
  assets.py
  audio_sr.py
  cmd-denoise.py
  my_utils.py
  portable_runtime.py
  slice_audio.py
  slicer2.py
  subfix_webui.py
.dockerignore
.gitignore
.pre-commit-config.yaml
Colab-Inference.ipynb
Colab-WebUI.ipynb
Dockerfile
LICENSE
README.md
api.py
api_v2.py
config.py
docker-compose.yaml
docker_build.sh
extra-req.txt
go-webui.bat
go-webui.ps1
install.ps1
install.sh
requirements.txt
test_api_v2_streaming.py
test_official_streaming.py
webui.py
```

## Entry points

- [GPT_SoVITS/AR/data/dataset.py:300](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/AR/data/dataset.py#L300)
- [GPT_SoVITS/AR/modules/lr_schedulers.py:65](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/AR/modules/lr_schedulers.py#L65)
- [GPT_SoVITS/AR/modules/scaling.py:62](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/AR/modules/scaling.py#L62)
- [GPT_SoVITS/AR/text_processing/phonemizer.py:64](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/AR/text_processing/phonemizer.py#L64)
- [GPT_SoVITS/Accel/PyTorch/AR/export.py:23](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/Accel/PyTorch/AR/export.py#L23)
- [GPT_SoVITS/Accel/logger.py:269](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/Accel/logger.py#L269)
- [GPT_SoVITS/TTS_infer_pack/text_segmentation_method.py:187](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/TTS_infer_pack/text_segmentation_method.py#L187)
- [GPT_SoVITS/export_torch_script.py:1078](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/export_torch_script.py#L1078)
- [GPT_SoVITS/feature_extractor/cnhubert.py:103](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/feature_extractor/cnhubert.py#L103)
- [GPT_SoVITS/inference_cli.py:102](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/inference_cli.py#L102)
- [GPT_SoVITS/inference_gui.py:312](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/inference_gui.py#L312)
- [GPT_SoVITS/inference_webui.py:1558](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/GPT_SoVITS/inference_webui.py#L1558)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 36 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. Observed top-level functions: change_choices, custom_sort_key, get_device_dt… |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: change_label, change_tts_inference, change_uvr5, check_pretrained_is_exist, close1Ba, close1Bb. |
| Data layer | data | Observed | Groups 17 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: APNet_BWE_Model, Bert, BertEmbeddings, CFM, CodePredictor, ConvNeXtBlock. Observed top-level functions… |
| Docker package | library | Observed | Groups 2 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 42 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Typer. Observed routes: POST /set_model, GET /set_model, POST /contr… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: G2PWOnnxConverter, _G2PWBaseOnnxConverter. Observed top-level functions: _find_first_existin… |
| GPT_SoVITS package | library | Observed | Groups 97 file(s) under gpt_sovits package (observed from repository paths and static analysis). Observed top-level classes: AFF, AMPBlock1, AMPBlock2, ASTP, AccelInference, ActNorm. Observed top-level functions: _check… |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: APIV2StreamingTests, AcousticRNGTests, AcousticTests, AdapterTests, CancelTests, CancellationTests. Observed… |
| tools package | library | Observed | Groups 24 file(s) under tools package (observed from repository paths and static analysis). Observed top-level classes: AP_BWE, ASPPModule, Attend, Attention, AudioPre, AudioPreDeEcho. Observed top-level functions: MLP,… |

## Important files

- `.dockerignore` (container)
- `.github/workflows/build_windows_packages.yaml` (ci)
- `.github/workflows/docker-publish.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `GPT_SoVITS/configs/s1.yaml` (config)
- `GPT_SoVITS/configs/s1big.yaml` (config)
- `GPT_SoVITS/configs/s1big2.yaml` (config)
- `GPT_SoVITS/configs/s1longer-v2.yaml` (config)
- `GPT_SoVITS/configs/s1longer.yaml` (config)
- `GPT_SoVITS/configs/s1mq.yaml` (config)
- `GPT_SoVITS/configs/s2.json` (config)
- `GPT_SoVITS/configs/s2v2Pro.json` (config)
- `GPT_SoVITS/configs/s2v2ProPlus.json` (config)
- `GPT_SoVITS/configs/train.yaml` (config)
- `GPT_SoVITS/configs/tts_infer.yaml` (config)
- `docker-compose.yaml` (container)
- `requirements-py312-win-flash_attention/requirements_py312_win_cu118_china.txt` (manifest)
- `requirements-py312-win-flash_attention/requirements_py312_win_cu118_overseas.txt` (manifest)
- `requirements-py312-win-flash_attention/requirements_py312_win_cu128_china.txt` (manifest)
- `requirements-py312-win-flash_attention/requirements_py312_win_cu128_overseas.txt` (manifest)
- `requirements.txt` (manifest)
- `tools/AP_BWE_main/24kto48k/config.json` (config)
- `tools/i18n/locale/en_US.json` (config)
- `tools/i18n/locale/es_ES.json` (config)
- `tools/i18n/locale/fr_FR.json` (config)
- `tools/i18n/locale/it_IT.json` (config)
- `tools/i18n/locale/ja_JP.json` (config)
- `tools/i18n/locale/ko_KR.json` (config)
- `tools/i18n/locale/pt_BR.json` (config)
- `tools/i18n/locale/ru_RU.json` (config)
- `tools/i18n/locale/tr_TR.json` (config)
- `tools/i18n/locale/zh_CN.json` (config)
- `tools/i18n/locale/zh_HK.json` (config)
- `tools/i18n/locale/zh_SG.json` (config)
- `tools/i18n/locale/zh_TW.json` (config)
- `tools/uvr5/lib/lib_v5/modelparams/4band_v2.json` (config)
- `tools/uvr5/lib/lib_v5/modelparams/4band_v3.json` (config)

## Top-level layout

- `GPT_SoVITS` — 177 analysed file(s)
- `tools` — 56 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `docs` — 10 analysed file(s)
- `requirements-py312-win-flash_attention` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `Docker` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `6d51ffceafbf240145619af4c92408a6e54b7924` is the revision these paths and observations refer to.
