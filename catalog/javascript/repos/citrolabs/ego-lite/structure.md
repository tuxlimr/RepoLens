# Project structure: citrolabs/ego-lite

**Analysed commit:** `bacaece43900e8ca68eea3b6f1663835ea38df9e`

**Commit reference:** [bacaece43900e8ca68eea3b6f1663835ea38df9e](https://github.com/citrolabs/ego-lite/commit/bacaece43900e8ca68eea3b6f1663835ea38df9e)

**Tree at this commit:** [citrolabs/ego-lite@bacaece43900](https://github.com/citrolabs/ego-lite/tree/bacaece43900e8ca68eea3b6f1663835ea38df9e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | citrolabs/ego-lite |
| Description | The fastest browser for AI agents to run browser automation, built for sharing your logged-in browser state with your AI agents, like Codex or Claude Code, without disturbing you. Zero cost, zero config. |
| Stars | 22877 |
| Forks | 1293 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `bacaece43900e8ca68eea3b6f1663835ea38df9e` |
| Retrieved at | 2026-11-14T19:11:06.371010+00:00 |
| Files in this snapshot | 242 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.claude-plugin/  (1 files)
  marketplace.json
.cursor-plugin/  (1 files)
  marketplace.json
.github/  (14 files)
  dev-skills/  (2 files)
    ego-lite-simplify/  (2 files)
      … 2 files under this directory
  star-history/  (6 files)
    FONT-LICENSE.txt
    action-runtime.patch
    branch-readme.md
    postprocess-svg.py
    y-axis.patch
    y-axis.test.ts
  workflows/  (5 files)
    ci.yml
    codex-review.yml
    main-pr-source.yml
    purge-camo-cache.yml
    star-history.yml
  release.yml
docs/  (6 files)
  ego-browser-skill-command.md
  local-runtime-development.md
  native-bindings-api.md
  native-javascript-dialog-requirement.md
  native-sdk-lifecycle-requirement.md
  native-snapshot-ref-requirement.md
package/  (139 files)
  ego-browser/  (139 files)
    scripts/  (55 files)
      … 55 files under this directory
    skill-body/  (1 files)
      … 1 files under this directory
    src/  (79 files)
      … 79 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
plugins/  (41 files)
  ego/  (39 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .codebuddy-plugin/  (1 files)
      … 1 files under this directory
    .codex-plugin/  (1 files)
      … 1 files under this directory
    .cursor-plugin/  (1 files)
      … 1 files under this directory
    .qoder-plugin/  (1 files)
      … 1 files under this directory
    dsh/  (1 files)
      … 1 files under this directory
    skills/  (22 files)
      … 22 files under this directory
    tests/  (5 files)
      … 5 files under this directory
    LICENSE
    README.md
    cordis.patch.yml
    index.js
    package.json
    plugin.json
  scripts/  (2 files)
    package-plugins.mjs
    sync-skills.mjs
skills/  (22 files)
  ego-browser/  (22 files)
    agents/  (1 files)
      … 1 files under this directory
    learnings/  (15 files)
      … 15 files under this directory
    references/  (4 files)
      … 4 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
spec/  (1 files)
  agent-skills-spec.md
.gitignore
.prettierignore
AGENTS.md
CONTRIBUTING.md
LICENSE
README.es.md
README.fr.md
README.it.md
README.ja.md
README.ko.md
README.md
README.pt.md
README.ru.md
README.zh-CN.md
install.md
lefthook.yml
```

## Entry points

- [.github/star-history/postprocess-svg.py:85](https://github.com/citrolabs/ego-lite/blob/bacaece43900e8ca68eea3b6f1663835ea38df9e/.github/star-history/postprocess-svg.py#L85)
- [package/ego-browser/src/index.ts](https://github.com/citrolabs/ego-lite/blob/bacaece43900e8ca68eea3b6f1663835ea38df9e/package/ego-browser/src/index.ts)
- [plugins/ego/index.js](https://github.com/citrolabs/ego-lite/blob/bacaece43900e8ca68eea3b6f1663835ea38df9e/plugins/ego/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| package package | library | Observed | Groups 134 file(s) under package package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 13 file(s) under plugins package (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 9 file(s) under skills package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.cursor-plugin/marketplace.json` (config)
- `.github/dev-skills/ego-lite-simplify/agents/openai.yaml` (config)
- `.github/release.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codex-review.yml` (ci)
- `.github/workflows/main-pr-source.yml` (ci)
- `.github/workflows/purge-camo-cache.yml` (ci)
- `.github/workflows/star-history.yml` (ci)
- `lefthook.yml` (config)
- `package/ego-browser/package.json` (manifest)
- `package/ego-browser/tsconfig.json` (config)
- `plugins/ego/.claude-plugin/plugin.json` (config)
- `plugins/ego/.codebuddy-plugin/plugin.json` (config)
- `plugins/ego/.codex-plugin/plugin.json` (config)
- `plugins/ego/.cursor-plugin/plugin.json` (config)
- `plugins/ego/.qoder-plugin/plugin.json` (config)
- `plugins/ego/cordis.patch.yml` (config)
- `plugins/ego/package.json` (manifest)
- `plugins/ego/plugin.json` (config)
- `plugins/ego/skills/ego-browser/agents/openai.yaml` (config)
- `plugins/ego/skills/ego-browser/learnings/github/manifest.json` (config)
- `plugins/ego/skills/ego-browser/learnings/google/manifest.json` (config)
- `plugins/ego/skills/ego-browser/learnings/x-com/manifest.json` (config)
- `skills/ego-browser/agents/openai.yaml` (config)
- `skills/ego-browser/learnings/github/manifest.json` (config)
- `skills/ego-browser/learnings/google/manifest.json` (config)
- `skills/ego-browser/learnings/x-com/manifest.json` (config)

## Top-level layout

- `package` — 139 analysed file(s)
- `plugins` — 41 analysed file(s)
- `skills` — 22 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 14 analysed file(s)
- `docs` — 6 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `.cursor-plugin` — 1 analysed file(s)
- `spec` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bacaece43900e8ca68eea3b6f1663835ea38df9e` is the revision these paths and observations refer to.
