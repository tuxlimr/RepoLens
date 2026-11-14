# Project structure: microsoft/JARVIS

**Analysed commit:** `7624cf388b47334ff8a0868e7d862dde18cfda86`

**Commit reference:** [7624cf388b47334ff8a0868e7d862dde18cfda86](https://github.com/microsoft/JARVIS/commit/7624cf388b47334ff8a0868e7d862dde18cfda86)

**Tree at this commit:** [microsoft/JARVIS@7624cf388b47](https://github.com/microsoft/JARVIS/tree/7624cf388b47334ff8a0868e7d862dde18cfda86)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/JARVIS |
| Description | JARVIS, a system to connect LLMs with ML community. Paper: https://arxiv.org/pdf/2303.17580.pdf |
| Stars | 25654 |
| Forks | 2291 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `7624cf388b47334ff8a0868e7d862dde18cfda86` |
| Retrieved at | 2026-11-14T19:07:31.245966+00:00 |
| Files in this snapshot | 87 |

## Directory tree

```text
easytool/  (14 files)
  data_funcqa/  (3 files)
    funchub/  (1 files)
      … 1 files under this directory
    tool_instruction/  (2 files)
      … 2 files under this directory
  data_restbench/  (1 files)
    tool_instruction/  (1 files)
      … 1 files under this directory
  easytool/  (6 files)
    __init__.py
    funcQA.py
    restbench.py
    toolbench.py
    toolbench_retrieve.py
    util.py
  README.md
  data_process.py
  main.py
  requirements.txt
hugginggpt/  (49 files)
  server/  (14 files)
    configs/  (4 files)
      … 4 files under this directory
    demos/  (3 files)
      … 3 files under this directory
    models/  (2 files)
      … 2 files under this directory
    awesome_chat.py
    get_token_ids.py
    models_server.py
    requirements.txt
    run_gradio_demo.py
  web/  (32 files)
    electron/  (4 files)
      … 4 files under this directory
    public/  (2 files)
      … 2 files under this directory
    src/  (18 files)
      … 18 files under this directory
    env.d.ts
    index.html
    package.json
    postcss.config.js
    tailwind.config.js
    tsconfig.config.json
    tsconfig.json
    vite.config.ts
  .dockerignore
  Dockerfile.jetson
  README.md
taskbench/  (16 files)
  data_dailylifeapis/  (2 files)
    graph_desc.json
    tool_desc.json
  data_huggingface/  (2 files)
    graph_desc.json
    tool_desc.json
  data_multimedia/  (2 files)
    graph_desc.json
    tool_desc.json
  README.md
  batch_evaluate.sh
  data_engine.py
  evaluate.py
  format_data.py
  generate_graph.py
  graph_sampler.py
  inference.py
  requirements.txt
  visualize_graph.py
.gitignore
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
SUPPORT.md
```

## Entry points

- [easytool/data_process.py:108](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/easytool/data_process.py#L108)
- [easytool/easytool/util.py:108](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/easytool/easytool/util.py#L108)
- [easytool/main.py:11](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/easytool/main.py#L11)
- [hugginggpt/server/awesome_chat.py:1019](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/hugginggpt/server/awesome_chat.py#L1019)
- [hugginggpt/server/models_server.py:71](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/hugginggpt/server/models_server.py#L71)
- [taskbench/data_engine.py:48](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/taskbench/data_engine.py#L48)
- [taskbench/evaluate.py:178](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/taskbench/evaluate.py#L178)
- [taskbench/format_data.py:60](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/taskbench/format_data.py#L60)
- [taskbench/generate_graph.py:49](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/taskbench/generate_graph.py#L49)
- [taskbench/graph_sampler.py:210](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/taskbench/graph_sampler.py#L210)
- [taskbench/inference.py:37](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/taskbench/inference.py#L37)
- [taskbench/visualize_graph.py:8](https://github.com/microsoft/JARVIS/blob/7624cf388b47334ff8a0868e7d862dde18cfda86/taskbench/visualize_graph.py#L8)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 26 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| easytool package | library | Observed | Groups 6 file(s) under easytool package (observed from repository paths and static analysis). Observed top-level functions: Call_function, add_, answer_check, answer_generation, answer_generation_depend, answer_generati… |
| Application entry point | entrypoint | Observed | Groups 12 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /running, ROUTE /status/<path:model_id>, ROUTE… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| hugginggpt package | library | Observed | Groups 14 file(s) under hugginggpt package (observed from repository paths and static analysis). Observed top-level functions: add_message, add_text, bot, count_tokens, extract_medias, get_max_context_length. |
| taskbench package | library | Observed | Groups 1 file(s) under taskbench package (observed from repository paths and static analysis). |

## Important files

- `easytool/data_funcqa/tool_instruction/functions_data.json` (config)
- `easytool/data_restbench/tool_instruction/tmdb_tool.json` (config)
- `easytool/requirements.txt` (manifest)
- `hugginggpt/.dockerignore` (container)
- `hugginggpt/Dockerfile.jetson` (container)
- `hugginggpt/server/configs/config.azure.yaml` (config)
- `hugginggpt/server/configs/config.default.yaml` (config)
- `hugginggpt/server/configs/config.gradio.yaml` (config)
- `hugginggpt/server/configs/config.lite.yaml` (config)
- `hugginggpt/server/demos/demo_choose_model.json` (config)
- `hugginggpt/server/demos/demo_parse_task.json` (config)
- `hugginggpt/server/demos/demo_response_results.json` (config)
- `hugginggpt/server/requirements.txt` (manifest)
- `hugginggpt/web/electron/electron-builder.yml` (config)
- `hugginggpt/web/electron/package.json` (manifest)
- `hugginggpt/web/package.json` (manifest)
- `hugginggpt/web/tsconfig.config.json` (config)
- `hugginggpt/web/tsconfig.json` (config)
- `taskbench/data_dailylifeapis/graph_desc.json` (config)
- `taskbench/data_dailylifeapis/tool_desc.json` (config)
- `taskbench/data_huggingface/graph_desc.json` (config)
- `taskbench/data_huggingface/tool_desc.json` (config)
- `taskbench/data_multimedia/graph_desc.json` (config)
- `taskbench/data_multimedia/tool_desc.json` (config)
- `taskbench/requirements.txt` (manifest)

## Top-level layout

- `hugginggpt` — 49 analysed file(s)
- `taskbench` — 16 analysed file(s)
- `easytool` — 14 analysed file(s)
- `(root files)` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7624cf388b47334ff8a0868e7d862dde18cfda86` is the revision these paths and observations refer to.
