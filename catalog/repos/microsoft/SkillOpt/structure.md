# Project structure: microsoft/SkillOpt

**Analysed commit:** `45f65ca04f5f6713bca7b9797b495696ba812751`

**Commit reference:** [45f65ca04f5f6713bca7b9797b495696ba812751](https://github.com/microsoft/SkillOpt/commit/45f65ca04f5f6713bca7b9797b495696ba812751)

**Tree at this commit:** [microsoft/SkillOpt@45f65ca04f5f](https://github.com/microsoft/SkillOpt/tree/45f65ca04f5f6713bca7b9797b495696ba812751)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/SkillOpt |
| Description | SkillOpt is a text-space optimizer that trains reusable natural-language skills for frozen LLM agents through trajectory-driven edits, validation-gated updates, and deployable best_skill.md artifacts. |
| Stars | 19078 |
| Forks | 1830 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `45f65ca04f5f6713bca7b9797b495696ba812751` |
| Retrieved at | 2026-11-14T19:08:17.532175+00:00 |
| Files in this snapshot | 482 |

## Directory tree

```text
.cursor-plugin/  (1 files)
  marketplace.json
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  dependabot.yml
blog/  (2 files)
  gating-reflection-safe-updates/  (1 files)
    index.html
  index.html
ckpt/  (7 files)
  alfworld/  (1 files)
    gpt5.5_skill.md
  docvqa/  (1 files)
    gpt5.5_skill.md
  livemath/  (1 files)
    gpt5.5_skill.md
  officeqa/  (1 files)
    gpt5.5_skill.md
  searchqa/  (1 files)
    gpt5.5_skill.md
  spreadsheetbench/  (1 files)
    gpt5.5_skill.md
  README.md
configs/  (8 files)
  _base_/  (1 files)
    default.yaml
  alfworld/  (1 files)
    default.yaml
  docvqa/  (1 files)
    default.yaml
  features/  (1 files)
    soft_gate.yaml
  livemathematicianbench/  (1 files)
    default.yaml
  officeqa/  (1 files)
    default.yaml
  searchqa/  (1 files)
    default.yaml
  spreadsheetbench/  (1 files)
    default.yaml
data/  (25 files)
  alfworld_path_split/  (4 files)
    test/  (1 files)
      … 1 files under this directory
    train/  (1 files)
      … 1 files under this directory
    val/  (1 files)
      … 1 files under this directory
    split_manifest.json
  docvqa_id_split/  (4 files)
    test/  (1 files)
      … 1 files under this directory
    train/  (1 files)
      … 1 files under this directory
    val/  (1 files)
      … 1 files under this directory
    split_manifest.json
  livemathematicianbench_id_split/  (4 files)
    test/  (1 files)
      … 1 files under this directory
    train/  (1 files)
      … 1 files under this directory
    val/  (1 files)
      … 1 files under this directory
    split_manifest.json
  officeqa_id_split/  (4 files)
    test/  (1 files)
      … 1 files under this directory
    train/  (1 files)
      … 1 files under this directory
    val/  (1 files)
      … 1 files under this directory
    split_manifest.json
  searchqa_id_split/  (4 files)
    test/  (1 files)
      … 1 files under this directory
    train/  (1 files)
      … 1 files under this directory
    val/  (1 files)
      … 1 files under this directory
    split_manifest.json
  spreadsheetbench_id_split/  (4 files)
    test/  (1 files)
      … 1 files under this directory
    train/  (1 files)
      … 1 files under this directory
    val/  (1 files)
      … 1 files under this directory
    split_manifest.json
  README.md
docs/  (26 files)
  guide/  (10 files)
    configuration.md
    dl-analogy.md
    first-experiment.md
    installation.md
    local-env-smoke.md
    new-backend.md
    new-benchmark.md
    offline-reproducibility.md
    skill-document.md
    training-loop.md
  reference/  (3 files)
    api.md
    cli.md
    config.md
  sleep/  (7 files)
    examples/  (2 files)
      … 2 files under this directory
    README.md
    RESULTS.md
    evalkit.md
    multi-skill-staging.md
    openai-compatible-endpoints.md
  superpowers/  (2 files)
    specs/  (1 files)
      … 1 files under this directory
    SECURITY.md
  contributing.md
  guideline.html
  index.md
  review_guidelines.md
plugins/  (67 files)
  claude-code/  (11 files)
    .claude-plugin/  (2 files)
      … 2 files under this directory
    commands/  (2 files)
      … 2 files under this directory
    hooks/  (2 files)
      … 2 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    README.md
  codex/  (4 files)
    skills/  (1 files)
      … 1 files under this directory
    README.md
    install.ps1
    install.sh
  copilot/  (8 files)
    skillopt/  (4 files)
      … 4 files under this directory
    README.md
    copilot-instructions.snippet.md
    mcp-config.example.json
    mcp_server.py
  cursor/  (7 files)
    .cursor-plugin/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
    install.ps1
    install.sh
  devin/  (10 files)
    fixtures/  (1 files)
      … 1 files under this directory
    hooks/  (2 files)
      … 2 files under this directory
    README.md
    devin-rules.snippet.md
    harvest_devin.py
    install.sh
    judge.py
    mcp-config.example.json
    mcp_server.py
  dsh/  (13 files)
    scripts/  (6 files)
      … 6 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
    README.zh.md
    cordis.patch.yml
    package.json
  openclaw/  (10 files)
    tests/  (3 files)
      … 3 files under this directory
    README.md
    SKILL.md
    config.json
    run_sleep.py
    run_sleep_cron.sh
    skillopt_sleep_openclaw.py
    slash_sleep.py
  README.md
  run-sleep.cmd
  run-sleep.ps1
  run-sleep.sh
scripts/  (9 files)
  __init__.py
  check_reproducibility.py
  eval_only.py
  materialize_searchqa.py
  run_alfworld.sh
  run_searchqa.sh
  run_spreadsheetbench.sh
  smoke_superpowers.sh
  train.py
skillopt/  (139 files)
  datasets/  (2 files)
    __init__.py
    base.py
  engine/  (2 files)
    __init__.py
    trainer.py
  envs/  (74 files)
    _template/  (4 files)
      … 4 files under this directory
    alfworld/  (11 files)
      … 11 files under this directory
    docvqa/  (9 files)
      … 9 files under this directory
    livemathematicianbench/  (10 files)
      … 10 files under this directory
    officeqa/  (12 files)
      … 12 files under this directory
    searchqa/  (10 files)
      … 10 files under this directory
    spreadsheetbench/  (15 files)
      … 15 files under this directory
    __init__.py
    base.py
    task_output.py
  evaluation/  (2 files)
    __init__.py
    gate.py
  gradient/  (3 files)
    __init__.py
    aggregate.py
    reflect.py
  model/  (13 files)
    __init__.py
    azure_openai.py
    backend_config.py
    claude_backend.py
    claude_code_backend.py
    codex_backend.py
    codex_harness.py
    common.py
    copilot_backend.py
    minimax_backend.py
    openai_compatible_backend.py
    qwen_backend.py
    router.py
  optimizer/  (12 files)
    __init__.py
    appendix.py
    clip.py
    lr_autonomous.py
    meta_skill.py
    rewrite.py
    scheduler.py
    select.py
    skill.py
    skill_aware.py
    slow_update.py
    update_modes.py
  prompts/  (22 files)
    __init__.py
    analyst_error.md
    analyst_error_full_rewrite.md
    analyst_error_rewrite.md
    analyst_success.md
    analyst_success_full_rewrite.md
    analyst_success_rewrite.md
    lr_autonomous.md
    merge_failure.md
    merge_failure_full_rewrite.md
    merge_failure_rewrite.md
    merge_final.md
    merge_final_full_rewrite.md
    merge_final_rewrite.md
    merge_success.md
    merge_success_full_rewrite.md
    merge_success_rewrite.md
    meta_skill.md
    ranking.md
    ranking_rewrite.md
    rewrite_skill.md
    slow_update.md
  scheduler/  (1 files)
    __init__.py
  utils/  (5 files)
    __init__.py
    console.py
    json_utils.py
    reproducibility.py
    scoring.py
  __init__.py
  config.py
  types.py
skillopt-assets/  (1 files)
  arxiv-logomark-small.svg
skillopt_sleep/  (45 files)
  adapters/  (2 files)
    __init__.py
    superpowers.py
  experiments/  (8 files)
    __init__.py
    gbrain_bench.py
    personas.py
    report.py
    run_experiment.py
    run_gbrain.py
    run_transfer.py
    sweep.py
  __init__.py
  __main__.py
  backend.py
  budget.py
  config.py
  consolidate.py
  cycle.py
  dream.py
  evalkit.py
  evidence.py
  gate.py
  handoff_backend.py
  harvest.py
  harvest_codex.py
  harvest_copilot.py
  harvest_copilot_cli.py
  harvest_cursor.py
  harvest_opencode.py
  harvest_pi.py
  harvest_sources.py
  judges.py
  llm_miner.py
  memory.py
  mine.py
  … 11 more files
skillopt_webui/  (3 files)
  __init__.py
  __main__.py
  app.py
tests/  (135 files)
  fixtures/  (14 files)
    copilot/  (2 files)
      … 2 files under this directory
    evalkit/  (4 files)
      … 4 files under this directory
    reproducibility/  (8 files)
      … 8 files under this directory
  PREFERENCE_SCOPE_MATRIX_154.md
  __init__.py
  test_aggregate_fallback.py
  test_alfworld_paths.py
  test_alfworld_task_output_confinement.py
  test_azure_openai_compat.py
  test_azure_usage_accounting.py
  test_backend_opencode.py
  test_backend_opencode_live.py
  test_backend_pi.py
  test_benchmark_task_output_paths.py
  test_claude_backend_tempdir.py
  test_claude_code_backend.py
  test_claude_code_exec_resolution.py
  test_claude_replay_isolation.py
  test_cli_backend_cache.py
  test_cli_path_resolution.py
  test_codex_cli_prompt_stdin.py
  test_codex_config_aliases.py
  test_codex_optimizer_backend.py
  test_console_encoding.py
  test_consolidate_split.py
  test_consolidation_edit_bookkeeping.py
  test_copilot_exec_backend.py
  … 97 more files
.env.example
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
index.html
mkdocs.yml
pyproject.toml
requirements.txt
skillopt.html
```

## Entry points

- [plugins/copilot/mcp_server.py:387](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/plugins/copilot/mcp_server.py#L387)
- [plugins/copilot/skillopt/mcp_server.py:228](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/plugins/copilot/skillopt/mcp_server.py#L228)
- [plugins/devin/harvest_devin.py:532](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/plugins/devin/harvest_devin.py#L532)
- [plugins/devin/judge.py:128](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/plugins/devin/judge.py#L128)
- [plugins/devin/mcp_server.py:429](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/plugins/devin/mcp_server.py#L429)
- [plugins/dsh/scripts/sleep.py:118](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/plugins/dsh/scripts/sleep.py#L118)
- [plugins/openclaw/run_sleep.py:144](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/plugins/openclaw/run_sleep.py#L144)
- [plugins/openclaw/slash_sleep.py:330](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/plugins/openclaw/slash_sleep.py#L330)
- [scripts/check_reproducibility.py:32](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/scripts/check_reproducibility.py#L32)
- [scripts/eval_only.py](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/scripts/eval_only.py)
- [scripts/materialize_searchqa.py:169](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/scripts/materialize_searchqa.py#L169)
- [scripts/train.py](https://github.com/microsoft/SkillOpt/blob/45f65ca04f5f6713bca7b9797b495696ba812751/scripts/train.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 44 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigError, SleepConfig. Observed top-level functions: _cast_value, _deep_merge, _d… |
| Application entry point | entrypoint | Observed | Groups 22 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BootstrapCI, EngineResult, EvalReport, EvalResults, EvalkitError, McNemarResult. Observed… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 17 file(s) under plugins package (observed from repository paths and static analysis). Observed top-level classes: OpenClawDeepSeekBackend. Observed top-level functions: _chat, _embed. |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| skillopt package | library | Observed | Groups 87 file(s) under skillopt package (observed from repository paths and static analysis). Observed top-level classes: ALFWorldAdapter, ALFWorldBatchRun, ALFWorldDataLoader, AutonomousScheduler, BaseDataLoader, Batc… |
| skillopt_sleep package | library | Observed | Groups 35 file(s) under skillopt_sleep package (observed from repository paths and static analysis). Observed top-level classes: AdoptedSkill, AzureOpenAIBackend, AzureResponsesBackend, Backend, Budget, ClaudeCliBackend… |
| skillopt_webui package | library | Observed | Groups 1 file(s) under skillopt_webui package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 144 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH skillopt.model.codex_harness.subprocess.run, PATCH skillopt.model.codex_harness.subprocess.run, PATCH sys.platf… |

## Important files

- `.cursor-plugin/marketplace.json` (config)
- `.env.example` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `configs/_base_/default.yaml` (config)
- `configs/alfworld/default.yaml` (config)
- `configs/docvqa/default.yaml` (config)
- `configs/features/soft_gate.yaml` (config)
- `configs/livemathematicianbench/default.yaml` (config)
- `configs/officeqa/default.yaml` (config)
- `configs/searchqa/default.yaml` (config)
- `configs/spreadsheetbench/default.yaml` (config)
- `data/alfworld_path_split/split_manifest.json` (config)
- `data/alfworld_path_split/train/items.json` (config)
- `data/alfworld_path_split/val/items.json` (config)
- `data/docvqa_id_split/split_manifest.json` (config)
- `data/docvqa_id_split/train/items.json` (config)
- `data/docvqa_id_split/val/items.json` (config)
- `data/livemathematicianbench_id_split/split_manifest.json` (config)
- `data/livemathematicianbench_id_split/train/items.json` (config)
- `data/livemathematicianbench_id_split/val/items.json` (config)
- `data/officeqa_id_split/split_manifest.json` (config)
- `data/officeqa_id_split/train/items.json` (config)
- `data/officeqa_id_split/val/items.json` (config)
- `data/searchqa_id_split/split_manifest.json` (config)
- `data/searchqa_id_split/train/items.json` (config)
- `data/searchqa_id_split/val/items.json` (config)
- `data/spreadsheetbench_id_split/split_manifest.json` (config)
- `data/spreadsheetbench_id_split/train/items.json` (config)
- `data/spreadsheetbench_id_split/val/items.json` (config)
- `mkdocs.yml` (config)
- `plugins/claude-code/.claude-plugin/marketplace.json` (config)
- `plugins/claude-code/.claude-plugin/plugin.json` (config)
- `plugins/claude-code/hooks/hooks.json` (config)
- `plugins/copilot/mcp-config.example.json` (config)
- `plugins/copilot/skillopt/mcp-config.example.json` (config)
- `plugins/cursor/.cursor-plugin/plugin.json` (config)
- `plugins/devin/fixtures/devin_sample.json` (config)
- `plugins/devin/hooks/hooks.v1.json` (config)
- `plugins/devin/mcp-config.example.json` (config)
- `plugins/dsh/cordis.patch.yml` (config)
- `plugins/dsh/package.json` (manifest)
- `plugins/openclaw/config.json` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `skillopt/envs/_template/config_template.yaml` (config)

## Top-level layout

- `skillopt` — 139 analysed file(s)
- `tests` — 135 analysed file(s)
- `plugins` — 67 analysed file(s)
- `skillopt_sleep` — 45 analysed file(s)
- `docs` — 26 analysed file(s)
- `data` — 25 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `scripts` — 9 analysed file(s)
- `configs` — 8 analysed file(s)
- `ckpt` — 7 analysed file(s)
- `skillopt_webui` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `blog` — 2 analysed file(s)
- `.cursor-plugin` — 1 analysed file(s)
- `skillopt-assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 8 file(s) were skipped during inventory (8 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `45f65ca04f5f6713bca7b9797b495696ba812751` is the revision these paths and observations refer to.
