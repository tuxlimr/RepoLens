# Project structure: openai/skills

**Analysed commit:** `49f948faa9258a0c61caceaf225e179651397431`

**Commit reference:** [49f948faa9258a0c61caceaf225e179651397431](https://github.com/openai/skills/commit/49f948faa9258a0c61caceaf225e179651397431)

**Tree at this commit:** [openai/skills@49f948faa925](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/skills |
| Description | Skills Catalog for Codex |
| Stars | 28745 |
| Forks | 2013 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `49f948faa9258a0c61caceaf225e179651397431` |
| Retrieved at | 2026-11-14T19:07:15.903107+00:00 |
| Files in this snapshot | 748 |

## Directory tree

```text
skills/  (745 files)
  .curated/  (707 files)
    aspnet-core/  (16 files)
      … 16 files under this directory
    chatgpt-apps/  (11 files)
      … 11 files under this directory
    cli-creator/  (4 files)
      … 4 files under this directory
    cloudflare-deploy/  (311 files)
      … 311 files under this directory
    define-goal/  (3 files)
      … 3 files under this directory
    figma/  (7 files)
      … 7 files under this directory
    figma-code-connect-components/  (7 files)
      … 7 files under this directory
    figma-create-design-system-rules/  (7 files)
      … 7 files under this directory
    figma-create-new-file/  (6 files)
      … 6 files under this directory
    figma-generate-design/  (6 files)
      … 6 files under this directory
    figma-generate-library/  (22 files)
      … 22 files under this directory
    figma-implement-design/  (5 files)
      … 5 files under this directory
    figma-use/  (27 files)
      … 27 files under this directory
    gh-address-comments/  (5 files)
      … 5 files under this directory
    gh-fix-ci/  (5 files)
      … 5 files under this directory
    hatch-pet/  (14 files)
      … 14 files under this directory
    jupyter-notebook/  (11 files)
      … 11 files under this directory
    linear/  (4 files)
      … 4 files under this directory
    migrate-to-codex/  (19 files)
      … 19 files under this directory
    netlify-deploy/  (7 files)
      … 7 files under this directory
    notion-knowledge-capture/  (17 files)
      … 17 files under this directory
    notion-meeting-intelligence/  (18 files)
      … 18 files under this directory
    notion-research-documentation/  (22 files)
      … 22 files under this directory
    notion-spec-to-implementation/  (18 files)
      … 18 files under this directory
    openai-docs/  (9 files)
      … 9 files under this directory
    pdf/  (3 files)
      … 3 files under this directory
    playwright/  (8 files)
      … 8 files under this directory
    playwright-interactive/  (5 files)
      … 5 files under this directory
    render-deploy/  (20 files)
      … 20 files under this directory
    screenshot/  (10 files)
      … 10 files under this directory
    security-best-practices/  (13 files)
      … 13 files under this directory
    security-ownership-map/  (8 files)
      … 8 files under this directory
    security-threat-model/  (5 files)
      … 5 files under this directory
    sentry/  (4 files)
      … 4 files under this directory
    speech/  (15 files)
      … 15 files under this directory
    transcribe/  (6 files)
      … 6 files under this directory
    vercel-deploy/  (5 files)
      … 5 files under this directory
    winui-app/  (20 files)
      … 20 files under this directory
    yeet/  (4 files)
      … 4 files under this directory
  .system/  (38 files)
    imagegen/  (10 files)
      … 10 files under this directory
    openai-docs/  (9 files)
      … 9 files under this directory
    plugin-creator/  (5 files)
      … 5 files under this directory
    skill-creator/  (7 files)
      … 7 files under this directory
    skill-installer/  (7 files)
      … 7 files under this directory
.gitignore
README.md
contributing.md
```

## Entry points

- [skills/.curated/figma-code-connect-components/scripts/normalize_node_id.py:24](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/figma-code-connect-components/scripts/normalize_node_id.py#L24)
- [skills/.curated/gh-address-comments/scripts/fetch_comments.py:236](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-address-comments/scripts/fetch_comments.py#L236)
- [skills/.curated/gh-fix-ci/scripts/inspect_pr_checks.py:508](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci/scripts/inspect_pr_checks.py#L508)
- [skills/.curated/hatch-pet/scripts/compose_atlas.py:168](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet/scripts/compose_atlas.py#L168)
- [skills/.curated/hatch-pet/scripts/derive_running_left_from_running_right.py:149](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet/scripts/derive_running_left_from_running_right.py#L149)
- [skills/.curated/hatch-pet/scripts/extract_strip_frames.py:407](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet/scripts/extract_strip_frames.py#L407)
- [skills/.curated/hatch-pet/scripts/inspect_frames.py:255](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet/scripts/inspect_frames.py#L255)
- [skills/.curated/hatch-pet/scripts/make_contact_sheet.py:95](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet/scripts/make_contact_sheet.py#L95)
- [skills/.curated/hatch-pet/scripts/prepare_pet_run.py:829](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet/scripts/prepare_pet_run.py#L829)
- [skills/.curated/hatch-pet/scripts/render_animation_previews.py:77](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet/scripts/render_animation_previews.py#L77)
- [skills/.curated/hatch-pet/scripts/validate_atlas.py:156](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet/scripts/validate_atlas.py#L156)
- [skills/.curated/jupyter-notebook/scripts/new_notebook.py:129](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook/scripts/new_notebook.py#L129)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 66 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 28 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Args, DeployMode, DeploymentPlan, GhResult, InstallError, ListError. Observed top-level f… |
| skills package | library | Observed | Groups 31 file(s) under skills package (observed from repository paths and static analysis). Observed top-level classes: ArtifactKind, ClaudeHookCommand, ClaudeHookMatcherGroup, ClaudeHooks, ConversionResult, GeneratedT… |

## Important files

- `skills/.curated/aspnet-core/agents/openai.yaml` (config)
- `skills/.curated/chatgpt-apps/agents/openai.yaml` (config)
- `skills/.curated/cli-creator/agents/openai.yaml` (config)
- `skills/.curated/cloudflare-deploy/agents/openai.yaml` (config)
- `skills/.curated/define-goal/agents/openai.yaml` (config)
- `skills/.curated/figma-code-connect-components/agents/openai.yaml` (config)
- `skills/.curated/figma-create-design-system-rules/agents/openai.yaml` (config)
- `skills/.curated/figma-create-new-file/agents/openai.yaml` (config)
- `skills/.curated/figma-create-new-file/maintainers.yml` (config)
- `skills/.curated/figma-generate-design/agents/openai.yaml` (config)
- `skills/.curated/figma-generate-design/maintainers.yml` (config)
- `skills/.curated/figma-generate-library/agents/openai.yaml` (config)
- `skills/.curated/figma-generate-library/maintainers.yml` (config)
- `skills/.curated/figma-implement-design/agents/openai.yaml` (config)
- `skills/.curated/figma-use/agents/openai.yaml` (config)
- `skills/.curated/figma-use/maintainers.yml` (config)
- `skills/.curated/figma-use/references/maintainers.yml` (config)
- `skills/.curated/figma-use/references/working-with-design-systems/maintainers.yml` (config)
- `skills/.curated/figma/agents/openai.yaml` (config)
- `skills/.curated/gh-address-comments/agents/openai.yaml` (config)
- `skills/.curated/gh-fix-ci/agents/openai.yaml` (config)
- `skills/.curated/hatch-pet/agents/openai.yaml` (config)
- `skills/.curated/jupyter-notebook/agents/openai.yaml` (config)
- `skills/.curated/linear/agents/openai.yaml` (config)
- `skills/.curated/migrate-to-codex/agents/openai.yaml` (config)
- `skills/.curated/netlify-deploy/agents/openai.yaml` (config)
- `skills/.curated/notion-knowledge-capture/agents/openai.yaml` (config)
- `skills/.curated/notion-knowledge-capture/evaluations/conversation-to-wiki.json` (config)
- `skills/.curated/notion-knowledge-capture/evaluations/decision-record.json` (config)
- `skills/.curated/notion-meeting-intelligence/agents/openai.yaml` (config)
- `skills/.curated/notion-meeting-intelligence/evaluations/decision-meeting-prep.json` (config)
- `skills/.curated/notion-meeting-intelligence/evaluations/status-meeting-prep.json` (config)
- `skills/.curated/notion-research-documentation/agents/openai.yaml` (config)
- `skills/.curated/notion-research-documentation/evaluations/basic-research.json` (config)
- `skills/.curated/notion-research-documentation/evaluations/research-to-database.json` (config)
- `skills/.curated/notion-spec-to-implementation/agents/openai.yaml` (config)
- `skills/.curated/notion-spec-to-implementation/evaluations/basic-spec-implementation.json` (config)
- `skills/.curated/notion-spec-to-implementation/evaluations/spec-to-tasks.json` (config)
- `skills/.curated/openai-docs/agents/openai.yaml` (config)
- `skills/.curated/pdf/agents/openai.yaml` (config)
- `skills/.curated/playwright-interactive/agents/openai.yaml` (config)
- `skills/.curated/playwright/agents/openai.yaml` (config)
- `skills/.curated/render-deploy/agents/openai.yaml` (config)
- `skills/.curated/render-deploy/assets/docker.yaml` (config)
- `skills/.curated/render-deploy/assets/go-api.yaml` (config)
- `skills/.curated/render-deploy/assets/nextjs-postgres.yaml` (config)
- `skills/.curated/render-deploy/assets/node-express.yaml` (config)
- `skills/.curated/render-deploy/assets/python-django.yaml` (config)
- `skills/.curated/render-deploy/assets/static-site.yaml` (config)
- `skills/.curated/screenshot/agents/openai.yaml` (config)
- `skills/.curated/security-best-practices/agents/openai.yaml` (config)
- `skills/.curated/security-ownership-map/agents/openai.yaml` (config)
- `skills/.curated/security-threat-model/agents/openai.yaml` (config)
- `skills/.curated/sentry/agents/openai.yaml` (config)
- `skills/.curated/speech/agents/openai.yaml` (config)
- `skills/.curated/transcribe/agents/openai.yaml` (config)
- `skills/.curated/vercel-deploy/agents/openai.yaml` (config)
- `skills/.curated/winui-app/agents/openai.yaml` (config)
- `skills/.curated/winui-app/config.yaml` (config)
- `skills/.curated/yeet/agents/openai.yaml` (config)
- `skills/.system/imagegen/agents/openai.yaml` (config)
- `skills/.system/openai-docs/agents/openai.yaml` (config)
- `skills/.system/plugin-creator/agents/openai.yaml` (config)
- `skills/.system/skill-creator/agents/openai.yaml` (config)
- `skills/.system/skill-installer/agents/openai.yaml` (config)

## Top-level layout

- `skills` — 745 analysed file(s)
- `(root files)` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `49f948faa9258a0c61caceaf225e179651397431` is the revision these paths and observations refer to.
