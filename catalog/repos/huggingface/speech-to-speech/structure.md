# Project structure: huggingface/speech-to-speech

**Analysed commit:** `d1dc31deab44510188ffcd7edfc87203ed9077fb`

**Commit reference:** [d1dc31deab44510188ffcd7edfc87203ed9077fb](https://github.com/huggingface/speech-to-speech/commit/d1dc31deab44510188ffcd7edfc87203ed9077fb)

**Tree at this commit:** [huggingface/speech-to-speech@d1dc31deab44](https://github.com/huggingface/speech-to-speech/tree/d1dc31deab44510188ffcd7edfc87203ed9077fb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | huggingface/speech-to-speech |
| Description | Build voice agents with open-source models |
| Stars | 13693 |
| Forks | 1693 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `d1dc31deab44510188ffcd7edfc87203ed9077fb` |
| Retrieved at | 2026-11-14T19:09:43.694232+00:00 |
| Files in this snapshot | 428 |

## Directory tree

```text
.github/  (6 files)
  scripts/  (1 files)
    star_history.py
  workflows/  (4 files)
    ci.yml
    omnivoice.yml
    publish.yml
    star-history.yml
  dependabot.yml
archive/  (10 files)
  STT/  (2 files)
    __init__.py
    moonshine_handler.py
  TTS/  (3 files)
    __init__.py
    melo_handler.py
    parler_handler.py
  arguments_classes/  (3 files)
    __init__.py
    melo_tts_arguments.py
    parler_tts_arguments.py
  README.md
  __init__.py
assets/  (1 files)
  star-history.svg
demo/  (47 files)
  docs/  (1 files)
    adr/  (1 files)
      … 1 files under this directory
  livekit/  (3 files)
    README.md
    agent.py
    requirements.txt
  tests/  (17 files)
    agents-adapter.test.mjs
    agents-webrtc.test.mjs
    agents-websocket.test.mjs
    conversation-language-ui.test.mjs
    conversation-language.test.mjs
    error-message.test.mjs
    helpers.mjs
    interrupted-reply-ui.test.mjs
    local-vad-browser.test.mjs
    local-vad.test.mjs
    playback-helpers.mjs
    playback-sdk.test.mjs
    playback.test.mjs
    reasoning-ui.test.mjs
    turn-latency-ui.test.mjs
    turn-latency.test.mjs
    visemes.test.mjs
  ui/  (4 files)
    account.js
    chat.js
    dom.js
    reasoning.js
  worklets/  (2 files)
    audio-playback.js
    mic-capture.js
  ws/  (4 files)
    codec.js
    local-vad.js
    orb-visualizer.js
    user-audio-recorder.js
  .dockerignore
  .gitignore
  CONTEXT.md
  DESIGN.md
  Dockerfile
  README.md
  auth.py
  index.html
  limiter.py
  main.js
  package.json
  requirements.txt
  s2s-realtime-client.js
  server.py
  style.css
  turn-latency.js
docs/  (8 files)
  releases/  (2 files)
    v1.0.0.md
    v1.1.0.md
  configuration.md
  echo-cancellation.md
  openai-compatible-stt.md
  openai-compatible-tts.md
  response-latency.md
  vibe-checks.md
example_configs/  (1 files)
  mac.yaml
examples/  (4 files)
  gemma4-12b-macos/  (1 files)
    README.md
  streaming-diarization/  (1 files)
    README.md
  realtime_web_search_tool.py
  realtime_youcom_search_tool.py
scripts/  (5 files)
  benchmark_stt.py
  benchmark_tts.py
  check_pocket_tts_farsi.py
  prepare_eval_space.py
  synthetic_conversation_realtime_client.py
src/  (180 files)
  speech_to_speech/  (180 files)
    LLM/  (18 files)
      … 18 files under this directory
    STT/  (18 files)
      … 18 files under this directory
    STV/  (4 files)
      … 4 files under this directory
    TTS/  (19 files)
      … 19 files under this directory
    VAD/  (6 files)
      … 6 files under this directory
    api/  (26 files)
      … 26 files under this directory
    arguments_classes/  (36 files)
      … 36 files under this directory
    diarization/  (3 files)
      … 3 files under this directory
    evals/  (12 files)
      … 12 files under this directory
    pipeline/  (16 files)
      … 16 files under this directory
    utils/  (5 files)
      … 5 files under this directory
    zerogpu/  (7 files)
      … 7 files under this directory
    __init__.py
    _config_yaml.py
    backend_registry.py
    baseHandler.py
    cli.py
    config.py
    configured_runtime.py
    language_codes.py
    s2s_pipeline.py
    speech_languages.py
tests/  (155 files)
  evals/  (11 files)
    __init__.py
    conftest.py
    test_big_bench_audio_cli.py
    test_big_bench_audio_dataset.py
    test_big_bench_audio_hub.py
    test_big_bench_audio_job.py
    test_big_bench_audio_judge.py
    test_big_bench_audio_report.py
    test_big_bench_audio_runner.py
    test_big_bench_audio_scoring.py
    test_prepare_eval_space.py
  openai_realtime/  (31 files)
    __init__.py
    agents_sdk_server.py
    conftest.py
    realtime_contract.py
    test_audio_client.py
    test_conversation_delete.py
    test_conversation_retrieve.py
    test_create_response.py
    test_input_resampler.py
    test_interrupted_playback_history.py
    test_kitten_latency_finalization.py
    test_llm_proxy.py
    test_openai_client.py
    test_output_resampling.py
    test_pipeline_builder.py
    test_realtime_protocol_contract.py
    test_reasoning_effort.py
    test_reasoning_text.py
    test_response_input_identity.py
    test_runtime_config.py
    test_send_loop_wakeup.py
    test_server_turn_latency.py
    test_speaker_conversation.py
    test_speculative_turn_protocol.py
    … 7 more files
  tool_call/  (3 files)
    __init__.py
    test_function_parser.py
    test_signature_from_schema.py
  __init__.py
  install_smoke.py
  llm_history.py
  reopen_dispatch.py
  test_audio_input_notifier.py
  test_auto_language_spelling.py
  test_backend_registry.py
  test_base_tts_handler.py
  test_chat.py
  test_chat_completions_backend.py
  test_chat_turn_order.py
  test_chattts_streaming.py
  test_chattts_tts_latency.py
  test_cli_defaults.py
  test_config.py
  test_configured_runtime.py
  test_conversation_output.py
  test_demo_agents_adapter.py
  test_demo_input_transcription.py
  test_demo_server.py
  test_demo_user_audio.py
  test_device.py
  test_diarization_transformers.py
  test_diarization_worker.py
  … 86 more files
.dockerignore
.gitignore
AGENTS.md
Dockerfile
Dockerfile.arm64
LICENSE
MANIFEST.in
README.md
docker-compose.yml
mypy.ini
pyproject.toml
```

## Entry points

- [src/speech_to_speech/STT/smart_progressive_streaming.py:342](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/src/speech_to_speech/STT/smart_progressive_streaming.py#L342)
- [src/speech_to_speech/api/openai_realtime/websocket_router.py:623](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/src/speech_to_speech/api/openai_realtime/websocket_router.py#L623)
- [src/speech_to_speech/cli.py](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/src/speech_to_speech/cli.py)
- [src/speech_to_speech/evals/big_bench_audio/__main__.py:386](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/src/speech_to_speech/evals/big_bench_audio/__main__.py#L386)
- [src/speech_to_speech/evals/big_bench_audio/job.py:79](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/src/speech_to_speech/evals/big_bench_audio/job.py#L79)
- [src/speech_to_speech/s2s_pipeline.py:918](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/src/speech_to_speech/s2s_pipeline.py#L918)
- [.github/scripts/star_history.py:193](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/.github/scripts/star_history.py#L193)
- [demo/livekit/agent.py:56](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/demo/livekit/agent.py#L56)
- [demo/server.py:150](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/demo/server.py#L150)
- [scripts/benchmark_stt.py:384](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/scripts/benchmark_stt.py#L384)
- [scripts/benchmark_tts.py:414](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/scripts/benchmark_tts.py#L414)
- [scripts/check_pocket_tts_farsi.py:123](https://github.com/huggingface/speech-to-speech/blob/d1dc31deab44510188ffcd7edfc87203ed9077fb/scripts/check_pocket_tts_farsi.py#L123)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 23 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: ArrowDecoder, AudioHandler, ConnState, ConversationHandler, EchoCanceller, GlobalUsageMetrics. Observed… |
| archive package | library | Observed | Groups 9 file(s) under archive package (observed from repository paths and static analysis). Observed top-level classes: MeloTTSHandler, MeloTTSHandlerArguments, MoonshineSTTHandler, ParlerTTSHandler, ParlerTTSHandlerAr… |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigDocument, ConfigurationError, ResolvedConfig, ResolvedPipeline, ResolvedStage.… |
| demo package | library | Observed | Groups 15 file(s) under demo package (observed from repository paths and static analysis). Observed top-level functions: _add, _client_ip, _connect, _field, _oauth_token, _oauth_token_expired. |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /vendor/openai-realtime-agents.umd.js, GET /ven… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| speech_to_speech package | library | Observed | Groups 141 file(s) under speech_to_speech package (observed from repository paths and static analysis). Observed top-level classes: AssistantMessage, AssistantOutputEvent, AssistantReasoningPart, AssistantResponseDoneEv… |
| Tests | test | Observed | Groups 172 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Connection, ControlledOperation, FakeApi, FakeArguments, FakeAsyncClient, FakeDiarizer. Observed top-level… |

## Important files

- `.dockerignore` (container)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/omnivoice.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/star-history.yml` (ci)
- `Dockerfile` (container)
- `Dockerfile.arm64` (container)
- `MANIFEST.in` (manifest)
- `demo/.dockerignore` (container)
- `demo/Dockerfile` (container)
- `demo/livekit/requirements.txt` (manifest)
- `demo/package.json` (manifest)
- `demo/requirements.txt` (manifest)
- `docker-compose.yml` (container)
- `example_configs/mac.yaml` (config)
- `mypy.ini` (config)
- `pyproject.toml` (manifest)
- `src/speech_to_speech/STV/phoneme_viseme_map.json` (config)
- `src/speech_to_speech/evals/big_bench_audio/Dockerfile.eval` (container)

## Top-level layout

- `src` — 180 analysed file(s)
- `tests` — 155 analysed file(s)
- `demo` — 47 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `archive` — 10 analysed file(s)
- `docs` — 8 analysed file(s)
- `.github` — 6 analysed file(s)
- `scripts` — 5 analysed file(s)
- `examples` — 4 analysed file(s)
- `assets` — 1 analysed file(s)
- `example_configs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d1dc31deab44510188ffcd7edfc87203ed9077fb` is the revision these paths and observations refer to.
