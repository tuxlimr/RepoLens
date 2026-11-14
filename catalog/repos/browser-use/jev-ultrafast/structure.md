# Project structure: browser-use/jev-ultrafast

**Analysed commit:** `cf3c406f0fc4becff8986ed4d4d37b7b9f102e45`

**Commit reference:** [cf3c406f0fc4becff8986ed4d4d37b7b9f102e45](https://github.com/browser-use/jev-ultrafast/commit/cf3c406f0fc4becff8986ed4d4d37b7b9f102e45)

**Tree at this commit:** [browser-use/jev-ultrafast@cf3c406f0fc4](https://github.com/browser-use/jev-ultrafast/tree/cf3c406f0fc4becff8986ed4d4d37b7b9f102e45)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | browser-use/jev-ultrafast |
| Description | Fastest and cheapest web agent |
| Stars | 24497 |
| Forks | 1887 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `cf3c406f0fc4becff8986ed4d4d37b7b9f102e45` |
| Retrieved at | 2026-11-14T19:07:36.302240+00:00 |
| Files in this snapshot | 35 |

## Directory tree

```text
docs/  (9 files)
  banner.svg
  design.md
  flights-measurement.json
  flights-prepared-measurement.json
  full-speed-measurement.json
  launch-draft.md
  measurement.json
  performance-prepared.md
  performance.md
examples/  (2 files)
  flights.py
  run.py
jev_ultrafast/  (11 files)
  static/  (4 files)
    app.js
    fixture.html
    index.html
    style.css
  __init__.py
  agent.py
  browser.py
  demo.py
  model.py
  questions.py
  snapshot.js
scripts/  (6 files)
  check_guards.py
  measure_flights.py
  record_flights.py
  render_demo.py
  render_fixture.py
  smoke.py
tests/  (1 files)
  test_agent.py
.env.example
.gitignore
AGENTS.md
LICENSE
README.md
pyproject.toml
```

## Entry points

- [jev_ultrafast/demo.py](https://github.com/browser-use/jev-ultrafast/blob/cf3c406f0fc4becff8986ed4d4d37b7b9f102e45/jev_ultrafast/demo.py)
- [scripts/check_guards.py:136](https://github.com/browser-use/jev-ultrafast/blob/cf3c406f0fc4becff8986ed4d4d37b7b9f102e45/scripts/check_guards.py#L136)
- [scripts/smoke.py:56](https://github.com/browser-use/jev-ultrafast/blob/cf3c406f0fc4becff8986ed4d4d37b7b9f102e45/scripts/smoke.py#L56)
- [jev_ultrafast/static/app.js](https://github.com/browser-use/jev-ultrafast/blob/cf3c406f0fc4becff8986ed4d4d37b7b9f102e45/jev_ultrafast/static/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: action_space, choose, field_context, field_text, post_json, validate_choice. |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Handler. Observed top-level functions: close_browser, command, load_environment, main, res… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| jev_ultrafast package | library | Observed | Groups 6 file(s) under jev_ultrafast package (observed from repository paths and static analysis). Observed top-level classes: Agent, Browser, StalePage. Observed top-level functions: browser_operation, fingerprint. |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: capture, font, mono, timed. |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: choice, decision, page, runner, test_all_heads_are_one_request_and_only_matching_head_executes, test_chang… |

## Important files

- `.env.example` (config)
- `docs/flights-measurement.json` (config)
- `docs/flights-prepared-measurement.json` (config)
- `docs/full-speed-measurement.json` (config)
- `docs/measurement.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `jev_ultrafast` — 11 analysed file(s)
- `docs` — 9 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `scripts` — 6 analysed file(s)
- `examples` — 2 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `cf3c406f0fc4becff8986ed4d4d37b7b9f102e45` is the revision these paths and observations refer to.
