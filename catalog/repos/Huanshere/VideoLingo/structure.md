# Project structure: Huanshere/VideoLingo

**Analysed commit:** `d2d5a046d97526ae4950294cc5663ad520b22f52`

**Commit reference:** [d2d5a046d97526ae4950294cc5663ad520b22f52](https://github.com/Huanshere/VideoLingo/commit/d2d5a046d97526ae4950294cc5663ad520b22f52)

**Tree at this commit:** [Huanshere/VideoLingo@d2d5a046d975](https://github.com/Huanshere/VideoLingo/tree/d2d5a046d97526ae4950294cc5663ad520b22f52)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Huanshere/VideoLingo |
| Description | Netflix-level subtitle cutting, translation, alignment, and even dubbing - one-click fully automated AI video subtitle team | Netflix级字幕切割、翻译、对齐、甚至加上配音，一键全自动视频搬运AI字幕组 |
| Stars | 19251 |
| Forks | 2126 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `d2d5a046d97526ae4950294cc5663ad520b22f52` |
| Retrieved at | 2026-11-14T19:08:15.566598+00:00 |
| Files in this snapshot | 212 |

## Directory tree

```text
.streamlit/  (1 files)
  config.toml
core/  (64 files)
  asr_backend/  (9 files)
    __init__.py
    audio_preprocess.py
    demucs_vl.py
    elevenlabs_asr.py
    mai_asr.py
    qwen_asr_local.py
    speech_edges.py
    transcription_cache.py
    whisperX_local.py
  spacy_utils/  (6 files)
    __init__.py
    load_nlp_model.py
    split_by_comma.py
    split_by_connector.py
    split_by_mark.py
    split_long_by_root.py
  st_utils/  (5 files)
    __init__.py
    download_video_section.py
    imports_and_utils.py
    sidebar_setting.py
    tts_settings.py
  tts_backend/  (10 files)
    _302_f5tts.py
    custom_tts.py
    edge_tts.py
    estimate_duration.py
    fish_audio_tts.py
    gpt_sovits_tts.py
    openai_tts.py
    sf_cosyvoice2.py
    sf_fishtts.py
    tts_main.py
  utils/  (13 files)
    __init__.py
    ask_gpt.py
    config_utils.py
    decorator.py
    delete_retry_dubbing.py
    models.py
    onekeycleanup.py
    pypi_autochoose.py
    subtitle_fonts.py
    subtitle_style.py
    subtitle_width.py
    task_literals.py
    typeset.py
  _10_gen_audio.py
  _11_merge_audio.py
  _12_dub_to_vid.py
  _1_ytdlp.py
  _2_asr.py
  _2_import_subtitles.py
  _3_1_split_nlp.py
  _3_2_split_meaning.py
  _4_1_summarize.py
  _4_2_translate.py
  _5_split_sub.py
  _6_gen_sub.py
  _7_sub_into_vid.py
  _8_1_audio_task.py
  _8_2_dub_chunks.py
  _9_refer_audio.py
  __init__.py
  pipeline.py
  prompts.py
  task_runner.py
  translate_lines.py
docs/  (58 files)
  components/  (13 files)
    landing/  (6 files)
      … 6 files under this directory
    ui/  (7 files)
      … 7 files under this directory
  lib/  (1 files)
    utils.ts
  pages/  (21 files)
    docs/  (13 files)
      … 13 files under this directory
    _app.mdx
    _meta.en-US.json
    _meta.ja.json
    _meta.zh-CN.json
    globals.css
    index.en-US.mdx
    index.ja.mdx
    index.zh-CN.mdx
  public/  (2 files)
    favicon.svg
    site.webmanifest
  .gitignore
  api.md
  audio-extract-quality.md
  audio-timeline.md
  components.json
  deployment-versions.md
  download-network.md
  dubbing-loudness.md
  ffmpeg-runtime.md
  logo.svg
  middleware.js
  next-env.d.ts
  next.config.js
  package.json
  postcss.config.js
  runtime-compatibility.md
  runtime-dependencies.md
  tailwind.config.js
  theme.config.jsx
  transcription-cache.md
  tsconfig.json
fonts/  (24 files)
  licenses/  (24 files)
    OFL-NotoSans.txt
    OFL-NotoSansArabic.txt
    OFL-NotoSansBengali.txt
    OFL-NotoSansDevanagari.txt
    OFL-NotoSansGujarati.txt
    OFL-NotoSansGurmukhi.txt
    OFL-NotoSansHK.txt
    OFL-NotoSansHebrew.txt
    OFL-NotoSansJP.txt
    OFL-NotoSansKannada.txt
    OFL-NotoSansKhmer.txt
    OFL-NotoSansLao.txt
    OFL-NotoSansMalayalam.txt
    OFL-NotoSansMyanmar.txt
    OFL-NotoSansOriya.txt
    OFL-NotoSansSC.txt
    OFL-NotoSansSinhala.txt
    OFL-NotoSansTC.txt
    OFL-NotoSansTamil.txt
    OFL-NotoSansTelugu.txt
    OFL-NotoSansThai.txt
    OFL-Pretendard.txt
    OFL-Roboto.txt
    README.md
scripts/  (2 files)
  build_subtitle_fonts.py
  streamlit-log.ps1
tests/  (30 files)
  __init__.py
  test_api.py
  test_asr_runtime.py
  test_audio_extract_quality.py
  test_audio_timeline.py
  test_backlog_fixes.py
  test_demucs_vl.py
  test_dependencies.py
  test_download_proxy.py
  test_dubbing_loudness.py
  test_estimate_duration.py
  test_ffmpeg_runtime.py
  test_fish_audio_tts.py
  test_language_support.py
  test_mai_asr.py
  test_pipeline_integration.py
  test_qwen_asr_local.py
  test_runtime_compatibility.py
  test_sf_fishtts.py
  test_source_language.py
  test_speech_edges.py
  test_subtitle_burn.py
  test_subtitle_fonts.py
  test_subtitle_split.py
  … 6 more files
translations/  (14 files)
  README.es.md
  README.fr.md
  README.ja.md
  README.ru.md
  README.zh-TW.md
  README.zh.md
  en.json
  es.json
  fr.json
  ja.json
  ru.json
  translations.py
  zh-CN.json
  zh-HK.json
.cursorrules
.dockerignore
.gitignore
Dockerfile
LICENSE
OneKeyStart.bat
README.md
VideoLingo_colab.ipynb
api.py
config.yaml
install.py
installer.py
launch.py
requirements.txt
runtime_libraries.py
setup.py
setup_env.py
st.py
start.py
```

## Entry points

- [api.py:28](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/api.py#L28)
- [core/_10_gen_audio.py:280](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_10_gen_audio.py#L280)
- [core/_11_merge_audio.py:145](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_11_merge_audio.py#L145)
- [core/_12_dub_to_vid.py:118](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_12_dub_to_vid.py#L118)
- [core/_1_ytdlp.py:170](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_1_ytdlp.py#L170)
- [core/_2_asr.py:129](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_2_asr.py#L129)
- [core/_3_1_split_nlp.py:14](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_3_1_split_nlp.py#L14)
- [core/_3_2_split_meaning.py:160](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_3_2_split_meaning.py#L160)
- [core/_4_1_summarize.py:72](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_4_1_summarize.py#L72)
- [core/_4_2_translate.py:118](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_4_2_translate.py#L118)
- [core/_5_split_sub.py:181](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_5_split_sub.py#L181)
- [core/_6_gen_sub.py:193](https://github.com/Huanshere/VideoLingo/blob/d2d5a046d97526ae4950294cc5663ad520b22f52/core/_6_gen_sub.py#L193)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: check_whisperx_runtime, configure_ffmpeg, configure_ffmpeg_dlls, validate_ffmpeg. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 45 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: POST /input, POST /run, GET /status, POST /resume,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 26 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: StopTask, TaskRunner, _NumpyNumbers. Observed top-level functions: __getattr__, _align, _a… |
| Tests | test | Observed | Groups 30 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Clock, FindVideoFilesTests, LayoutTests, LineTests, LocalBackendTests, MaiAsrTests. Observed top-level func… |
| translations package | library | Observed | Groups 1 file(s) under translations package (observed from repository paths and static analysis). Observed top-level functions: _config_language, _language_from_accept_language, _streamlit_language, get_current_language… |

## Important files

- `.dockerignore` (container)
- `.streamlit/config.toml` (config)
- `Dockerfile` (container)
- `config.yaml` (config)
- `docs/components.json` (config)
- `docs/package.json` (manifest)
- `docs/pages/_meta.en-US.json` (config)
- `docs/pages/_meta.ja.json` (config)
- `docs/pages/_meta.zh-CN.json` (config)
- `docs/pages/docs/_meta.en-US.json` (config)
- `docs/pages/docs/_meta.ja.json` (config)
- `docs/pages/docs/_meta.zh-CN.json` (config)
- `docs/tsconfig.json` (config)
- `requirements.txt` (manifest)
- `setup.py` (manifest)
- `translations/en.json` (config)
- `translations/es.json` (config)
- `translations/fr.json` (config)
- `translations/ja.json` (config)
- `translations/ru.json` (config)
- `translations/zh-CN.json` (config)
- `translations/zh-HK.json` (config)

## Top-level layout

- `core` — 64 analysed file(s)
- `docs` — 58 analysed file(s)
- `tests` — 30 analysed file(s)
- `fonts` — 24 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `translations` — 14 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.streamlit` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d2d5a046d97526ae4950294cc5663ad520b22f52` is the revision these paths and observations refer to.
