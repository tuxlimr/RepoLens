# Project structure: andkret/Cookbook

**Analysed commit:** `bf463f65b173aa4ecf02425456bd31c75878c188`

**Commit reference:** [bf463f65b173aa4ecf02425456bd31c75878c188](https://github.com/andkret/Cookbook/commit/bf463f65b173aa4ecf02425456bd31c75878c188)

**Tree at this commit:** [andkret/Cookbook@bf463f65b173](https://github.com/andkret/Cookbook/tree/bf463f65b173aa4ecf02425456bd31c75878c188)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | andkret/Cookbook |
| Description | The Data Engineering Cookbook |
| Stars | 15548 |
| Forks | 2764 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `bf463f65b173aa4ecf02425456bd31c75878c188` |
| Retrieved at | 2026-11-14T19:09:01.606126+00:00 |
| Files in this snapshot | 24 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    copy-to-documenation-branch.yml
    linkchecker.yml
Code Examples/  (8 files)
  GenAI-RAG/  (5 files)
    conversations.json
    cvpipeline.py
    docker-compose.yml
    index.py
    query.py
  #102 Spark Week Day 3.txt
  Movies.txt
  template-readme.md
sections/  (10 files)
  01-Introduction.md
  02-BasicSkills.md
  03-AdvancedSkills.md
  04-HandsOnCourse.md
  05-CaseStudies.md
  06-BestPracticesCloud.md
  07-DataSources.md
  08-InterviewQuestions.md
  09-BooksAndCourses.md
  10-Updates.md
.gitignore
FUNDING.yml
LICENSE
README.md
```

## Entry points

- [Code Examples/GenAI-RAG/cvpipeline.py:89](https://github.com/andkret/Cookbook/blob/bf463f65b173aa4ecf02425456bd31c75878c188/Code%20Examples/GenAI-RAG/cvpipeline.py#L89)
- [Code Examples/GenAI-RAG/index.py:67](https://github.com/andkret/Cookbook/blob/bf463f65b173aa4ecf02425456bd31c75878c188/Code%20Examples/GenAI-RAG/index.py#L67)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Code Examples package | library | Observed | Groups 1 file(s) under code examples package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: extract_text_from_pdf, get_documents_from_file, main, prepare_text_to_json. |

## Important files

- `.github/workflows/copy-to-documenation-branch.yml` (ci)
- `.github/workflows/linkchecker.yml` (ci)
- `Code Examples/GenAI-RAG/conversations.json` (config)
- `Code Examples/GenAI-RAG/docker-compose.yml` (container)
- `FUNDING.yml` (config)

## Top-level layout

- `sections` — 10 analysed file(s)
- `Code Examples` — 8 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bf463f65b173aa4ecf02425456bd31c75878c188` is the revision these paths and observations refer to.
