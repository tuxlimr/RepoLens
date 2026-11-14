# Project structure: ymcui/Chinese-LLaMA-Alpaca

**Analysed commit:** `5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14`

**Commit reference:** [5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14](https://github.com/ymcui/Chinese-LLaMA-Alpaca/commit/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14)

**Tree at this commit:** [ymcui/Chinese-LLaMA-Alpaca@5b8bb552e8b7](https://github.com/ymcui/Chinese-LLaMA-Alpaca/tree/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ymcui/Chinese-LLaMA-Alpaca |
| Description | 中文LLaMA&Alpaca大语言模型+本地CPU/GPU训练部署 (Chinese LLaMA & Alpaca LLMs) |
| Stars | 18911 |
| Forks | 1831 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14` |
| Retrieved at | 2026-11-14T19:08:21.891353+00:00 |
| Files in this snapshot | 89 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    ISSUE_TEMPLATE_EN.yml
    ISSUE_TEMPLATE_ZH.yml
    config.yml
  workflows/  (1 files)
    stale.yml
data/  (1 files)
  README.md
examples/  (45 files)
  f16-p7b-p13b-33b/  (11 files)
    CODE.md
    DIALOGUE.md
    ENTERTAINMENT.md
    ETHICS.md
    GENERATION.md
    LITERATURE.md
    OQA.md
    QA.md
    README.md
    REASONING.md
    TRANSLATION.md
  q4_7b-13b/  (11 files)
    CODE.md
    DIALOGUE.md
    ENTERTAINMENT.md
    ETHICS.md
    GENERATION.md
    LITERATURE.md
    OQA.md
    QA.md
    README.md
    REASONING.md
    TRANSLATION.md
  q8_13b-p7b-p13b/  (11 files)
    CODE.md
    DIALOGUE.md
    ENTERTAINMENT.md
    ETHICS.md
    GENERATION.md
    LITERATURE.md
    OQA.md
    QA.md
    README.md
    REASONING.md
    TRANSLATION.md
  q8_7b-13b-p7b/  (11 files)
    CODE.md
    DIALOGUE.md
    ENTERTAINMENT.md
    ETHICS.md
    GENERATION.md
    LITERATURE.md
    OQA.md
    QA.md
    README.md
    REASONING.md
    TRANSLATION.md
  README.md
notebooks/  (6 files)
  legacy/  (2 files)
    convert_and_quantize_chinese_alpaca_plus.ipynb
    convert_and_quantize_chinese_llama.ipynb
  README.md
  finetune_chinese_alpaca_lora.ipynb
  gradio_web_demo.ipynb
  pretrain_chinese_llama_lora.ipynb
scripts/  (25 files)
  ceval/  (4 files)
    eval.py
    evaluator.py
    llama_evaluator.py
    subject_mapping.json
  inference/  (3 files)
    gradio_demo.py
    inference_hf.py
    patches.py
  langchain/  (3 files)
    doc.txt
    langchain_qa.py
    langchain_sum.py
  merge_tokenizer/  (1 files)
    merge_tokenizers.py
  openai_server_demo/  (4 files)
    README.md
    openai_api_protocol.py
    openai_api_server.py
    patches.py
  training/  (6 files)
    build_dataset.py
    ds_zero2_no_offload.json
    run_clm_pt_with_peft.py
    run_clm_sft_with_peft.py
    run_pt.sh
    run_sft.sh
  README.md
  crawl_prompt.py
  merge_llama_with_chinese_lora.py
  merge_llama_with_chinese_lora_low_mem.py
.gitattributes
.gitignore
CITATION.cff
LICENSE.md
README.md
README_EN.md
SHA256.md
requirements.txt
```

## Entry points

- [scripts/ceval/eval.py:79](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14/scripts/ceval/eval.py#L79)
- [scripts/crawl_prompt.py:31](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14/scripts/crawl_prompt.py#L31)
- [scripts/inference/inference_hf.py:56](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14/scripts/inference/inference_hf.py#L56)
- [scripts/langchain/langchain_qa.py:56](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14/scripts/langchain/langchain_qa.py#L56)
- [scripts/langchain/langchain_sum.py:37](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14/scripts/langchain/langchain_sum.py#L37)
- [scripts/merge_llama_with_chinese_lora.py:214](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14/scripts/merge_llama_with_chinese_lora.py#L214)
- [scripts/merge_llama_with_chinese_lora_low_mem.py:226](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14/scripts/merge_llama_with_chinese_lora_low_mem.py#L226)
- [scripts/openai_server_demo/openai_api_server.py:172](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14/scripts/openai_server_demo/openai_api_server.py#L172)
- [scripts/training/run_clm_pt_with_peft.py:641](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14/scripts/training/run_clm_pt_with_peft.py#L641)
- [scripts/training/run_clm_sft_with_peft.py:440](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14/scripts/training/run_clm_sft_with_peft.py#L440)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /v1/chat/completions, POST /v1/completions, PO… |
| scripts package | library | Observed | Groups 10 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: ChatCompletionRequest, ChatCompletionResponse, ChatCompletionResponseChoice, ChatMessage, Complet… |

## Important files

- `.github/ISSUE_TEMPLATE/ISSUE_TEMPLATE_EN.yml` (config)
- `.github/ISSUE_TEMPLATE/ISSUE_TEMPLATE_ZH.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/stale.yml` (ci)
- `requirements.txt` (manifest)
- `scripts/ceval/subject_mapping.json` (config)
- `scripts/training/ds_zero2_no_offload.json` (config)

## Top-level layout

- `examples` — 45 analysed file(s)
- `scripts` — 25 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `notebooks` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `data` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5b8bb552e8b738da0f19a8e2cedf6db6b5c3fd14` is the revision these paths and observations refer to.
