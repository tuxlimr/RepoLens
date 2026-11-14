# Project structure: lucidrains/vit-pytorch

**Analysed commit:** `42298e16ad7915ea6f531049e7909e7ee07bc5fe`

**Commit reference:** [42298e16ad7915ea6f531049e7909e7ee07bc5fe](https://github.com/lucidrains/vit-pytorch/commit/42298e16ad7915ea6f531049e7909e7ee07bc5fe)

**Tree at this commit:** [lucidrains/vit-pytorch@42298e16ad79](https://github.com/lucidrains/vit-pytorch/tree/42298e16ad7915ea6f531049e7909e7ee07bc5fe)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lucidrains/vit-pytorch |
| Description | Implementation of Vision Transformer, a simple way to achieve SOTA in vision classification with only a single transformer encoder, in Pytorch |
| Stars | 25571 |
| Forks | 3495 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `42298e16ad7915ea6f531049e7909e7ee07bc5fe` |
| Retrieved at | 2026-11-14T19:07:30.793629+00:00 |
| Files in this snapshot | 93 |

## Directory tree

```text
tests/  (2 files)
  test_dino_loss.py
  test_vit.py
vit_pytorch/  (85 files)
  __init__.py
  accept_video_wrapper.py
  ats_vit.py
  attn_residual_with_dca_simple_vit.py
  cait.py
  cct.py
  cct_3d.py
  cross_vit.py
  crossformer.py
  cvt.py
  deepvit.py
  dino.py
  distill.py
  efficient.py
  es_vit.py
  extractor.py
  jet_vit.py
  jumbo_vit.py
  learnable_memory_vit.py
  lejepa.py
  levit.py
  levjepa.py
  levjepa_nd.py
  local_vit.py
  … 61 more files
.gitignore
LICENSE
MANIFEST.in
README.md
pyproject.toml
train_vit_decorr.py
```

## Entry points

- [vit_pytorch/accept_video_wrapper.py:184](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/accept_video_wrapper.py#L184)
- [vit_pytorch/attn_residual_with_dca_simple_vit.py:268](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/attn_residual_with_dca_simple_vit.py#L268)
- [vit_pytorch/jumbo_vit.py:187](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/jumbo_vit.py#L187)
- [vit_pytorch/lejepa.py:346](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/lejepa.py#L346)
- [vit_pytorch/levjepa.py:449](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/levjepa.py#L449)
- [vit_pytorch/levjepa_nd.py:432](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/levjepa_nd.py#L432)
- [vit_pytorch/look_vit.py:259](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/look_vit.py#L259)
- [vit_pytorch/looped_vit.py:405](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/looped_vit.py#L405)
- [vit_pytorch/na_vit_nested_tensor.py:305](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/na_vit_nested_tensor.py#L305)
- [vit_pytorch/na_vit_nested_tensor_3d.py:327](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/na_vit_nested_tensor_3d.py#L327)
- [vit_pytorch/normalized_vit.py:250](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/normalized_vit.py#L250)
- [vit_pytorch/simple_uvit.py:161](https://github.com/lucidrains/vit-pytorch/blob/42298e16ad7915ea6f531049e7909e7ee07bc5fe/vit_pytorch/simple_uvit.py#L161)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: exists. |
| Application entry point | entrypoint | Observed | Groups 34 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AST, AcceptVideoWrapper, AdaptiveLoopGate, Attention, AttentionResidual, AutoencodingHead… |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: test_loss_and_gradient_stay_finite_for_low_precision_logits, test_loss_gradient_matches_log_softmax_refere… |
| vit_pytorch package | library | Observed | Groups 51 file(s) under vit_pytorch package (observed from repository paths and static analysis). Observed top-level classes: Adapter, AdaptiveTokenSampling, Attend, Attention, AxialRotaryEmbedding, CCT. Observed top-le… |

## Important files

- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `vit_pytorch` — 85 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `tests` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `42298e16ad7915ea6f531049e7909e7ee07bc5fe` is the revision these paths and observations refer to.
