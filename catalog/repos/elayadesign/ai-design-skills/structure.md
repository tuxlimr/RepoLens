# Project structure: elayadesign/ai-design-skills

**Analysed commit:** `456d9e0d3e2d84c748bb143c6ca3d90c45e16213`

**Commit reference:** [456d9e0d3e2d84c748bb143c6ca3d90c45e16213](https://github.com/elayadesign/ai-design-skills/commit/456d9e0d3e2d84c748bb143c6ca3d90c45e16213)

**Tree at this commit:** [elayadesign/ai-design-skills@456d9e0d3e2d](https://github.com/elayadesign/ai-design-skills/tree/456d9e0d3e2d84c748bb143c6ca3d90c45e16213)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | elayadesign/ai-design-skills |
| Description | Not provided |
| Stars | 15534 |
| Forks | 1195 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `456d9e0d3e2d84c748bb143c6ca3d90c45e16213` |
| Retrieved at | 2026-11-14T19:09:01.036530+00:00 |
| Files in this snapshot | 8 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    validate-skills.yml
scripts/  (1 files)
  validate_skills.py
skills/  (2 files)
  figma-designer/  (1 files)
    SKILL.md
  landing-page-design/  (1 files)
    SKILL.md
tests/  (1 files)
  test_validate_skills.py
.gitignore
LICENSE
README.md
```

## Entry points

- [scripts/validate_skills.py:127](https://github.com/elayadesign/ai-design-skills/blob/456d9e0d3e2d84c748bb143c6ca3d90c45e16213/scripts/validate_skills.py#L127)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: check_text_field, main, read_frontmatter, report, validate_skill. |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: MainTest, ValidateSkillTest. |

## Important files

- `.github/workflows/validate-skills.yml` (ci)

## Top-level layout

- `(root files)` — 3 analysed file(s)
- `skills` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `456d9e0d3e2d84c748bb143c6ca3d90c45e16213` is the revision these paths and observations refer to.
