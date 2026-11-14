# Project structure: PromtEngineer/localGPT

**Analysed commit:** `34f3107f56a88203859092312231b945a711c619`

**Commit reference:** [34f3107f56a88203859092312231b945a711c619](https://github.com/PromtEngineer/localGPT/commit/34f3107f56a88203859092312231b945a711c619)

**Tree at this commit:** [PromtEngineer/localGPT@34f3107f56a8](https://github.com/PromtEngineer/localGPT/tree/34f3107f56a88203859092312231b945a711c619)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | PromtEngineer/localGPT |
| Description | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  |
| Stars | 22193 |
| Forks | 2449 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `34f3107f56a88203859092312231b945a711c619` |
| Retrieved at | 2026-11-14T19:07:53.814693+00:00 |
| Files in this snapshot | 212 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    ci.yml
  pull_request_template.md
Documentation/  (19 files)
  research/  (4 files)
    README.md
    academic-evidence-2026.md
    component-map-2026.md
    industry-evidence-2026.md
  api_reference.md
  architecture_overview.md
  deployment_guide.md
  design_rationale.md
  docker_usage.md
  improvement_plan.md
  indexing_pipeline.md
  installation_guide.md
  prompt_inventory.md
  quick_start.md
  research_roadmap.md
  retrieval_pipeline.md
  system_overview.md
  triage_system.md
  verifier.md
backend/  (6 files)
  README.md
  database.py
  ollama_client.py
  requirements.txt
  server.py
  test_gateway_routing.py
eval/  (90 files)
  corpora/  (31 files)
    rfc/  (25 files)
      … 25 files under this directory
    acquisition.facts.json
    atlas7_service_manual.facts.json
    make_hr_handbook.py
    northwind_leave_policy.facts.json
    repo_docs.facts.json
    verify_facts.py
  decisions/  (34 files)
    completeness-clause-ab-2026-08-15.md
    component-ablation-2026-08-18.md
    cross-bench-validation-2026-08-15.md
    embedder.md
    experiments-resolveonly-maxsim-2026-08-19.md
    fixset-impact-2026-08-17.md
    ftslc-index-fix-2026-08-15.md
    glm-ocr-spike.md
    judge-sonnet-validation-2026-08-13.json
    multiturn-decomposer-2026-08-16.md
    multivector-retrieval-2026-08-19.md
    paraphrase-robustness-2026-08-20.md
    phase2-gateway.md
    phase2-pipeline.md
    phase4-answer-quality.md
    phase4-crossref-prefilter.md
    phase4-escalation-rerun.md
    phase4-escalation-tokens.md
    phase4-eval-final-metric.md
    phase4-filters-askfolder.md
    phase4-retrieval-benchmarks.md
    reranker.md
    rfc-shakedown-2026-08-13.md
    rfc-shakedown-sonnet-panel.json
    … 10 more files
  goldset/  (10 files)
    _generated/  (3 files)
      … 3 files under this directory
    acquisition.jsonl
    atlas7.jsonl
    docs.jsonl
    hr.jsonl
    multiturn.jsonl
    paraphrases.jsonl
    rfc.jsonl
  multiturn/  (2 files)
    decomp_stability.py
    run_e2e_multiturn.py
  BASELINE.md
  DECISIONS.md
  README.md
  build_goldset.py
  finalize_goldset.py
  judge.py
  judge_hard_cases.jsonl
  judge_validation.jsonl
  run_eval.py
  smoke_e2e.py
  validate_judge_hard.py
  verify_crossref_goldset.py
  verify_rfc_goldset.py
public/  (1 files)
  .gitkeep
rag_system/  (38 files)
  agent/  (4 files)
    __init__.py
    escalation.py
    loop.py
    verifier.py
  indexing/  (7 files)
    __init__.py
    contextualizer.py
    crossref.py
    embedders.py
    latechunk.py
    overview_builder.py
    representations.py
  ingestion/  (4 files)
    __init__.py
    chunking.py
    docling_chunker.py
    document_converter.py
  pipelines/  (3 files)
    __init__.py
    indexing_pipeline.py
    retrieval_pipeline.py
  rerankers/  (3 files)
    __init__.py
    reranker.py
    sentence_pruner.py
  retrieval/  (5 files)
    __init__.py
    document_fetch.py
    filters.py
    query_transformer.py
    retrievers.py
  utils/  (4 files)
    batch_processor.py
    logging_utils.py
    ollama_client.py
    watsonx_client.py
  DOCUMENTATION.md
  README.md
  __init__.py
  api_server.py
  ask_folder.py
  factory.py
  main.py
  requirements.txt
src/  (28 files)
  app/  (3 files)
    globals.css
    layout.tsx
    page.tsx
  components/  (21 files)
    ui/  (14 files)
      … 14 files under this directory
    IndexForm.tsx
    IndexPicker.tsx
    LandingMenu.tsx
    Markdown.tsx
    ModelSelect.tsx
    SessionIndexInfo.tsx
    demo.tsx
  lib/  (3 files)
    api.ts
    types.ts
    utils.ts
  utils/  (1 files)
    textNormalization.ts
.env.example
.gitignore
CONTRIBUTING.md
DOCKER_README.md
DOCKER_TROUBLESHOOTING.md
Dockerfile.backend
Dockerfile.frontend
Dockerfile.rag-api
LICENSE
README.md
WATSONX_README.md
create_index_script.py
docker-compose.yml
docker.env
env.example.watsonx
eslint.config.mjs
next.config.ts
package.json
postcss.config.mjs
requirements-docker.txt
requirements.txt
run_system.py
start-docker.sh
system_health_check.py
… 2 more files
```

## Entry points

- [backend/database.py:748](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/backend/database.py#L748)
- [backend/ollama_client.py:240](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/backend/ollama_client.py#L240)
- [backend/server.py:1290](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/backend/server.py#L1290)
- [create_index_script.py:410](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/create_index_script.py#L410)
- [eval/build_goldset.py:236](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/eval/build_goldset.py#L236)
- [eval/corpora/make_hr_handbook.py:122](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/eval/corpora/make_hr_handbook.py#L122)
- [eval/corpora/rfc/download.py:157](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/eval/corpora/rfc/download.py#L157)
- [eval/corpora/verify_facts.py:127](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/eval/corpora/verify_facts.py#L127)
- [eval/finalize_goldset.py:168](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/eval/finalize_goldset.py#L168)
- [eval/judge.py:326](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/eval/judge.py#L326)
- [eval/multiturn/decomp_stability.py:202](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/eval/multiturn/decomp_stability.py#L202)
- [eval/multiturn/run_e2e_multiturn.py:245](https://github.com/PromtEngineer/localGPT/blob/34f3107f56a88203859092312231b945a711c619/eval/multiturn/run_e2e_multiturn.py#L245)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 2 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 21 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 25 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 28 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AdvancedRagApiHandler, BatchProcessor, ChatBackendError, ChatDatabase, ChatHandler, Color… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: OllamaClient, TokenUsageTracker. Observed top-level functions: _apply_num_ctx, _num_ctx_for,… |
| lib package | library | Observed | Groups 3 file(s) under lib package (observed from repository paths and static analysis). |
| rag_system package | library | Observed | Groups 25 file(s) under rag_system package (observed from repository paths and static analysis). Observed top-level classes: Agent, CompiledFilter, ContextualEnricher, CrossRefExtractor, DoclingChunker, DocumentConverte… |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: check, main. |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/workflows/ci.yml` (ci)
- `Dockerfile.backend` (container)
- `Dockerfile.frontend` (container)
- `Dockerfile.rag-api` (container)
- `backend/requirements.txt` (manifest)
- `docker-compose.yml` (container)
- `eval/corpora/acquisition.facts.json` (config)
- `eval/corpora/atlas7_service_manual.facts.json` (config)
- `eval/corpora/northwind_leave_policy.facts.json` (config)
- `eval/corpora/repo_docs.facts.json` (config)
- `eval/corpora/rfc/rfc.facts.json` (config)
- `eval/decisions/judge-sonnet-validation-2026-08-13.json` (config)
- `eval/decisions/rfc-shakedown-sonnet-panel.json` (config)
- `eval/decisions/synthesis-ab-arm-e-panel.json` (config)
- `eval/decisions/synthesis-ab-arm-f-panel.json` (config)
- `eval/decisions/synthesis-ab-arm-g-panel.json` (config)
- `eval/decisions/synthesis-ab-arm-g2-panel.json` (config)
- `eval/decisions/synthesis-ab-arm-h-panel.json` (config)
- `eval/decisions/synthesis-ab-arm-h2-panel.json` (config)
- `eval/decisions/synthesis-ab-arm-i-panel.json` (config)
- `eval/decisions/synthesis-ab-sonnet-panels.json` (config)
- `package.json` (manifest)
- `rag_system/requirements.txt` (manifest)
- `requirements-docker.txt` (manifest)
- `requirements.txt` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `eval` — 90 analysed file(s)
- `rag_system` — 38 analysed file(s)
- `src` — 28 analysed file(s)
- `(root files)` — 26 analysed file(s)
- `Documentation` — 19 analysed file(s)
- `backend` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `34f3107f56a88203859092312231b945a711c619` is the revision these paths and observations refer to.
