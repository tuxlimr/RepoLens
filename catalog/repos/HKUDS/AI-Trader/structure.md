# Project structure: HKUDS/AI-Trader

**Analysed commit:** `d03ff6c056b32ced735adf7c19ed8175adb1c8df`

**Commit reference:** [d03ff6c056b32ced735adf7c19ed8175adb1c8df](https://github.com/HKUDS/AI-Trader/commit/d03ff6c056b32ced735adf7c19ed8175adb1c8df)

**Tree at this commit:** [HKUDS/AI-Trader@d03ff6c056b3](https://github.com/HKUDS/AI-Trader/tree/d03ff6c056b32ced735adf7c19ed8175adb1c8df)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | HKUDS/AI-Trader |
| Description | "AI-Trader: 100% Fully-Automated Agent-Native Trading"   |
| Stars | 23267 |
| Forks | 3504 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `d03ff6c056b32ced735adf7c19ed8175adb1c8df` |
| Retrieved at | 2026-11-14T19:07:49.152851+00:00 |
| Files in this snapshot | 146 |

## Directory tree

```text
docs/  (7 files)
  api/  (2 files)
    copytrade.yaml
    openapi.yaml
  local-ops/  (1 files)
    production-branch.md
  README_AGENT.md
  README_AGENT_ZH.md
  README_USER.md
  README_USER_ZH.md
research/  (39 files)
  exports/  (3 files)
    figures/  (1 files)
      … 1 files under this directory
    tables/  (1 files)
      … 1 files under this directory
    .gitkeep
  notebooks/  (1 files)
    .gitkeep
  schemas/  (25 files)
    agents.schema.json
    challenge_participants.schema.json
    challenge_results.schema.json
    challenge_submissions.schema.json
    challenge_trades.schema.json
    challenges.schema.json
    events.schema.json
    experiment_assignments.schema.json
    network_edges.schema.json
    positions.schema.json
    predictions.schema.json
    profit_history.schema.json
    quality_scores.schema.json
    rewards.schema.json
    signal_replies.schema.json
    signals.schema.json
    subscriptions.schema.json
    team_contributions.schema.json
    team_members.schema.json
    team_messages.schema.json
    team_missions.schema.json
    team_results.schema.json
    team_submissions.schema.json
    teams.schema.json
    … 1 more files
  scripts/  (7 files)
    analyze_experiments.py
    build_agent_features.py
    build_network_edges.py
    compute_metrics.py
    export_research_dataset.py
    generate_figures.py
    research_common.py
  README.md
  experiment_process_log.md
  requirements.txt
service/  (87 files)
  frontend/  (18 files)
    src/  (13 files)
      … 13 files under this directory
    index.html
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.mts
  server/  (67 files)
    scripts/  (9 files)
      … 9 files under this directory
    tests/  (21 files)
      … 21 files under this directory
    cache.py
    challenge_scoring.py
    challenges.py
    config.py
    database.py
    experiment_events.py
    experiment_metrics.py
    experiment_notifications.py
    experiments.py
    fees.py
    main.py
    market_intel.py
    permissions.py
    price_fetcher.py
    research_exports.py
    rewards.py
    routes.py
    routes_agent.py
    routes_challenges.py
    routes_experiments.py
    routes_market.py
    routes_misc.py
    routes_models.py
    routes_research.py
    … 13 more files
  README.md
  requirements.txt
skills/  (6 files)
  ai4trade/  (1 files)
    SKILL.md
  copytrade/  (1 files)
    SKILL.md
  heartbeat/  (1 files)
    SKILL.md
  market-intel/  (1 files)
    SKILL.md
  polymarket/  (1 files)
    SKILL.md
  tradesync/  (1 files)
    SKILL.md
.env.example
.gitignore
README.md
README_ZH.md
impeccable.context.tmp
package.json
tsconfig.json
```

## Entry points

- [research/scripts/analyze_experiments.py:323](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/research/scripts/analyze_experiments.py#L323)
- [research/scripts/build_agent_features.py:93](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/research/scripts/build_agent_features.py#L93)
- [research/scripts/build_network_edges.py:40](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/research/scripts/build_network_edges.py#L40)
- [research/scripts/compute_metrics.py:80](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/research/scripts/compute_metrics.py#L80)
- [research/scripts/export_research_dataset.py:54](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/research/scripts/export_research_dataset.py#L54)
- [research/scripts/generate_figures.py:180](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/research/scripts/generate_figures.py#L180)
- [service/server/main.py:99](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/service/server/main.py#L99)
- [service/server/routes.py:27](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/service/server/routes.py#L27)
- [service/server/scripts/cleanup_dirty_trade_data.py:600](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/service/server/scripts/cleanup_dirty_trade_data.py#L600)
- [service/server/scripts/fix_agent_profit.py:47](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/service/server/scripts/fix_agent_profit.py#L47)
- [service/server/scripts/manage_leaderboard_exclusions.py:336](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/service/server/scripts/manage_leaderboard_exclusions.py#L336)
- [service/server/scripts/migrate_sqlite_to_postgres.py:230](https://github.com/HKUDS/AI-Trader/blob/d03ff6c056b32ced735adf7c19ed8175adb1c8df/service/server/scripts/migrate_sqlite_to_postgres.py#L230)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 33 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: DatabaseConnection, DatabaseCursor. Observed top-level functions: _adapt_sql_for_postgres, _ensure_chal… |
| Application entry point | entrypoint | Observed | Groups 18 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: PositionState, RepairPlan, TrackSpec. Ob… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| research package | library | Observed | Groups 1 file(s) under research package (observed from repository paths and static analysis). Observed top-level functions: add_common_export_filters, as_float, as_int, benjamini_hochberg, bootstrap_ci, ensure_dir. |
| Service / domain layer | service | Observed | Groups 44 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AgentLogin, AgentMessageCreate, AgentMessagesMarkReadRequest, AgentPasswordResetConfirm, A… |
| Tests | test | Observed | Groups 21 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: PATCH market_intel.set_json, PATCH market_intel.get_json, PATCH marke… |

## Important files

- `.env.example` (config)
- `docs/api/copytrade.yaml` (config)
- `docs/api/openapi.yaml` (config)
- `package.json` (manifest)
- `research/requirements.txt` (manifest)
- `research/schemas/agents.schema.json` (config)
- `research/schemas/challenge_participants.schema.json` (config)
- `research/schemas/challenge_results.schema.json` (config)
- `research/schemas/challenge_submissions.schema.json` (config)
- `research/schemas/challenge_trades.schema.json` (config)
- `research/schemas/challenges.schema.json` (config)
- `research/schemas/events.schema.json` (config)
- `research/schemas/experiment_assignments.schema.json` (config)
- `research/schemas/network_edges.schema.json` (config)
- `research/schemas/positions.schema.json` (config)
- `research/schemas/predictions.schema.json` (config)
- `research/schemas/profit_history.schema.json` (config)
- `research/schemas/quality_scores.schema.json` (config)
- `research/schemas/rewards.schema.json` (config)
- `research/schemas/signal_replies.schema.json` (config)
- `research/schemas/signals.schema.json` (config)
- `research/schemas/subscriptions.schema.json` (config)
- `research/schemas/team_contributions.schema.json` (config)
- `research/schemas/team_members.schema.json` (config)
- `research/schemas/team_messages.schema.json` (config)
- `research/schemas/team_missions.schema.json` (config)
- `research/schemas/team_results.schema.json` (config)
- `research/schemas/team_submissions.schema.json` (config)
- `research/schemas/teams.schema.json` (config)
- `research/schemas/trades.schema.json` (config)
- `service/frontend/package.json` (manifest)
- `service/frontend/tsconfig.json` (config)
- `service/frontend/tsconfig.node.json` (config)
- `service/requirements.txt` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `service` — 87 analysed file(s)
- `research` — 39 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `docs` — 7 analysed file(s)
- `skills` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d03ff6c056b32ced735adf7c19ed8175adb1c8df` is the revision these paths and observations refer to.
