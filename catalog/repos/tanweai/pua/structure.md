# Project structure: tanweai/pua

**Analysed commit:** `e6e6cd237ad17750d179674bff52f8184abea8fd`

**Commit reference:** [e6e6cd237ad17750d179674bff52f8184abea8fd](https://github.com/tanweai/pua/commit/e6e6cd237ad17750d179674bff52f8184abea8fd)

**Tree at this commit:** [tanweai/pua@e6e6cd237ad1](https://github.com/tanweai/pua/tree/e6e6cd237ad17750d179674bff52f8184abea8fd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tanweai/pua |
| Description | 你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement. | Lead: Minwei Wang (https://www.minwei.wang · ORCID: 0009-0002-7976-4689 · DOI: 10.5281/zenodo.24156132) |
| Stars | 19839 |
| Forks | 1202 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `e6e6cd237ad17750d179674bff52f8184abea8fd` |
| Retrieved at | 2026-11-14T19:08:06.735063+00:00 |
| Files in this snapshot | 242 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.codebuddy-plugin/  (2 files)
  marketplace.json
  plugin.json
.codex/  (1 files)
  INSTALL.md
.github/  (6 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    config.yml
    feature_request.md
    question.md
  workflows/  (1 files)
    release.yml
  CONTRIBUTING.md
.trae/  (3 files)
  skills/  (3 files)
    pua/  (1 files)
      … 1 files under this directory
    pua-en/  (1 files)
      … 1 files under this directory
    pua-trae/  (1 files)
      … 1 files under this directory
agents/  (7 files)
  cto-p10.md
  pua-action-executor.md
  pua-policy-guardian.md
  pua-self-reviewer.md
  pua-verifier.md
  senior-engineer-p7.md
  tech-lead-p9.md
assets/  (2 files)
  pua-skill-lockup.svg
  pua-skill-logo.svg
chatgpt/  (3 files)
  pua/  (2 files)
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  PUA-Paste.md
codebuddy/  (3 files)
  pua/  (1 files)
    SKILL.md
  pua-en/  (1 files)
    SKILL.md
  pua-ja/  (1 files)
    SKILL.md
codex/  (21 files)
  pua/  (2 files)
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  pua-cancel-loop/  (1 files)
    SKILL.md
  pua-en/  (1 files)
    SKILL.md
  pua-flavor/  (1 files)
    SKILL.md
  pua-ja/  (1 files)
    SKILL.md
  pua-kpi/  (1 files)
    SKILL.md
  pua-loop/  (1 files)
    SKILL.md
  pua-mama/  (1 files)
    SKILL.md
  pua-off/  (1 files)
    SKILL.md
  pua-offline/  (1 files)
    SKILL.md
  pua-on/  (1 files)
    SKILL.md
  pua-p10/  (1 files)
    SKILL.md
  pua-p7/  (1 files)
    SKILL.md
  pua-p9/  (1 files)
    SKILL.md
  pua-pro/  (1 files)
    SKILL.md
  pua-reap-orphans/  (1 files)
    SKILL.md
  pua-survey/  (1 files)
    SKILL.md
  pua-team-status/  (1 files)
    SKILL.md
  pua-teardown-all/  (1 files)
    SKILL.md
  pua-yes/  (1 files)
    SKILL.md
commands/  (22 files)
  again.md
  cancel-pua-loop.md
  ding.md
  done-check.md
  evidence.md
  flavor.md
  kpi.md
  mama.md
  off.md
  offline.md
  on.md
  p10.md
  p7.md
  p9.md
  pro.md
  pua-loop.md
  pua.md
  reap-orphans.md
  survey.md
  team-status.md
  teardown-all.md
  yes.md
compat/  (2 files)
  runtime-contract.md
  runtime-core.md
cursor/  (3 files)
  rules/  (3 files)
    pua-en.mdc
    pua-ja.mdc
    pua.mdc
docs/  (7 files)
  FAQ.md
  MODEL-COMPAT-20260909.md
  MODEL-COMPAT-RESULTS-20260909.md
  MODEL-MATRIX-20260909.md
  PUA-FABLE-5-20260909.md
  PUA-FABLE-EVAL-WORKFLOW.md
  TESTING.md
evals/  (40 files)
  trigger-prompts/  (2 files)
    should-not-trigger.txt
    should-trigger.txt
  cc0_fable_evidence.py
  check-fable-artifacts.py
  check-model-compat-fix.py
  check-model-compat-text.py
  evals.json
  grade-fable-evals.py
  inspect-claude-evidence.py
  model_compat_utils.py
  omp_evidence.py
  prepare-fable-evals.py
  prepare-model-compat.py
  prepare-multimodel-evals.py
  render-fable-review.py
  run-cc0-fable.py
  run-claude-model-compat.py
  run-codex-pua.py
  run-omp-pua.py
  run-trigger-test.sh
  test-agent-governance.sh
  test-behavior.sh
  test-cc0-fable.py
  test-codex-evidence.py
  test-feedback-runtime.py
  test-helpers.sh
  … 14 more files
hermes/  (3 files)
  pua/  (1 files)
    SKILL.md
  pua-en/  (1 files)
    SKILL.md
  pua-ja/  (1 files)
    SKILL.md
hooks/  (12 files)
  checkpoint-save.sh
  failure-detector.sh
  flavor-helper.sh
  frustration-trigger.sh
  hooks.json
  integrity-guard.sh
  pua-loop-hook.sh
  runtime-state.py
  sanitize-session.sh
  session-restore.sh
  stop-feedback.sh
  subagent-teardown.sh
kimi/  (3 files)
  pua/  (1 files)
    SKILL.md
  pua-en/  (1 files)
    SKILL.md
  pua-ja/  (1 files)
    SKILL.md
kiro/  (3 files)
  steering/  (3 files)
    pua-en.md
    pua-ja.md
    pua.md
landing/  (21 files)
  public/  (1 files)
    vite.svg
  src/  (8 files)
    components/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    test/  (1 files)
      … 1 files under this directory
    App.tsx
    i18n.ts
    index.css
    main.tsx
  .gitignore
  README.md
  components.json
  eslint.config.js
  index.html
  package.json
  tsconfig.app.json
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
  vitest.config.ts
  wrangler.toml
pi/  (9 files)
  package/  (4 files)
    extensions/  (1 files)
      … 1 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  pua/  (5 files)
    INSTALL.md
    README.md
    global.d.ts
    index.ts
    tsconfig.json
scripts/  (3 files)
  build-model-compat.py
  prepare-release.py
  setup-pua-loop.sh
skills/  (44 files)
  ding/  (3 files)
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  mama/  (1 files)
    SKILL.md
  p10/  (1 files)
    SKILL.md
  p7/  (1 files)
    SKILL.md
  p9/  (1 files)
    SKILL.md
  pro/  (1 files)
    SKILL.md
  pua/  (31 files)
    references/  (30 files)
      … 30 files under this directory
    SKILL.md
  pua-en/  (1 files)
    SKILL.md
  pua-ja/  (1 files)
    SKILL.md
  pua-loop/  (1 files)
    SKILL.md
  shot/  (1 files)
    SKILL.md
  yes/  (1 files)
    SKILL.md
trae/  (4 files)
  DIFF.md
  INSTALL.md
  pua-en.md
  pua.md
vscode/  (9 files)
  instructions/  (3 files)
    pua-en.instructions.md
    pua-ja.instructions.md
    pua.instructions.md
  prompts/  (3 files)
    pua-en.prompt.md
    pua-ja.prompt.md
    pua.prompt.md
  copilot-instructions-en.md
  copilot-instructions-ja.md
  copilot-instructions.md
.gitignore
CHANGELOG.md
README.ja.md
README.md
README.zh-CN.md
landing.html
plugin.json
```

## Entry points

- [evals/check-fable-artifacts.py:148](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/check-fable-artifacts.py#L148)
- [evals/check-model-compat-fix.py:141](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/check-model-compat-fix.py#L141)
- [evals/check-model-compat-text.py:72](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/check-model-compat-text.py#L72)
- [evals/grade-fable-evals.py:101](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/grade-fable-evals.py#L101)
- [evals/inspect-claude-evidence.py:34](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/inspect-claude-evidence.py#L34)
- [evals/prepare-fable-evals.py:82](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/prepare-fable-evals.py#L82)
- [evals/prepare-model-compat.py:110](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/prepare-model-compat.py#L110)
- [evals/prepare-multimodel-evals.py:109](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/prepare-multimodel-evals.py#L109)
- [evals/render-fable-review.py:96](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/render-fable-review.py#L96)
- [evals/run-cc0-fable.py:177](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/run-cc0-fable.py#L177)
- [evals/run-claude-model-compat.py:110](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/run-claude-model-compat.py#L110)
- [evals/run-codex-pua.py:1161](https://github.com/tanweai/pua/blob/e6e6cd237ad17750d179674bff52f8184abea8fd/evals/run-codex-pua.py#L1161)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 23 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CodexEvidenceRunnerTests, EvidenceTests, FeedbackTests, HookRuntimeTests, ModelCompatArti… |
| evals package | library | Observed | Groups 17 file(s) under evals package (observed from repository paths and static analysis). Observed top-level functions: _agent_end_record, _block_type, _canonical_selector, _event_messages, _load_messages, _message_co… |
| hooks package | library | Observed | Groups 10 file(s) under hooks package (observed from repository paths and static analysis). |
| landing package | library | Observed | Groups 9 file(s) under landing package (observed from repository paths and static analysis). |
| pi package | library | Observed | Groups 3 file(s) under pi package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.codebuddy-plugin/marketplace.json` (config)
- `.codebuddy-plugin/plugin.json` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/release.yml` (ci)
- `evals/evals.json` (config)
- `hooks/hooks.json` (config)
- `landing/components.json` (config)
- `landing/package.json` (manifest)
- `landing/tsconfig.app.json` (config)
- `landing/tsconfig.json` (config)
- `landing/tsconfig.node.json` (config)
- `landing/wrangler.toml` (config)
- `pi/package/package.json` (manifest)
- `pi/pua/tsconfig.json` (config)
- `plugin.json` (config)

## Top-level layout

- `skills` — 44 analysed file(s)
- `evals` — 40 analysed file(s)
- `commands` — 22 analysed file(s)
- `codex` — 21 analysed file(s)
- `landing` — 21 analysed file(s)
- `hooks` — 12 analysed file(s)
- `pi` — 9 analysed file(s)
- `vscode` — 9 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `agents` — 7 analysed file(s)
- `docs` — 7 analysed file(s)
- `.github` — 6 analysed file(s)
- `trae` — 4 analysed file(s)
- `.trae` — 3 analysed file(s)
- `chatgpt` — 3 analysed file(s)
- `codebuddy` — 3 analysed file(s)
- `cursor` — 3 analysed file(s)
- `hermes` — 3 analysed file(s)
- `kimi` — 3 analysed file(s)
- `kiro` — 3 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `.codebuddy-plugin` — 2 analysed file(s)
- `assets` — 2 analysed file(s)
- `compat` — 2 analysed file(s)
- `.codex` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e6e6cd237ad17750d179674bff52f8184abea8fd` is the revision these paths and observations refer to.
