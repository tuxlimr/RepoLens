# Project structure: Open-LLM-VTuber/Open-LLM-VTuber

**Analysed commit:** `992309c0aa19845960228f880013d4685fde93b5`

**Commit reference:** [992309c0aa19845960228f880013d4685fde93b5](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/commit/992309c0aa19845960228f880013d4685fde93b5)

**Tree at this commit:** [Open-LLM-VTuber/Open-LLM-VTuber@992309c0aa19](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/tree/992309c0aa19845960228f880013d4685fde93b5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Open-LLM-VTuber/Open-LLM-VTuber |
| Description | Talk to any LLM with hands-free voice interaction, voice interruption, and Live2D avatar running locally across platforms |
| Stars | 14709 |
| Forks | 1762 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `992309c0aa19845960228f880013d4685fde93b5` |
| Retrieved at | 2026-11-14T19:09:21.834063+00:00 |
| Files in this snapshot | 217 |

## Directory tree

```text
.cursor/  (1 files)
  rules/  (1 files)
    olv-core-rules.mdc
.gemini/  (2 files)
  GEMINI.md
  styleguide.md
.github/  (10 files)
  ISSUE_TEMPLATE/  (2 files)
    bug---question---get-help---bug---提问---求助.md
    feature-request---功能建议.md
  workflows/  (6 files)
    codeql.yml
    create_release.yml
    docker-blacksmith.yml
    fossa_scan.yml
    ruff.yml
    update-requirements.yml
  FUNDING.yml
  copilot-instructions.md
backgrounds/  (1 files)
  README.md
characters/  (5 files)
  README.md
  en_nuke_debate.yaml
  en_unhelpful_ai.yaml
  zh_米粒.yaml
  zh_翻译腔.yaml
config_templates/  (3 files)
  README.md
  conf.ZH.default.yaml
  conf.default.yaml
doc/  (6 files)
  sample_conf/  (5 files)
    sherpaASRTTS_sense_voice_melo.yaml
    sherpaASRTTS_sense_voice_piper_en.yaml
    sherpaASRTTS_sense_voice_vits_zh.yaml
    sherpaASR_paraformer.yaml
    sherpaASR_sense_voice.yaml
  README.md
live2d-models/  (29 files)
  mao_pro/  (20 files)
    runtime/  (19 files)
      … 19 files under this directory
    ReadMe.txt
  shizuku/  (9 files)
    runtime/  (8 files)
      … 8 files under this directory
    ReadMe.txt
prompts/  (12 files)
  utils/  (9 files)
    concise_style_prompt.txt
    group_conversation_prompt.txt
    live2d_expression_prompt.txt
    live_prompt.txt
    mcp_prompt.txt
    proactive_speak_prompt.txt
    speakable_prompt.txt
    think_tag_prompt.txt
    tool_guidance_prompt.txt
  README.md
  __init__.py
  prompt_loader.py
scripts/  (1 files)
  run_bilibili_live.py
src/  (107 files)
  open_llm_vtuber/  (107 files)
    agent/  (19 files)
      … 19 files under this directory
    asr/  (11 files)
      … 11 files under this directory
    config_manager/  (13 files)
      … 13 files under this directory
    conversations/  (7 files)
      … 7 files under this directory
    live/  (2 files)
      … 2 files under this directory
    mcpp/  (8 files)
      … 8 files under this directory
    translate/  (5 files)
      … 5 files under this directory
    tts/  (22 files)
      … 22 files under this directory
    utils/  (5 files)
      … 5 files under this directory
    vad/  (4 files)
      … 4 files under this directory
    __init__.py
    chat_group.py
    chat_history_manager.py
    live2d_model.py
    message_handler.py
    proxy_handler.py
    proxy_message_queue.py
    routes.py
    server.py
    service_context.py
    websocket_handler.py
upgrade_codes/  (13 files)
  from_version/  (2 files)
    __init__.py
    v_1_1_1.py
  upgrade_core/  (6 files)
    __init__.py
    comment_diff_fn.py
    comment_sync.py
    constants.py
    language.py
    upgrade_utils.py
  __init__.py
  compare_yaml.py
  config_sync.py
  upgrade_manager.py
  version_manager.py
web_tool/  (4 files)
  README.md
  index.html
  main.js
  recorder.js
.dockerignore
.gitattributes
.gitignore
.gitmodules
.pre-commit-config.yaml
.python-version
CLAUDE.md
CONTRIBUTING.md
LICENSE
LICENSE-Live2D.md
README.CN.md
README.JP.md
README.KR.md
README.md
dockerfile
mcp_servers.json
model_dict.json
pixi.lock
pyproject.toml
requirements-bilibili.txt
requirements.txt
run_server.py
upgrade.py
```

## Entry points

- [src/open_llm_vtuber/asr/azure_asr.py:154](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/src/open_llm_vtuber/asr/azure_asr.py#L154)
- [src/open_llm_vtuber/asr/utils.py:164](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/src/open_llm_vtuber/asr/utils.py#L164)
- [src/open_llm_vtuber/chat_group.py:22](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/src/open_llm_vtuber/chat_group.py#L22)
- [src/open_llm_vtuber/mcpp/json_detector.py:140](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/src/open_llm_vtuber/mcpp/json_detector.py#L140)
- [src/open_llm_vtuber/tts/azure_tts.py:136](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/src/open_llm_vtuber/tts/azure_tts.py#L136)
- [src/open_llm_vtuber/tts/pyttsx3_tts.py:40](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/src/open_llm_vtuber/tts/pyttsx3_tts.py#L40)
- [src/open_llm_vtuber/tts/tts_factory.py:221](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/src/open_llm_vtuber/tts/tts_factory.py#L221)
- [src/open_llm_vtuber/vad/silero.py:226](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/src/open_llm_vtuber/vad/silero.py#L226)
- [run_server.py:167](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/run_server.py#L167)
- [scripts/run_bilibili_live.py:56](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/scripts/run_bilibili_live.py#L56)
- [upgrade.py:170](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/upgrade.py#L170)
- [upgrade_codes/compare_yaml.py:74](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/blob/992309c0aa19845960228f880013d4685fde93b5/upgrade_codes/compare_yaml.py#L74)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 39 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Group. Observed top-level classes: AvatarStaticFiles, CORSStaticFiles, ChatGr… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: MCPClient. |
| open_llm_vtuber package | library | Observed | Groups 96 file(s) under open_llm_vtuber package (observed from repository paths and static analysis). Observed top-level classes: ASRConfig, ASRFactory, ASRInterface, Actions, AgentConfig, AgentFactory. Observed top-lev… |
| prompts package | library | Observed | Groups 2 file(s) under prompts package (observed from repository paths and static analysis). Observed top-level functions: _load_file_content, load_persona, load_util. |
| upgrade_codes package | library | Observed | Groups 12 file(s) under upgrade_codes package (observed from repository paths and static analysis). Observed top-level classes: CommentSynchronizer, ConfigSynchronizer, UpgradeManager, UpgradeUtility, VersionUpgradeMana… |
| web_tool package | library | Observed | Groups 2 file(s) under web_tool package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/create_release.yml` (ci)
- `.github/workflows/docker-blacksmith.yml` (ci)
- `.github/workflows/fossa_scan.yml` (ci)
- `.github/workflows/ruff.yml` (ci)
- `.github/workflows/update-requirements.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `characters/en_nuke_debate.yaml` (config)
- `characters/en_unhelpful_ai.yaml` (config)
- `characters/zh_米粒.yaml` (config)
- `characters/zh_翻译腔.yaml` (config)
- `config_templates/conf.ZH.default.yaml` (config)
- `config_templates/conf.default.yaml` (config)
- `doc/sample_conf/sherpaASRTTS_sense_voice_melo.yaml` (config)
- `doc/sample_conf/sherpaASRTTS_sense_voice_piper_en.yaml` (config)
- `doc/sample_conf/sherpaASRTTS_sense_voice_vits_zh.yaml` (config)
- `doc/sample_conf/sherpaASR_paraformer.yaml` (config)
- `doc/sample_conf/sherpaASR_sense_voice.yaml` (config)
- `dockerfile` (container)
- `live2d-models/mao_pro/runtime/expressions/exp_01.exp3.json` (config)
- `live2d-models/mao_pro/runtime/expressions/exp_02.exp3.json` (config)
- `live2d-models/mao_pro/runtime/expressions/exp_03.exp3.json` (config)
- `live2d-models/mao_pro/runtime/expressions/exp_04.exp3.json` (config)
- `live2d-models/mao_pro/runtime/expressions/exp_05.exp3.json` (config)
- `live2d-models/mao_pro/runtime/expressions/exp_06.exp3.json` (config)
- `live2d-models/mao_pro/runtime/expressions/exp_07.exp3.json` (config)
- `live2d-models/mao_pro/runtime/expressions/exp_08.exp3.json` (config)
- `live2d-models/mao_pro/runtime/mao_pro.cdi3.json` (config)
- `live2d-models/mao_pro/runtime/mao_pro.model3.json` (config)
- `live2d-models/mao_pro/runtime/mao_pro.physics3.json` (config)
- `live2d-models/mao_pro/runtime/mao_pro.pose3.json` (config)
- `live2d-models/mao_pro/runtime/motions/mtn_01.motion3.json` (config)
- `live2d-models/mao_pro/runtime/motions/mtn_02.motion3.json` (config)
- `live2d-models/mao_pro/runtime/motions/mtn_03.motion3.json` (config)
- `live2d-models/mao_pro/runtime/motions/mtn_04.motion3.json` (config)
- `live2d-models/mao_pro/runtime/motions/special_01.motion3.json` (config)
- `live2d-models/mao_pro/runtime/motions/special_02.motion3.json` (config)
- `live2d-models/mao_pro/runtime/motions/special_03.motion3.json` (config)
- `live2d-models/shizuku/runtime/motion/01.motion3.json` (config)
- `live2d-models/shizuku/runtime/motion/02.motion3.json` (config)
- `live2d-models/shizuku/runtime/motion/03.motion3.json` (config)
- `live2d-models/shizuku/runtime/motion/04.motion3.json` (config)
- `live2d-models/shizuku/runtime/shizuku.cdi3.json` (config)
- `live2d-models/shizuku/runtime/shizuku.model3.json` (config)
- `live2d-models/shizuku/runtime/shizuku.physics3.json` (config)
- `live2d-models/shizuku/runtime/shizuku.pose3.json` (config)
- `mcp_servers.json` (config)
- `model_dict.json` (config)
- `pyproject.toml` (manifest)
- `requirements-bilibili.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `src` — 107 analysed file(s)
- `live2d-models` — 29 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `upgrade_codes` — 13 analysed file(s)
- `prompts` — 12 analysed file(s)
- `.github` — 10 analysed file(s)
- `doc` — 6 analysed file(s)
- `characters` — 5 analysed file(s)
- `web_tool` — 4 analysed file(s)
- `config_templates` — 3 analysed file(s)
- `.gemini` — 2 analysed file(s)
- `.cursor` — 1 analysed file(s)
- `backgrounds` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `992309c0aa19845960228f880013d4685fde93b5` is the revision these paths and observations refer to.
