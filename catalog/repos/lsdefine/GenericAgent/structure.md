# Project structure: lsdefine/GenericAgent

**Analysed commit:** `68d996a4588210aacb39cf79a4974d2743316e64`

**Commit reference:** [68d996a4588210aacb39cf79a4974d2743316e64](https://github.com/lsdefine/GenericAgent/commit/68d996a4588210aacb39cf79a4974d2743316e64)

**Tree at this commit:** [lsdefine/GenericAgent@68d996a45882](https://github.com/lsdefine/GenericAgent/tree/68d996a4588210aacb39cf79a4974d2743316e64)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lsdefine/GenericAgent |
| Description | Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption |
| Stars | 14422 |
| Forks | 1669 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `68d996a4588210aacb39cf79a4974d2743316e64` |
| Retrieved at | 2026-11-14T19:09:25.385992+00:00 |
| Files in this snapshot | 176 |

## Directory tree

```text
assets/  (23 files)
  tmwd_cdp_bridge/  (6 files)
    background.js
    content.js
    disable_dialogs.js
    manifest.json
    popup.html
    popup.js
  agent_bbs.py
  cc_system_template.txt
  code_run_header.py
  configure_mykey.py
  ga_httpapp.py
  ga_install.ps1
  ga_install.sh
  ga_ultraplan.py
  global_mem_insight_template.txt
  global_mem_insight_template_en.txt
  insight_fixed_structure.txt
  insight_fixed_structure_en.txt
  supergrok_proxy.py
  sys_prompt.txt
  sys_prompt_en.txt
  tools_schema.json
  tools_schema_cn.json
docs/  (6 files)
  GETTING_STARTED.md
  SETUP_FEISHU.md
  desktop_components.md
  installation.md
  installation_zh.md
  macos_desktop_installation_zh.md
frontends/  (71 files)
  conductor_im_plugins/  (3 files)
    _TEMPLATE.py
    _email_example.py
    _lark_example.py
  desktop/  (2 files)
    .gitignore
    README.md
  skins/  (9 files)
    boy/  (1 files)
      … 1 files under this directory
    dinosaur/  (1 files)
      … 1 files under this directory
    doux/  (1 files)
      … 1 files under this directory
    glube/  (1 files)
      … 1 files under this directory
    line/  (2 files)
      … 2 files under this directory
    mort/  (1 files)
      … 1 files under this directory
    tard/  (1 files)
      … 1 files under this directory
    vita/  (1 files)
      … 1 files under this directory
  tests/  (18 files)
    requirements.txt
    test_bridge_capabilities.py
    test_bridge_e2e_controls.py
    test_bridge_hub.py
    test_bridge_model_switch.py
    test_bridge_origin_security.py
    test_bridge_sessions.py
    test_bridge_submit.py
    test_bridge_uploads.py
    test_bridge_utils.py
    test_conductor_model_routing.py
    test_cost_tracker_ledger.py
    test_data_backup.py
    test_desktop_history.py
    test_ga_root_contract.py
    test_hub_p2p_wait.py
    test_release_qualification.py
    test_tauri_security_contract.py
  DESKTOP_PET_README.md
  at_complete.py
  btw_cmd.py
  chatapp_common.py
  conductor.html
  conductor.py
  continue_cmd.py
  cost_tracker.py
  data_backup.py
  dcapp.py
  desktop_bridge.py
  desktop_history.py
  desktop_pet_v2.pyw
  desktop_settings.py
  dingtalkapp.py
  export_cmd.py
  fsapp.py
  ga_contract_probe.py
  genericagent_acp_bridge.py
  hub.html
  hub.py
  hub_p2p.py
  keysym.py
  model_cmd.py
  … 15 more files
ga_cli/  (5 files)
  __init__.py
  __main__.py
  cli.py
  ga-cli-install.cmd
  ga_cli.cmd
memory/  (43 files)
  L4_raw_sessions/  (2 files)
    compress_session.py
    salient_mining_sop.md
  autonomous_operation_sop/  (2 files)
    helper.py
    task_planning.md
  review_sop/  (2 files)
    review_inline_prompt.en.txt
    review_inline_prompt.txt
  adb_ui.py
  autonomous_operation_sop.md
  checklist_helper.py
  checklist_sop.md
  code_review_principles.md
  computer_use.md
  deliverable_audit_sop.md
  ganet_pc_setup_sop.md
  github_contribution_sop.md
  goal_hive_master_duty.md
  goal_hive_sop.md
  goal_mode_sop.md
  incubator_sop.md
  keychain.py
  ljqCtrl.py
  ljqCtrlBg.py
  ljqCtrl_sop.md
  macljqCtrl.py
  memory_cleanup_sop.md
  memory_management_sop.md
  morphling_sop.md
  ocr_utils.py
  plan_sop.md
  procmem_scanner.py
  … 13 more files
plugins/  (4 files)
  __init__.py
  hooks.py
  langfuse_tracing.py
  project_mode.py
reflect/  (5 files)
  agent_team_worker.py
  autonomous.py
  checklist_master.py
  goal_mode.py
  scheduler.py
.gitattributes
.gitignore
CONTRIBUTING.md
LICENSE
README.md
TMWebDriver.py
agent_loop.py
agentmain.py
ga
ga.cmd
ga.py
launch.pyw
legacy_llmcore.py
llmcore.py
mykey_template.py
mykey_template_en.py
pyproject.toml
service_manager.pyw
simphtml.py
```

## Entry points

- [TMWebDriver.py:288](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/TMWebDriver.py#L288)
- [agentmain.py:231](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/agentmain.py#L231)
- [assets/agent_bbs.py:40](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/assets/agent_bbs.py#L40)
- [assets/configure_mykey.py:1425](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/assets/configure_mykey.py#L1425)
- [assets/ga_httpapp.py:124](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/assets/ga_httpapp.py#L124)
- [assets/supergrok_proxy.py:389](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/assets/supergrok_proxy.py#L389)
- [frontends/conductor.py:136](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/frontends/conductor.py#L136)
- [frontends/dcapp.py:403](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/frontends/dcapp.py#L403)
- [frontends/desktop_bridge.py:3072](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/frontends/desktop_bridge.py#L3072)
- [frontends/dingtalkapp.py:146](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/frontends/dingtalkapp.py#L146)
- [frontends/fsapp.py:872](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/frontends/fsapp.py#L872)
- [frontends/ga_contract_probe.py:105](https://github.com/lsdefine/GenericAgent/blob/68d996a4588210aacb39cf79a4974d2743316e64/frontends/ga_contract_probe.py#L105)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 7 file(s) under assets package (observed from repository paths and static analysis). Observed top-level classes: _H. Observed top-level functions: _bind, _d, _fmt, _need_plan, _note, _op. |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: BaseHandler, BaseSession, ClaudeSession, GenericAgentHandler, LLMSession, MixinSession. Observed top-… |
| Application entry point | entrypoint | Observed | Groups 32 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Click, FastAPI, Group. Observed routes: GET /readme, GET /, POST /register, P… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Group, HTTPExporter, HTTPLocalProxy, HubUnion, Invite, P2PSocket. Observed top-level functio… |
| frontends package | library | Observed | Groups 22 file(s) under frontends package (observed from repository paths and static analysis). Observed top-level classes: AgentChatMixin, BackupFormatError, CheckpointNode, CheckpointTree, CompressedTree, DesktopSetti… |
| ga_cli package | library | Observed | Groups 1 file(s) under ga_cli package (observed from repository paths and static analysis). |
| memory package | library | Observed | Groups 3 file(s) under memory package (observed from repository paths and static analysis). Observed top-level classes: CL, SecretStr, _Keys. Observed top-level functions: __getattr__, _iou, _ocr_crops_batch, _ocr_full,… |
| plugins package | library | Observed | Groups 4 file(s) under plugins package (observed from repository paths and static analysis). Observed top-level functions: _active_project, _build_injection, _mem_path, _memory_stat, _project_dir, clear. |
| reflect package | library | Observed | Groups 5 file(s) under reflect package (observed from repository paths and static analysis). Observed top-level functions: _last_run, _load, _parse_cooldown, _poll_bbs, _prompt, _save. |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Backend, Client, FakeAgent, FakeSession, StubGenericAgent, TestAddMessageExtra. Observed top-level function… |

## Important files

- `assets/tmwd_cdp_bridge/manifest.json` (config)
- `assets/tools_schema.json` (config)
- `assets/tools_schema_cn.json` (config)
- `frontends/skins/boy/skin.json` (config)
- `frontends/skins/dinosaur/skin.json` (config)
- `frontends/skins/doux/skin.json` (config)
- `frontends/skins/glube/skin.json` (config)
- `frontends/skins/line/skin.json` (config)
- `frontends/skins/mort/skin.json` (config)
- `frontends/skins/tard/skin.json` (config)
- `frontends/skins/vita/skin.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `frontends` — 71 analysed file(s)
- `memory` — 43 analysed file(s)
- `assets` — 23 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `docs` — 6 analysed file(s)
- `ga_cli` — 5 analysed file(s)
- `reflect` — 5 analysed file(s)
- `plugins` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `68d996a4588210aacb39cf79a4974d2743316e64` is the revision these paths and observations refer to.
