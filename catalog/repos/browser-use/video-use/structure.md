# Project structure: browser-use/video-use

**Analysed commit:** `43cfc566833548093455c9d4a46bd69913b7e552`

**Commit reference:** [43cfc566833548093455c9d4a46bd69913b7e552](https://github.com/browser-use/video-use/commit/43cfc566833548093455c9d4a46bd69913b7e552)

**Tree at this commit:** [browser-use/video-use@43cfc5668335](https://github.com/browser-use/video-use/tree/43cfc566833548093455c9d4a46bd69913b7e552)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | browser-use/video-use |
| Description | Edit videos with coding agents |
| Stars | 31051 |
| Forks | 3597 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `43cfc566833548093455c9d4a46bd69913b7e552` |
| Retrieved at | 2026-11-14T19:07:08.758794+00:00 |
| Files in this snapshot | 35 |

## Directory tree

```text
helpers/  (6 files)
  grade.py
  pack_transcripts.py
  render.py
  timeline_view.py
  transcribe.py
  transcribe_batch.py
skills/  (17 files)
  manim-video/  (17 files)
    references/  (14 files)
      … 14 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    README.md
    SKILL.md
static/  (1 files)
  timeline-view.svg
tests/  (3 files)
  test_render_captions.py
  test_render_fps.py
  test_render_orientation.py
.env.example
.gitignore
LICENSE
README.md
SKILL.md
install.md
poster.html
pyproject.toml
```

## Entry points

- [helpers/grade.py:374](https://github.com/browser-use/video-use/blob/43cfc566833548093455c9d4a46bd69913b7e552/helpers/grade.py#L374)
- [helpers/pack_transcripts.py:205](https://github.com/browser-use/video-use/blob/43cfc566833548093455c9d4a46bd69913b7e552/helpers/pack_transcripts.py#L205)
- [helpers/render.py:800](https://github.com/browser-use/video-use/blob/43cfc566833548093455c9d4a46bd69913b7e552/helpers/render.py#L800)
- [helpers/timeline_view.py:391](https://github.com/browser-use/video-use/blob/43cfc566833548093455c9d4a46bd69913b7e552/helpers/timeline_view.py#L391)
- [helpers/transcribe.py:240](https://github.com/browser-use/video-use/blob/43cfc566833548093455c9d4a46bd69913b7e552/helpers/transcribe.py#L240)
- [helpers/transcribe_batch.py:125](https://github.com/browser-use/video-use/blob/43cfc566833548093455c9d4a46bd69913b7e552/helpers/transcribe_batch.py#L125)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _sample_frame_stats, _srt_timestamp, _words_in_range, apply_grade, apply_loudnorm_two_pa… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 1 file(s) under skills package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BuildMasterSrtTests, ChunkWordsTests, ParseFpsTests, PortraitDetectionTests, ProbeSourceFpsTests, RenderRate… |

## Important files

- `.env.example` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `skills` — 17 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `helpers` — 6 analysed file(s)
- `tests` — 3 analysed file(s)
- `static` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `43cfc566833548093455c9d4a46bd69913b7e552` is the revision these paths and observations refer to.
