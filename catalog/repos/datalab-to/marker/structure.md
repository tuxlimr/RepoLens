# Project structure: datalab-to/marker

**Analysed commit:** `d580b63874d9c8510fa54494975b9df1e8b527d0`

**Commit reference:** [d580b63874d9c8510fa54494975b9df1e8b527d0](https://github.com/datalab-to/marker/commit/d580b63874d9c8510fa54494975b9df1e8b527d0)

**Tree at this commit:** [datalab-to/marker@d580b63874d9](https://github.com/datalab-to/marker/tree/d580b63874d9c8510fa54494975b9df1e8b527d0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | datalab-to/marker |
| Description | Convert PDF to markdown + JSON quickly with high accuracy |
| Stars | 40910 |
| Forks | 2954 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `d580b63874d9c8510fa54494975b9df1e8b527d0` |
| Retrieved at | 2026-11-14T19:06:41.910069+00:00 |
| Files in this snapshot | 212 |

## Directory tree

```text
.agents/  (1 files)
  skills/  (1 files)
    marker/  (1 files)
      … 1 files under this directory
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    breaking-bug-report.md
    feature_request.md
    output-bug-report.md
  workflows/  (4 files)
    ci.yml
    cla.yml
    publish.yml
    scripts.yml
benchmarks/  (8 files)
  competitors/  (3 files)
    docling_infer.py
    liteparse_infer.py
    mineru_infer.sh
  README.md
  inference.py
  plot_benchmarks.py
  postprocess.py
  summarize.py
data/  (6 files)
  examples/  (4 files)
    markdown/  (4 files)
      … 4 files under this directory
  .gitignore
  latex_to_md.sh
examples/  (2 files)
  README.md
  marker_modal_deployment.py
marker/  (129 files)
  builders/  (6 files)
    __init__.py
    document.py
    layout.py
    line.py
    ocr.py
    structure.py
  config/  (4 files)
    __init__.py
    crawler.py
    parser.py
    printer.py
  converters/  (4 files)
    __init__.py
    ocr.py
    pdf.py
    table.py
  ocr/  (2 files)
    __init__.py
    indra.py
  processors/  (32 files)
    llm/  (12 files)
      … 12 files under this directory
    __init__.py
    blank_page.py
    block_relabel.py
    blockquote.py
    code.py
    debug.py
    document_toc.py
    equation.py
    footnote.py
    ignoretext.py
    line_merge.py
    line_numbers.py
    list.py
    marginalia.py
    page_header.py
    reference.py
    sectionheader.py
    table.py
    table_recon.py
    text.py
  providers/  (10 files)
    __init__.py
    document.py
    epub.py
    html.py
    image.py
    pdf.py
    powerpoint.py
    registry.py
    spreadsheet.py
    utils.py
  renderers/  (6 files)
    __init__.py
    chunk.py
    html.py
    json.py
    markdown.py
    ocr_json.py
  schema/  (41 files)
    blocks/  (25 files)
      … 25 files under this directory
    groups/  (7 files)
      … 7 files under this directory
    text/  (4 files)
      … 4 files under this directory
    __init__.py
    document.py
    labels.py
    polygon.py
    registry.py
  scripts/  (6 files)
    __init__.py
    common.py
    convert.py
    convert_single.py
    server.py
    viewer.py
  services/  (8 files)
    __init__.py
    azure_openai.py
    claude.py
    gemini.py
    ollama.py
    openai.py
    openrouter.py
    vertex.py
  skills/  (2 files)
    SKILL.md
    __init__.py
  utils/  (3 files)
    __init__.py
    batch.py
    image.py
  logger.py
  models.py
  output.py
  settings.py
  util.py
signatures/  (1 files)
  version1/  (1 files)
    cla.json
static/  (1 files)
  fonts/  (1 files)
    .gitignore
tests/  (45 files)
  builders/  (11 files)
    test_blank_page.py
    test_document_builder.py
    test_garbled_pdf.py
    test_layout_replace.py
    test_ocr_builder.py
    test_ocr_pipeline.py
    test_overriding.py
    test_pdf_links.py
    test_rotated_bboxes.py
    test_strip_existing_ocr.py
    test_structure.py
  config/  (2 files)
    test_config.py
    test_font_settings.py
  converters/  (5 files)
    test_modes.py
    test_ocr_converter.py
    test_olmocr_bench.py
    test_pdf_converter.py
    test_table_converter.py
  data/  (2 files)
    olmocr_bench/  (2 files)
      … 2 files under this directory
  ocr/  (1 files)
    test_indra_ocr.py
  processors/  (8 files)
    test_accuracy_fixes.py
    test_document_toc_processor.py
    test_equation_processor.py
    test_footnote_processor.py
    test_ignoretext.py
    test_llm_processors.py
    test_table_merge.py
    test_table_processor.py
  providers/  (3 files)
    test_document_providers.py
    test_image_provider.py
    test_pdf_provider.py
  renderers/  (5 files)
    test_chunk_renderer.py
    test_extract_images.py
    test_html_renderer.py
    test_json_renderer.py
    test_markdown_renderer.py
  schema/  (2 files)
    blocks/  (1 files)
      … 1 files under this directory
    groups/  (1 files)
      … 1 files under this directory
  security/  (1 files)
    test_security_hardening.py
  services/  (3 files)
    test_ollama.py
    test_openrouter_model_config.py
    test_service_init.py
  conftest.py
  utils.py
.gitignore
.pre-commit-config.yaml
CLA.md
LICENSE
MODEL_LICENSE
README.md
convert.py
convert_single.py
marker_app.py
marker_server.py
pyproject.toml
pytest.ini
```

## Entry points

- [benchmarks/competitors/docling_infer.py:117](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/benchmarks/competitors/docling_infer.py#L117)
- [benchmarks/competitors/liteparse_infer.py:108](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/benchmarks/competitors/liteparse_infer.py#L108)
- [benchmarks/inference.py:279](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/benchmarks/inference.py#L279)
- [benchmarks/plot_benchmarks.py:660](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/benchmarks/plot_benchmarks.py#L660)
- [benchmarks/summarize.py:75](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/benchmarks/summarize.py#L75)
- [convert.py:3](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/convert.py#L3)
- [convert_single.py:3](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/convert_single.py#L3)
- [marker/scripts/convert.py](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/marker/scripts/convert.py)
- [marker/scripts/convert_single.py](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/marker/scripts/convert_single.py)
- [marker/scripts/server.py](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/marker/scripts/server.py)
- [marker/scripts/viewer.py](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/marker/scripts/viewer.py)
- [marker_app.py:3](https://github.com/datalab-to/marker/blob/d580b63874d9c8510fa54494975b9df1e8b527d0/marker_app.py#L3)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 2 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level functions: _latex_to_unicode, _strip_escapes_outside_math, _subsup_to_unicode, postprocess. |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigCrawler, ConfigParser, CustomClickPrinter, Settings. Observed top-level functi… |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: _ensure_surya_cache_writable, create_model_dict, shutdown_models. |
| Application entry point | entrypoint | Observed | Groups 11 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: CommonParams, ViewerEngine, ViewerPagePa… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| marker package | library | Observed | Groups 112 file(s) under marker package (observed from repository paths and static analysis). Observed top-level classes: BaseBuilder, BaseConverter, BaseLLMComplexBlockProcessor, BaseLLMProcessor, BaseLLMSimpleBlockPro… |
| Service / domain layer | service | Observed | Groups 8 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AzureOpenAIService, BaseGeminiService, BaseService, ClaudeService, GoogleGeminiService, Goo… |
| Tests | test | Observed | Groups 45 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: NewLine, NewSectionHeader, ResponseSchema, ServiceConfig, ServiceConfigWithKey. Observed top-level function… |

## Important files

- `.github/workflows/ci.yml` (ci)
- `.github/workflows/cla.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/scripts.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `data/examples/markdown/multicolcnn/multicolcnn_meta.json` (config)
- `data/examples/markdown/switch_transformers/switch_trans_meta.json` (config)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `signatures/version1/cla.json` (config)

## Top-level layout

- `marker` — 129 analysed file(s)
- `tests` — 45 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `benchmarks` — 8 analysed file(s)
- `.github` — 7 analysed file(s)
- `data` — 6 analysed file(s)
- `examples` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `signatures` — 1 analysed file(s)
- `static` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d580b63874d9c8510fa54494975b9df1e8b527d0` is the revision these paths and observations refer to.
