# Project structure: petergyang/no-ai-slop

**Analysed commit:** `000650b156983f5159695b441477f4e63b25dc85`

**Commit reference:** [000650b156983f5159695b441477f4e63b25dc85](https://github.com/petergyang/no-ai-slop/commit/000650b156983f5159695b441477f4e63b25dc85)

**Tree at this commit:** [petergyang/no-ai-slop@000650b15698](https://github.com/petergyang/no-ai-slop/tree/000650b156983f5159695b441477f4e63b25dc85)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | petergyang/no-ai-slop |
| Description | Removes 20+ patterns of AI slop from any piece of writing. |
| Stars | 13498 |
| Forks | 945 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `000650b156983f5159695b441477f4e63b25dc85` |
| Retrieved at | 2026-11-14T19:09:48.399288+00:00 |
| Files in this snapshot | 13 |

## Directory tree

```text
.codex-plugin/  (1 files)
  plugin.json
.github/  (1 files)
  workflows/  (1 files)
    plugin.yml
agents/  (1 files)
  openai.yaml
scripts/  (1 files)
  build_plugin.py
skills/  (3 files)
  no-ai-slop/  (3 files)
    agents/  (1 files)
      … 1 files under this directory
    SKILL.md
    eval.md
.gitignore
LICENSE
PRIVACY.md
README.md
TERMS.md
plugin-submission.md
```

## Entry points

- [scripts/build_plugin.py:126](https://github.com/petergyang/no-ai-slop/blob/000650b156983f5159695b441477f4e63b25dc85/scripts/build_plugin.py#L126)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: build_plugin, main, parse_args, validate_build, validate_source. |

## Important files

- `.codex-plugin/plugin.json` (config)
- `.github/workflows/plugin.yml` (ci)
- `agents/openai.yaml` (config)
- `skills/no-ai-slop/agents/openai.yaml` (config)

## Top-level layout

- `(root files)` — 6 analysed file(s)
- `skills` — 3 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)
- `.github` — 1 analysed file(s)
- `agents` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `000650b156983f5159695b441477f4e63b25dc85` is the revision these paths and observations refer to.
