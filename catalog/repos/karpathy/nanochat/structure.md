# Project structure: karpathy/nanochat

**Analysed commit:** `92d63d4e8bb4df75c3b71618f31ddde2378b2bcd`

**Commit reference:** [92d63d4e8bb4df75c3b71618f31ddde2378b2bcd](https://github.com/karpathy/nanochat/commit/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd)

**Tree at this commit:** [karpathy/nanochat@92d63d4e8bb4](https://github.com/karpathy/nanochat/tree/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | karpathy/nanochat |
| Description | The best ChatGPT that $100 can buy. |
| Stars | 60555 |
| Forks | 8500 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `92d63d4e8bb4df75c3b71618f31ddde2378b2bcd` |
| Retrieved at | 2026-11-14T19:06:22.449336+00:00 |
| Files in this snapshot | 50 |

## Directory tree

```text
.claude/  (1 files)
  skills/  (1 files)
    read-arxiv-paper/  (1 files)
      … 1 files under this directory
dev/  (5 files)
  LEADERBOARD.md
  LOG.md
  estimate_gpt3_core.ipynb
  repackage_data_reference.py
  scaling_analysis.ipynb
nanochat/  (14 files)
  __init__.py
  checkpoint_manager.py
  common.py
  core_eval.py
  dataloader.py
  dataset.py
  engine.py
  execution.py
  flash_attention.py
  fp8.py
  gpt.py
  loss_eval.py
  optim.py
  tokenizer.py
runs/  (4 files)
  miniseries.sh
  runcpu.sh
  scaling_laws.sh
  speedrun.sh
scripts/  (9 files)
  base_eval.py
  base_train.py
  chat_cli.py
  chat_eval.py
  chat_rl.py
  chat_sft.py
  infer_bench.py
  tok_eval.py
  tok_train.py
tasks/  (6 files)
  arc.py
  common.py
  gsm8k.py
  humaneval.py
  mmlu.py
  smoltalk.py
tests/  (6 files)
  test_attention_fallback.py
  test_engine.py
  test_execution.py
  test_optim.py
  test_tasks.py
  test_tokenizer.py
.gitignore
.python-version
LICENSE
README.md
pyproject.toml
```

## Entry points

- [nanochat/dataset.py:136](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/nanochat/dataset.py#L136)
- [nanochat/engine.py:302](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/nanochat/engine.py#L302)
- [scripts/base_eval.py:242](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/scripts/base_eval.py#L242)
- [scripts/chat_eval.py:178](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/scripts/chat_eval.py#L178)
- [scripts/infer_bench.py:245](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/scripts/infer_bench.py#L245)
- [tasks/common.py:209](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/tasks/common.py#L209)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dev package | library | Observed | Groups 1 file(s) under dev package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Engine, HubDataset, KVCache, RowState, Task, TaskMixture. Observed top-level functions: be… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| nanochat package | library | Observed | Groups 12 file(s) under nanochat package (observed from repository paths and static analysis). Observed top-level classes: Block, CausalSelfAttention, ColoredFormatter, DummyWandb, ExecutionResult, Float8Linear. Observe… |
| runs package | library | Observed | Groups 4 file(s) under runs package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: build_model_meta, disable_fp8, get_batch, get_lr_multiplier, get_muon_momentum, get_scaling_para… |
| tasks package | library | Observed | Groups 5 file(s) under tasks package (observed from repository paths and static analysis). Observed top-level classes: ARC, GSM8K, HumanEval, MMLU, SmolTalk. Observed top-level functions: extract_answer, extract_imports… |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ByteTokenizer, MockConfig, MockModel, TestFA3VsSDPA, TestOverrideMechanism, TestSDPAOnly. Observed top-level… |

## Important files

- `pyproject.toml` (manifest)

## Top-level layout

- `nanochat` — 14 analysed file(s)
- `scripts` — 9 analysed file(s)
- `tasks` — 6 analysed file(s)
- `tests` — 6 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `dev` — 5 analysed file(s)
- `runs` — 4 analysed file(s)
- `.claude` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `92d63d4e8bb4df75c3b71618f31ddde2378b2bcd` is the revision these paths and observations refer to.
