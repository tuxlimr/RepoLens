# Project structure: tirth8205/code-review-graph

**Analysed commit:** `bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208`

**Commit reference:** [bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208](https://github.com/tirth8205/code-review-graph/commit/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208)

**Tree at this commit:** [tirth8205/code-review-graph@bbdda4b9e4b4](https://github.com/tirth8205/code-review-graph/tree/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tirth8205/code-review-graph |
| Description | Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools read only what matters, with benchmarked context reductions on reviews and large-repo workflows. |
| Stars | 32766 |
| Forks | 2979 |
| Licence | MIT |
| Language | Python |
| Default branch | staging |
| Analysed commit | `bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208` |
| Retrieved at | 2026-11-14T19:07:03.502069+00:00 |
| Files in this snapshot | 552 |

## Directory tree

```text
.beads/  (9 files)
  hooks/  (5 files)
    post-checkout
    post-merge
    pre-commit
    pre-push
    prepare-commit-msg
  .gitignore
  README.md
  config.yaml
  metadata.json
.github/  (15 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    platform_request.yml
  workflows/  (7 files)
    ci.yml
    eval.yml
    pr-review-comment.yml
    pr-review.yml
    promote.yml
    promotion-gate.yml
    publish.yml
  PULL_REQUEST_TEMPLATE.md
  copilot-instructions.md
  dependabot.yml
  requirements-minimum.txt
code-review-graph-vscode/  (30 files)
  media/  (4 files)
    icons/  (1 files)
      … 1 files under this directory
    walkthrough/  (3 files)
      … 3 files under this directory
  src/  (17 files)
    backend/  (3 files)
      … 3 files under this directory
    features/  (6 files)
      … 6 files under this directory
    onboarding/  (2 files)
      … 2 files under this directory
    views/  (4 files)
      … 4 files under this directory
    webview/  (1 files)
      … 1 files under this directory
    extension.ts
  test/  (1 files)
    sqlite.test.ts
  .gitignore
  .vscodeignore
  CHANGELOG.md
  LICENSE
  README.md
  esbuild.mjs
  package.json
  tsconfig.json
code_review_graph/  (101 files)
  assets/  (3 files)
    code-review-graph/  (3 files)
      … 3 files under this directory
  docs/  (1 files)
    LLM-OPTIMIZED-REFERENCE.md
  eval/  (20 files)
    benchmarks/  (9 files)
      … 9 files under this directory
    configs/  (6 files)
      … 6 files under this directory
    __init__.py
    reporter.py
    runner.py
    scorer.py
    token_benchmark.py
  tools/  (12 files)
    __init__.py
    _common.py
    analysis_tools.py
    build.py
    community_tools.py
    context.py
    docs.py
    flows_tools.py
    query.py
    refactor_tools.py
    registry_tools.py
    review.py
  __init__.py
  __main__.py
  _legacy_instructions.py
  analysis.py
  aop_resolver.py
  build_state.py
  change_details.py
  changes.py
  cli.py
  codex_skill.py
  communities.py
  config_keys.py
  constants.py
  context_history.py
  context_savings.py
  csharp_resolver.py
  custom_languages.py
  daemon.py
  daemon_cli.py
  doctor.py
  dsh.py
  embeddings.py
  enrich.py
  errors.py
  … 41 more files
diagrams/  (2 files)
  context-savings-demo.tape
  generate_diagrams.py
docs/  (14 files)
  COMMANDS.md
  CUSTOM_LANGUAGES.md
  FAQ.md
  FEATURES.md
  GITHUB_ACTION.md
  INDEX.md
  LEGAL.md
  RELEASING.md
  REPRODUCING.md
  ROADMAP.md
  TROUBLESHOOTING.md
  USAGE.md
  architecture.md
  schema.md
evaluate/  (24 files)
  results/  (24 files)
    code-review-graph_agent_baseline_2026-09-22.csv
    code-review-graph_impact_accuracy_2026-08-02.csv
    code-review-graph_multi_hop_retrieval_2026-05-25.csv
    code-review-graph_token_efficiency_2026-05-25.csv
    express_agent_baseline_2026-09-22.csv
    express_impact_accuracy_2026-08-02.csv
    express_multi_hop_retrieval_2026-05-25.csv
    express_token_efficiency_2026-05-25.csv
    fastapi_agent_baseline_2026-09-22.csv
    fastapi_impact_accuracy_2026-08-02.csv
    fastapi_multi_hop_retrieval_2026-05-25.csv
    fastapi_token_efficiency_2026-05-25.csv
    flask_agent_baseline_2026-09-22.csv
    flask_impact_accuracy_2026-08-02.csv
    flask_multi_hop_retrieval_2026-05-25.csv
    flask_token_efficiency_2026-05-25.csv
    gin_agent_baseline_2026-09-22.csv
    gin_impact_accuracy_2026-08-02.csv
    gin_multi_hop_retrieval_2026-05-25.csv
    gin_token_efficiency_2026-05-25.csv
    httpx_agent_baseline_2026-09-22.csv
    httpx_impact_accuracy_2026-08-02.csv
    httpx_multi_hop_retrieval_2026-05-25.csv
    httpx_token_efficiency_2026-05-25.csv
hooks/  (2 files)
  hooks.json
  session-start.sh
scripts/  (7 files)
  audit_python_imports.py
  diagnose_pypi_connectivity.py
  generate_documentary_skills.py
  print_minimum_dependencies.py
  promotion_gate.py
  render_pr_comment.py
  smoke_google_embeddings.py
skills/  (7 files)
  build-graph/  (1 files)
    SKILL.md
  debug-issue/  (1 files)
    SKILL.md
  explore-codebase/  (1 files)
    SKILL.md
  refactor-safely/  (1 files)
    SKILL.md
  review-changes/  (1 files)
    SKILL.md
  review-delta/  (1 files)
    SKILL.md
  review-pr/  (1 files)
    SKILL.md
tests/  (322 files)
  fixtures/  (83 files)
    __tests__/  (1 files)
      … 1 files under this directory
    cpp_qt_headers/  (4 files)
      … 4 files under this directory
    graphml_xsd/  (6 files)
      … 6 files under this directory
    playbooks/  (1 files)
      … 1 files under this directory
    roles/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    tasks/  (1 files)
      … 1 files under this directory
    KafkaPatterns.java
    MarkdownMsg.tsx
    Sample.cs
    SampleJava.java
    SpringDI.java
    TemporalWorkflow.java
    alias_importer.ts
    caller_example.py
    detect_changes_sample.json
    multi_call_example.py
    sample.R
    sample.c
    sample.cpp
    sample.dart
    sample.ex
    sample.gd
    sample.hh
    sample.jl
    sample.kt
    sample.liquid
    sample.lua
    sample.luau
    sample.m
    sample.nix
    … 44 more files
  __init__.py
  conftest.py
  corpus_baselines.json
  determinism_build_runner.py
  determinism_dump.py
  import_audit.py
  mcp_client_compat.py
  real_repo_corpus.py
  test_action_e2e.py
  test_action_render.py
  test_affected_flows_limits.py
  test_agent_transparency.py
  test_ansible_parser.py
  test_aop_resolution_edge_cases.py
  test_aop_resolver.py
  test_build_tool_errors.py
  test_call_site_provenance.py
  test_callback_context_preservation.py
  test_change_details.py
  test_changes.py
  test_changes_path_normalization.py
  test_churn_runtime.py
  test_cjs_and_kts_extensions.py
  test_cli.py
  … 215 more files
.gitattributes
.gitignore
.mcp.json
AGENTS.md
CHANGELOG.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
GEMINI.md
LICENSE
README.hi-IN.md
README.ja-JP.md
README.ko-KR.md
README.md
README.zh-CN.md
SECURITY.md
action.yml
pyproject.toml
```

## Entry points

- [code_review_graph/assets/code-review-graph/scripts/crg_readonly.py:280](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/code_review_graph/assets/code-review-graph/scripts/crg_readonly.py#L280)
- [code_review_graph/cli.py](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/code_review_graph/cli.py)
- [code_review_graph/daemon_cli.py](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/code_review_graph/daemon_cli.py)
- [code_review_graph/main.py:1760](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/code_review_graph/main.py#L1760)
- [diagrams/generate_diagrams.py:769](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/diagrams/generate_diagrams.py#L769)
- [scripts/audit_python_imports.py:1134](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/scripts/audit_python_imports.py#L1134)
- [scripts/diagnose_pypi_connectivity.py:62](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/scripts/diagnose_pypi_connectivity.py#L62)
- [scripts/generate_documentary_skills.py:60](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/scripts/generate_documentary_skills.py#L60)
- [scripts/print_minimum_dependencies.py:23](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/scripts/print_minimum_dependencies.py#L23)
- [scripts/promotion_gate.py:721](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/scripts/promotion_gate.py#L721)
- [scripts/render_pr_comment.py:1103](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/scripts/render_pr_comment.py#L1103)
- [scripts/smoke_google_embeddings.py:23](https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/scripts/smoke_google_embeddings.py#L23)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| code_review_graph package | library | Observed | Groups 87 file(s) under code_review_graph package (observed from repository paths and static analysis). Observed top-level classes: CallInfo, ChangeDiscoveryError, CodeReviewGraphError, ConfigWatcher, ConnectionPool, Co… |
| code-review-graph-vscode package | library | Observed | Groups 14 file(s) under code-review-graph-vscode package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Check, ReportError, Totals, _CallSite, _EmbeddingRefreshKwargs, _FileFacts. Observed top-… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 1 file(s) under hooks package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 323 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH os.kill, PATCH code_review_graph.daemon.pid_alive, PATCH os.kill, PATCH os.kill, PATCH os.kill. Observed top-le… |

## Important files

- `.beads/config.yaml` (config)
- `.beads/metadata.json` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/platform_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/requirements-minimum.txt` (manifest)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/eval.yml` (ci)
- `.github/workflows/pr-review-comment.yml` (ci)
- `.github/workflows/pr-review.yml` (ci)
- `.github/workflows/promote.yml` (ci)
- `.github/workflows/promotion-gate.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.mcp.json` (config)
- `Dockerfile` (container)
- `action.yml` (config)
- `code-review-graph-vscode/package.json` (manifest)
- `code-review-graph-vscode/tsconfig.json` (config)
- `code_review_graph/assets/code-review-graph/agents/openai.yaml` (config)
- `code_review_graph/eval/configs/code-review-graph.yaml` (config)
- `code_review_graph/eval/configs/express.yaml` (config)
- `code_review_graph/eval/configs/fastapi.yaml` (config)
- `code_review_graph/eval/configs/flask.yaml` (config)
- `code_review_graph/eval/configs/gin.yaml` (config)
- `code_review_graph/eval/configs/httpx.yaml` (config)
- `hooks/hooks.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 322 analysed file(s)
- `code_review_graph` — 101 analysed file(s)
- `code-review-graph-vscode` — 30 analysed file(s)
- `evaluate` — 24 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 15 analysed file(s)
- `docs` — 14 analysed file(s)
- `.beads` — 9 analysed file(s)
- `scripts` — 7 analysed file(s)
- `skills` — 7 analysed file(s)
- `diagrams` — 2 analysed file(s)
- `hooks` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208` is the revision these paths and observations refer to.
