# Project structure: LlamaChinese/Llama-Chinese

**Analysed commit:** `6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b`

**Commit reference:** [6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b](https://github.com/LlamaChinese/Llama-Chinese/commit/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b)

**Tree at this commit:** [LlamaChinese/Llama-Chinese@6fa0fffb0dd8](https://github.com/LlamaChinese/Llama-Chinese/tree/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | LlamaChinese/Llama-Chinese |
| Description | Llama中文社区，实时汇总最新Llama学习资料，构建最好的中文Llama大模型开源生态，完全开源可商用 |
| Stars | 14755 |
| Forks | 1282 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b` |
| Retrieved at | 2026-11-14T19:09:17.116912+00:00 |
| Files in this snapshot | 48 |

## Directory tree

```text
assets/  (2 files)
  meta_eval_13B.md
  meta_eval_7B.md
data/  (1 files)
  dev_sft.csv
docker/  (3 files)
  Dockerfile
  Dockerfile_train
  docker-compose.yml
docs/  (2 files)
  chat_gradio_guide.md
  inference_speed_guide.md
examples/  (3 files)
  chat_gradio.py
  chat_gradio_no_merge.py
  llama2_for_langchain.py
inference-speed/  (13 files)
  CPU/  (1 files)
    ggml/  (1 files)
      … 1 files under this directory
  GPU/  (12 files)
    FasterTransformer_example/  (1 files)
      … 1 files under this directory
    JittorLLMs_example/  (1 files)
      … 1 files under this directory
    TensorRT-LLM_example/  (3 files)
      … 3 files under this directory
    lmdeploy_example/  (2 files)
      … 2 files under this directory
    vllm_example/  (5 files)
      … 5 files under this directory
scripts/  (6 files)
  api/  (3 files)
    README.md
    accelerate_client.py
    accelerate_server.py
  convert2hf/  (2 files)
    README.md
    convert_llama_weights_to_hf.py
  test_model/  (1 files)
    test_pretrain_model.ipynb
train/  (15 files)
  merge_peft_model/  (4 files)
    merge.sh
    merge_muilt.sh
    merge_muilt_peft_adapter.py
    merge_peft_adapter.py
  pretrain/  (5 files)
    accuracy.py
    ds_config_zero2.json
    ds_config_zero3.json
    pretrain.sh
    pretrain_clm.py
  sft/  (6 files)
    accuracy.py
    ds_config_zero2.json
    finetune.sh
    finetune_clm.py
    finetune_clm_lora.py
    finetune_lora.sh
README.md
README_EN.md
requirements.txt
```

## Entry points

- [inference-speed/GPU/TensorRT-LLM_example/atom_inference.py:182](https://github.com/LlamaChinese/Llama-Chinese/blob/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b/inference-speed/GPU/TensorRT-LLM_example/atom_inference.py#L182)
- [inference-speed/GPU/vllm_example/api_server.py:16](https://github.com/LlamaChinese/Llama-Chinese/blob/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b/inference-speed/GPU/vllm_example/api_server.py#L16)
- [inference-speed/GPU/vllm_example/client_test.py:125](https://github.com/LlamaChinese/Llama-Chinese/blob/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b/inference-speed/GPU/vllm_example/client_test.py#L125)
- [scripts/api/accelerate_client.py:45](https://github.com/LlamaChinese/Llama-Chinese/blob/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b/scripts/api/accelerate_client.py#L45)
- [scripts/api/accelerate_server.py:30](https://github.com/LlamaChinese/Llama-Chinese/blob/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b/scripts/api/accelerate_server.py#L30)
- [scripts/convert2hf/convert_llama_weights_to_hf.py:305](https://github.com/LlamaChinese/Llama-Chinese/blob/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b/scripts/convert2hf/convert_llama_weights_to_hf.py#L305)
- [train/pretrain/pretrain_clm.py:613](https://github.com/LlamaChinese/Llama-Chinese/blob/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b/train/pretrain/pretrain_clm.py#L613)
- [train/sft/finetune_clm.py:613](https://github.com/LlamaChinese/Llama-Chinese/blob/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b/train/sft/finetune_clm.py#L613)
- [train/sft/finetune_clm_lora.py:693](https://github.com/LlamaChinese/Llama-Chinese/blob/6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b/train/sft/finetune_clm_lora.py#L693)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /generate, POST /generate. Observed top-level c… |
| inference-speed package | library | Observed | Groups 3 file(s) under inference-speed package (observed from repository paths and static analysis). Observed top-level functions: get_engine_version, load_tokenizer, read_model_name, throttle_generator. |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: get_prompt_llama2_meta, get_prompt_llama3_meta, get_prompt_llama_chinese, input_prompt, main, test_api_ser… |
| train package | library | Observed | Groups 9 file(s) under train package (observed from repository paths and static analysis). Observed top-level classes: Accuracy, ScriptArguments. |

## Important files

- `docker/Dockerfile` (container)
- `docker/Dockerfile_train` (container)
- `docker/docker-compose.yml` (container)
- `requirements.txt` (manifest)
- `train/pretrain/ds_config_zero2.json` (config)
- `train/pretrain/ds_config_zero3.json` (config)
- `train/sft/ds_config_zero2.json` (config)

## Top-level layout

- `train` — 15 analysed file(s)
- `inference-speed` — 13 analysed file(s)
- `scripts` — 6 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `docker` — 3 analysed file(s)
- `examples` — 3 analysed file(s)
- `assets` — 2 analysed file(s)
- `docs` — 2 analysed file(s)
- `data` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b` is the revision these paths and observations refer to.
