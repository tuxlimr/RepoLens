# Project structure: linyqh/NarratoAI

**Analysed commit:** `29a11b6cdf61b69ba90321fc5babc160e0ca2657`

**Commit reference:** [29a11b6cdf61b69ba90321fc5babc160e0ca2657](https://github.com/linyqh/NarratoAI/commit/29a11b6cdf61b69ba90321fc5babc160e0ca2657)

**Tree at this commit:** [linyqh/NarratoAI@29a11b6cdf61](https://github.com/linyqh/NarratoAI/tree/29a11b6cdf61b69ba90321fc5babc160e0ca2657)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | linyqh/NarratoAI |
| Description | 利用 AI 大模型，一键解说并剪辑视频 |
| Stars | 11825 |
| Forks | 1620 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `29a11b6cdf61b69ba90321fc5babc160e0ca2657` |
| Retrieved at | 2026-11-14T19:10:22.674939+00:00 |
| Files in this snapshot | 178 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (3 files)
    auto-release-generator.yml
    codeReview.yml
    discord-release-notification.yml
  pull_request_template.md
  release-drafter.yml
app/  (117 files)
  config/  (6 files)
    __init__.py
    audio_config.py
    config.py
    defaults.py
    ffmpeg_config.py
    test_config_bootstrap_unittest.py
  models/  (4 files)
    __init__.py
    const.py
    exception.py
    schema.py
  services/  (97 files)
    SDE/  (1 files)
      … 1 files under this directory
    SDP/  (5 files)
      … 5 files under this directory
    documentary/  (3 files)
      … 3 files under this directory
    llm/  (16 files)
      … 16 files under this directory
    prompts/  (28 files)
      … 28 files under this directory
    __init__.py
    audio_merger.py
    audio_normalizer.py
    clip_video.py
    fun_asr_subtitle.py
    generate_narration_script.py
    generate_video.py
    jianying_draft_builder.py
    jianying_task.py
    llm.py
    material.py
    merger_video.py
    script_service.py
    script_subtitle.py
    short_drama_narration_validation.py
    sonilo.py
    state.py
    subtitle.py
    subtitle_corrector.py
    subtitle_merger.py
    subtitle_text.py
    subtitle_translator.py
    task.py
    tavily_search.py
    … 20 more files
  utils/  (9 files)
    check_script.py
    ffmpeg_detector.py
    ffmpeg_utils.py
    openai_base_url_security.py
    qwenvl_analyzer.py
    script_generator.py
    test_ffmpeg_detector_unittest.py
    utils.py
    video_processor.py
  __init__.py
resource/  (6 files)
  fonts/  (1 files)
    fonts_in_here.txt
  public/  (1 files)
    index.html
  scripts/  (1 files)
    script_in_here.txt
  songs/  (1 files)
    song_in_here.txt
  srt/  (1 files)
    srt_in_here.txt
  videos/  (1 files)
    video_in_here.txt
tests/  (8 files)
  test_documentary_frame_analysis_service.py
  test_generate_narration_script_documentary_unittest.py
  test_generate_script_docu_unittest.py
  test_script_service_documentary_unittest.py
  test_sonilo_bgm_unittest.py
  test_sonilo_sfx_unittest.py
  test_streamlit_widget_session_state.py
  test_video_processor_documentary_unittest.py
webui/  (25 files)
  components/  (11 files)
    __init__.py
    audio_settings.py
    basic_settings.py
    ffmpeg_diagnostics.py
    script_settings.py
    subtitle_settings.py
    system_settings.py
    test_audio_settings_unittest.py
    test_subtitle_settings_unittest.py
    test_system_settings_unittest.py
    video_settings.py
  config/  (1 files)
    settings.py
  i18n/  (3 files)
    __init__.py
    en.json
    zh.json
  tools/  (6 files)
    base.py
    generate_script_docu.py
    generate_script_short.py
    generate_short_summary.py
    test_generate_script_short_unittest.py
    test_generate_short_summary_unittest.py
  utils/  (3 files)
    cache.py
    file_utils.py
    vision_analyzer.py
  __init__.py
.dockerignore
.gitignore
.python-version
Dockerfile
LICENSE
Makefile
README-en.md
README.md
config.example.toml
conftest.py
docker-compose.yml
docker-deploy.sh
docker-entrypoint.sh
project_version
pyproject.toml
requirements.txt
webui.py
```

## Entry points

- [app/config/audio_config.py:208](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/config/audio_config.py#L208)
- [app/services/SDE/short_drama_explanation.py:1066](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/SDE/short_drama_explanation.py#L1066)
- [app/services/audio_merger.py:137](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/audio_merger.py#L137)
- [app/services/audio_normalizer.py:305](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/audio_normalizer.py#L305)
- [app/services/clip_video.py:1180](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/clip_video.py#L1180)
- [app/services/generate_narration_script.py:231](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/generate_narration_script.py#L231)
- [app/services/generate_video.py:1824](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/generate_video.py#L1824)
- [app/services/llm.py:790](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/llm.py#L790)
- [app/services/merger_video.py:830](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/merger_video.py#L830)
- [app/services/subtitle.py:434](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/subtitle.py#L434)
- [app/services/subtitle_merger.py:188](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/subtitle_merger.py#L188)
- [app/services/task.py:1040](https://github.com/linyqh/NarratoAI/blob/29a11b6cdf61b69ba90321fc5babc160e0ca2657/app/services/task.py#L1040)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 8 file(s) under app package (observed from repository paths and static analysis). Observed top-level classes: BaseGenerator, DeepSeekGenerator, FFmpegEngine, GeminiGenerator, GeminiOpenAIGenerator, MoonshotGenera… |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: FFmpegConfigManager, FFmpegProfile, WebUIConfig. Observed top-level functions: __ini… |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AudioVolumeDefaults, FileNotFoundException, HttpException, MaterialInfo, SubtitlePosition, VideoAspect. |
| Application entry point | entrypoint | Observed | Groups 16 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AudioConfig, AudioNormalizer, SubtitleAnalyzer, VideoAspect, VideoProcessor. Observed top… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 66 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: APICallError, AuthenticationError, BaseLLMProvider, BasePrompt, BaseState, Commentary. Obs… |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ApplySfxTests, ApplySoniloSfxTaskTests, AudioSettingsSourcePillsTests, ConfigBootstrapDefaultsTests, Consum… |
| webui package | library | Observed | Groups 16 file(s) under webui package (observed from repository paths and static analysis). Observed top-level classes: VisionAnalyzer. Observed top-level functions: _build_combined_subtitle_content, _build_plot_analysi… |

## Important files

- `.dockerignore` (container)
- `.github/release-drafter.yml` (config)
- `.github/workflows/auto-release-generator.yml` (ci)
- `.github/workflows/codeReview.yml` (ci)
- `.github/workflows/discord-release-notification.yml` (ci)
- `Dockerfile` (container)
- `config.example.toml` (config)
- `docker-compose.yml` (container)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `webui/i18n/en.json` (config)
- `webui/i18n/zh.json` (config)

## Top-level layout

- `app` — 117 analysed file(s)
- `webui` — 25 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `tests` — 8 analysed file(s)
- `resource` — 6 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `29a11b6cdf61b69ba90321fc5babc160e0ca2657` is the revision these paths and observations refer to.
