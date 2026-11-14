# Project structure: Wan-Video/Wan2.2

**Analysed commit:** `1ea34ff48f87168174e12956e200b1d908b1c5ff`

**Commit reference:** [1ea34ff48f87168174e12956e200b1d908b1c5ff](https://github.com/Wan-Video/Wan2.2/commit/1ea34ff48f87168174e12956e200b1d908b1c5ff)

**Tree at this commit:** [Wan-Video/Wan2.2@1ea34ff48f87](https://github.com/Wan-Video/Wan2.2/tree/1ea34ff48f87168174e12956e200b1d908b1c5ff)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Wan-Video/Wan2.2 |
| Description | Wan: Open and Advanced Large-Scale Video Generative Models |
| Stars | 18649 |
| Forks | 2480 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `1ea34ff48f87168174e12956e200b1d908b1c5ff` |
| Retrieved at | 2026-11-14T19:08:22.295166+00:00 |
| Files in this snapshot | 69 |

## Directory tree

```text
tests/  (2 files)
  README.md
  test.sh
wan/  (57 files)
  configs/  (7 files)
    __init__.py
    shared_config.py
    wan_animate_14B.py
    wan_i2v_A14B.py
    wan_s2v_14B.py
    wan_t2v_A14B.py
    wan_ti2v_5B.py
  distributed/  (5 files)
    __init__.py
    fsdp.py
    sequence_parallel.py
    ulysses.py
    util.py
  modules/  (32 files)
    animate/  (18 files)
      … 18 files under this directory
    s2v/  (7 files)
      … 7 files under this directory
    __init__.py
    attention.py
    model.py
    t5.py
    tokenizers.py
    vae2_1.py
    vae2_2.py
  utils/  (7 files)
    __init__.py
    fm_solvers.py
    fm_solvers_unipc.py
    prompt_extend.py
    qwen_vl_utils.py
    system_prompt.py
    utils.py
  __init__.py
  animate.py
  image2video.py
  speech2video.py
  text2video.py
  textimage2video.py
.gitignore
INSTALL.md
LICENSE.txt
Makefile
README.md
generate.py
pyproject.toml
requirements.txt
requirements_animate.txt
requirements_s2v.txt
```

## Entry points

- [generate.py:573](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/generate.py#L573)
- [wan/modules/animate/preprocess/human_visualization.py:1280](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/wan/modules/animate/preprocess/human_visualization.py#L1280)
- [wan/modules/animate/preprocess/preprocess_data.py:94](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/wan/modules/animate/preprocess/preprocess_data.py#L94)
- [wan/modules/s2v/motioner.py:785](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/wan/modules/s2v/motioner.py#L785)
- [wan/utils/prompt_extend.py:430](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/wan/utils/prompt_extend.py#L430)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Head, WanAttentionBlock, WanCrossAttention, WanLayerNorm, WanModel, WanRMSNorm. Observed top-level func… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CasualSelfAttention, DashScopePromptExpander, FramePackMotioner, Head, LayerNorm, Motioner… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |
| wan package | library | Observed | Groups 44 file(s) under wan package (observed from repository paths and static analysis). Observed top-level classes: AAPoseMeta, AttentionBlock, AttentionPool, AudioCrossAttention, AudioEncoder, AudioInjector_WAN. Obse… |

## Important files

- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `requirements_animate.txt` (manifest)
- `requirements_s2v.txt` (manifest)

## Top-level layout

- `wan` — 57 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `tests` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1ea34ff48f87168174e12956e200b1d908b1c5ff` is the revision these paths and observations refer to.
