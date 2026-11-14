# Project structure: HKUDS/RAG-Anything

**Analysed commit:** `eb7a670f724e59056b6a08f7016d753226a865ee`

**Commit reference:** [eb7a670f724e59056b6a08f7016d753226a865ee](https://github.com/HKUDS/RAG-Anything/commit/eb7a670f724e59056b6a08f7016d753226a865ee)

**Tree at this commit:** [HKUDS/RAG-Anything@eb7a670f724e](https://github.com/HKUDS/RAG-Anything/tree/eb7a670f724e59056b6a08f7016d753226a865ee)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | HKUDS/RAG-Anything |
| Description | "RAG-Anything: All-in-One RAG Framework" |
| Stars | 24533 |
| Forks | 2869 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `eb7a670f724e59056b6a08f7016d753226a865ee` |
| Retrieved at | 2026-11-14T19:07:37.916686+00:00 |
| Files in this snapshot | 154 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    question.yml
  workflows/  (3 files)
    linting.yaml
    pypi-publish.yml
    test.yaml
  dependabot.yml
  pull_request_template.md
docs/  (6 files)
  batch_processing.md
  context_aware_processing.md
  enhanced_markdown.md
  multimodal_rag_failure_modes.md
  offline_setup.md
  vllm_integration.md
examples/  (14 files)
  batch_dry_run_example.py
  batch_processing_example.py
  enhanced_markdown_example.py
  image_format_test.py
  insert_content_list_example.py
  lmstudio_integration_example.py
  minimax_integration_example.py
  modalprocessors_example.py
  multimodal_ingest_call_count_bench.py
  office_document_test.py
  ollama_integration_example.py
  raganything_example.py
  text_format_test.py
  vllm_integration_example.py
raganything/  (25 files)
  __init__.py
  asset_urls.py
  base.py
  batch.py
  batch_parser.py
  callbacks.py
  config.py
  document_context.py
  enhanced_markdown.py
  image_signature.py
  mineru_content.py
  modalprocessors.py
  modalprocessors_audio.py
  modalprocessors_video.py
  omml_extractor.py
  parse_options.py
  parser.py
  processor.py
  prompt.py
  prompt_manager.py
  prompts_zh.py
  query.py
  raganything.py
  resilience.py
  … 1 more files
reproduce/  (4 files)
  env.example
  index.py
  llm_answer_evaluator.py
  query.py
scripts/  (1 files)
  create_tiktoken_cache.py
tests/  (84 files)
  test_asset_urls.py
  test_audio_processor.py
  test_batch_parser_workers.py
  test_batch_rag_async.py
  test_batch_rag_incremental.py
  test_callbacks.py
  test_chart_image_routing.py
  test_chinese_cid_font.py
  test_circuit_breaker_stale_results.py
  test_circuit_breaker_sync_cancellation.py
  test_close_event_loop.py
  test_config_environment.py
  test_content_list_alias_handling.py
  test_core_modules.py
  test_custom_parser.py
  test_doc_status_creation.py
  test_doc_status_lightrag_server_compatibility.py
  test_docling_content_blocks.py
  test_docling_page_provenance.py
  test_docling_text_files.py
  test_document_context_isolation.py
  test_document_deletion_cascade.py
  test_embedding_examples.py
  test_enhanced_markdown_css.py
  … 60 more files
.gitignore
.pre-commit-config.yaml
LICENSE
MANIFEST.in
README.md
README_zh.md
SECURITY.md
env.example
pyproject.toml
requirements.txt
setup.py
```

## Entry points

- [raganything/batch_parser.py:801](https://github.com/HKUDS/RAG-Anything/blob/eb7a670f724e59056b6a08f7016d753226a865ee/raganything/batch_parser.py#L801)
- [raganything/enhanced_markdown.py:678](https://github.com/HKUDS/RAG-Anything/blob/eb7a670f724e59056b6a08f7016d753226a865ee/raganything/enhanced_markdown.py#L678)
- [raganything/parser.py:3743](https://github.com/HKUDS/RAG-Anything/blob/eb7a670f724e59056b6a08f7016d753226a865ee/raganything/parser.py#L3743)
- [reproduce/index.py:283](https://github.com/HKUDS/RAG-Anything/blob/eb7a670f724e59056b6a08f7016d753226a865ee/reproduce/index.py#L283)
- [reproduce/llm_answer_evaluator.py:1875](https://github.com/HKUDS/RAG-Anything/blob/eb7a670f724e59056b6a08f7016d753226a865ee/reproduce/llm_answer_evaluator.py#L1875)
- [reproduce/query.py:335](https://github.com/HKUDS/RAG-Anything/blob/eb7a670f724e59056b6a08f7016d753226a865ee/reproduce/query.py#L335)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: RAGAnythingConfig. Observed top-level functions: read_long_description, read_requirem… |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BatchParser, BatchProcessingResult, DoclingParser, EnhancedMarkdownConverter, EvaluationCo… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| raganything package | library | Observed | Groups 21 file(s) under raganything package (observed from repository paths and static analysis). Observed top-level classes: AudioModalProcessor, BaseModalProcessor, BatchMixin, CallbackManager, CircuitBreaker, Context… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 87 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH subprocess.Popen, PATCH pathlib.Path.mkdir, PATCH subprocess.Popen, PATCH pathlib.Path.mkdir, PATCH subprocess.P… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/linting.yaml` (ci)
- `.github/workflows/pypi-publish.yml` (ci)
- `.github/workflows/test.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `tests` — 84 analysed file(s)
- `raganything` — 25 analysed file(s)
- `examples` — 14 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 9 analysed file(s)
- `docs` — 6 analysed file(s)
- `reproduce` — 4 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `eb7a670f724e59056b6a08f7016d753226a865ee` is the revision these paths and observations refer to.
