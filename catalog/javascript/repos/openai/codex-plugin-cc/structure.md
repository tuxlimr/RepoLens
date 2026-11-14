# Project structure: openai/codex-plugin-cc

**Analysed commit:** `db52e28f4d9ded852ab3942cea316258ae4ef346`

**Commit reference:** [db52e28f4d9ded852ab3942cea316258ae4ef346](https://github.com/openai/codex-plugin-cc/commit/db52e28f4d9ded852ab3942cea316258ae4ef346)

**Tree at this commit:** [openai/codex-plugin-cc@db52e28f4d9d](https://github.com/openai/codex-plugin-cc/tree/db52e28f4d9ded852ab3942cea316258ae4ef346)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/codex-plugin-cc |
| Description | Use Codex from Claude Code to review code or delegate tasks. |
| Stars | 35124 |
| Forks | 2436 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `db52e28f4d9ded852ab3942cea316258ae4ef346` |
| Retrieved at | 2026-11-14T19:10:43.034060+00:00 |
| Files in this snapshot | 62 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
.github/  (1 files)
  workflows/  (1 files)
    pull-request-ci.yml
plugins/  (43 files)
  codex/  (43 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (8 files)
      … 8 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    prompts/  (2 files)
      … 2 files under this directory
    schemas/  (1 files)
      … 1 files under this directory
    scripts/  (20 files)
      … 20 files under this directory
    skills/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    LICENSE
    NOTICE
scripts/  (1 files)
  bump-version.mjs
tests/  (10 files)
  broker-endpoint.test.mjs
  bump-version.test.mjs
  commands.test.mjs
  fake-codex-fixture.mjs
  git.test.mjs
  helpers.mjs
  process.test.mjs
  render.test.mjs
  runtime.test.mjs
  state.test.mjs
.gitignore
LICENSE
NOTICE
README.md
package.json
tsconfig.app-server.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 20 file(s) under plugins package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.github/workflows/pull-request-ci.yml` (ci)
- `package.json` (manifest)
- `plugins/codex/.claude-plugin/plugin.json` (config)
- `plugins/codex/hooks/hooks.json` (config)
- `plugins/codex/schemas/review-output.schema.json` (config)
- `tsconfig.app-server.json` (config)

## Top-level layout

- `plugins` — 43 analysed file(s)
- `tests` — 10 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `.github` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `db52e28f4d9ded852ab3942cea316258ae4ef346` is the revision these paths and observations refer to.
