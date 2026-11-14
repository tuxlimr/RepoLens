# Project structure: vibrantlabsai/ragas

**Analysed commit:** `8c63f10d500c44efbf24fdb9e2920de2104c321c`

**Commit reference:** [8c63f10d500c44efbf24fdb9e2920de2104c321c](https://github.com/vibrantlabsai/ragas/commit/8c63f10d500c44efbf24fdb9e2920de2104c321c)

**Tree at this commit:** [vibrantlabsai/ragas@8c63f10d500c](https://github.com/vibrantlabsai/ragas/tree/8c63f10d500c44efbf24fdb9e2920de2104c321c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vibrantlabsai/ragas |
| Description | Supercharge Your LLM Application Evaluations 🚀 |
| Stars | 16320 |
| Forks | 1818 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `8c63f10d500c44efbf24fdb9e2920de2104c321c` |
| Retrieved at | 2026-11-14T19:08:53.166971+00:00 |
| Files in this snapshot | 641 |

## Directory tree

```text
.claude/  (2 files)
  commands/  (2 files)
    create-pr.md
    fix-github-issue.md
.cursor/  (8 files)
  commands/  (2 files)
    git-pr.md
    update-howto-guide.md
  rules/  (5 files)
    docs-diataxis-guidelines.mdc
    docs-structure.mdc
    project-structure.mdc
    update-guide.mdc
    use-uv-cli.mdc
  worktrees.json
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    question.md
  workflows/  (6 files)
    ci.yaml
    claude-code-review.yml
    claude-docs-check.yml
    claude.yml
    issue-manager.yaml
    python-publish.yml
  pull_request_template.md
docs/  (191 files)
  _static/  (17 files)
    css/  (7 files)
      … 7 files under this directory
    imgs/  (2 files)
      … 2 files under this directory
    js/  (5 files)
      … 5 files under this directory
    annotated_data.json
    edited_chain_runs.json
    sample_annotated_summary.json
  community/  (2 files)
    index.md
    pdf_export.md
  concepts/  (33 files)
    components/  (4 files)
      … 4 files under this directory
    feedback/  (1 files)
      … 1 files under this directory
    metrics/  (22 files)
      … 22 files under this directory
    test_data_generation/  (3 files)
      … 3 files under this directory
    datasets.md
    experimentation.md
    index.md
  extra/  (5 files)
    components/  (2 files)
      … 2 files under this directory
    overrides/  (1 files)
      … 1 files under this directory
    ragas-modern.css
    style.css
  getstarted/  (7 files)
    evals.md
    experiments_quickstart.md
    index.md
    install.md
    quickstart.md
    rag_eval.md
    rag_testset_generation.md
  howtos/  (96 files)
    applications/  (17 files)
      … 17 files under this directory
    cli/  (10 files)
      … 10 files under this directory
    customizations/  (22 files)
      … 22 files under this directory
    integrations/  (42 files)
      … 42 files under this directory
    migrations/  (2 files)
      … 2 files under this directory
    index.md
    llm-adapters.md
    observability.md
  references/  (19 files)
    aevaluate.md
    cache.md
    embeddings.md
    evaluate.md
    evaluation_schema.md
    executor.md
    generate.md
    graph.md
    index.md
    integrations.md
    llms.md
    metrics.md
    optimizers.md
    prompt.md
    run_config.md
    synthesizers.md
    testset_schema.md
    tokenizers.md
    transforms.md
  tutorials/  (5 files)
    agent.md
    index.md
    prompt.md
    rag.md
    workflow.md
  INSTALL
  Makefile
  alfred.py
  index.md
  ipynb_to_md.py
  make.bat
  quoted_spans_metric.md
examples/  (59 files)
  iterate_prompt/  (6 files)
    datasets/  (1 files)
      … 1 files under this directory
    __init__.py
    evals.py
    promptv1.txt
    promptv2_fewshot.txt
    run_prompt.py
  ragas_examples/  (47 files)
    ag_ui_agent_experiments/  (5 files)
      … 5 files under this directory
    agent_evals/  (3 files)
      … 3 files under this directory
    benchmark_llm/  (4 files)
      … 4 files under this directory
    improve_rag/  (5 files)
      … 5 files under this directory
    judge_alignment/  (2 files)
      … 2 files under this directory
    llamaIndex_agent_evals/  (6 files)
      … 6 files under this directory
    prompt_evals/  (3 files)
      … 3 files under this directory
    rag_eval/  (4 files)
      … 4 files under this directory
    text2sql/  (11 files)
      … 11 files under this directory
    workflow_eval/  (3 files)
      … 3 files under this directory
    __init__.py
  LICENSE
  README.md
  gdrive_append_example.py
  gdrive_backend_example.py
  oci_genai_example.py
  pyproject.toml
scripts/  (1 files)
  dev_docs.sh
src/  (242 files)
  ragas/  (242 files)
    backends/  (10 files)
      … 10 files under this directory
    embeddings/  (8 files)
      … 8 files under this directory
    integrations/  (15 files)
      … 15 files under this directory
    llms/  (9 files)
      … 9 files under this directory
    metrics/  (114 files)
      … 114 files under this directory
    optimizers/  (7 files)
      … 7 files under this directory
    prompt/  (23 files)
      … 23 files under this directory
    testset/  (33 files)
      … 33 files under this directory
    __init__.py
    _analytics.py
    _safe_fetch.py
    async_utils.py
    cache.py
    callbacks.py
    cli.py
    config.py
    cost.py
    dataset.py
    dataset_schema.py
    evaluation.py
    exceptions.py
    executor.py
    experiment.py
    losses.py
    messages.py
    py.typed
    run_config.py
    sdk.py
    tokenizers.py
    utils.py
    validation.py
tests/  (113 files)
  benchmarks/  (4 files)
    Dockerfile
    benchmark_eval.py
    benchmark_testsetgen.py
    utils.py
  docs/  (2 files)
    __init__.py
    test_run_config.py
  e2e/  (29 files)
    metrics_migration/  (21 files)
      … 21 files under this directory
    __init__.py
    test_adaptation.py
    test_amnesty_in_ci.py
    test_dataset_utils.py
    test_dspy_integration.py
    test_fullflow.py
    test_langchain_llm_attributes.py
    test_testset_generation.py
  unit/  (72 files)
    backends/  (4 files)
      … 4 files under this directory
    integrations/  (3 files)
      … 3 files under this directory
    llms/  (4 files)
      … 4 files under this directory
    prompt/  (5 files)
      … 5 files under this directory
    test_analytics.py
    test_async_evaluation.py
    test_async_utils.py
    test_average_precision_algorithm.py
    test_cache.py
    test_cancellation.py
    test_chrf_score.py
    test_chrf_score_collections.py
    test_cli.py
    test_cosine_relationship_builders.py
    test_cost.py
    test_datacompy_score_collections.py
    test_dataset_schema.py
    test_datatable_inheritance.py
    test_domain_specific_rubrics_collections.py
    test_dspy_adapter.py
    test_dspy_optimizer.py
    test_embeddings.py
    test_embeddings_caching.py
    test_engine.py
    test_executor.py
    test_executor_in_jupyter.ipynb
    test_experiment.py
    test_graph.py
    … 32 more files
  utils/  (3 files)
    __init__.py
    llm_setup.py
    metric_comparison.py
  __init__.py
  conftest.py
  test_quoted_spans.py
.dockerignore
.gitattributes
.gitignore
.pre-commit-config.yaml
.readthedocs.yml
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
SECURITY.md
mkdocs-pdf.yml
mkdocs.yml
pyproject.toml
```

## Entry points

- [src/ragas/cli.py](https://github.com/vibrantlabsai/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/src/ragas/cli.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: DemonstrationConfig, InstructionConfig. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level functions: calculate_aggregated_metrics, create_cate… |
| External integrations | external | Observed | Groups 19 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AGUIEventCollector, CacheConfig, EvaluatorChain, HeliconeSingleton, InstructorAdapter, Lang… |
| ragas package | library | Observed | Groups 217 file(s) under ragas package (observed from repository paths and static analysis). Observed top-level classes: AIMessage, AgentGoalAccuracyWithReference, AgentGoalAccuracyWithoutReference, AnalyticsBatcher, An… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 112 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH ragas.backends.gdrive_backend.build, PATCH ragas.backends.gdrive_backend.Credentials, PATCH os.path.exists, PAT… |

## Important files

- `.cursor/worktrees.json` (config)
- `.dockerignore` (container)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/claude-code-review.yml` (ci)
- `.github/workflows/claude-docs-check.yml` (ci)
- `.github/workflows/claude.yml` (ci)
- `.github/workflows/issue-manager.yaml` (ci)
- `.github/workflows/python-publish.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yml` (config)
- `docs/_static/annotated_data.json` (config)
- `docs/_static/edited_chain_runs.json` (config)
- `docs/_static/sample_annotated_summary.json` (config)
- `examples/pyproject.toml` (manifest)
- `examples/ragas_examples/improve_rag/pyproject.toml` (manifest)
- `examples/ragas_examples/llamaIndex_agent_evals/contexts/ambiguous_removal_request.json` (config)
- `examples/ragas_examples/llamaIndex_agent_evals/contexts/duplicate_addition.json` (config)
- `examples/ragas_examples/llamaIndex_agent_evals/contexts/repeated_removal.json` (config)
- `examples/ragas_examples/rag_eval/pyproject.toml` (manifest)
- `mkdocs-pdf.yml` (config)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)
- `tests/benchmarks/Dockerfile` (container)

## Top-level layout

- `src` — 242 analysed file(s)
- `docs` — 191 analysed file(s)
- `tests` — 113 analysed file(s)
- `examples` — 59 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 10 analysed file(s)
- `.cursor` — 8 analysed file(s)
- `.claude` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8c63f10d500c44efbf24fdb9e2920de2104c321c` is the revision these paths and observations refer to.
