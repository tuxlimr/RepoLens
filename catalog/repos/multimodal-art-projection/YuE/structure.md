# Project structure: multimodal-art-projection/YuE

**Analysed commit:** `1116bea76032bee5668e5f097294d082fa0b84f0`

**Commit reference:** [1116bea76032bee5668e5f097294d082fa0b84f0](https://github.com/multimodal-art-projection/YuE/commit/1116bea76032bee5668e5f097294d082fa0b84f0)

**Tree at this commit:** [multimodal-art-projection/YuE@1116bea76032](https://github.com/multimodal-art-projection/YuE/tree/1116bea76032bee5668e5f097294d082fa0b84f0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | multimodal-art-projection/YuE |
| Description | YuE2: frontier music generation with symbolic planning, zero-shot covers, and agentic music editing. |
| Stars | 13483 |
| Forks | 1558 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `1116bea76032bee5668e5f097294d082fa0b84f0` |
| Retrieved at | 2026-11-14T19:09:48.715772+00:00 |
| Files in this snapshot | 126 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    tests.yml
assets/  (4 files)
  discord.svg
  frontier-teaser.svg
  institutions-mobile.svg
  institutions.svg
docs/  (13 files)
  benchmark-results.csv
  benchmark-results.json
  benchmarks.md
  cover-results.csv
  cover-results.json
  covers.md
  editing-results.csv
  editing-results.json
  editing.md
  frontier-composites.json
  generation.md
  hardware.md
  source-notes.md
examples/  (7 files)
  README.md
  generate.py
  instrumental_clip.py
  melody.abc
  score-jazz.abc
  score.abc
  song.json
licenses/  (2 files)
  SnakeBeta-NVIDIA-MIT.txt
  stable-audio-tools-MIT.txt
skills/  (42 files)
  yue2-music/  (42 files)
    agents/  (1 files)
      … 1 files under this directory
    assets/  (2 files)
      … 2 files under this directory
    instrumental/  (27 files)
      … 27 files under this directory
    references/  (5 files)
      … 5 files under this directory
    scripts/  (5 files)
      … 5 files under this directory
    LICENSE
    SKILL.md
src/  (16 files)
  yue2/  (16 files)
    __init__.py
    cli.py
    cuda_graph.py
    devices.py
    fast.py
    modeling_vae.py
    modeling_yue2.py
    nar.py
    pipeline.py
    placement.py
    progress.py
    protocol.py
    quantization.py
    sampling.py
    storage.py
    tokenization_yue2.py
tests/  (32 files)
  test_attention_portability.py
  test_cli_batch.py
  test_cli_decode.py
  test_cli_export.py
  test_cli_inspect.py
  test_cli_public.py
  test_cuda_graph.py
  test_devices.py
  test_example_generate.py
  test_fast.py
  test_instrumental_delivery.py
  test_model.py
  test_nar.py
  test_offline_workflow.py
  test_pipeline.py
  test_placement.py
  test_preflight.py
  test_progress.py
  test_progress_integration.py
  test_protocol.py
  test_public_export.py
  test_sampling.py
  test_skill_abc_tools.py
  test_skill_listen.py
  … 8 more files
tools/  (1 files)
  build_release.py
.gitattributes
.gitignore
LICENSE
MANIFEST.in
MODEL_LICENSE
README.md
THIRD_PARTY_NOTICES.md
pyproject.toml
```

## Entry points

- [src/yue2/cli.py](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/src/yue2/cli.py)
- [src/yue2/fast.py:423](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/src/yue2/fast.py#L423)
- [skills/yue2-music/instrumental/scripts/abc_tools.py:336](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/skills/yue2-music/instrumental/scripts/abc_tools.py#L336)
- [skills/yue2-music/instrumental/scripts/compile_score.py:225](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/skills/yue2-music/instrumental/scripts/compile_score.py#L225)
- [skills/yue2-music/instrumental/scripts/instrumental.py:505](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/skills/yue2-music/instrumental/scripts/instrumental.py#L505)
- [skills/yue2-music/instrumental/scripts/instrumentalize.py:139](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/skills/yue2-music/instrumental/scripts/instrumentalize.py#L139)
- [skills/yue2-music/instrumental/scripts/setup_runtime.py:112](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/skills/yue2-music/instrumental/scripts/setup_runtime.py#L112)
- [skills/yue2-music/instrumental/scripts/transcribe_cover.py:119](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/skills/yue2-music/instrumental/scripts/transcribe_cover.py#L119)
- [skills/yue2-music/instrumental/scripts/verify_bundle.py:40](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/skills/yue2-music/instrumental/scripts/verify_bundle.py#L40)
- [skills/yue2-music/scripts/abc_tools.py:336](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/skills/yue2-music/scripts/abc_tools.py#L336)
- [skills/yue2-music/scripts/listen.py:290](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/skills/yue2-music/scripts/listen.py#L290)
- [skills/yue2-music/scripts/run_yue2.py:212](https://github.com/multimodal-art-projection/YuE/blob/1116bea76032bee5668e5f097294d082fa0b84f0/skills/yue2-music/scripts/run_yue2.py#L212)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AbcError, Score, Voice, _Worker. Observed top-level functions: __getattr__, _emit, _stop_… |
| skills package | library | Observed | Groups 2 file(s) under skills package (observed from repository paths and static analysis). Observed top-level functions: fresh_directory, read_json, sha256, write_json. |
| Tests | test | Observed | Groups 33 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ABCChecks, ComposerRoutingTests, ListenChecks, LoadedPipeline, Model, OldModel. Observed top-level function… |
| yue2 package | library | Observed | Groups 14 file(s) under yue2 package (observed from repository paths and static analysis). Observed top-level classes: Attention, AudioPositionEmbedding, Backbone, CachedNAR, Chunk, DecoderBlock. Observed top-level func… |

## Important files

- `.github/workflows/tests.yml` (ci)
- `MANIFEST.in` (manifest)
- `docs/benchmark-results.json` (config)
- `docs/cover-results.json` (config)
- `docs/editing-results.json` (config)
- `docs/frontier-composites.json` (config)
- `examples/song.json` (config)
- `pyproject.toml` (manifest)
- `skills/yue2-music/agents/openai.yaml` (config)
- `skills/yue2-music/assets/prompt.json` (config)
- `skills/yue2-music/instrumental/agents/openai.yaml` (config)
- `skills/yue2-music/instrumental/assets/cover-release.json` (config)
- `skills/yue2-music/instrumental/assets/example-repairs.json` (config)
- `skills/yue2-music/instrumental/assets/release.json` (config)
- `skills/yue2-music/instrumental/assets/validation.json` (config)
- `skills/yue2-music/instrumental/bundle-manifest.json` (config)
- `skills/yue2-music/instrumental/requirements-inference.txt` (manifest)

## Top-level layout

- `skills` — 42 analysed file(s)
- `tests` — 32 analysed file(s)
- `src` — 16 analysed file(s)
- `docs` — 13 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `examples` — 7 analysed file(s)
- `assets` — 4 analysed file(s)
- `licenses` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `tools` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1116bea76032bee5668e5f097294d082fa0b84f0` is the revision these paths and observations refer to.
