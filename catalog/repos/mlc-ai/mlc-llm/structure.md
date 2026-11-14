# Project structure: mlc-ai/mlc-llm

**Analysed commit:** `3b7663abb6962c1ac1be0337630321fd7bfcf9ff`

**Commit reference:** [3b7663abb6962c1ac1be0337630321fd7bfcf9ff](https://github.com/mlc-ai/mlc-llm/commit/3b7663abb6962c1ac1be0337630321fd7bfcf9ff)

**Tree at this commit:** [mlc-ai/mlc-llm@3b7663abb696](https://github.com/mlc-ai/mlc-llm/tree/3b7663abb6962c1ac1be0337630321fd7bfcf9ff)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mlc-ai/mlc-llm |
| Description | Universal LLM Deployment Engine with ML Compilation |
| Stars | 23417 |
| Forks | 2210 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `3b7663abb6962c1ac1be0337630321fd7bfcf9ff` |
| Retrieved at | 2026-11-14T19:07:49.728327+00:00 |
| Files in this snapshot | 703 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (8 files)
    bug-report.md
    config.yml
    documentation.md
    feature-request.md
    general.md
    model-request.md
    speed-report.md
    tracking.md
  workflows/  (4 files)
    documentation.yaml
    lint.yml
    update-relax.yaml
    windows-build.yaml
android/  (63 files)
  MLCChat/  (28 files)
    app/  (19 files)
      … 19 files under this directory
    gradle/  (1 files)
      … 1 files under this directory
    README.md
    build.gradle
    bundle_weight.py
    gradle.properties
    gradlew
    gradlew.bat
    mlc-package-config.json
    settings.gradle
  MLCEngineExample/  (24 files)
    app/  (15 files)
      … 15 files under this directory
    gradle/  (1 files)
      … 1 files under this directory
    README.md
    build.gradle
    bundle_weight.py
    gradle.properties
    gradlew
    gradlew.bat
    mlc-package-config.json
    settings.gradle
  mlc4j/  (9 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    CMakeLists.txt
    build.gradle
    prepare_libs.py
  .gitignore
  README.md
ci/  (8 files)
  task/  (5 files)
    build_clean.sh
    build_lib.sh
    build_win.bat
    test_model_compile.sh
    test_unittest.sh
  bash.sh
  build-environment.yaml
  jenkinsfile.groovy
cmake/  (2 files)
  StaticRuntime.cmake
  gen_cmake_config.py
cpp/  (83 files)
  json_ffi/  (8 files)
    conv_template.cc
    conv_template.h
    image_utils.cc
    image_utils.h
    json_ffi_engine.cc
    json_ffi_engine.h
    openai_api_protocol.cc
    openai_api_protocol.h
  metadata/  (2 files)
    model.cc
    model.h
  multi_gpu/  (2 files)
    builtin.cc
    multi_gpu_loader.cc
  serve/  (50 files)
    engine_actions/  (17 files)
      … 17 files under this directory
    sampler/  (3 files)
      … 3 files under this directory
    config.cc
    config.h
    data.cc
    data.h
    draft_token_workspace_manager.cc
    draft_token_workspace_manager.h
    engine.cc
    engine.h
    engine_state.cc
    engine_state.h
    event_trace_recorder.cc
    event_trace_recorder.h
    function_table.cc
    function_table.h
    logit_processor.cc
    logit_processor.h
    metrics.cc
    metrics.h
    model.cc
    model.h
    prefix_cache.cc
    prefix_cache.h
    radix_tree.cc
    radix_tree.h
    … 6 more files
  support/  (16 files)
    debug_utils.h
    device.h
    dynamic_bitset.h
    encoding.cc
    encoding.h
    json_parser.h
    load_bytes_from_file.h
    module_vtable.h
    nvtx.h
    progress_bar.h
    random.h
    result.h
    threading_backend.h
    utils.h
    vlm_utils.cc
    vlm_utils.h
  tokenizers/  (4 files)
    streamer.cc
    streamer.h
    tokenizers.cc
    tokenizers.h
  base.h
docs/  (33 files)
  _static/  (1 files)
    img/  (1 files)
      … 1 files under this directory
  community/  (2 files)
    faq.rst
    guideline.rst
  compilation/  (6 files)
    compile_models.rst
    configure_quantization.rst
    convert_weights.rst
    define_new_models.rst
    model_artifact_manifest.rst
    package_libraries_and_weights.rst
  deploy/  (8 files)
    android.rst
    cli.rst
    ide_integration.rst
    ios.rst
    mlc_chat_config.rst
    python_engine.rst
    rest.rst
    webllm.rst
  get_started/  (2 files)
    introduction.rst
    quick_start.rst
  install/  (5 files)
    conda.rst
    emcc.rst
    gpu.rst
    mlc_llm.rst
    tvm.rst
  microserving/  (1 files)
    tutorial.rst
  .gitignore
  Makefile
  README.md
  conf.py
  index.rst
  make.bat
  privacy.rst
  requirements.txt
examples/  (14 files)
  python/  (2 files)
    microserving/  (1 files)
      … 1 files under this directory
    sample_mlc_engine.py
  rest/  (12 files)
    nodejs/  (7 files)
      … 7 files under this directory
    python/  (3 files)
      … 3 files under this directory
    resources/  (2 files)
      … 2 files under this directory
ios/  (48 files)
  MLCChat/  (27 files)
    MLCChat/  (19 files)
      … 19 files under this directory
    MLCChat.xcodeproj/  (6 files)
      … 6 files under this directory
    README.md
    mlc-package-config.json
  MLCEngineExample/  (12 files)
    MLCEngineExample/  (7 files)
      … 7 files under this directory
    MLCEngineExample.xcodeproj/  (3 files)
      … 3 files under this directory
    README.md
    mlc-package-config.json
  MLCSwift/  (6 files)
    Sources/  (4 files)
      … 4 files under this directory
    Package.swift
    README.md
  .gitignore
  README.md
  prepare_libs.sh
python/  (336 files)
  mlc_llm/  (334 files)
    bench/  (8 files)
      … 8 files under this directory
    cli/  (15 files)
      … 15 files under this directory
    compiler_pass/  (24 files)
      … 24 files under this directory
    contrib/  (4 files)
      … 4 files under this directory
    conversation_template/  (30 files)
      … 30 files under this directory
    interface/  (12 files)
      … 12 files under this directory
    json_ffi/  (2 files)
      … 2 files under this directory
    loader/  (7 files)
      … 7 files under this directory
    model/  (144 files)
      … 144 files under this directory
    nn/  (4 files)
      … 4 files under this directory
    op/  (13 files)
      … 13 files under this directory
    protocol/  (9 files)
      … 9 files under this directory
    quantization/  (11 files)
      … 11 files under this directory
    router/  (2 files)
      … 2 files under this directory
    serve/  (20 files)
      … 20 files under this directory
    support/  (17 files)
      … 17 files under this directory
    testing/  (4 files)
      … 4 files under this directory
    tokenizers/  (4 files)
      … 4 files under this directory
    __init__.py
    __main__.py
    base.py
    libinfo.py
  requirements.txt
  setup.py
scripts/  (5 files)
  build_mlc_for_docs.sh
  build_site.sh
  check_url_validity.py
  gh_deploy_site.sh
  local_deploy_site.sh
site/  (12 files)
  _includes/  (4 files)
    arrow.svg
    github.svg
    head.html
    hero.html
  assets/  (2 files)
    css/  (1 files)
      … 1 files under this directory
    img/  (1 files)
      … 1 files under this directory
  .gitignore
  CNAME
  Gemfile
  _config.yml
  index.md
  privacy.md
tests/  (71 files)
  cpp/  (2 files)
    conv_template_unittest.cc
    support_utils_unittest.cc
  python/  (68 files)
    compiler_pass/  (5 files)
      … 5 files under this directory
    conversation_template/  (3 files)
      … 3 files under this directory
    integration/  (1 files)
      … 1 files under this directory
    json_ffi/  (3 files)
      … 3 files under this directory
    loader/  (2 files)
      … 2 files under this directory
    model/  (15 files)
      … 15 files under this directory
    op/  (6 files)
      … 6 files under this directory
    protocol/  (1 files)
      … 1 files under this directory
    quantization/  (2 files)
      … 2 files under this directory
    router/  (1 files)
      … 1 files under this directory
    serve/  (20 files)
      … 20 files under this directory
    support/  (6 files)
      … 6 files under this directory
    tokenizers/  (1 files)
      … 1 files under this directory
    __init__.py
    conftest.py
  README.md
web/  (4 files)
  emcc/  (1 files)
    mlc_wasm_runtime.cc
  Makefile
  README.md
  prep_emcc_deps.sh
.clang-format
.gitignore
.gitmodules
.pre-commit-config.yaml
.yamllint.yaml
CMakeLists.txt
CONTRIBUTORS.md
LICENSE
NOTICE
README.md
pyproject.toml
version.py
```

## Entry points

- [android/MLCChat/bundle_weight.py:39](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/android/MLCChat/bundle_weight.py#L39)
- [android/MLCEngineExample/bundle_weight.py:39](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/android/MLCEngineExample/bundle_weight.py#L39)
- [android/mlc4j/prepare_libs.py:109](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/android/mlc4j/prepare_libs.py#L109)
- [cmake/gen_cmake_config.py:5](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/cmake/gen_cmake_config.py#L5)
- [python/mlc_llm/__main__.py:66](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/python/mlc_llm/__main__.py#L66)
- [python/mlc_llm/bench/__main__.py:178](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/python/mlc_llm/bench/__main__.py#L178)
- [python/mlc_llm/bench/evaluation/gsm8k.py:294](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/python/mlc_llm/bench/evaluation/gsm8k.py#L294)
- [python/mlc_llm/bench/evaluation/mmlu.py:225](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/python/mlc_llm/bench/evaluation/mmlu.py#L225)
- [python/mlc_llm/cli/check_device.py:33](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/python/mlc_llm/cli/check_device.py#L33)
- [python/mlc_llm/cli/delivery.py:451](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/python/mlc_llm/cli/delivery.py#L451)
- [python/mlc_llm/cli/disco_remote_socket_session.py:24](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/python/mlc_llm/cli/disco_remote_socket_session.py#L24)
- [python/mlc_llm/cli/lib_delivery.py:198](https://github.com/mlc-ai/mlc-llm/blob/3b7663abb6962c1ac1be0337630321fd7bfcf9ff/python/mlc_llm/cli/lib_delivery.py#L198)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| android package | library | Observed | Groups 2 file(s) under android package (observed from repository paths and static analysis). |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). Observed routes: POST /debug/dump_event_trace, POST /debug/cuda_profiler_start, POST /debug/cuda_profiler_stop, POST /debug/dump_eng… |
| ci package | library | Observed | Groups 3 file(s) under ci package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 24 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BinaryDistribution, ConfigBase, ConfigOverrideBase, EngineConfig. Observed top-level… |
| cpp package | library | Observed | Groups 41 file(s) under cpp package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: EmbeddingMetadata, Model. |
| Application entry point | entrypoint | Observed | Groups 20 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: DebugChat, DefaultDebugInstrument, Defer… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). |
| ios package | library | Observed | Groups 2 file(s) under ios package (observed from repository paths and static analysis). |
| python package | library | Observed | Groups 311 file(s) under python package (observed from repository paths and static analysis). Observed top-level classes: APIEndPoint, AWQQuantize, AWQQuantizeLinear, ArgumentParser, ArtifactDefinition, AsyncChat. Obser… |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 73 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: _Dimension, _Parameter. Observed top-level functions: _build_and_run, _config, _create_json_file, _evaluate… |
| web package | library | Observed | Groups 1 file(s) under web package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/documentation.yaml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/update-relax.yaml` (ci)
- `.github/workflows/windows-build.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.yamllint.yaml` (config)
- `android/MLCChat/app/build.gradle` (manifest)
- `android/MLCChat/build.gradle` (manifest)
- `android/MLCChat/mlc-package-config.json` (config)
- `android/MLCEngineExample/app/build.gradle` (manifest)
- `android/MLCEngineExample/build.gradle` (manifest)
- `android/MLCEngineExample/mlc-package-config.json` (config)
- `android/mlc4j/build.gradle` (manifest)
- `ci/build-environment.yaml` (config)
- `docs/requirements.txt` (manifest)
- `examples/rest/nodejs/package.json` (manifest)
- `examples/rest/nodejs/tsconfig.json` (config)
- `ios/MLCChat/MLCChat/Assets.xcassets/AccentColor.colorset/Contents.json` (config)
- `ios/MLCChat/MLCChat/Assets.xcassets/AppIcon.appiconset/Contents.json` (config)
- `ios/MLCChat/MLCChat/Assets.xcassets/Contents.json` (config)
- `ios/MLCChat/MLCChat/Preview Content/Preview Assets.xcassets/Contents.json` (config)
- `ios/MLCChat/mlc-package-config.json` (config)
- `ios/MLCEngineExample/MLCEngineExample/Assets.xcassets/AccentColor.colorset/Contents.json` (config)
- `ios/MLCEngineExample/MLCEngineExample/Assets.xcassets/AppIcon.appiconset/Contents.json` (config)
- `ios/MLCEngineExample/MLCEngineExample/Assets.xcassets/Contents.json` (config)
- `ios/MLCEngineExample/MLCEngineExample/Preview Content/Preview Assets.xcassets/Contents.json` (config)
- `ios/MLCEngineExample/mlc-package-config.json` (config)
- `pyproject.toml` (manifest)
- `python/requirements.txt` (manifest)
- `python/setup.py` (manifest)
- `site/_config.yml` (config)

## Top-level layout

- `python` — 336 analysed file(s)
- `cpp` — 83 analysed file(s)
- `tests` — 71 analysed file(s)
- `android` — 63 analysed file(s)
- `ios` — 48 analysed file(s)
- `docs` — 33 analysed file(s)
- `examples` — 14 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 12 analysed file(s)
- `site` — 12 analysed file(s)
- `ci` — 8 analysed file(s)
- `scripts` — 5 analysed file(s)
- `web` — 4 analysed file(s)
- `cmake` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3b7663abb6962c1ac1be0337630321fd7bfcf9ff` is the revision these paths and observations refer to.
