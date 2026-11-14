# Project structure: anthropics/skills

**Analysed commit:** `1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064`

**Commit reference:** [1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064](https://github.com/anthropics/skills/commit/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064)

**Tree at this commit:** [anthropics/skills@1780c5e5a552](https://github.com/anthropics/skills/tree/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | anthropics/skills |
| Description | Public repository for Agent Skills |
| Stars | 194526 |
| Forks | 22893 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064` |
| Retrieved at | 2026-11-14T19:06:00.645291+00:00 |
| Files in this snapshot | 388 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
skills/  (382 files)
  academy-guide/  (2 files)
    LICENSE.txt
    SKILL.md
  algorithmic-art/  (4 files)
    templates/  (2 files)
      … 2 files under this directory
    LICENSE.txt
    SKILL.md
  brand-guidelines/  (2 files)
    LICENSE.txt
    SKILL.md
  canvas-design/  (29 files)
    canvas-fonts/  (27 files)
      … 27 files under this directory
    LICENSE.txt
    SKILL.md
  claude-api/  (95 files)
    csharp/  (5 files)
      … 5 files under this directory
    curl/  (2 files)
      … 2 files under this directory
    go/  (5 files)
      … 5 files under this directory
    java/  (5 files)
      … 5 files under this directory
    php/  (6 files)
      … 6 files under this directory
    python/  (7 files)
      … 7 files under this directory
    ruby/  (4 files)
      … 4 files under this directory
    shared/  (53 files)
      … 53 files under this directory
    typescript/  (6 files)
      … 6 files under this directory
    LICENSE.txt
    SKILL.md
  discernment-nudge/  (2 files)
    LICENSE.txt
    SKILL.md
  doc-coauthoring/  (1 files)
    SKILL.md
  docx/  (60 files)
    scripts/  (58 files)
      … 58 files under this directory
    LICENSE.txt
    SKILL.md
  frontend-design/  (2 files)
    LICENSE.txt
    SKILL.md
  internal-comms/  (6 files)
    examples/  (4 files)
      … 4 files under this directory
    LICENSE.txt
    SKILL.md
  mcp-builder/  (11 files)
    reference/  (5 files)
      … 5 files under this directory
    scripts/  (4 files)
      … 4 files under this directory
    LICENSE.txt
    SKILL.md
  pdf/  (12 files)
    scripts/  (8 files)
      … 8 files under this directory
    FORMS.md
    LICENSE.txt
    REFERENCE.md
    SKILL.md
  pptx/  (57 files)
    scripts/  (55 files)
      … 55 files under this directory
    LICENSE.txt
    SKILL.md
  skill-creator/  (18 files)
    agents/  (3 files)
      … 3 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    eval-viewer/  (2 files)
      … 2 files under this directory
    references/  (1 files)
      … 1 files under this directory
    scripts/  (9 files)
      … 9 files under this directory
    LICENSE.txt
    SKILL.md
  slack-gif-creator/  (7 files)
    core/  (4 files)
      … 4 files under this directory
    LICENSE.txt
    SKILL.md
    requirements.txt
  theme-factory/  (12 files)
    themes/  (10 files)
      … 10 files under this directory
    LICENSE.txt
    SKILL.md
  web-artifacts-builder/  (4 files)
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE.txt
    SKILL.md
  webapp-testing/  (6 files)
    examples/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE.txt
    SKILL.md
  xlsx/  (52 files)
    scripts/  (50 files)
      … 50 files under this directory
    LICENSE.txt
    SKILL.md
spec/  (1 files)
  agent-skills-spec.md
template/  (1 files)
  SKILL.md
.gitignore
README.md
THIRD_PARTY_NOTICES.md
```

## Entry points

- [skills/claude-api/shared/preserved-thinking-migration/drop_block_probe.py:1065](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/claude-api/shared/preserved-thinking-migration/drop_block_probe.py#L1065)
- [skills/claude-api/shared/preserved-thinking-migration/prefix_diff.py:1531](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/claude-api/shared/preserved-thinking-migration/prefix_diff.py#L1531)
- [skills/docx/scripts/accept_changes.py:121](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/docx/scripts/accept_changes.py#L121)
- [skills/docx/scripts/comment.py:367](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/docx/scripts/comment.py#L367)
- [skills/docx/scripts/merge_runs.py:309](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/docx/scripts/merge_runs.py#L309)
- [skills/docx/scripts/office/soffice.py:189](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/docx/scripts/office/soffice.py#L189)
- [skills/docx/scripts/office/validate.py:209](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/docx/scripts/office/validate.py#L209)
- [skills/docx/scripts/office/validators/base.py:886](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/docx/scripts/office/validators/base.py#L886)
- [skills/docx/scripts/office/validators/docx.py:518](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/docx/scripts/office/validators/docx.py#L518)
- [skills/docx/scripts/office/validators/pptx.py:548](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/docx/scripts/office/validators/pptx.py#L548)
- [skills/docx/scripts/office/validators/redlining.py:477](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/docx/scripts/office/validators/redlining.py#L477)
- [skills/mcp-builder/scripts/evaluation.py:372](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/mcp-builder/scripts/evaluation.py#L372)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 45 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BaseSchemaValidator, DOCXSchemaValidator, PPTXSchemaValidator, RectAndField, RedliningVal… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: GIFBuilder. Observed top-level functions: apply_squash_stretch, calculate_arc_motion, creat… |
| skills package | library | Observed | Groups 30 file(s) under skills package (observed from repository paths and static analysis). Observed top-level classes: MCPConnection, MCPConnectionHTTP, MCPConnectionSSE, MCPConnectionStdio. Observed top-level functio… |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `skills/mcp-builder/scripts/requirements.txt` (manifest)
- `skills/slack-gif-creator/requirements.txt` (manifest)

## Top-level layout

- `skills` — 382 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `spec` — 1 analysed file(s)
- `template` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064` is the revision these paths and observations refer to.
