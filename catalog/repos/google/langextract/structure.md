# Project structure: google/langextract

**Analysed commit:** `0e441bf77ddc3119dd0aa413322959234dd84ee5`

**Commit reference:** [0e441bf77ddc3119dd0aa413322959234dd84ee5](https://github.com/google/langextract/commit/0e441bf77ddc3119dd0aa413322959234dd84ee5)

**Tree at this commit:** [google/langextract@0e441bf77ddc](https://github.com/google/langextract/tree/0e441bf77ddc3119dd0aa413322959234dd84ee5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google/langextract |
| Description | A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization. |
| Stars | 39310 |
| Forks | 2750 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `0e441bf77ddc3119dd0aa413322959234dd84ee5` |
| Retrieved at | 2026-11-14T19:06:45.797102+00:00 |
| Files in this snapshot | 148 |

## Directory tree

```text
.github/  (22 files)
  ISSUE_TEMPLATE/  (3 files)
    1-bug.md
    2-feature-request.md
    config.yml
  PULL_REQUEST_TEMPLATE/  (1 files)
    pull_request_template.md
  scripts/  (5 files)
    add-new-checks.sh
    add-size-labels.sh
    pr_security_check.py
    revalidate-all-prs.sh
    zenodo_publish.py
  workflows/  (12 files)
    auto-update-pr.yaml
    check-infrastructure-changes.yml
    check-linked-issue.yml
    check-pr-security.yml
    check-pr-size.yml
    check-pr-up-to-date.yaml
    ci.yaml
    publish.yml
    revalidate-pr.yml
    validate-community-providers.yaml
    validate_pr_template.yaml
    zenodo-publish.yml
  CODEOWNERS
benchmarks/  (5 files)
  benchmark.py
  config.py
  fuzzy_benchmark.py
  plotting.py
  utils.py
docs/  (7 files)
  _static/  (2 files)
    langextract_concept.html
    logo.svg
  examples/  (5 files)
    batch_api_example.md
    japanese_extraction.md
    longer_text_example.md
    medication_examples.md
    output_schema.md
examples/  (12 files)
  custom_provider_plugin/  (6 files)
    langextract_provider_example/  (3 files)
      … 3 files under this directory
    README.md
    pyproject.toml
    test_example_provider.py
  notebooks/  (1 files)
    romeo_juliet_extraction.ipynb
  ollama/  (5 files)
    .dockerignore
    Dockerfile
    README.md
    demo_ollama.py
    docker-compose.yml
langextract/  (49 files)
  _compat/  (6 files)
    README.md
    __init__.py
    exceptions.py
    inference.py
    registry.py
    schema.py
  core/  (10 files)
    __init__.py
    base_model.py
    data.py
    debug_utils.py
    exceptions.py
    format_handler.py
    output_schema.py
    schema.py
    tokenizer.py
    types.py
  providers/  (13 files)
    schemas/  (3 files)
      … 3 files under this directory
    README.md
    __init__.py
    builtin_registry.py
    gemini.py
    gemini_batch.py
    ollama.py
    openai.py
    openai_batch.py
    patterns.py
    router.py
  __init__.py
  annotation.py
  chunking.py
  data.py
  data_lib.py
  exceptions.py
  extraction.py
  factory.py
  inference.py
  io.py
  plugins.py
  progress.py
  prompt_validation.py
  prompting.py
  py.typed
  registry.py
  resolver.py
  schema.py
  tokenizer.py
  visualization.py
scripts/  (2 files)
  create_provider_plugin.py
  validate_community_providers.py
skills/  (8 files)
  langextract-usage/  (8 files)
    examples/  (3 files)
      … 3 files under this directory
    references/  (3 files)
      … 3 files under this directory
    README.md
    SKILL.md
tests/  (31 files)
  .pylintrc
  annotation_test.py
  chunking_test.py
  create_provider_plugin_test.py
  data_lib_test.py
  extract_precedence_test.py
  extract_schema_integration_test.py
  factory_schema_test.py
  factory_test.py
  format_handler_test.py
  fuzzy_alignment_cases_test.py
  gemini_retry_test.py
  inference_test.py
  init_test.py
  io_test.py
  openai_batch_test.py
  pr_security_check_test.py
  progress_test.py
  prompt_validation_test.py
  prompting_test.py
  provider_plugin_test.py
  provider_schema_test.py
  registry_test.py
  resolver_test.py
  … 7 more files
.gitignore
.pre-commit-config.yaml
.pylintrc
CITATION.cff
COMMUNITY_PROVIDERS.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
autoformat.sh
pyproject.toml
tox.ini
```

## Entry points

- [.github/scripts/pr_security_check.py:949](https://github.com/google/langextract/blob/0e441bf77ddc3119dd0aa413322959234dd84ee5/.github/scripts/pr_security_check.py#L949)
- [.github/scripts/zenodo_publish.py:235](https://github.com/google/langextract/blob/0e441bf77ddc3119dd0aa413322959234dd84ee5/.github/scripts/zenodo_publish.py#L235)
- [benchmarks/benchmark.py:437](https://github.com/google/langextract/blob/0e441bf77ddc3119dd0aa413322959234dd84ee5/benchmarks/benchmark.py#L437)
- [benchmarks/fuzzy_benchmark.py:504](https://github.com/google/langextract/blob/0e441bf77ddc3119dd0aa413322959234dd84ee5/benchmarks/fuzzy_benchmark.py#L504)
- [scripts/create_provider_plugin.py:1530](https://github.com/google/langextract/blob/0e441bf77ddc3119dd0aa413322959234dd84ee5/scripts/create_provider_plugin.py#L1530)
- [scripts/validate_community_providers.py:201](https://github.com/google/langextract/blob/0e441bf77ddc3119dd0aa413322959234dd84ee5/scripts/validate_community_providers.py#L201)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 2 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level functions: _plot_entity_comparison, _plot_extraction_density, _plot_processing_speed, _plot_success_rate… |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: DisplayConfig, ModelConfig, PathConfig, TextTypes, TokenizationConfig. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BenchmarkRunner. Observed top-level functions: _build_cases, _derive_sample_model_id, _doc… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| langextract package | library | Observed | Groups 36 file(s) under langextract package (observed from repository paths and static analysis). Observed top-level classes: AbstractResolver, AlignmentPolicy, Annotator, BatchConfig, ChunkIterator, ContextAwarePromptB… |
| Service / domain layer | service | Observed | Groups 10 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AlignmentStatus, AnnotatedDocument, BaseLanguageModel, BaseSchema, BaseTokenizerError, Cha… |
| skills package | library | Observed | Groups 3 file(s) under skills package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 32 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH langextract.annotation.Annotator, PATCH langextract.extraction.factory.create_model, PATCH langextract.annotatio… |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/auto-update-pr.yaml` (ci)
- `.github/workflows/check-infrastructure-changes.yml` (ci)
- `.github/workflows/check-linked-issue.yml` (ci)
- `.github/workflows/check-pr-security.yml` (ci)
- `.github/workflows/check-pr-size.yml` (ci)
- `.github/workflows/check-pr-up-to-date.yaml` (ci)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/revalidate-pr.yml` (ci)
- `.github/workflows/validate-community-providers.yaml` (ci)
- `.github/workflows/validate_pr_template.yaml` (ci)
- `.github/workflows/zenodo-publish.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `examples/custom_provider_plugin/pyproject.toml` (manifest)
- `examples/ollama/.dockerignore` (container)
- `examples/ollama/Dockerfile` (container)
- `examples/ollama/docker-compose.yml` (container)
- `pyproject.toml` (manifest)
- `tox.ini` (config)

## Top-level layout

- `langextract` — 49 analysed file(s)
- `tests` — 31 analysed file(s)
- `.github` — 22 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `examples` — 12 analysed file(s)
- `skills` — 8 analysed file(s)
- `docs` — 7 analysed file(s)
- `benchmarks` — 5 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0e441bf77ddc3119dd0aa413322959234dd84ee5` is the revision these paths and observations refer to.
