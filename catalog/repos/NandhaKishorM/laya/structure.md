# Project structure: NandhaKishorM/laya

**Analysed commit:** `af8ada066685d66b3fc0b31e6c56b96def23fe2f`

**Commit reference:** [af8ada066685d66b3fc0b31e6c56b96def23fe2f](https://github.com/NandhaKishorM/laya/commit/af8ada066685d66b3fc0b31e6c56b96def23fe2f)

**Tree at this commit:** [NandhaKishorM/laya@af8ada066685](https://github.com/NandhaKishorM/laya/tree/af8ada066685d66b3fc0b31e6c56b96def23fe2f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | NandhaKishorM/laya |
| Description | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ languages, with a router that picks the right checkpoint per request. |
| Stars | 35521 |
| Forks | 3186 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `af8ada066685d66b3fc0b31e6c56b96def23fe2f` |
| Retrieved at | 2026-11-14T19:06:58.013955+00:00 |
| Files in this snapshot | 633 |

## Directory tree

```text
.github/  (18 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (13 files)
    ci.yml
    cpp.yml
    docker.yml
    docs.yml
    dotnet.yml
    evals.yml
    go.yml
    java.yml
    release-java.yml
    release-ts.yml
    release.yml
    rust.yml
    security.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
assets/  (6 files)
  logo-lockup-dark.svg
  logo-lockup.svg
  logo-mark-ink.svg
  logo-mark-mono.svg
  logo-mark.svg
  make_logo.py
benchmarks/  (120 files)
  results/  (108 files)
    compile-defaults/  (42 files)
      … 42 files under this directory
    cpu/  (53 files)
      … 53 files under this directory
    aoti_multilingual_rtx4070.json
    fast_english_rtx4070.json
    fast_multilingual_rtx4070.json
    mps_autocast_english_m1pro.json
    mps_autocast_english_m5pro.json
    mps_autocast_multilingual_m1pro.json
    mps_autocast_multilingual_m5pro.json
    parity_english_fp16_rtx4070.json
    parity_english_rtx4070.json
    parity_multilingual_fp16_rtx4070.json
    parity_multilingual_rtx4070.json
    parity_typed_decisions_fp16_rtx4070.json
    parity_typed_decisions_rtx4070.json
  bench_compile.py
  bench_compile_defaults.py
  bench_cpu.py
  bench_fast.py
  bench_mps_autocast.py
  bench_predict_batch.py
  compare_compile_defaults.py
  parity_fast.py
  plot_results.py
  results-consistency-rtx4070.json
  results-router-rtx4070.json
  results-rtx4070.json
docker/  (3 files)
  check_torch.py
  entrypoint.py
  prefetch_modelscope.py
docs/  (41 files)
  hooks/  (8 files)
    .nav.yml
    api.md
    errors.md
    examples.md
    index.md
    lifecycle.md
    patterns.md
    tracing.md
  reference/  (7 files)
    .nav.yml
    agent.md
    helpers.md
    index.md
    langchain.md
    router.md
    train.md
  .nav.yml
  agno.md
  benchmarks.md
  cli-mcp.md
  compile-and-fast-path.md
  crewai.md
  docker-platforms.md
  docker.md
  evals.md
  fast-backends.md
  finetune.md
  finetune_browser_agent.md
  guardrail-limitations.md
  http-api.md
  index.md
  langchain.md
  llamaindex.md
  questions-and-answers.md
  routing.md
  security.md
  staged-adoption.md
  structured.md
  tools.md
  typescript-sdk.md
  … 2 more files
examples/  (60 files)
  data/  (1 files)
    routing_labels.csv
  docker/  (2 files)
    quickstart.py
    request.json
  evals/  (1 files)
    teacher_agreement.py
  hooks/  (5 files)
    README.md
    audit.py
    cache.py
    otel.py
    redact.py
  01_first_call_minimal.py
  02_hello_world_decision.py
  03_reading_the_result.py
  04_choice_question.py
  05_choice_criteria_design.py
  06_score_question.py
  07_score_levels.py
  08_noul_question.py
  09_noul_criteria_wording.py
  10_mixed_primitives_one_pass.py
  11_json_state.py
  12_state_wording_matters.py
  13_email_state_and_cleaning.py
  14_conversation_turns.py
  15_truncation_basics.py
  16_many_questions_one_pass.py
  17_timing_a_call.py
  18_confidence_gating.py
  19_many_states_loop.py
  20_which_checkpoint.py
  21_routing_without_running.py
  22_route_and_predict_multilingual.py
  23_local_offline_models.py
  24_preload_and_memory.py
  … 27 more files
laya-cpp/  (69 files)
  cmake/  (3 files)
    check_compile_flags.cmake
    check_discovery_time.cmake
    onnxruntime.cmake
  include/  (17 files)
    laya/  (17 files)
      … 17 files under this directory
  scripts/  (4 files)
    fixtures/  (1 files)
      … 1 files under this directory
    check_ort_root.sh
    check_test_xml.py
    test_check_test_xml.py
  src/  (18 files)
    agent.cpp
    cnum.hpp
    collate.cpp
    decode.cpp
    infer.cpp
    lang.cpp
    lang_tables.inc
    onnx.cpp
    onnx_graph.cpp
    pyjson.cpp
    pyvalue.cpp
    schema.cpp
    sequence.cpp
    sha256.cpp
    tokenizer.cpp
    unicodedata.cpp
    unicodedata_tables.inc
    version.cpp
  tests/  (23 files)
    tools/  (6 files)
      … 6 files under this directory
    agent_test.cpp
    checkpoint.hpp
    decode_test.cpp
    foundation_test.cpp
    golden.hpp
    hardening_test.cpp
    lang_boundary.inc
    lang_test.cpp
    onnx_hostile_graphs.inc
    onnx_test.cpp
    question_fixture.hpp
    schema_test.cpp
    sequence_test.cpp
    stub_session.hpp
    tokenizer_test.cpp
    unicode_digests.inc
    version_test.cpp
  .gitignore
  CMakeLists.txt
  CMakePresets.json
  README.md
laya-dotnet/  (288 files)
  samples/  (12 files)
    Laya.Benchmark/  (4 files)
      … 4 files under this directory
    Laya.Routing/  (4 files)
      … 4 files under this directory
    Laya.Sample/  (4 files)
      … 4 files under this directory
  src/  (31 files)
    Laya/  (31 files)
      … 31 files under this directory
  tests/  (238 files)
    Laya.Tests/  (238 files)
      … 238 files under this directory
  .gitignore
  CHANGELOG.md
  Directory.Build.props
  Laya.slnx
  MODELS.md
  README.md
  global.json
laya-go/  (2 files)
  onnx/  (1 files)
    go.sum
  go.mod
research/  (3 files)
  benchmarks/  (1 files)
    es_phone_turns/  (1 files)
      … 1 files under this directory
  eval/  (1 files)
    __init__.py
  __init__.py
sdk/  (1 files)
  python/  (1 files)
    src/  (1 files)
      … 1 files under this directory
.dockerignore
.envrc
.gitattributes
.gitignore
.gitleaksignore
AGENTS.md
BENCHMARKS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
LOCAL_SETUP.md
README.md
SECURITY.md
compose.cuda.yaml
compose.example.yml
compose.http.yaml
compose.modelscope.yaml
compose.spark.yaml
compose.yaml
flake.lock
flake.nix
```

## Entry points

- [assets/make_logo.py:144](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/assets/make_logo.py#L144)
- [benchmarks/bench_compile.py:63](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/benchmarks/bench_compile.py#L63)
- [benchmarks/bench_compile_defaults.py:87](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/benchmarks/bench_compile_defaults.py#L87)
- [benchmarks/bench_cpu.py:275](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/benchmarks/bench_cpu.py#L275)
- [benchmarks/bench_mps_autocast.py:161](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/benchmarks/bench_mps_autocast.py#L161)
- [benchmarks/bench_predict_batch.py:248](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/benchmarks/bench_predict_batch.py#L248)
- [benchmarks/compare_compile_defaults.py:28](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/benchmarks/compare_compile_defaults.py#L28)
- [benchmarks/parity_fast.py:103](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/benchmarks/parity_fast.py#L103)
- [benchmarks/plot_results.py:121](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/benchmarks/plot_results.py#L121)
- [docker/check_torch.py:88](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/docker/check_torch.py#L88)
- [docker/entrypoint.py:46](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/docker/entrypoint.py#L46)
- [docker/prefetch_modelscope.py:307](https://github.com/NandhaKishorM/laya/blob/af8ada066685d66b3fc0b31e6c56b96def23fe2f/docker/prefetch_modelscope.py#L307)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 1 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level functions: batch, fwd, qs, timeit. |
| Configuration and deployment | config | Observed | Groups 67 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _refuse, _refuse_dtd, answers, arc_path, batch, bench. |
| laya-cpp package | library | Observed | Groups 16 file(s) under laya-cpp package (observed from repository paths and static analysis). |
| laya-dotnet package | library | Observed | Groups 34 file(s) under laya-dotnet package (observed from repository paths and static analysis). |
| research package | library | Observed | Groups 2 file(s) under research package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 262 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CheckerTest. Observed top-level functions: report, run. |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/cpp.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/dotnet.yml` (ci)
- `.github/workflows/evals.yml` (ci)
- `.github/workflows/go.yml` (ci)
- `.github/workflows/java.yml` (ci)
- `.github/workflows/release-java.yml` (ci)
- `.github/workflows/release-ts.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/rust.yml` (ci)
- `.github/workflows/security.yml` (ci)
- `Dockerfile` (container)
- `benchmarks/results-consistency-rtx4070.json` (config)
- `benchmarks/results-router-rtx4070.json` (config)
- `benchmarks/results-rtx4070.json` (config)
- `benchmarks/results/aoti_multilingual_rtx4070.json` (config)
- `benchmarks/results/cpu/diagnostic-plan.json` (config)
- `benchmarks/results/cpu/linux-english-latency.json` (config)
- `benchmarks/results/cpu/linux-english-long-options.json` (config)
- `benchmarks/results/cpu/linux-english-memory-baseline.json` (config)
- `benchmarks/results/cpu/linux-english-memory-selected.json` (config)
- `benchmarks/results/cpu/linux-environment.json` (config)
- `benchmarks/results/cpu/linux-multilingual-latency.json` (config)
- `benchmarks/results/cpu/linux-multilingual-long-options.json` (config)
- `benchmarks/results/cpu/linux-multilingual-memory-baseline.json` (config)
- `benchmarks/results/cpu/linux-multilingual-memory-selected.json` (config)
- `benchmarks/results/cpu/linux-typed-decisions-latency.json` (config)
- `benchmarks/results/cpu/linux-typed-decisions-long-options.json` (config)
- `benchmarks/results/cpu/linux-typed-decisions-memory-baseline.json` (config)
- `benchmarks/results/cpu/linux-typed-decisions-memory-selected.json` (config)
- `benchmarks/results/cpu/mac-english-diagnostic.json` (config)
- `benchmarks/results/cpu/mac-english-long-options.json` (config)
- `benchmarks/results/cpu/mac-english-memory-baseline.json` (config)
- `benchmarks/results/cpu/mac-english-memory-selected.json` (config)
- `benchmarks/results/cpu/mac-english-standard.json` (config)
- `benchmarks/results/cpu/mac-multilingual-ablation-head.json` (config)
- `benchmarks/results/cpu/mac-multilingual-ablation-windows.json` (config)
- `benchmarks/results/cpu/mac-multilingual-long-options.json` (config)
- `benchmarks/results/cpu/mac-multilingual-memory-baseline.json` (config)
- `benchmarks/results/cpu/mac-multilingual-memory-selected.json` (config)
- `benchmarks/results/cpu/mac-multilingual-standard.json` (config)
- `benchmarks/results/cpu/mac-typed-decisions-long-options.json` (config)
- `benchmarks/results/cpu/mac-typed-decisions-memory-baseline.json` (config)
- `benchmarks/results/cpu/mac-typed-decisions-memory-selected.json` (config)
- `benchmarks/results/cpu/mac-typed-decisions-standard.json` (config)
- `benchmarks/results/cpu/manifest.json` (config)
- `benchmarks/results/cpu/massive-en-summary.json` (config)
- `benchmarks/results/cpu/upstream/bench_latency-baseline.json` (config)
- `benchmarks/results/cpu/upstream/bench_latency-pr.json` (config)
- `benchmarks/results/cpu/upstream/bench_long_context-baseline.json` (config)
- `benchmarks/results/cpu/upstream/bench_long_context-pr.json` (config)
- `benchmarks/results/cpu/upstream/completed.json` (config)
- `benchmarks/results/cpu/upstream/device-repeat-completed.json` (config)
- `benchmarks/results/cpu/upstream/device-repeat-plan.json` (config)
- `benchmarks/results/cpu/upstream/manifest.json` (config)
- `benchmarks/results/cpu/upstream/plan.json` (config)
- `benchmarks/results/cpu/validation.json` (config)
- `benchmarks/results/fast_english_rtx4070.json` (config)
- `benchmarks/results/fast_multilingual_rtx4070.json` (config)
- `benchmarks/results/mps_autocast_english_m1pro.json` (config)
- `benchmarks/results/mps_autocast_english_m5pro.json` (config)
- `benchmarks/results/mps_autocast_multilingual_m1pro.json` (config)
- `benchmarks/results/mps_autocast_multilingual_m5pro.json` (config)
- `benchmarks/results/parity_english_fp16_rtx4070.json` (config)
- `benchmarks/results/parity_english_rtx4070.json` (config)
- `benchmarks/results/parity_multilingual_fp16_rtx4070.json` (config)
- `benchmarks/results/parity_multilingual_rtx4070.json` (config)
- `benchmarks/results/parity_typed_decisions_fp16_rtx4070.json` (config)
- `benchmarks/results/parity_typed_decisions_rtx4070.json` (config)
- `compose.cuda.yaml` (config)
- `compose.example.yml` (config)
- `compose.http.yaml` (config)
- `compose.modelscope.yaml` (config)
- `compose.spark.yaml` (config)
- `compose.yaml` (container)
- `docs/.nav.yml` (config)
- `docs/hooks/.nav.yml` (config)
- `docs/reference/.nav.yml` (config)
- `examples/docker/request.json` (config)
- `laya-cpp/CMakePresets.json` (config)
- `laya-dotnet/global.json` (config)
- `laya-go/go.mod` (manifest)

## Top-level layout

- `laya-dotnet` — 288 analysed file(s)
- `benchmarks` — 120 analysed file(s)
- `laya-cpp` — 69 analysed file(s)
- `examples` — 60 analysed file(s)
- `docs` — 41 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `.github` — 18 analysed file(s)
- `assets` — 6 analysed file(s)
- `docker` — 3 analysed file(s)
- `research` — 3 analysed file(s)
- `laya-go` — 2 analysed file(s)
- `sdk` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `af8ada066685d66b3fc0b31e6c56b96def23fe2f` is the revision these paths and observations refer to.
