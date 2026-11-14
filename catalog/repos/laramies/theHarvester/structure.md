# Project structure: laramies/theHarvester

**Analysed commit:** `b9b00561a66b4a2c829c606403a4765f3fff1ae9`

**Commit reference:** [b9b00561a66b4a2c829c606403a4765f3fff1ae9](https://github.com/laramies/theHarvester/commit/b9b00561a66b4a2c829c606403a4765f3fff1ae9)

**Tree at this commit:** [laramies/theHarvester@b9b00561a66b](https://github.com/laramies/theHarvester/tree/b9b00561a66b4a2c829c606403a4765f3fff1ae9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | laramies/theHarvester |
| Description | E-mails, subdomains and names Harvester - OSINT  |
| Stars | 18324 |
| Forks | 2737 |
| Licence | GPL-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `b9b00561a66b4a2c829c606403a4765f3fff1ae9` |
| Retrieved at | 2026-11-14T19:08:25.397484+00:00 |
| Files in this snapshot | 330 |

## Directory tree

```text
.github/  (15 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (9 files)
    codeql-analysis.yml
    dependency-review.yml
    docker-build-push.yml
    dockerci.yml
    harvestview-container.yml
    harvestview-e2e.yml
    provider-smoke.yml
    scorecards.yml
    theHarvester.yml
  FUNDING.yml
  dependabot.yml
  zizmor.yml
README/  (1 files)
  LICENSES
bin/  (2 files)
  harvestview
  theHarvester
docs/  (36 files)
  adr/  (8 files)
    0003-run-worker-lifecycle.md
    0004-keep-network-evidence-typed-and-external.md
    0005-persist-asn-organization-attribution-as-sourced-evidence.md
    0006-schedule-finite-runs-through-a-private-control-plane.md
    0007-keep-operator-hostname-as-exact-scope.md
    0008-fail-closed-when-explicit-proxy-mode-is-unavailable.md
    0009-scope-proxy-mode-to-http-transport.md
    0010-own-api-background-state-in-the-app-lifespan.md
  agents/  (3 files)
    domain.md
    issue-tracker.md
    triage-labels.md
  images/  (6 files)
    harvestview-architecture.html
    harvestview-architecture.svg
    run-evidence-architecture.html
    run-evidence-architecture.svg
    vhost-classifier.svg
    vhost-sweep-overview.svg
  wiki/  (16 files)
    Configuration-and-API-Keys.md
    Contributing-and-Security.md
    Home.md
    How-to-add-a-new-module.md
    Installation.md
    Moving-from-4.11-to-5.0.md
    Operator-Workflows.md
    Quick-Start.md
    Responsible-Use-and-Scope.md
    Rest-API.md
    Results-and-Local-Data.md
    Roadmap.md
    Troubleshooting.md
    Virtual-Host-Discovery.md
    _Footer.md
    _Sidebar.md
  architecture.md
  coding-standards-research.md
  context-glossary-research.md
tests/  (121 files)
  discovery/  (74 files)
    __init__.py
    test_api_endpoints.py
    test_apisguru.py
    test_arquivo.py
    test_baidusearch.py
    test_bevigil.py
    test_brave.py
    test_bufferoverun.py
    test_builtwith.py
    test_censys.py
    test_certspotter.py
    test_commoncrawl.py
    test_criminalip.py
    test_crtname.py
    test_crtsh.py
    test_darkeye.py
    test_dnsdb.py
    test_dnsdumpster.py
    test_duckduckgo.py
    test_dymosearch.py
    test_fofa.py
    test_fullhuntsearch.py
    test_githubcode.py
    test_githubcode_additions.py
    … 50 more files
  e2e/  (2 files)
    conftest.py
    test_harvestview.py
  fixtures/  (1 files)
    takeover_can_i_take_over_xyz_5bd4e128.fixture
  lib/  (21 files)
    test_active_evidence.py
    test_api_v1.py
    test_completed_persistence.py
    test_completed_result.py
    test_configuration_contract.py
    test_core.py
    test_dns_consensus.py
    test_enumeration.py
    test_harvestview_ui.py
    test_hostchecker.py
    test_hostnames.py
    test_output.py
    test_recursive_dns.py
    test_routeviews.py
    test_run_backend.py
    test_runtime_services.py
    test_schedules.py
    test_source_catalog.py
    test_source_runner.py
    test_target_identity.py
    test_virtual_host.py
  __init__.py
  conftest.py
  runtime_helpers.py
  screenshot_helpers.py
  test_agent_guidance.py
  test_all_source_orchestration.py
  test_bootstrap.py
  test_docker.py
  test_harness.py
  test_harvestview_launcher.py
  test_harvestview_log_level.py
  test_logging.py
  test_main.py
  test_myparser.py
  test_no_hosts.py
  test_provider_contract_coverage.py
  test_readme.py
  test_release_artifacts.py
  test_runtime_dependencies.py
  test_saved_run_report_cli.py
  test_screenshot.py
  test_security.py
  test_workflow_contract.py
theHarvester/  (137 files)
  data/  (4 files)
    wordlists/  (2 files)
      … 2 files under this directory
    api-keys.yaml
    proxies.yaml
  discovery/  (72 files)
    __init__.py
    api_endpoints.py
    apisguru.py
    arquivo.py
    baidusearch.py
    bevigil.py
    bravesearch.py
    bufferoverun.py
    builtwith.py
    censysearch.py
    certspottersearch.py
    commoncrawl.py
    constants.py
    criminalip.py
    crtname.py
    crtsh.py
    darkeye.py
    dnsdb.py
    dnssearch.py
    duckduckgosearch.py
    dymosearch.py
    fofa.py
    fullhuntsearch.py
    githubcode.py
    … 48 more files
  lib/  (51 files)
    api/  (23 files)
      … 23 files under this directory
    __init__.py
    active_evidence.py
    asn_attribution.py
    cancellation.py
    completed_result.py
    configuration.py
    core.py
    database.py
    dns_consensus.py
    enumeration.py
    evidence_types.py
    hostchecker.py
    hostname_comparison.py
    hostnames.py
    network_evidence.py
    output.py
    recursive_dns.py
    resolver_selection.py
    result_values.py
    routeviews.py
    shodan_evidence.py
    source_catalog.py
    source_execution.py
    source_runner.py
    … 4 more files
  parsers/  (3 files)
    __init__.py
    intelxparser.py
    myparser.py
  screenshot/  (2 files)
    __init__.py
    screenshot.py
  __init__.py
  __main__.py
  harvestview.py
  saved_run_report.py
  theHarvester.py
.dockerignore
.git-blame-ignore-revs
.gitattributes
.gitignore
.python-version
AGENTS.md
CHANGELOG.md
CODING_STANDARDS.md
CONTRIBUTING.md
DESIGN.md
Dockerfile
GLOSSARY.md
LICENSE
PRODUCT.md
README.md
SECURITY.md
docker-compose.yml
pyproject.toml
```

## Entry points

- [theHarvester/harvestview.py](https://github.com/laramies/theHarvester/blob/b9b00561a66b4a2c829c606403a4765f3fff1ae9/theHarvester/harvestview.py)
- [theHarvester/lib/api/api.py:50](https://github.com/laramies/theHarvester/blob/b9b00561a66b4a2c829c606403a4765f3fff1ae9/theHarvester/lib/api/api.py#L50)
- [theHarvester/lib/api/run_worker.py:508](https://github.com/laramies/theHarvester/blob/b9b00561a66b4a2c829c606403a4765f3fff1ae9/theHarvester/lib/api/run_worker.py#L508)
- [theHarvester/saved_run_report.py](https://github.com/laramies/theHarvester/blob/b9b00561a66b4a2c829c606403a4765f3fff1ae9/theHarvester/saved_run_report.py)
- [theHarvester/theHarvester.py](https://github.com/laramies/theHarvester/blob/b9b00561a66b4a2c829c606403a4765f3fff1ae9/theHarvester/theHarvester.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 16 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /, GET /schedules, GET /runs, GET /sources, POST /runs. Observed top-level classes: ActionResponse, ApiRuntime… |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DuplicateRunError, ResultStore, ResultStoreError, ResultStoreUnavailableError, RunLifecycleStore, _Arti… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: RunWorker, RunWorkerService, _WorkerSessi… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 121 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BlockingResolver, BrowserFailures, BrowserState, CnameHeavyResolver, ConfigurationEnvironment, DummyConten… |
| theHarvester package | library | Observed | Groups 107 file(s) under theharvester package (observed from repository paths and static analysis). Observed top-level classes: ActionExecution, ActionObservation, ActiveEvidence, ActivityClass, Addressability, AioDNSRe… |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/dependency-review.yml` (ci)
- `.github/workflows/docker-build-push.yml` (ci)
- `.github/workflows/dockerci.yml` (ci)
- `.github/workflows/harvestview-container.yml` (ci)
- `.github/workflows/harvestview-e2e.yml` (ci)
- `.github/workflows/provider-smoke.yml` (ci)
- `.github/workflows/scorecards.yml` (ci)
- `.github/workflows/theHarvester.yml` (ci)
- `.github/zizmor.yml` (config)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `pyproject.toml` (manifest)
- `theHarvester/data/api-keys.yaml` (config)
- `theHarvester/data/proxies.yaml` (config)

## Top-level layout

- `theHarvester` — 137 analysed file(s)
- `tests` — 121 analysed file(s)
- `docs` — 36 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 15 analysed file(s)
- `bin` — 2 analysed file(s)
- `README` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b9b00561a66b4a2c829c606403a4765f3fff1ae9` is the revision these paths and observations refer to.
