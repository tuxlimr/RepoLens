# Project structure: AgriciDaniel/claude-obsidian

**Analysed commit:** `2e545563172f97f02ecaaaab376ceea1246a0583`

**Commit reference:** [2e545563172f97f02ecaaaab376ceea1246a0583](https://github.com/AgriciDaniel/claude-obsidian/commit/2e545563172f97f02ecaaaab376ceea1246a0583)

**Tree at this commit:** [AgriciDaniel/claude-obsidian@2e545563172f](https://github.com/AgriciDaniel/claude-obsidian/tree/2e545563172f97f02ecaaaab376ceea1246a0583)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | AgriciDaniel/claude-obsidian |
| Description | Self-organizing AI second brain for Obsidian + Claude Code. Drop any source and Claude reads, links, and files it into one connected knowledge graph of plain Markdown you own. AI note-taking, personal knowledge management (PKM), and an open-source Notion alternative. Based on Karpathy's LLM Wiki pa… |
| Stars | 16492 |
| Forks | 1619 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `2e545563172f97f02ecaaaab376ceea1246a0583` |
| Retrieved at | 2026-11-14T19:08:46.772819+00:00 |
| Files in this snapshot | 255 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.cursor/  (1 files)
  rules/  (1 files)
    claude-obsidian.mdc
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    codeql.yml
    test.yml
  FUNDING.yml
  copilot-instructions.md
  dependabot.yml
  pull_request_template.md
.windsurf/  (1 files)
  rules/  (1 files)
    claude-obsidian.md
agents/  (3 files)
  verifier.md
  wiki-ingest.md
  wiki-lint.md
assets/  (5 files)
  diagrams/  (2 files)
    knowledge-loop.svg
    product-vault-boundary.svg
  readme/  (3 files)
    btn-hub.svg
    btn-pro.svg
    btn-youtube.svg
claude_obsidian/  (32 files)
  __init__.py
  __main__.py
  artifacts.py
  capacity.py
  capture.py
  checkpoint.py
  cli.py
  contracts.py
  extensions.py
  gates.py
  gitignore.py
  hook_adapter.py
  json_utils.py
  ledgers.py
  legacy_lock.py
  limits.py
  lint_engine.py
  markdown_links.py
  mode_config.py
  ollama.py
  package_validation.py
  page_schema.py
  paths.py
  prompt_eval.py
  … 8 more files
config/  (6 files)
  adapters.json
  capabilities.json
  product-contract.json
  public-marketplace.json
  release-allowlist.json
  upstream-references.json
docs/  (13 files)
  capacity-and-recovery.md
  compound-vault-guide.md
  dragonscale-guide.md
  install-guide.md
  methodology-modes-guide.md
  namespace-migration.md
  native-conformance.md
  prefix-providers.md
  prompt-evaluation.md
  retrieval-evaluation.md
  upstream-references.md
  windows-wsl.md
  workflow-acceptance.md
examples/  (13 files)
  sample-vault/  (13 files)
    .obsidian/  (1 files)
      … 1 files under this directory
    .raw/  (1 files)
      … 1 files under this directory
    inbox/  (1 files)
      … 1 files under this directory
    wiki/  (8 files)
      … 8 files under this directory
    .claude-obsidian.json
    .gitignore
hooks/  (2 files)
  README.md
  hooks.json
scripts/  (18 files)
  allocate-address.sh
  bm25-index.py
  boundary-score.py
  claude-obsidian.py
  contextual-prefix.py
  detect-transport.sh
  evaluate-prompts.py
  evaluate-retrieval.py
  rerank.py
  retrieve.py
  setup-dragonscale.sh
  setup-mode.sh
  setup-multi-agent.sh
  setup-retrieve.sh
  setup-vault.sh
  tiling-check.py
  wiki-lock.sh
  wiki-mode.py
skills/  (38 files)
  autoresearch/  (2 files)
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  canvas/  (2 files)
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  defuddle/  (1 files)
    SKILL.md
  obsidian-bases/  (1 files)
    SKILL.md
  obsidian-markdown/  (1 files)
    SKILL.md
  save/  (1 files)
    SKILL.md
  think/  (1 files)
    SKILL.md
  wiki/  (15 files)
    references/  (14 files)
      … 14 files under this directory
    SKILL.md
  wiki-cli/  (1 files)
    SKILL.md
  wiki-fold/  (2 files)
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  wiki-ingest/  (1 files)
    SKILL.md
  wiki-lint/  (1 files)
    SKILL.md
  wiki-mode/  (7 files)
    templates/  (6 files)
      … 6 files under this directory
    SKILL.md
  wiki-query/  (1 files)
    SKILL.md
  wiki-retrieve/  (1 files)
    SKILL.md
templates/  (11 files)
  vault/  (11 files)
    .obsidian/  (4 files)
      … 4 files under this directory
    .raw/  (1 files)
      … 1 files under this directory
    inbox/  (1 files)
      … 1 files under this directory
    wiki/  (4 files)
      … 4 files under this directory
    .gitignore
tests/  (83 files)
  fixtures/  (38 files)
    capture/  (1 files)
      … 1 files under this directory
    contracts/  (3 files)
      … 3 files under this directory
    forward/  (4 files)
      … 4 files under this directory
    lint/  (10 files)
      … 10 files under this directory
    migration/  (1 files)
      … 1 files under this directory
    prompt-quality/  (3 files)
      … 3 files under this directory
    release/  (1 files)
      … 1 files under this directory
    retrieval-quality/  (13 files)
      … 13 files under this directory
    setup/  (2 files)
      … 2 files under this directory
  test_allocate_address.sh
  test_bm25_index.py
  test_boundary_score.py
  test_capacity.py
  test_capture.py
  test_checkpoint.py
  test_cli_approval.py
  test_cli_mode.py
  test_concurrent_write.sh
  test_contextual_prefix.py
  test_contracts.py
  test_detect_transport.py
  test_developer_safety.py
  test_distribution_vaults.py
  test_extensions.py
  test_gates.py
  test_gitignore.py
  test_hooks.py
  test_installed_tree_boundary.py
  test_knowledge_contracts.py
  test_ledgers.py
  test_legacy_lock.py
  test_lint_engine.py
  test_native_artifacts.py
  … 21 more files
.gitattributes
.gitignore
AGENTS.md
ATTRIBUTION.md
CHANGELOG.md
CITATION.cff
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
GEMINI.md
LICENSE
Makefile
PRIVACY.md
README.md
RELEASE_MANIFEST.json
SECURITY.md
SHA256SUMS
WIKI.md
ZCODE.md
```

## Entry points

- [claude_obsidian/contracts.py:1364](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/claude_obsidian/contracts.py#L1364)
- [claude_obsidian/legacy_lock.py:688](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/claude_obsidian/legacy_lock.py#L688)
- [claude_obsidian/lint_engine.py:2162](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/claude_obsidian/lint_engine.py#L2162)
- [scripts/bm25-index.py:851](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/scripts/bm25-index.py#L851)
- [scripts/boundary-score.py:350](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/scripts/boundary-score.py#L350)
- [scripts/contextual-prefix.py:1659](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/scripts/contextual-prefix.py#L1659)
- [scripts/evaluate-prompts.py:56](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/scripts/evaluate-prompts.py#L56)
- [scripts/evaluate-retrieval.py:42](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/scripts/evaluate-retrieval.py#L42)
- [scripts/rerank.py:743](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/scripts/rerank.py#L743)
- [scripts/retrieve.py:375](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/scripts/retrieve.py#L375)
- [scripts/tiling-check.py:822](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/scripts/tiling-check.py#L822)
- [scripts/wiki-mode.py:411](https://github.com/AgriciDaniel/claude-obsidian/blob/2e545563172f97f02ecaaaab376ceea1246a0583/scripts/wiki-mode.py#L411)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| claude_obsidian package | library | Observed | Groups 27 file(s) under claude_obsidian package (observed from repository paths and static analysis). Observed top-level classes: ArtifactValidationError, CaptureBudget, CaptureBudgetExceeded, CaptureConfig, CaptureConf… |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: IndexValidationError, LegacyLockError, LockRecord, ParsedArguments, ProviderOperationBudg… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 9 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 83 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AuditTests, BuildTests, CanonicalContractTests, CanonicalPolicyTests, CanonicalReleasePolicyTests, Capacity… |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `RELEASE_MANIFEST.json` (config)
- `config/adapters.json` (config)
- `config/capabilities.json` (config)
- `config/product-contract.json` (config)
- `config/public-marketplace.json` (config)
- `config/release-allowlist.json` (config)
- `config/upstream-references.json` (config)
- `examples/sample-vault/.claude-obsidian.json` (config)
- `examples/sample-vault/.obsidian/app.json` (config)
- `examples/sample-vault/.raw/.manifest.json` (config)
- `hooks/hooks.json` (config)
- `templates/vault/.obsidian/app.json` (config)
- `templates/vault/.obsidian/appearance.json` (config)
- `templates/vault/.obsidian/graph.json` (config)
- `templates/vault/.raw/.manifest.json` (config)

## Top-level layout

- `tests` — 83 analysed file(s)
- `skills` — 38 analysed file(s)
- `claude_obsidian` — 32 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `scripts` — 18 analysed file(s)
- `docs` — 13 analysed file(s)
- `examples` — 13 analysed file(s)
- `templates` — 11 analysed file(s)
- `.github` — 8 analysed file(s)
- `config` — 6 analysed file(s)
- `assets` — 5 analysed file(s)
- `agents` — 3 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `hooks` — 2 analysed file(s)
- `.cursor` — 1 analysed file(s)
- `.windsurf` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2e545563172f97f02ecaaaab376ceea1246a0583` is the revision these paths and observations refer to.
