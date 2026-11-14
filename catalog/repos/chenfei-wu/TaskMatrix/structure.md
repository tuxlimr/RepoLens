# Project structure: chenfei-wu/TaskMatrix

**Analysed commit:** `4b7664f8d3a23804ac1b795d75a73efd162769f0`

**Commit reference:** [4b7664f8d3a23804ac1b795d75a73efd162769f0](https://github.com/chenfei-wu/TaskMatrix/commit/4b7664f8d3a23804ac1b795d75a73efd162769f0)

**Tree at this commit:** [chenfei-wu/TaskMatrix@4b7664f8d3a2](https://github.com/chenfei-wu/TaskMatrix/tree/4b7664f8d3a23804ac1b795d75a73efd162769f0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chenfei-wu/TaskMatrix |
| Description | Not provided |
| Stars | 33896 |
| Forks | 3184 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `4b7664f8d3a23804ac1b795d75a73efd162769f0` |
| Retrieved at | 2026-11-14T19:07:00.189248+00:00 |
| Files in this snapshot | 25 |

## Directory tree

```text
LowCodeLLM/  (17 files)
  src/  (14 files)
    test/  (6 files)
      … 6 files under this directory
    app.py
    executingLLM.py
    index.html
    lowCodeLLM.py
    openAIWrapper.py
    planningLLM.py
    requirements.txt
    supervisord.conf
  Dockerfile
  README.md
  config.template
TaskMatrix.AI/  (1 files)
  README.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.txt
README.md
SECURITY.md
requirements.txt
visual_chatgpt.py
```

## Entry points

- [LowCodeLLM/src/app.py:11](https://github.com/chenfei-wu/TaskMatrix/blob/4b7664f8d3a23804ac1b795d75a73efd162769f0/LowCodeLLM/src/app.py#L11)
- [visual_chatgpt.py:1555](https://github.com/chenfei-wu/TaskMatrix/blob/4b7664f8d3a23804ac1b795d75a73efd162769f0/visual_chatgpt.py#L1555)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /api/get_workflow, ROUTE /api/extend_wo… |
| LowCodeLLM package | library | Observed | Groups 4 file(s) under lowcodellm package (observed from repository paths and static analysis). Observed top-level classes: OpenAIWrapper, executingLLM, lowCodeLLM, planningLLM. |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: test_extend_workflow, test_get_workflow. |

## Important files

- `LowCodeLLM/Dockerfile` (container)
- `LowCodeLLM/src/requirements.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `LowCodeLLM` — 17 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `TaskMatrix.AI` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4b7664f8d3a23804ac1b795d75a73efd162769f0` is the revision these paths and observations refer to.
