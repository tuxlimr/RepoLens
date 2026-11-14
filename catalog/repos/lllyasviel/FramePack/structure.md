# Project structure: lllyasviel/FramePack

**Analysed commit:** `97fe5dbe06ac1f337ece08935b1076a35eefeeb9`

**Commit reference:** [97fe5dbe06ac1f337ece08935b1076a35eefeeb9](https://github.com/lllyasviel/FramePack/commit/97fe5dbe06ac1f337ece08935b1076a35eefeeb9)

**Tree at this commit:** [lllyasviel/FramePack@97fe5dbe06ac](https://github.com/lllyasviel/FramePack/tree/97fe5dbe06ac1f337ece08935b1076a35eefeeb9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lllyasviel/FramePack |
| Description | Lets make video diffusion practical! |
| Stars | 17356 |
| Forks | 1750 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `97fe5dbe06ac1f337ece08935b1076a35eefeeb9` |
| Retrieved at | 2026-11-14T19:08:33.978752+00:00 |
| Files in this snapshot | 19 |

## Directory tree

```text
diffusers_helper/  (13 files)
  gradio/  (1 files)
    progress_bar.py
  k_diffusion/  (2 files)
    uni_pc_fm.py
    wrapper.py
  models/  (1 files)
    hunyuan_video_packed.py
  pipelines/  (1 files)
    k_diffusion_hunyuan.py
  bucket_tools.py
  clip_vision.py
  dit_common.py
  hf_login.py
  hunyuan.py
  memory.py
  thread_utils.py
  utils.py
.gitignore
LICENSE
README.md
demo_gradio.py
demo_gradio_f1.py
requirements.txt
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: end_process, process, worker. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AdaLayerNormContinuous, AdaLayerNormZero, AdaLayerNormZeroSingle, ClipVisionProjection, CombinedTimeste… |
| diffusers_helper package | library | Observed | Groups 12 file(s) under diffusers_helper package (observed from repository paths and static analysis). Observed top-level classes: AsyncStream, DynamicSwapInstaller, FIFOQueue, FlowMatchUniPC, Listener. Observed top-lev… |

## Important files

- `requirements.txt` (manifest)

## Top-level layout

- `diffusers_helper` — 13 analysed file(s)
- `(root files)` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `97fe5dbe06ac1f337ece08935b1076a35eefeeb9` is the revision these paths and observations refer to.
