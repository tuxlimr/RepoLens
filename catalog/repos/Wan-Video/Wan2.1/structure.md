# Project structure: Wan-Video/Wan2.1

**Analysed commit:** `9737cba9c1c3c4d04b33fcad41c111989865d315`

**Commit reference:** [9737cba9c1c3c4d04b33fcad41c111989865d315](https://github.com/Wan-Video/Wan2.1/commit/9737cba9c1c3c4d04b33fcad41c111989865d315)

**Tree at this commit:** [Wan-Video/Wan2.1@9737cba9c1c3](https://github.com/Wan-Video/Wan2.1/tree/9737cba9c1c3c4d04b33fcad41c111989865d315)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Wan-Video/Wan2.1 |
| Description | Wan: Open and Advanced Large-Scale Video Generative Models |
| Stars | 17435 |
| Forks | 4061 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `9737cba9c1c3c4d04b33fcad41c111989865d315` |
| Retrieved at | 2026-11-14T19:08:34.475519+00:00 |
| Files in this snapshot | 46 |

## Directory tree

```text
gradio/  (6 files)
  fl2v_14B_singleGPU.py
  i2v_14B_singleGPU.py
  t2i_14B_singleGPU.py
  t2v_1.3B_singleGPU.py
  t2v_14B_singleGPU.py
  vace.py
tests/  (2 files)
  README.md
  test.sh
wan/  (29 files)
  configs/  (5 files)
    __init__.py
    shared_config.py
    wan_i2v_14B.py
    wan_t2v_14B.py
    wan_t2v_1_3B.py
  distributed/  (3 files)
    __init__.py
    fsdp.py
    xdit_context_parallel.py
  modules/  (9 files)
    __init__.py
    attention.py
    clip.py
    model.py
    t5.py
    tokenizers.py
    vace_model.py
    vae.py
    xlm_roberta.py
  utils/  (7 files)
    __init__.py
    fm_solvers.py
    fm_solvers_unipc.py
    prompt_extend.py
    qwen_vl_utils.py
    utils.py
    vace_processor.py
  __init__.py
  first_last_frame2video.py
  image2video.py
  text2video.py
  vace.py
.gitignore
.style.yapf
INSTALL.md
LICENSE.txt
Makefile
README.md
generate.py
pyproject.toml
requirements.txt
```

## Entry points

- [generate.py:585](https://github.com/Wan-Video/Wan2.1/blob/9737cba9c1c3c4d04b33fcad41c111989865d315/generate.py#L585)
- [gradio/fl2v_14B_singleGPU.py:238](https://github.com/Wan-Video/Wan2.1/blob/9737cba9c1c3c4d04b33fcad41c111989865d315/gradio/fl2v_14B_singleGPU.py#L238)
- [gradio/i2v_14B_singleGPU.py:272](https://github.com/Wan-Video/Wan2.1/blob/9737cba9c1c3c4d04b33fcad41c111989865d315/gradio/i2v_14B_singleGPU.py#L272)
- [gradio/t2i_14B_singleGPU.py:177](https://github.com/Wan-Video/Wan2.1/blob/9737cba9c1c3c4d04b33fcad41c111989865d315/gradio/t2i_14B_singleGPU.py#L177)
- [gradio/t2v_1.3B_singleGPU.py:179](https://github.com/Wan-Video/Wan2.1/blob/9737cba9c1c3c4d04b33fcad41c111989865d315/gradio/t2v_1.3B_singleGPU.py#L179)
- [gradio/t2v_14B_singleGPU.py:177](https://github.com/Wan-Video/Wan2.1/blob/9737cba9c1c3c4d04b33fcad41c111989865d315/gradio/t2v_14B_singleGPU.py#L177)
- [gradio/vace.py:289](https://github.com/Wan-Video/Wan2.1/blob/9737cba9c1c3c4d04b33fcad41c111989865d315/gradio/vace.py#L289)
- [wan/utils/prompt_extend.py:526](https://github.com/Wan-Video/Wan2.1/blob/9737cba9c1c3c4d04b33fcad41c111989865d315/wan/utils/prompt_extend.py#L526)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Head, MLPProj, WanAttentionBlock, WanI2VCrossAttention, WanLayerNorm, WanModel. Observed top-level func… |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: DashScopePromptExpander, FixedSizeQueue, PromptExpander, PromptOutput, QwenPromptExpander,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |
| wan package | library | Observed | Groups 22 file(s) under wan package (observed from repository paths and static analysis). Observed top-level classes: AttentionBlock, AttentionPool, BaseWanAttentionBlock, CLIPModel, CausalConv3d, Decoder3d. Observed to… |

## Important files

- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `wan` — 29 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `gradio` — 6 analysed file(s)
- `tests` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9737cba9c1c3c4d04b33fcad41c111989865d315` is the revision these paths and observations refer to.
