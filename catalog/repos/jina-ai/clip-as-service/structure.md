# Project structure: jina-ai/clip-as-service

**Analysed commit:** `03410570d4398084f5ca5c88ad968248e0f3fc5d`

**Commit reference:** [03410570d4398084f5ca5c88ad968248e0f3fc5d](https://github.com/jina-ai/clip-as-service/commit/03410570d4398084f5ca5c88ad968248e0f3fc5d)

**Tree at this commit:** [jina-ai/clip-as-service@03410570d439](https://github.com/jina-ai/clip-as-service/tree/03410570d4398084f5ca5c88ad968248e0f3fc5d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jina-ai/clip-as-service |
| Description | 🏄 Scalable embedding, reasoning, ranking for images and sentences with CLIP |
| Stars | 12841 |
| Forks | 2063 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `03410570d4398084f5ca5c88ad968248e0f3fc5d` |
| Retrieved at | 2026-11-14T19:09:58.697681+00:00 |
| Files in this snapshot | 123 |

## Directory tree

```text
.github/  (16 files)
  README-exec/  (2 files)
    onnx.readme.md
    torch.readme.md
  README-img/  (2 files)
    banner.svg
    rerank-chart.svg
  workflows/  (9 files)
    cd.yml
    ci.yml
    force-docker-build-cas.yml
    force-docker-build.yml
    force-docs-build.yml
    force-hub-push.yml
    force-release.yml
    label-pr.yml
    tag.yml
  codecov.yml
  labeler.yml
  release-template.ejs
Dockerfiles/  (4 files)
  base.Dockerfile
  cuda.Dockerfile
  server.Dockerfile
  tensorrt.Dockerfile
client/  (4 files)
  clip_client/  (3 files)
    __init__.py
    client.py
    helper.py
  setup.py
docs/  (44 files)
  _static/  (20 files)
    JCloud-dark.svg
    JCloud-light.svg
    cas-dark.svg
    cas-grafana.json
    cas-light.svg
    demo-embed.html
    demo-text-rank.html
    docarray-dark.svg
    docarray-light.svg
    finetuner-dark.svg
    finetuner-light.svg
    hub-dark.svg
    hub-light.svg
    logo-dark.svg
    logo-light.svg
    main.css
    now-dark.svg
    now-light.svg
    search-dark.svg
    search-light.svg
  _templates/  (3 files)
    sidebar/  (2 files)
      … 2 files under this directory
    page.html
  changelog/  (1 files)
    index.md
  hosting/  (5 files)
    by-jina.md
    cas-on-colab.ipynb
    cas-on-colab.svg
    colab.md
    on-jcloud.md
  html_extra/  (1 files)
    robots.txt
  playground/  (3 files)
    embedding.md
    reasoning.md
    searching.md
  user-guides/  (6 files)
    benchmark.rst
    client.md
    faq.md
    finetuner.md
    retriever.md
    server.md
  Makefile
  conf.py
  index.md
  makedoc.sh
  requirements.txt
scripts/  (10 files)
  MANIFEST.in
  benchmark.py
  black.sh
  docstrings_lint.sh
  get-all-test-paths.sh
  get-last-release-note.py
  get-requirements.py
  onnx_helper.py
  release.sh
  setup.py
server/  (27 files)
  clip_server/  (25 files)
    executors/  (5 files)
      … 5 files under this directory
    model/  (14 files)
      … 14 files under this directory
    __init__.py
    __main__.py
    helper.py
    onnx-flow.yml
    tensorrt-flow.yml
    torch-flow.yml
  MANIFEST.in
  setup.py
tests/  (12 files)
  __init__.py
  conftest.py
  test_asyncio.py
  test_client.py
  test_helper.py
  test_model.py
  test_ranker.py
  test_search.py
  test_server.py
  test_simple.py
  test_tensorrt.py
  test_tokenization.py
.dockerignore
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
LICENSE
README.md
```

## Entry points

- [scripts/benchmark.py:107](https://github.com/jina-ai/clip-as-service/blob/03410570d4398084f5ca5c88ad968248e0f3fc5d/scripts/benchmark.py#L107)
- [server/clip_server/__main__.py:5](https://github.com/jina-ai/clip-as-service/blob/03410570d4398084f5ca5c88ad968248e0f3fc5d/server/clip_server/__main__.py#L5)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: CLIP, CLIPTextCfg, CLIPVisionCfg, CustomTextCLIP, ModifiedResNet, ResidualAttentionBlock. Observed top-… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BenchmarkClient. Observed top-level functions: main, warn. |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Client. Observed top-level functions: _version_check, is_latest_version. |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: convert_float_to_float16, quantize. |
| server package | library | Observed | Groups 20 file(s) under server package (observed from repository paths and static analysis). Observed top-level classes: BaseCLIPModel, CLIPEncoder, CLIPModel, CLIPOnnxModel, CLIPTensorRTModel, CNClipModel. Observed top… |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ErrorExec, Exec1, Exec2. Observed top-level functions: another_heavylifting_job, make_flow, make_search_flo… |

## Important files

- `.dockerignore` (container)
- `.github/codecov.yml` (config)
- `.github/labeler.yml` (config)
- `.github/workflows/cd.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/force-docker-build-cas.yml` (ci)
- `.github/workflows/force-docker-build.yml` (ci)
- `.github/workflows/force-docs-build.yml` (ci)
- `.github/workflows/force-hub-push.yml` (ci)
- `.github/workflows/force-release.yml` (ci)
- `.github/workflows/label-pr.yml` (ci)
- `.github/workflows/tag.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `client/setup.py` (manifest)
- `docs/_static/cas-grafana.json` (config)
- `docs/requirements.txt` (manifest)
- `scripts/MANIFEST.in` (manifest)
- `scripts/setup.py` (manifest)
- `server/MANIFEST.in` (manifest)
- `server/clip_server/onnx-flow.yml` (config)
- `server/clip_server/tensorrt-flow.yml` (config)
- `server/clip_server/torch-flow.yml` (config)
- `server/setup.py` (manifest)

## Top-level layout

- `docs` — 44 analysed file(s)
- `server` — 27 analysed file(s)
- `.github` — 16 analysed file(s)
- `tests` — 12 analysed file(s)
- `scripts` — 10 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `Dockerfiles` — 4 analysed file(s)
- `client` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `03410570d4398084f5ca5c88ad968248e0f3fc5d` is the revision these paths and observations refer to.
