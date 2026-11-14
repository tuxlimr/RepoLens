# Project structure: jarrodwatts/claude-hud

**Analysed commit:** `9d2b6fa4df43c8ced61c0c23956fd291551726ac`

**Commit reference:** [9d2b6fa4df43c8ced61c0c23956fd291551726ac](https://github.com/jarrodwatts/claude-hud/commit/9d2b6fa4df43c8ced61c0c23956fd291551726ac)

**Tree at this commit:** [jarrodwatts/claude-hud@9d2b6fa4df43](https://github.com/jarrodwatts/claude-hud/tree/9d2b6fa4df43c8ced61c0c23956fd291551726ac)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jarrodwatts/claude-hud |
| Description | A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress |
| Stars | 29201 |
| Forks | 1338 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `9d2b6fa4df43c8ced61c0c23956fd291551726ac` |
| Retrieved at | 2026-11-14T19:10:48.574486+00:00 |
| Files in this snapshot | 160 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.github/  (8 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    case.yml
    config.yml
    feature_request.md
  workflows/  (3 files)
    ci.yml
    maintain.yml
    verify.yml
  pull_request_template.md
maintainer/  (6 files)
  PLAYBOOK.md
  act.mjs
  harness.mjs
  outbox.schema.json
  probe.mjs
  scorecard.mjs
scripts/  (1 files)
  statusline.mjs
skills/  (1 files)
  hud/  (1 files)
    SKILL.md
src/  (49 files)
  i18n/  (5 files)
    en.ts
    index.ts
    types.ts
    zh-Hans.ts
    zh-Hant.ts
  render/  (16 files)
    activity.ts
    ansi.ts
    colors.ts
    compact.ts
    context.ts
    derive.ts
    expanded.ts
    frame.ts
    index.ts
    labels.ts
    lines.ts
    order.ts
    parts.ts
    time.ts
    usage.ts
    vcs.ts
  utils/  (5 files)
    format.ts
    hyperlinks.ts
    sanitize.ts
    terminal.ts
    truncate.ts
  auth.ts
  channel.ts
  commands.ts
  config-reader.ts
  config.ts
  cost.ts
  daily-cost.ts
  debug.ts
  effort.ts
  external-usage.ts
  extra-cmd.ts
  git.ts
  index.ts
  jj.ts
  main.ts
  memory.ts
  model-source.ts
  schema.ts
  speed.ts
  stdin.ts
  transcript.ts
  types.ts
  usage-pace.ts
tests/  (62 files)
  corpus/  (22 files)
    0100-daily-cost-numeric-session-id.json
    0100-model-name-escapes.json
    0100-output-style-escapes.json
    0378-no-stdin-kept-open.json
    0430-initial-zero-frame.json
    0589-autocompact-window-not-integer.json
    0662-weekly-hidden-below-default-threshold.json
    0673-cjk-narrow-fits.json
    0678-full-path-bidi.json
    0687-variation-selectors-fit.json
    0693-hostile-max-width.json
    0727-prompt-cache-until.json
    0753-version-from-stdin.json
    0754-session-name-escapes.json
    0801-partial-stdin-kept-open.json
    0811-folder-separator-closes-link.json
    0830-jj-bookmark-emoji-at-cap.json
    0830-output-style-emoji-at-cap.json
    0830-session-name-emoji-at-cap.json
    0857-changed-files-git-order.json
    changelog-0.10.0-vcs-branch-link-from-workspace-repo.json
    changelog-0.10.0-vcs-no-commits-shows-branch.json
  fixtures/  (3 files)
    expected/  (1 files)
      … 1 files under this directory
    transcript-render.jsonl
    transcript-ultracode.jsonl
  golden/  (6 files)
    cases.mjs
    expected.txt
    freeze-time.mjs
    transcript-activity.jsonl
    transcript-deleted-tasks.jsonl
    transcript.jsonl
  ansi.test.js
  auth.test.js
  cage.test.js
  clean-env.js
  commands.test.js
  config-reader.test.js
  config.test.js
  daily-cost.test.js
  effort.test.js
  external-usage.test.js
  extra-cmd.test.js
  format-reset-time.test.js
  git-runner.test.js
  git.test.js
  golden.test.js
  hud.test.js
  hyperlinks.test.js
  i18n.test.js
  install.test.js
  integration.test.js
  jj.test.js
  memory-coverage.test.js
  memory.test.js
  prompt-cache.test.js
  … 7 more files
verify/  (14 files)
  lib/  (5 files)
    ans2html.mjs
    claude-code.mjs
    escape-probe.mjs
    fake-api.mjs
    fake-github.mjs
  arch.check.mjs
  case.mjs
  corpus.check.mjs
  e2e.check.mjs
  escape.check.mjs
  launcher.check.mjs
  maintainer.check.mjs
  owner.check.mjs
  run.mjs
.editorconfig
.gitignore
ARCHITECTURE.md
CHANGELOG.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
README.zh.md
SECURITY.md
collector.mjs
fence.mjs
hud.mjs
install.mjs
package.json
tsconfig.json
```

## Entry points

- [hud.mjs](https://github.com/jarrodwatts/claude-hud/blob/9d2b6fa4df43c8ced61c0c23956fd291551726ac/hud.mjs)
- [src/i18n/index.ts](https://github.com/jarrodwatts/claude-hud/blob/9d2b6fa4df43c8ced61c0c23956fd291551726ac/src/i18n/index.ts)
- [src/index.ts](https://github.com/jarrodwatts/claude-hud/blob/9d2b6fa4df43c8ced61c0c23956fd291551726ac/src/index.ts)
- [src/main.ts](https://github.com/jarrodwatts/claude-hud/blob/9d2b6fa4df43c8ced61c0c23956fd291551726ac/src/main.ts)
- [src/render/index.ts](https://github.com/jarrodwatts/claude-hud/blob/9d2b6fa4df43c8ced61c0c23956fd291551726ac/src/render/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| auth.ts package | library | Observed | Groups 1 file(s) under auth.ts package (observed from repository paths and static analysis). |
| channel.ts package | library | Observed | Groups 1 file(s) under channel.ts package (observed from repository paths and static analysis). |
| commands.ts package | library | Observed | Groups 1 file(s) under commands.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config-reader.ts package | library | Observed | Groups 1 file(s) under config-reader.ts package (observed from repository paths and static analysis). |
| config.ts package | library | Observed | Groups 1 file(s) under config.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| cost.ts package | library | Observed | Groups 1 file(s) under cost.ts package (observed from repository paths and static analysis). |
| daily-cost.ts package | library | Observed | Groups 1 file(s) under daily-cost.ts package (observed from repository paths and static analysis). |
| debug.ts package | library | Observed | Groups 1 file(s) under debug.ts package (observed from repository paths and static analysis). |
| effort.ts package | library | Observed | Groups 1 file(s) under effort.ts package (observed from repository paths and static analysis). |
| external-usage.ts package | library | Observed | Groups 1 file(s) under external-usage.ts package (observed from repository paths and static analysis). |
| extra-cmd.ts package | library | Observed | Groups 1 file(s) under extra-cmd.ts package (observed from repository paths and static analysis). |
| git.ts package | library | Observed | Groups 1 file(s) under git.ts package (observed from repository paths and static analysis). |
| i18n package | library | Observed | Groups 5 file(s) under i18n package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| jj.ts package | library | Observed | Groups 1 file(s) under jj.ts package (observed from repository paths and static analysis). |
| main.ts package | library | Observed | Groups 1 file(s) under main.ts package (observed from repository paths and static analysis). |
| maintainer package | library | Observed | Groups 4 file(s) under maintainer package (observed from repository paths and static analysis). |
| memory.ts package | library | Observed | Groups 1 file(s) under memory.ts package (observed from repository paths and static analysis). |
| model-source.ts package | library | Observed | Groups 1 file(s) under model-source.ts package (observed from repository paths and static analysis). |
| render package | library | Observed | Groups 16 file(s) under render package (observed from repository paths and static analysis). |
| schema.ts package | library | Observed | Groups 1 file(s) under schema.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| speed.ts package | library | Observed | Groups 1 file(s) under speed.ts package (observed from repository paths and static analysis). |
| stdin.ts package | library | Observed | Groups 1 file(s) under stdin.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 62 file(s) under tests (observed from repository paths and static analysis). |
| transcript.ts package | library | Observed | Groups 1 file(s) under transcript.ts package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| usage-pace.ts package | library | Observed | Groups 1 file(s) under usage-pace.ts package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |
| verify package | library | Observed | Groups 14 file(s) under verify package (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/case.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/maintain.yml` (ci)
- `.github/workflows/verify.yml` (ci)
- `maintainer/outbox.schema.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `tests` — 62 analysed file(s)
- `src` — 49 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `verify` — 14 analysed file(s)
- `.github` — 8 analysed file(s)
- `maintainer` — 6 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)
- `skills` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9d2b6fa4df43c8ced61c0c23956fd291551726ac` is the revision these paths and observations refer to.
