# Project structure: ayghri/i-have-adhd

**Analysed commit:** `1ecea1993b7fce257ffbd686c070948b5e07eda6`

**Commit reference:** [1ecea1993b7fce257ffbd686c070948b5e07eda6](https://github.com/ayghri/i-have-adhd/commit/1ecea1993b7fce257ffbd686c070948b5e07eda6)

**Tree at this commit:** [ayghri/i-have-adhd@1ecea1993b7f](https://github.com/ayghri/i-have-adhd/tree/1ecea1993b7fce257ffbd686c070948b5e07eda6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ayghri/i-have-adhd |
| Description | A skill to stop your coding agent from burying the answer. ADHD-friendly output. |
| Stars | 61183 |
| Forks | 3587 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `1ecea1993b7fce257ffbd686c070948b5e07eda6` |
| Retrieved at | 2026-11-14T19:06:20.928338+00:00 |
| Files in this snapshot | 73 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.codex-plugin/  (1 files)
  plugin.json
.cursor/  (1 files)
  skills/  (1 files)
    i-have-adhd/  (1 files)
      … 1 files under this directory
.github/  (24 files)
  install/  (8 files)
    INSTALL.ar.md
    INSTALL.fa.md
    INSTALL.id.md
    INSTALL.ja.md
    INSTALL.ko.md
    INSTALL.pt-BR.md
    INSTALL.vi.md
    INSTALL.zh-CN.md
  readme/  (11 files)
    README.ar.md
    README.es.md
    README.fa.md
    README.fr.md
    README.id.md
    README.ja.md
    README.ko.md
    README.pt-BR.md
    README.th.md
    README.vi.md
    README.zh-CN.md
  workflows/  (4 files)
    claude.yml
    cursor-skill-sync.yml
    pi-load-check.yml
    plugin-load-check.yml
  pull_request_template.md
.opencode/  (3 files)
  command/  (1 files)
    i-have-adhd.md
  plugins/  (2 files)
    i-have-adhd.js
    i-have-adhd.mjs
evals/  (7 files)
  scenarios/  (2 files)
    persistence-topic-switch-stop/  (2 files)
      … 2 files under this directory
  README.md
  RESULTS.md
  cases.jsonl
  rubric.md
  runners.example.json
extensions/  (2 files)
  context-compat.ts
  i-have-adhd.ts
hooks/  (4 files)
  always-on.mjs
  always-on.ps1
  always-on.sh
  hooks.json
scripts/  (5 files)
  check_context_compat.ts
  check_pi_extension.py
  judge.py
  run_evals.py
  run_scenario_eval.py
skills/  (3 files)
  i-have-adhd/  (3 files)
    agents/  (2 files)
      … 2 files under this directory
    SKILL.md
tests/  (8 files)
  opencode_plugin_driver.mjs
  test_always_on_hooks.py
  test_install_docs.py
  test_judge.py
  test_omp_package.py
  test_opencode_plugin.py
  test_run_evals.py
  test_run_scenario_eval.py
.gitignore
AGENTS.md
CONTRIBUTING.md
GEMINI.md
INSTALL.md
LICENSE
README.md
gemini-extension.json
kimi.plugin.json
package.json
plugin.json
qwen-extension.json
```

## Entry points

- [scripts/check_pi_extension.py:427](https://github.com/ayghri/i-have-adhd/blob/1ecea1993b7fce257ffbd686c070948b5e07eda6/scripts/check_pi_extension.py#L427)
- [scripts/judge.py:333](https://github.com/ayghri/i-have-adhd/blob/1ecea1993b7fce257ffbd686c070948b5e07eda6/scripts/judge.py#L333)
- [scripts/run_evals.py:550](https://github.com/ayghri/i-have-adhd/blob/1ecea1993b7fce257ffbd686c070948b5e07eda6/scripts/run_evals.py#L550)
- [scripts/run_scenario_eval.py:168](https://github.com/ayghri/i-have-adhd/blob/1ecea1993b7fce257ffbd686c070948b5e07eda6/scripts/run_scenario_eval.py#L168)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: RpcClient. Observed top-level functions: _build_parser, _check_pairing, _condition_prompt,… |
| extensions package | library | Observed | Groups 2 file(s) under extensions package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 2 file(s) under hooks package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH run_scenario_eval.subprocess.run, PATCH run_scenario_eval.subprocess.run, PATCH run_scenario_eval.subprocess.run,… |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.github/workflows/claude.yml` (ci)
- `.github/workflows/cursor-skill-sync.yml` (ci)
- `.github/workflows/pi-load-check.yml` (ci)
- `.github/workflows/plugin-load-check.yml` (ci)
- `evals/runners.example.json` (config)
- `gemini-extension.json` (config)
- `hooks/hooks.json` (config)
- `kimi.plugin.json` (config)
- `package.json` (manifest)
- `plugin.json` (config)
- `qwen-extension.json` (config)
- `skills/i-have-adhd/agents/gemini.toml` (config)
- `skills/i-have-adhd/agents/openai.yaml` (config)

## Top-level layout

- `.github` — 24 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `tests` — 8 analysed file(s)
- `evals` — 7 analysed file(s)
- `scripts` — 5 analysed file(s)
- `hooks` — 4 analysed file(s)
- `.opencode` — 3 analysed file(s)
- `skills` — 3 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `extensions` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)
- `.cursor` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1ecea1993b7fce257ffbd686c070948b5e07eda6` is the revision these paths and observations refer to.
