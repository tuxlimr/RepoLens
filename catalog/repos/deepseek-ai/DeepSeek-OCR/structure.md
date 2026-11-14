# Project structure: deepseek-ai/DeepSeek-OCR

**Analysed commit:** `09eaf526153e7a01ed16c9dea8c96282aaea29c0`

**Commit reference:** [09eaf526153e7a01ed16c9dea8c96282aaea29c0](https://github.com/deepseek-ai/DeepSeek-OCR/commit/09eaf526153e7a01ed16c9dea8c96282aaea29c0)

**Tree at this commit:** [deepseek-ai/DeepSeek-OCR@09eaf526153e](https://github.com/deepseek-ai/DeepSeek-OCR/tree/09eaf526153e7a01ed16c9dea8c96282aaea29c0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | deepseek-ai/DeepSeek-OCR |
| Description | Contexts Optical Compression |
| Stars | 24162 |
| Forks | 2218 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `09eaf526153e7a01ed16c9dea8c96282aaea29c0` |
| Retrieved at | 2026-11-14T19:07:40.301703+00:00 |
| Files in this snapshot | 18 |

## Directory tree

```text
DeepSeek-OCR-master/  (13 files)
  DeepSeek-OCR-hf/  (1 files)
    run_dpsk_ocr.py
  DeepSeek-OCR-vllm/  (12 files)
    deepencoder/  (4 files)
      … 4 files under this directory
    process/  (3 files)
      … 3 files under this directory
    config.py
    deepseek_ocr.py
    run_dpsk_ocr_eval_batch.py
    run_dpsk_ocr_image.py
    run_dpsk_ocr_pdf.py
assets/  (2 files)
  badge.svg
  logo.svg
LICENSE
README.md
requirements.txt
```

## Entry points

- [DeepSeek-OCR-master/DeepSeek-OCR-vllm/deepencoder/clip_sdpa.py:455](https://github.com/deepseek-ai/DeepSeek-OCR/blob/09eaf526153e7a01ed16c9dea8c96282aaea29c0/DeepSeek-OCR-master/DeepSeek-OCR-vllm/deepencoder/clip_sdpa.py#L455)
- [DeepSeek-OCR-master/DeepSeek-OCR-vllm/run_dpsk_ocr_eval_batch.py:91](https://github.com/deepseek-ai/DeepSeek-OCR/blob/09eaf526153e7a01ed16c9dea8c96282aaea29c0/DeepSeek-OCR-master/DeepSeek-OCR-vllm/run_dpsk_ocr_eval_batch.py#L91)
- [DeepSeek-OCR-master/DeepSeek-OCR-vllm/run_dpsk_ocr_image.py:204](https://github.com/deepseek-ai/DeepSeek-OCR/blob/09eaf526153e7a01ed16c9dea8c96282aaea29c0/DeepSeek-OCR-master/DeepSeek-OCR-vllm/run_dpsk_ocr_image.py#L204)
- [DeepSeek-OCR-master/DeepSeek-OCR-vllm/run_dpsk_ocr_pdf.py:233](https://github.com/deepseek-ai/DeepSeek-OCR/blob/09eaf526153e7a01ed16c9dea8c96282aaea29c0/DeepSeek-OCR-master/DeepSeek-OCR-vllm/run_dpsk_ocr_pdf.py#L233)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| DeepSeek-OCR-master package | library | Observed | Groups 8 file(s) under deepseek-ocr-master package (observed from repository paths and static analysis). Observed top-level classes: Attention, Block, DeepseekOCRDummyInputsBuilder, DeepseekOCRForCausalLM, DeepseekOCRMu… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CLIPVisionEmbeddings, Colors, LayerNormfp32, NoTPAttention, NoTPFeedForward, NoTPTransform… |

## Important files

- `requirements.txt` (manifest)

## Top-level layout

- `DeepSeek-OCR-master` — 13 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `assets` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `09eaf526153e7a01ed16c9dea8c96282aaea29c0` is the revision these paths and observations refer to.
