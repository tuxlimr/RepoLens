# Project structure: fauxpilot/fauxpilot

**Analysed commit:** `788edd44f29b3a3c33136f956c8c20d055604438`

**Commit reference:** [788edd44f29b3a3c33136f956c8c20d055604438](https://github.com/fauxpilot/fauxpilot/commit/788edd44f29b3a3c33136f956c8c20d055604438)

**Tree at this commit:** [fauxpilot/fauxpilot@788edd44f29b](https://github.com/fauxpilot/fauxpilot/tree/788edd44f29b3a3c33136f956c8c20d055604438)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fauxpilot/fauxpilot |
| Description | FauxPilot - an open-source alternative to GitHub Copilot server |
| Stars | 14649 |
| Forks | 637 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `788edd44f29b3a3c33136f956c8c20d055604438` |
| Retrieved at | 2026-11-14T19:09:22.290822+00:00 |
| Files in this snapshot | 111 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    Bug_report.md
    Feature_request.md
    Support_request.md
  workflows/  (3 files)
    lint.yml
    publish-docker-images.yaml
    python_backend_tests.yaml
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
converter/  (67 files)
  models/  (60 files)
    codegen-16B-mono-1gpu/  (2 files)
      … 2 files under this directory
    codegen-16B-mono-2gpu/  (2 files)
      … 2 files under this directory
    codegen-16B-mono-4gpu/  (1 files)
      … 1 files under this directory
    codegen-16B-multi-1gpu/  (2 files)
      … 2 files under this directory
    codegen-16B-multi-2gpu/  (2 files)
      … 2 files under this directory
    codegen-16B-multi-4gpu/  (1 files)
      … 1 files under this directory
    codegen-16B-nl-1gpu/  (2 files)
      … 2 files under this directory
    codegen-16B-nl-2gpu/  (2 files)
      … 2 files under this directory
    codegen-16B-nl-4gpu/  (1 files)
      … 1 files under this directory
    codegen-2B-mono-1gpu/  (2 files)
      … 2 files under this directory
    codegen-2B-mono-2gpu/  (2 files)
      … 2 files under this directory
    codegen-2B-mono-4gpu/  (1 files)
      … 1 files under this directory
    codegen-2B-multi-1gpu/  (2 files)
      … 2 files under this directory
    codegen-2B-multi-2gpu/  (2 files)
      … 2 files under this directory
    codegen-2B-multi-4gpu/  (1 files)
      … 1 files under this directory
    codegen-2B-nl-1gpu/  (2 files)
      … 2 files under this directory
    codegen-2B-nl-2gpu/  (2 files)
      … 2 files under this directory
    codegen-2B-nl-4gpu/  (1 files)
      … 1 files under this directory
    codegen-350M-mono-1gpu/  (2 files)
      … 2 files under this directory
    codegen-350M-mono-2gpu/  (2 files)
      … 2 files under this directory
    codegen-350M-mono-4gpu/  (1 files)
      … 1 files under this directory
    codegen-350M-multi-1gpu/  (2 files)
      … 2 files under this directory
    codegen-350M-multi-2gpu/  (2 files)
      … 2 files under this directory
    codegen-350M-multi-4gpu/  (1 files)
      … 1 files under this directory
    codegen-350M-nl-1gpu/  (2 files)
      … 2 files under this directory
    codegen-350M-nl-2gpu/  (2 files)
      … 2 files under this directory
    codegen-350M-nl-4gpu/  (1 files)
      … 1 files under this directory
    codegen-6B-mono-1gpu/  (2 files)
      … 2 files under this directory
    codegen-6B-mono-2gpu/  (2 files)
      … 2 files under this directory
    codegen-6B-mono-4gpu/  (1 files)
      … 1 files under this directory
    codegen-6B-multi-1gpu/  (2 files)
      … 2 files under this directory
    codegen-6B-multi-2gpu/  (2 files)
      … 2 files under this directory
    codegen-6B-multi-4gpu/  (1 files)
      … 1 files under this directory
    codegen-6B-nl-1gpu/  (2 files)
      … 2 files under this directory
    codegen-6B-nl-2gpu/  (2 files)
      … 2 files under this directory
    codegen-6B-nl-4gpu/  (1 files)
      … 1 files under this directory
  Dockerfile
  README.md
  codegen_gptj_convert.py
  config_template.pbtxt
  download_and_convert_model.sh
  huggingface_gptj_convert.py
  triton_config_gen.py
copilot_proxy/  (12 files)
  cgtok/  (3 files)
    added_tokens.json
    special_tokens_map.json
    tokenizer_config.json
  config/  (2 files)
    __init__.py
    log_config.py
  utils/  (3 files)
    __init__.py
    codegen.py
    errors.py
  __init__.py
  app.py
  models.py
  requirements.txt
documentation/  (2 files)
  client.md
  server.md
python_backend/  (3 files)
  config_template.pbtxt
  init_model.py
  model.py
tests/  (6 files)
  python_backend/  (6 files)
    .gitignore
    docker-compose-with-gpus.yaml
    docker-compose-without-gpus.yaml
    requirements.txt
    runner.env
    test_setup.py
.editorconfig
.gitignore
LICENSE
README.md
api.dockerignore
docker-compose.yaml
launch.sh
proxy.Dockerfile
setup.cfg
setup.sh
shutdown.sh
triton.Dockerfile
triton.dockerignore
```

## Entry points

- [converter/huggingface_gptj_convert.py:178](https://github.com/fauxpilot/fauxpilot/blob/788edd44f29b3a3c33136f956c8c20d055604438/converter/huggingface_gptj_convert.py#L178)
- [copilot_proxy/app.py:22](https://github.com/fauxpilot/fauxpilot/blob/788edd44f29b3a3c33136f956c8c20d055604438/copilot_proxy/app.py#L22)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| converter package | library | Observed | Groups 3 file(s) under converter package (observed from repository paths and static analysis). Observed top-level functions: replace, replace_by_name, round_up. |
| copilot_proxy package | library | Observed | Groups 4 file(s) under copilot_proxy package (observed from repository paths and static analysis). Observed top-level classes: CodeGenProxy, FauxPilotException. |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: OpenAIinput, TritonPythonModel. Observed top-level functions: pb2torch, torch2pb. |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /copilot_internal/v2/token, POST /v1/engines/cod… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| python_backend package | library | Observed | Groups 1 file(s) under python_backend package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: enter_input, load_test_env, run_common_setup_steps, run_inference, setup_module, teardown_module. |

## Important files

- `.editorconfig` (config)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/publish-docker-images.yaml` (ci)
- `.github/workflows/python_backend_tests.yaml` (ci)
- `converter/Dockerfile` (container)
- `copilot_proxy/cgtok/added_tokens.json` (config)
- `copilot_proxy/cgtok/special_tokens_map.json` (config)
- `copilot_proxy/cgtok/tokenizer_config.json` (config)
- `copilot_proxy/requirements.txt` (manifest)
- `docker-compose.yaml` (container)
- `setup.cfg` (manifest)

## Top-level layout

- `converter` — 67 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `copilot_proxy` — 12 analysed file(s)
- `.github` — 8 analysed file(s)
- `tests` — 6 analysed file(s)
- `python_backend` — 3 analysed file(s)
- `documentation` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `788edd44f29b3a3c33136f956c8c20d055604438` is the revision these paths and observations refer to.
