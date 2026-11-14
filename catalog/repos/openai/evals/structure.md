# Project structure: openai/evals

**Analysed commit:** `8eac7a7de5215c907fbddc30efdaf316913eccdd`

**Commit reference:** [8eac7a7de5215c907fbddc30efdaf316913eccdd](https://github.com/openai/evals/commit/8eac7a7de5215c907fbddc30efdaf316913eccdd)

**Tree at this commit:** [openai/evals@8eac7a7de521](https://github.com/openai/evals/tree/8eac7a7de5215c907fbddc30efdaf316913eccdd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/evals |
| Description | Evals is a framework for evaluating LLMs and LLM systems, and an open-source registry of benchmarks. |
| Stars | 19743 |
| Forks | 3133 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `8eac7a7de5215c907fbddc30efdaf316913eccdd` |
| Retrieved at | 2026-11-14T19:08:07.688741+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    feature_request.yml
  workflows/  (3 files)
    parse_yaml.py
    run_tests.yaml
    test_eval.yaml
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
  config.yml
docs/  (6 files)
  build-eval.md
  completion-fn-protocol.md
  completion-fns.md
  custom-eval.md
  eval-templates.md
  run-evals.md
evals/  (778 files)
  cli/  (2 files)
    oaieval.py
    oaievalset.py
  completion_fns/  (7 files)
    __init__.py
    cot.py
    langchain_llm.py
    langchain_math.py
    openai.py
    retrieval.py
    solver_completion_fn.py
  elsuite/  (385 files)
    already_said_that/  (11 files)
      … 11 files under this directory
    ballots/  (7 files)
      … 7 files under this directory
    basic/  (11 files)
      … 11 files under this directory
    bluff/  (14 files)
      … 14 files under this directory
    bugged_tools/  (8 files)
      … 8 files under this directory
    cant_do_that_anymore/  (14 files)
      … 14 files under this directory
    error_recovery/  (6 files)
      … 6 files under this directory
    function_deduction/  (10 files)
      … 10 files under this directory
    hr_ml_agent_bench/  (106 files)
      … 106 files under this directory
    identifying_variables/  (22 files)
      … 22 files under this directory
    make_me_pay/  (12 files)
      … 12 files under this directory
    make_me_say/  (7 files)
      … 7 files under this directory
    mmmu/  (1 files)
      … 1 files under this directory
    modelgraded/  (3 files)
      … 3 files under this directory
    multistep_web_tasks/  (61 files)
      … 61 files under this directory
    sandbagging/  (13 files)
      … 13 files under this directory
    schelling_point/  (4 files)
      … 4 files under this directory
    self_prompting/  (9 files)
      … 9 files under this directory
    skill_acquisition/  (11 files)
      … 11 files under this directory
    steganography/  (15 files)
      … 15 files under this directory
    test/  (1 files)
      … 1 files under this directory
    text_compression/  (14 files)
      … 14 files under this directory
    theory_of_mind/  (4 files)
      … 4 files under this directory
    track_the_stat/  (9 files)
      … 9 files under this directory
    twenty_questions/  (6 files)
      … 6 files under this directory
    lambada.py
    multiple_choice.py
    solver_tools_convo.py
    translate.py
    utils.py
    utils_test.py
  prompt/  (1 files)
    base.py
  registry/  (372 files)
    completion_fns/  (3 files)
      … 3 files under this directory
    data/  (369 files)
      … 369 files under this directory
  __init__.py
  api.py
  base.py
  data.py
  data_test.py
  eval.py
  formatting.py
  metrics.py
  record.py
  record_test.py
  registry.py
.gitattributes
.gitignore
.pre-commit-config.yaml
LICENSE.md
MANIFEST.in
Makefile
README.md
SECURITY.md
```

## Entry points

- [.github/workflows/parse_yaml.py:13](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/.github/workflows/parse_yaml.py#L13)
- [evals/cli/oaieval.py:310](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/cli/oaieval.py#L310)
- [evals/cli/oaievalset.py:140](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/cli/oaievalset.py#L140)
- [evals/elsuite/already_said_that/distractors.py:130](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/elsuite/already_said_that/distractors.py#L130)
- [evals/elsuite/already_said_that/scripts/gen_data.py:59](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/elsuite/already_said_that/scripts/gen_data.py#L59)
- [evals/elsuite/already_said_that/scripts/make_plots.py:319](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/elsuite/already_said_that/scripts/make_plots.py#L319)
- [evals/elsuite/ballots/scripts/make_plots.py:298](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/elsuite/ballots/scripts/make_plots.py#L298)
- [evals/elsuite/bluff/scripts/make_plots.py:140](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/elsuite/bluff/scripts/make_plots.py#L140)
- [evals/elsuite/bugged_tools/bugged_tools.py:156](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/elsuite/bugged_tools/bugged_tools.py#L156)
- [evals/elsuite/bugged_tools/scripts/plot_experiments.py:137](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/elsuite/bugged_tools/scripts/plot_experiments.py#L137)
- [evals/elsuite/cant_do_that_anymore/chess/board_test.py:94](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/elsuite/cant_do_that_anymore/chess/board_test.py#L94)
- [evals/elsuite/cant_do_that_anymore/scripts/dataset_creation.py:273](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/evals/elsuite/cant_do_that_anymore/scripts/dataset_creation.py#L273)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: MockApi. Observed top-level functions: generate_binary_array_and_factors, generate_combinations, genera… |
| Application entry point | entrypoint | Observed | Groups 50 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /setup, ROUTE /shutdown, ROUTE /exec_c… |
| evals package | library | Observed | Groups 252 file(s) under evals package (observed from repository paths and static analysis). Observed top-level classes: AccTreeBrowserObservation, AccessibilityTreeNode, Action, ActionInfo, ActionParsingError, Agent. O… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: ClientForwarder, Forwarder, KeyboardForwarder, MouseForwarder, PageForwarder, ViewportSize. |
| Service / domain layer | service | Observed | Groups 2 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: Action, BashBrowserExperimentConfig, BashExperimentConfig, BrowserExperimentConfig, DummyOb… |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: MyDataClass, MyPydanticClass, TestMatch. Observed top-level functions: _is_api_key_set, ambiguous_sentences… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/config.yml` (config)
- `.github/workflows/parse_yaml.py` (ci)
- `.github/workflows/run_tests.yaml` (ci)
- `.github/workflows/test_eval.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `evals/elsuite/hr_ml_agent_bench/benchmarks/bipedal_walker/scripts/requirements.txt` (manifest)
- `evals/elsuite/hr_ml_agent_bench/benchmarks/cartpole/scripts/requirements.txt` (manifest)
- `evals/elsuite/hr_ml_agent_bench/benchmarks/cifar10/scripts/requirements.txt` (manifest)
- `evals/elsuite/hr_ml_agent_bench/benchmarks/humanoid/scripts/requirements.txt` (manifest)
- `evals/elsuite/hr_ml_agent_bench/benchmarks/imdb/scripts/requirements.txt` (manifest)
- `evals/elsuite/hr_ml_agent_bench/benchmarks/ogbn_arxiv/scripts/requirements.txt` (manifest)
- `evals/elsuite/hr_ml_agent_bench/benchmarks/spaceship_titanic/scripts/requirements.txt` (manifest)
- `evals/elsuite/hr_ml_agent_bench/devcontainer.json` (config)
- `evals/elsuite/hr_ml_agent_bench/requirements.txt` (manifest)
- `evals/elsuite/multistep_web_tasks/docker/dc-evals-bash/Dockerfile` (container)
- `evals/elsuite/multistep_web_tasks/docker/flask-playwright/Dockerfile` (container)
- `evals/elsuite/multistep_web_tasks/docker/homepage/Dockerfile` (container)
- `evals/elsuite/multistep_web_tasks/docker/homepage/requirements.txt` (manifest)
- `evals/elsuite/multistep_web_tasks/reproducibility/all_tasks.json` (config)
- `evals/elsuite/multistep_web_tasks/webarena/.auth/gitlab.reddit_state.json` (config)
- `evals/elsuite/multistep_web_tasks/webarena/.auth/gitlab.shopping_admin_state.json` (config)
- `evals/elsuite/multistep_web_tasks/webarena/.auth/gitlab.shopping_state.json` (config)
- `evals/elsuite/multistep_web_tasks/webarena/.auth/gitlab_state.json` (config)
- `evals/elsuite/multistep_web_tasks/webarena/.auth/reddit_state.json` (config)
- `evals/elsuite/multistep_web_tasks/webarena/.auth/shopping.shopping_admin_state.json` (config)
- `evals/elsuite/multistep_web_tasks/webarena/.auth/shopping_admin_state.json` (config)
- `evals/elsuite/multistep_web_tasks/webarena/.auth/shopping_state.json` (config)
- `evals/elsuite/steganography/scripts/dataset/requirements.txt` (manifest)
- `evals/elsuite/text_compression/scripts/dataset/requirements.txt` (manifest)
- `evals/registry/completion_fns/cot.yaml` (config)
- `evals/registry/completion_fns/langchain_chains.yaml` (config)
- `evals/registry/completion_fns/langchain_llms.yaml` (config)

## Top-level layout

- `evals` — 778 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 8 analysed file(s)
- `docs` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8eac7a7de5215c907fbddc30efdaf316913eccdd` is the revision these paths and observations refer to.
