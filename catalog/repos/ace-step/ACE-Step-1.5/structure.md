# Project structure: ace-step/ACE-Step-1.5

**Analysed commit:** `ca1e85fe9430179831e6bc6be790c332190a3866`

**Commit reference:** [ca1e85fe9430179831e6bc6be790c332190a3866](https://github.com/ace-step/ACE-Step-1.5/commit/ca1e85fe9430179831e6bc6be790c332190a3866)

**Tree at this commit:** [ace-step/ACE-Step-1.5@ca1e85fe9430](https://github.com/ace-step/ACE-Step-1.5/tree/ca1e85fe9430179831e6bc6be790c332190a3866)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ace-step/ACE-Step-1.5 |
| Description | The most powerful local music generation model that outperforms almost all commercial alternatives, supporting Mac, AMD, Intel, and CUDA devices. |
| Stars | 14757 |
| Forks | 1956 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `ca1e85fe9430179831e6bc6be790c332190a3866` |
| Retrieved at | 2026-11-14T19:09:15.363762+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.claude/  (35 files)
  skills/  (35 files)
    acestep/  (4 files)
      … 4 files under this directory
    acestep-docs/  (12 files)
      … 12 files under this directory
    acestep-lyrics-transcription/  (3 files)
      … 3 files under this directory
    acestep-simplemv/  (12 files)
      … 12 files under this directory
    acestep-songwriting/  (1 files)
      … 1 files under this directory
    acestep-thumbnail/  (3 files)
      … 3 files under this directory
.githooks/  (1 files)
  pre-push
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (4 files)
    close-inactive-issues.yml
    codeql.yml
    container.yml
    docs.yml
  codeql-config.yml
  copilot-instructions.md
acestep/  (614 files)
  api/  (110 files)
    http/  (36 files)
      … 36 files under this directory
    jobs/  (9 files)
      … 9 files under this directory
    __init__.py
    job_analysis_runtime.py
    job_analysis_runtime_test.py
    job_blocking_generation.py
    job_blocking_generation_test.py
    job_execution_runtime.py
    job_execution_runtime_test.py
    job_generation_runtime.py
    job_generation_runtime_test.py
    job_generation_setup.py
    job_generation_setup_test.py
    job_llm_preparation.py
    job_llm_preparation_test.py
    job_model_selection.py
    job_model_selection_on_demand_test.py
    job_model_selection_test.py
    job_result_payload.py
    job_result_payload_test.py
    job_runtime_state.py
    job_runtime_state_test.py
    lifespan_runtime.py
    lifespan_runtime_test.py
    llm_generation_inputs.py
    llm_readiness.py
    … 41 more files
  core/  (115 files)
    audio/  (1 files)
      … 1 files under this directory
    generation/  (98 files)
      … 98 files under this directory
    llm/  (1 files)
      … 1 files under this directory
    lora/  (6 files)
      … 6 files under this directory
    scoring/  (7 files)
      … 7 files under this directory
    system/  (1 files)
      … 1 files under this directory
    __init__.py
  dataset/  (3 files)
    builder/  (1 files)
      … 1 files under this directory
    runtime/  (1 files)
      … 1 files under this directory
    __init__.py
  models/  (48 files)
    base/  (4 files)
      … 4 files under this directory
    common/  (15 files)
      … 15 files under this directory
    mlx/  (10 files)
      … 10 files under this directory
    sft/  (4 files)
      … 4 files under this directory
    turbo/  (3 files)
      … 3 files under this directory
    xl_base/  (4 files)
      … 4 files under this directory
    xl_sft/  (4 files)
      … 4 files under this directory
    xl_turbo/  (3 files)
      … 3 files under this directory
    __init__.py
  text_tasks/  (27 files)
    __init__.py
    external_ai_json_parsing.py
    external_ai_json_parsing_test.py
    external_ai_protocols.py
    external_ai_protocols_test.py
    external_ai_request_helpers.py
    external_ai_request_helpers_test.py
    external_ai_response_parsing.py
    external_ai_response_parsing_test.py
    external_ai_types.py
    external_ai_types_test.py
    external_lm_captioning.py
    external_lm_captioning_fallback_locale.py
    external_lm_captioning_test.py
    external_lm_model_cache.py
    external_lm_model_cache_test.py
    external_lm_model_discovery.py
    external_lm_model_discovery_test.py
    external_lm_providers.py
    external_lm_providers_test.py
    external_lm_runtime_store.py
    external_lm_runtime_store_persistence_test.py
    external_lm_runtime_store_test.py
    passphrase_store.py
    … 3 more files
  third_parts/  (28 files)
    nano-vllm/  (28 files)
      … 28 files under this directory
  training/  (35 files)
    dataset_builder_modules/  (23 files)
      … 23 files under this directory
    __init__.py
    configs.py
    data_module.py
    data_module_test.py
    dataset_builder.py
    lokr_utils.py
    lora_checkpoint.py
    lora_injection.py
    lora_utils.py
    path_safety.py
    test_lora_utils.py
    trainer.py
  training_v2/  (56 files)
    cli/  (8 files)
      … 8 files under this directory
    presets/  (7 files)
      … 7 files under this directory
    ui/  (19 files)
      … 19 files under this directory
    __init__.py
    configs.py
    estimate.py
    fixed_lora_module.py
    fixed_lora_module_precision_test.py
    gpu_utils.py
    make_test_fixtures.py
    model_discovery.py
    model_loader.py
    optim.py
    preprocess.py
    preprocess_discovery.py
    preprocess_prompt.py
    preprocess_vae.py
    settings.py
    tensorboard_utils.py
    timestep_sampling.py
    trainer_basic_loop.py
    trainer_fixed.py
    trainer_helpers.py
    trainer_helpers_test.py
    trainer_vanilla.py
  ui/  (152 files)
    gradio/  (151 files)
      … 151 files under this directory
    __init__.py
  __init__.py
  acestep_v15_pipeline.py
  acestep_v15_pipeline_test.py
  api_server.py
  audio_utils.py
  audio_utils_test.py
  audio_utils_uuid_test.py
  cli_args.py
  cli_args_test.py
  constants.py
  constrained_logits_processor.py
  dataset_handler.py
  debug_utils.py
  direct_conditioning_tasks_test.py
  gpu_config.py
  gpu_config_effective_free_vram_test.py
  gpu_config_lm_memory_ratio_test.py
  gpu_config_test.py
  handler.py
  inference.py
  inference_repaint_cache_test.py
  inference_seed_fallback_test.py
  launcher_compat.py
  launcher_compat_test.py
  … 16 more files
assets/  (1 files)
  acemusic-logo.svg
docs/  (64 files)
  .vitepress/  (3 files)
    theme/  (2 files)
      … 2 files under this directory
    config.mts
  en/  (18 files)
    ACE-Step1.5-Rocm-Manual-Linux.md
    ALT_VAE.md
    API.md
    BENCHMARK.md
    CLI.md
    DCW.md
    GPU_COMPATIBILITY.md
    GPU_TROUBLESHOOTING.md
    GRADIO_GUIDE.md
    INFERENCE.md
    INSTALL.md
    Large_Scale_SFT_Training_Guide.md
    LoRA_Training_Tutorial.md
    Openrouter_API_DOC.md
    Tutorial.md
    UI_SUPPORT.md
    ace_step_musicians_guide.md
    index.md
  ja/  (9 files)
    API.md
    GPU_COMPATIBILITY.md
    GRADIO_GUIDE.md
    INFERENCE.md
    INSTALL.md
    LoRA_Training_Tutorial.md
    Openrouter_API_DOC.md
    Tutorial.md
    index.md
  ko/  (8 files)
    API.md
    GPU_COMPATIBILITY.md
    GRADIO_GUIDE.md
    INFERENCE.md
    LoRA_Training_Tutorial.md
    Openrouter_API_DOC.md
    Tutorial.md
    index.md
  public/  (1 files)
    favicon.svg
  sidestep/  (14 files)
    Dataset Preparation.md
    End-to-End Tutorial.md
    Estimation Guide.md
    Getting Started.md
    Model Management.md
    ObsidianREADME.md
    Preset Management.md
    RepositoryREADME.md
    Shift and Timestep Sampling.md
    The Settings Wizard.md
    Training Guide.md
    Using Your Adapter.md
    VRAM Optimization Guide.md
    Windows Notes.md
  zh/  (10 files)
    API.md
    BENCHMARK.md
    GPU_COMPATIBILITY.md
    GRADIO_GUIDE.md
    INFERENCE.md
    INSTALL.md
    LoRA_Training_Tutorial.md
    Openrouter_API_DOC.md
    Tutorial.md
    index.md
  index.md
examples/  (58 files)
  simple_mode/  (58 files)
    example_01.json
    example_02.json
    example_03.json
    example_04.json
    example_05.json
    example_06.json
    example_07.json
    example_08.json
    example_09.json
    example_10.json
    example_100.json
    example_101.json
    example_102.json
    example_103.json
    example_104.json
    example_105.json
    example_106.json
    example_107.json
    example_108.json
    example_109.json
    example_11.json
    example_110.json
    example_111.json
    example_112.json
    … 34 more files
.dockerignore
.editorconfig
.env.example
.gitignore
AGENTS.md
CONTRIBUTING.md
Dockerfile
Dockerfile.jetson
LICENSE
README-XPU.md
README.md
SECURITY.md
check_update.bat
check_update.sh
cli.py
close_api_server.sh
docker-compose.jetson.yml
docker-compose.yml
```

## Entry points

- [acestep/acestep_v15_pipeline.py:708](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/acestep_v15_pipeline.py#L708)
- [acestep/acestep_v15_pipeline_test.py:152](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/acestep_v15_pipeline_test.py#L152)
- [acestep/api/http/audio_route_http_test.py:27](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api/http/audio_route_http_test.py#L27)
- [acestep/api/http/audio_route_test.py:34](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api/http/audio_route_test.py#L34)
- [acestep/api/http/auth_test.py:83](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api/http/auth_test.py#L83)
- [acestep/api/http/lora_routes_http_test.py:76](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api/http/lora_routes_http_test.py#L76)
- [acestep/api/http/lora_routes_test.py:83](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api/http/lora_routes_test.py#L83)
- [acestep/api/http/model_init_service_test.py:316](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api/http/model_init_service_test.py#L316)
- [acestep/api/http/model_service_routes_http_test.py:75](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api/http/model_service_routes_http_test.py#L75)
- [acestep/api/http/model_service_routes_test.py:56](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api/http/model_service_routes_test.py#L56)
- [acestep/api/http/query_result_route_http_test.py:62](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api/http/query_result_route_http_test.py#L62)
- [acestep/api/http/query_result_route_test.py:72](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/acestep/api/http/query_result_route_test.py#L72)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| acestep package | library | Observed | Groups 228 file(s) under acestep package (observed from repository paths and static analysis). Observed top-level classes: AceStepDataModule, AceStepHandler, AceStepTrainingDataset, AssistantMessage, Attention, AudioCon… |
| API layer | api | Observed | Groups 60 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /health, GET /v1/models, GET /v1/audio, POST /create_random_sample, POST /query_result. Observed top-level cla… |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. Observed top-level functions: _default_settings, get_checkpoint_dir, is_firs… |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 36 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AceStepConfig, AudioSample, DCWCorrector, DatasetMetadata, MLXAttention, MLXAutoEncoderOobleck. Observ… |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: AceStepAttention, AceStepAudioTokenizer,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 76 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AudioCodesMixin, BatchPrepMixin, ConditioningBatchMixin, ConditioningEmbedMixin, Condition… |
| Tests | test | Observed | Groups 184 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: PATCH acestep.api.job_runtime_state.update_local_cache, PATCH aceste… |

## Important files

- `.claude/skills/acestep-lyrics-transcription/scripts/config.example.json` (config)
- `.claude/skills/acestep-simplemv/scripts/package.json` (manifest)
- `.claude/skills/acestep-simplemv/scripts/tsconfig.json` (config)
- `.claude/skills/acestep-thumbnail/scripts/config.example.json` (config)
- `.claude/skills/acestep/scripts/config.example.json` (config)
- `.dockerignore` (container)
- `.editorconfig` (config)
- `.env.example` (config)
- `.github/codeql-config.yml` (config)
- `.github/workflows/close-inactive-issues.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/container.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `Dockerfile` (container)
- `Dockerfile.jetson` (container)
- `acestep/third_parts/nano-vllm/pyproject.toml` (manifest)
- `acestep/training_v2/presets/high_quality.json` (config)
- `acestep/training_v2/presets/quick_test.json` (config)
- `acestep/training_v2/presets/recommended.json` (config)
- `acestep/training_v2/presets/vram_12gb.json` (config)
- `acestep/training_v2/presets/vram_16gb.json` (config)
- `acestep/training_v2/presets/vram_24gb_plus.json` (config)
- `acestep/training_v2/presets/vram_8gb.json` (config)
- `acestep/ui/gradio/i18n/en.json` (config)
- `acestep/ui/gradio/i18n/he.json` (config)
- `acestep/ui/gradio/i18n/ja.json` (config)
- `acestep/ui/gradio/i18n/pt.json` (config)
- `acestep/ui/gradio/i18n/zh.json` (config)
- `docker-compose.jetson.yml` (config)
- `docker-compose.yml` (container)
- `examples/simple_mode/example_01.json` (config)
- `examples/simple_mode/example_02.json` (config)
- `examples/simple_mode/example_03.json` (config)
- `examples/simple_mode/example_04.json` (config)
- `examples/simple_mode/example_05.json` (config)
- `examples/simple_mode/example_06.json` (config)
- `examples/simple_mode/example_07.json` (config)
- `examples/simple_mode/example_08.json` (config)
- `examples/simple_mode/example_09.json` (config)
- `examples/simple_mode/example_10.json` (config)
- `examples/simple_mode/example_100.json` (config)
- `examples/simple_mode/example_101.json` (config)
- `examples/simple_mode/example_102.json` (config)
- `examples/simple_mode/example_103.json` (config)
- `examples/simple_mode/example_104.json` (config)
- `examples/simple_mode/example_105.json` (config)
- `examples/simple_mode/example_106.json` (config)
- `examples/simple_mode/example_107.json` (config)
- `examples/simple_mode/example_108.json` (config)
- `examples/simple_mode/example_109.json` (config)
- `examples/simple_mode/example_11.json` (config)
- `examples/simple_mode/example_110.json` (config)
- `examples/simple_mode/example_111.json` (config)
- `examples/simple_mode/example_112.json` (config)
- `examples/simple_mode/example_113.json` (config)
- `examples/simple_mode/example_114.json` (config)
- `examples/simple_mode/example_115.json` (config)
- `examples/simple_mode/example_116.json` (config)
- `examples/simple_mode/example_117.json` (config)
- `examples/simple_mode/example_118.json` (config)
- `examples/simple_mode/example_119.json` (config)
- `examples/simple_mode/example_12.json` (config)
- `examples/simple_mode/example_120.json` (config)
- `examples/simple_mode/example_121.json` (config)
- `examples/simple_mode/example_122.json` (config)
- `examples/simple_mode/example_123.json` (config)
- `examples/simple_mode/example_124.json` (config)
- `examples/simple_mode/example_125.json` (config)
- `examples/simple_mode/example_126.json` (config)
- `examples/simple_mode/example_127.json` (config)
- `examples/simple_mode/example_128.json` (config)
- `examples/simple_mode/example_129.json` (config)
- `examples/simple_mode/example_13.json` (config)
- `examples/simple_mode/example_130.json` (config)
- `examples/simple_mode/example_131.json` (config)
- `examples/simple_mode/example_132.json` (config)
- `examples/simple_mode/example_133.json` (config)
- `examples/simple_mode/example_134.json` (config)
- `examples/simple_mode/example_135.json` (config)
- `examples/simple_mode/example_136.json` (config)
- `examples/simple_mode/example_137.json` (config)
- `examples/simple_mode/example_138.json` (config)
- `examples/simple_mode/example_139.json` (config)
- `examples/simple_mode/example_14.json` (config)
- `examples/simple_mode/example_140.json` (config)
- `examples/simple_mode/example_141.json` (config)
- `examples/simple_mode/example_142.json` (config)
- `examples/simple_mode/example_143.json` (config)

## Top-level layout

- `acestep` — 614 analysed file(s)
- `docs` — 64 analysed file(s)
- `examples` — 58 analysed file(s)
- `.claude` — 35 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 8 analysed file(s)
- `.githooks` — 1 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ca1e85fe9430179831e6bc6be790c332190a3866` is the revision these paths and observations refer to.
