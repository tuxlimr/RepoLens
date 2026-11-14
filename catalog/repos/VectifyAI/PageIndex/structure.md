# Project structure: VectifyAI/PageIndex

**Analysed commit:** `cc035e8ddcfa51633309ddf2f794b161a17d8cbc`

**Commit reference:** [cc035e8ddcfa51633309ddf2f794b161a17d8cbc](https://github.com/VectifyAI/PageIndex/commit/cc035e8ddcfa51633309ddf2f794b161a17d8cbc)

**Tree at this commit:** [VectifyAI/PageIndex@cc035e8ddcfa](https://github.com/VectifyAI/PageIndex/tree/cc035e8ddcfa51633309ddf2f794b161a17d8cbc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | VectifyAI/PageIndex |
| Description | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
| Stars | 40429 |
| Forks | 3474 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `cc035e8ddcfa51633309ddf2f794b161a17d8cbc` |
| Retrieved at | 2026-11-14T19:06:43.948480+00:00 |
| Files in this snapshot | 150 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (4 files)
    codeql.yml
    dependency-review.yml
    publish.yml
    tests.yml
  dependabot.yml
assets/  (2 files)
  vectorless-rag-dark.svg
  vectorless-rag-light.svg
cookbook/  (11 files)
  pageindex-vs-vector-10k/  (4 files)
    answers_pageindex.jsonl
    nvidia-10k-questions.json
    pageindex-vs-embeddings-10k.ipynb
    pageindex-vs-vector-10k.ipynb
  pageindex-claude-subscription.py
  pageindex-flash-demo.ipynb
  pageindex-indexing-cost-demo.ipynb
  pageindex-metadata.ipynb
  pageindex-multimodal.ipynb
  pageindex-query-pricing-demo.ipynb
  pageindex-vision-rag.ipynb
examples/  (8 files)
  results/  (8 files)
    2023-annual-report-truncated_structure.json
    2023-annual-report_structure.json
    PRML_structure.json
    Regulation Best Interest_Interpretive release_structure.json
    Regulation Best Interest_proposed rule_structure.json
    earthmover_structure.json
    four-lectures_structure.json
    q1-fy25-earnings_structure.json
pageindex/  (103 files)
  flash/  (78 files)
    blocks/  (3 files)
      … 3 files under this directory
    classification/  (5 files)
      … 5 files under this directory
    clustering/  (3 files)
      … 3 files under this directory
    columns/  (3 files)
      … 3 files under this directory
    data/  (3 files)
      … 3 files under this directory
    heading_detection/  (8 files)
      … 8 files under this directory
    labels/  (3 files)
      … 3 files under this directory
    model/  (6 files)
      … 6 files under this directory
    outline/  (3 files)
      … 3 files under this directory
    outline_assembly/  (6 files)
      … 6 files under this directory
    parser_pdfium_charlevel/  (14 files)
      … 14 files under this directory
    phases/  (3 files)
      … 3 files under this directory
    stats/  (3 files)
      … 3 files under this directory
    title/  (4 files)
      … 4 files under this directory
    tokens/  (5 files)
      … 5 files under this directory
    README.md
    __init__.py
    api.py
    embedded_toc.py
    main.py
    parser_pdfium_parallel.py
  integrations/  (4 files)
    __init__.py
    anthropic_sdk.py
    claude_agent_sdk.py
    openai_agents.py
  __init__.py
  _version.py
  agent_tools.py
  chat_stream.py
  client.py
  cloud_api.py
  config.yaml
  errors.py
  imaging.py
  local_api.py
  local_chat.py
  local_store.py
  mcp_bridge.py
  naming.py
  page_index_classic.py
  page_index_md.py
  py.typed
  retry.py
  tree_optimize.py
  types.py
  utils.py
tests/  (14 files)
  data/  (2 files)
    flash/  (1 files)
      … 1 files under this directory
    cloud_mcp_contract.json
  fixtures/  (1 files)
    naming-v1.json
  conftest.py
  test_agent_tools.py
  test_claude_code.py
  test_flash_extraction.py
  test_imaging.py
  test_issue_163.py
  test_naming.py
  test_package_surface.py
  test_page_index.py
  test_page_index_md.py
  test_tree_format.py
.gitattributes
.gitignore
LICENSE
README.md
pyproject.toml
requirements.txt
run_pageindex.py
```

## Entry points

- [pageindex/page_index_md.py:306](https://github.com/VectifyAI/PageIndex/blob/cc035e8ddcfa51633309ddf2f794b161a17d8cbc/pageindex/page_index_md.py#L306)
- [pageindex/tree_optimize.py:1147](https://github.com/VectifyAI/PageIndex/blob/cc035e8ddcfa51633309ddf2f794b161a17d8cbc/pageindex/tree_optimize.py#L1147)
- [run_pageindex.py:10](https://github.com/VectifyAI/PageIndex/blob/cc035e8ddcfa51633309ddf2f794b161a17d8cbc/run_pageindex.py#L10)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| cookbook package | library | Observed | Groups 1 file(s) under cookbook package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: DocumentState. Observed top-level functions: S, S_residual, _normalize_text_key, _sibling_… |
| External integrations | external | Observed | Groups 7 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: CloudAPI, LocalAPI, PageIndexClient, PageIndexCloudClient, PageIndexLocalClient, _Host. Obse… |
| pageindex package | library | Observed | Groups 87 file(s) under pageindex package (observed from repository paths and static analysis). Observed top-level classes: Block, BlockClusterContext, BlockNeighborCache, Bounded, BuiltTrie, CaptionContext. Observed to… |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH pageindex.page_index_classic.llm_completion, PATCH pageindex.page_index_classic.llm_completion, PATCH pageindex.… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/dependency-review.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `cookbook/pageindex-vs-vector-10k/nvidia-10k-questions.json` (config)
- `examples/results/2023-annual-report-truncated_structure.json` (config)
- `examples/results/2023-annual-report_structure.json` (config)
- `examples/results/PRML_structure.json` (config)
- `examples/results/Regulation Best Interest_Interpretive release_structure.json` (config)
- `examples/results/Regulation Best Interest_proposed rule_structure.json` (config)
- `examples/results/earthmover_structure.json` (config)
- `examples/results/four-lectures_structure.json` (config)
- `examples/results/q1-fy25-earnings_structure.json` (config)
- `pageindex/config.yaml` (config)
- `pageindex/flash/data/glyph_name_table.json` (config)
- `pageindex/flash/data/normalized_unicodes.json` (config)
- `pageindex/flash/data/script_bucket_table.json` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `pageindex` — 103 analysed file(s)
- `tests` — 14 analysed file(s)
- `cookbook` — 11 analysed file(s)
- `examples` — 8 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 5 analysed file(s)
- `assets` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `cc035e8ddcfa51633309ddf2f794b161a17d8cbc` is the revision these paths and observations refer to.
