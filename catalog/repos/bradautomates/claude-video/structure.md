# Project structure: bradautomates/claude-video

**Analysed commit:** `03ceb42f7fa2c4439aca01752118044baabffb8f`

**Commit reference:** [03ceb42f7fa2c4439aca01752118044baabffb8f](https://github.com/bradautomates/claude-video/commit/03ceb42f7fa2c4439aca01752118044baabffb8f)

**Tree at this commit:** [bradautomates/claude-video@03ceb42f7fa2](https://github.com/bradautomates/claude-video/tree/03ceb42f7fa2c4439aca01752118044baabffb8f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bradautomates/claude-video |
| Description | Give Claude the ability to watch any video. /watch downloads, extracts frames, transcribes, hands it all to Claude. |
| Stars | 20805 |
| Forks | 2210 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `03ceb42f7fa2c4439aca01752118044baabffb8f` |
| Retrieved at | 2026-11-14T19:08:01.051430+00:00 |
| Files in this snapshot | 22 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.codex-plugin/  (1 files)
  plugin.json
hooks/  (2 files)
  scripts/  (1 files)
    check-setup.sh
  hooks.json
skills/  (11 files)
  watch/  (11 files)
    scripts/  (10 files)
      … 10 files under this directory
    SKILL.md
.skillignore
AGENTS.md
CHANGELOG.md
CLAUDE.md
LICENSE
README.md
```

## Entry points

- [skills/watch/scripts/download.py:203](https://github.com/bradautomates/claude-video/blob/03ceb42f7fa2c4439aca01752118044baabffb8f/skills/watch/scripts/download.py#L203)
- [skills/watch/scripts/frames.py:686](https://github.com/bradautomates/claude-video/blob/03ceb42f7fa2c4439aca01752118044baabffb8f/skills/watch/scripts/frames.py#L686)
- [skills/watch/scripts/setup.py:336](https://github.com/bradautomates/claude-video/blob/03ceb42f7fa2c4439aca01752118044baabffb8f/skills/watch/scripts/setup.py#L336)
- [skills/watch/scripts/transcribe.py:109](https://github.com/bradautomates/claude-video/blob/03ceb42f7fa2c4439aca01752118044baabffb8f/skills/watch/scripts/transcribe.py#L109)
- [skills/watch/scripts/watch.py:425](https://github.com/bradautomates/claude-video/blob/03ceb42f7fa2c4439aca01752118044baabffb8f/skills/watch/scripts/watch.py#L425)
- [skills/watch/scripts/whisper.py:413](https://github.com/bradautomates/claude-video/blob/03ceb42f7fa2c4439aca01752118044baabffb8f/skills/watch/scripts/whisper.py#L413)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigError. Observed top-level functions: _brew_pkg, _check_binaries, _check_file_pe… |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Segments. Observed top-level functions: _build_multipart, _clamp_fps, _common, _dedupe, _d… |
| hooks package | library | Observed | Groups 1 file(s) under hooks package (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 3 file(s) under skills package (observed from repository paths and static analysis). Observed top-level functions: _call, _clock, _error_message, _fail, _processing, ask. |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.codex-plugin/plugin.json` (config)
- `hooks/hooks.json` (config)
- `skills/watch/scripts/setup.py` (manifest)

## Top-level layout

- `skills` — 11 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `hooks` — 2 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `03ceb42f7fa2c4439aca01752118044baabffb8f` is the revision these paths and observations refer to.
