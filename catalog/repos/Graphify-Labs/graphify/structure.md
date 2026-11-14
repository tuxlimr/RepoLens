# Project structure: Graphify-Labs/graphify

**Analysed commit:** `52cb28218eea0c68d80a9f4b2ae102d2fa63e267`

**Commit reference:** [52cb28218eea0c68d80a9f4b2ae102d2fa63e267](https://github.com/Graphify-Labs/graphify/commit/52cb28218eea0c68d80a9f4b2ae102d2fa63e267)

**Tree at this commit:** [Graphify-Labs/graphify@52cb28218eea](https://github.com/Graphify-Labs/graphify/tree/52cb28218eea0c68d80a9f4b2ae102d2fa63e267)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Graphify-Labs/graphify |
| Description | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store. |
| Stars | 147656 |
| Forks | 14157 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | v8 |
| Analysed commit | `52cb28218eea0c68d80a9f4b2ae102d2fa63e267` |
| Retrieved at | 2026-11-14T19:06:05.234495+00:00 |
| Files in this snapshot | 600 |

## Directory tree

```text
.github/  (13 files)
  DISCUSSION_TEMPLATE/  (1 files)
    q-a.yml
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (5 files)
    ci.yml
    pr-management.yml
    publish.yml
    release-graph.yml
    welcome.yml
  CODEOWNERS
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  TEAM_MEMBERS
docs/  (39 files)
  superpowers/  (2 files)
    plans/  (1 files)
      … 1 files under this directory
    specs/  (1 files)
      … 1 files under this directory
  translations/  (31 files)
    README.ar-SA.md
    README.cs-CZ.md
    README.da-DK.md
    README.de-DE.md
    README.el-GR.md
    README.es-ES.md
    README.fa-IR.md
    README.fi-FI.md
    README.fil-PH.md
    README.fr-FR.md
    README.he-IL.md
    README.hi-IN.md
    README.hu-HU.md
    README.id-ID.md
    README.it-IT.md
    README.ja-JP.md
    README.ko-KR.md
    README.nl-NL.md
    README.no-NO.md
    README.pl-PL.md
    README.pt-BR.md
    README.ro-RO.md
    README.ru-RU.md
    README.sv-SE.md
    … 7 more files
  demo-path.svg
  docker-mcp-sqlite.md
  how-it-works.md
  logo-icon.svg
  logo-text.svg
  node-summaries-rfc.md
graphify/  (232 files)
  always_on/  (6 files)
    agents-md.md
    antigravity-rules.md
    claude-md.md
    gemini-md.md
    kiro-steering.md
    vscode-instructions.md
  exporters/  (4 files)
    __init__.py
    base.py
    graphdb.py
    html.py
  extractors/  (36 files)
    MIGRATION.md
    __init__.py
    apex.py
    base.py
    bash.py
    blade.py
    cobol.py
    commonlisp.py
    csharp.py
    dart.py
    dm.py
    elixir.py
    erlang.py
    fortran.py
    go.py
    json_config.py
    julia.py
    markdown.py
    models.py
    objc.py
    ocaml.py
    pascal.py
    pascal_forms.py
    powershell.py
    … 12 more files
  pi/  (2 files)
    index.ts
    package.json
  skills/  (112 files)
    agents/  (8 files)
      … 8 files under this directory
    amp/  (8 files)
      … 8 files under this directory
    claude/  (8 files)
      … 8 files under this directory
    claw/  (8 files)
      … 8 files under this directory
    codex/  (8 files)
      … 8 files under this directory
    copilot/  (8 files)
      … 8 files under this directory
    droid/  (8 files)
      … 8 files under this directory
    kilo/  (8 files)
      … 8 files under this directory
    kiro/  (8 files)
      … 8 files under this directory
    opencode/  (8 files)
      … 8 files under this directory
    pi/  (8 files)
      … 8 files under this directory
    trae/  (8 files)
      … 8 files under this directory
    vscode/  (8 files)
      … 8 files under this directory
    windows/  (8 files)
      … 8 files under this directory
  __init__.py
  __main__.py
  _minhash.py
  affected.py
  analyze.py
  benchmark.py
  build.py
  cache.py
  callflow_html.py
  cargo_introspect.py
  cluster.py
  command-kilo.md
  cpp_resolution.py
  cross_repo_calls.py
  cross_repo_types.py
  csharp_dispatch.py
  dedup.py
  detect.py
  diagnostics.py
  export.py
  file_slice.py
  global_graph.py
  go_dispatch.py
  google_workspace.py
  … 48 more files
scripts/  (1 files)
  gen_demo_path.py
tests/  (292 files)
  fixtures/  (124 files)
    4978/  (1 files)
      … 1 files under this directory
    cpp_logger/  (4 files)
      … 4 files under this directory
    cpp_paired/  (3 files)
      … 3 files under this directory
    cpp_samedir/  (3 files)
      … 3 files under this directory
    crate_a/  (2 files)
      … 2 files under this directory
    crate_b/  (2 files)
      … 2 files under this directory
    graphify-out/  (5 files)
      … 5 files under this directory
    new_languages/  (5 files)
      … 5 files under this directory
    objc_mixed/  (4 files)
      … 4 files under this directory
    pascal_cross_file/  (3 files)
      … 3 files under this directory
    swift_cross_file/  (2 files)
      … 2 files under this directory
    xaml_viewmodel/  (11 files)
      … 11 files under this directory
    barrel_reexport.ts
    bindings.xaml
    cjs_require.js
    cookieHelpers.ts
    deploy_guide.md
    dynamic_import.ts
    extraction.json
    robot_keywords.resource
    sample.c
    sample.cls
    sample.cpp
    sample.cs
    sample.csproj
    sample.cu
    sample.dfm
    sample.dm
    sample.dmf
    sample.dmm
    sample.ex
    sample.f90
    sample.go
    sample.groovy
    sample.java
    sample.jl
    … 55 more files
  __init__.py
  bench_extract.py
  bench_query_scoring.py
  conftest.py
  csharp_extension_harness.py
  pi.test.ts
  test_4874_jvm_resolution.py
  test_4909_reference_binding_scale.py
  test_4978_reconcile_cost.py
  test_4992_ts_import_types.py
  test_5072_splittable_under_cap_retry.py
  test_affected_cli.py
  test_affected_defines.py
  test_affected_member_seed.py
  test_affected_overrides.py
  test_affected_path_file_node.py
  test_affected_seed_reference_forms.py
  test_agents_platform.py
  test_alias_folding.py
  test_analyze.py
  test_anthropic_custom_endpoint.py
  test_antigravity_install.py
  test_apm_fallback_version.py
  test_architecture_doc.py
  … 144 more files
tools/  (3 files)
  skillgen/  (2 files)
    fragments/  (1 files)
      … 1 files under this directory
    __init__.py
  __init__.py
.dockerignore
.gitattributes
.gitignore
.pre-commit-config.yaml
AGENTS.md
ARCHITECTURE.md
BENCHMARKS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
GEMINI.md
LICENSE
LICENSE-MIT
NOTICE
README.md
RELEASING.md
SECURITY.md
SUPPORT.md
gemini-extension.json
pyproject.toml
```

## Entry points

- [graphify/__main__.py](https://github.com/Graphify-Labs/graphify/blob/52cb28218eea0c68d80a9f4b2ae102d2fa63e267/graphify/__main__.py)
- [graphify/callflow_html.py:2050](https://github.com/Graphify-Labs/graphify/blob/52cb28218eea0c68d80a9f4b2ae102d2fa63e267/graphify/callflow_html.py#L2050)
- [graphify/ingest.py:396](https://github.com/Graphify-Labs/graphify/blob/52cb28218eea0c68d80a9f4b2ae102d2fa63e267/graphify/ingest.py#L396)
- [graphify/serve.py](https://github.com/Graphify-Labs/graphify/blob/52cb28218eea0c68d80a9f4b2ae102d2fa63e267/graphify/serve.py)
- [graphify/watch.py:3844](https://github.com/Graphify-Labs/graphify/blob/52cb28218eea0c68d80a9f4b2ae102d2fa63e267/graphify/watch.py#L3844)
- [graphify/pi/index.ts](https://github.com/Graphify-Labs/graphify/blob/52cb28218eea0c68d80a9f4b2ae102d2fa63e267/graphify/pi/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: LanguageConfig, _NamespaceExportFact, _StarExportFact, _SymbolAliasFact, _SymbolDeclarationFact, _Symbo… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CallflowOptions, ToolError, _ApiKeyMiddleware, _GraphContextCache, _MCPASGIApp, _QueryScor… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| graphify package | library | Observed | Groups 89 file(s) under graphify package (observed from repository paths and static analysis). Observed top-level classes: AffectedHit, CapabilityCheck, CppTypeLookup, CsharpNameResolver, DeclIdRegistry, FileSlice. Obse… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: e, kt, line_len, op0, reveal. |
| Tests | test | Observed | Groups 292 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Analyzer, Anchors, ExtDecl, Fixture, Probe, Runbook. Observed top-level functions: _added_calls, _affected… |
| tools package | library | Observed | Groups 2 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/DISCUSSION_TEMPLATE/q-a.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/pr-management.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/release-graph.yml` (ci)
- `.github/workflows/welcome.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `gemini-extension.json` (config)
- `graphify/pi/package.json` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 292 analysed file(s)
- `graphify` — 232 analysed file(s)
- `docs` — 39 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 13 analysed file(s)
- `tools` — 3 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `52cb28218eea0c68d80a9f4b2ae102d2fa63e267` is the revision these paths and observations refer to.
