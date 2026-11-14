# Project structure: asgeirtj/system_prompts_leaks

**Analysed commit:** `bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f`

**Commit reference:** [bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f](https://github.com/asgeirtj/system_prompts_leaks/commit/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f)

**Tree at this commit:** [asgeirtj/system_prompts_leaks@bb4c9c5a8bcb](https://github.com/asgeirtj/system_prompts_leaks/tree/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | asgeirtj/system_prompts_leaks |
| Description | Leaked system prompts of ChatGPT, Claude, Gemini and more. The hidden system prompt of every popular chatbot, in full, every version since May 2025. Also Anthropic Claude Code, OpenAI Codex, Google Antigravity, xAI Grok, Meta Muse, Moonshot Kimi, Alibaba Qwen, Z.ai GLM ZCode, MiniMax, Cursor, Perpl… |
| Stars | 71410 |
| Forks | 11492 |
| Licence | CC0-1.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f` |
| Retrieved at | 2026-11-14T19:06:18.316598+00:00 |
| Files in this snapshot | 547 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
Anthropic/  (544 files)
  artifact-types/  (72 files)
    dashboard/  (17 files)
      … 17 files under this directory
    design/  (14 files)
      … 14 files under this directory
    design-system/  (7 files)
      … 7 files under this directory
    docs/  (1 files)
      … 1 files under this directory
    motion/  (12 files)
      … 12 files under this directory
    sheets/  (1 files)
      … 1 files under this directory
    slides/  (16 files)
      … 16 files under this directory
    whiteboard/  (3 files)
      … 3 files under this directory
    types-listing.md
  claude-code/  (468 files)
    agents/  (9 files)
      … 9 files under this directory
    output-styles/  (4 files)
      … 4 files under this directory
    prompts/  (10 files)
      … 10 files under this directory
    skills/  (444 files)
      … 444 files under this directory
    claude-code-docs-assistant.md
  claude-design/  (2 files)
    skills/  (2 files)
      … 2 files under this directory
  anthropic-interviewer.md
  anthropic_reminders.md
.editorconfig
.gitattributes
```

## Entry points

- [Anthropic/claude-code/skills/claude-api/shared/latency-optimization/latency_probe.py:1041](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/claude-api/shared/latency-optimization/latency_probe.py#L1041)
- [Anthropic/claude-code/skills/claude-api/shared/preserved-thinking-migration/drop_block_probe.py:1074](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/claude-api/shared/preserved-thinking-migration/drop_block_probe.py#L1074)
- [Anthropic/claude-code/skills/claude-api/shared/preserved-thinking-migration/prefix_diff.py:1531](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/claude-api/shared/preserved-thinking-migration/prefix_diff.py#L1531)
- [Anthropic/claude-code/skills/dataviz/scripts/validate_palette.py:342](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/dataviz/scripts/validate_palette.py#L342)
- [Anthropic/claude-code/skills/docx/scripts/accept_changes.py:121](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/docx/scripts/accept_changes.py#L121)
- [Anthropic/claude-code/skills/docx/scripts/comment.py:367](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/docx/scripts/comment.py#L367)
- [Anthropic/claude-code/skills/docx/scripts/merge_runs.py:309](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/docx/scripts/merge_runs.py#L309)
- [Anthropic/claude-code/skills/docx/scripts/office/soffice.py:189](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/docx/scripts/office/soffice.py#L189)
- [Anthropic/claude-code/skills/docx/scripts/office/validate.py:209](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/docx/scripts/office/validate.py#L209)
- [Anthropic/claude-code/skills/docx/scripts/office/validators/base.py:886](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/docx/scripts/office/validators/base.py#L886)
- [Anthropic/claude-code/skills/docx/scripts/office/validators/docx.py:518](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/docx/scripts/office/validators/docx.py#L518)
- [Anthropic/claude-code/skills/docx/scripts/office/validators/pptx.py:548](https://github.com/asgeirtj/system_prompts_leaks/blob/bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f/Anthropic/claude-code/skills/docx/scripts/office/validators/pptx.py#L548)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Anthropic package | library | Observed | Groups 72 file(s) under anthropic package (observed from repository paths and static analysis). Observed top-level functions: _canonical_ids, _check_chart_axis_references, _check_decimal_settings, _check_preset_dashes,… |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 47 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BaseSchemaValidator, Connection, DOCXSchemaValidator, PPTXSchemaValidator, RectAndField,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `Anthropic/artifact-types/design-system/artifact-type/reference/sample-seazar-tokens.json` (config)
- `Anthropic/artifact-types/design/artifact-type/reference/google-fonts-families.json` (config)
- `Anthropic/artifact-types/design/artifact-type/reference/google-fonts-reserved.json` (config)
- `Anthropic/artifact-types/slides/artifact-type/reference/google-fonts-families.json` (config)
- `Anthropic/artifact-types/slides/artifact-type/reference/google-fonts-reserved.json` (config)

## Top-level layout

- `Anthropic` — 544 analysed file(s)
- `(root files)` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bb4c9c5a8bcbe281e2fbe3fd1fa961e514c0a93f` is the revision these paths and observations refer to.
