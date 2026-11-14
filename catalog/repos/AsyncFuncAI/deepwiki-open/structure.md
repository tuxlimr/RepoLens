# Project structure: AsyncFuncAI/deepwiki-open

**Analysed commit:** `72f7d7f105f7e35851793e6c3eb43b82befe6a69`

**Commit reference:** [72f7d7f105f7e35851793e6c3eb43b82befe6a69](https://github.com/AsyncFuncAI/deepwiki-open/commit/72f7d7f105f7e35851793e6c3eb43b82befe6a69)

**Tree at this commit:** [AsyncFuncAI/deepwiki-open@72f7d7f105f7](https://github.com/AsyncFuncAI/deepwiki-open/tree/72f7d7f105f7e35851793e6c3eb43b82befe6a69)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | AsyncFuncAI/deepwiki-open |
| Description | Open Source DeepWiki: AI-Powered Wiki Generator for GitHub/Gitlab/Bitbucket Repositories. Join the discord: https://discord.gg/gMwThUMeme |
| Stars | 18421 |
| Forks | 2036 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `72f7d7f105f7e35851793e6c3eb43b82befe6a69` |
| Retrieved at | 2026-11-14T19:08:23.990951+00:00 |
| Files in this snapshot | 195 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    docker-build-push.yml
    helm-chart.yml
  ct.yaml
.vscode/  (1 files)
  launch.json
api/  (58 files)
  chat/  (3 files)
    __init__.py
    _prompts.py
    _stream.py
  clients/  (8 files)
    __init__.py
    anthropic.py
    bedrock.py
    dashscope.py
    google_embedder.py
    litellm.py
    ollama.py
    openrouter.py
  config/  (9 files)
    embedder.json
    embedder.json.bak
    embedder.litellm.json
    embedder.ollama.json.bak
    embedder.openai_compatible.json.bak
    generator.json
    generator.litellm.json
    lang.json
    repo.json
  rag/  (3 files)
    __init__.py
    pipeline.py
    rag.py
  routers/  (7 files)
    __init__.py
    auth.py
    chat.py
    codemap.py
    repo.py
    system.py
    wiki.py
  schemas/  (9 files)
    __init__.py
    auth.py
    base.py
    chat.py
    codemap.py
    io.py
    models.py
    repo.py
    wiki.py
  services/  (10 files)
    wiki/  (6 files)
      … 6 files under this directory
    __init__.py
    codemap.py
    deep_research.py
    research.py
  README.md
  __init__.py
  config.py
  logger.py
  main.py
  prompts.py
  pyproject.toml
  repository.py
  utils.py
charts/  (20 files)
  deepwiki-open/  (20 files)
    ci/  (2 files)
      … 2 files under this directory
    templates/  (10 files)
      … 10 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    .helmignore
    Chart.yaml
    README.md
    README.md.gotmpl
    values.schema.json
    values.yaml
public/  (5 files)
  file.svg
  globe.svg
  next.svg
  vercel.svg
  window.svg
src/  (51 files)
  app/  (16 files)
    [owner]/  (3 files)
      … 3 files under this directory
    api/  (9 files)
      … 9 files under this directory
    wiki/  (1 files)
      … 1 files under this directory
    globals.css
    layout.tsx
    page.tsx
  components/  (13 files)
    Ask.tsx
    CodeMap.tsx
    CodeViewer.tsx
    ConfigurationModal.tsx
    Markdown.tsx
    Mermaid.tsx
    ModelSelectionModal.tsx
    ProcessedProjects.tsx
    TokenInput.tsx
    UserSelector.tsx
    WikiTreeView.tsx
    WikiTypeSelector.tsx
    theme-toggle.tsx
  contexts/  (1 files)
    LanguageContext.tsx
  hooks/  (1 files)
    useProcessedProjects.ts
  messages/  (10 files)
    en.json
    es.json
    fr.json
    ja.json
    kr.json
    pt-br.json
    ru.json
    vi.json
    zh-tw.json
    zh.json
  types/  (3 files)
    wiki/  (2 files)
      … 2 files under this directory
    repoinfo.tsx
  utils/  (6 files)
    contentDisposition.ts
    getRepoUrl.tsx
    prepareRepo.ts
    urlDecoder.tsx
    websocketClient.ts
    wikiTask.ts
  i18n.ts
tests/  (26 files)
  api/  (2 files)
    __init__.py
    test_api.py
  backend/  (10 files)
    rag/  (1 files)
      … 1 files under this directory
    routers/  (2 files)
      … 2 files under this directory
    schemas/  (2 files)
      … 2 files under this directory
    services/  (5 files)
      … 5 files under this directory
  frontend/  (1 files)
    contentDisposition.test.mjs
  integration/  (2 files)
    __init__.py
    test_full_integration.py
  unit/  (4 files)
    __init__.py
    test_all_embedders.py
    test_chat.py
    test_google_embedder.py
  README.md
  __init__.py
  conftest.py
  run_tests.py
  test_config.py
  test_extract_repo_name.py
  test_repository.py
.dockerignore
.gitignore
.pre-commit-config.yaml
.python-version
Dockerfile
Dockerfile-litellm
Dockerfile-ollama-local
LICENSE
Ollama-instruction.md
README.es.md
README.fr.md
README.ja.md
README.kr.md
README.md
README.pt-br.md
README.ru.md
README.vi.md
README.zh-tw.md
README.zh.md
docker-compose-litellm.env
docker-compose-litellm.yml
docker-compose.yml
eslint.config.mjs
litellm-config.yml
… 7 more files
```

## Entry points

- [api/main.py:50](https://github.com/AsyncFuncAI/deepwiki-open/blob/72f7d7f105f7e35851793e6c3eb43b82befe6a69/api/main.py#L50)
- [src/app/page.tsx](https://github.com/AsyncFuncAI/deepwiki-open/blob/72f7d7f105f7e35851793e6c3eb43b82befe6a69/src/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 55 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /status, POST /validate, POST /chat/completions/stream, POST /codemap/stream, GET /codemap/file. Observed top-… |
| app package | library | Observed | Groups 6 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 13 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 38 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| contexts package | library | Observed | Groups 1 file(s) under contexts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /. Observed top-level functions: root. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 1 file(s) under hooks package (observed from repository paths and static analysis). |
| i18n.ts package | library | Observed | Groups 1 file(s) under i18n.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 29 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Message, TestDataPipelineFunctions, TestEmbedderClients, TestEmbedderConfiguration, TestEmbedderFactory, Te… |
| types package | library | Observed | Groups 3 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 6 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/ct.yaml` (config)
- `.github/workflows/docker-build-push.yml` (ci)
- `.github/workflows/helm-chart.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/launch.json` (config)
- `Dockerfile` (container)
- `Dockerfile-litellm` (container)
- `Dockerfile-ollama-local` (container)
- `api/config/embedder.json` (config)
- `api/config/embedder.litellm.json` (config)
- `api/config/generator.json` (config)
- `api/config/generator.litellm.json` (config)
- `api/config/lang.json` (config)
- `api/config/repo.json` (config)
- `api/pyproject.toml` (manifest)
- `charts/deepwiki-open/Chart.yaml` (config)
- `charts/deepwiki-open/ci/default-values.yaml` (config)
- `charts/deepwiki-open/ci/no-persistence-values.yaml` (config)
- `charts/deepwiki-open/templates/configmap.yaml` (config)
- `charts/deepwiki-open/templates/deployment.yaml` (config)
- `charts/deepwiki-open/templates/httproute.yaml` (config)
- `charts/deepwiki-open/templates/ingress.yaml` (config)
- `charts/deepwiki-open/templates/pvc.yaml` (config)
- `charts/deepwiki-open/templates/service.yaml` (config)
- `charts/deepwiki-open/templates/serviceaccount.yaml` (config)
- `charts/deepwiki-open/values.schema.json` (config)
- `charts/deepwiki-open/values.yaml` (config)
- `docker-compose-litellm.yml` (config)
- `docker-compose.yml` (container)
- `litellm-config.yml` (config)
- `package.json` (manifest)
- `pytest.ini` (config)
- `src/messages/en.json` (config)
- `src/messages/es.json` (config)
- `src/messages/fr.json` (config)
- `src/messages/ja.json` (config)
- `src/messages/kr.json` (config)
- `src/messages/pt-br.json` (config)
- `src/messages/ru.json` (config)
- `src/messages/vi.json` (config)
- `src/messages/zh-tw.json` (config)
- `src/messages/zh.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `api` — 58 analysed file(s)
- `src` — 51 analysed file(s)
- `(root files)` — 31 analysed file(s)
- `tests` — 26 analysed file(s)
- `charts` — 20 analysed file(s)
- `public` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `72f7d7f105f7e35851793e6c3eb43b82befe6a69` is the revision these paths and observations refer to.
