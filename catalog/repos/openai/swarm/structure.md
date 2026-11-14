# Project structure: openai/swarm

**Analysed commit:** `6af0b4caf37dca4526dfd98e9fbd8ce36e7eeb22`

**Commit reference:** [6af0b4caf37dca4526dfd98e9fbd8ce36e7eeb22](https://github.com/openai/swarm/commit/6af0b4caf37dca4526dfd98e9fbd8ce36e7eeb22)

**Tree at this commit:** [openai/swarm@6af0b4caf37d](https://github.com/openai/swarm/tree/6af0b4caf37dca4526dfd98e9fbd8ce36e7eeb22)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | openai/swarm |
| Description | Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team. |
| Stars | 22138 |
| Forks | 2355 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `6af0b4caf37dca4526dfd98e9fbd8ce36e7eeb22` |
| Retrieved at | 2026-11-14T19:07:55.648836+00:00 |
| Files in this snapshot | 285 |

## Directory tree

```text
examples/  (236 files)
  airline/  (15 files)
    configs/  (3 files)
      … 3 files under this directory
    data/  (3 files)
      … 3 files under this directory
    evals/  (6 files)
      … 6 files under this directory
    README.md
    __init__.py
    main.py
  basic/  (6 files)
    README.md
    agent_handoff.py
    bare_minimum.py
    context_variables.py
    function_calling.py
    simple_loop_no_helpers.py
  customer_service/  (5 files)
    logs/  (5 files)
      … 5 files under this directory
  customer_service_lite/  (4 files)
    logs/  (4 files)
      … 4 files under this directory
  customer_service_streaming/  (108 files)
    configs/  (11 files)
      … 11 files under this directory
    data/  (76 files)
      … 76 files under this directory
    logs/  (1 files)
      … 1 files under this directory
    src/  (14 files)
      … 14 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    .gitignore
    docker-compose.yaml
    main.py
    prep_data.py
  personal_shopper/  (4 files)
    README.md
    __init__.py
    database.py
    main.py
  support_bot/  (84 files)
    data/  (76 files)
      … 76 files under this directory
    Makefile
    README.md
    __init__.py
    customer_service.py
    docker-compose.yaml
    main.py
    prep_data.py
    requirements.txt
  triage_agent/  (5 files)
    README.md
    agents.py
    evals.py
    evals_util.py
    run.py
  weather_agent/  (4 files)
    README.md
    agents.py
    evals.py
    run.py
  __init__.py
logs/  (31 files)
  session_20240402-112114.json
  session_20240402-112443.json
  session_20240402-112456.json
  session_20240402-112501.json
  session_20240402-113222.json
  session_20240402-113415.json
  session_20240425-135655.json
  session_20240425-135657.json
  session_20240425-135728.json
  session_20240425-140427.json
  session_20240425-140502.json
  session_20240425-140516.json
  session_20240425-140553.json
  session_20240425-141416.json
  session_20240425-141509.json
  session_20240425-141709.json
  session_20240425-145129.json
  session_20240425-145324.json
  session_20240425-145907.json
  session_20240425-145930.json
  session_20240425-150004.json
  session_20240425-150040.json
  session_20240425-155814.json
  session_20240425-172809.json
  … 7 more files
swarm/  (6 files)
  repl/  (2 files)
    __init__.py
    repl.py
  __init__.py
  core.py
  types.py
  util.py
tests/  (5 files)
  test_runs/  (1 files)
    test_20240402-113647.json
  __init__.py
  mock_client.py
  test_core.py
  test_util.py
.gitignore
.pre-commit-config.yaml
LICENSE
README.md
SECURITY.md
pyproject.toml
setup.cfg
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 33 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| swarm package | library | Observed | Groups 6 file(s) under swarm package (observed from repository paths and static analysis). Observed top-level classes: Agent, Response, Result, Swarm. Observed top-level functions: debug_print, function_to_json, merge_c… |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: MockOpenAIClient. Observed top-level functions: create_mock_response, mock_openai_client, test_basic_functio… |

## Important files

- `.pre-commit-config.yaml` (config)
- `examples/airline/evals/eval_cases/flight_modification_cases.json` (config)
- `examples/airline/evals/eval_cases/triage_cases.json` (config)
- `examples/airline/evals/eval_results/flight_modification_evals.json` (config)
- `examples/airline/evals/eval_results/triage_evals.json` (config)
- `examples/customer_service/logs/session_20240422-134602.json` (config)
- `examples/customer_service/logs/session_20240422-135231.json` (config)
- `examples/customer_service/logs/session_20240422-135321.json` (config)
- `examples/customer_service/logs/session_20240422-140035.json` (config)
- `examples/customer_service/logs/session_20240422-141344.json` (config)
- `examples/customer_service_lite/logs/session_20240425-175026.json` (config)
- `examples/customer_service_lite/logs/session_20240425-175112.json` (config)
- `examples/customer_service_lite/logs/session_20240425-175154.json` (config)
- `examples/customer_service_lite/logs/session_20240425-175210.json` (config)
- `examples/customer_service_streaming/configs/assistants/user_interface/assistant.json` (config)
- `examples/customer_service_streaming/configs/swarm_tasks.json` (config)
- `examples/customer_service_streaming/configs/tools/query_docs/tool.json` (config)
- `examples/customer_service_streaming/configs/tools/send_email/tool.json` (config)
- `examples/customer_service_streaming/configs/tools/submit_ticket/tool.json` (config)
- `examples/customer_service_streaming/data/article_6233728.json` (config)
- `examples/customer_service_streaming/data/article_6272941.json` (config)
- `examples/customer_service_streaming/data/article_6272952.json` (config)
- `examples/customer_service_streaming/data/article_6283125.json` (config)
- `examples/customer_service_streaming/data/article_6338764.json` (config)
- `examples/customer_service_streaming/data/article_6338765.json` (config)
- `examples/customer_service_streaming/data/article_6378378.json` (config)
- `examples/customer_service_streaming/data/article_6378407.json` (config)
- `examples/customer_service_streaming/data/article_6399305.json` (config)
- `examples/customer_service_streaming/data/article_6402865.json` (config)
- `examples/customer_service_streaming/data/article_6425277.json` (config)
- `examples/customer_service_streaming/data/article_6431339.json` (config)
- `examples/customer_service_streaming/data/article_6431922.json` (config)
- `examples/customer_service_streaming/data/article_6468065.json` (config)
- `examples/customer_service_streaming/data/article_6485334.json` (config)
- `examples/customer_service_streaming/data/article_6503842.json` (config)
- `examples/customer_service_streaming/data/article_6516417.json` (config)
- `examples/customer_service_streaming/data/article_6582257.json` (config)
- `examples/customer_service_streaming/data/article_6582391.json` (config)
- `examples/customer_service_streaming/data/article_6584194.json` (config)
- `examples/customer_service_streaming/data/article_6584249.json` (config)
- `examples/customer_service_streaming/data/article_6613520.json` (config)
- `examples/customer_service_streaming/data/article_6613605.json` (config)
- `examples/customer_service_streaming/data/article_6613629.json` (config)
- `examples/customer_service_streaming/data/article_6613657.json` (config)
- `examples/customer_service_streaming/data/article_6614161.json` (config)
- `examples/customer_service_streaming/data/article_6614209.json` (config)
- `examples/customer_service_streaming/data/article_6614457.json` (config)
- `examples/customer_service_streaming/data/article_6639781.json` (config)
- `examples/customer_service_streaming/data/article_6640792.json` (config)
- `examples/customer_service_streaming/data/article_6640864.json` (config)
- `examples/customer_service_streaming/data/article_6640875.json` (config)
- `examples/customer_service_streaming/data/article_6641048.json` (config)
- `examples/customer_service_streaming/data/article_6643004.json` (config)
- `examples/customer_service_streaming/data/article_6643036.json` (config)
- `examples/customer_service_streaming/data/article_6643167.json` (config)
- `examples/customer_service_streaming/data/article_6643200.json` (config)
- `examples/customer_service_streaming/data/article_6643435.json` (config)
- `examples/customer_service_streaming/data/article_6653653.json` (config)
- `examples/customer_service_streaming/data/article_6654000.json` (config)
- `examples/customer_service_streaming/data/article_6654303.json` (config)
- `examples/customer_service_streaming/data/article_6681258.json` (config)
- `examples/customer_service_streaming/data/article_6684216.json` (config)
- `examples/customer_service_streaming/data/article_6696591.json` (config)
- `examples/customer_service_streaming/data/article_6705023.json` (config)
- `examples/customer_service_streaming/data/article_6742369.json` (config)
- `examples/customer_service_streaming/data/article_6781152.json` (config)
- `examples/customer_service_streaming/data/article_6781222.json` (config)
- `examples/customer_service_streaming/data/article_6781228.json` (config)
- `examples/customer_service_streaming/data/article_6783457.json` (config)
- `examples/customer_service_streaming/data/article_6811186.json` (config)
- `examples/customer_service_streaming/data/article_6824809.json` (config)
- `examples/customer_service_streaming/data/article_6825453.json` (config)
- `examples/customer_service_streaming/data/article_6837156.json` (config)
- `examples/customer_service_streaming/data/article_6843909.json` (config)
- `examples/customer_service_streaming/data/article_6843914.json` (config)
- `examples/customer_service_streaming/data/article_6882433.json` (config)
- `examples/customer_service_streaming/data/article_6891753.json` (config)
- `examples/customer_service_streaming/data/article_6891767.json` (config)
- `examples/customer_service_streaming/data/article_6891781.json` (config)
- `examples/customer_service_streaming/data/article_6891827.json` (config)
- `examples/customer_service_streaming/data/article_6891829.json` (config)
- `examples/customer_service_streaming/data/article_6891831.json` (config)
- `examples/customer_service_streaming/data/article_6891834.json` (config)
- `examples/customer_service_streaming/data/article_6891839.json` (config)
- `examples/customer_service_streaming/data/article_6897179.json` (config)
- `examples/customer_service_streaming/data/article_6897186.json` (config)
- `examples/customer_service_streaming/data/article_6897191.json` (config)
- `examples/customer_service_streaming/data/article_6897194.json` (config)
- `examples/customer_service_streaming/data/article_6897198.json` (config)
- `examples/customer_service_streaming/data/article_6897199.json` (config)
- `examples/customer_service_streaming/data/article_6897202.json` (config)
- `examples/customer_service_streaming/data/article_6897204.json` (config)
- `examples/customer_service_streaming/data/article_6897213.json` (config)
- `examples/customer_service_streaming/data/article_6901266.json` (config)
- `examples/customer_service_streaming/data/article_6950777.json` (config)
- `examples/customer_service_streaming/docker-compose.yaml` (container)
- `examples/support_bot/data/article_6233728.json` (config)
- `examples/support_bot/data/article_6272941.json` (config)
- `examples/support_bot/data/article_6272952.json` (config)
- `examples/support_bot/data/article_6283125.json` (config)
- `examples/support_bot/data/article_6338764.json` (config)
- `examples/support_bot/data/article_6338765.json` (config)
- `examples/support_bot/data/article_6378378.json` (config)
- `examples/support_bot/data/article_6378407.json` (config)
- `examples/support_bot/data/article_6399305.json` (config)
- `examples/support_bot/data/article_6402865.json` (config)
- `examples/support_bot/data/article_6425277.json` (config)
- `examples/support_bot/data/article_6431339.json` (config)
- `examples/support_bot/data/article_6431922.json` (config)
- `examples/support_bot/data/article_6468065.json` (config)
- `examples/support_bot/data/article_6485334.json` (config)
- `examples/support_bot/data/article_6503842.json` (config)
- `examples/support_bot/data/article_6516417.json` (config)
- `examples/support_bot/data/article_6582257.json` (config)
- `examples/support_bot/data/article_6582391.json` (config)
- `examples/support_bot/data/article_6584194.json` (config)
- `examples/support_bot/data/article_6584249.json` (config)
- `examples/support_bot/data/article_6613520.json` (config)
- `examples/support_bot/data/article_6613605.json` (config)
- `examples/support_bot/data/article_6613629.json` (config)
- `examples/support_bot/data/article_6613657.json` (config)
- `examples/support_bot/data/article_6614161.json` (config)
- `examples/support_bot/data/article_6614209.json` (config)
- `examples/support_bot/data/article_6614457.json` (config)
- `examples/support_bot/data/article_6639781.json` (config)
- `examples/support_bot/data/article_6640792.json` (config)
- `examples/support_bot/data/article_6640864.json` (config)
- `examples/support_bot/data/article_6640875.json` (config)
- `examples/support_bot/data/article_6641048.json` (config)
- `examples/support_bot/data/article_6643004.json` (config)
- `examples/support_bot/data/article_6643036.json` (config)
- `examples/support_bot/data/article_6643167.json` (config)
- `examples/support_bot/data/article_6643200.json` (config)
- `examples/support_bot/data/article_6643435.json` (config)
- `examples/support_bot/data/article_6653653.json` (config)
- `examples/support_bot/data/article_6654000.json` (config)
- `examples/support_bot/data/article_6654303.json` (config)
- `examples/support_bot/data/article_6681258.json` (config)
- `examples/support_bot/data/article_6684216.json` (config)
- `examples/support_bot/data/article_6696591.json` (config)
- `examples/support_bot/data/article_6705023.json` (config)
- `examples/support_bot/data/article_6742369.json` (config)
- `examples/support_bot/data/article_6781152.json` (config)
- `examples/support_bot/data/article_6781222.json` (config)
- `examples/support_bot/data/article_6781228.json` (config)
- `examples/support_bot/data/article_6783457.json` (config)
- `examples/support_bot/data/article_6811186.json` (config)
- `examples/support_bot/data/article_6824809.json` (config)
- `examples/support_bot/data/article_6825453.json` (config)
- `examples/support_bot/data/article_6837156.json` (config)
- `examples/support_bot/data/article_6843909.json` (config)
- `examples/support_bot/data/article_6843914.json` (config)
- `examples/support_bot/data/article_6882433.json` (config)
- `examples/support_bot/data/article_6891753.json` (config)
- `examples/support_bot/data/article_6891767.json` (config)
- `examples/support_bot/data/article_6891781.json` (config)
- `examples/support_bot/data/article_6891827.json` (config)
- `examples/support_bot/data/article_6891829.json` (config)
- `examples/support_bot/data/article_6891831.json` (config)
- `examples/support_bot/data/article_6891834.json` (config)
- `examples/support_bot/data/article_6891839.json` (config)
- `examples/support_bot/data/article_6897179.json` (config)
- `examples/support_bot/data/article_6897186.json` (config)
- `examples/support_bot/data/article_6897191.json` (config)
- `examples/support_bot/data/article_6897194.json` (config)
- `examples/support_bot/data/article_6897198.json` (config)
- `examples/support_bot/data/article_6897199.json` (config)
- `examples/support_bot/data/article_6897202.json` (config)
- `examples/support_bot/data/article_6897204.json` (config)
- `examples/support_bot/data/article_6897213.json` (config)
- `examples/support_bot/data/article_6901266.json` (config)
- `examples/support_bot/data/article_6950777.json` (config)
- `examples/support_bot/docker-compose.yaml` (container)
- `examples/support_bot/requirements.txt` (manifest)
- `logs/session_20240402-112114.json` (config)
- `logs/session_20240402-112443.json` (config)
- `logs/session_20240402-112456.json` (config)
- `logs/session_20240402-112501.json` (config)
- `logs/session_20240402-113222.json` (config)
- `logs/session_20240402-113415.json` (config)
- `logs/session_20240425-135655.json` (config)
- `logs/session_20240425-135657.json` (config)
- `logs/session_20240425-135728.json` (config)
- `logs/session_20240425-140427.json` (config)
- `logs/session_20240425-140502.json` (config)
- `logs/session_20240425-140516.json` (config)
- `logs/session_20240425-140553.json` (config)
- `logs/session_20240425-141416.json` (config)
- `logs/session_20240425-141509.json` (config)
- `logs/session_20240425-141709.json` (config)
- `logs/session_20240425-145129.json` (config)
- `logs/session_20240425-145324.json` (config)
- `logs/session_20240425-145907.json` (config)
- `logs/session_20240425-145930.json` (config)
- `logs/session_20240425-150004.json` (config)
- `logs/session_20240425-150040.json` (config)
- `logs/session_20240425-155814.json` (config)
- `logs/session_20240425-172809.json` (config)
- `logs/session_20240425-211732.json` (config)
- `logs/session_20240425-211813.json` (config)
- `logs/session_20240425-211942.json` (config)
- `logs/session_20240425-212341.json` (config)
- `logs/session_20240425-212431.json` (config)
- `logs/session_20240425-212748.json` (config)
- `logs/session_20240425-213023.json` (config)
- `pyproject.toml` (manifest)
- `setup.cfg` (manifest)

## Top-level layout

- `examples` — 236 analysed file(s)
- `logs` — 31 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `swarm` — 6 analysed file(s)
- `tests` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `6af0b4caf37dca4526dfd98e9fbd8ce36e7eeb22` is the revision these paths and observations refer to.
