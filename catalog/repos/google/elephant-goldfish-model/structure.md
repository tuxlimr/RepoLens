# Project structure: google/elephant-goldfish-model

**Analysed commit:** `e4747323aab66157812cd3a71755f6447b2803a2`

**Commit reference:** [e4747323aab66157812cd3a71755f6447b2803a2](https://github.com/google/elephant-goldfish-model/commit/e4747323aab66157812cd3a71755f6447b2803a2)

**Tree at this commit:** [google/elephant-goldfish-model@e4747323aab6](https://github.com/google/elephant-goldfish-model/tree/e4747323aab66157812cd3a71755f6447b2803a2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google/elephant-goldfish-model |
| Description | Open-source plugin for designing and reviewing software with agents |
| Stars | 19058 |
| Forks | 1416 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `e4747323aab66157812cd3a71755f6447b2803a2` |
| Retrieved at | 2026-11-14T19:08:17.392286+00:00 |
| Files in this snapshot | 269 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.claude-plugin/  (12 files)
  agents/  (10 files)
    bootstrap_orchestrator.md
    codebase_details.md
    comprehension.md
    design_critic.md
    implementation_readiness.md
    inventive_catalyst.md
    structural.md
    style.md
    synthesizer.md
    zoom_out.md
  marketplace.json
  plugin.json
.codex-plugin/  (1 files)
  plugin.json
.cursor-plugin/  (12 files)
  agents/  (8 files)
    codebase_details.md
    comprehension.md
    design_critic.md
    implementation_readiness.md
    inventive_catalyst.md
    structural.md
    style.md
    zoom_out.md
  assets/  (1 files)
    icon.svg
  rules/  (1 files)
    egm.mdc
  marketplace.json
  plugin.json
.gemini/  (2 files)
  config.yaml
  styleguide.md
.github/  (17 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    config.yml
    feature_proposal.md
    task.md
  scripts/  (1 files)
    review_pr.py
  workflows/  (9 files)
    copilot-native.yml
    cursor-native.yml
    deploy-site.yml
    opencode-native.yml
    pr-scope-advisory.yml
    pr-triage-review.yml
    release.yml
    scorecard.yml
    tests.yml
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.plugin/  (1 files)
  plugin.json
.vscode/  (1 files)
  settings.json
.windsurf/  (8 files)
  rules/  (1 files)
    egm.md
  workflows/  (7 files)
    egm-bootstrap.md
    egm-brainstorm.md
    egm-draft.md
    egm-drift-report.md
    egm-resolve.md
    egm-review-loop.md
    egm-review.md
adapters/  (1 files)
  opencode/  (1 files)
    install.py
agents/  (10 files)
  bootstrap_orchestrator.md
  codebase_details.md
  comprehension.md
  design_critic.md
  implementation_readiness.md
  inventive_catalyst.md
  structural.md
  style.md
  synthesizer.md
  zoom_out.md
assets/  (1 files)
  icon.svg
com.github.copilot/  (9 files)
  agents/  (9 files)
    egm-codebase-details.agent.md
    egm-comprehension.agent.md
    egm-design.agent.md
    egm-implementation-readiness.agent.md
    egm-inventive-catalyst.agent.md
    egm-structural.agent.md
    egm-style.agent.md
    egm-zoom-out.agent.md
    egm.agent.md
docs/  (46 files)
  assets/  (1 files)
    readme-header.svg
  designs/  (19 files)
    README.md
    additional-harnesses.md
    architecture.md
    ask.md
    bootstrap.md
    brainstorm.md
    claude_release_branch_distribution.md
    draft.md
    drift_report.md
    multi_harness_support.md
    plugin_listing_presentation.md
    releases.md
    review.md
    runtime_packaging.md
    site_documentation.md
    skill_icons.md
    synthesizer.md
    triz_integration.md
    windsurf_support.md
  site/  (12 files)
    skills/  (7 files)
      … 7 files under this directory
    getting-started.md
    guide.md
    install.md
    skills.md
    workflow.md
  verification/  (1 files)
    skill-discovery-316.md
  claude.md
  codex.md
  copilot.md
  cursor.md
  directory.md
  faq.md
  getting_started.md
  harnesses.md
  index.md
  muse.md
  opencode.md
  privacy.md
  releases.md
resources/  (7 files)
  document_standards/  (5 files)
    feature-spec-standard.md
    heilmeier-standard.md
    implementation-readiness-standard.md
    re-implementation-standard.md
    zoom-out-standard.md
  README.md
  execution_instructions.md
scripts/  (2 files)
  pack_plugin.py
  prepare_release.py
site/  (57 files)
  public/  (3 files)
    CNAME
    favicon.svg
    robots.txt
  scripts/  (4 files)
    capture.mjs
    check-docs.mjs
    og.html
    verify-analytics.mjs
  src/  (42 files)
    assets/  (11 files)
      … 11 files under this directory
    components/  (21 files)
      … 21 files under this directory
    layouts/  (1 files)
      … 1 files under this directory
    lib/  (2 files)
      … 2 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    styles/  (4 files)
      … 4 files under this directory
    content.config.ts
  tests/  (3 files)
    analytics.test.mjs
    copy-accessibility.test.mjs
    explainer.test.mjs
  .gitignore
  README.md
  astro.config.mjs
  package.json
  tsconfig.json
skills/  (38 files)
  egm-bootstrap/  (7 files)
    agents/  (1 files)
      … 1 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
    TEST.md
    test_scenarios.yaml
  egm-brainstorm/  (5 files)
    agents/  (1 files)
      … 1 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    SKILL.md
    TEST.md
    test_scenarios.yaml
  egm-draft/  (6 files)
    agents/  (1 files)
      … 1 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
    TEST.md
    test_scenarios.yaml
  egm-drift-report/  (5 files)
    agents/  (1 files)
      … 1 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    SKILL.md
    TEST.md
    test_scenarios.yaml
  egm-resolve/  (5 files)
    agents/  (1 files)
      … 1 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    SKILL.md
    TEST.md
    test_scenarios.yaml
  egm-review/  (5 files)
    agents/  (1 files)
      … 1 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    SKILL.md
    TEST.md
    test_scenarios.yaml
  egm-review-loop/  (5 files)
    agents/  (1 files)
      … 1 files under this directory
    assets/  (1 files)
      … 1 files under this directory
    SKILL.md
    TEST.md
    test_scenarios.yaml
tests/  (31 files)
  integration/  (8 files)
    opencode-ci/  (2 files)
      … 2 files under this directory
    copilot_controlled_probe.py
    cursor_child_reads.py
    opencode_native_probe.py
    opencode_trace_verifier.py
    test_claude.py
    test_codex.py
  unit/  (20 files)
    test_ci_workflow.py
    test_claude_traces.py
    test_codex_traces.py
    test_copilot_adapter.py
    test_cursor.py
    test_cursor_child_reads.py
    test_frontmatter.py
    test_harnesses.py
    test_link_integrity.py
    test_markdown_tables.py
    test_opencode_adapter.py
    test_opencode_trace_verifier.py
    test_packaging.py
    test_pr_triage_review.py
    test_releases.py
    test_scenario_coverage.py
    test_scope_advisory.py
    test_skill_load_limits.py
    test_style_and_boundaries.py
    test_windsurf.py
  conftest.py
  pr_triage_post.cjs
  scope_advisory.cjs
.editorconfig
.gitattributes
.gitignore
ACCESSIBILITY.md
AGENTS.md
AI_POLICY.md
CONTRIBUTING.md
LICENSE
README.md
TESTING.md
plugin.json
pyproject.toml
```

## Entry points

- [.github/scripts/review_pr.py:1789](https://github.com/google/elephant-goldfish-model/blob/e4747323aab66157812cd3a71755f6447b2803a2/.github/scripts/review_pr.py#L1789)
- [adapters/opencode/install.py:143](https://github.com/google/elephant-goldfish-model/blob/e4747323aab66157812cd3a71755f6447b2803a2/adapters/opencode/install.py#L143)
- [scripts/pack_plugin.py:132](https://github.com/google/elephant-goldfish-model/blob/e4747323aab66157812cd3a71755f6447b2803a2/scripts/pack_plugin.py#L132)
- [scripts/prepare_release.py:93](https://github.com/google/elephant-goldfish-model/blob/e4747323aab66157812cd3a71755f6447b2803a2/scripts/prepare_release.py#L93)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: build, install, name, prepare, version_for_tag. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 8 file(s) under site package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 41 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: EvidenceError, MockProvider. Observed top-level functions: _identifier, _interval, _nonempty_file_output, _… |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.cursor-plugin/marketplace.json` (config)
- `.cursor-plugin/plugin.json` (config)
- `.editorconfig` (config)
- `.gemini/config.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/copilot-native.yml` (ci)
- `.github/workflows/cursor-native.yml` (ci)
- `.github/workflows/deploy-site.yml` (ci)
- `.github/workflows/opencode-native.yml` (ci)
- `.github/workflows/pr-scope-advisory.yml` (ci)
- `.github/workflows/pr-triage-review.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.plugin/plugin.json` (config)
- `.vscode/settings.json` (config)
- `plugin.json` (config)
- `pyproject.toml` (manifest)
- `site/package.json` (manifest)
- `site/tsconfig.json` (config)
- `skills/egm-bootstrap/agents/openai.yaml` (config)
- `skills/egm-bootstrap/references/worker-return.schema.json` (config)
- `skills/egm-brainstorm/agents/openai.yaml` (config)
- `skills/egm-draft/agents/openai.yaml` (config)
- `skills/egm-drift-report/agents/openai.yaml` (config)
- `skills/egm-resolve/agents/openai.yaml` (config)
- `skills/egm-review-loop/agents/openai.yaml` (config)
- `skills/egm-review/agents/openai.yaml` (config)

## Top-level layout

- `site` — 57 analysed file(s)
- `docs` — 46 analysed file(s)
- `skills` — 38 analysed file(s)
- `tests` — 31 analysed file(s)
- `.github` — 17 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.claude-plugin` — 12 analysed file(s)
- `.cursor-plugin` — 12 analysed file(s)
- `agents` — 10 analysed file(s)
- `com.github.copilot` — 9 analysed file(s)
- `.windsurf` — 8 analysed file(s)
- `resources` — 7 analysed file(s)
- `.gemini` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)
- `.plugin` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `adapters` — 1 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e4747323aab66157812cd3a71755f6447b2803a2` is the revision these paths and observations refer to.
