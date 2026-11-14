# Project structure: lllyasviel/stable-diffusion-webui-forge

**Analysed commit:** `dfdcbab685e57677014f05a3309b48cc87383167`

**Commit reference:** [dfdcbab685e57677014f05a3309b48cc87383167](https://github.com/lllyasviel/stable-diffusion-webui-forge/commit/dfdcbab685e57677014f05a3309b48cc87383167)

**Tree at this commit:** [lllyasviel/stable-diffusion-webui-forge@dfdcbab685e5](https://github.com/lllyasviel/stable-diffusion-webui-forge/tree/dfdcbab685e57677014f05a3309b48cc87383167)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lllyasviel/stable-diffusion-webui-forge |
| Description | Not provided |
| Stars | 13126 |
| Forks | 1787 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `dfdcbab685e57677014f05a3309b48cc87383167` |
| Retrieved at | 2026-11-14T19:09:57.697372+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
backend/  (219 files)
  diffusion_engine/  (7 files)
    base.py
    chroma.py
    flux.py
    sd15.py
    sd20.py
    sd35.py
    sdxl.py
  huggingface/  (168 files)
    Chroma/  (7 files)
      … 7 files under this directory
    Kwai-Kolors/  (8 files)
      … 8 files under this directory
    Tencent-Hunyuan/  (11 files)
      … 11 files under this directory
    black-forest-labs/  (24 files)
      … 24 files under this directory
    diffusers/  (10 files)
      … 10 files under this directory
    lllyasviel/  (1 files)
      … 1 files under this directory
    playgroundai/  (10 files)
      … 10 files under this directory
    runwayml/  (19 files)
      … 19 files under this directory
    stabilityai/  (78 files)
      … 78 files under this directory
  misc/  (5 files)
    checkpoint_pickle.py
    diffusers_state_dict.py
    image_resize.py
    sub_quadratic_attention.py
    tomesd.py
  modules/  (3 files)
    k_diffusion_extra.py
    k_model.py
    k_prediction.py
  nn/  (10 files)
    cnets/  (2 files)
      … 2 files under this directory
    base.py
    chroma.py
    clip.py
    flux.py
    mmditx.py
    t5.py
    unet.py
    vae.py
  patcher/  (7 files)
    base.py
    clip.py
    clipvision.py
    controlnet.py
    lora.py
    unet.py
    vae.py
  sampling/  (2 files)
    condition.py
    sampling_function.py
  text_processing/  (5 files)
    classic_engine.py
    emphasis.py
    parsing.py
    t5_engine.py
    textual_inversion.py
  README.md
  args.py
  attention.py
  loader.py
  memory_management.py
  operations.py
  operations_bnb.py
  operations_gguf.py
  shared.py
  state_dict.py
  stream.py
  utils.py
embeddings/  (1 files)
  Place Textual Inversion embeddings here.txt
extensions-builtin/  (566 files)
  ScuNET/  (2 files)
    scripts/  (1 files)
      … 1 files under this directory
    preload.py
  SwinIR/  (2 files)
    scripts/  (1 files)
      … 1 files under this directory
    preload.py
  extra-options-section/  (1 files)
    scripts/  (1 files)
      … 1 files under this directory
  forge_legacy_preprocessors/  (561 files)
    annotator/  (559 files)
      … 559 files under this directory
    .gitignore
    LICENSE
.eslintignore
.eslintrc.js
.git-blame-ignore-revs
.gitignore
.pylintrc
CHANGELOG.md
CITATION.cff
CODEOWNERS
LICENSE.txt
NEWS.md
README.md
_typos.toml
download_supported_configs.py
environment-wsl2.yaml
```

## Entry points

- [extensions-builtin/forge_legacy_preprocessors/annotator/leres/leres/network_auxi.py:411](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/leres/leres/network_auxi.py#L411)
- [extensions-builtin/forge_legacy_preprocessors/annotator/leres/pix2pix/util/html.py:76](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/leres/pix2pix/util/html.py#L76)
- [extensions-builtin/forge_legacy_preprocessors/annotator/mmpkg/mmseg/utils/collect_env.py:15](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/mmpkg/mmseg/utils/collect_env.py#L15)
- [extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/data/datasets/cityscapes.py:281](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/data/datasets/cityscapes.py#L281)
- [extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/data/datasets/coco.py:509](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/data/datasets/coco.py#L509)
- [extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/data/datasets/coco_panoptic.py:193](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/data/datasets/coco_panoptic.py#L193)
- [extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/data/datasets/lvis.py:213](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/data/datasets/lvis.py#L213)
- [extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/evaluation/panoptic_evaluation.py:180](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/evaluation/panoptic_evaluation.py#L180)
- [extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/utils/collect_env.py:225](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/utils/collect_env.py#L225)
- [extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/utils/colormap.py:145](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/detectron2/utils/colormap.py#L145)
- [extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/oneformer/demo/colormap.py:157](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/dfdcbab685e57677014f05a3309b48cc87383167/extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/oneformer/demo/colormap.py#L157)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 5 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: BaseFileHandler, JsonHandler, PickleHandler, YamlHandler. Observed top-level functions: set_default. |
| backend package | library | Observed | Groups 50 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: AbstractPrediction, Adapter, Adapter_light, Approximator, AttentionProcessorForge, AttnBlock. Obs… |
| Configuration and deployment | config | Observed | Groups 188 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: CfgNode, Config, ConfigDict, ConverterV1, ConverterV2, DictAction. Observed top-lev… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 100 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ACM, AFNB, ANNHead, APCHead, APNB, ASPPHead. Observed top-level functions: HFlip_rotated_box, Resize_… |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AO, ATA, COCOPanopticEvaluator, Decoder, DepthNet, FFM. Observed top-level functions: _ci… |
| extensions-builtin package | library | Observed | Groups 393 file(s) under extensions-builtin package (observed from repository paths and static analysis). Observed top-level classes: ADE20KDataset, AMPTrainer, ASPP, AddReadout, AdjustGamma, AlexNet. Observed top-level… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BaseStorageBackend, COCOeval_opt, CephBackend, FileClient, HTTPBackend, HardDiskBackend. |
| Service / domain layer | service | Observed | Groups 12 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: BasePixelSampler, DistEvalHook, EvalHook, OHEMPixelSampler. Observed top-level functions:… |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: DatasetMapperTTA, GeneralizedRCNNWithTTA, MultiScaleFlipAug, TestOptions. |

## Important files

- `_typos.toml` (config)
- `backend/huggingface/Chroma/model_index.json` (config)
- `backend/huggingface/Chroma/scheduler/scheduler_config.json` (config)
- `backend/huggingface/Chroma/text_encoder/config.json` (config)
- `backend/huggingface/Chroma/text_encoder/model.safetensors.index.json` (config)
- `backend/huggingface/Chroma/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/Chroma/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/Chroma/vae/config.json` (config)
- `backend/huggingface/Kwai-Kolors/Kolors/model_index.json` (config)
- `backend/huggingface/Kwai-Kolors/Kolors/scheduler/scheduler_config.json` (config)
- `backend/huggingface/Kwai-Kolors/Kolors/text_encoder/config.json` (config)
- `backend/huggingface/Kwai-Kolors/Kolors/text_encoder/pytorch_model.bin.index.json` (config)
- `backend/huggingface/Kwai-Kolors/Kolors/text_encoder/tokenizer_config.json` (config)
- `backend/huggingface/Kwai-Kolors/Kolors/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/Kwai-Kolors/Kolors/unet/config.json` (config)
- `backend/huggingface/Kwai-Kolors/Kolors/vae/config.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/model_index.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/scheduler/scheduler_config.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/text_encoder/config.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/text_encoder_2/config.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/text_encoder_2/model.safetensors.index.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/tokenizer_2/special_tokens_map.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/tokenizer_2/tokenizer_config.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/transformer/config.json` (config)
- `backend/huggingface/Tencent-Hunyuan/HunyuanDiT-Diffusers/vae/config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/model_index.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/scheduler/scheduler_config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/text_encoder/config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/text_encoder_2/config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/text_encoder_2/model.safetensors.index.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/tokenizer_2/special_tokens_map.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/tokenizer_2/tokenizer_config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/transformer/config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/transformer/diffusion_pytorch_model.safetensors.index.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-dev/vae/config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/model_index.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/scheduler/scheduler_config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/text_encoder/config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/text_encoder_2/config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/text_encoder_2/model.safetensors.index.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/tokenizer_2/special_tokens_map.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/tokenizer_2/tokenizer_config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/transformer/config.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/transformer/diffusion_pytorch_model.safetensors.index.json` (config)
- `backend/huggingface/black-forest-labs/FLUX.1-schnell/vae/config.json` (config)
- `backend/huggingface/diffusers/stable-diffusion-xl-1.0-inpainting-0.1/model_index.json` (config)
- `backend/huggingface/diffusers/stable-diffusion-xl-1.0-inpainting-0.1/scheduler/scheduler_config.json` (config)
- `backend/huggingface/diffusers/stable-diffusion-xl-1.0-inpainting-0.1/text_encoder/config.json` (config)
- `backend/huggingface/diffusers/stable-diffusion-xl-1.0-inpainting-0.1/text_encoder_2/config.json` (config)
- `backend/huggingface/diffusers/stable-diffusion-xl-1.0-inpainting-0.1/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/diffusers/stable-diffusion-xl-1.0-inpainting-0.1/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/diffusers/stable-diffusion-xl-1.0-inpainting-0.1/tokenizer_2/special_tokens_map.json` (config)
- `backend/huggingface/diffusers/stable-diffusion-xl-1.0-inpainting-0.1/tokenizer_2/tokenizer_config.json` (config)
- `backend/huggingface/diffusers/stable-diffusion-xl-1.0-inpainting-0.1/unet/config.json` (config)
- `backend/huggingface/diffusers/stable-diffusion-xl-1.0-inpainting-0.1/vae/config.json` (config)
- `backend/huggingface/lllyasviel/control_v11p_sd15_canny/config.json` (config)
- `backend/huggingface/playgroundai/playground-v2.5-1024px-aesthetic/model_index.json` (config)
- `backend/huggingface/playgroundai/playground-v2.5-1024px-aesthetic/scheduler/scheduler_config.json` (config)
- `backend/huggingface/playgroundai/playground-v2.5-1024px-aesthetic/text_encoder/config.json` (config)
- `backend/huggingface/playgroundai/playground-v2.5-1024px-aesthetic/text_encoder_2/config.json` (config)
- `backend/huggingface/playgroundai/playground-v2.5-1024px-aesthetic/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/playgroundai/playground-v2.5-1024px-aesthetic/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/playgroundai/playground-v2.5-1024px-aesthetic/tokenizer_2/special_tokens_map.json` (config)
- `backend/huggingface/playgroundai/playground-v2.5-1024px-aesthetic/tokenizer_2/tokenizer_config.json` (config)
- `backend/huggingface/playgroundai/playground-v2.5-1024px-aesthetic/unet/config.json` (config)
- `backend/huggingface/playgroundai/playground-v2.5-1024px-aesthetic/vae/config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-inpainting/config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-inpainting/feature_extractor/preprocessor_config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-inpainting/model_index.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-inpainting/safety_checker/config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-inpainting/scheduler/scheduler_config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-inpainting/text_encoder/config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-inpainting/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-inpainting/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-inpainting/unet/config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-inpainting/vae/config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-v1-5/feature_extractor/preprocessor_config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-v1-5/model_index.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-v1-5/safety_checker/config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-v1-5/scheduler/scheduler_config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-v1-5/text_encoder/config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-v1-5/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-v1-5/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-v1-5/unet/config.json` (config)
- `backend/huggingface/runwayml/stable-diffusion-v1-5/vae/config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade-prior/feature_extractor/preprocessor_config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade-prior/image_encoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade-prior/model_index.json` (config)
- `backend/huggingface/stabilityai/stable-cascade-prior/prior/config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade-prior/prior_lite/config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade-prior/scheduler/scheduler_config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade-prior/text_encoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade-prior/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-cascade-prior/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade/decoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade/decoder_lite/config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade/model_index.json` (config)
- `backend/huggingface/stabilityai/stable-cascade/scheduler/scheduler_config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade/text_encoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-cascade/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-cascade/vqgan/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-1/feature_extractor/preprocessor_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-1/model_index.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-1/scheduler/scheduler_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-1/text_encoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-1/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-1/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-1/unet/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-1/vae/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-inpainting/feature_extractor/preprocessor_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-inpainting/model_index.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-inpainting/scheduler/scheduler_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-inpainting/text_encoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-inpainting/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-inpainting/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-inpainting/unet/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-2-inpainting/vae/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/model_index.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/scheduler/scheduler_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/text_encoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/text_encoder_2/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/text_encoder_3/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/text_encoder_3/model.safetensors.index.fp16.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/text_encoder_3/model.safetensors.index.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/tokenizer_2/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/tokenizer_2/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/tokenizer_3/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/tokenizer_3/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/transformer/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-3-medium-diffusers/vae/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-x4-upscaler/low_res_scheduler/scheduler_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-x4-upscaler/model_index.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-x4-upscaler/scheduler/scheduler_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-x4-upscaler/text_encoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-x4-upscaler/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-x4-upscaler/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-x4-upscaler/unet/.ipynb_checkpoints/config-checkpoint.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-x4-upscaler/unet/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-x4-upscaler/vae/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/model_index.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/scheduler/scheduler_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/text_encoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/text_encoder_2/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/tokenizer_2/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/tokenizer_2/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/unet/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/vae/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/vae_1_0/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/vae_decoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-base-1.0/vae_encoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-refiner-1.0/model_index.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-refiner-1.0/scheduler/scheduler_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-refiner-1.0/text_encoder/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-refiner-1.0/tokenizer/special_tokens_map.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-refiner-1.0/tokenizer/tokenizer_config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-refiner-1.0/unet/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-refiner-1.0/vae/config.json` (config)
- `backend/huggingface/stabilityai/stable-diffusion-xl-refiner-1.0/vae_1_0/config.json` (config)
- `environment-wsl2.yaml` (config)
- `extensions-builtin/forge_legacy_preprocessors/annotator/mmpkg/mmcv/model_zoo/deprecated.json` (config)
- `extensions-builtin/forge_legacy_preprocessors/annotator/mmpkg/mmcv/model_zoo/mmcls.json` (config)
- `extensions-builtin/forge_legacy_preprocessors/annotator/mmpkg/mmcv/model_zoo/open_mmlab.json` (config)
- `extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/configs/ade20k/Base-ADE20K-UnifiedSegmentation.yaml` (config)
- `extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/configs/ade20k/oneformer_R50_bs16_160k.yaml` (config)
- `extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/configs/ade20k/oneformer_swin_large_IN21k_384_bs16_160k.yaml` (config)
- `extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/configs/coco/Base-COCO-UnifiedSegmentation.yaml` (config)
- `extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/configs/coco/oneformer_R50_bs16_50ep.yaml` (config)
- `extensions-builtin/forge_legacy_preprocessors/annotator/oneformer/configs/coco/oneformer_swin_large_IN21k_384_bs16_100ep.yaml` (config)

## Top-level layout

- `extensions-builtin` — 566 analysed file(s)
- `backend` — 219 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `embeddings` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `dfdcbab685e57677014f05a3309b48cc87383167` is the revision these paths and observations refer to.
