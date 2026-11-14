# Project structure: BlinkDL/RWKV-LM

**Analysed commit:** `2eebb381a6160837ac45896c60d6963ef3cda929`

**Commit reference:** [2eebb381a6160837ac45896c60d6963ef3cda929](https://github.com/BlinkDL/RWKV-LM/commit/2eebb381a6160837ac45896c60d6963ef3cda929)

**Tree at this commit:** [BlinkDL/RWKV-LM@2eebb381a616](https://github.com/BlinkDL/RWKV-LM/tree/2eebb381a6160837ac45896c60d6963ef3cda929)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BlinkDL/RWKV-LM |
| Description | RWKV (pronounced RwaKuv) is an RNN with great LLM performance, which can also be directly trained like a GPT transformer (parallelizable). We are at RWKV-7 "Goose". So it's combining the best of RNN and transformer - great performance, linear time, constant space (no kv-cache), fast training, infin… |
| Stars | 14774 |
| Forks | 1026 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `2eebb381a6160837ac45896c60d6963ef3cda929` |
| Retrieved at | 2026-11-14T19:09:16.460861+00:00 |
| Files in this snapshot | 160 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
RWKV-v1/  (5 files)
  src/  (4 files)
    __init__.py
    model.py
    trainer.py
    utils.py
  train.py
RWKV-v2-RNN/  (8 files)
  cuda/  (2 files)
    timex_cuda.cu
    timex_op.cpp
  src/  (4 files)
    model.py
    model_run.py
    trainer.py
    utils.py
  run.py
  train.py
RWKV-v3/  (9 files)
  cuda/  (2 files)
    timex_cuda.cu
    timex_op.cpp
  src/  (4 files)
    model.py
    model_run.py
    trainer.py
    utils.py
  run.py
  train.py
  verify.py
RWKV-v4/  (10 files)
  cuda/  (2 files)
    wkv_cuda.cu
    wkv_op.cpp
  src/  (5 files)
    binidx.py
    model.py
    model_run.py
    trainer.py
    utils.py
  run.py
  train.py
  verify.py
RWKV-v4neo/  (20 files)
  cuda/  (6 files)
    wkv5_cuda.cu
    wkv5_op.cpp
    wkv_cuda.cu
    wkv_cuda_bf16.cu
    wkv_op.cpp
    wkv_op_bf16.cpp
  math_demo/  (1 files)
    run.py
  src/  (8 files)
    __init__.py
    binidx.py
    dataset.py
    model.py
    model_img.py
    model_run.py
    trainer.py
    utils.py
  chat.py
  img_demoAE.py
  run.py
  train.py
  verify.py
RWKV-v5/  (25 files)
  cuda/  (8 files)
    wkv5_cuda.cu
    wkv5_op.cpp
    wkv6_cuda.cu
    wkv6_op.cpp
    wkv6state_cuda.cu
    wkv6state_op.cpp
    wkv7_cuda.cu
    wkv7_op.cpp
  src/  (6 files)
    __init__.py
    binidx.py
    dataset.py
    model.py
    trainer.py
    utils.py
  tokenizer/  (2 files)
    __init__.py
    rwkv_tokenizer.py
  compute_magic_prime.py
  demo-training-prepare-v7-pile.sh
  demo-training-prepare.sh
  demo-training-run-v7-pile.sh
  demo-training-run.sh
  make_data.py
  requirements.txt
  rwkv_v6_demo.py
  train.py
RWKV-v6/  (1 files)
  README.md
RWKV-v7/  (63 files)
  cuda/  (4 files)
    wkv7.cu
    wkv7_op.cpp
    wkv7s.cu
    wkv7s_op.cpp
  mmlu_dev_dataset/  (2 files)
    dataset_info.json
    state.json
  mmlu_test_dataset/  (2 files)
    dataset_info.json
    state.json
  train_temp/  (40 files)
    cuda/  (27 files)
      … 27 files under this directory
    src/  (5 files)
      … 5 files under this directory
    README.md
    demo-training-prepare-v7-pile.sh
    demo-training-prepare.sh
    demo-training-run-v7-pile.sh
    demo-training-run.sh
    requirements.txt
    rwkv7_train_simplified.py
    train.py
  README.md
  RWKV7-G1x-templates.txt
  run_qwen35_make_pth.py
  run_rwkv7_context_parallelism.py
  run_rwkv7_qwen35.md
  run_rwkv7_qwen35.py
  rwkv_mmlu_eval.py
  rwkv_v7_demo.py
  rwkv_v7_demo_fast.py
  rwkv_v7_demo_rnn.py
  rwkv_v7_numpy.py
  rwkv_v7a_demo.py
  rwkv_v7b_demo.py
  rwkv_v8_rc00_demo.py
  rwkv_v8_rc00_hybrid_demo.py
RWKV-v8/  (12 files)
  cuda/  (2 files)
    wkv7_cuda.cu
    wkv7_op.cpp
  251014_rosa_1bit_layer.py
  251014_rosa_1bit_train.py
  251014_rosa_onlyemb_train.py
  251016_rosa_1bit_run.py
  251018_rosa_4bit_run.py
  251024_rosaQKV_run.py
  251105_reverse_run.py
  260212_rosa1bitLM_L12.py
  260222_rosa4bitLM_L12.py
  README.md
Research/  (1 files)
  rwkv7-g0-7.2b.md
.gitignore
CITATION.cff
LICENSE
README.md
RWKV-8.md
```

## Entry points

- [RWKV-v2-RNN/train.py:79](https://github.com/BlinkDL/RWKV-LM/blob/2eebb381a6160837ac45896c60d6963ef3cda929/RWKV-v2-RNN/train.py#L79)
- [RWKV-v3/train.py:99](https://github.com/BlinkDL/RWKV-LM/blob/2eebb381a6160837ac45896c60d6963ef3cda929/RWKV-v3/train.py#L99)
- [RWKV-v4/train.py:190](https://github.com/BlinkDL/RWKV-LM/blob/2eebb381a6160837ac45896c60d6963ef3cda929/RWKV-v4/train.py#L190)
- [RWKV-v4neo/train.py:8](https://github.com/BlinkDL/RWKV-LM/blob/2eebb381a6160837ac45896c60d6963ef3cda929/RWKV-v4neo/train.py#L8)
- [RWKV-v5/train.py:8](https://github.com/BlinkDL/RWKV-LM/blob/2eebb381a6160837ac45896c60d6963ef3cda929/RWKV-v5/train.py#L8)
- [RWKV-v7/run_qwen35_make_pth.py:222](https://github.com/BlinkDL/RWKV-LM/blob/2eebb381a6160837ac45896c60d6963ef3cda929/RWKV-v7/run_qwen35_make_pth.py#L222)
- [RWKV-v7/run_rwkv7_context_parallelism.py:182](https://github.com/BlinkDL/RWKV-LM/blob/2eebb381a6160837ac45896c60d6963ef3cda929/RWKV-v7/run_rwkv7_context_parallelism.py#L182)
- [RWKV-v7/run_rwkv7_qwen35.py:246](https://github.com/BlinkDL/RWKV-LM/blob/2eebb381a6160837ac45896c60d6963ef3cda929/RWKV-v7/run_rwkv7_qwen35.py#L246)
- [RWKV-v7/train_temp/train.py:8](https://github.com/BlinkDL/RWKV-LM/blob/2eebb381a6160837ac45896c60d6963ef3cda929/RWKV-v7/train_temp/train.py#L8)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 7 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Block, FixedNorm, GPT, GPTConfig, GeGLU, L2Wrap. Observed top-level functions: RUN_CUDA, RWKV_Init, __n… |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: LLM, Qwen35, RWKV7, RWKV_RNN, TOKENIZER. Observed top-level functions: DPLR, DPLR_RWKV, D… |
| RWKV-v1 package | library | Observed | Groups 4 file(s) under rwkv-v1 package (observed from repository paths and static analysis). Observed top-level classes: Dataset, Trainer, TrainerConfig. Observed top-level functions: sample_logits, set_seed, top_k_logi… |
| RWKV-v2-RNN package | library | Observed | Groups 4 file(s) under rwkv-v2-rnn package (observed from repository paths and static analysis). Observed top-level classes: Dataset, RWKV_RNN, TOKENIZER, Trainer, TrainerConfig. Observed top-level functions: set_seed,… |
| RWKV-v3 package | library | Observed | Groups 5 file(s) under rwkv-v3 package (observed from repository paths and static analysis). Observed top-level classes: Block, Dataset, RWKV_ChannelMix, RWKV_GPT, RWKV_RNN, RWKV_TimeMix. Observed top-level functions: s… |
| RWKV-v4 package | library | Observed | Groups 6 file(s) under rwkv-v4 package (observed from repository paths and static analysis). Observed top-level classes: Block, Dataset, MMapIndexedDataset, RWKV_ChannelMix, RWKV_GPT, RWKV_RNN. Observed top-level functi… |
| RWKV-v4neo package | library | Observed | Groups 13 file(s) under rwkv-v4neo package (observed from repository paths and static analysis). Observed top-level classes: DISTS, L2pooling, MMapIndexedDataset, MyDataset, RWKV_IMG, RWKV_RNN. Observed top-level functi… |
| RWKV-v5 package | library | Observed | Groups 18 file(s) under rwkv-v5 package (observed from repository paths and static analysis). Observed top-level classes: Block, MMapIndexedDataset, MMapIndexedDatasetBuilder, MyDataset, RWKV, RWKV_CMix_x060. Observed t… |
| RWKV-v7 package | library | Observed | Groups 33 file(s) under rwkv-v7 package (observed from repository paths and static analysis). Observed top-level classes: Block, FFN, MMapIndexedDataset, MODEL, MyDataset, RWKV. Observed top-level functions: RUN_CUDA_RW… |
| RWKV-v8 package | library | Observed | Groups 10 file(s) under rwkv-v8 package (observed from repository paths and static analysis). Observed top-level classes: Block, Emb_ROSA, FFN, MODEL, ROSA_1bit, ROSA_1bit_LAYER. Observed top-level functions: RUN_CUDA_R… |

## Important files

- `.github/FUNDING.yml` (config)
- `RWKV-v5/requirements.txt` (manifest)
- `RWKV-v7/mmlu_dev_dataset/dataset_info.json` (config)
- `RWKV-v7/mmlu_dev_dataset/state.json` (config)
- `RWKV-v7/mmlu_test_dataset/dataset_info.json` (config)
- `RWKV-v7/mmlu_test_dataset/state.json` (config)
- `RWKV-v7/train_temp/requirements.txt` (manifest)

## Top-level layout

- `RWKV-v7` — 63 analysed file(s)
- `RWKV-v5` — 25 analysed file(s)
- `RWKV-v4neo` — 20 analysed file(s)
- `RWKV-v8` — 12 analysed file(s)
- `RWKV-v4` — 10 analysed file(s)
- `RWKV-v3` — 9 analysed file(s)
- `RWKV-v2-RNN` — 8 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `RWKV-v1` — 5 analysed file(s)
- `.github` — 1 analysed file(s)
- `RWKV-v6` — 1 analysed file(s)
- `Research` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2eebb381a6160837ac45896c60d6963ef3cda929` is the revision these paths and observations refer to.
