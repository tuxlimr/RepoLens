# Project structure: google-research/harness2

**Analysed commit:** `6868817518876de8fd170c6a8354daca273b6191`

**Commit reference:** [6868817518876de8fd170c6a8354daca273b6191](https://github.com/google-research/harness2/commit/6868817518876de8fd170c6a8354daca273b6191)

**Tree at this commit:** [google-research/harness2@686881751887](https://github.com/google-research/harness2/tree/6868817518876de8fd170c6a8354daca273b6191)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google-research/harness2 |
| Description | Not provided |
| Stars | 23880 |
| Forks | 2401 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `6868817518876de8fd170c6a8354daca273b6191` |
| Retrieved at | 2026-11-14T19:07:43.052980+00:00 |
| Files in this snapshot | 133 |

## Directory tree

```text
dependencies/  (3 files)
  ASSETS.json
  PINNED.md
  README.md
docs/  (3 files)
  BENCHMARKS.md
  EXPERIMENTS.md
  SETUP.md
harness2/  (39 files)
  benchmarks/  (7 files)
    __init__.py
    jb_opencode_runner.py
    jobbench.py
    lab.py
    tasks.py
    wb_render.py
    workbuddy.py
  cli/  (9 files)
    __init__.py
    _common.py
    bridge.py
    check.py
    demo.py
    judge.py
    report.py
    run_sweep.py
    setup.py
  core/  (14 files)
    __init__.py
    context.py
    judge.py
    ledger.py
    library.py
    prompts.py
    proposer.py
    recursion.py
    report.py
    runmark.py
    schedule.py
    selection.py
    spec.py
    tree.py
  substrate/  (4 files)
    __init__.py
    base.py
    codex.py
    opencode.py
  __init__.py
  config.py
  demo.py
  install.py
  preflight.py
scripts/  (8 files)
  check_provenance.py
  check_setup.py
  render_readme_typing.py
  run_jobbench.sh
  run_lab.sh
  run_workbuddy.sh
  setup_benchmark.py
  split_tasks.py
tests/  (25 files)
  fixtures/  (10 files)
    harvey-labs/  (7 files)
      … 7 files under this directory
    job-bench-eval/  (3 files)
      … 3 files under this directory
  test_baseline_judge.py
  test_env_example.py
  test_jobbench_killed_rollout.py
  test_jobbench_rollout_isolation.py
  test_jobbench_worker_failure.py
  test_lab_judge_patch.py
  test_lab_nested_deliverables.py
  test_proposer_failures.py
  test_proposer_session_errors.py
  test_requested_mode_resume.py
  test_runner_seed.py
  test_stage_retry.py
  test_subprocess_env.py
  test_task_input_identity.py
  test_workflow.py
third_party/  (48 files)
  jb_runner/  (12 files)
    codex_base_harness/  (1 files)
      … 1 files under this directory
    harness_baseline_oc/  (8 files)
      … 8 files under this directory
    LICENSE
    PROVENANCE.md
    run_benchmark_codex_cli_adapt.sh
  lab_runner/  (12 files)
    adapt_runs_cx/  (1 files)
      … 1 files under this directory
    opencode/  (7 files)
      … 7 files under this directory
    tts_lab/  (2 files)
      … 2 files under this directory
    LICENSE
    PROVENANCE.md
  licenses/  (4 files)
    harvey-labs.LICENSE
    job-bench-eval.LICENSE
    opencode.LICENSE
    workbuddy-bench.LICENSE
  patches/  (4 files)
    harvey-labs-judge-vertex-anthropic.diff
    job-bench-eval-judge.diff
    opencode-compat.diff
    workbuddy-bench-runtime.diff
  wb_runner/  (15 files)
    agents/  (4 files)
      … 4 files under this directory
    configs/  (9 files)
      … 9 files under this directory
    LICENSE
    PROVENANCE.md
  README.md
.env.example
.gitignore
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
pyproject.toml
```

## Entry points

- [harness2/benchmarks/jb_opencode_runner.py:346](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/benchmarks/jb_opencode_runner.py#L346)
- [harness2/benchmarks/wb_render.py:560](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/benchmarks/wb_render.py#L560)
- [harness2/cli/bridge.py](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/cli/bridge.py)
- [harness2/cli/check.py](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/cli/check.py)
- [harness2/cli/demo.py](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/cli/demo.py)
- [harness2/cli/judge.py](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/cli/judge.py)
- [harness2/cli/report.py](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/cli/report.py)
- [harness2/cli/run_sweep.py](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/cli/run_sweep.py)
- [harness2/cli/setup.py](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/harness2/cli/setup.py)
- [scripts/check_provenance.py:42](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/scripts/check_provenance.py#L42)
- [scripts/check_setup.py:20](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/scripts/check_setup.py#L20)
- [scripts/render_readme_typing.py:139](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/scripts/render_readme_typing.py#L139)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigError. Observed top-level functions: documents_dir, env, env_int, jb_repo, lab… |
| Application entry point | entrypoint | Observed | Groups 16 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: RenderBackendError, RenderInputError, Settings. Observed top-level functions: _admit, _at… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| harness2 package | library | Observed | Groups 15 file(s) under harness2 package (observed from repository paths and static analysis). Observed top-level classes: CodexSubstrate, DemoAdapter, DemoProposer, HelpFormatter, Install, JobBenchAdapter. Observed top… |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: BenchPrompts, BenchSpec, BenchmarkAdapter, BudgetError, ChannelSpec, ContextTree. Observed… |
| Tests | test | Observed | Groups 25 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BaselineJudgeTests, EnvExampleTests, FirstCandidateSelector, InputsFingerprintTests, JobbenchWorkerFailureT… |
| third_party package | library | Observed | Groups 10 file(s) under third_party package (observed from repository paths and static analysis). Observed top-level classes: CodexAgent, CodexHarnessAgent, OcAgent, OcHarnessAgent, RenderResult. Observed top-level func… |

## Important files

- `.env.example` (config)
- `MANIFEST.in` (manifest)
- `dependencies/ASSETS.json` (config)
- `harness2/cli/setup.py` (manifest)
- `pyproject.toml` (manifest)
- `third_party/jb_runner/harness_baseline_oc/harness.yaml` (config)
- `third_party/wb_runner/configs/harnesses/codex-harness/_defaults.yaml` (config)
- `third_party/wb_runner/configs/harnesses/codex-harness/versions/0.144.6.yaml` (config)
- `third_party/wb_runner/configs/harnesses/oc-harness/_defaults.yaml` (config)
- `third_party/wb_runner/configs/harnesses/oc-harness/versions/1.14.18.yaml` (config)
- `third_party/wb_runner/configs/harnesses/opencode/_defaults.yaml` (config)
- `third_party/wb_runner/configs/harnesses/opencode/docker/Dockerfile` (container)
- `third_party/wb_runner/configs/harnesses/opencode/presets/settings/v1_14.json` (config)
- `third_party/wb_runner/configs/harnesses/opencode/versions/1.14.18.yaml` (config)

## Top-level layout

- `third_party` — 48 analysed file(s)
- `harness2` — 39 analysed file(s)
- `tests` — 25 analysed file(s)
- `scripts` — 8 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `dependencies` — 3 analysed file(s)
- `docs` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `6868817518876de8fd170c6a8354daca273b6191` is the revision these paths and observations refer to.
