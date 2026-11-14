# Project structure: blader/humanizer

**Analysed commit:** `b48c832f0f809c1b5658edbb838c2521b72f2413`

**Commit reference:** [b48c832f0f809c1b5658edbb838c2521b72f2413](https://github.com/blader/humanizer/commit/b48c832f0f809c1b5658edbb838c2521b72f2413)

**Tree at this commit:** [blader/humanizer@b48c832f0f80](https://github.com/blader/humanizer/tree/b48c832f0f809c1b5658edbb838c2521b72f2413)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | blader/humanizer |
| Description | Agent skill that removes signs of AI-generated writing from text |
| Stars | 69103 |
| Forks | 5429 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `b48c832f0f809c1b5658edbb838c2521b72f2413` |
| Retrieved at | 2026-11-14T19:06:17.737433+00:00 |
| Files in this snapshot | 15 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.cursor-plugin/  (1 files)
  plugin.json
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    config.yml
    new-pattern.yml
    rewrite-problem.yml
  workflows/  (1 files)
    validate.yml
agents/  (1 files)
  openai.yaml
scripts/  (1 files)
  validate-package.py
AGENTS.md
CHANGELOG.md
LICENSE
README.md
SKILL.md
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: read_package_file, require_match. |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.cursor-plugin/plugin.json` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/new-pattern.yml` (config)
- `.github/ISSUE_TEMPLATE/rewrite-problem.yml` (config)
- `.github/workflows/validate.yml` (ci)
- `agents/openai.yaml` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `.cursor-plugin` — 1 analysed file(s)
- `agents` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b48c832f0f809c1b5658edbb838c2521b72f2413` is the revision these paths and observations refer to.
