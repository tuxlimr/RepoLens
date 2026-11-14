# Project structure: AntonOsika/gpt-engineer

**Analysed commit:** `a90fcd543eedcc0ff2c34561bc0785d2ba83c47e`

**Commit reference:** [a90fcd543eedcc0ff2c34561bc0785d2ba83c47e](https://github.com/AntonOsika/gpt-engineer/commit/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e)

**Tree at this commit:** [AntonOsika/gpt-engineer@a90fcd543eed](https://github.com/AntonOsika/gpt-engineer/tree/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | AntonOsika/gpt-engineer |
| Description | CLI platform to experiment with codegen. Precursor to: https://lovable.dev |
| Stars | 54957 |
| Forks | 7264 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `a90fcd543eedcc0ff2c34561bc0785d2ba83c47e` |
| Retrieved at | 2026-11-14T19:06:29.145661+00:00 |
| Files in this snapshot | 179 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    documentation-clarification.md
    feature-request.md
  PULL_REQUEST_TEMPLATE/  (1 files)
    PULL_REQUEST_TEMPLATE.md
  workflows/  (4 files)
    automation.yml
    ci.yaml
    pre-commit.yaml
    release.yaml
  CODEOWNERS
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
docker/  (3 files)
  Dockerfile
  README.md
  entrypoint.sh
docs/  (21 files)
  examples/  (3 files)
    open_llms/  (3 files)
      … 3 files under this directory
  Makefile
  api_reference.rst
  code_conduct_link.rst
  conf.py
  contributing_link.rst
  create_api_rst.py
  disclaimer_link.rst
  docs_building.md
  index.rst
  installation.rst
  introduction.md
  make.bat
  open_models.md
  quickstart.rst
  roadmap_link.rst
  terms_link.rst
  tracing_debugging.md
  windows_readme_link.rst
gpt_engineer/  (57 files)
  applications/  (7 files)
    cli/  (6 files)
      … 6 files under this directory
    __init__.py
  benchmark/  (14 files)
    benchmarks/  (8 files)
      … 8 files under this directory
    __init__.py
    __main__.py
    bench_config.py
    default_bench_config.toml
    run.py
    types.py
  core/  (23 files)
    default/  (8 files)
      … 8 files under this directory
    __init__.py
    ai.py
    base_agent.py
    base_execution_env.py
    base_memory.py
    chat_to_files.py
    diff.py
    files_dict.py
    git.py
    linting.py
    preprompts_holder.py
    project_config.py
    prompt.py
    token_usage.py
    version_manager.py
  preprompts/  (9 files)
    clarify
    entrypoint
    file_format
    file_format_diff
    file_format_fix
    generate
    improve
    philosophy
    roadmap
  tools/  (3 files)
    __init__.py
    custom_steps.py
    supported_languages.py
  __init__.py
projects/  (11 files)
  example/  (1 files)
    prompt
  example-improve/  (8 files)
    README.md
    controller.py
    main.py
    model.py
    prompt
    requirements.txt
    run.sh
    view.py
  example-vision/  (2 files)
    navigation.html
    prompt
scripts/  (4 files)
  clean_benchmarks.py
  legacy_benchmark.py
  print_chat.py
  test_api.py
tests/  (51 files)
  applications/  (7 files)
    cli/  (6 files)
      … 6 files under this directory
    __init__.py
  benchmark/  (1 files)
    test_BenchConfig.py
  core/  (37 files)
    default/  (5 files)
      … 5 files under this directory
    improve_function_test_cases/  (25 files)
      … 25 files under this directory
    __init__.py
    test_ai.py
    test_chat_to_files.py
    test_file_selector_enhancements.py
    test_git.py
    test_salvage_correct_hunks.py
    test_token_usage.py
  tools/  (1 files)
    example_snake_files.py
  __init__.py
  ai_cache.json
  mock_ai.py
  test_install.py
  test_project_config.py
.dockerignore
.env.template
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
Acknowledgements.md
DISCLAIMER.md
GOVERNANCE.md
LICENSE
MANIFEST.in
Makefile
README.md
ROADMAP.md
TERMS_OF_USE.md
WINDOWS_README.md
citation.cff
docker-compose.yml
pyproject.toml
sweep.yaml
tox.ini
```

## Entry points

- [gpt_engineer/applications/cli/main.py:66](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/gpt_engineer/applications/cli/main.py#L66)
- [gpt_engineer/benchmark/__main__.py:38](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/gpt_engineer/benchmark/__main__.py#L38)
- [projects/example-improve/main.py:17](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/projects/example-improve/main.py#L17)
- [scripts/clean_benchmarks.py:42](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/scripts/clean_benchmarks.py#L42)
- [scripts/legacy_benchmark.py:225](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/scripts/legacy_benchmark.py#L225)
- [scripts/print_chat.py:12](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/scripts/print_chat.py#L12)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Game, Point. |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level functions: ask_yes_no, compare, concatenate_paths, e… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| gpt_engineer package | library | Observed | Groups 21 file(s) under gpt_engineer package (observed from repository paths and static analysis). Observed top-level classes: AppsAssertion, AppsConfig, Assertable, BenchConfig, Benchmark, CliAgent. Observed top-level… |
| projects package | library | Observed | Groups 3 file(s) under projects package (observed from repository paths and static analysis). Observed top-level classes: Controller, View. |
| Service / domain layer | service | Observed | Groups 23 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AI, BaseAgent, BaseExecutionEnv, BaseVersionManager, ClipboardAI, Config. Observed top-lev… |
| Tests | test | Observed | Groups 52 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: DefaultArgumentsMain, MockAI, TestBenchConfig, TestGenCode, TestGenEntrypoint, TestImprove. Observed top-le… |

## Important files

- `.dockerignore` (container)
- `.env.template` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/automation.yml` (ci)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/pre-commit.yaml` (ci)
- `.github/workflows/release.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `docker-compose.yml` (container)
- `docker/Dockerfile` (container)
- `gpt_engineer/benchmark/default_bench_config.toml` (config)
- `projects/example-improve/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `sweep.yaml` (config)
- `tox.ini` (config)

## Top-level layout

- `gpt_engineer` — 57 analysed file(s)
- `tests` — 51 analysed file(s)
- `docs` — 21 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 12 analysed file(s)
- `projects` — 11 analysed file(s)
- `scripts` — 4 analysed file(s)
- `docker` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `a90fcd543eedcc0ff2c34561bc0785d2ba83c47e` is the revision these paths and observations refer to.
