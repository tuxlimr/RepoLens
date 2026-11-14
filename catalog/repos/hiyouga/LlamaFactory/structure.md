# Project structure: hiyouga/LlamaFactory

**Analysed commit:** `5f1f6ad537e69216e0604671223cc1eeecbb7ba6`

**Commit reference:** [5f1f6ad537e69216e0604671223cc1eeecbb7ba6](https://github.com/hiyouga/LlamaFactory/commit/5f1f6ad537e69216e0604671223cc1eeecbb7ba6)

**Tree at this commit:** [hiyouga/LlamaFactory@5f1f6ad537e6](https://github.com/hiyouga/LlamaFactory/tree/5f1f6ad537e69216e0604671223cc1eeecbb7ba6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hiyouga/LlamaFactory |
| Description | Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) |
| Stars | 76042 |
| Forks | 9371 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `5f1f6ad537e69216e0604671223cc1eeecbb7ba6` |
| Retrieved at | 2026-11-14T19:06:12.240998+00:00 |
| Files in this snapshot | 606 |

## Directory tree

```text
.agents/  (5 files)
  skills/  (5 files)
    llamafactory-qwen38-sft/  (5 files)
      … 5 files under this directory
.ai/  (1 files)
  CLAUDE.md
.claude/  (7 files)
  skills/  (7 files)
    llamafactory-qwen38-sft/  (5 files)
      … 5 files under this directory
    llamafactory-sft/  (1 files)
      … 1 files under this directory
    llamafactory-v1-docs/  (1 files)
      … 1 files under this directory
.github/  (18 files)
  ISSUE_TEMPLATE/  (3 files)
    1-bug-report.yml
    2-feature-request.yml
    config.yml
  workflows/  (8 files)
    docker.yml
    docker_npu.yml
    docs.yml
    label_issue.yml
    publish.yml
    tests.yml
    tests_cuda.yml
    tests_npu.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
  SECURITY.md
  copilot-instructions.md
  instructions-v0.md
  instructions-v1.md
assets/  (6 files)
  sponsors/  (1 files)
    serpapi.svg
  thirdparty/  (5 files)
    colab.svg
    discord.svg
    dsw.svg
    lab4ai.svg
    online.svg
data/  (13 files)
  README.md
  README_zh.md
  dataset_info.json
  identity.json
  mllm_audio_demo.json
  mllm_demo.json
  mllm_video_audio_demo.json
  mllm_video_demo.json
  v1_dpo_demo.jsonl
  v1_dpo_demo.yaml
  v1_multimodal_demo.jsonl
  v1_multimodal_demo.yaml
  v1_sft_demo.yaml
docker/  (16 files)
  docker-cuda/  (6 files)
    Dockerfile
    Dockerfile.base
    Dockerfile.mbridge
    Dockerfile.megatron
    README.md
    docker-compose.yml
  docker-npu/  (5 files)
    Dockerfile
    OVERVIEW.md
    OVERVIEW.zh.md
    docker-compose.yml
    supported_tags.md
  docker-rocm/  (2 files)
    Dockerfile
    docker-compose.yml
  docker-xpu/  (3 files)
    Dockerfile
    README.md
    docker-compose.yml
docs/  (74 files)
  _static/  (3 files)
    css/  (2 files)
      … 2 files under this directory
    js/  (1 files)
      … 1 files under this directory
  en/  (30 files)
    advanced/  (10 files)
      … 10 files under this directory
    data-preparation/  (1 files)
      … 1 files under this directory
    dev-guide/  (7 files)
      … 7 files under this directory
    hyperparameters/  (4 files)
      … 4 files under this directory
    inference/  (1 files)
      … 1 files under this directory
    training/  (2 files)
      … 2 files under this directory
    conf.py
    getting-started.md
    index.rst
    installation.md
    llamaboard-web-ui.md
  zh/  (37 files)
    configuration/  (5 files)
      … 5 files under this directory
    developer-guide/  (16 files)
      … 16 files under this directory
    feature-guide/  (12 files)
      … 12 files under this directory
    multi-backend/  (1 files)
      … 1 files under this directory
    conf.py
    index.rst
    quick_start.md
  Makefile
  conf.py
  make.bat
  requirements.txt
examples/  (112 files)
  accelerate/  (7 files)
    fsdp2_config.yaml
    fsdp2_config_qwen35.yaml
    fsdp2_config_qwen35_moe.yaml
    fsdp2_config_qwen38.yaml
    fsdp_config.yaml
    fsdp_config_multiple_nodes.yaml
    fsdp_config_offload.yaml
  ascend/  (7 files)
    qwen3_5_full_sft_fsdp2.yaml
    qwen3_5moe_lora_sft_fsdp2.yaml
    qwen3_8_full_sft_hyper_fsdp2.yaml
    qwen3_full_sft_fsdp2.yaml
    qwen3moe_full_sft_fsdp.yaml
    qwen3vlmoe_full_sft_fsdp2.yaml
    qwen3vlmoe_lora_sft_fsdp.yaml
  deepspeed/  (7 files)
    ds_z0_config.json
    ds_z2_autotp_config.json
    ds_z2_config.json
    ds_z2_offload_config.json
    ds_z3_config.json
    ds_z3_fp8_config.json
    ds_z3_offload_config.json
  extras/  (26 files)
    adam_mini/  (1 files)
      … 1 files under this directory
    apollo/  (1 files)
      … 1 files under this directory
    asft/  (2 files)
      … 2 files under this directory
    badam/  (1 files)
      … 1 files under this directory
    dft/  (1 files)
      … 1 files under this directory
    eaft/  (1 files)
      … 1 files under this directory
    fp8/  (2 files)
      … 2 files under this directory
    fsdp_qlora/  (2 files)
      … 2 files under this directory
    galore/  (1 files)
      … 1 files under this directory
    llama_pro/  (2 files)
      … 2 files under this directory
    loraplus/  (1 files)
      … 1 files under this directory
    mod/  (1 files)
      … 1 files under this directory
    multi_tokens/  (1 files)
      … 1 files under this directory
    muon/  (1 files)
      … 1 files under this directory
    nlg_eval/  (1 files)
      … 1 files under this directory
    oft/  (2 files)
      … 2 files under this directory
    pissa/  (2 files)
      … 2 files under this directory
    qoft/  (3 files)
      … 3 files under this directory
  inference/  (5 files)
    mossvl.yaml
    qwen3.yaml
    qwen3_full_sft.yaml
    qwen3_lora_sft.yaml
    qwen3vl.yaml
  ktransformers/  (11 files)
    accelerate/  (5 files)
      … 5 files under this directory
    train_lora/  (6 files)
      … 6 files under this directory
  megatron/  (2 files)
    qwen2_vl_full.yaml
    qwen3_moe_full.yaml
  megatron_bridge/  (1 files)
    llama3_sft.yaml
  merge_lora/  (5 files)
    mossvl_lora_sft.yaml
    qwen3_full_sft.yaml
    qwen3_gptq.yaml
    qwen3_lora_sft.yaml
    qwen3vl_lora_sft.yaml
  train_full/  (3 files)
    mossvl_full_sft.yaml
    qwen3_full_sft.yaml
    qwen3vl_full_sft.yaml
  train_lora/  (12 files)
    mossvl_lora_sft.yaml
    qwen3_lora_dpo.yaml
    qwen3_lora_kto.yaml
    qwen3_lora_pretrain.yaml
    qwen3_lora_reward.yaml
    qwen3_lora_sft.sh
    qwen3_lora_sft.yaml
    qwen3_lora_sft_ds3.yaml
    qwen3_lora_sft_ray.yaml
    qwen3_preprocess.yaml
    qwen3vl_lora_dpo.yaml
    qwen3vl_lora_sft.yaml
  train_qlora/  (5 files)
    llama3_lora_sft_aqlm.yaml
    llama3_lora_sft_awq.yaml
    llama3_lora_sft_gptq.yaml
    qwen3_lora_sft_bnb_npu.yaml
    qwen3_lora_sft_otfq.yaml
  v1/  (19 files)
    train_batching_strategy/  (4 files)
      … 4 files under this directory
    train_freeze/  (1 files)
      … 1 files under this directory
    train_full/  (9 files)
      … 9 files under this directory
    train_lora/  (4 files)
      … 4 files under this directory
    train_qlora/  (1 files)
      … 1 files under this directory
  README.md
  README_zh.md
requirements/  (26 files)
  adam-mini.txt
  apollo.txt
  aqlm.txt
  badam.txt
  bitsandbytes.txt
  deepspeed.txt
  dev.txt
  eetq.txt
  fp8-te.txt
  fp8.txt
  fsdpturbo.txt
  galore.txt
  gptq.txt
  hqq.txt
  ktransformers.txt
  liger-kernel.txt
  metrics.txt
  minicpm-v.txt
  moss-vl.txt
  npu.txt
  openmind.txt
  sglang.txt
  swanlab.txt
  triton_ascend.txt
  … 2 more files
scripts/  (21 files)
  api_example/  (2 files)
    test_image.py
    test_toolcall.py
  convert_ckpt/  (4 files)
    llamafy_baichuan2.py
    llamafy_qwen.py
    tiny_llama4.py
    tiny_qwen3.py
  stat_utils/  (5 files)
    cal_flops.py
    cal_lr.py
    cal_mfu.py
    cal_ppl.py
    length_cdf.py
  bench_qwen.py
  dcp2hf.py
  eval_bleu_rouge.py
  hf2dcp.py
  llama_pro.py
  loftq_init.py
  megatron_merge.py
  pissa_init.py
  qwen_omni_merge.py
  vllm_infer.py
src/  (236 files)
  llamafactory/  (233 files)
    api/  (5 files)
      … 5 files under this directory
    chat/  (6 files)
      … 6 files under this directory
    data/  (17 files)
      … 17 files under this directory
    eval/  (3 files)
      … 3 files under this directory
    extras/  (7 files)
      … 7 files under this directory
    hparams/  (9 files)
      … 9 files under this directory
    model/  (20 files)
      … 20 files under this directory
    third_party/  (11 files)
      … 11 files under this directory
    train/  (39 files)
      … 39 files under this directory
    v1/  (94 files)
      … 94 files under this directory
    webui/  (19 files)
      … 19 files under this directory
    __init__.py
    cli.py
    launcher.py
  api.py
  train.py
  webui.py
tests/  (39 files)
  data/  (13 files)
    processor/  (5 files)
      … 5 files under this directory
    test_collator.py
    test_converter.py
    test_formatter.py
    test_loader.py
    test_mm_plugin.py
    test_moss_vl_plugin.py
    test_moss_vl_training_configs.py
    test_template.py
  e2e/  (3 files)
    test_chat.py
    test_sglang.py
    test_train.py
  eval/  (1 files)
    test_eval_template.py
  model/  (12 files)
    model_utils/  (7 files)
      … 7 files under this directory
    test_base.py
    test_freeze.py
    test_full.py
    test_lora.py
    test_pissa.py
  train/  (7 files)
    megatron_bridge/  (5 files)
      … 5 files under this directory
    test_hyper_parallel.py
    test_sft_trainer.py
  check_license.py
  conftest.py
  version.txt
tests_v1/  (21 files)
  accelerator/  (1 files)
    test_interface.py
  config/  (1 files)
    test_args_parser.py
  core/  (4 files)
    rendering/  (1 files)
      … 1 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    test_data_engine.py
    test_model_loader.py
  plugins/  (10 files)
    data_plugins/  (1 files)
      … 1 files under this directory
    model_plugins/  (6 files)
      … 6 files under this directory
    trainer_plugins/  (3 files)
      … 3 files under this directory
  sampler/  (1 files)
    test_cli_sampler.py
  trainers/  (3 files)
    test_dpo_loss_precision.py
    test_fsdp2_dpo_trainer.py
    test_fsdp2_sft_trainer.py
  conftest.py
.dockerignore
.gitattributes
.gitignore
.pre-commit-config.yaml
CITATION.cff
LICENSE
MANIFEST.in
Makefile
README.md
README_zh.md
pyproject.toml
```

## Entry points

- [src/api.py:32](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/api.py#L32)
- [src/llamafactory/api/app.py:71](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/api/app.py#L71)
- [src/llamafactory/cli.py](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/cli.py)
- [src/llamafactory/cli.py](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/cli.py)
- [src/llamafactory/launcher.py:182](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/launcher.py#L182)
- [src/llamafactory/v1/accelerator/interface.py:272](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/v1/accelerator/interface.py#L272)
- [src/llamafactory/v1/config/arg_parser.py:68](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/v1/config/arg_parser.py#L68)
- [src/llamafactory/v1/core/data_engine.py:215](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/v1/core/data_engine.py#L215)
- [src/llamafactory/v1/core/model_engine.py:242](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/v1/core/model_engine.py#L242)
- [src/llamafactory/v1/core/utils/batching.py:367](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/v1/core/utils/batching.py#L367)
- [src/llamafactory/v1/launcher.py:187](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/v1/launcher.py#L187)
- [src/llamafactory/v1/samplers/cli_sampler.py:124](https://github.com/hiyouga/LlamaFactory/blob/5f1f6ad537e69216e0604671223cc1eeecbb7ba6/src/llamafactory/v1/samplers/cli_sampler.py#L124)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: ChatCompletionMessage, ChatCompletionRequest, ChatCompletionResponse, ChatCompletionResponseChoice, Chat… |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BatchingStrategy, DataArguments, ModelArguments, ModelClass, PluginConfig, SampleArg… |
| Data layer | data | Observed | Groups 17 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AlpacaDatasetConverter, BasePlugin, DatasetAttr, DatasetConverter, DatasetModule, DatasetProcessor. Ob… |
| Application entry point | entrypoint | Observed | Groups 35 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: BatchGenerator, DPOTrainer, DataEngine,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| llamafactory package | library | Observed | Groups 180 file(s) under llamafactory package (observed from repository paths and static analysis). Observed top-level classes: AlpacaSample, ApolloArguments, AttentionFunction, AverageMeter, BAdamArgument, Backend. Obs… |
| Service / domain layer | service | Observed | Groups 12 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: BaseEngine, BaseSampler, BaseTrainer, HuggingFaceEngine, Renderer, TrainingCheckpointCoord… |
| Tests | test | Observed | Groups 63 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CharTokenizer, DataCollatorWithVerbose, FakeFusedExpertsModel, FakeLegacyExpert, FakeLegacyExpertsModel, Ho… |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/1-bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/2-feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/docker_npu.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/label_issue.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/tests_cuda.yml` (ci)
- `.github/workflows/tests_npu.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `data/dataset_info.json` (config)
- `data/identity.json` (config)
- `data/mllm_audio_demo.json` (config)
- `data/mllm_demo.json` (config)
- `data/mllm_video_audio_demo.json` (config)
- `data/mllm_video_demo.json` (config)
- `data/v1_dpo_demo.yaml` (config)
- `data/v1_multimodal_demo.yaml` (config)
- `data/v1_sft_demo.yaml` (config)
- `docker/docker-cuda/Dockerfile` (container)
- `docker/docker-cuda/Dockerfile.base` (container)
- `docker/docker-cuda/Dockerfile.mbridge` (container)
- `docker/docker-cuda/Dockerfile.megatron` (container)
- `docker/docker-cuda/docker-compose.yml` (container)
- `docker/docker-npu/Dockerfile` (container)
- `docker/docker-npu/docker-compose.yml` (container)
- `docker/docker-rocm/Dockerfile` (container)
- `docker/docker-rocm/docker-compose.yml` (container)
- `docker/docker-xpu/Dockerfile` (container)
- `docker/docker-xpu/docker-compose.yml` (container)
- `docs/requirements.txt` (manifest)
- `examples/accelerate/fsdp2_config.yaml` (config)
- `examples/accelerate/fsdp2_config_qwen35.yaml` (config)
- `examples/accelerate/fsdp2_config_qwen35_moe.yaml` (config)
- `examples/accelerate/fsdp2_config_qwen38.yaml` (config)
- `examples/accelerate/fsdp_config.yaml` (config)
- `examples/accelerate/fsdp_config_multiple_nodes.yaml` (config)
- `examples/accelerate/fsdp_config_offload.yaml` (config)
- `examples/ascend/qwen3_5_full_sft_fsdp2.yaml` (config)
- `examples/ascend/qwen3_5moe_lora_sft_fsdp2.yaml` (config)
- `examples/ascend/qwen3_8_full_sft_hyper_fsdp2.yaml` (config)
- `examples/ascend/qwen3_full_sft_fsdp2.yaml` (config)
- `examples/ascend/qwen3moe_full_sft_fsdp.yaml` (config)
- `examples/ascend/qwen3vlmoe_full_sft_fsdp2.yaml` (config)
- `examples/ascend/qwen3vlmoe_lora_sft_fsdp.yaml` (config)
- `examples/deepspeed/ds_z0_config.json` (config)
- `examples/deepspeed/ds_z2_autotp_config.json` (config)
- `examples/deepspeed/ds_z2_config.json` (config)
- `examples/deepspeed/ds_z2_offload_config.json` (config)
- `examples/deepspeed/ds_z3_config.json` (config)
- `examples/deepspeed/ds_z3_fp8_config.json` (config)
- `examples/deepspeed/ds_z3_offload_config.json` (config)
- `examples/extras/adam_mini/qwen2_full_sft.yaml` (config)
- `examples/extras/apollo/llama3_full_sft.yaml` (config)
- `examples/extras/asft/llama2_full_asft.yaml` (config)
- `examples/extras/asft/qwen2_full_asft.yaml` (config)
- `examples/extras/badam/llama3_full_sft.yaml` (config)
- `examples/extras/dft/qwen2_full_sft.yaml` (config)
- `examples/extras/eaft/qwen25_05b_eaft_full.yaml` (config)
- `examples/extras/fp8/llama3_fp8_deepspeed_sft.yaml` (config)
- `examples/extras/fp8/llama3_fp8_fsdp_sft.yaml` (config)
- `examples/extras/fsdp_qlora/llama3_lora_sft.yaml` (config)
- `examples/extras/galore/llama3_full_sft.yaml` (config)
- `examples/extras/llama_pro/llama3_freeze_sft.yaml` (config)
- `examples/extras/loraplus/llama3_lora_sft.yaml` (config)
- `examples/extras/mod/llama3_full_sft.yaml` (config)
- `examples/extras/multi_tokens/tokens_cfg.yaml` (config)
- `examples/extras/muon/qwen2_full_sft.yaml` (config)
- `examples/extras/nlg_eval/llama3_lora_predict.yaml` (config)
- `examples/extras/oft/llama3_oft_sft.yaml` (config)
- `examples/extras/oft/qwen2_5vl_oft_sft.yaml` (config)
- `examples/extras/pissa/llama3_lora_sft.yaml` (config)
- `examples/extras/qoft/llama3_oft_sft_awq.yaml` (config)
- `examples/extras/qoft/llama3_oft_sft_bnb_npu.yaml` (config)
- `examples/extras/qoft/llama3_oft_sft_gptq.yaml` (config)
- `examples/inference/mossvl.yaml` (config)
- `examples/inference/qwen3.yaml` (config)
- `examples/inference/qwen3_full_sft.yaml` (config)
- `examples/inference/qwen3_lora_sft.yaml` (config)
- `examples/inference/qwen3vl.yaml` (config)
- `examples/ktransformers/accelerate/fsdp2_kt_bf16.yaml` (config)
- `examples/ktransformers/accelerate/fsdp2_kt_int4.yaml` (config)
- `examples/ktransformers/accelerate/fsdp2_kt_int8.yaml` (config)
- `examples/ktransformers/accelerate/fsdp2_kt_int8_1gpu.yaml` (config)
- `examples/ktransformers/accelerate/fsdp2_kt_int8_8gpu.yaml` (config)
- `examples/ktransformers/train_lora/deepseek_v2_lora_sft_kt.yaml` (config)
- `examples/ktransformers/train_lora/deepseek_v3_int8_lora_sft_kt.yaml` (config)
- `examples/ktransformers/train_lora/deepseek_v3_lora_sft_kt.yaml` (config)
- `examples/ktransformers/train_lora/qwen3_5moe_lora_sft_kt.yaml` (config)
- `examples/ktransformers/train_lora/qwen3moe_lora_sft_kt.yaml` (config)
- `examples/ktransformers/train_lora/qwen3vlmoe_lora_sft_kt.yaml` (config)
- `examples/megatron/qwen2_vl_full.yaml` (config)
- `examples/megatron/qwen3_moe_full.yaml` (config)
- `examples/megatron_bridge/llama3_sft.yaml` (config)
- `examples/merge_lora/mossvl_lora_sft.yaml` (config)
- `examples/merge_lora/qwen3_full_sft.yaml` (config)
- `examples/merge_lora/qwen3_gptq.yaml` (config)
- `examples/merge_lora/qwen3_lora_sft.yaml` (config)
- `examples/merge_lora/qwen3vl_lora_sft.yaml` (config)
- `examples/train_full/mossvl_full_sft.yaml` (config)
- `examples/train_full/qwen3_full_sft.yaml` (config)
- `examples/train_full/qwen3vl_full_sft.yaml` (config)
- `examples/train_lora/mossvl_lora_sft.yaml` (config)
- `examples/train_lora/qwen3_lora_dpo.yaml` (config)
- `examples/train_lora/qwen3_lora_kto.yaml` (config)
- `examples/train_lora/qwen3_lora_pretrain.yaml` (config)
- `examples/train_lora/qwen3_lora_reward.yaml` (config)
- `examples/train_lora/qwen3_lora_sft.yaml` (config)
- `examples/train_lora/qwen3_lora_sft_ds3.yaml` (config)
- `examples/train_lora/qwen3_lora_sft_ray.yaml` (config)
- `examples/train_lora/qwen3_preprocess.yaml` (config)
- `examples/train_lora/qwen3vl_lora_dpo.yaml` (config)
- `examples/train_lora/qwen3vl_lora_sft.yaml` (config)
- `examples/train_qlora/llama3_lora_sft_aqlm.yaml` (config)
- `examples/train_qlora/llama3_lora_sft_awq.yaml` (config)
- `examples/train_qlora/llama3_lora_sft_gptq.yaml` (config)
- `examples/train_qlora/qwen3_lora_sft_bnb_npu.yaml` (config)
- `examples/train_qlora/qwen3_lora_sft_otfq.yaml` (config)
- `examples/v1/train_batching_strategy/train_full_fsdp2_batching_normal.yaml` (config)
- `examples/v1/train_batching_strategy/train_full_fsdp2_dynamic_batching.yaml` (config)
- `examples/v1/train_batching_strategy/train_full_fsdp2_dynamic_padding_free.yaml` (config)
- `examples/v1/train_batching_strategy/train_full_fsdp2_padding_free.yaml` (config)
- `examples/v1/train_freeze/train_freeze_sft.yaml` (config)
- `examples/v1/train_full/train_full_chunk_loss.yaml` (config)
- `examples/v1/train_full/train_full_deepspeed.yaml` (config)
- `examples/v1/train_full/train_full_fsdp2.yaml` (config)
- `examples/v1/train_full/train_full_liger_kernel.yaml` (config)
- `examples/v1/train_full/train_full_multimodal_ulysses_cp.yaml` (config)
- `examples/v1/train_full/train_full_muon.yaml` (config)
- `examples/v1/train_full/train_full_qwen3_moe_fsdpturbo_ep_fsdp.yaml` (config)
- `examples/v1/train_full/train_full_ulysses_cp.yaml` (config)
- `examples/v1/train_full/train_multimodal.yaml` (config)
- `examples/v1/train_lora/export_lora.yaml` (config)
- `examples/v1/train_lora/train_lora_dpo.yaml` (config)
- `examples/v1/train_lora/train_lora_sft.yaml` (config)
- `examples/v1/train_lora/train_lora_sft_rank0.yaml` (config)
- `examples/v1/train_qlora/quantization.yaml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `src` — 236 analysed file(s)
- `examples` — 112 analysed file(s)
- `docs` — 74 analysed file(s)
- `tests` — 39 analysed file(s)
- `requirements` — 26 analysed file(s)
- `scripts` — 21 analysed file(s)
- `tests_v1` — 21 analysed file(s)
- `.github` — 18 analysed file(s)
- `docker` — 16 analysed file(s)
- `data` — 13 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.claude` — 7 analysed file(s)
- `assets` — 6 analysed file(s)
- `.agents` — 5 analysed file(s)
- `.ai` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5f1f6ad537e69216e0604671223cc1eeecbb7ba6` is the revision these paths and observations refer to.
