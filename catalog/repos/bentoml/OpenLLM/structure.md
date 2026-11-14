# Project structure: bentoml/OpenLLM

**Analysed commit:** `200b37fbf6f75b174e0737b937b886af460495e9`

**Commit reference:** [200b37fbf6f75b174e0737b937b886af460495e9](https://github.com/bentoml/OpenLLM/commit/200b37fbf6f75b174e0737b937b886af460495e9)

**Tree at this commit:** [bentoml/OpenLLM@200b37fbf6f7](https://github.com/bentoml/OpenLLM/tree/200b37fbf6f75b174e0737b937b886af460495e9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bentoml/OpenLLM |
| Description | Run any open-source LLMs, such as DeepSeek and Llama, as OpenAI compatible API endpoint in the cloud. |
| Stars | 12600 |
| Forks | 848 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `200b37fbf6f75b174e0737b937b886af460495e9` |
| Retrieved at | 2026-11-14T19:10:03.880603+00:00 |
| Files in this snapshot | 40 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (2 files)
    create-releases.yml
    dependabot-auto-merge.yml
  CODEOWNERS
  CODE_OF_CONDUCT.md
  SECURITY.md
  dependabot.yml
src/  (12 files)
  openllm/  (12 files)
    __init__.py
    __main__.py
    accelerator_spec.py
    analytic.py
    clean.py
    cloud.py
    common.py
    local.py
    model.py
    py.typed
    repo.py
    venv.py
.editorconfig
.envrc.template
.git-blame-ignore-revs
.git_archival.txt
.gitattributes
.gitignore
.pre-commit-config.yaml
.python-version-default
.ruff.toml
CITATION.cff
DEVELOPMENT.md
LICENSE
README.md
README.md.tpl
SECURITY.md
gen_readme.py
pyproject.toml
pyrightconfig.json
release.sh
```

## Entry points

- [src/openllm/__main__.py](https://github.com/bentoml/OpenLLM/blob/200b37fbf6f75b174e0737b937b886af460495e9/src/openllm/__main__.py)
- [src/openllm/clean.py:32](https://github.com/bentoml/OpenLLM/blob/200b37fbf6f75b174e0737b937b886af460495e9/src/openllm/clean.py#L32)
- [src/openllm/model.py:16](https://github.com/bentoml/OpenLLM/blob/200b37fbf6f75b174e0737b937b886af460495e9/src/openllm/model.py#L16)
- [src/openllm/repo.py:25](https://github.com/bentoml/OpenLLM/blob/200b37fbf6f75b174e0737b937b886af460495e9/src/openllm/repo.py#L25)
- [gen_readme.py:11](https://github.com/bentoml/OpenLLM/blob/200b37fbf6f75b174e0737b937b886af460495e9/gen_readme.py#L11)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: _extract_first_number, ensure_bento, get, list_bento, list_model. |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _clone_repo, _complete_alias, _select_action, _select_bento_name, _select_bento_version,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| openllm package | library | Observed | Groups 8 file(s) under openllm package (observed from repository paths and static analysis). Observed top-level classes: Accelerator, BentoInfo, BentoMetadata, CliEvent, Config, ContextVar. Observed top-level functions:… |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/create-releases.yml` (ci)
- `.github/workflows/dependabot-auto-merge.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.ruff.toml` (config)
- `pyproject.toml` (manifest)
- `pyrightconfig.json` (config)

## Top-level layout

- `(root files)` — 19 analysed file(s)
- `src` — 12 analysed file(s)
- `.github` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `200b37fbf6f75b174e0737b937b886af460495e9` is the revision these paths and observations refer to.
