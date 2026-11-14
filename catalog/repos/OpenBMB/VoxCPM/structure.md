# Project structure: OpenBMB/VoxCPM

**Analysed commit:** `300e4260b509066151d623dc9c0aa922cf82232b`

**Commit reference:** [300e4260b509066151d623dc9c0aa922cf82232b](https://github.com/OpenBMB/VoxCPM/commit/300e4260b509066151d623dc9c0aa922cf82232b)

**Tree at this commit:** [OpenBMB/VoxCPM@300e4260b509](https://github.com/OpenBMB/VoxCPM/tree/300e4260b509066151d623dc9c0aa922cf82232b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | OpenBMB/VoxCPM |
| Description | VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning |
| Stars | 42480 |
| Forks | 4853 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `300e4260b509066151d623dc9c0aa922cf82232b` |
| Retrieved at | 2026-11-14T19:06:39.598286+00:00 |
| Files in this snapshot | 71 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    publish-to-pypi.yml
conf/  (6 files)
  voxcpm_v1/  (2 files)
    voxcpm_finetune_all.yaml
    voxcpm_finetune_lora.yaml
  voxcpm_v1.5/  (2 files)
    voxcpm_finetune_all.yaml
    voxcpm_finetune_lora.yaml
  voxcpm_v2/  (2 files)
    voxcpm_finetune_all.yaml
    voxcpm_finetune_lora.yaml
docker/  (4 files)
  Dockerfile
  README.md
  docker-compose.yml
  nginx.conf
examples/  (1 files)
  train_data_example.jsonl
scripts/  (4 files)
  test_pick_runtime_dtype.py
  test_voxcpm_ft_infer.py
  test_voxcpm_lora_infer.py
  train_voxcpm_finetune.py
src/  (38 files)
  voxcpm/  (38 files)
    model/  (4 files)
      … 4 files under this directory
    modules/  (17 files)
      … 17 files under this directory
    timestamps/  (4 files)
      … 4 files under this directory
    training/  (8 files)
      … 8 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    __init__.py
    cli.py
    core.py
    zipenhancer.py
tests/  (7 files)
  test_cli.py
  test_lora_checkpoint_loading.py
  test_model_utils.py
  test_timestamps.py
  test_torch_load_safety.py
  test_training_data.py
  test_validate.py
.dockerignore
.gitignore
LICENSE
README.md
README_zh.md
app.py
app_old.py
i18n.py
lora_ft_webui.py
pyproject.toml
```

## Entry points

- [src/voxcpm/cli.py](https://github.com/OpenBMB/VoxCPM/blob/300e4260b509066151d623dc9c0aa922cf82232b/src/voxcpm/cli.py)
- [app.py:576](https://github.com/OpenBMB/VoxCPM/blob/300e4260b509066151d623dc9c0aa922cf82232b/app.py#L576)
- [app_old.py:291](https://github.com/OpenBMB/VoxCPM/blob/300e4260b509066151d623dc9c0aa922cf82232b/app_old.py#L291)
- [lora_ft_webui.py:1271](https://github.com/OpenBMB/VoxCPM/blob/300e4260b509066151d623dc9c0aa922cf82232b/lora_ft_webui.py#L1271)
- [scripts/train_voxcpm_finetune.py:855](https://github.com/OpenBMB/VoxCPM/blob/300e4260b509066151d623dc9c0aa922cf82232b/scripts/train_voxcpm_finetune.py#L855)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: MiniCPM4Config, RopeScalingConfig. Observed top-level functions: load_yaml_config, p… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: t. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: MiniCPMAttention, MiniCPMDecoderLayer, MiniCPMLongRoPE, MiniCPMMLP, MiniCPMModel, MiniCPMRMSNorm. Obser… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: VoxCPMDemo. Observed top-level functions: _add_common_generation_args, _add_lora_args, _ad… |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: DummyModel, DummyTTSModel, StubVoxCPM, TestValidateManifest. Observed top-level functions: _create_wav, _ha… |
| voxcpm package | library | Observed | Groups 34 file(s) under voxcpm package (observed from repository paths and static analysis). Observed top-level classes: Accelerator, AudioFeatureProcessingPacker, AudioVAE, AudioVAEConfig, BatchProcessor, CausalConv1d.… |

## Important files

- `.dockerignore` (container)
- `.github/workflows/publish-to-pypi.yml` (ci)
- `conf/voxcpm_v1.5/voxcpm_finetune_all.yaml` (config)
- `conf/voxcpm_v1.5/voxcpm_finetune_lora.yaml` (config)
- `conf/voxcpm_v1/voxcpm_finetune_all.yaml` (config)
- `conf/voxcpm_v1/voxcpm_finetune_lora.yaml` (config)
- `conf/voxcpm_v2/voxcpm_finetune_all.yaml` (config)
- `conf/voxcpm_v2/voxcpm_finetune_lora.yaml` (config)
- `docker/Dockerfile` (container)
- `docker/docker-compose.yml` (container)
- `pyproject.toml` (manifest)

## Top-level layout

- `src` — 38 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `tests` — 7 analysed file(s)
- `conf` — 6 analysed file(s)
- `docker` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.github` — 1 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `300e4260b509066151d623dc9c0aa922cf82232b` is the revision these paths and observations refer to.
