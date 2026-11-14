# Project structure: nicobailon/visual-explainer

**Analysed commit:** `9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad`

**Commit reference:** [9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad](https://github.com/nicobailon/visual-explainer/commit/9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad)

**Tree at this commit:** [nicobailon/visual-explainer@9d5f880b7e8e](https://github.com/nicobailon/visual-explainer/tree/9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nicobailon/visual-explainer |
| Description | Agent skill that generates rich HTML pages or slide decks for diagrams, diff reviews, plan audits, data tables, and project recaps |
| Stars | 11090 |
| Forks | 700 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad` |
| Retrieved at | 2026-11-14T19:12:26.410456+00:00 |
| Files in this snapshot | 93 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
configs/  (7 files)
  antigravity/  (1 files)
    AGENTS.md
  codex/  (1 files)
    AGENTS.md
  copilot/  (1 files)
    AGENTS.md
  cursor/  (1 files)
    visual-explainer.mdc
  openclaw/  (1 files)
    AGENTS.md
  opencode/  (1 files)
    AGENTS.md
  pi/  (1 files)
    AGENTS.md
eval/  (4 files)
  README.md
  judge.md
  prompts.md
  score.mjs
examples/  (1 files)
  replay-job-queue.html
plugins/  (51 files)
  visual-explainer/  (51 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (10 files)
      … 10 files under this directory
    kit/  (15 files)
      … 15 files under this directory
    mcp/  (2 files)
      … 2 files under this directory
    plan/  (3 files)
      … 3 files under this directory
    pptx/  (2 files)
      … 2 files under this directory
    references/  (10 files)
      … 10 files under this directory
    templates/  (3 files)
      … 3 files under this directory
    video/  (3 files)
      … 3 files under this directory
    SKILL.md
    extension.ts
scripts/  (21 files)
  fixtures/  (17 files)
    machines/  (17 files)
      … 17 files under this directory
  check-ask.mjs
  check-kit.mjs
  check-machine.mjs
  check-versions.mjs
.gitignore
CHANGELOG.md
LICENSE
README.md
install-pi.sh
package.json
plugin.json
```

## Entry points

- [plugins/visual-explainer/mcp/server.mjs](https://github.com/nicobailon/visual-explainer/blob/9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad/plugins/visual-explainer/mcp/server.mjs)
- [plugins/visual-explainer/pptx/export.mjs](https://github.com/nicobailon/visual-explainer/blob/9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad/plugins/visual-explainer/pptx/export.mjs)
- [plugins/visual-explainer/video/render.mjs](https://github.com/nicobailon/visual-explainer/blob/9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad/plugins/visual-explainer/video/render.mjs)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| eval package | library | Observed | Groups 1 file(s) under eval package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 19 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 13 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `package.json` (manifest)
- `plugin.json` (config)
- `plugins/visual-explainer/.claude-plugin/plugin.json` (config)

## Top-level layout

- `plugins` — 51 analysed file(s)
- `scripts` — 21 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `configs` — 7 analysed file(s)
- `eval` — 4 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad` is the revision these paths and observations refer to.
