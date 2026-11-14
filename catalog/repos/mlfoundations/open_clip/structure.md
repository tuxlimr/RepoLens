# Project structure: mlfoundations/open_clip

**Analysed commit:** `4cc208d3a44a2fb6d6435006a46f520d2ccc29b1`

**Commit reference:** [4cc208d3a44a2fb6d6435006a46f520d2ccc29b1](https://github.com/mlfoundations/open_clip/commit/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1)

**Tree at this commit:** [mlfoundations/open_clip@4cc208d3a44a](https://github.com/mlfoundations/open_clip/tree/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mlfoundations/open_clip |
| Description | An open source implementation of CLIP. |
| Stars | 14265 |
| Forks | 1337 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `4cc208d3a44a2fb6d6435006a46f520d2ccc29b1` |
| Retrieved at | 2026-11-14T19:09:29.338111+00:00 |
| Files in this snapshot | 387 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    ci.yml
    clear-cache.yml
    python-publish.yml
docs/  (23 files)
  script_examples/  (10 files)
    clipa/  (6 files)
      … 6 files under this directory
    clipav2/  (3 files)
      … 3 files under this directory
    stability_example.sh
  Interacting_with_open_coca.ipynb
  LOW_ACC.md
  MIGRATING_3_TO_4.md
  PRETRAINED.md
  clip_conceptual_captions.md
  clipa.md
  datacomp_models.md
  linear_probe.md
  model_profile.csv
  multilabel_zeroshot.md
  openclip_classification_results.csv
  openclip_results.csv
  openclip_retrieval_results.csv
scripts/  (19 files)
  probe_configs/  (7 files)
    bigearthnet_v2_rgb.json
    csv_multilabel.json
    nih_chest_xray14.json
    oxford_iiit_pet.json
    plant_pathology_2021.json
    resisc45.json
    webdataset_single_label.json
  clap_zeroshot.py
  clipav1_vit_l16_i37_t8.sh
  clipav2_vit_h14_i84_224_336_cl32_gap_datacomp1b.sh
  convert_audio_patch_layout.py
  genlip_attentive_probe.py
  genlip_caption_stats.py
  genlip_zeroshot.py
  h14_224_32_finetune.sh
  h14_84_8_pretrain.sh
  linear_probe.py
  linear_probe_data.py
  multilabel_zeroshot.py
src/  (272 files)
  open_clip/  (249 files)
    audio/  (12 files)
      … 12 files under this directory
    model_configs/  (196 files)
      … 196 files under this directory
    task/  (11 files)
      … 11 files under this directory
    __init__.py
    clap_model.py
    coca_model.py
    constants.py
    convert.py
    factory.py
    generation.py
    hf_configs.py
    hf_model.py
    layers.py
    loss.py
    mammut_model.py
    model.py
    model_traits.py
    modified_resnet.py
    naflex_config.py
    naflex_convert.py
    naflex_genlap_model.py
    naflex_genlip_model.py
    pos_embed.py
    pretrained.py
    push_to_hf_hub.py
    timm_model.py
    tokenizer.py
    … 6 more files
  open_clip_train/  (23 files)
    __init__.py
    audio_data.py
    audio_zero_shot.py
    data.py
    distributed.py
    eval_utils.py
    file_utils.py
    legacy_data.py
    legacy_main.py
    legacy_train.py
    logger.py
    loss.py
    main.py
    metrics.py
    naflex_data.py
    optim.py
    params.py
    precision.py
    profiler.py
    scheduler.py
    train.py
    utils.py
    zero_shot.py
tests/  (57 files)
  test_audio_checkpointing.py
  test_audio_convert.py
  test_audio_data.py
  test_audio_model_configs.py
  test_audio_truncation.py
  test_audio_wds.py
  test_audio_zero_shot.py
  test_clap_task.py
  test_coca2.py
  test_context_masking.py
  test_data_csv.py
  test_download_pretrained.py
  test_eval_task.py
  test_factory_loss.py
  test_factory_task.py
  test_fused_caption_loss.py
  test_grad_accum.py
  test_hf_model.py
  test_inference.py
  test_inference_simple.py
  test_legacy_data.py
  test_loss.py
  test_mammut.py
  test_model_traits.py
  … 33 more files
.gitattributes
.gitignore
CITATION.cff
HISTORY.md
LICENSE
MANIFEST.in
Makefile
README.md
pyproject.toml
pytest.ini
requirements-test.txt
requirements-training.txt
requirements.txt
```

## Entry points

- [src/open_clip/push_to_hf_hub.py:309](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/src/open_clip/push_to_hf_hub.py#L309)
- [src/open_clip_train/legacy_main.py:552](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/src/open_clip_train/legacy_main.py#L552)
- [src/open_clip_train/main.py:751](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/src/open_clip_train/main.py#L751)
- [src/open_clip_train/profiler.py:252](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/src/open_clip_train/profiler.py#L252)
- [scripts/clap_zeroshot.py:99](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/scripts/clap_zeroshot.py#L99)
- [scripts/convert_audio_patch_layout.py:86](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/scripts/convert_audio_patch_layout.py#L86)
- [scripts/genlip_attentive_probe.py:294](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/scripts/genlip_attentive_probe.py#L294)
- [scripts/genlip_caption_stats.py:269](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/scripts/genlip_caption_stats.py#L269)
- [scripts/genlip_zeroshot.py:229](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/scripts/genlip_zeroshot.py#L229)
- [scripts/linear_probe.py:594](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/scripts/linear_probe.py#L594)
- [scripts/multilabel_zeroshot.py:740](https://github.com/mlfoundations/open_clip/blob/4cc208d3a44a2fb6d6435006a46f520d2ccc29b1/scripts/multilabel_zeroshot.py#L740)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 210 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: CLIPAudioCfg. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: CLIP, CLIPTextCfg, CLIPVisionCfg, CustomTextCLIP. Observed top-level functions: _add_intermediate_logit… |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: FeatureProvider, ProbeHead. Observed top-level functions: _baseline_prompts, _geom, _get_… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| open_clip package | library | Observed | Groups 50 file(s) under open_clip package (observed from repository paths and static analysis). Observed top-level classes: AFF, Attention, AttentionPool2d, AttentionalPooler, AudioAugmentationCfg, AudioNaFlexCfg. Obser… |
| open_clip_train package | library | Observed | Groups 20 file(s) under open_clip_train package (observed from repository paths and static analysis). Observed top-level classes: AudioCaptionTokenizer, AudioTokenLength, AudioZeroShotData, AverageMeter, CaptionLength,… |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: ClassificationSource, ImageCollator, MetadataReader, TimmClassificationDataset. Observed top-level… |
| Tests | test | Observed | Groups 57 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH open_clip.pretrained.urllib, PATCH open_clip.pretrained.urllib, PATCH open_clip.pretrained.urllib, PATCH open_cl… |

## Important files

- `.github/workflows/ci.yml` (ci)
- `.github/workflows/clear-cache.yml` (ci)
- `.github/workflows/python-publish.yml` (ci)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `requirements-test.txt` (manifest)
- `requirements-training.txt` (manifest)
- `requirements.txt` (manifest)
- `scripts/probe_configs/bigearthnet_v2_rgb.json` (config)
- `scripts/probe_configs/csv_multilabel.json` (config)
- `scripts/probe_configs/nih_chest_xray14.json` (config)
- `scripts/probe_configs/oxford_iiit_pet.json` (config)
- `scripts/probe_configs/plant_pathology_2021.json` (config)
- `scripts/probe_configs/resisc45.json` (config)
- `scripts/probe_configs/webdataset_single_label.json` (config)
- `src/open_clip/model_configs/CLAP-HTSAT-base-Roberta-base.json` (config)
- `src/open_clip/model_configs/CLAP-HTSAT-base.json` (config)
- `src/open_clip/model_configs/CLAP-HTSAT-large.json` (config)
- `src/open_clip/model_configs/CLAP-HTSAT-tiny-Roberta-base-fused.json` (config)
- `src/open_clip/model_configs/CLAP-HTSAT-tiny-Roberta-base.json` (config)
- `src/open_clip/model_configs/CLAP-HTSAT-tiny.json` (config)
- `src/open_clip/model_configs/CLAP-Whisper-base-Roberta-base.json` (config)
- `src/open_clip/model_configs/CLAP-Whisper-small-Roberta-base.json` (config)
- `src/open_clip/model_configs/CLAP-Whisper-tiny-Roberta-base.json` (config)
- `src/open_clip/model_configs/EVA01-g-14-plus.json` (config)
- `src/open_clip/model_configs/EVA01-g-14.json` (config)
- `src/open_clip/model_configs/EVA02-B-16.json` (config)
- `src/open_clip/model_configs/EVA02-E-14-plus.json` (config)
- `src/open_clip/model_configs/EVA02-E-14.json` (config)
- `src/open_clip/model_configs/EVA02-L-14-336.json` (config)
- `src/open_clip/model_configs/EVA02-L-14.json` (config)
- `src/open_clip/model_configs/MobileCLIP-B.json` (config)
- `src/open_clip/model_configs/MobileCLIP-S1.json` (config)
- `src/open_clip/model_configs/MobileCLIP-S2.json` (config)
- `src/open_clip/model_configs/MobileCLIP2-B.json` (config)
- `src/open_clip/model_configs/MobileCLIP2-L-14.json` (config)
- `src/open_clip/model_configs/MobileCLIP2-S0.json` (config)
- `src/open_clip/model_configs/MobileCLIP2-S2.json` (config)
- `src/open_clip/model_configs/MobileCLIP2-S3.json` (config)
- `src/open_clip/model_configs/MobileCLIP2-S4.json` (config)
- `src/open_clip/model_configs/PE-Core-B-16.json` (config)
- `src/open_clip/model_configs/PE-Core-L-14-336.json` (config)
- `src/open_clip/model_configs/PE-Core-S-16-384.json` (config)
- `src/open_clip/model_configs/PE-Core-T-16-384.json` (config)
- `src/open_clip/model_configs/PE-Core-bigG-14-448.json` (config)
- `src/open_clip/model_configs/RN101-quickgelu.json` (config)
- `src/open_clip/model_configs/RN101.json` (config)
- `src/open_clip/model_configs/RN50-quickgelu.json` (config)
- `src/open_clip/model_configs/RN50.json` (config)
- `src/open_clip/model_configs/RN50x16-quickgelu.json` (config)
- `src/open_clip/model_configs/RN50x16.json` (config)
- `src/open_clip/model_configs/RN50x4-quickgelu.json` (config)
- `src/open_clip/model_configs/RN50x4.json` (config)
- `src/open_clip/model_configs/RN50x64-quickgelu.json` (config)
- `src/open_clip/model_configs/RN50x64.json` (config)
- `src/open_clip/model_configs/ViT-B-16-SigLIP-256.json` (config)
- `src/open_clip/model_configs/ViT-B-16-SigLIP-384.json` (config)
- `src/open_clip/model_configs/ViT-B-16-SigLIP-512.json` (config)
- `src/open_clip/model_configs/ViT-B-16-SigLIP-i18n-256.json` (config)
- `src/open_clip/model_configs/ViT-B-16-SigLIP.json` (config)
- `src/open_clip/model_configs/ViT-B-16-SigLIP2-256.json` (config)
- `src/open_clip/model_configs/ViT-B-16-SigLIP2-384.json` (config)
- `src/open_clip/model_configs/ViT-B-16-SigLIP2-512.json` (config)
- `src/open_clip/model_configs/ViT-B-16-SigLIP2-naflex.json` (config)
- `src/open_clip/model_configs/ViT-B-16-SigLIP2.json` (config)
- `src/open_clip/model_configs/ViT-B-16-plus-240.json` (config)
- `src/open_clip/model_configs/ViT-B-16-plus.json` (config)
- `src/open_clip/model_configs/ViT-B-16-quickgelu.json` (config)
- `src/open_clip/model_configs/ViT-B-16.json` (config)
- `src/open_clip/model_configs/ViT-B-32-256.json` (config)
- `src/open_clip/model_configs/ViT-B-32-SigLIP2-256.json` (config)
- `src/open_clip/model_configs/ViT-B-32-plus-256.json` (config)
- `src/open_clip/model_configs/ViT-B-32-quickgelu.json` (config)
- `src/open_clip/model_configs/ViT-B-32.json` (config)
- `src/open_clip/model_configs/ViT-H-14-378-quickgelu.json` (config)
- `src/open_clip/model_configs/ViT-H-14-378.json` (config)
- `src/open_clip/model_configs/ViT-H-14-CLIPA-336.json` (config)
- `src/open_clip/model_configs/ViT-H-14-CLIPA.json` (config)
- `src/open_clip/model_configs/ViT-H-14-quickgelu.json` (config)
- `src/open_clip/model_configs/ViT-H-14-worldwide-378.json` (config)
- `src/open_clip/model_configs/ViT-H-14-worldwide-quickgelu.json` (config)
- `src/open_clip/model_configs/ViT-H-14-worldwide.json` (config)
- `src/open_clip/model_configs/ViT-H-14.json` (config)
- `src/open_clip/model_configs/ViT-H-16.json` (config)
- `src/open_clip/model_configs/ViT-L-14-280.json` (config)
- `src/open_clip/model_configs/ViT-L-14-336-quickgelu.json` (config)
- `src/open_clip/model_configs/ViT-L-14-336.json` (config)
- `src/open_clip/model_configs/ViT-L-14-CLIPA-336.json` (config)
- `src/open_clip/model_configs/ViT-L-14-CLIPA.json` (config)
- `src/open_clip/model_configs/ViT-L-14-quickgelu.json` (config)
- `src/open_clip/model_configs/ViT-L-14-worldwide-quickgelu.json` (config)
- `src/open_clip/model_configs/ViT-L-14-worldwide.json` (config)
- `src/open_clip/model_configs/ViT-L-14.json` (config)
- `src/open_clip/model_configs/ViT-L-16-320.json` (config)
- `src/open_clip/model_configs/ViT-L-16-SigLIP-256.json` (config)
- `src/open_clip/model_configs/ViT-L-16-SigLIP-384.json` (config)
- `src/open_clip/model_configs/ViT-L-16-SigLIP2-256.json` (config)
- `src/open_clip/model_configs/ViT-L-16-SigLIP2-384.json` (config)
- `src/open_clip/model_configs/ViT-L-16-SigLIP2-512.json` (config)
- `src/open_clip/model_configs/ViT-L-16.json` (config)
- `src/open_clip/model_configs/ViT-M-16-alt.json` (config)
- `src/open_clip/model_configs/ViT-M-16.json` (config)
- `src/open_clip/model_configs/ViT-M-32-alt.json` (config)
- `src/open_clip/model_configs/ViT-M-32.json` (config)
- `src/open_clip/model_configs/ViT-S-16-alt.json` (config)
- `src/open_clip/model_configs/ViT-S-16.json` (config)
- `src/open_clip/model_configs/ViT-S-32-alt.json` (config)
- `src/open_clip/model_configs/ViT-S-32.json` (config)
- `src/open_clip/model_configs/ViT-SO400M-14-SigLIP-378.json` (config)
- `src/open_clip/model_configs/ViT-SO400M-14-SigLIP-384.json` (config)
- `src/open_clip/model_configs/ViT-SO400M-14-SigLIP.json` (config)
- `src/open_clip/model_configs/ViT-SO400M-14-SigLIP2-378.json` (config)
- `src/open_clip/model_configs/ViT-SO400M-14-SigLIP2.json` (config)
- `src/open_clip/model_configs/ViT-SO400M-16-SigLIP-i18n-256.json` (config)
- `src/open_clip/model_configs/ViT-SO400M-16-SigLIP2-256.json` (config)
- `src/open_clip/model_configs/ViT-SO400M-16-SigLIP2-384.json` (config)
- `src/open_clip/model_configs/ViT-SO400M-16-SigLIP2-512.json` (config)
- `src/open_clip/model_configs/ViT-SO400M-16-SigLIP2-naflex.json` (config)
- `src/open_clip/model_configs/ViT-bigG-14-CLIPA-336.json` (config)
- `src/open_clip/model_configs/ViT-bigG-14-CLIPA.json` (config)
- `src/open_clip/model_configs/ViT-bigG-14-quickgelu.json` (config)
- `src/open_clip/model_configs/ViT-bigG-14-worldwide-378.json` (config)
- `src/open_clip/model_configs/ViT-bigG-14-worldwide.json` (config)
- `src/open_clip/model_configs/ViT-bigG-14.json` (config)
- `src/open_clip/model_configs/ViT-e-14.json` (config)
- `src/open_clip/model_configs/ViT-g-14.json` (config)
- `src/open_clip/model_configs/ViT-gopt-16-SigLIP2-256.json` (config)
- `src/open_clip/model_configs/ViT-gopt-16-SigLIP2-384.json` (config)
- `src/open_clip/model_configs/ViTamin-B-LTT.json` (config)
- `src/open_clip/model_configs/ViTamin-B.json` (config)
- `src/open_clip/model_configs/ViTamin-L-256.json` (config)
- `src/open_clip/model_configs/ViTamin-L-336.json` (config)
- `src/open_clip/model_configs/ViTamin-L-384.json` (config)
- `src/open_clip/model_configs/ViTamin-L.json` (config)
- `src/open_clip/model_configs/ViTamin-L2-256.json` (config)
- `src/open_clip/model_configs/ViTamin-L2-336.json` (config)
- `src/open_clip/model_configs/ViTamin-L2-384.json` (config)
- `src/open_clip/model_configs/ViTamin-L2.json` (config)
- `src/open_clip/model_configs/ViTamin-S-LTT.json` (config)
- `src/open_clip/model_configs/ViTamin-S.json` (config)
- `src/open_clip/model_configs/ViTamin-XL-256.json` (config)
- `src/open_clip/model_configs/ViTamin-XL-336.json` (config)
- `src/open_clip/model_configs/ViTamin-XL-384.json` (config)
- `src/open_clip/model_configs/coca2-moderntext-naflex_ViT-B-32.json` (config)
- `src/open_clip/model_configs/coca2-moderntext_ViT-B-32.json` (config)
- `src/open_clip/model_configs/coca2_ViT-B-32.json` (config)
- `src/open_clip/model_configs/coca_ViT-B-32.json` (config)
- `src/open_clip/model_configs/coca_ViT-L-14.json` (config)
- `src/open_clip/model_configs/coca_base.json` (config)
- `src/open_clip/model_configs/coca_roberta-ViT-B-32.json` (config)
- `src/open_clip/model_configs/convnext_base.json` (config)
- `src/open_clip/model_configs/convnext_base_w.json` (config)
- `src/open_clip/model_configs/convnext_base_w_320.json` (config)
- `src/open_clip/model_configs/convnext_large.json` (config)
- `src/open_clip/model_configs/convnext_large_d.json` (config)
- `src/open_clip/model_configs/convnext_large_d_320.json` (config)
- `src/open_clip/model_configs/convnext_small.json` (config)
- `src/open_clip/model_configs/convnext_tiny.json` (config)
- `src/open_clip/model_configs/convnext_xlarge.json` (config)
- `src/open_clip/model_configs/convnext_xxlarge.json` (config)
- `src/open_clip/model_configs/convnext_xxlarge_320.json` (config)
- `src/open_clip/model_configs/gte-modernbert-base-ViT-B-32-256.json` (config)
- `src/open_clip/model_configs/mammut2-moderntext_ViT-B-32.json` (config)
- `src/open_clip/model_configs/mammut2-naflex_ViT-B-16.json` (config)
- `src/open_clip/model_configs/mammut2-naflex_ViT-B-32.json` (config)
- `src/open_clip/model_configs/mammut2_ViT-B-16.json` (config)
- `src/open_clip/model_configs/mammut2_ViT-B-32.json` (config)
- `src/open_clip/model_configs/mammut2_ViT-L-14.json` (config)
- `src/open_clip/model_configs/mammut_ViT-L-14.json` (config)
- `src/open_clip/model_configs/moderntext-ViT-B-32-256.json` (config)
- `src/open_clip/model_configs/moderntext-naflex_ViT-B-16.json` (config)
- `src/open_clip/model_configs/moderntext-naflex_ViT-B-32.json` (config)
- `src/open_clip/model_configs/moderntext-naflex_ViT-B-deep-16.json` (config)
- `src/open_clip/model_configs/moderntext-naflex_ViT-SO150M2-16.json` (config)
- `src/open_clip/model_configs/mt5-base-ViT-B-32.json` (config)
- `src/open_clip/model_configs/mt5-xl-ViT-H-14.json` (config)
- `src/open_clip/model_configs/naflex_ViT-B-16.json` (config)
- `src/open_clip/model_configs/naflex_ViT-B-32.json` (config)
- `src/open_clip/model_configs/naflexclap_base_pf4_pt20_moderntextp.json` (config)
- `src/open_clip/model_configs/naflexclap_base_pf8_pt16_moderntext.json` (config)
- `src/open_clip/model_configs/naflexclap_base_pf8_pt16_moderntextp.json` (config)
- `src/open_clip/model_configs/naflexclap_base_pf8_pt20_moderntextp.json` (config)
- `src/open_clip/model_configs/naflexclap_large.json` (config)
- `src/open_clip/model_configs/naflexclap_little.json` (config)
- `src/open_clip/model_configs/naflexclap_little_roberta.json` (config)
- `src/open_clip/model_configs/naflexclap_medium.json` (config)
- `src/open_clip/model_configs/naflexclap_mediumd.json` (config)
- `src/open_clip/model_configs/naflexclap_mediumd_pf4_pt20_moderntextp.json` (config)
- `src/open_clip/model_configs/naflexclap_mediumd_roberta.json` (config)
- `src/open_clip/model_configs/naflexclap_small.json` (config)
- `src/open_clip/model_configs/naflexclap_test.json` (config)
- `src/open_clip/model_configs/naflexclap_xs.json` (config)
- `src/open_clip/model_configs/naflexclap_xxs.json` (config)
- `src/open_clip/model_configs/naflexgenlap_betwixt.json` (config)
- `src/open_clip/model_configs/naflexgenlap_so150m2.json` (config)
- `src/open_clip/model_configs/naflexgenlap_test_1d.json` (config)
- `src/open_clip/model_configs/naflexgenlap_test_2d.json` (config)
- `src/open_clip/model_configs/naflexgenlip_b16.json` (config)
- `src/open_clip/model_configs/naflexgenlip_so150m2.json` (config)
- `src/open_clip/model_configs/naflexgenlip_so16.json` (config)
- `src/open_clip/model_configs/naflexgenlip_test.json` (config)
- `src/open_clip/model_configs/nllb-clip-base-siglip.json` (config)
- `src/open_clip/model_configs/nllb-clip-base.json` (config)
- `src/open_clip/model_configs/nllb-clip-large-siglip.json` (config)
- `src/open_clip/model_configs/nllb-clip-large.json` (config)
- `src/open_clip/model_configs/roberta-ViT-B-32.json` (config)
- `src/open_clip/model_configs/swin_base_patch4_window7_224.json` (config)
- `src/open_clip/model_configs/vit_medium_patch16_gap_256.json` (config)
- `src/open_clip/model_configs/vit_relpos_medium_patch16_cls_224.json` (config)
- `src/open_clip/model_configs/xlm-roberta-base-ViT-B-32.json` (config)
- `src/open_clip/model_configs/xlm-roberta-large-ViT-H-14.json` (config)

## Top-level layout

- `src` — 272 analysed file(s)
- `tests` — 57 analysed file(s)
- `docs` — 23 analysed file(s)
- `scripts` — 19 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4cc208d3a44a2fb6d6435006a46f520d2ccc29b1` is the revision these paths and observations refer to.
