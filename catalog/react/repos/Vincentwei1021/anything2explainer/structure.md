# Project structure: Vincentwei1021/anything2explainer

**Analysed commit:** `0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab`

**Commit reference:** [0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab](https://github.com/Vincentwei1021/anything2explainer/commit/0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab)

**Tree at this commit:** [Vincentwei1021/anything2explainer@0b85f6c7bfc4](https://github.com/Vincentwei1021/anything2explainer/tree/0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Vincentwei1021/anything2explainer |
| Description | Topic in, narrated explainer video out. A Claude Code / Codex skill that turns any topic into a black-canvas motion-graphics explainer video with TTS voiceover, subtitles and a chapter progress bar. Chinese or English; every frame drawn in code with Remotion. |
| Stars | 3317 |
| Forks | 423 |
| Licence | Other |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab` |
| Retrieved at | 2026-11-14T19:15:24.285187+00:00 |
| Files in this snapshot | 171 |

## Directory tree

```text
examples/  (97 files)
  contrast/  (1 files)
    README.md
  rag/  (96 files)
    qc/  (5 files)
      … 5 files under this directory
    shots_src/  (81 files)
      … 81 files under this directory
    AGENT_RAG_BUILD_RULES.md
    AGENT_RAG_QC_RULES.md
    README.md
    narration.txt
    research.md
    storyboard_src.md
    timeline.md
    ui_rag.tsx
    交付说明.md
    分镜表.md
reference/  (11 files)
  agent-build-rules.md
  agent-qc-rules.md
  composition-and-light.md
  lessons.md
  motion-vocabulary.md
  narration-guidance.md
  narration-guidance.zh.md
  narration-storyboard.md
  prompts.md
  research-brief.md
  style-guide.md
template/  (57 files)
  public/  (1 files)
    fonts/  (1 files)
      … 1 files under this directory
  script/  (1 files)
    narration.txt
  scripts/  (12 files)
    frame_metrics.py
    motion_check.py
    new_project.sh
    preview.sh
    render.sh
    render_storyboard.py
    selfcheck.py
    sheet.py
    still.sh
    test_portable_scripts.py
    test_render.sh
    tts_build.py
  src/  (39 files)
    common/  (14 files)
      … 14 files under this directory
    overlay/  (3 files)
      … 3 files under this directory
    shots/  (16 files)
      … 16 files under this directory
    Main.tsx
    Root.tsx
    config.ts
    fx.tsx
    index.ts
    ui.tsx
  .gitignore
  package.json
  remotion.config.ts
  tsconfig.json
.gitignore
CITATION.cff
LICENSE
README.md
README_ZH.md
SKILL.md
```

## Entry points

- [template/scripts/tts_build.py:522](https://github.com/Vincentwei1021/anything2explainer/blob/0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab/template/scripts/tts_build.py#L522)
- [template/src/Main.tsx](https://github.com/Vincentwei1021/anything2explainer/blob/0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab/template/src/Main.tsx)
- [template/src/common/index.ts](https://github.com/Vincentwei1021/anything2explainer/blob/0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab/template/src/common/index.ts)
- [template/src/index.ts](https://github.com/Vincentwei1021/anything2explainer/blob/0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab/template/src/index.ts)
- [template/src/overlay/index.ts](https://github.com/Vincentwei1021/anything2explainer/blob/0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab/template/src/overlay/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _file_fp, apply_pronounce, cache_path, chunk_starts, decode, detect_lang. |
| template package | library | Observed | Groups 49 file(s) under template package (observed from repository paths and static analysis). Observed top-level functions: analyze, cfg_bg, changed_px, diff_series, dot_mask, frame_path. |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: PortableScriptsTests. |

## Important files

- `template/package.json` (manifest)
- `template/tsconfig.json` (config)

## Top-level layout

- `examples` — 97 analysed file(s)
- `template` — 57 analysed file(s)
- `reference` — 11 analysed file(s)
- `(root files)` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0b85f6c7bfc4ef094ee1afb6c68c06fcf329cfab` is the revision these paths and observations refer to.
