# Project structure: GaiZhenbiao/ChuanhuChatGPT

**Analysed commit:** `2c7d5304c215520dbc6077f185fc45d8e0c8d919`

**Commit reference:** [2c7d5304c215520dbc6077f185fc45d8e0c8d919](https://github.com/GaiZhenbiao/ChuanhuChatGPT/commit/2c7d5304c215520dbc6077f185fc45d8e0c8d919)

**Tree at this commit:** [GaiZhenbiao/ChuanhuChatGPT@2c7d5304c215](https://github.com/GaiZhenbiao/ChuanhuChatGPT/tree/2c7d5304c215520dbc6077f185fc45d8e0c8d919)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | GaiZhenbiao/ChuanhuChatGPT |
| Description | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI. |
| Stars | 15241 |
| Forks | 2178 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `2c7d5304c215520dbc6077f185fc45d8e0c8d919` |
| Retrieved at | 2026-11-14T19:09:06.044543+00:00 |
| Files in this snapshot | 113 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (7 files)
    config.yml
    feature-request.yml
    report-bug.yml
    report-docker.yml
    report-localhost.yml
    report-others.yml
    report-server.yml
  workflows/  (2 files)
    Build_Docker.yml
    Release_docker.yml
  CONTRIBUTING.md
  pull_request_template.md
configs/  (1 files)
  ds_config_chatbot.json
locale/  (8 files)
  en_US.json
  extract_locale.py
  ja_JP.json
  ko_KR.json
  ru_RU.json
  sv_SE.json
  vi_VN.json
  zh_CN.json
modules/  (40 files)
  models/  (28 files)
    Azure.py
    ChatGLM.py
    ChuanhuAgent.py
    Claude.py
    DALLE3.py
    ERNIE.py
    GoogleGemini.py
    GoogleGemma.py
    GooglePaLM.py
    Groq.py
    LLaMA.py
    MOSS.py
    Ollama.py
    OpenAIInstruct.py
    OpenAIVision.py
    Qwen.py
    StableLM.py
    XMChat.py
    __init__.py
    base_model.py
    configuration_moss.py
    inspurai.py
    midjourney.py
    minimax.py
    … 4 more files
  __init__.py
  config.py
  index_func.py
  overwrites.py
  pdf_func.py
  presets.py
  repo.py
  shared.py
  train_func.py
  utils.py
  webui.py
  webui_locale.py
readme/  (4 files)
  README_en.md
  README_ja.md
  README_ko.md
  README_ru.md
templates/  (6 files)
  1 中文提示词.json
  2 English Prompts.csv
  3 繁體提示詞.json
  4 川虎的Prompts.json
  5 日本語Prompts.json
  6 Russian Prompts.json
web_assets/  (31 files)
  html/  (11 files)
    appearance_switcher.html
    billing_info.html
    chatbot_header_btn.html
    chatbot_more.html
    chatbot_placeholder.html
    close_btn.html
    footer.html
    func_nav.html
    header_title.html
    update.html
    web_config.html
  javascript/  (13 files)
    ChuanhuChat.js
    chat-history.js
    chat-list.js
    external-scripts.js
    fake-gradio.js
    file-input.js
    localization.js
    message-button.js
    sliders.js
    updater.js
    user-info.js
    utils.js
    webui.js
  model_logos/  (1 files)
    gemini.svg
  stylesheet/  (5 files)
    ChuanhuChat.css
    chatbot.css
    custom-components.css
    markdown.css
    override-gradio.css
  manifest.json
.gitignore
CITATION.cff
ChuanhuChatbot.py
Dockerfile
LICENSE
README.md
config_example.json
requirements.txt
requirements_advanced.txt
run_Linux.sh
run_Windows.bat
run_macOS.command
```

## Entry points

- [ChuanhuChatbot.py:790](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/2c7d5304c215520dbc6077f185fc45d8e0c8d919/ChuanhuChatbot.py#L790)
- [locale/extract_locale.py:185](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/2c7d5304c215520dbc6077f185fc45d8e0c8d919/locale/extract_locale.py#L185)
- [modules/models/MOSS.py:362](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/2c7d5304c215520dbc6077f185fc45d8e0c8d919/modules/models/MOSS.py#L362)
- [modules/models/models.py:173](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/2c7d5304c215520dbc6077f185fc45d8e0c8d919/modules/models/models.py#L173)
- [modules/pdf_func.py:149](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/2c7d5304c215520dbc6077f185fc45d8e0c8d919/modules/pdf_func.py#L149)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: load_config_to_environ, retrieve_openai_api, retrieve_proxy, update_doc_config. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 26 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Azure_OpenAI_Client, BaseLLMModel, Base_Chat_Langchain_Client, CallbackToIterator, ChatGLM_Client, Chu… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: MOSS_Client. Observed top-level functions: auto_translate, create_new_model, flatten, get_… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 10 file(s) under modules package (observed from repository paths and static analysis). Observed top-level classes: ConfigItem, ConfigType, I18nAuto, SetupWizard, State. Observed top-level functions: _flatten, _lo… |
| web_assets package | library | Observed | Groups 13 file(s) under web_assets package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/report-bug.yml` (config)
- `.github/ISSUE_TEMPLATE/report-docker.yml` (config)
- `.github/ISSUE_TEMPLATE/report-localhost.yml` (config)
- `.github/ISSUE_TEMPLATE/report-others.yml` (config)
- `.github/ISSUE_TEMPLATE/report-server.yml` (config)
- `.github/workflows/Build_Docker.yml` (ci)
- `.github/workflows/Release_docker.yml` (ci)
- `Dockerfile` (container)
- `config_example.json` (config)
- `configs/ds_config_chatbot.json` (config)
- `locale/en_US.json` (config)
- `locale/ja_JP.json` (config)
- `locale/ko_KR.json` (config)
- `locale/ru_RU.json` (config)
- `locale/sv_SE.json` (config)
- `locale/vi_VN.json` (config)
- `locale/zh_CN.json` (config)
- `requirements.txt` (manifest)
- `requirements_advanced.txt` (manifest)
- `templates/1 中文提示词.json` (config)
- `templates/3 繁體提示詞.json` (config)
- `templates/4 川虎的Prompts.json` (config)
- `templates/5 日本語Prompts.json` (config)
- `templates/6 Russian Prompts.json` (config)
- `web_assets/manifest.json` (config)

## Top-level layout

- `modules` — 40 analysed file(s)
- `web_assets` — 31 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 11 analysed file(s)
- `locale` — 8 analysed file(s)
- `templates` — 6 analysed file(s)
- `readme` — 4 analysed file(s)
- `configs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2c7d5304c215520dbc6077f185fc45d8e0c8d919` is the revision these paths and observations refer to.
