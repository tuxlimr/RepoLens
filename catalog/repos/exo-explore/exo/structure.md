# Project structure: exo-explore/exo

**Analysed commit:** `a60b95698ca81737d367443674dd5563cbc9559b`

**Commit reference:** [a60b95698ca81737d367443674dd5563cbc9559b](https://github.com/exo-explore/exo/commit/a60b95698ca81737d367443674dd5563cbc9559b)

**Tree at this commit:** [exo-explore/exo@a60b95698ca8](https://github.com/exo-explore/exo/tree/a60b95698ca81737d367443674dd5563cbc9559b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | exo-explore/exo |
| Description | Run frontier AI locally. |
| Stars | 48406 |
| Forks | 3616 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `a60b95698ca81737d367443674dd5563cbc9559b` |
| Retrieved at | 2026-11-14T19:06:33.220273+00:00 |
| Files in this snapshot | 787 |

## Directory tree

```text
.githooks/  (4 files)
  post-checkout
  post-commit
  post-merge
  pre-push
.github/  (15 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  actions/  (8 files)
    conditional-commit/  (1 files)
      … 1 files under this directory
    format/  (1 files)
      … 1 files under this directory
    lint/  (1 files)
      … 1 files under this directory
    lint-check/  (1 files)
      … 1 files under this directory
    regenerate-protobufs/  (1 files)
      … 1 files under this directory
    setup-python-uv/  (1 files)
      … 1 files under this directory
    unit-test/  (1 files)
      … 1 files under this directory
    verify-clean/  (1 files)
      … 1 files under this directory
  workflows/  (3 files)
    build-app.yml
    cluster-nightly.yml
    pipeline.yml
  CODEOWNERS
  pull_request_template.md
.typings/  (293 files)
  mflux/  (221 files)
    callbacks/  (4 files)
      … 4 files under this directory
    cli/  (2 files)
      … 2 files under this directory
    models/  (206 files)
      … 206 files under this directory
    release/  (1 files)
      … 1 files under this directory
    utils/  (7 files)
      … 7 files under this directory
    __init__.pyi
  mlx/  (28 files)
    core/  (6 files)
      … 6 files under this directory
    nn/  (21 files)
      … 21 files under this directory
    utils.pyi
  mlx_lm/  (38 files)
    kernels/  (1 files)
      … 1 files under this directory
    models/  (27 files)
      … 27 files under this directory
    tuner/  (3 files)
      … 3 files under this directory
    __init__.pyi
    _version.pyi
    convert.pyi
    generate.pyi
    sample_utils.pyi
    tokenizer_utils.pyi
    utils.pyi
  mlx_vlm/  (3 files)
    __init__.pyi
    prompt_utils.pyi
    utils.pyi
  pynvml/  (1 files)
    __init__.pyi
  safetensors/  (1 files)
    __init__.pyi
  .gitkeep
.vscode/  (2 files)
  extensions.json
  settings.json
.zed/  (1 files)
  settings.json
app/  (85 files)
  EXO/  (85 files)
    EXO/  (61 files)
      … 61 files under this directory
    EXO.xcodeproj/  (5 files)
      … 5 files under this directory
    EXOTests/  (16 files)
      … 16 files under this directory
    EXOUITests/  (2 files)
      … 2 files under this directory
    uninstall-exo.sh
bench/  (12 files)
  eval_configs/  (1 files)
    models.toml
  METHODOLOGY.md
  bench.toml
  eval_tool_calls.py
  exo_bench.py
  exo_eval.py
  parallel_requests.py
  prefill-decode.toml
  prefill_decode_bench.py
  pyproject.toml
  scenarios.toml
  single-m3-ultra.toml
dashboard/  (73 files)
  src/  (53 files)
    lib/  (44 files)
      … 44 files under this directory
    routes/  (6 files)
      … 6 files under this directory
    app.css
    app.d.ts
    app.html
  tests/  (14 files)
    api_errors.test.ts
    conversation_sync.test.ts
    deployments.test.ts
    disk_fit.test.ts
    download_activity.test.ts
    download_progress.test.ts
    download_total_review.test.ts
    downloads.test.ts
    downloads_catalogue.test.ts
    instance_health.test.ts
    model_download_index.test.ts
    other_versions.test.ts
    rdma.test.ts
    stream_errors.test.ts
  dashboard.nix
  package.json
  parts.nix
  svelte.config.js
  tsconfig.json
  vite.config.ts
docs/  (1 files)
  api.md
nix/  (4 files)
  apple-sdk/  (1 files)
    metadata/  (1 files)
      … 1 files under this directory
  apple-sdk-overlay.nix
  darwin-build-fixes.patch
  metal-toolchain.nix
packaging/  (3 files)
  dmg/  (2 files)
    create-dmg.sh
    generate-background.py
  pyinstaller/  (1 files)
    exo.spec
python/  (1 files)
  parts.nix
resources/  (176 files)
  image_model_cards/  (18 files)
    exolabs--FLUX.1-Kontext-dev-4bit.toml
    exolabs--FLUX.1-Kontext-dev-8bit.toml
    exolabs--FLUX.1-Kontext-dev.toml
    exolabs--FLUX.1-Krea-dev-4bit.toml
    exolabs--FLUX.1-Krea-dev-8bit.toml
    exolabs--FLUX.1-Krea-dev.toml
    exolabs--FLUX.1-dev-4bit.toml
    exolabs--FLUX.1-dev-8bit.toml
    exolabs--FLUX.1-dev.toml
    exolabs--FLUX.1-schnell-4bit.toml
    exolabs--FLUX.1-schnell-8bit.toml
    exolabs--FLUX.1-schnell.toml
    exolabs--Qwen-Image-4bit.toml
    exolabs--Qwen-Image-8bit.toml
    exolabs--Qwen-Image-Edit-2509-4bit.toml
    exolabs--Qwen-Image-Edit-2509-8bit.toml
    exolabs--Qwen-Image-Edit-2509.toml
    exolabs--Qwen-Image.toml
  inference_model_cards/  (158 files)
    deepseek_v3/  (4 files)
      … 4 files under this directory
    deepseek_v4/  (4 files)
      … 4 files under this directory
    deepseek_v41/  (2 files)
      … 2 files under this directory
    flint/  (3 files)
      … 3 files under this directory
    gemma/  (16 files)
      … 16 files under this directory
    glm/  (17 files)
      … 17 files under this directory
    gpt_oss/  (2 files)
      … 2 files under this directory
    hy_v3/  (1 files)
      … 1 files under this directory
    inkling/  (2 files)
      … 2 files under this directory
    kimi/  (6 files)
      … 6 files under this directory
    laguna/  (5 files)
      … 5 files under this directory
    llama/  (16 files)
      … 16 files under this directory
    minimax/  (16 files)
      … 16 files under this directory
    muse_spark/  (2 files)
      … 2 files under this directory
    nemotron_h/  (14 files)
      … 14 files under this directory
    qwen3/  (45 files)
      … 45 files under this directory
    step/  (3 files)
      … 3 files under this directory
rust/  (23 files)
  exo_rs/  (12 files)
    src/  (6 files)
      … 6 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    Cargo.toml
    README.md
    exo_rs.pyi
    pyproject.toml
  networking/  (10 files)
    examples/  (4 files)
      … 4 files under this directory
    src/  (5 files)
      … 5 files under this directory
    Cargo.toml
  parts.nix
scripts/  (2 files)
  download_model_to_cluster.py
  fetch_kv_heads.py
src/  (74 files)
  exo/  (74 files)
    api/  (48 files)
      … 48 files under this directory
    download/  (17 files)
      … 17 files under this directory
    master/  (6 files)
      … 6 files under this directory
    __init__.py
    __main__.py
    main.py
.clauderules
.cursorrules
.envrc
.gitignore
.python-version
.swift-format
AGENTS.md
CONTRIBUTING.md
Cargo.toml
LICENSE
PLATFORMS.md
README.md
RULES.md
TODO.md
flake.lock
flake.nix
justfile
pyproject.toml
```

## Entry points

- [src/exo/__main__.py:35](https://github.com/exo-explore/exo/blob/a60b95698ca81737d367443674dd5563cbc9559b/src/exo/__main__.py#L35)
- [src/exo/main.py](https://github.com/exo-explore/exo/blob/a60b95698ca81737d367443674dd5563cbc9559b/src/exo/main.py)
- [bench/eval_tool_calls.py:1152](https://github.com/exo-explore/exo/blob/a60b95698ca81737d367443674dd5563cbc9559b/bench/eval_tool_calls.py#L1152)
- [bench/exo_bench.py:935](https://github.com/exo-explore/exo/blob/a60b95698ca81737d367443674dd5563cbc9559b/bench/exo_bench.py#L935)
- [bench/exo_eval.py:1751](https://github.com/exo-explore/exo/blob/a60b95698ca81737d367443674dd5563cbc9559b/bench/exo_eval.py#L1751)
- [bench/parallel_requests.py:254](https://github.com/exo-explore/exo/blob/a60b95698ca81737d367443674dd5563cbc9559b/bench/parallel_requests.py#L254)
- [bench/prefill_decode_bench.py:783](https://github.com/exo-explore/exo/blob/a60b95698ca81737d367443674dd5563cbc9559b/bench/prefill_decode_bench.py#L783)
- [packaging/dmg/generate-background.py:87](https://github.com/exo-explore/exo/blob/a60b95698ca81737d367443674dd5563cbc9559b/packaging/dmg/generate-background.py#L87)
- [scripts/download_model_to_cluster.py:211](https://github.com/exo-explore/exo/blob/a60b95698ca81737d367443674dd5563cbc9559b/scripts/download_model_to_cluster.py#L211)
- [scripts/fetch_kv_heads.py:132](https://github.com/exo-explore/exo/blob/a60b95698ca81737d367443674dd5563cbc9559b/scripts/fetch_kv_heads.py#L132)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 26 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: AddCustomModelParams, AdvancedImageParams, ApiPortInUseError, ApplyPatchCallInputItem, ApplyPatchCallOu… |
| app package | library | Observed | Groups 1 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 195 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dashboard package | library | Observed | Groups 47 file(s) under dashboard package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 12 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: API, ApiResult, AppliedClusterCommand, Args, BenchmarkConfig, InstanceFailedError. Observ… |
| exo package | library | Observed | Groups 12 file(s) under exo package (observed from repository paths and static analysis). Observed top-level classes: Decisions, DownloadCoordinator, DownloadSettings, FileProgress, FileState, Hasher. Observed top-level… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| packaging package | library | Observed | Groups 1 file(s) under packaging package (observed from repository paths and static analysis). |
| rust package | library | Observed | Groups 15 file(s) under rust package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 54 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: Blob, Commit, Corrupt, DiskUsage, DownloadNode, Drop. Obse… |

## Important files

- `.github/actions/conditional-commit/action.yml` (config)
- `.github/actions/format/action.yml` (config)
- `.github/actions/lint-check/action.yml` (config)
- `.github/actions/lint/action.yml` (config)
- `.github/actions/regenerate-protobufs/action.yml` (config)
- `.github/actions/setup-python-uv/action.yml` (config)
- `.github/actions/unit-test/action.yml` (config)
- `.github/actions/verify-clean/action.yml` (config)
- `.github/workflows/build-app.yml` (ci)
- `.github/workflows/cluster-nightly.yml` (ci)
- `.github/workflows/pipeline.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `.zed/settings.json` (config)
- `Cargo.toml` (manifest)
- `app/EXO/EXO/Assets.xcassets/AccentColor.colorset/Contents.json` (config)
- `app/EXO/EXO/Assets.xcassets/AppIcon.appiconset/Contents.json` (config)
- `app/EXO/EXO/Assets.xcassets/Contents.json` (config)
- `app/EXO/EXO/Preview Content/Preview Assets.xcassets/Contents.json` (config)
- `app/EXO/EXOTests/Fixtures/state.json` (config)
- `bench/bench.toml` (config)
- `bench/eval_configs/models.toml` (config)
- `bench/prefill-decode.toml` (config)
- `bench/pyproject.toml` (manifest)
- `bench/scenarios.toml` (config)
- `bench/single-m3-ultra.toml` (config)
- `dashboard/package.json` (manifest)
- `dashboard/tsconfig.json` (config)
- `nix/apple-sdk/metadata/versions.json` (config)
- `pyproject.toml` (manifest)
- `resources/image_model_cards/exolabs--FLUX.1-Kontext-dev-4bit.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-Kontext-dev-8bit.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-Kontext-dev.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-Krea-dev-4bit.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-Krea-dev-8bit.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-Krea-dev.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-dev-4bit.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-dev-8bit.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-dev.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-schnell-4bit.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-schnell-8bit.toml` (config)
- `resources/image_model_cards/exolabs--FLUX.1-schnell.toml` (config)
- `resources/image_model_cards/exolabs--Qwen-Image-4bit.toml` (config)
- `resources/image_model_cards/exolabs--Qwen-Image-8bit.toml` (config)
- `resources/image_model_cards/exolabs--Qwen-Image-Edit-2509-4bit.toml` (config)
- `resources/image_model_cards/exolabs--Qwen-Image-Edit-2509-8bit.toml` (config)
- `resources/image_model_cards/exolabs--Qwen-Image-Edit-2509.toml` (config)
- `resources/image_model_cards/exolabs--Qwen-Image.toml` (config)
- `resources/inference_model_cards/deepseek_v3/mlx-community--DeepSeek-V3.1-4bit.toml` (config)
- `resources/inference_model_cards/deepseek_v3/mlx-community--DeepSeek-V3.1-8bit.toml` (config)
- `resources/inference_model_cards/deepseek_v3/mlx-community--DeepSeek-V3.2-4bit.toml` (config)
- `resources/inference_model_cards/deepseek_v3/mlx-community--DeepSeek-V3.2-8bit.toml` (config)
- `resources/inference_model_cards/deepseek_v4/deepseek-ai--DeepSeek-V4-Flash-0731.toml` (config)
- `resources/inference_model_cards/deepseek_v4/deepseek-ai--DeepSeek-V4-Pro-0813.toml` (config)
- `resources/inference_model_cards/deepseek_v4/mlx-community--DeepSeek-V4-Flash.toml` (config)
- `resources/inference_model_cards/deepseek_v4/mlx-community--DeepSeek-V4-Pro.toml` (config)
- `resources/inference_model_cards/deepseek_v41/deepseek-ai--DeepSeek-V4.1-Flash-1017.toml` (config)
- `resources/inference_model_cards/deepseek_v41/deepseek-ai--DeepSeek-V4.1-Flash.toml` (config)
- `resources/inference_model_cards/flint/RecursiveSI--flint-int4.toml` (config)
- `resources/inference_model_cards/flint/RecursiveSI--flint.toml` (config)
- `resources/inference_model_cards/flint/mlx-community--flint-mixed-3-4bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-26b-a4b-it-4bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-26b-a4b-it-6bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-26b-a4b-it-8bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-26b-a4b-it-bf16.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-31b-it-4bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-31b-it-6bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-31b-it-8bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-31b-it-bf16.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-e2b-it-4bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-e2b-it-6bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-e2b-it-8bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-e2b-it-bf16.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-e4b-it-4bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-e4b-it-6bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-e4b-it-8bit.toml` (config)
- `resources/inference_model_cards/gemma/mlx-community--gemma-4-e4b-it-bf16.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-4.5-Air-8bit.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-4.5-Air-bf16.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-4.7-4bit.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-4.7-6bit.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-4.7-8bit.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-4.7-Flash-4bit.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-4.7-Flash-5bit.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-4.7-Flash-6bit.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-4.7-Flash-8bit.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-5-8bit.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-5-MXFP4-Q8.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-5-bf16.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-5.1-DQ4plus-q8.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-5.1-MXFP4-Q8.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-5.1.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-5.3-4bit.toml` (config)
- `resources/inference_model_cards/glm/mlx-community--GLM-5.3-Flash-4bit.toml` (config)
- `resources/inference_model_cards/gpt_oss/mlx-community--gpt-oss-120b-MXFP4-Q8.toml` (config)
- `resources/inference_model_cards/gpt_oss/mlx-community--gpt-oss-20b-MXFP4-Q8.toml` (config)
- `resources/inference_model_cards/hy_v3/XavierLocalAI--Hy3-4bit.toml` (config)
- `resources/inference_model_cards/inkling/mlx-community--Inkling-Small-mlx-4bit.toml` (config)
- `resources/inference_model_cards/inkling/thinkingmachines--Inkling-Small.toml` (config)
- `resources/inference_model_cards/kimi/mlx-community--Kimi-K2-Instruct-4bit.toml` (config)
- `resources/inference_model_cards/kimi/mlx-community--Kimi-K2-Thinking.toml` (config)
- `resources/inference_model_cards/kimi/mlx-community--Kimi-K2.5.toml` (config)
- `resources/inference_model_cards/kimi/mlx-community--Kimi-K2.6-mlx-DQ3_K_M-q8.toml` (config)
- `resources/inference_model_cards/kimi/moonshotai--Kimi-K2.6.toml` (config)
- `resources/inference_model_cards/kimi/moonshotai--Kimi-K2.7-Code.toml` (config)
- `resources/inference_model_cards/laguna/mlx-community--Laguna-S-2.1-oQ4e.toml` (config)
- `resources/inference_model_cards/laguna/mlx-community--Laguna-S-2.1-oQ6e.toml` (config)
- `resources/inference_model_cards/laguna/poolside--Laguna-S-2.1.toml` (config)
- `resources/inference_model_cards/laguna/poolside--Laguna-XS-2.1-NVFP4-mlx.toml` (config)
- `resources/inference_model_cards/laguna/poolside--Laguna-XS-2.1.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.1-Nemotron-70B-Instruct-HF-4bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.1-Nemotron-70B-Instruct-HF-8bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.1-Nemotron-70B-Instruct-HF-bf16.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.1-Nemotron-Nano-4B-v1.1-4bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.1-Nemotron-Nano-4B-v1.1-8bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.1-Nemotron-Nano-4B-v1.1-bf16.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.2-1B-Instruct-4bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.2-3B-Instruct-4bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.2-3B-Instruct-8bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.3-70B-Instruct-4bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Llama-3.3-70B-Instruct-8bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Meta-Llama-3.1-70B-Instruct-4bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Meta-Llama-3.1-8B-Instruct-4bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Meta-Llama-3.1-8B-Instruct-8bit.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--Meta-Llama-3.1-8B-Instruct-bf16.toml` (config)
- `resources/inference_model_cards/llama/mlx-community--llama-3.3-70b-instruct-fp16.toml` (config)
- `resources/inference_model_cards/minimax/MiniMaxAI--MiniMax-M3-MXFP8.toml` (config)
- `resources/inference_model_cards/minimax/MiniMaxAI--MiniMax-M3.1-Flash.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.1-3bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.1-8bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.5-4bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.5-6bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.5-8bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.7-4bit-mxfp4.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.7-4bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.7-5bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.7-6bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.7-8bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M2.7.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M3-4bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M3.1-Flash-Text-3bit.toml` (config)
- `resources/inference_model_cards/minimax/mlx-community--MiniMax-M3.1-Flash-Text-4bit.toml` (config)
- `resources/inference_model_cards/muse_spark/mlx-community--Muse-Spark-Open-816B-A42B-3bit.toml` (config)
- `resources/inference_model_cards/muse_spark/mlx-community--Muse-Spark-Open-816B-A42B-4bit.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-4Bit.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-5Bit.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-6Bit.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-8Bit.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-BF16.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-MXFP4.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-3.5-Lightning-30B-A3B-4bit.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-3.5-Lightning-30B-A3B-8bit.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-3.5-Lightning-30B-A3B-bf16.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-Nano-9B-v2-4bits.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--NVIDIA-Nemotron-Nano-9B-v2-6bit.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--Nemotron-3-Ultra-550B-A55B-4bit.toml` (config)
- `resources/inference_model_cards/nemotron_h/mlx-community--Nemotron-3-Ultra-550B-A55B.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-0.6B-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-0.6B-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-235B-A22B-Instruct-2507-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-235B-A22B-Instruct-2507-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-30B-A3B-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-30B-A3B-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Coder-480B-A35B-Instruct-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Coder-480B-A35B-Instruct-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Coder-Next-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Coder-Next-5bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Coder-Next-6bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Coder-Next-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Coder-Next-bf16.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Next-80B-A3B-Instruct-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Next-80B-A3B-Instruct-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Next-80B-A3B-Thinking-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-Next-80B-A3B-Thinking-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3-VL-4B-Instruct-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-122B-A10B-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-122B-A10B-6bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-122B-A10B-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-122B-A10B-bf16.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-27B-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-27B-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-2B-MLX-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-35B-A3B-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-35B-A3B-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-397B-A17B-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-397B-A17B-6bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-397B-A17B-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-9B-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.5-9B-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.6-27B-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.6-27B-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.6-27B-bf16.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.6-35B-A3B-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.6-35B-A3B-5bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.6-35B-A3B-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.6-35B-A3B-bf16.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.8-27B-4bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.8-27B-8bit.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.8-27B-bf16.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.8-27B-mxfp4.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.8-27B-nvfp4.toml` (config)
- `resources/inference_model_cards/qwen3/mlx-community--Qwen3.8-Flash-Next-4bit.toml` (config)
- `resources/inference_model_cards/step/mlx-community--Step-3.5-Flash-4bit.toml` (config)
- `resources/inference_model_cards/step/mlx-community--Step-3.5-Flash-6bit.toml` (config)
- `resources/inference_model_cards/step/mlx-community--Step-3.5-Flash-8bit.toml` (config)
- `rust/exo_rs/Cargo.toml` (manifest)
- `rust/exo_rs/pyproject.toml` (manifest)
- `rust/networking/Cargo.toml` (manifest)

## Top-level layout

- `.typings` — 293 analysed file(s)
- `resources` — 176 analysed file(s)
- `app` — 85 analysed file(s)
- `src` — 74 analysed file(s)
- `dashboard` — 73 analysed file(s)
- `rust` — 23 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 15 analysed file(s)
- `bench` — 12 analysed file(s)
- `.githooks` — 4 analysed file(s)
- `nix` — 4 analysed file(s)
- `packaging` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.zed` — 1 analysed file(s)
- `docs` — 1 analysed file(s)
- `python` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 13 file(s) were skipped during inventory (3 x lockfile excluded; 10 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a60b95698ca81737d367443674dd5563cbc9559b` is the revision these paths and observations refer to.
