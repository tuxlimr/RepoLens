# Project structure: NVIDIA/SkillSpector

**Analysed commit:** `c81615007d40e86051a302a3cf897f8a05264928`

**Commit reference:** [c81615007d40e86051a302a3cf897f8a05264928](https://github.com/NVIDIA/SkillSpector/commit/c81615007d40e86051a302a3cf897f8a05264928)

**Tree at this commit:** [NVIDIA/SkillSpector@c81615007d40](https://github.com/NVIDIA/SkillSpector/tree/c81615007d40e86051a302a3cf897f8a05264928)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | NVIDIA/SkillSpector |
| Description | Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them. |
| Stars | 26025 |
| Forks | 2313 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `c81615007d40e86051a302a3cf897f8a05264928` |
| Retrieved at | 2026-11-14T19:07:24.563153+00:00 |
| Files in this snapshot | 471 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (4 files)
    ci.yml
    release.yml
    scorecard.yml
    update-pr-branches.yml
.opencode/  (3 files)
  commands/  (1 files)
    skillspector.md
  tools/  (2 files)
    skillspector_scan.ts
    skillspector_scan_lib.ts
contrib/  (34 files)
  batch_scan/  (34 files)
    docs/  (8 files)
      … 8 files under this directory
    tests/  (15 files)
      … 15 files under this directory
    .env.example
    CONTRIBUTING.md
    __init__.py
    annotation.py
    api_pool.py
    batch_scan.py
    detection.py
    discovery.py
    gap_fill.py
    reports.py
    runner.py
docs/  (42 files)
  release/  (23 files)
    json-quote-ownership-migration.md
    skillspector-2.10.0.md
    skillspector-2.11.0.md
    skillspector-2.11.1.md
    skillspector-2.11.2.md
    skillspector-2.12.0.md
    skillspector-2.5.0.md
    skillspector-2.5.1.md
    skillspector-2.5.2.md
    skillspector-2.5.3.md
    skillspector-2.6.0.md
    skillspector-2.7.0.md
    skillspector-2.7.2.md
    skillspector-2.8.0.md
    skillspector-2.8.1.md
    skillspector-2.8.2.md
    skillspector-2.9.0.md
    skillspector-2.9.1.md
    skillspector-2.9.2.md
    skillspector-2.9.3.md
    skillspector-2.9.4.md
    skillspector-2.9.5.md
    skillspector-2.9.6.md
  validation/  (2 files)
    CONTRIBUTOR_ONBOARDING.md
    contributor-onboarding-2026-11-06.md
  ANALYSIS_RESOURCE_BOUNDS.md
  AS3_SELF_REFERENCES.md
  B.3.1-mcp-least-privilege.md
  B.3.2-mcp-tool-poisoning.md
  DEPENDENCY_CONTENT_INSPECTION.md
  DEPENDENCY_SOURCE_REDIRECTION.md
  DEVELOPMENT.md
  EVAL_DATASETS.md
  INFERENCE_USAGE.md
  LLM_ANALYZER_BASE_GUIDE.md
  NESTED_ARTIFACT_INSPECTION.md
  OPENCODE_EXTENSION.md
  PI_EXTENSION.md
  SC4-osv-live-vulnerability-lookups.md
  SUPPRESSION.md
  passive-documentation-images.md
  scan-completeness.md
extensions/  (1 files)
  skillspector.ts
scripts/  (3 files)
  release/  (1 files)
    public/  (1 files)
      … 1 files under this directory
  compare_scan_accuracy.py
  generate_unicode_confusables.py
skills/  (1 files)
  skill-inspector/  (1 files)
    SKILL.md
src/  (161 files)
  skillspector/  (161 files)
    nodes/  (42 files)
      … 42 files under this directory
    providers/  (48 files)
      … 48 files under this directory
    yara_rules/  (5 files)
      … 5 files under this directory
    __init__.py
    _workflow_warnings.py
    allowed_tools.py
    artifacts.py
    baseline_tokens.py
    cleanup.py
    cli.py
    cli_entry.py
    constants.py
    dependency_downloader.py
    dependency_inspection.py
    dependency_sandbox.py
    dependency_sources.py
    dependency_worker.py
    file_output.py
    graph.py
    graph_proxy.py
    inference_usage.py
    input_handler.py
    inspection_ledger.py
    javascript_ast.py
    javascript_tokens.py
    json_tokens.py
    llm_analyzer_base.py
    … 42 more files
tests/  (205 files)
  docker/  (1 files)
    smoke.sh
  evasion_corpus/  (3 files)
    __init__.py
    corpus.py
    test_canonical_sink_fitness.py
  fixtures/  (53 files)
    as3_self_reference/  (2 files)
      … 2 files under this directory
    e2_shell_env_harvest/  (1 files)
      … 1 files under this directory
    malicious_skill/  (2 files)
      … 2 files under this directory
    mcp_clean_skill/  (2 files)
      … 2 files under this directory
    mcp_mismatched_skill/  (2 files)
      … 2 files under this directory
    mcp_overprivileged_skill/  (2 files)
      … 2 files under this directory
    mcp_poisoned_tool/  (2 files)
      … 2 files under this directory
    mcp_registry/  (2 files)
      … 2 files under this directory
    mcp_underdeclared_skill/  (2 files)
      … 2 files under this directory
    oms/  (1 files)
      … 1 files under this directory
    pe3_bare_keyring/  (2 files)
      … 2 files under this directory
    safe_skill/  (1 files)
      … 1 files under this directory
    sdi/  (10 files)
      … 10 files under this directory
    sqp/  (16 files)
      … 16 files under this directory
    ssd/  (5 files)
      … 5 files under this directory
    tp4_markdown_fenced_code/  (1 files)
      … 1 files under this directory
  integration/  (10 files)
    __init__.py
    conftest.py
    test_agent_cli_live.py
    test_graph.py
    test_graph_scanner.py
    test_linked_zip_coverage.py
    test_meta_analyzer_use_llm.py
    test_opaque_reference_reporting.py
    test_ransomware_rule.py
    test_stream_invoke_parity.py
  nodes/  (133 files)
    analyzers/  (122 files)
      … 122 files under this directory
    __init__.py
    test_analysis_completeness.py
    test_as3_source_identity.py
    test_build_context.py
    test_deduplicate.py
    test_explicit_exclusions.py
    test_fragment_terminal_ledger.py
    test_inspection_notices.py
    test_json_capacity_scan.py
    test_json_capacity_upgrade.py
    test_passive_documentation_images.py
  provider/  (1 files)
    __init__.py
  unit/  (2 files)
    __init__.py
    test_wheel_contents.py
  __init__.py
  conftest.py
.dockerignore
.env.example
.gitignore
.pre-commit-config.yaml
.skillspector-baseline.example.yaml
CHANGELOG.md
CONTRIBUTING.md
Dockerfile
LICENSE
Makefile
README.md
SECURITY.md
THIRD_PARTY_NOTICES.md
langgraph.json
model_registry.yaml
package.json
pyproject.toml
```

## Entry points

- [src/skillspector/cli.py:518](https://github.com/NVIDIA/SkillSpector/blob/c81615007d40e86051a302a3cf897f8a05264928/src/skillspector/cli.py#L518)
- [src/skillspector/cli_entry.py](https://github.com/NVIDIA/SkillSpector/blob/c81615007d40e86051a302a3cf897f8a05264928/src/skillspector/cli_entry.py)
- [src/skillspector/dependency_downloader.py:34](https://github.com/NVIDIA/SkillSpector/blob/c81615007d40e86051a302a3cf897f8a05264928/src/skillspector/dependency_downloader.py#L34)
- [src/skillspector/dependency_worker.py:368](https://github.com/NVIDIA/SkillSpector/blob/c81615007d40e86051a302a3cf897f8a05264928/src/skillspector/dependency_worker.py#L368)
- [contrib/batch_scan/batch_scan.py:558](https://github.com/NVIDIA/SkillSpector/blob/c81615007d40e86051a302a3cf897f8a05264928/contrib/batch_scan/batch_scan.py#L558)
- [scripts/compare_scan_accuracy.py:1874](https://github.com/NVIDIA/SkillSpector/blob/c81615007d40e86051a302a3cf897f8a05264928/scripts/compare_scan_accuracy.py#L1874)
- [scripts/generate_unicode_confusables.py:75](https://github.com/NVIDIA/SkillSpector/blob/c81615007d40e86051a302a3cf897f8a05264928/scripts/generate_unicode_confusables.py#L75)
- [scripts/release/public/create_github_release.py:269](https://github.com/NVIDIA/SkillSpector/blob/c81615007d40e86051a302a3cf897f8a05264928/scripts/release/public/create_github_release.py#L269)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| contrib package | library | Observed | Groups 8 file(s) under contrib package (observed from repository paths and static analysis). Observed top-level classes: ApiKey, ApiKeyPool, GapFillAnalyzer, GapFillError, GapFillFinding, GapFillResult. Observed top-lev… |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AnalyzerFinding, AnalyzerPlugin, Finding, Location, Severity. Observed top-level functions: _new_findin… |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level classes: FormatChoice, InspectionError, TransportCho… |
| extensions package | library | Observed | Groups 1 file(s) under extensions package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: OsvQueryBudget, OsvQueryLimitation, QueryBatchResults, VulnResult, _OsvLimitReachedError. Ob… |
| skillspector package | library | Observed | Groups 140 file(s) under skillspector package (observed from repository paths and static analysis). Observed top-level classes: AgentCLICapable, AgentCLIChatModel, AgentCLIError, AgentCLIProviderBase, AnalysisCompletene… |
| Tests | test | Observed | Groups 220 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH (path not a literal), PATCH (path not a literal), PATCH (path not a literal), PATCH (path not a literal), PATCH… |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `.github/workflows/update-pr-branches.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.skillspector-baseline.example.yaml` (config)
- `Dockerfile` (container)
- `contrib/batch_scan/.env.example` (config)
- `langgraph.json` (config)
- `model_registry.yaml` (config)
- `package.json` (manifest)
- `pyproject.toml` (manifest)
- `src/skillspector/providers/anthropic/model_registry.yaml` (config)
- `src/skillspector/providers/anthropic_proxy/model_registry.yaml` (config)
- `src/skillspector/providers/azure_openai/model_registry.yaml` (config)
- `src/skillspector/providers/bedrock/model_registry.yaml` (config)
- `src/skillspector/providers/gemini/model_registry.yaml` (config)
- `src/skillspector/providers/minimax/model_registry.yaml` (config)
- `src/skillspector/providers/nv_build/model_registry.yaml` (config)
- `src/skillspector/providers/ollama/model_registry.yaml` (config)
- `src/skillspector/providers/openai/model_registry.yaml` (config)
- `src/skillspector/providers/openai_compatible/model_registry.yaml` (config)

## Top-level layout

- `tests` — 205 analysed file(s)
- `src` — 161 analysed file(s)
- `docs` — 42 analysed file(s)
- `contrib` — 34 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 4 analysed file(s)
- `.opencode` — 3 analysed file(s)
- `scripts` — 3 analysed file(s)
- `extensions` — 1 analysed file(s)
- `skills` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c81615007d40e86051a302a3cf897f8a05264928` is the revision these paths and observations refer to.
