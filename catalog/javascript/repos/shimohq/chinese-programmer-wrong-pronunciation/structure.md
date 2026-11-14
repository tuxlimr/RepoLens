# Project structure: shimohq/chinese-programmer-wrong-pronunciation

**Analysed commit:** `1f04534b8d12f1bb5977cc683caceb7d1f393033`

**Commit reference:** [1f04534b8d12f1bb5977cc683caceb7d1f393033](https://github.com/shimohq/chinese-programmer-wrong-pronunciation/commit/1f04534b8d12f1bb5977cc683caceb7d1f393033)

**Tree at this commit:** [shimohq/chinese-programmer-wrong-pronunciation@1f04534b8d12](https://github.com/shimohq/chinese-programmer-wrong-pronunciation/tree/1f04534b8d12f1bb5977cc683caceb7d1f393033)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | shimohq/chinese-programmer-wrong-pronunciation |
| Description | 中国程序员容易发音错误的单词 |
| Stars | 23376 |
| Forks | 1598 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `1f04534b8d12f1bb5977cc683caceb7d1f393033` |
| Retrieved at | 2026-11-14T19:11:04.926082+00:00 |
| Files in this snapshot | 21 |

## Directory tree

```text
.github/  (1 files)
  PULL_REQUEST_TEMPLATE.md
tools/  (17 files)
  chromium_extension/  (16 files)
    css/  (1 files)
      … 1 files under this directory
    images/  (1 files)
      … 1 files under this directory
    js/  (7 files)
      … 7 files under this directory
    rules/  (1 files)
      … 1 files under this directory
    web-components/  (2 files)
      … 2 files under this directory
    README.md
    format-code.sh
    manifest.json
    package.json
  addword.py
.editorconfig
.gitignore
README.md
```

## Entry points

- [tools/addword.py:51](https://github.com/shimohq/chinese-programmer-wrong-pronunciation/blob/1f04534b8d12f1bb5977cc683caceb7d1f393033/tools/addword.py#L51)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: get_pronunciations, main. |
| tools package | library | Observed | Groups 8 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `tools/chromium_extension/manifest.json` (config)
- `tools/chromium_extension/package.json` (manifest)
- `tools/chromium_extension/rules/remove_content_security_policy.json` (config)

## Top-level layout

- `tools` — 17 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1f04534b8d12f1bb5977cc683caceb7d1f393033` is the revision these paths and observations refer to.
