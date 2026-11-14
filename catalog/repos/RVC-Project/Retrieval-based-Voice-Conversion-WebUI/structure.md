# Project structure: RVC-Project/Retrieval-based-Voice-Conversion-WebUI

**Analysed commit:** `81eed5e8f68b6bed1789f682fe78cdd324495afc`

**Commit reference:** [81eed5e8f68b6bed1789f682fe78cdd324495afc](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/commit/81eed5e8f68b6bed1789f682fe78cdd324495afc)

**Tree at this commit:** [RVC-Project/Retrieval-based-Voice-Conversion-WebUI@81eed5e8f68b](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/tree/81eed5e8f68b6bed1789f682fe78cdd324495afc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | RVC-Project/Retrieval-based-Voice-Conversion-WebUI |
| Description | Easily train a good VC model with voice data <= 10 mins! |
| Stars | 39261 |
| Forks | 5353 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `81eed5e8f68b6bed1789f682fe78cdd324495afc` |
| Retrieved at | 2026-11-14T19:06:45.219552+00:00 |
| Files in this snapshot | 274 |

## Directory tree

```text
RVCRealtimeVST/  (25 files)
  resources/  (3 files)
    README.txt
    main.rc
    resource.h
  scripts/  (4 files)
    build.ps1
    prepare-dependencies.ps1
    test-all.ps1
    test-worker.ps1
  src/  (6 files)
    RVCRealtime.cpp
    RVCRealtime.h
    RvcParameters.hpp
    SpscRing.hpp
    WorkerClient.cpp
    WorkerClient.hpp
  third_party/  (2 files)
    licenses/  (1 files)
      … 1 files under this directory
    vst2-compat/  (1 files)
      … 1 files under this directory
  tools/  (2 files)
    vst2_smoke.cpp
    worker_smoke.cpp
  worker/  (1 files)
    rvc_worker.py
  .gitignore
  CMakeLists.txt
  LICENSE.txt
  README.en.md
  README.md
  THIRD_PARTY_NOTICES.md
  config.h
assets/  (4 files)
  pymss_weights/  (4 files)
    config_mel_band_roformer_karaoke.yaml
    dereverb_mel_band_roformer_anvuew.yaml
    model_bs_roformer_ep_317_sdr_12.9755.yaml
    model_bs_roformer_ep_368_sdr_12.9628.yaml
configs/  (7 files)
  v1/  (3 files)
    32k.json
    40k.json
    48k.json
  v2/  (2 files)
    32k.json
    48k.json
  config.json
  config.py
docs/  (35 files)
  cn/  (3 files)
    Changelog_CN.md
    cli.md
    faq.md
  en/  (6 files)
    Changelog_EN.md
    README.en.md
    cli.md
    faiss_tips_en.md
    faq_en.md
    training_tips_en.md
  fr/  (5 files)
    Changelog_FR.md
    README.fr.md
    faiss_tips_fr.md
    faq_fr.md
    training_tips_fr.md
  jp/  (5 files)
    Changelog_JA.md
    README.ja.md
    faiss_tips_ja.md
    faq_ja.md
    training_tips_ja.md
  kr/  (6 files)
    Changelog_KO.md
    README.ko.han.md
    README.ko.md
    faiss_tips_ko.md
    faq_ko.md
    training_tips_ko.md
  pt/  (5 files)
    Changelog_pt.md
    README.pt.md
    faiss_tips_pt.md
    faq_pt.md
    training_tips_pt.md
  tr/  (5 files)
    Changelog_TR.md
    README.tr.md
    faiss_tips_tr.md
    faq_tr.md
    training_tips_tr.md
i18n/  (14 files)
  locale/  (13 files)
    en_US.json
    es_ES.json
    fr_FR.json
    it_IT.json
    ja_JP.json
    ko_KR.json
    pt_BR.json
    ru_RU.json
    tr_TR.json
    zh_CN.json
    zh_HK.json
    zh_SG.json
    zh_TW.json
  i18n.py
infer/  (15 files)
  module/  (5 files)
    attentions.py
    commons.py
    models.py
    modules.py
    transforms.py
  vc/  (4 files)
    __init__.py
    modules.py
    pipeline.py
    utils.py
  audio.py
  cli.py
  fcpe.py
  hubert.py
  rmvpe.py
  rtrvc.py
tools/  (152 files)
  pymss/  (56 files)
    modules/  (9 files)
      … 9 files under this directory
    resources/  (25 files)
      … 25 files under this directory
    server/  (9 files)
      … 9 files under this directory
    LICENSE
    __init__.py
    audio_io.py
    cli.py
    config.py
    ensemble.py
    logger.py
    model_download.py
    model_registry.py
    progress.py
    separator.py
    utils.py
    workflow.py
  pymss_core/  (87 files)
    modules/  (57 files)
      … 57 files under this directory
    resources/  (25 files)
      … 25 files under this directory
    LICENSE
    __init__.py
    checkpoint.py
    config.py
    utils.py
  torchgate/  (3 files)
    __init__.py
    torchgate.py
    utils.py
  cuda_graph.py
  file_io.py
  multispeaker.py
  process_utils.py
  progress.py
  pymss_webui.py
train/  (11 files)
  dataset/  (3 files)
    extract_f0.py
    extract_hubert_feature.py
    slicer2.py
  data_utils.py
  losses.py
  mel_processing.py
  preprocess.py
  process_ckpt.py
  train.py
  train_index.py
  utils.py
.gitmodules
LICENSE
MIT协议暨相关引用库协议
README.md
go-realtime_gui.bat
go-webui.bat
realtime_gui.py
requirments_cpu_py312.txt
requirments_cu118_py312.txt
requirments_cu128_py312.txt
webui.py
```

## Entry points

- [RVCRealtimeVST/worker/rvc_worker.py:344](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/RVCRealtimeVST/worker/rvc_worker.py#L344)
- [infer/cli.py:292](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/infer/cli.py#L292)
- [infer/rmvpe.py:637](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/infer/rmvpe.py#L637)
- [realtime_gui.py:24](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/realtime_gui.py#L24)
- [tools/pymss/cli.py:586](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/tools/pymss/cli.py#L586)
- [tools/pymss/server/app.py:663](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/tools/pymss/server/app.py#L663)
- [train/dataset/extract_f0.py:175](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/train/dataset/extract_f0.py#L175)
- [train/dataset/slicer2.py:259](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/train/dataset/slicer2.py#L259)
- [train/preprocess.py:226](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/train/preprocess.py#L226)
- [train/train.py:665](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/81eed5e8f68b6bed1789f682fe78cdd324495afc/train/train.py#L665)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 77 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AttrDict, Config, ConfigLoader, ServerConfig. Observed top-level functions: _detect_… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: ToolButton. Observed top-level functions: add_multispeaker_row, artifact_names, begin_train_task, but… |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DiscriminatorP, DiscriminatorS, Generator, GeneratorNSF, MultiPeriodDiscriminator, MultiPeriodDiscrimin… |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: BiGRU, ConvBlockRes, Decoder, DeepUnet,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| i18n package | library | Observed | Groups 1 file(s) under i18n package (observed from repository paths and static analysis). Observed top-level classes: I18nAuto. Observed top-level functions: load_language_list. |
| infer package | library | Observed | Groups 12 file(s) under infer package (observed from repository paths and static analysis). Observed top-level classes: ConvFlow, ConvReluNorm, DDSConv, Decoder, ElementwiseAffine, Encoder. Observed top-level functions:… |
| RVCRealtimeVST package | library | Observed | Groups 8 file(s) under rvcrealtimevst package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 10 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: BandSplitModule, BandsplitCoreBase, BandsplitSpecification, BarkBandsplitSpecification, Ba… |
| tools package | library | Observed | Groups 83 file(s) under tools package (observed from repository paths and static analysis). Observed top-level classes: APIError, ASPPModule, AdaptiveHyperedgeGeneration, AdaptiveHypergraphComputation, Apollo, Attend. O… |
| train package | library | Observed | Groups 7 file(s) under train package (observed from repository paths and static analysis). Observed top-level classes: DistributedBucketSampler, HParams, TextAudioCollate, TextAudioCollateMultiNSFsid, TextAudioLoader, T… |

## Important files

- `assets/pymss_weights/config_mel_band_roformer_karaoke.yaml` (config)
- `assets/pymss_weights/dereverb_mel_band_roformer_anvuew.yaml` (config)
- `assets/pymss_weights/model_bs_roformer_ep_317_sdr_12.9755.yaml` (config)
- `assets/pymss_weights/model_bs_roformer_ep_368_sdr_12.9628.yaml` (config)
- `configs/config.json` (config)
- `configs/v1/32k.json` (config)
- `configs/v1/40k.json` (config)
- `configs/v1/48k.json` (config)
- `configs/v2/32k.json` (config)
- `configs/v2/48k.json` (config)
- `i18n/locale/en_US.json` (config)
- `i18n/locale/es_ES.json` (config)
- `i18n/locale/fr_FR.json` (config)
- `i18n/locale/it_IT.json` (config)
- `i18n/locale/ja_JP.json` (config)
- `i18n/locale/ko_KR.json` (config)
- `i18n/locale/pt_BR.json` (config)
- `i18n/locale/ru_RU.json` (config)
- `i18n/locale/tr_TR.json` (config)
- `i18n/locale/zh_CN.json` (config)
- `i18n/locale/zh_HK.json` (config)
- `i18n/locale/zh_SG.json` (config)
- `i18n/locale/zh_TW.json` (config)
- `tools/pymss/resources/vr_modelparams/1band_sr16000_hl512.json` (config)
- `tools/pymss/resources/vr_modelparams/1band_sr32000_hl512.json` (config)
- `tools/pymss/resources/vr_modelparams/1band_sr33075_hl384.json` (config)
- `tools/pymss/resources/vr_modelparams/1band_sr44100_hl1024.json` (config)
- `tools/pymss/resources/vr_modelparams/1band_sr44100_hl256.json` (config)
- `tools/pymss/resources/vr_modelparams/1band_sr44100_hl512.json` (config)
- `tools/pymss/resources/vr_modelparams/1band_sr44100_hl512_cut.json` (config)
- `tools/pymss/resources/vr_modelparams/1band_sr44100_hl512_nf1024.json` (config)
- `tools/pymss/resources/vr_modelparams/2band_32000.json` (config)
- `tools/pymss/resources/vr_modelparams/2band_44100_lofi.json` (config)
- `tools/pymss/resources/vr_modelparams/2band_48000.json` (config)
- `tools/pymss/resources/vr_modelparams/3band_44100.json` (config)
- `tools/pymss/resources/vr_modelparams/3band_44100_mid.json` (config)
- `tools/pymss/resources/vr_modelparams/3band_44100_msb2.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_44100.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_44100_mid.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_44100_msb.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_44100_msb2.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_44100_reverse.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_44100_sw.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_v2.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_v2_sn.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_v3.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_v3_sn.json` (config)
- `tools/pymss/resources/vr_modelparams/4band_v4_ms_fullband.json` (config)
- `tools/pymss_core/resources/vr_modelparams/1band_sr16000_hl512.json` (config)
- `tools/pymss_core/resources/vr_modelparams/1band_sr32000_hl512.json` (config)
- `tools/pymss_core/resources/vr_modelparams/1band_sr33075_hl384.json` (config)
- `tools/pymss_core/resources/vr_modelparams/1band_sr44100_hl1024.json` (config)
- `tools/pymss_core/resources/vr_modelparams/1band_sr44100_hl256.json` (config)
- `tools/pymss_core/resources/vr_modelparams/1band_sr44100_hl512.json` (config)
- `tools/pymss_core/resources/vr_modelparams/1band_sr44100_hl512_cut.json` (config)
- `tools/pymss_core/resources/vr_modelparams/1band_sr44100_hl512_nf1024.json` (config)
- `tools/pymss_core/resources/vr_modelparams/2band_32000.json` (config)
- `tools/pymss_core/resources/vr_modelparams/2band_44100_lofi.json` (config)
- `tools/pymss_core/resources/vr_modelparams/2band_48000.json` (config)
- `tools/pymss_core/resources/vr_modelparams/3band_44100.json` (config)
- `tools/pymss_core/resources/vr_modelparams/3band_44100_mid.json` (config)
- `tools/pymss_core/resources/vr_modelparams/3band_44100_msb2.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_44100.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_44100_mid.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_44100_msb.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_44100_msb2.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_44100_reverse.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_44100_sw.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_v2.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_v2_sn.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_v3.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_v3_sn.json` (config)
- `tools/pymss_core/resources/vr_modelparams/4band_v4_ms_fullband.json` (config)

## Top-level layout

- `tools` — 152 analysed file(s)
- `docs` — 35 analysed file(s)
- `RVCRealtimeVST` — 25 analysed file(s)
- `infer` — 15 analysed file(s)
- `i18n` — 14 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `train` — 11 analysed file(s)
- `configs` — 7 analysed file(s)
- `assets` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `81eed5e8f68b6bed1789f682fe78cdd324495afc` is the revision these paths and observations refer to.
