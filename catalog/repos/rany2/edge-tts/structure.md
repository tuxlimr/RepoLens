# Project structure: rany2/edge-tts

**Analysed commit:** `bd44c1d1aaebdc1db7f47456ee12431b42ec7cac`

**Commit reference:** [bd44c1d1aaebdc1db7f47456ee12431b42ec7cac](https://github.com/rany2/edge-tts/commit/bd44c1d1aaebdc1db7f47456ee12431b42ec7cac)

**Tree at this commit:** [rany2/edge-tts@bd44c1d1aaeb](https://github.com/rany2/edge-tts/tree/bd44c1d1aaebdc1db7f47456ee12431b42ec7cac)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | rany2/edge-tts |
| Description | Use Microsoft Edge's online text-to-speech service from Python WITHOUT needing Microsoft Edge |
| Stars | 12541 |
| Forks | 1185 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `bd44c1d1aaebdc1db7f47456ee12431b42ec7cac` |
| Retrieved at | 2026-11-14T19:10:04.392758+00:00 |
| Files in this snapshot | 42 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (2 files)
    code-quality.yml
    codeql-analysis.yml
  FUNDING.yml
  dependabot.yml
examples/  (6 files)
  async_audio_gen_with_dynamic_voice_selection.py
  async_audio_gen_with_predefined_voice.py
  async_audio_streaming_with_predefined_voice_and_subtitles.py
  sync_audio_gen_with_predefined_voice.py
  sync_audio_streaming_with_predefined_voice_subtitles.py
  sync_audio_streaming_with_predefined_voice_subtitles_print2stdout.py
src/  (20 files)
  edge_playback/  (5 files)
    __init__.py
    __main__.py
    py.typed
    util.py
    win32_playback.py
  edge_tts/  (15 files)
    __init__.py
    __main__.py
    communicate.py
    constants.py
    data_classes.py
    drm.py
    exceptions.py
    progress.py
    py.typed
    srt_composer.py
    submaker.py
    typing.py
    util.py
    version.py
    voices.py
.gitignore
.isort.cfg
LICENSE
README.md
build_and_publish.sh
format.sh
gpl-3.0.txt
lint.sh
mypy.ini
pylintrc
setup.cfg
setup.py
```

## Entry points

- [src/edge_playback/__main__.py:132](https://github.com/rany2/edge-tts/blob/bd44c1d1aaebdc1db7f47456ee12431b42ec7cac/src/edge_playback/__main__.py#L132)
- [src/edge_tts/__main__.py:5](https://github.com/rany2/edge-tts/blob/bd44c1d1aaebdc1db7f47456ee12431b42ec7cac/src/edge_tts/__main__.py#L5)
- [src/edge_tts/util.py:187](https://github.com/rany2/edge-tts/blob/bd44c1d1aaebdc1db7f47456ee12431b42ec7cac/src/edge_tts/util.py#L187)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| edge_playback package | library | Observed | Groups 3 file(s) under edge_playback package (observed from repository paths and static analysis). Observed top-level functions: play_mp3_win32, pr_err. |
| edge_tts package | library | Observed | Groups 12 file(s) under edge_tts package (observed from repository paths and static analysis). Observed top-level classes: Communicate, CommunicateState, DRM, EdgeTTSException, NoAudioReceived, ProgressBar. Observed top… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _check_deps, _cleanup, _create_temp_files, _main, _parse_args, _play_media. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/code-quality.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.isort.cfg` (config)
- `mypy.ini` (config)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `src` — 20 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `examples` — 6 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bd44c1d1aaebdc1db7f47456ee12431b42ec7cac` is the revision these paths and observations refer to.
