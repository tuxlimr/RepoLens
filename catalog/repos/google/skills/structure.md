# Project structure: google/skills

**Analysed commit:** `e3c591afe426ea585e4c21799e5199d6d47cd1be`

**Commit reference:** [e3c591afe426ea585e4c21799e5199d6d47cd1be](https://github.com/google/skills/commit/e3c591afe426ea585e4c21799e5199d6d47cd1be)

**Tree at this commit:** [google/skills@e3c591afe426](https://github.com/google/skills/tree/e3c591afe426ea585e4c21799e5199d6d47cd1be)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google/skills |
| Description | Agent Skills for Google products and technologies |
| Stars | 24235 |
| Forks | 2014 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `e3c591afe426ea585e4c21799e5199d6d47cd1be` |
| Retrieved at | 2026-11-14T19:07:38.511136+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.claude-plugin/  (1 files)
  marketplace.json
.github/  (1 files)
  workflows/  (1 files)
    link-checker.yml
plugins/  (27 files)
  cloud/  (27 files)
    data-cloud/  (1 files)
      … 1 files under this directory
    google-cloud-developer/  (26 files)
      … 26 files under this directory
skills/  (762 files)
  ads/  (57 files)
    data-manager-api-audience-ingestion/  (3 files)
      … 3 files under this directory
    data-manager-api-event-ingestion/  (1 files)
      … 1 files under this directory
    data-manager-api-setup/  (7 files)
      … 7 files under this directory
    google-ads-api-account-diagnostics/  (1 files)
      … 1 files under this directory
    google-ads-api-mcp-setup/  (1 files)
      … 1 files under this directory
    google-ads-api-quickstart/  (8 files)
      … 8 files under this directory
    google-mobile-ads-android-migrate-to-next-gen/  (1 files)
      … 1 files under this directory
    google-mobile-ads-banner/  (4 files)
      … 4 files under this directory
    google-mobile-ads-get-started/  (4 files)
      … 4 files under this directory
    google-mobile-ads-interstitial/  (4 files)
      … 4 files under this directory
    google-mobile-ads-rewarded/  (4 files)
      … 4 files under this directory
    google-mobile-ads-validate/  (6 files)
      … 6 files under this directory
    ima-dai-sdk/  (6 files)
      … 6 files under this directory
    ima-sdk-client-side/  (7 files)
      … 7 files under this directory
  analytics/  (16 files)
    google-analytics-admin-api-basics/  (8 files)
      … 8 files under this directory
    google-analytics-data-api-basics/  (8 files)
      … 8 files under this directory
  cloud/  (689 files)
    agent-platform-access-audit/  (3 files)
      … 3 files under this directory
    agent-platform-alert-configuration/  (29 files)
      … 29 files under this directory
    agent-platform-architecture/  (9 files)
      … 9 files under this directory
    agent-platform-autorater-customization/  (12 files)
      … 12 files under this directory
    agent-platform-deploy/  (9 files)
      … 9 files under this directory
    agent-platform-endpoint-management/  (2 files)
      … 2 files under this directory
    agent-platform-eval-flywheel/  (14 files)
      … 14 files under this directory
    agent-platform-inference/  (10 files)
      … 10 files under this directory
    agent-platform-migrate-from-ai-studio/  (2 files)
      … 2 files under this directory
    agent-platform-model-registry/  (2 files)
      … 2 files under this directory
    agent-platform-prompt-management/  (3 files)
      … 3 files under this directory
    agent-platform-rag-engine-management/  (2 files)
      … 2 files under this directory
    agent-platform-skill-registry/  (9 files)
      … 9 files under this directory
    agent-platform-troubleshooting/  (8 files)
      … 8 files under this directory
    agent-platform-tuning/  (13 files)
      … 13 files under this directory
    agent-platform-tuning-management/  (2 files)
      … 2 files under this directory
    alloydb-basics/  (7 files)
      … 7 files under this directory
    api-gateway-backend-security-and-rate-limiting/  (7 files)
      … 7 files under this directory
    api-gateway-mcp-server/  (7 files)
      … 7 files under this directory
    api-gateway-openapi-spec-authoring/  (6 files)
      … 6 files under this directory
    api-gateway-troubleshooting/  (9 files)
      … 9 files under this directory
    apigee-agent-gateway-governance/  (26 files)
      … 26 files under this directory
    application-design-center-design-deploy/  (15 files)
      … 15 files under this directory
    application-integration-authoring/  (7 files)
      … 7 files under this directory
    application-integration-basics/  (7 files)
      … 7 files under this directory
    application-integration-troubleshooting/  (7 files)
      … 7 files under this directory
    assured-workloads-basics/  (7 files)
      … 7 files under this directory
    assuredworkloads-environment-assessor/  (5 files)
      … 5 files under this directory
    assuredworkloads-frameworks-author/  (4 files)
      … 4 files under this directory
    assuredworkloads-frameworks-navigator/  (10 files)
      … 10 files under this directory
    bigquery-ai-ml/  (25 files)
      … 25 files under this directory
    bigquery-basics/  (10 files)
      … 10 files under this directory
    bigquery-bigframes/  (4 files)
      … 4 files under this directory
    bigquery-migration-data-loader/  (3 files)
      … 3 files under this directory
    bigquery-migration-metadata-extractor/  (6 files)
      … 6 files under this directory
    bigquery-migration-sql-translator/  (34 files)
      … 34 files under this directory
    bigquery-migration-validator/  (10 files)
      … 10 files under this directory
    bigquery-observability/  (11 files)
      … 11 files under this directory
    bigquery-optimization/  (10 files)
      … 10 files under this directory
    bigquery-troubleshooting/  (8 files)
      … 8 files under this directory
    bigquery-udfs/  (6 files)
      … 6 files under this directory
    bigtable-basics/  (9 files)
      … 9 files under this directory
    cloud-armor-crs-rule-upgrader/  (7 files)
      … 7 files under this directory
    cloud-build-basics/  (5 files)
      … 5 files under this directory
    cloud-databases-onboarding/  (6 files)
      … 6 files under this directory
    cloud-logging-configuration-basics/  (2 files)
      … 2 files under this directory
    cloud-logging-cross-project-configuration/  (2 files)
      … 2 files under this directory
    cloud-logging-finops/  (25 files)
      … 25 files under this directory
    cloud-logging-query-generation/  (24 files)
      … 24 files under this directory
    cloud-monitoring-alert-configuration/  (41 files)
      … 41 files under this directory
    cloud-monitoring-chart-generation/  (11 files)
      … 11 files under this directory
    cloud-monitoring-list-time-series-request/  (3 files)
      … 3 files under this directory
    cloud-monitoring-metric-selection/  (2 files)
      … 2 files under this directory
    cloud-monitoring-notification-channels-configuration/  (10 files)
      … 10 files under this directory
    cloud-monitoring-promql-query/  (6 files)
      … 6 files under this directory
    cloud-network-insights/  (4 files)
      … 4 files under this directory
    cloud-operator/  (2 files)
      … 2 files under this directory
    cloud-operator-setup/  (2 files)
      … 2 files under this directory
    cloud-operator-share-context/  (2 files)
      … 2 files under this directory
    cloud-run-alert-configuration/  (5 files)
      … 5 files under this directory
    cloud-run-basics/  (9 files)
      … 9 files under this directory
    cloud-sql-basics/  (9 files)
      … 9 files under this directory
    cloud-trace-querying/  (90 files)
      … 90 files under this directory
    compute-future-reservations/  (2 files)
      … 2 files under this directory
    compute-on-demand-reservations/  (2 files)
      … 2 files under this directory
    compute-spot-capacity-advice/  (2 files)
      … 2 files under this directory
    compute-vm-creation/  (3 files)
      … 3 files under this directory
    datalineage-bigquery-asset-impact-analysis/  (3 files)
      … 3 files under this directory
    datalineage-summary/  (3 files)
      … 3 files under this directory
    dbt-sf-to-bq-translator/  (5 files)
      … 5 files under this directory
    detection-engineering-coverage-evaluation/  (2 files)
      … 2 files under this directory
    developer-device-platform-basics/  (11 files)
      … 11 files under this directory
.gitignore
.gitmodules
.lycheeignore
CONTRIBUTING.md
LICENSE
README.md
index.json
lychee.toml
```

## Entry points

- [skills/cloud/cloud-trace-querying/scripts/fetch_entire_trace/src/main.py:62](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/cloud-trace-querying/scripts/fetch_entire_trace/src/main.py#L62)
- [skills/cloud/cloud-trace-querying/scripts/fetch_related_logs/src/main.py:84](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/cloud-trace-querying/scripts/fetch_related_logs/src/main.py#L84)
- [skills/cloud/cloud-trace-querying/scripts/fetch_trace_span/src/main.py:88](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/cloud-trace-querying/scripts/fetch_trace_span/src/main.py#L88)
- [skills/cloud/cloud-trace-querying/scripts/generate_links/src/main.py:53](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/cloud-trace-querying/scripts/generate_links/src/main.py#L53)
- [skills/cloud/cloud-trace-querying/scripts/get_trace_project/src/main.py:19](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/cloud-trace-querying/scripts/get_trace_project/src/main.py#L19)
- [skills/cloud/cloud-trace-querying/scripts/run_python_with_deps/src/cleanup_env.py:67](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/cloud-trace-querying/scripts/run_python_with_deps/src/cleanup_env.py#L67)
- [skills/cloud/cloud-trace-querying/scripts/run_python_with_deps/src/manage_venv.py:52](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/cloud-trace-querying/scripts/run_python_with_deps/src/manage_venv.py#L52)
- [skills/cloud/cloud-trace-querying/scripts/search_traces/src/main.py:75](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/cloud-trace-querying/scripts/search_traces/src/main.py#L75)
- [skills/cloud/agent-platform-alert-configuration/scripts/analyze_traffic.py:404](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/agent-platform-alert-configuration/scripts/analyze_traffic.py#L404)
- [skills/cloud/agent-platform-alert-configuration/scripts/analyze_traffic_test.py:227](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/agent-platform-alert-configuration/scripts/analyze_traffic_test.py#L227)
- [skills/cloud/agent-platform-alert-configuration/scripts/check_telemetry.py:181](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/agent-platform-alert-configuration/scripts/check_telemetry.py#L181)
- [skills/cloud/agent-platform-alert-configuration/scripts/check_telemetry_test.py:153](https://github.com/google/skills/blob/e3c591afe426ea585e4c21799e5199d6d47cd1be/skills/cloud/agent-platform-alert-configuration/scripts/check_telemetry_test.py#L153)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 58 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 78 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AdbForwarder, CatalogMatchResult, CredentialsMissingError, DBResourcesStore, GcloudError,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 63 file(s) under skills package (observed from repository paths and static analysis). Observed top-level classes: Action, Aggregation, BillingResult, ChartOptions, Claim, DataSet. Observed top-level functions: _a… |
| Tests | test | Observed | Groups 41 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH sys.exit, PATCH builtins.print, PATCH google.cloud.monitoring_v3.MetricServiceClient, PATCH sys.exit, PATCH buil… |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.github/workflows/link-checker.yml` (ci)
- `index.json` (config)
- `lychee.toml` (config)
- `plugins/cloud/google-cloud-developer/.claude-plugin/plugin.json` (config)
- `plugins/cloud/google-cloud-developer/.codex-plugin/plugin.json` (config)
- `plugins/cloud/google-cloud-developer/.mcp.json` (config)
- `plugins/cloud/google-cloud-developer/com.google.antigravity/mcp_config.json` (config)
- `plugins/cloud/google-cloud-developer/gemini-extension.json` (config)
- `plugins/cloud/google-cloud-developer/mcp.json` (config)
- `plugins/cloud/google-cloud-developer/mcp_config.json` (config)
- `plugins/cloud/google-cloud-developer/plugin.json` (config)
- `skills/cloud/agent-platform-alert-configuration/scripts/requirements.txt` (manifest)
- `skills/cloud/agent-platform-inference/scripts/requirements.txt` (manifest)
- `skills/cloud/agent-platform-skill-registry/scripts/requirements.txt` (manifest)
- `skills/cloud/agent-platform-tuning/references/requirements.txt` (manifest)
- `skills/cloud/apigee-agent-gateway-governance/assets/apigee-agent-gateway-governance.example.yaml` (config)
- `skills/cloud/apigee-agent-gateway-governance/assets/apigee-proxy-template.yaml` (config)
- `skills/cloud/apigee-agent-gateway-governance/assets/authz-extension.example.yaml` (config)
- `skills/cloud/apigee-agent-gateway-governance/assets/authz-policy.example.yaml` (config)
- `skills/cloud/apigee-agent-gateway-governance/assets/feature-identity.yaml` (config)
- `skills/cloud/apigee-agent-gateway-governance/assets/feature-model-armor.yaml` (config)
- `skills/cloud/apigee-agent-gateway-governance/assets/feature-normalize.yaml` (config)
- `skills/cloud/apigee-agent-gateway-governance/assets/feature-semantic-cache.yaml` (config)
- `skills/cloud/apigee-agent-gateway-governance/assets/feature-token-enforce.yaml` (config)
- `skills/cloud/apigee-agent-gateway-governance/assets/feature-token-metering.yaml` (config)
- `skills/cloud/assuredworkloads-frameworks-author/assets/locations.json` (config)
- `skills/cloud/assuredworkloads-frameworks-navigator/assets/locations.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/environment_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/experimental_input_formats_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/experimental_metadata_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/experimental_object_rewriter_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/experimental_optimizer_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/experimental_statement_rewriter_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/input_formats_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/metadata_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/object_rewriter_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/optimizer_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_examples/statement_rewriter_example.yaml` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/environment.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/experimental_input_formats.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/experimental_metadata.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/experimental_object_rewriter.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/experimental_optimizer.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/experimental_statement_rewriter.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/input_formats.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/metadata.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/object_rewriter.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/optimizer.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/statement_rewriter.json` (config)
- `skills/cloud/bigquery-migration-sql-translator/assets/translation_config_schemas/transpiler_config_spec.json` (config)
- `skills/cloud/bigtable-basics/assets/row_key_schema.yaml` (config)
- `skills/cloud/cloud-logging-finops/scripts/requirements.txt` (manifest)
- `skills/cloud/cloud-monitoring-alert-configuration/scripts/agent_platform/requirements.txt` (manifest)
- `skills/cloud/cloud-monitoring-chart-generation/scripts/requirements.txt` (manifest)
- `skills/cloud/cloud-trace-querying/assets/formatting/a2ui/single_span/display.a2ui.json` (config)
- `skills/cloud/cloud-trace-querying/assets/formatting/a2ui/trace_chart/display.a2ui.json` (config)
- `skills/cloud/cloud-trace-querying/assets/formatting/a2ui/trace_flow/display.a2ui.json` (config)
- `skills/cloud/cloud-trace-querying/assets/formatting/a2ui/traces_heat_map/display.a2ui.json` (config)
- `skills/cloud/cloud-trace-querying/scripts/requirements.txt` (manifest)

## Top-level layout

- `skills` — 762 analysed file(s)
- `plugins` — 27 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e3c591afe426ea585e4c21799e5199d6d47cd1be` is the revision these paths and observations refer to.
