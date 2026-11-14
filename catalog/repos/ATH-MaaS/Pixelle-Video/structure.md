# Project structure: ATH-MaaS/Pixelle-Video

**Analysed commit:** `848b054e4fae40dabc62ec58e960b573e83793ac`

**Commit reference:** [848b054e4fae40dabc62ec58e960b573e83793ac](https://github.com/ATH-MaaS/Pixelle-Video/commit/848b054e4fae40dabc62ec58e960b573e83793ac)

**Tree at this commit:** [ATH-MaaS/Pixelle-Video@848b054e4fae](https://github.com/ATH-MaaS/Pixelle-Video/tree/848b054e4fae40dabc62ec58e960b573e83793ac)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ATH-MaaS/Pixelle-Video |
| Description | 🚀 AI 全自动短视频引擎 | AI Fully Automated Short Video Engine |
| Stars | 30101 |
| Forks | 4369 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `848b054e4fae40dabc62ec58e960b573e83793ac` |
| Retrieved at | 2026-11-14T19:07:10.909824+00:00 |
| Files in this snapshot | 244 |

## Directory tree

```text
.devcontainer/  (3 files)
  devcontainer.json
  postCreate.sh
  postStart.sh
.github/  (1 files)
  workflows/  (1 files)
    docs.yml
api/  (27 files)
  routers/  (11 files)
    __init__.py
    content.py
    files.py
    frame.py
    health.py
    image.py
    llm.py
    resources.py
    tasks.py
    tts.py
    video.py
  schemas/  (9 files)
    __init__.py
    base.py
    content.py
    frame.py
    image.py
    llm.py
    resources.py
    tts.py
    video.py
  tasks/  (3 files)
    __init__.py
    manager.py
    models.py
  __init__.py
  app.py
  config.py
  dependencies.py
docs/  (41 files)
  en/  (18 files)
    development/  (2 files)
      … 2 files under this directory
    gallery/  (1 files)
      … 1 files under this directory
    getting-started/  (3 files)
      … 3 files under this directory
    reference/  (2 files)
      … 2 files under this directory
    tutorials/  (3 files)
      … 3 files under this directory
    user-guide/  (4 files)
      … 4 files under this directory
    faq.md
    index.md
    troubleshooting.md
  gallery/  (2 files)
    reading-habit/  (1 files)
      … 1 files under this directory
    index.md
  stylesheets/  (1 files)
    extra.css
  zh/  (18 files)
    development/  (2 files)
      … 2 files under this directory
    gallery/  (1 files)
      … 1 files under this directory
    getting-started/  (3 files)
      … 3 files under this directory
    reference/  (2 files)
      … 2 files under this directory
    tutorials/  (3 files)
      … 3 files under this directory
    user-guide/  (4 files)
      … 4 files under this directory
    faq.md
    index.md
    troubleshooting.md
  FAQ.md
  FAQ_CN.md
packaging/  (6 files)
  windows/  (6 files)
    config/  (1 files)
      … 1 files under this directory
    templates/  (2 files)
      … 2 files under this directory
    README.md
    build.py
    requirements.txt
pixelle_video/  (60 files)
  config/  (4 files)
    __init__.py
    loader.py
    manager.py
    schema.py
  models/  (3 files)
    media.py
    progress.py
    storyboard.py
  pipelines/  (6 files)
    __init__.py
    asset_based.py
    base.py
    custom.py
    linear.py
    standard.py
  prompts/  (8 files)
    __init__.py
    asset_script_generation.py
    content_narration.py
    image_generation.py
    style_conversion.py
    title_generation.py
    topic_narration.py
    video_generation.py
  services/  (27 files)
    api_services/  (13 files)
      … 13 files under this directory
    __init__.py
    api_asset_analysis.py
    api_media.py
    comfy_base_service.py
    frame_html.py
    frame_processor.py
    history_manager.py
    image_analysis.py
    llm_service.py
    media.py
    persistence.py
    tts_service.py
    video.py
    video_analysis.py
  utils/  (8 files)
    __init__.py
    content_generators.py
    llm_util.py
    os_util.py
    prompt_helper.py
    template_util.py
    tts_util.py
    workflow_util.py
  __init__.py
  llm_presets.py
  service.py
  tts_voices.py
templates/  (31 files)
  1080x1080/  (1 files)
    image_minimal_framed.html
  1080x1920/  (25 files)
    asset_default.html
    image_blur_card.html
    image_book.html
    image_cartoon.html
    image_default.html
    image_elegant.html
    image_excerpt.html
    image_fashion_vintage.html
    image_full.html
    image_healing.html
    image_health_preservation.html
    image_life_insights.html
    image_life_insights_light.html
    image_long_text.html
    image_modern.html
    image_neon.html
    image_psychology_card.html
    image_purple.html
    image_satirical_cartoon.html
    image_simple_black.html
    image_simple_line_drawing.html
    static_default.html
    static_excerpt.html
    video_default.html
    … 1 more files
  1920x1080/  (5 files)
    image_book.html
    image_film.html
    image_full.html
    image_ultrawide_minimal.html
    image_wide_darktech.html
web/  (31 files)
  components/  (8 files)
    __init__.py
    content_input.py
    digital_tts_config.py
    faq.py
    header.py
    output_preview.py
    settings.py
    style_config.py
  i18n/  (3 files)
    locales/  (2 files)
      … 2 files under this directory
    __init__.py
  pages/  (3 files)
    1_🎬_Home.py
    2_📚_History.py
    __init__.py
  pipelines/  (8 files)
    __init__.py
    action_transfer.py
    api_workflows.py
    asset_based.py
    base.py
    digital_human.py
    i2v.py
    standard.py
  state/  (2 files)
    __init__.py
    session.py
  utils/  (5 files)
    __init__.py
    async_helpers.py
    batch_manager.py
    history_persistence.py
    streamlit_helpers.py
  __init__.py
  app.py
workflows/  (29 files)
  runninghub/  (21 files)
    af_scail.json
    analyse_image.json
    digital_combination.json
    digital_customize.json
    digital_image.json
    i2v_LTX2.json
    image_Z-image.json
    image_flux.json
    image_flux2.json
    image_qwen.json
    image_qwen_chinese_cartoon.json
    image_sd3.5.json
    image_sdxl.json
    tts_edge.json
    tts_index2.json
    tts_spark.json
    video_Z_image_wan2.2.json
    video_qwen_wan2.2.json
    video_understanding.json
    video_wan2.1_fusionx.json
    video_wan2.2.json
  selfhost/  (8 files)
    analyse_image.json
    analyse_video.json
    image_flux.json
    image_nano_banana.json
    image_qwen.json
    tts_edge.json
    tts_index2.json
    video_wan2.1_fusionx.json
.dockerignore
.gitignore
Dockerfile
LICENSE
NOTICE
README.md
README_EN.md
config.example.yaml
docker-compose.yml
docker-start.sh
mkdocs.yml
pyproject.toml
requirements-docs.txt
start_web.bat
start_web.sh
```

## Entry points

- [api/app.py:82](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/api/app.py#L82)
- [packaging/windows/build.py:689](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/packaging/windows/build.py#L689)
- [pixelle_video/services/api_services/image_dashscope.py:192](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/pixelle_video/services/api_services/image_dashscope.py#L192)
- [pixelle_video/services/api_services/image_gpt.py:148](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/pixelle_video/services/api_services/image_gpt.py#L148)
- [pixelle_video/services/api_services/image_seedream.py:247](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/pixelle_video/services/api_services/image_seedream.py#L247)
- [pixelle_video/services/api_services/video_dashscope.py:570](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/pixelle_video/services/api_services/video_dashscope.py#L570)
- [pixelle_video/services/api_services/video_kling.py:407](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/pixelle_video/services/api_services/video_kling.py#L407)
- [pixelle_video/services/api_services/video_seedance.py:179](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/pixelle_video/services/api_services/video_seedance.py#L179)
- [pixelle_video/services/api_services/vlm_dashscope.py:83](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/pixelle_video/services/api_services/vlm_dashscope.py#L83)
- [web/app.py:61](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/web/app.py#L61)
- [web/pages/1_🎬_Home.py:87](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/web/pages/1_%F0%9F%8E%AC_Home.py#L87)
- [web/pages/2_📚_History.py:465](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/web/pages/2_%F0%9F%93%9A_History.py#L465)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 26 file(s) under api layer (observed from repository paths and static analysis). Observed routes: POST /narration, POST /image-prompt, POST /title, GET /{file_path:path}, POST /render. Observed top-level classes:… |
| Configuration and deployment | config | Observed | Groups 45 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: APIKeyProviderConfig, APIProviderCommonConfig, APIProvidersConfig, AccessSecretProvi… |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: ContentMetadata, MediaResult, ProgressEvent, Storyboard, StoryboardConfig, StoryboardFrame. |
| Application entry point | entrypoint | Observed | Groups 12 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /. Observed top-level classes: Color, DashScope… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: ImageClient, VLM, VideoClient. |
| pixelle_video package | library | Observed | Groups 25 file(s) under pixelle_video package (observed from repository paths and static analysis). Observed top-level classes: AssetBasedPipeline, BasePipeline, CustomPipeline, LinearVideoPipeline, PipelineContext, Sce… |
| Service / domain layer | service | Observed | Groups 17 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: APIAssetAnalysisService, APIProviderMediaService, ComfyBaseService, FrameProcessor, HTMLFr… |
| web package | library | Observed | Groups 25 file(s) under web package (observed from repository paths and static analysis). Observed top-level classes: ActionTransferPipelineUI, AssetBasedPipelineUI, DigitalHumanPipelineUI, ImageToVideoPipelineUI, Pipel… |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.github/workflows/docs.yml` (ci)
- `Dockerfile` (container)
- `config.example.yaml` (config)
- `docker-compose.yml` (container)
- `mkdocs.yml` (config)
- `packaging/windows/config/build_config.yaml` (config)
- `packaging/windows/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `requirements-docs.txt` (manifest)
- `web/i18n/locales/en_US.json` (config)
- `web/i18n/locales/zh_CN.json` (config)
- `workflows/runninghub/af_scail.json` (config)
- `workflows/runninghub/analyse_image.json` (config)
- `workflows/runninghub/digital_combination.json` (config)
- `workflows/runninghub/digital_customize.json` (config)
- `workflows/runninghub/digital_image.json` (config)
- `workflows/runninghub/i2v_LTX2.json` (config)
- `workflows/runninghub/image_Z-image.json` (config)
- `workflows/runninghub/image_flux.json` (config)
- `workflows/runninghub/image_flux2.json` (config)
- `workflows/runninghub/image_qwen.json` (config)
- `workflows/runninghub/image_qwen_chinese_cartoon.json` (config)
- `workflows/runninghub/image_sd3.5.json` (config)
- `workflows/runninghub/image_sdxl.json` (config)
- `workflows/runninghub/tts_edge.json` (config)
- `workflows/runninghub/tts_index2.json` (config)
- `workflows/runninghub/tts_spark.json` (config)
- `workflows/runninghub/video_Z_image_wan2.2.json` (config)
- `workflows/runninghub/video_qwen_wan2.2.json` (config)
- `workflows/runninghub/video_understanding.json` (config)
- `workflows/runninghub/video_wan2.1_fusionx.json` (config)
- `workflows/runninghub/video_wan2.2.json` (config)
- `workflows/selfhost/analyse_image.json` (config)
- `workflows/selfhost/analyse_video.json` (config)
- `workflows/selfhost/image_flux.json` (config)
- `workflows/selfhost/image_nano_banana.json` (config)
- `workflows/selfhost/image_qwen.json` (config)
- `workflows/selfhost/tts_edge.json` (config)
- `workflows/selfhost/tts_index2.json` (config)
- `workflows/selfhost/video_wan2.1_fusionx.json` (config)

## Top-level layout

- `pixelle_video` — 60 analysed file(s)
- `docs` — 41 analysed file(s)
- `templates` — 31 analysed file(s)
- `web` — 31 analysed file(s)
- `workflows` — 29 analysed file(s)
- `api` — 27 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `packaging` — 6 analysed file(s)
- `.devcontainer` — 3 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `848b054e4fae40dabc62ec58e960b573e83793ac` is the revision these paths and observations refer to.
