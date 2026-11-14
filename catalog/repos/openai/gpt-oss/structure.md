# Project structure: openai/gpt-oss

**Analysed commit:** `277020131d524f06bed5f66b694a92ed7f6e5224`

**Commit reference:** [277020131d524f06bed5f66b694a92ed7f6e5224](https://github.com/openai/gpt-oss/commit/277020131d524f06bed5f66b694a92ed7f6e5224)

**Tree at this commit:** [openai/gpt-oss@277020131d52](https://github.com/openai/gpt-oss/tree/277020131d524f06bed5f66b694a92ed7f6e5224)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/gpt-oss |
| Description | gpt-oss-120b and gpt-oss-20b are two open-weight language models by OpenAI |
| Stars | 20533 |
| Forks | 2196 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `277020131d524f06bed5f66b694a92ed7f6e5224` |
| Retrieved at | 2026-11-14T19:08:04.482371+00:00 |
| Files in this snapshot | 154 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (1 files)
    config.yml
  workflows/  (1 files)
    CI.yml
  CODEOWNERS
_build/  (2 files)
  gpt_oss_build_backend/  (2 files)
    __init__.py
    backend.py
compatibility-test/  (9 files)
  .gitignore
  README.md
  analysis.ts
  cases.jsonl
  index.ts
  package.json
  providers.ts
  runCase.ts
  tools.ts
examples/  (6 files)
  agents-sdk-js/  (2 files)
    index.ts
    package.json
  agents-sdk-python/  (2 files)
    example.py
    pyproject.toml
  gradio/  (1 files)
    gradio_chat.py
  streamlit/  (1 files)
    streamlit_chat.py
gpt-oss-mcp-server/  (6 files)
  README.md
  browser_server.py
  build-system-prompt.py
  pyproject.toml
  python_server.py
  reference-system-prompt.py
gpt_oss/  (114 files)
  evals/  (12 files)
    README.md
    __init__.py
    __main__.py
    abcd_grader.py
    aime_eval.py
    basic_eval.py
    chat_completions_sampler.py
    gpqa_eval.py
    healthbench_eval.py
    report.py
    responses_sampler.py
    types.py
  metal/  (67 files)
    benchmark/  (6 files)
      … 6 files under this directory
    examples/  (2 files)
      … 2 files under this directory
    include/  (4 files)
      … 4 files under this directory
    python/  (5 files)
      … 5 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    source/  (35 files)
      … 35 files under this directory
    test/  (12 files)
      … 12 files under this directory
    CMakeLists.txt
    __init__.py
  responses_api/  (13 files)
    inference/  (7 files)
      … 7 files under this directory
    __init__.py
    api_server.py
    events.py
    serve.py
    types.py
    utils.py
  tools/  (9 files)
    python_docker/  (1 files)
      … 1 files under this directory
    simple_browser/  (4 files)
      … 4 files under this directory
    __init__.py
    apply_patch.md
    apply_patch.py
    tool.py
  torch/  (4 files)
    __init__.py
    model.py
    utils.py
    weights.py
  triton/  (4 files)
    __init__.py
    attention.py
    model.py
    moe.py
  vllm/  (1 files)
    token_generator.py
  __init__.py
  chat.py
  generate.py
  tokenizer.py
tests/  (4 files)
  gpt_oss/  (1 files)
    tools/  (1 files)
      … 1 files under this directory
  conftest.py
  test_api_endpoints.py
  test_responses_api.py
tests-data/  (2 files)
  basic-event-stream.txt
  web-search-event-stream.txt
.gitignore
CMakeLists.txt
LICENSE
MANIFEST.in
README.md
USAGE_POLICY
awesome-gpt-oss.md
pyproject.toml
```

## Entry points

- [gpt_oss/chat.py:289](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/gpt_oss/chat.py#L289)
- [gpt_oss/evals/__main__.py:210](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/gpt_oss/evals/__main__.py#L210)
- [gpt_oss/evals/abcd_grader.py:119](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/gpt_oss/evals/abcd_grader.py#L119)
- [gpt_oss/evals/gpqa_eval.py:100](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/gpt_oss/evals/gpqa_eval.py#L100)
- [gpt_oss/evals/healthbench_eval.py:611](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/gpt_oss/evals/healthbench_eval.py#L611)
- [gpt_oss/generate.py:40](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/gpt_oss/generate.py#L40)
- [gpt_oss/metal/scripts/create-local-model.py:357](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/gpt_oss/metal/scripts/create-local-model.py#L357)
- [gpt_oss/responses_api/api_server.py:103](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/gpt_oss/responses_api/api_server.py#L103)
- [gpt_oss/responses_api/serve.py:13](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/gpt_oss/responses_api/serve.py#L13)
- [gpt_oss/tools/apply_patch.py:528](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/gpt_oss/tools/apply_patch.py#L528)
- [compatibility-test/index.ts](https://github.com/openai/gpt-oss/blob/277020131d524f06bed5f66b694a92ed7f6e5224/compatibility-test/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| _build package | library | Observed | Groups 2 file(s) under _build package (observed from repository paths and static analysis). Observed top-level functions: _backend, _scikit_build_backend, _setuptools_backend, _use_metal_backend, build_editable, build_s… |
| compatibility-test package | library | Observed | Groups 5 file(s) under compatibility-test package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AttentionBlock, Cache, MLPBlock, ModelConfig, RMSNorm, RotaryEmbedding. Observed top-level functions: _… |
| Application entry point | entrypoint | Observed | Groups 12 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: ActionType, Chunk, Commit, DiffError, Fi… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| gpt_oss package | library | Observed | Groups 61 file(s) under gpt_oss package (observed from repository paths and static analysis). Observed top-level classes: AIME25Eval, Backend, BackendError, BasicEval, BrowserToolConfig, ChatCompletionsSampler. Observed… |
| gpt-oss-mcp-server package | library | Observed | Groups 4 file(s) under gpt-oss-mcp-server package (observed from repository paths and static analysis). Observed top-level classes: AppContext. Observed top-level functions: app_lifespan, find_pattern, list_server_and_t… |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH aiohttp.ClientSession.get, PATCH aiohttp.ClientSession.get, PATCH aiohttp.ClientSession.get, PATCH aiohttp.Clien… |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/CI.yml` (ci)
- `MANIFEST.in` (manifest)
- `compatibility-test/package.json` (manifest)
- `examples/agents-sdk-js/package.json` (manifest)
- `examples/agents-sdk-python/pyproject.toml` (manifest)
- `gpt-oss-mcp-server/pyproject.toml` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `gpt_oss` — 114 analysed file(s)
- `compatibility-test` — 9 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `examples` — 6 analysed file(s)
- `gpt-oss-mcp-server` — 6 analysed file(s)
- `tests` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `_build` — 2 analysed file(s)
- `tests-data` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `277020131d524f06bed5f66b694a92ed7f6e5224` is the revision these paths and observations refer to.
