# Project structure: simonw/llm

**Analysed commit:** `8b475ffdfc2d33aa86c9518baff3ac94bcea409e`

**Commit reference:** [8b475ffdfc2d33aa86c9518baff3ac94bcea409e](https://github.com/simonw/llm/commit/8b475ffdfc2d33aa86c9518baff3ac94bcea409e)

**Tree at this commit:** [simonw/llm@8b475ffdfc2d](https://github.com/simonw/llm/tree/8b475ffdfc2d33aa86c9518baff3ac94bcea409e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | simonw/llm |
| Description | Access large language models from the command-line |
| Stars | 12756 |
| Forks | 1089 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `8b475ffdfc2d33aa86c9518baff3ac94bcea409e` |
| Retrieved at | 2026-11-14T19:10:00.755671+00:00 |
| Files in this snapshot | 123 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (4 files)
    cog.yml
    publish.yml
    stable-docs.yml
    test.yml
  FUNDING.yml
  dependabot.yml
docs/  (35 files)
  _templates/  (1 files)
    base.html
  embeddings/  (5 files)
    cli.md
    index.md
    python-api.md
    storage.md
    writing-plugins.md
  plugins/  (9 files)
    llm-markov/  (2 files)
      … 2 files under this directory
    advanced-model-plugins.md
    directory.md
    index.md
    installing-plugins.md
    plugin-hooks.md
    plugin-utilities.md
    tutorial-model-plugin.md
  .gitignore
  Makefile
  aliases.md
  changelog.md
  conf.py
  contributing.md
  fragments.md
  help.md
  index.md
  logging.md
  openai-models.md
  other-models.md
  python-api.md
  related-tools.md
  requirements.txt
  schemas.md
  setup.md
  templates.md
  tools.md
  usage.md
llm/  (20 files)
  default_plugins/  (3 files)
    __init__.py
    default_tools.py
    openai_models.py
  __init__.py
  __main__.py
  cli.py
  embeddings.py
  embeddings_migrations.py
  errors.py
  hookspecs.py
  logs.py
  migrations.py
  models.py
  parts.py
  plugins.py
  py.typed
  serialization.py
  templates.py
  tools.py
  utils.py
tests/  (51 files)
  cassettes/  (12 files)
    test_openai_responses/  (6 files)
      … 6 files under this directory
    test_tools/  (2 files)
      … 2 files under this directory
    test_tools_streaming/  (4 files)
      … 4 files under this directory
  conftest.py
  test-llm-load-plugins.sh
  test_aliases.py
  test_async.py
  test_async_parity.py
  test_attachments.py
  test_chain_callbacks.py
  test_chat.py
  test_chat_templates.py
  test_cli_openai_models.py
  test_cli_options.py
  test_cli_streaming.py
  test_connection_cleanup.py
  test_embed.py
  test_embed_cli.py
  test_encode_decode.py
  test_fragments_cli.py
  test_incremental_logging.py
  test_keys.py
  test_llm.py
  test_llm_logs.py
  test_logs_store.py
  test_migrate.py
  test_openai_endpoint.py
  … 15 more files
.gitignore
.readthedocs.yaml
AGENTS.md
Justfile
LICENSE
MANIFEST.in
README.md
mypy.ini
pyproject.toml
pytest.ini
ruff.toml
```

## Entry points

- [llm/__main__.py:3](https://github.com/simonw/llm/blob/8b475ffdfc2d33aa86c9518baff3ac94bcea409e/llm/__main__.py#L3)
- [llm/cli.py](https://github.com/simonw/llm/blob/8b475ffdfc2d33aa86c9518baff3ac94bcea409e/llm/cli.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AsyncChainResponse, AsyncConversation, AsyncKeyModel, AsyncModel, AsyncResponse, Attachment. Observed t… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AttachmentError, AttachmentType, FragmentNotFound, LoadTemplateError. Observed top-level f… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| llm package | library | Observed | Groups 16 file(s) under llm package (observed from repository paths and static analysis). Observed top-level classes: AsyncChat, AsyncResponses, AttachmentDict, AttachmentPart, AttachmentPartDict, AttachmentType. Observ… |
| Tests | test | Observed | Groups 51 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AsyncMockModel, AsyncServerToolsOnlyModel, AsyncSingleTurnModel, Counter, DemoServerSideTool, Discovery. Ob… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/cog.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/stable-docs.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `docs/plugins/llm-markov/pyproject.toml` (manifest)
- `docs/requirements.txt` (manifest)
- `mypy.ini` (config)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `ruff.toml` (config)

## Top-level layout

- `tests` — 51 analysed file(s)
- `docs` — 35 analysed file(s)
- `llm` — 20 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8b475ffdfc2d33aa86c9518baff3ac94bcea409e` is the revision these paths and observations refer to.
