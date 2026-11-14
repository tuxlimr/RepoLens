# Project structure: anderspitman/awesome-tunneling

**Analysed commit:** `b0e9dd2aef30e09d0a80eca1fe42daf2dcb62ce6`

**Commit reference:** [b0e9dd2aef30e09d0a80eca1fe42daf2dcb62ce6](https://github.com/anderspitman/awesome-tunneling/commit/b0e9dd2aef30e09d0a80eca1fe42daf2dcb62ce6)

**Tree at this commit:** [anderspitman/awesome-tunneling@b0e9dd2aef30](https://github.com/anderspitman/awesome-tunneling/tree/b0e9dd2aef30e09d0a80eca1fe42daf2dcb62ce6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | anderspitman/awesome-tunneling |
| Description | List of ngrok, Cloudflare Tunnel, Tailscale, and ZeroTier alternatives and other tunneling software and services. Focus on self-hosting. |
| Stars | 22044 |
| Forks | 1072 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `b0e9dd2aef30e09d0a80eca1fe42daf2dcb62ce6` |
| Retrieved at | 2026-11-14T19:07:55.822351+00:00 |
| Files in this snapshot | 3 |

## Directory tree

```text
scripts/  (1 files)
  sort_by_stars.py
.gitignore
README.md
```

## Entry points

- [scripts/sort_by_stars.py:174](https://github.com/anderspitman/awesome-tunneling/blob/b0e9dd2aef30e09d0a80eca1fe42daf2dcb62ce6/scripts/sort_by_stars.py#L174)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: fetch_star_count, github_token, load_cache, main, repo_for_entry, save_cache. |

## Important files

No manifest, config, CI, or container files were observed in the analysed set.

## Top-level layout

- `(root files)` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b0e9dd2aef30e09d0a80eca1fe42daf2dcb62ce6` is the revision these paths and observations refer to.
