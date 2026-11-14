# Project structure: huggingface/pytorch-image-models

**Analysed commit:** `43b549bfe9d680bc94284cfd0b611152d18e97d7`

**Commit reference:** [43b549bfe9d680bc94284cfd0b611152d18e97d7](https://github.com/huggingface/pytorch-image-models/commit/43b549bfe9d680bc94284cfd0b611152d18e97d7)

**Tree at this commit:** [huggingface/pytorch-image-models@43b549bfe9d6](https://github.com/huggingface/pytorch-image-models/tree/43b549bfe9d680bc94284cfd0b611152d18e97d7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | huggingface/pytorch-image-models |
| Description | The largest collection of PyTorch image encoders / backbones. Including train, eval, inference, export scripts, and pretrained weights -- ResNet, ResNeXT, EfficientNet, NFNet, Vision Transformer (ViT), MobileNetV4, MobileNet-V3 & V2, RegNet, DPN, CSPNet, Swin Transformer, MaxViT, CoAtNet, ConvNeXt,… |
| Stars | 37284 |
| Forks | 5229 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `43b549bfe9d680bc94284cfd0b611152d18e97d7` |
| Retrieved at | 2026-11-14T19:06:50.733790+00:00 |
| Files in this snapshot | 413 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (5 files)
    build_documentation.yml
    build_pr_documentation.yml
    tests.yml
    trufflehog.yml
    upload_pr_documentation.yml
  FUNDING.yml
  dependabot.yml
  pull_request_template.md
convert/  (4 files)
  convert_from_mxnet.py
  convert_gemma4_vit.py
  convert_lcnetv2_paddle.py
  convert_nest_flax.py
hfdocs/  (119 files)
  source/  (117 files)
    models/  (98 files)
      … 98 files under this directory
    reference/  (5 files)
      … 5 files under this directory
    _redirects.yml
    _toctree.yml
    changes.mdx
    feature_extraction.mdx
    hf_hub.mdx
    hparams.mdx
    index.mdx
    installation.mdx
    model_adaptation.mdx
    model_api.mdx
    models.mdx
    quickstart.mdx
    results.mdx
    training_script.mdx
  README.md
  generate_model_docs.py
results/  (33 files)
  README.md
  benchmark-infer-amp-nchw-pt113-cu117-rtx3090.csv
  benchmark-infer-amp-nchw-pt210-cu121-rtx3090.csv
  benchmark-infer-amp-nchw-pt240-cu124-rtx3090.csv
  benchmark-infer-amp-nchw-pt240-cu124-rtx4090-dynamo.csv
  benchmark-infer-amp-nchw-pt240-cu124-rtx4090.csv
  benchmark-infer-amp-nchw-pt291-cu128-4090-dynamo.csv
  benchmark-infer-amp-nchw-pt291-cu128-4090.csv
  benchmark-infer-amp-nchw-pt291-cu130-5090-dynamo.csv
  benchmark-infer-amp-nchw-pt291-cu130-5090.csv
  benchmark-infer-amp-nchw-pt291-cu130-pro6000maxq-dynamo.csv
  benchmark-infer-amp-nchw-pt291-cu130-pro6000maxq.csv
  benchmark-infer-amp-nhwc-pt113-cu117-rtx3090.csv
  benchmark-infer-amp-nhwc-pt210-cu121-rtx3090.csv
  benchmark-infer-amp-nhwc-pt240-cu124-rtx3090.csv
  benchmark-infer-amp-nhwc-pt240-cu124-rtx4090.csv
  benchmark-infer-amp_bf16-nchw-pt291-cu130-pro6000maxq-dynamo.csv
  benchmark-infer-bf16-nchw-pt291-cu130-pro6000maxq-dynamo.csv
  benchmark-infer-fp32-nchw-pt221-cpu-i9_10940x-dynamo.csv
  benchmark-infer-fp32-nchw-pt240-cpu-i7_12700h-dynamo.csv
  benchmark-infer-fp32-nchw-pt240-cpu-i9_10940x-dynamo.csv
  benchmark-train-amp-nchw-pt112-cu113-rtx3090.csv
  benchmark-train-amp-nhwc-pt112-cu113-rtx3090.csv
  generate_csv_results.py
  … 9 more files
tests/  (27 files)
  __init__.py
  conftest.py
  test_checkpoint_loading.py
  test_checkpoint_saver.py
  test_data.py
  test_dataset_info.py
  test_factory.py
  test_hub.py
  test_input_conv.py
  test_layers.py
  test_layers_drop.py
  test_layers_pool.py
  test_layers_pos_embed.py
  test_model_input.py
  test_models.py
  test_multilabel.py
  test_naflex_dataset.py
  test_optim.py
  test_prune.py
  test_reader_wds.py
  test_scheduled_sampler.py
  test_scheduler.py
  test_sweep.py
  test_sweep_fuzz.py
  … 3 more files
timm/  (191 files)
  data/  (54 files)
    _info/  (15 files)
      … 15 files under this directory
    readers/  (15 files)
      … 15 files under this directory
    __init__.py
    auto_augment.py
    config.py
    constants.py
    dataset.py
    dataset_factory.py
    dataset_info.py
    distributed_sampler.py
    imagenet_info.py
    loader.py
    mixup.py
    model_config.py
    naflex_dataset.py
    naflex_loader.py
    naflex_mixup.py
    naflex_random_erasing.py
    naflex_transforms.py
    random_erasing.py
    real_labels.py
    scheduled_sampler.py
    target_transforms.py
    tf_preprocessing.py
    transforms.py
    transforms_factory.py
  layers/  (69 files)
    __init__.py
    _fx.py
    activations.py
    activations_me.py
    adaptive_avgmax_pool.py
    attention.py
    attention2d.py
    attention_pool.py
    attention_pool2d.py
    blur_pool.py
    bottleneck_attn.py
    cbam.py
    classifier.py
    cond_conv2d.py
    config.py
    conv2d_same.py
    conv_bn_act.py
    coord_attn.py
    create_act.py
    create_attn.py
    create_conv2d.py
    create_norm.py
    create_norm_act.py
    diff_attention.py
    … 45 more files
  loss/  (11 files)
    __init__.py
    _loss_factory.py
    asymmetric_loss.py
    binary_cross_entropy.py
    class_weights.py
    cross_entropy.py
    distribution_balanced_loss.py
    jsd.py
    poly_loss.py
    two_way_loss.py
    zlpr_loss.py
  models/  (52 files)
    _pruned/  (5 files)
      … 5 files under this directory
    layers/  (1 files)
      … 1 files under this directory
    __init__.py
    _builder.py
    _efficientnet_blocks.py
    _efficientnet_builder.py
    _factory.py
    _features.py
    _features_fx.py
    _helpers.py
    _hub.py
    _input.py
    _manipulate.py
    _pretrained.py
    _prune.py
    _registry.py
    beit.py
    byoanet.py
    byobnet.py
    cait.py
    coat.py
    convit.py
    convmixer.py
    convnext.py
    cpubone.py
    crossvit.py
    … 22 more files
  optim/  (2 files)
    __init__.py
    optim_factory.py
  __init__.py
  py.typed
  version.py
.gitattributes
.gitignore
AGENTS.md
CITATION.cff
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
UPGRADING.md
avg_checkpoints.py
benchmark.py
bulk_runner.py
class_weights.py
clean_checkpoint.py
distributed_train.sh
hubconf.py
inference.py
legacy_distributed_train.sh
legacy_train.py
onnx_export.py
onnx_validate.py
pyproject.toml
… 4 more files
```

## Entry points

- [avg_checkpoints.py:152](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/avg_checkpoints.py#L152)
- [benchmark.py:700](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/benchmark.py#L700)
- [bulk_runner.py:243](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/bulk_runner.py#L243)
- [class_weights.py:183](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/class_weights.py#L183)
- [clean_checkpoint.py:114](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/clean_checkpoint.py#L114)
- [convert/convert_from_mxnet.py:106](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/convert/convert_from_mxnet.py#L106)
- [convert/convert_gemma4_vit.py:223](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/convert/convert_gemma4_vit.py#L223)
- [convert/convert_lcnetv2_paddle.py:79](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/convert/convert_lcnetv2_paddle.py#L79)
- [convert/convert_nest_flax.py:106](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/convert/convert_nest_flax.py#L106)
- [hfdocs/generate_model_docs.py:1969](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/hfdocs/generate_model_docs.py#L1969)
- [inference.py:415](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/inference.py#L415)
- [legacy_train.py:1365](https://github.com/huggingface/pytorch-image-models/blob/43b549bfe9d680bc94284cfd0b611152d18e97d7/legacy_train.py#L1365)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: set_exportable, set_layer_config, set_no_jit, set_scriptable. Observed top-level func… |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 86 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Attention, Attention2d, Attention2dDownsample, AugMixAugment, AugMixDataset, AugmentOp. Observed top-l… |
| Application entry point | entrypoint | Observed | Groups 15 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ArchInfo, BenchmarkRunner, Executor, FamilyData, InferenceBenchmarkRunner, JobState. Obse… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| results package | library | Observed | Groups 1 file(s) under results package (observed from repository paths and static analysis). Observed top-level functions: diff. |
| Tests | test | Observed | Groups 28 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Died, FakeProc, MLP, ModuleWrapper, Rank, Sim. Observed top-level functions: _adahessian_steps, _add_member… |
| timm package | library | Observed | Groups 82 file(s) under timm package (observed from repository paths and static analysis). Observed top-level classes: AdaptiveAvgMaxPool2d, AdaptiveCatAvgMaxPool2d, AsymmetricLossMultiLabel, AsymmetricLossSingleLabel,… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build_documentation.yml` (ci)
- `.github/workflows/build_pr_documentation.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/trufflehog.yml` (ci)
- `.github/workflows/upload_pr_documentation.yml` (ci)
- `MANIFEST.in` (manifest)
- `hfdocs/source/_redirects.yml` (config)
- `hfdocs/source/_toctree.yml` (config)
- `pyproject.toml` (manifest)
- `requirements-dev.txt` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)

## Top-level layout

- `timm` — 191 analysed file(s)
- `hfdocs` — 119 analysed file(s)
- `results` — 33 analysed file(s)
- `(root files)` — 28 analysed file(s)
- `tests` — 27 analysed file(s)
- `.github` — 11 analysed file(s)
- `convert` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `43b549bfe9d680bc94284cfd0b611152d18e97d7` is the revision these paths and observations refer to.
