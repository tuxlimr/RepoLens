# Project structure: gunthercox/ChatterBot

**Analysed commit:** `be68629cedb8a40f072bb2e456f7af2d4ea91998`

**Commit reference:** [be68629cedb8a40f072bb2e456f7af2d4ea91998](https://github.com/gunthercox/ChatterBot/commit/be68629cedb8a40f072bb2e456f7af2d4ea91998)

**Tree at this commit:** [gunthercox/ChatterBot@be68629cedb8](https://github.com/gunthercox/ChatterBot/tree/be68629cedb8a40f072bb2e456f7af2d4ea91998)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gunthercox/ChatterBot |
| Description | ChatterBot is a machine learning, conversational dialog engine for creating chat bots |
| Stars | 14523 |
| Forks | 4406 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `be68629cedb8a40f072bb2e456f7af2d4ea91998` |
| Retrieved at | 2026-11-14T19:09:23.607024+00:00 |
| Files in this snapshot | 238 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    publish-documentation.yml
    python-package.yml
  FUNDING.yml
chatterbot/  (67 files)
  ext/  (32 files)
    django_chatterbot/  (29 files)
      … 29 files under this directory
    sqlalchemy_app/  (2 files)
      … 2 files under this directory
    __init__.py
  logic/  (9 files)
    __init__.py
    best_match.py
    llm_adapters.py
    logic_adapter.py
    mathematical_evaluation.py
    mcp_tools.py
    specific_response.py
    time_adapter.py
    unit_conversion.py
  storage/  (6 files)
    __init__.py
    django_storage.py
    mongodb.py
    redis.py
    sql_storage.py
    storage_adapter.py
  __init__.py
  __main__.py
  adapters.py
  chatterbot.py
  comparisons.py
  components.py
  constants.py
  conversation.py
  corpus.py
  exceptions.py
  filters.py
  languages.py
  parsing.py
  preprocessors.py
  response_selection.py
  search.py
  tagging.py
  trainers.py
  utils.py
  vectorstores.py
docs/  (64 files)
  _ext/  (2 files)
    canonical.py
    github.py
  _includes/  (1 files)
    python_module_structure.txt
  _static/  (9 files)
    MongoDB_Fores-Green.svg
    Redis_Logo_Red_RGB.svg
    bigrams.svg
    mobile.js
    silktide-consent-manager.css
    silktide-consent-manager.js
    statement-relationship.svg
    statement-response-relationship.svg
    style.css
  _templates/  (4 files)
    footer.html
    layout.html
    page.html
    sidebar_ad.html
  django/  (11 files)
    tutorial/  (6 files)
      … 6 files under this directory
    custom-models.rst
    index.rst
    settings.rst
    views.rst
    wsgi.rst
  logic/  (3 files)
    create-a-logic-adapter.rst
    index.rst
    response-selection.rst
  storage/  (6 files)
    create-a-storage-adapter.rst
    index.rst
    mongodb.rst
    redis.rst
    sql.rst
    text-search.rst
  chatterbot.rst
  commands.rst
  comparisons.rst
  conf.py
  contributing.rst
  conversations.rst
  corpus.rst
  development.rst
  encoding.rst
  examples.rst
  faq.rst
  filters.rst
  glossary.rst
  index.rst
  large-language-models.rst
  packaging.rst
  preprocessors.rst
  quickstart.rst
  releases.rst
  robots.txt
  security.rst
  setup.rst
  statements.txt
  testing.rst
  … 4 more files
examples/  (39 files)
  django_example/  (21 files)
    django_example/  (18 files)
      … 18 files under this directory
    README.rst
    manage.py
    requirements.txt
  __init__.py
  basic_example.py
  convert_units.py
  default_response_example.py
  export_example.py
  learning_feedback_example.py
  math_and_time.py
  memory_sql_example.py
  ollama_example.py
  openai_example.py
  specific_response_example.py
  tagged_dataset_example.py
  terminal_example.py
  terminal_mongo_example.py
  tkinter_gui.py
  training_example_chatterbot_corpus.py
  training_example_list_data.py
  training_example_ubuntu_corpus.py
graphics/  (1 files)
  README.md
tests/  (56 files)
  django_integration/  (11 files)
    __init__.py
    base_case.py
    test_chatbot.py
    test_chatterbot_corpus_training.py
    test_chatterbot_settings.py
    test_custom_models.py
    test_django_adapter.py
    test_logic_adapter_integration.py
    test_secondary_database.py
    test_settings.py
    test_statement_integration.py
  logic/  (8 files)
    __init__.py
    test_best_match.py
    test_data_cache.py
    test_logic_adapter.py
    test_mathematical_evaluation.py
    test_specific_response.py
    test_time.py
    test_unit_conversion.py
  storage/  (5 files)
    __init__.py
    test_mongo_adapter.py
    test_redis_adapter.py
    test_sql_adapter.py
    test_storage_adapter.py
  training/  (12 files)
    test_data/  (5 files)
      … 5 files under this directory
    __init__.py
    test_chatterbot_corpus_training.py
    test_csv_file_training.py
    test_json_file_training.py
    test_list_training.py
    test_training.py
    test_ubuntu_corpus_training.py
  __init__.py
  base_case.py
  test_adapter_validation.py
  test_benchmarks.py
  test_chatbot.py
  test_cli.py
  test_comparisons.py
  test_conversations.py
  test_corpus.py
  test_examples.py
  test_filters.py
  test_initialization.py
  test_languages.py
  test_parsing.py
  test_preprocessors.py
  test_response_selection.py
  test_search.py
  test_tagging.py
  test_turing.py
  test_utils.py
.codeclimate.yml
.gitignore
CODE_OF_CONDUCT.md
LICENSE
README.md
SECURITY.md
pyproject.toml
setup.cfg
```

## Entry points

- [chatterbot/__main__.py:19](https://github.com/gunthercox/ChatterBot/blob/be68629cedb8a40f072bb2e456f7af2d4ea91998/chatterbot/__main__.py#L19)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| chatterbot package | library | Observed | Groups 48 file(s) under chatterbot package (observed from repository paths and static analysis). Observed top-level classes: AAR, ABK, ACE, ACH, ADA, ADY. Observed top-level functions: chatterbot_bigram_indexer, chatter… |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 8 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DjangoStorageAdapter, ModelBase, MongoDatabaseAdapter, RedisVectorStorageAdapter, SQLStorageAdapter, St… |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: get_chatterbot_version. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 9 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: BestMatch, LLMLogicAdapter, LogicAdapter, MCPToolAdapter, MathematicalEvaluation, OllamaLog… |
| Tests | test | Observed | Groups 59 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AdapterValidationTests, ApiIntegrationTestCase, ApiTestCase, BenchmarkingMixin, BestMatchTestCase, ChatBotI… |

## Important files

- `.codeclimate.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/publish-documentation.yml` (ci)
- `.github/workflows/python-package.yml` (ci)
- `examples/django_example/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `setup.cfg` (manifest)

## Top-level layout

- `chatterbot` — 67 analysed file(s)
- `docs` — 64 analysed file(s)
- `tests` — 56 analysed file(s)
- `examples` — 39 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 3 analysed file(s)
- `graphics` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `be68629cedb8a40f072bb2e456f7af2d4ea91998` is the revision these paths and observations refer to.
