# Project structure: apple-aiml-research/ml-stable-diffusion

**Analysed commit:** `ea2805dc1945be20561c77e5f6d1d9a5a637cda2`

**Commit reference:** [ea2805dc1945be20561c77e5f6d1d9a5a637cda2](https://github.com/apple-aiml-research/ml-stable-diffusion/commit/ea2805dc1945be20561c77e5f6d1d9a5a637cda2)

**Tree at this commit:** [apple-aiml-research/ml-stable-diffusion@ea2805dc1945](https://github.com/apple-aiml-research/ml-stable-diffusion/tree/ea2805dc1945be20561c77e5f6d1d9a5a637cda2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | apple-aiml-research/ml-stable-diffusion |
| Description | Stable Diffusion with Core ML on Apple Silicon |
| Stars | 17958 |
| Forks | 1076 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `ea2805dc1945be20561c77e5f6d1d9a5a637cda2` |
| Retrieved at | 2026-11-14T19:08:27.755409+00:00 |
| Files in this snapshot | 56 |

## Directory tree

```text
python_coreml_stable_diffusion/  (14 files)
  __init__.py
  _version.py
  activation_quantization.py
  attention.py
  chunk_mlprogram.py
  controlnet.py
  coreml_model.py
  layer_norm.py
  mixed_bit_compression_apply.py
  mixed_bit_compression_pre_analysis.py
  multilingual_projection.py
  pipeline.py
  torch2coreml.py
  unet.py
swift/  (33 files)
  StableDiffusion/  (31 files)
    pipeline/  (28 files)
      … 28 files under this directory
    tokenizer/  (3 files)
      … 3 files under this directory
  StableDiffusionCLI/  (1 files)
    main.swift
  StableDiffusionTests/  (1 files)
    StableDiffusionTests.swift
tests/  (2 files)
  __init__.py
  test_stable_diffusion.py
.gitignore
ACKNOWLEDGEMENTS
LICENSE.md
Package.swift
README.md
requirements.txt
setup.py
```

## Entry points

- [python_coreml_stable_diffusion/activation_quantization.py:451](https://github.com/apple-aiml-research/ml-stable-diffusion/blob/ea2805dc1945be20561c77e5f6d1d9a5a637cda2/python_coreml_stable_diffusion/activation_quantization.py#L451)
- [python_coreml_stable_diffusion/chunk_mlprogram.py:375](https://github.com/apple-aiml-research/ml-stable-diffusion/blob/ea2805dc1945be20561c77e5f6d1d9a5a637cda2/python_coreml_stable_diffusion/chunk_mlprogram.py#L375)
- [python_coreml_stable_diffusion/mixed_bit_compression_apply.py:90](https://github.com/apple-aiml-research/ml-stable-diffusion/blob/ea2805dc1945be20561c77e5f6d1d9a5a637cda2/python_coreml_stable_diffusion/mixed_bit_compression_apply.py#L90)
- [python_coreml_stable_diffusion/mixed_bit_compression_pre_analysis.py:545](https://github.com/apple-aiml-research/ml-stable-diffusion/blob/ea2805dc1945be20561c77e5f6d1d9a5a637cda2/python_coreml_stable_diffusion/mixed_bit_compression_pre_analysis.py#L545)
- [python_coreml_stable_diffusion/multilingual_projection.py:48](https://github.com/apple-aiml-research/ml-stable-diffusion/blob/ea2805dc1945be20561c77e5f6d1d9a5a637cda2/python_coreml_stable_diffusion/multilingual_projection.py#L48)
- [python_coreml_stable_diffusion/pipeline.py:785](https://github.com/apple-aiml-research/ml-stable-diffusion/blob/ea2805dc1945be20561c77e5f6d1d9a5a637cda2/python_coreml_stable_diffusion/pipeline.py#L785)
- [python_coreml_stable_diffusion/torch2coreml.py:1783](https://github.com/apple-aiml-research/ml-stable-diffusion/blob/ea2805dc1945be20561c77e5f6d1d9a5a637cda2/python_coreml_stable_diffusion/torch2coreml.py#L1783)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CoreMLStableDiffusionPipeline. Observed top-level functions: _add_fp32_casts, _compile_cor… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| python_coreml_stable_diffusion package | library | Observed | Groups 7 file(s) under python_coreml_stable_diffusion package (observed from repository paths and static analysis). Observed top-level classes: AttentionImplementations, BasicTransformerBlock, ControlNetConditioningEmbe… |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestStableDiffusionForTextToImage. Observed top-level functions: _extend_parser, _get_test_artifacts_dir, _r… |

## Important files

- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `swift` — 33 analysed file(s)
- `python_coreml_stable_diffusion` — 14 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `tests` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ea2805dc1945be20561c77e5f6d1d9a5a637cda2` is the revision these paths and observations refer to.
