# Project structure: xmu-xiaoma666/External-Attention-pytorch

**Analysed commit:** `c413dae1f053ac2bbff9e2d668e1d7a62f07c335`

**Commit reference:** [c413dae1f053ac2bbff9e2d668e1d7a62f07c335](https://github.com/xmu-xiaoma666/External-Attention-pytorch/commit/c413dae1f053ac2bbff9e2d668e1d7a62f07c335)

**Tree at this commit:** [xmu-xiaoma666/External-Attention-pytorch@c413dae1f053](https://github.com/xmu-xiaoma666/External-Attention-pytorch/tree/c413dae1f053ac2bbff9e2d668e1d7a62f07c335)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xmu-xiaoma666/External-Attention-pytorch |
| Description | 🍀 Pytorch implementation of various Attention Mechanisms, MLP, Re-parameter, Convolution, which is helpful to further understand papers.⭐⭐⭐ |
| Stars | 12184 |
| Forks | 1932 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `c413dae1f053ac2bbff9e2d668e1d7a62f07c335` |
| Retrieved at | 2026-11-14T19:10:13.985372+00:00 |
| Files in this snapshot | 106 |

## Directory tree

```text
model/  (100 files)
  .vscode/  (1 files)
    settings.json
  analysis/  (3 files)
    Attention.md
    注意力机制.md
    重参数机制.md
  attention/  (38 files)
    A2Atttention.py
    ACmixAttention.py
    AFT.py
    Axial_attention.py
    BAM.py
    CBAM.py
    CoAtNet.py
    CoTAttention.py
    CoordAttention.py
    CrissCrossAttention.py
    Crossformer.py
    DANet.py
    DAT.py
    ECAAttention.py
    EMSA.py
    ExternalAttention.py
    HaloAttention.py
    MOATransformer.py
    MUSEAttention.py
    MobileViTAttention.py
    MobileViTv2Attention.py
    OutlookAttention.py
    PSA.py
    ParNetAttention.py
    … 14 more files
  backbone/  (29 files)
    CMT.py
    CPVT.py
    CaiT.py
    CeiT.py
    CoaT.py
    ConTNet.py
    ConViT.py
    Container.py
    ConvMixer.py
    CrossViT.py
    DViT.py
    DeiT.py
    EfficientFormer.py
    HATNet.py
    LeViT.py
    MobileNetV3.py
    MobileViT.py
    PIT.py
    PVT.py
    PatchConvnet.py
    ShuffleTransformer.py
    TnT.py
    VOLO.py
    convnextv2.py
    … 5 more files
  conv/  (6 files)
    CondConv.py
    DepthwiseSeparableConvolution.py
    DynamicConv.py
    HorNet.py
    Involution.py
    MBConv.py
  fighingcv.egg-info/  (6 files)
    PKG-INFO
    SOURCES.txt
    dependency_links.txt
    entry_points.txt
    requires.txt
    top_level.txt
  huggingface_hub.egg-info/  (6 files)
    PKG-INFO
    SOURCES.txt
    dependency_links.txt
    entry_points.txt
    requires.txt
    top_level.txt
  mlp/  (6 files)
    g_mlp.py
    mlp_mixer.py
    repmlp.py
    resmlp.py
    sMLP_block.py
    vip-mlp.py
  rep/  (4 files)
    acnet.py
    ddb.py
    mobileone.py
    repvgg.py
  __init__.py
LICENSE
README.md
README_EN.md
README_pip.md
main.py
setup.py
```

## Entry points

- [main.py:6](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/main.py#L6)
- [model/__init__.py:5](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/__init__.py#L5)
- [model/attention/A2Atttention.py:59](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/attention/A2Atttention.py#L59)
- [model/attention/ACmixAttention.py:102](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/attention/ACmixAttention.py#L102)
- [model/attention/AFT.py:58](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/attention/AFT.py#L58)
- [model/attention/Axial_attention.py:356](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/attention/Axial_attention.py#L356)
- [model/attention/BAM.py:87](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/attention/BAM.py#L87)
- [model/attention/CBAM.py:74](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/attention/CBAM.py#L74)
- [model/attention/CoAtNet.py:79](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/attention/CoAtNet.py#L79)
- [model/attention/CoTAttention.py:53](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/attention/CoTAttention.py#L53)
- [model/attention/CrissCrossAttention.py:51](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/attention/CrissCrossAttention.py#L51)
- [model/attention/Crossformer.py:610](https://github.com/xmu-xiaoma666/External-Attention-pytorch/blob/c413dae1f053ac2bbff9e2d668e1d7a62f07c335/model/attention/Crossformer.py#L610)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 79 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ACNet, ACmix, AFT_FULL, ALTGVT, Affine, Attention. Observed top-level functions: B120, B6… |
| model package | library | Observed | Groups 6 file(s) under model package (observed from repository paths and static analysis). Observed top-level classes: BasicLayer, CoordAtt, MobileNetV3, MobileNetV3Features, PatchEmbed, PatchMerging. Observed top-level… |

## Important files

- `model/.vscode/settings.json` (config)
- `setup.py` (manifest)

## Top-level layout

- `model` — 100 analysed file(s)
- `(root files)` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c413dae1f053ac2bbff9e2d668e1d7a62f07c335` is the revision these paths and observations refer to.
