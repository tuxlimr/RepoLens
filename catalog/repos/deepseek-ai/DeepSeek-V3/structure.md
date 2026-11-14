# Project structure: deepseek-ai/DeepSeek-V3

**Analysed commit:** `9b4e9788e4a3a731f7567338ed15d3ec549ce03b`

**Commit reference:** [9b4e9788e4a3a731f7567338ed15d3ec549ce03b](https://github.com/deepseek-ai/DeepSeek-V3/commit/9b4e9788e4a3a731f7567338ed15d3ec549ce03b)

**Tree at this commit:** [deepseek-ai/DeepSeek-V3@9b4e9788e4a3](https://github.com/deepseek-ai/DeepSeek-V3/tree/9b4e9788e4a3a731f7567338ed15d3ec549ce03b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | deepseek-ai/DeepSeek-V3 |
| Description | Not provided |
| Stars | 104827 |
| Forks | 16746 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `9b4e9788e4a3a731f7567338ed15d3ec549ce03b` |
| Retrieved at | 2026-11-14T19:06:07.543721+00:00 |
| Files in this snapshot | 18 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    stale.yml
inference/  (10 files)
  configs/  (4 files)
    config_16B.json
    config_236B.json
    config_671B.json
    config_v3.1.json
  convert.py
  fp8_cast_bf16.py
  generate.py
  kernel.py
  model.py
  requirements.txt
.gitignore
LICENSE-CODE
LICENSE-MODEL
README.md
README_WEIGHTS.md
```

## Entry points

- [inference/convert.py:88](https://github.com/deepseek-ai/DeepSeek-V3/blob/9b4e9788e4a3a731f7567338ed15d3ec549ce03b/inference/convert.py#L88)
- [inference/fp8_cast_bf16.py:106](https://github.com/deepseek-ai/DeepSeek-V3/blob/9b4e9788e4a3a731f7567338ed15d3ec549ce03b/inference/fp8_cast_bf16.py#L106)
- [inference/generate.py:161](https://github.com/deepseek-ai/DeepSeek-V3/blob/9b4e9788e4a3a731f7567338ed15d3ec549ce03b/inference/generate.py#L161)
- [inference/model.py:801](https://github.com/deepseek-ai/DeepSeek-V3/blob/9b4e9788e4a3a731f7567338ed15d3ec549ce03b/inference/model.py#L801)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Block, ColumnParallelLinear, Expert, Gate, Linear, MLA. Observed top-level functions: appl… |
| inference package | library | Observed | Groups 1 file(s) under inference package (observed from repository paths and static analysis). Observed top-level functions: act_quant, act_quant_kernel, fp8_gemm, fp8_gemm_kernel, weight_dequant, weight_dequant_kernel. |

## Important files

- `.github/workflows/stale.yml` (ci)
- `inference/configs/config_16B.json` (config)
- `inference/configs/config_236B.json` (config)
- `inference/configs/config_671B.json` (config)
- `inference/configs/config_v3.1.json` (config)
- `inference/requirements.txt` (manifest)

## Top-level layout

- `inference` — 10 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9b4e9788e4a3a731f7567338ed15d3ec549ce03b` is the revision these paths and observations refer to.
