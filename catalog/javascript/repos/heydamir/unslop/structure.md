# Project structure: heydamir/unslop

**Analysed commit:** `97daa3eb365670ea3f87ed85356cbfcee18105a5`

**Commit reference:** [97daa3eb365670ea3f87ed85356cbfcee18105a5](https://github.com/heydamir/unslop/commit/97daa3eb365670ea3f87ed85356cbfcee18105a5)

**Tree at this commit:** [heydamir/unslop@97daa3eb3656](https://github.com/heydamir/unslop/tree/97daa3eb365670ea3f87ed85356cbfcee18105a5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | heydamir/unslop |
| Description | A Claude skill that turns vibecoded, AI-looking UI into a designed interface |
| Stars | 15941 |
| Forks | 927 |
| Licence | CC-BY-4.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `97daa3eb365670ea3f87ed85356cbfcee18105a5` |
| Retrieved at | 2026-11-14T19:11:34.760992+00:00 |
| Files in this snapshot | 17 |

## Directory tree

```text
examples/  (2 files)
  dashboard.html
  hero.html
skills/  (9 files)
  unslop/  (9 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (5 files)
      … 5 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    SKILL.md
test/  (2 files)
  snapshot.test.mjs
  story.test.mjs
.gitignore
CITATION.cff
LICENSE
README.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 2 file(s) under skills package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `skills/unslop/agents/openai.yaml` (config)

## Top-level layout

- `skills` — 9 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `examples` — 2 analysed file(s)
- `test` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `97daa3eb365670ea3f87ed85356cbfcee18105a5` is the revision these paths and observations refer to.
