# Project structure: DietrichGebert/ponytail

**Analysed commit:** `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`

**Commit reference:** [96608e078b2d5ea607c5c3b8b5a54d1c1fba6846](https://github.com/DietrichGebert/ponytail/commit/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846)

**Tree at this commit:** [DietrichGebert/ponytail@96608e078b2d](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | DietrichGebert/ponytail |
| Description | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. |
| Stars | 190790 |
| Forks | 10668 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846` |
| Retrieved at | 2026-11-14T19:10:32.159287+00:00 |
| Files in this snapshot | 170 |

## Directory tree

```text
.agents/  (2 files)
  plugins/  (1 files)
    marketplace.json
  rules/  (1 files)
    ponytail.md
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.clinerules/  (1 files)
  ponytail.md
.codex-plugin/  (1 files)
  plugin.json
.cursor/  (1 files)
  rules/  (1 files)
    ponytail.mdc
.devin-plugin/  (1 files)
  plugin.json
.github/  (7 files)
  plugin/  (2 files)
    marketplace.json
    plugin.json
  workflows/  (2 files)
    publish.yml
    test.yml
  CONTRIBUTING.md
  FUNDING.yml
  copilot-instructions.md
.grok-plugin/  (1 files)
  marketplace.json
.kimi-plugin/  (1 files)
  plugin.json
.kiro/  (1 files)
  steering/  (1 files)
    ponytail.md
.openclaw/  (6 files)
  skills/  (6 files)
    ponytail/  (1 files)
      … 1 files under this directory
    ponytail-audit/  (1 files)
      … 1 files under this directory
    ponytail-debt/  (1 files)
      … 1 files under this directory
    ponytail-gain/  (1 files)
      … 1 files under this directory
    ponytail-help/  (1 files)
      … 1 files under this directory
    ponytail-review/  (1 files)
      … 1 files under this directory
.opencode/  (9 files)
  command/  (6 files)
    ponytail-audit.md
    ponytail-debt.md
    ponytail-gain.md
    ponytail-help.md
    ponytail-review.md
    ponytail.md
  plugins/  (3 files)
    index.js
    ponytail-frontmatter.cjs
    ponytail.mjs
.qoder/  (1 files)
  rules/  (1 files)
    ponytail.md
.qoder-plugin/  (1 files)
  plugin.json
.windsurf/  (1 files)
  rules/  (1 files)
    ponytail.md
assets/  (9 files)
  benchmark-3model.svg
  benchmark-agentic.svg
  logo-dark.svg
  logo-greenpt-dark.svg
  logo-greenpt.svg
  photoreunion-logo-dark.svg
  photoreunion-logo-light.svg
  retriever-logo-dark.svg
  retriever-logo-light.svg
benchmarks/  (30 files)
  agentic/  (7 files)
    README.md
    answer.py
    compare.py
    complete.py
    judge.py
    run.py
    tasks.py
  arms/  (4 files)
    baseline.js
    caveman-SKILL.md
    caveman.js
    ponytail.js
  results/  (10 files)
    2026-06-12-caveman-vs-ponytail.md
    2026-06-12-v4-hardening-vs-caveman.md
    2026-06-15-llama3.2-local.md
    2026-06-16-correctness-gate-fix.md
    2026-06-16-robustness-audit.md
    2026-06-17-agentic-safety.md
    2026-06-17-cost-verification.md
    2026-06-18-agentic.md
    2026-06-22-issue-245-217-comprehension.md
    2026-10-07-agentic.md
  .env.example
  README.md
  behavior.js
  behavior.yaml
  correctness.js
  loc.js
  promptfooconfig.gemini.yaml
  promptfooconfig.gpt-newest.yaml
  promptfooconfig.yaml
commands/  (6 files)
  ponytail-audit.toml
  ponytail-debt.toml
  ponytail-gain.toml
  ponytail-help.toml
  ponytail-review.toml
  ponytail.toml
docs/  (2 files)
  agent-portability.md
  cursor-hooks.md
examples/  (12 files)
  README.md
  csv-sum.md
  debounce.md
  deep-clone.md
  email-validation.md
  group-by.md
  infinite-scroll.md
  modal-dialog.md
  number-formatting.md
  rate-limit.md
  react-countdown.md
  url-params.md
hooks/  (20 files)
  band/  (5 files)
    board.ts
    logo.ts
    metrics.ts
    register.tsx
    types.d.ts
  claude-band.json
  claude-codex-hooks.json
  copilot-hooks.json
  cursor-hooks.json
  ponytail-activate.js
  ponytail-band-import.js
  ponytail-config.js
  ponytail-instructions.js
  ponytail-map.js
  ponytail-mode-tracker.js
  ponytail-runtime.js
  ponytail-statusline.ps1
  ponytail-statusline.sh
  ponytail-subagent.js
  qoder-hooks.json
i18n/  (4 files)
  README.es.md
  README.ja.md
  README.ko.md
  README.zh-CN.md
pi-extension/  (4 files)
  test/  (2 files)
    extension.test.js
    helpers.test.js
  index.js
  package.json
scripts/  (6 files)
  build-openclaw-skills.js
  check-rule-copies.js
  check-versions.js
  cursor-hooks.js
  publish-openclaw-skills.js
  uninstall.js
skills/  (7 files)
  ponytail/  (1 files)
    SKILL.md
  ponytail-audit/  (1 files)
    SKILL.md
  ponytail-debt/  (1 files)
    SKILL.md
  ponytail-gain/  (1 files)
    SKILL.md
  ponytail-help/  (1 files)
    SKILL.md
  ponytail-review/  (1 files)
    SKILL.md
  plugin.json
tests/  (22 files)
  activation-map.test.js
  band-import.test.js
  band.test.tsx
  behavior.test.js
  commands.test.js
  copilot-plugin.test.js
  correctness.test.js
  cursor-hooks.test.js
  gemini-extension.test.js
  grok-plugin.test.js
  hermes-plugin.test.js
  hooks-windows.test.js
  hooks.test.js
  kimi-plugin.test.js
  loc.test.js
  map.test.js
  openclaw-skills.test.js
  opencode-plugin.test.js
  package-scripts.test.js
  package.test.js
  qoder-plugin.test.js
  uninstall.test.js
.gitignore
AGENTS.md
INSTALL.md
LICENSE
README.md
__init__.py
after-install.md
gemini-extension.json
opencode.json
package.json
plugin.json
plugin.yaml
```

## Entry points

- [benchmarks/agentic/answer.py:287](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/benchmarks/agentic/answer.py#L287)
- [benchmarks/agentic/compare.py:92](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/benchmarks/agentic/compare.py#L92)
- [benchmarks/agentic/complete.py:177](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/benchmarks/agentic/complete.py#L177)
- [benchmarks/agentic/judge.py:197](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/benchmarks/agentic/judge.py#L197)
- [benchmarks/agentic/run.py:542](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/benchmarks/agentic/run.py#L542)
- [.opencode/plugins/index.js](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/.opencode/plugins/index.js)
- [pi-extension/index.js](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/pi-extension/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 7 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level functions: _contained, _fail, _find, _find_class, _import, _import_pkg. |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: _config_dir, _default_mode, _fallback_instructions, _filter_skill_body_for_mode, _handle_mode_comma… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _base_cmd, _cells, _claude_version, _cli_call, _count, _fixed_diff. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 14 file(s) under hooks package (observed from repository paths and static analysis). |
| pi-extension package | library | Observed | Groups 1 file(s) under pi-extension package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 24 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.devin-plugin/plugin.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/plugin/marketplace.json` (config)
- `.github/plugin/plugin.json` (config)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.grok-plugin/marketplace.json` (config)
- `.kimi-plugin/plugin.json` (config)
- `.qoder-plugin/plugin.json` (config)
- `benchmarks/.env.example` (config)
- `benchmarks/behavior.yaml` (config)
- `benchmarks/promptfooconfig.gemini.yaml` (config)
- `benchmarks/promptfooconfig.gpt-newest.yaml` (config)
- `benchmarks/promptfooconfig.yaml` (config)
- `commands/ponytail-audit.toml` (config)
- `commands/ponytail-debt.toml` (config)
- `commands/ponytail-gain.toml` (config)
- `commands/ponytail-help.toml` (config)
- `commands/ponytail-review.toml` (config)
- `commands/ponytail.toml` (config)
- `gemini-extension.json` (config)
- `hooks/claude-band.json` (config)
- `hooks/claude-codex-hooks.json` (config)
- `hooks/copilot-hooks.json` (config)
- `hooks/cursor-hooks.json` (config)
- `hooks/qoder-hooks.json` (config)
- `opencode.json` (config)
- `package.json` (manifest)
- `pi-extension/package.json` (manifest)
- `plugin.json` (config)
- `plugin.yaml` (config)
- `skills/plugin.json` (config)

## Top-level layout

- `benchmarks` — 30 analysed file(s)
- `tests` — 22 analysed file(s)
- `hooks` — 20 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `examples` — 12 analysed file(s)
- `.opencode` — 9 analysed file(s)
- `assets` — 9 analysed file(s)
- `.github` — 7 analysed file(s)
- `skills` — 7 analysed file(s)
- `.openclaw` — 6 analysed file(s)
- `commands` — 6 analysed file(s)
- `scripts` — 6 analysed file(s)
- `i18n` — 4 analysed file(s)
- `pi-extension` — 4 analysed file(s)
- `.agents` — 2 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `docs` — 2 analysed file(s)
- `.clinerules` — 1 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)
- `.cursor` — 1 analysed file(s)
- `.devin-plugin` — 1 analysed file(s)
- `.grok-plugin` — 1 analysed file(s)
- `.kimi-plugin` — 1 analysed file(s)
- `.kiro` — 1 analysed file(s)
- `.qoder` — 1 analysed file(s)
- `.qoder-plugin` — 1 analysed file(s)
- `.windsurf` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846` is the revision these paths and observations refer to.
