# Project structure: p-e-w/heretic

**Analysed commit:** `a14b8543537b50ce8db4db7eaae4eb295d5d5142`

**Commit reference:** [a14b8543537b50ce8db4db7eaae4eb295d5d5142](https://github.com/p-e-w/heretic/commit/a14b8543537b50ce8db4db7eaae4eb295d5d5142)

**Tree at this commit:** [p-e-w/heretic@a14b8543537b](https://github.com/p-e-w/heretic/tree/a14b8543537b50ce8db4db7eaae4eb295d5d5142)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | p-e-w/heretic |
| Description | Training-free language model modification: Remove censorship, suppress slop, reduce sycophancy, and more |
| Stars | 40595 |
| Forks | 4659 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `a14b8543537b50ce8db4db7eaae4eb295d5d5142` |
| Retrieved at | 2026-11-14T19:06:42.564151+00:00 |
| Files in this snapshot | 95 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  pull_request_template.md
docs/  (1 files)
  migration_v1_to_v2.md
src/  (21 files)
  heretic/  (21 files)
    modifiers/  (3 files)
      … 3 files under this directory
    scorers/  (6 files)
      … 6 files under this directory
    __init__.py
    config.py
    evaluator.py
    main.py
    model.py
    modifier.py
    plugin.py
    progress.py
    reproduce.py
    scorer.py
    system.py
    utils.py
tests/  (57 files)
  deepseek-v4/  (7 files)
    SHA256SUMS.ci
    SHA256SUMS.ci2
    SHA256SUMS.ci3
    SHA256SUMS.ci4
    SHA256SUMS.linux
    SHA256SUMS.windows
    config.toml
  deepseek-v4-ara/  (5 files)
    SHA256SUMS.ci
    SHA256SUMS.ci2
    SHA256SUMS.ci3
    SHA256SUMS.ci4
    config.toml
  gemma-3/  (5 files)
    SHA256SUMS.ci
    SHA256SUMS.ci2
    SHA256SUMS.ci3
    SHA256SUMS.windows
    config.toml
  gemma-4e/  (6 files)
    SHA256SUMS.ci
    SHA256SUMS.ci2
    SHA256SUMS.ci3
    SHA256SUMS.linux
    SHA256SUMS.windows
    config.toml
  gpt-oss/  (3 files)
    SHA256SUMS.linux
    SHA256SUMS.windows
    config.toml
  minicpm5/  (3 files)
    SHA256SUMS.linux
    SHA256SUMS.windows
    config.toml
  mistral-3/  (6 files)
    SHA256SUMS.ci
    SHA256SUMS.ci2
    SHA256SUMS.ci3
    SHA256SUMS.linux
    SHA256SUMS.windows
    config.toml
  qwen2.5/  (4 files)
    SHA256SUMS.ci
    SHA256SUMS.linux
    SHA256SUMS.windows
    config.toml
  qwen3.5-moe/  (5 files)
    SHA256SUMS.ci
    SHA256SUMS.ci2
    SHA256SUMS.linux
    SHA256SUMS.windows
    config.toml
  seed-oss/  (5 files)
    SHA256SUMS.ci
    SHA256SUMS.ci2
    SHA256SUMS.linux
    SHA256SUMS.windows
    config.toml
  README.md
  run_tests.py
  test_ara_lowrank_equivalence.py
  test_chat_template.py
  test_config.py
  test_keyword_rate.py
  test_plugin.py
  test_residual_streams.py
.gitattributes
.gitignore
.python-version
LICENSE
README.md
config.classifier.toml
config.default.toml
config.emotions.toml
config.nohumor.toml
config.noslop.toml
config.nosyco.toml
config.piqa.toml
config.terse.toml
pyproject.toml
```

## Entry points

- [src/heretic/main.py](https://github.com/p-e-w/heretic/blob/a14b8543537b50ce8db4db7eaae4eb295d5d5142/src/heretic/main.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BenchmarkSpecification, ExportStrategy, InitOnlySettings, ModifierConfig, Quantizati… |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Model. Observed top-level functions: _collapse_flattened_residual_streams, chat_template_supports_syste… |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _is_help_invocation, main, obtain_export_strategy, run. |
| heretic package | library | Observed | Groups 18 file(s) under heretic package (observed from repository paths and static analysis). Observed top-level classes: ARA, Abliteration, BERTClassifier, BenchmarkScore, Context, Evaluator. Observed top-level functio… |
| Tests | test | Observed | Groups 57 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ApplySystemRoleTests, ChatTemplateSupportTests, ConfigFileSelectionTests, DummyNestedSettings, DummyPlugin,… |

## Important files

- `.github/workflows/ci.yml` (ci)
- `config.classifier.toml` (config)
- `config.default.toml` (config)
- `config.emotions.toml` (config)
- `config.nohumor.toml` (config)
- `config.noslop.toml` (config)
- `config.nosyco.toml` (config)
- `config.piqa.toml` (config)
- `config.terse.toml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 57 analysed file(s)
- `src` — 21 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 2 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a14b8543537b50ce8db4db7eaae4eb295d5d5142` is the revision these paths and observations refer to.
