# Project structure: anthropics/claude-plugins-official

**Analysed commit:** `b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6`

**Commit reference:** [b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6](https://github.com/anthropics/claude-plugins-official/commit/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6)

**Tree at this commit:** [anthropics/claude-plugins-official@b5b01ac4f889](https://github.com/anthropics/claude-plugins-official/tree/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | anthropics/claude-plugins-official |
| Description | Official, Anthropic-managed directory of high quality Claude Code Plugins. |
| Stars | 47281 |
| Forks | 4910 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6` |
| Retrieved at | 2026-11-14T19:06:36.791265+00:00 |
| Files in this snapshot | 738 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
.github/  (14 files)
  policy/  (2 files)
    prompt.md
    schema.json
  scripts/  (4 files)
    discover_bumps.py
    plugin-dirs.sh
    validate-frontmatter.ts
    validate-plugin-folders.ts
  workflows/  (7 files)
    bump-plugin-shas.yml
    check-mcp-urls.yml
    close-external-prs.yml
    revert-failed-bumps.yml
    scan-plugins.yml
    validate-licenses.yml
    validate-plugins.yml
  bump-tracking.json
external_plugins/  (59 files)
  asana/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    README.md
  context7/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .mcp.json
    README.md
  discord/  (10 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    .mcp.json
    ACCESS.md
    LICENSE
    README.md
    bun.lock
    package.json
    server.ts
  fakechat/  (7 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .mcp.json
    LICENSE
    README.md
    bun.lock
    package.json
    server.ts
  firebase/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .mcp.json
  github/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .mcp.json
  gitlab/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .mcp.json
  imessage/  (10 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    .mcp.json
    ACCESS.md
    LICENSE
    README.md
    bun.lock
    package.json
    server.ts
  laravel-boost/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .mcp.json
  linear/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .mcp.json
  playwright/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .mcp.json
  serena/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .mcp.json
  telegram/  (10 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    .mcp.json
    ACCESS.md
    LICENSE
    README.md
    bun.lock
    package.json
    server.ts
  terraform/  (2 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    .mcp.json
plugins/  (661 files)
  agent-sdk-dev/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (2 files)
      … 2 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  champion-kit/  (12 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    skills/  (8 files)
      … 8 files under this directory
    LICENSE
    README.md
  clangd-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  claude-code-setup/  (9 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (6 files)
      … 6 files under this directory
    LICENSE
    README.md
  claude-for-manufacturing/  (93 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    shared/  (23 files)
      … 23 files under this directory
    skills/  (65 files)
      … 65 files under this directory
    .gitignore
    .mcp.json
    LICENSE
    README.md
  claude-md-management/  (8 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (4 files)
      … 4 files under this directory
    LICENSE
    README.md
  claude-security/  (46 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (9 files)
      … 9 files under this directory
    hooks/  (3 files)
      … 3 files under this directory
    scripts/  (20 files)
      … 20 files under this directory
    skills/  (7 files)
      … 7 files under this directory
    workflows/  (1 files)
      … 1 files under this directory
    .gitattributes
    LICENSE
    NOTICE.md
    README.md
    SECURITY.md
  code-modernization/  (91 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (8 files)
      … 8 files under this directory
    assets/  (2 files)
      … 2 files under this directory
    commands/  (13 files)
      … 13 files under this directory
    hooks/  (30 files)
      … 30 files under this directory
    scripts/  (17 files)
      … 17 files under this directory
    tests/  (10 files)
      … 10 files under this directory
    workflows/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    tsconfig.json
  code-review/  (4 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  code-simplifier/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    LICENSE
  commit-commands/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (3 files)
      … 3 files under this directory
    LICENSE
    README.md
  csharp-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  cwc-makers/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    LICENSE
    README.md
  example-plugin/  (7 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    .mcp.json
    LICENSE
    README.md
  explanatory-output-style/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    hooks-handlers/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  feature-dev/  (7 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  frontend-design/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    LICENSE
    README.md
  gopls-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  hookify/  (25 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (1 files)
      … 1 files under this directory
    commands/  (4 files)
      … 4 files under this directory
    core/  (3 files)
      … 3 files under this directory
    examples/  (4 files)
      … 4 files under this directory
    hooks/  (6 files)
      … 6 files under this directory
    matchers/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    .gitignore
    LICENSE
    README.md
  jdtls-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  kotlin-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  learning-output-style/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    hooks-handlers/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  lua-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  math-olympiad/  (14 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (11 files)
      … 11 files under this directory
    LICENSE
    README.md
  math-proof/  (9 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    skills/  (3 files)
      … 3 files under this directory
    LICENSE
    README.md
  mcp-server-dev/  (22 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (19 files)
      … 19 files under this directory
    LICENSE
    README.md
  mcp-tunnels/  (4 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  php-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  playground/  (10 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (7 files)
      … 7 files under this directory
    LICENSE
    README.md
  plugin-dev/  (60 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    skills/  (53 files)
      … 53 files under this directory
    LICENSE
    README.md
  pr-review-toolkit/  (10 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (6 files)
      … 6 files under this directory
    commands/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  project-artifact/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (3 files)
      … 3 files under this directory
    LICENSE
    README.md
  pyright-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  ralph-loop/  (9 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    commands/  (3 files)
      … 3 files under this directory
    hooks/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  receipts/  (6 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    skills/  (2 files)
      … 2 files under this directory
    LICENSE
    README.md
  ruby-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  rust-analyzer-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  security-guidance/  (88 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    hooks/  (13 files)
      … 13 files under this directory
    tests/  (72 files)
      … 72 files under this directory
    LICENSE
    README.md
  session-report/  (5 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (3 files)
      … 3 files under this directory
    LICENSE
  skill-creator/  (21 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    skills/  (18 files)
      … 18 files under this directory
    LICENSE
    README.md
  swift-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  theme-examples/  (23 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    hooks/  (19 files)
      … 19 files under this directory
    types/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
  typescript-lsp/  (3 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    LICENSE
    README.md
.gitignore
LICENSE
README.md
```

## Entry points

- [.github/scripts/discover_bumps.py:228](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/.github/scripts/discover_bumps.py#L228)
- [plugins/claude-for-manufacturing/shared/scripts/plant_setup.py:1418](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/claude-for-manufacturing/shared/scripts/plant_setup.py#L1418)
- [plugins/claude-for-manufacturing/skills/morning-plant-pulse/scripts/pulse_compute.py:2272](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/claude-for-manufacturing/skills/morning-plant-pulse/scripts/pulse_compute.py#L2272)
- [plugins/claude-for-manufacturing/skills/morning-plant-pulse/scripts/render_short.py:805](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/claude-for-manufacturing/skills/morning-plant-pulse/scripts/render_short.py#L805)
- [plugins/claude-security/hooks/hooks.py:491](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/claude-security/hooks/hooks.py#L491)
- [plugins/claude-security/scripts/patch_artifacts.py:1281](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/claude-security/scripts/patch_artifacts.py#L1281)
- [plugins/claude-security/scripts/render_report.py:978](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/claude-security/scripts/render_report.py#L978)
- [plugins/claude-security/scripts/save_result.py:531](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/claude-security/scripts/save_result.py#L531)
- [plugins/claude-security/scripts/write_scan_meta.py:548](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/claude-security/scripts/write_scan_meta.py#L548)
- [plugins/code-modernization/scripts/baseline_diff.py:808](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/code-modernization/scripts/baseline_diff.py#L808)
- [plugins/code-modernization/scripts/build_report.py:724](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/code-modernization/scripts/build_report.py#L724)
- [plugins/code-modernization/scripts/compare.py:486](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/code-modernization/scripts/compare.py#L486)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 90 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 34 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Args, AttackPath, Branch, CannotContinueError, Change, ChangedFiles. Observed top-level f… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: build_investigate_prompt, build_refute_prompt, cap_diff_for_prompt, filter_by_severity, fo… |
| external_plugins package | library | Observed | Groups 4 file(s) under external_plugins package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 101 file(s) under plugins package (observed from repository paths and static analysis). Observed top-level classes: Catalog, CatalogFile, Category, CategoryNames, Chain, Confidence. Observed top-level functions:… |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 89 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Base, BaselineDiff, BaselineEvidence, Box, BuildFacts, BuildReport. Observed top-level functions: _add, _ad… |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.github/bump-tracking.json` (config)
- `.github/policy/schema.json` (config)
- `.github/workflows/bump-plugin-shas.yml` (ci)
- `.github/workflows/check-mcp-urls.yml` (ci)
- `.github/workflows/close-external-prs.yml` (ci)
- `.github/workflows/revert-failed-bumps.yml` (ci)
- `.github/workflows/scan-plugins.yml` (ci)
- `.github/workflows/validate-licenses.yml` (ci)
- `.github/workflows/validate-plugins.yml` (ci)
- `external_plugins/asana/.claude-plugin/plugin.json` (config)
- `external_plugins/context7/.claude-plugin/plugin.json` (config)
- `external_plugins/context7/.mcp.json` (config)
- `external_plugins/discord/.claude-plugin/plugin.json` (config)
- `external_plugins/discord/.mcp.json` (config)
- `external_plugins/discord/package.json` (manifest)
- `external_plugins/fakechat/.claude-plugin/plugin.json` (config)
- `external_plugins/fakechat/.mcp.json` (config)
- `external_plugins/fakechat/package.json` (manifest)
- `external_plugins/firebase/.claude-plugin/plugin.json` (config)
- `external_plugins/firebase/.mcp.json` (config)
- `external_plugins/github/.claude-plugin/plugin.json` (config)
- `external_plugins/github/.mcp.json` (config)
- `external_plugins/gitlab/.claude-plugin/plugin.json` (config)
- `external_plugins/gitlab/.mcp.json` (config)
- `external_plugins/imessage/.claude-plugin/plugin.json` (config)
- `external_plugins/imessage/.mcp.json` (config)
- `external_plugins/imessage/package.json` (manifest)
- `external_plugins/laravel-boost/.claude-plugin/plugin.json` (config)
- `external_plugins/laravel-boost/.mcp.json` (config)
- `external_plugins/linear/.claude-plugin/plugin.json` (config)
- `external_plugins/linear/.mcp.json` (config)
- `external_plugins/playwright/.claude-plugin/plugin.json` (config)
- `external_plugins/playwright/.mcp.json` (config)
- `external_plugins/serena/.claude-plugin/plugin.json` (config)
- `external_plugins/serena/.mcp.json` (config)
- `external_plugins/telegram/.claude-plugin/plugin.json` (config)
- `external_plugins/telegram/.mcp.json` (config)
- `external_plugins/telegram/package.json` (manifest)
- `external_plugins/terraform/.claude-plugin/plugin.json` (config)
- `external_plugins/terraform/.mcp.json` (config)
- `plugins/agent-sdk-dev/.claude-plugin/plugin.json` (config)
- `plugins/champion-kit/.claude-plugin/plugin.json` (config)
- `plugins/clangd-lsp/.claude-plugin/plugin.json` (config)
- `plugins/claude-code-setup/.claude-plugin/plugin.json` (config)
- `plugins/claude-for-manufacturing/.claude-plugin/plugin.json` (config)
- `plugins/claude-for-manufacturing/.mcp.json` (config)
- `plugins/claude-md-management/.claude-plugin/plugin.json` (config)
- `plugins/claude-security/.claude-plugin/plugin.json` (config)
- `plugins/claude-security/hooks/hooks.json` (config)
- `plugins/claude-security/scripts/lib/cwe-categories.json` (config)
- `plugins/code-modernization/.claude-plugin/plugin.json` (config)
- `plugins/code-modernization/hooks/hooks.json` (config)
- `plugins/code-modernization/tsconfig.json` (config)
- `plugins/code-review/.claude-plugin/plugin.json` (config)
- `plugins/code-simplifier/.claude-plugin/plugin.json` (config)
- `plugins/commit-commands/.claude-plugin/plugin.json` (config)
- `plugins/csharp-lsp/.claude-plugin/plugin.json` (config)
- `plugins/cwc-makers/.claude-plugin/plugin.json` (config)
- `plugins/example-plugin/.claude-plugin/plugin.json` (config)
- `plugins/example-plugin/.mcp.json` (config)
- `plugins/explanatory-output-style/.claude-plugin/plugin.json` (config)
- `plugins/explanatory-output-style/hooks/hooks.json` (config)
- `plugins/feature-dev/.claude-plugin/plugin.json` (config)
- `plugins/frontend-design/.claude-plugin/plugin.json` (config)
- `plugins/gopls-lsp/.claude-plugin/plugin.json` (config)
- `plugins/hookify/.claude-plugin/plugin.json` (config)
- `plugins/hookify/hooks/hooks.json` (config)
- `plugins/jdtls-lsp/.claude-plugin/plugin.json` (config)
- `plugins/kotlin-lsp/.claude-plugin/plugin.json` (config)
- `plugins/learning-output-style/.claude-plugin/plugin.json` (config)
- `plugins/learning-output-style/hooks/hooks.json` (config)
- `plugins/lua-lsp/.claude-plugin/plugin.json` (config)
- `plugins/math-olympiad/.claude-plugin/plugin.json` (config)
- `plugins/math-olympiad/skills/math-olympiad/evals/trigger_eval.json` (config)
- `plugins/math-proof/.claude-plugin/plugin.json` (config)
- `plugins/mcp-server-dev/.claude-plugin/plugin.json` (config)
- `plugins/mcp-tunnels/.claude-plugin/plugin.json` (config)
- `plugins/php-lsp/.claude-plugin/plugin.json` (config)
- `plugins/playground/.claude-plugin/plugin.json` (config)
- `plugins/plugin-dev/.claude-plugin/plugin.json` (config)
- `plugins/plugin-dev/skills/mcp-integration/examples/http-server.json` (config)
- `plugins/plugin-dev/skills/mcp-integration/examples/sse-server.json` (config)
- `plugins/plugin-dev/skills/mcp-integration/examples/stdio-server.json` (config)
- `plugins/pr-review-toolkit/.claude-plugin/plugin.json` (config)
- `plugins/project-artifact/.claude-plugin/plugin.json` (config)
- `plugins/pyright-lsp/.claude-plugin/plugin.json` (config)
- `plugins/ralph-loop/.claude-plugin/plugin.json` (config)
- `plugins/ralph-loop/hooks/hooks.json` (config)
- `plugins/receipts/.claude-plugin/plugin.json` (config)
- `plugins/ruby-lsp/.claude-plugin/plugin.json` (config)
- `plugins/rust-analyzer-lsp/.claude-plugin/plugin.json` (config)
- `plugins/security-guidance/.claude-plugin/plugin.json` (config)
- `plugins/security-guidance/hooks/hooks.json` (config)
- `plugins/session-report/.claude-plugin/plugin.json` (config)
- `plugins/skill-creator/.claude-plugin/plugin.json` (config)
- `plugins/swift-lsp/.claude-plugin/plugin.json` (config)
- `plugins/theme-examples/.claude-plugin/plugin.json` (config)
- `plugins/theme-examples/hooks/hooks.json` (config)
- `plugins/typescript-lsp/.claude-plugin/plugin.json` (config)

## Top-level layout

- `plugins` — 661 analysed file(s)
- `external_plugins` — 59 analysed file(s)
- `.github` — 14 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (4 x likely secret file excluded; 1 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6` is the revision these paths and observations refer to.
