# Project structure: ScrapeGraphAI/Scrapegraph-ai

**Analysed commit:** `194055e203afce41ed4e70365dbc416bad756115`

**Commit reference:** [194055e203afce41ed4e70365dbc416bad756115](https://github.com/ScrapeGraphAI/Scrapegraph-ai/commit/194055e203afce41ed4e70365dbc416bad756115)

**Tree at this commit:** [ScrapeGraphAI/Scrapegraph-ai@194055e203af](https://github.com/ScrapeGraphAI/Scrapegraph-ai/tree/194055e203afce41ed4e70365dbc416bad756115)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ScrapeGraphAI/Scrapegraph-ai |
| Description | Python scraper based on AI |
| Stars | 32779 |
| Forks | 3347 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `194055e203afce41ed4e70365dbc416bad756115` |
| Retrieved at | 2026-11-14T19:07:02.027404+00:00 |
| Files in this snapshot | 368 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    custom.md
    feature_request.md
  workflows/  (4 files)
    codeql.yml
    dependency-review.yml
    release.yml
    test-suite.yml
  FUNDING.yml
PullRequests/  (1 files)
  PR_1027_reviews.md
docs/  (12 files)
  assets/  (1 files)
    scrapegraphai_logo.svg
  chinese.md
  french.md
  german.md
  italian.md
  japanese.md
  korean.md
  portuguese.md
  russian.md
  spanish.md
  timeout_configuration.md
  turkish.md
examples/  (112 files)
  code_generator_graph/  (4 files)
    ollama/  (1 files)
      … 1 files under this directory
    openai/  (1 files)
      … 1 files under this directory
    .env.example
    README.md
  csv_scraper_graph/  (8 files)
    ollama/  (3 files)
      … 3 files under this directory
    openai/  (3 files)
      … 3 files under this directory
    .env.example
    README.md
  custom_graph/  (4 files)
    ollama/  (1 files)
      … 1 files under this directory
    openai/  (1 files)
      … 1 files under this directory
    .env.example
    README.md
  depth_search_graph/  (4 files)
    ollama/  (1 files)
      … 1 files under this directory
    openai/  (1 files)
      … 1 files under this directory
    .env.example
    README.md
  document_scraper_graph/  (7 files)
    ollama/  (2 files)
      … 2 files under this directory
    openai/  (3 files)
      … 3 files under this directory
    .env.example
    README.md
  extras/  (20 files)
    .env.example
    authenticated_playwright.py
    browser_base_integration.py
    chromium_selenium.py
    cond_smartscraper_usage.py
    conditional_usage.py
    custom_prompt.py
    example.yml
    force_mode.py
    html_mode.py
    load_yml.py
    no_cut.py
    proxy_rotation.py
    rag_caching.py
    reasoning.py
    scrape_do.py
    screenshot_scaping.py
    serch_graph_scehma.py
    slow_mo.py
    undected_playwright.py
  json_scraper_graph/  (10 files)
    ollama/  (3 files)
      … 3 files under this directory
    openai/  (5 files)
      … 5 files under this directory
    .env.example
    README.md
  markdownify/  (4 files)
    .env.example
    markdownify_scrapegraphai.py
    markdownify_scrapegraphai_v3.py
    readme.md
  omni_scraper_graph/  (3 files)
    .env.example
    README.md
    omni_search_openai.py
  script_generator_graph/  (7 files)
    ollama/  (2 files)
      … 2 files under this directory
    openai/  (3 files)
      … 3 files under this directory
    .env.example
    README.md
  search_graph/  (11 files)
    ollama/  (2 files)
      … 2 files under this directory
    openai/  (3 files)
      … 3 files under this directory
    scrapegraphai/  (4 files)
      … 4 files under this directory
    .env.example
    README.md
  smart_scraper_graph/  (18 files)
    nvidia/  (1 files)
      … 1 files under this directory
    ollama/  (6 files)
      … 6 files under this directory
    openai/  (6 files)
      … 6 files under this directory
    scrapegraphai/  (4 files)
      … 4 files under this directory
    .env.example
  speech_graph/  (3 files)
    .env.example
    README.md
    speech_graph_openai.py
  xml_scraper_graph/  (8 files)
    ollama/  (3 files)
      … 3 files under this directory
    openai/  (3 files)
      … 3 files under this directory
    .env.example
    README.md
  readme.md
scrapegraphai/  (140 files)
  builders/  (2 files)
    __init__.py
    graph_builder.py
  docloaders/  (5 files)
    __init__.py
    browser_base.py
    chromium.py
    plasmate.py
    scrape_do.py
  graphs/  (28 files)
    __init__.py
    abstract_graph.py
    base_graph.py
    code_generator_graph.py
    csv_scraper_graph.py
    csv_scraper_multi_graph.py
    depth_search_graph.py
    document_scraper_graph.py
    document_scraper_multi_graph.py
    json_scraper_graph.py
    json_scraper_multi_graph.py
    markdownify_graph.py
    omni_scraper_graph.py
    omni_search_graph.py
    screenshot_scraper_graph.py
    script_creator_graph.py
    script_creator_multi_graph.py
    search_graph.py
    search_link_graph.py
    smart_scraper_graph.py
    smart_scraper_lite_graph.py
    smart_scraper_multi_batch_graph.py
    smart_scraper_multi_concat_graph.py
    smart_scraper_multi_graph.py
    … 4 more files
  helpers/  (6 files)
    __init__.py
    default_filters.py
    models_tokens.py
    nodes_metadata.py
    robots.py
    schemas.py
  integrations/  (4 files)
    __init__.py
    burr_bridge.py
    indexify_node.py
    scrapegraph_py_compat.py
  models/  (11 files)
    __init__.py
    atlascloud.py
    cheaperinference.py
    clod.py
    deepseek.py
    minimax.py
    nvidia.py
    oneapi.py
    openai_itt.py
    openai_tts.py
    xai.py
  nodes/  (33 files)
    __init__.py
    base_node.py
    batch_generate_answer_node.py
    concat_answers_node.py
    conditional_node.py
    description_node.py
    fetch_node.py
    fetch_node_level_k.py
    fetch_screen_node.py
    generate_answer_csv_node.py
    generate_answer_from_image_node.py
    generate_answer_node.py
    generate_answer_node_k_level.py
    generate_answer_omni_node.py
    generate_code_node.py
    generate_scraper_node.py
    get_probable_tags_node.py
    graph_iterator_node.py
    html_analyzer_node.py
    image_to_text_node.py
    markdownify_node.py
    merge_answers_node.py
    merge_generated_scripts_node.py
    parse_node.py
    … 9 more files
  prompts/  (17 files)
    __init__.py
    description_node_prompts.py
    generate_answer_node_csv_prompts.py
    generate_answer_node_omni_prompts.py
    generate_answer_node_pdf_prompts.py
    generate_answer_node_prompts.py
    generate_code_node_prompts.py
    get_probable_tags_node_prompts.py
    html_analyzer_node_prompts.py
    merge_answer_node_prompts.py
    merge_generated_scripts_prompts.py
    prompt_refiner_node_prompts.py
    reasoning_node_prompts.py
    robots_node_prompts.py
    search_internet_node_prompts.py
    search_link_node_prompts.py
    search_node_with_context_prompts.py
  telemetry/  (2 files)
    __init__.py
    telemetry.py
  utils/  (31 files)
    screenshot_scraping/  (3 files)
      … 3 files under this directory
    tokenizers/  (3 files)
      … 3 files under this directory
    __init__.py
    batch_api.py
    cleanup_code.py
    cleanup_html.py
    code_error_analysis.py
    code_error_correction.py
    convert_to_md.py
    copy.py
    custom_callback.py
    data_export.py
    dict_content_compare.py
    llm_callback_manager.py
    logging.py
    model_costs.py
    output_parser.py
    parse_state_keys.py
    prettify_exec_info.py
    proxy_rotation.py
    research_web.py
    save_audio_from_bytes.py
    save_code_to_file.py
    schema_trasform.py
    split_text_into_chunks.py
    sys_dynamic_import.py
    … 1 more files
  __init__.py
tests/  (74 files)
  fixtures/  (4 files)
    mock_server/  (2 files)
      … 2 files under this directory
    benchmarking.py
    helpers.py
  graphs/  (21 files)
    inputs/  (4 files)
      … 4 files under this directory
    .env.example
    abstract_graph_test.py
    code_generator_graph_openai_test.py
    depth_search_graph_openai_test.py
    scrape_plain_text_mistral_test.py
    scrape_xml_ollama_test.py
    screenshot_scraper_test.py
    script_generator_test.py
    search_graph_openai_test.py
    search_link_ollama.py
    smart_scraper_clod_test.py
    smart_scraper_ernie_test.py
    smart_scraper_fireworks_test.py
    smart_scraper_multi_lite_graph_openai_test.py
    smart_scraper_ollama_test.py
    smart_scraper_openai_test.py
    xml_scraper_openai_test.py
  inputs/  (4 files)
    books.xml
    example.json
    plain_html_example.txt
    username.csv
  integration/  (4 files)
    __init__.py
    test_file_formats_integration.py
    test_multi_graph_integration.py
    test_smart_scraper_integration.py
  nodes/  (8 files)
    inputs/  (4 files)
      … 4 files under this directory
    fetch_node_test.py
    robot_node_test.py
    search_internet_node_test.py
    search_link_node_test.py
  utils/  (8 files)
    convert_to_md_test.py
    copy_utils_test.py
    output_parser_test.py
    parse_state_keys_test.py
    research_web_test.py
    schema_transform_test.py
    test_proxy_rotation.py
    test_sys_dynamic_import.py
  QUICKSTART.md
  README_TESTING.md
  Readme.md
  conftest.py
  test_atlascloud_model.py
  test_batch_api.py
  test_cheaperinference_model.py
  test_chromium.py
  test_cleanup_html.py
  test_csv_scraper_multi_graph.py
  test_depth_search_graph.py
  test_error_page_detection.py
  test_fetch_node_timeout.py
  test_generate_answer_node.py
  test_json_scraper_graph.py
  test_json_scraper_multi_graph.py
  test_minimax_models.py
  test_models_tokens.py
  test_omni_search_graph.py
  test_plasmate.py
  test_scrape_do.py
  test_script_creator_multi_graph.py
  test_search_graph.py
  test_smart_scraper_multi_concat_graph.py
  … 1 more files
.gitattributes
.gitignore
.pre-commit-config.yaml
.releaserc.yml
.semantic-commits-applied
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
Makefile
README.md
SECURITY.md
SEMANTIC_COMMITS.md
TESTING_INFRASTRUCTURE.md
citation.cff
codebeaver.yml
docker-compose.yml
pyproject.toml
pytest.ini
test
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AtlasCloud, CLoD, CheaperInference, DeepSeek, MiniMax, Nvidia. |
| External integrations | external | Observed | Groups 5 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BatchJobInfo, BatchRequest, BatchResult, BurrBridge, BurrNodeBridge, IndexifyNode. Observed… |
| scrapegraphai package | library | Observed | Groups 123 file(s) under scrapegraphai package (observed from repository paths and static analysis). Observed top-level classes: AbstractGraph, AnalysisError, BaseGraph, BaseNode, BatchGenerateAnswerNode, CSVScraperGrap… |
| Tests | test | Observed | Groups 75 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH scrapegraphai.docloaders.chromium.dynamic_import, PATCH scrapegraphai.nodes.fetch_node.requests, PATCH scrapegra… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/dependency-review.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test-suite.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.releaserc.yml` (config)
- `Dockerfile` (container)
- `codebeaver.yml` (config)
- `docker-compose.yml` (container)
- `examples/code_generator_graph/.env.example` (config)
- `examples/csv_scraper_graph/.env.example` (config)
- `examples/custom_graph/.env.example` (config)
- `examples/depth_search_graph/.env.example` (config)
- `examples/document_scraper_graph/.env.example` (config)
- `examples/extras/.env.example` (config)
- `examples/extras/example.yml` (config)
- `examples/json_scraper_graph/.env.example` (config)
- `examples/json_scraper_graph/ollama/inputs/example.json` (config)
- `examples/json_scraper_graph/openai/inputs/example.json` (config)
- `examples/markdownify/.env.example` (config)
- `examples/omni_scraper_graph/.env.example` (config)
- `examples/script_generator_graph/.env.example` (config)
- `examples/search_graph/.env.example` (config)
- `examples/search_graph/scrapegraphai/.env.example` (config)
- `examples/smart_scraper_graph/.env.example` (config)
- `examples/smart_scraper_graph/scrapegraphai/.env.example` (config)
- `examples/speech_graph/.env.example` (config)
- `examples/xml_scraper_graph/.env.example` (config)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)

## Top-level layout

- `scrapegraphai` — 140 analysed file(s)
- `examples` — 112 analysed file(s)
- `tests` — 74 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `docs` — 12 analysed file(s)
- `.github` — 8 analysed file(s)
- `PullRequests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `194055e203afce41ed4e70365dbc416bad756115` is the revision these paths and observations refer to.
