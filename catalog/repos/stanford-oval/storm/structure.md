# Project structure: stanford-oval/storm

**Analysed commit:** `fb951af7744dab086e34962e9bc6fe878e145f83`

**Commit reference:** [fb951af7744dab086e34962e9bc6fe878e145f83](https://github.com/stanford-oval/storm/commit/fb951af7744dab086e34962e9bc6fe878e145f83)

**Tree at this commit:** [stanford-oval/storm@fb951af7744d](https://github.com/stanford-oval/storm/tree/fb951af7744dab086e34962e9bc6fe878e145f83)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | stanford-oval/storm |
| Description | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| Stars | 31878 |
| Forks | 3011 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `fb951af7744dab086e34962e9bc6fe878e145f83` |
| Retrieved at | 2026-11-14T19:07:07.711881+00:00 |
| Files in this snapshot | 67 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (2 files)
    format-check.yml
    python-package.yml
assets/  (1 files)
  logo.svg
examples/  (13 files)
  costorm_examples/  (1 files)
    run_costorm_gpt.py
  storm_examples/  (12 files)
    helper/  (1 files)
      … 1 files under this directory
    README.md
    run_storm_wiki_claude.py
    run_storm_wiki_deepseek.py
    run_storm_wiki_gemini.py
    run_storm_wiki_gpt.py
    run_storm_wiki_gpt_with_VectorRM.py
    run_storm_wiki_groq.py
    run_storm_wiki_mistral.py
    run_storm_wiki_ollama.py
    run_storm_wiki_ollama_with_searxng.py
    run_storm_wiki_serper.py
frontend/  (8 files)
  demo_light/  (8 files)
    .streamlit/  (1 files)
      … 1 files under this directory
    pages_util/  (2 files)
      … 2 files under this directory
    README.md
    demo_util.py
    requirements.txt
    stoc.py
    storm.py
knowledge_storm/  (34 files)
  collaborative_storm/  (15 files)
    modules/  (13 files)
      … 13 files under this directory
    __init__.py
    engine.py
  storm_wiki/  (11 files)
    modules/  (9 files)
      … 9 files under this directory
    __init__.py
    engine.py
  __init__.py
  dataclass.py
  encoder.py
  interface.py
  lm.py
  logging_wrapper.py
  rm.py
  utils.py
.gitignore
.pre-commit-config.yaml
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
requirements.txt
setup.py
```

## Entry points

- [frontend/demo_light/storm.py:67](https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/frontend/demo_light/storm.py#L67)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 4 file(s) under frontend package (observed from repository paths and static analysis). Observed top-level classes: DemoFileIOHelper, DemoTextProcessingHelper, DemoUIHelper, StreamlitCallbackHandler, stoc. Observe… |
| knowledge_storm package | library | Observed | Groups 34 file(s) under knowledge_storm package (observed from repository paths and static analysis). Observed top-level classes: Agent, AnswerQuestion, AnswerQuestionModule, Article, ArticleGenerationModule, ArticlePol… |

## Important files

- `.github/workflows/format-check.yml` (ci)
- `.github/workflows/python-package.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `frontend/demo_light/.streamlit/config.toml` (config)
- `frontend/demo_light/requirements.txt` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `knowledge_storm` — 34 analysed file(s)
- `examples` — 13 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `frontend` — 8 analysed file(s)
- `.github` — 3 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `fb951af7744dab086e34962e9bc6fe878e145f83` is the revision these paths and observations refer to.
