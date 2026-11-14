# Project structure: oso95/scroll-world

**Analysed commit:** `71cc36d3bb150248ae36a2c552f9cbf88802a79c`

**Commit reference:** [71cc36d3bb150248ae36a2c552f9cbf88802a79c](https://github.com/oso95/scroll-world/commit/71cc36d3bb150248ae36a2c552f9cbf88802a79c)

**Tree at this commit:** [oso95/scroll-world@71cc36d3bb15](https://github.com/oso95/scroll-world/tree/71cc36d3bb150248ae36a2c552f9cbf88802a79c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | oso95/scroll-world |
| Description | A skill that turn any brand into a scrollable 3D world landing page |
| Stars | 10995 |
| Forks | 1201 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `71cc36d3bb150248ae36a2c552f9cbf88802a79c` |
| Retrieved at | 2026-11-14T19:12:27.016151+00:00 |
| Files in this snapshot | 11 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
skills/  (6 files)
  scroll-world/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
.gitignore
LICENSE
README.md
```

## Entry points

- [skills/scroll-world/references/knockout.py:87](https://github.com/oso95/scroll-world/blob/71cc36d3bb150248ae36a2c552f9cbf88802a79c/skills/scroll-world/references/knockout.py#L87)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: corner_color, knock. |
| skills package | library | Observed | Groups 1 file(s) under skills package (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)

## Top-level layout

- `skills` — 6 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `71cc36d3bb150248ae36a2c552f9cbf88802a79c` is the revision these paths and observations refer to.
