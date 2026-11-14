# Project structure: yokoffing/Betterfox

**Analysed commit:** `067172a4b0dc90e78e5b8b94d9abfe6430c6a7be`

**Commit reference:** [067172a4b0dc90e78e5b8b94d9abfe6430c6a7be](https://github.com/yokoffing/Betterfox/commit/067172a4b0dc90e78e5b8b94d9abfe6430c6a7be)

**Tree at this commit:** [yokoffing/Betterfox@067172a4b0dc](https://github.com/yokoffing/Betterfox/tree/067172a4b0dc90e78e5b8b94d9abfe6430c6a7be)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yokoffing/Betterfox |
| Description | Firefox user.js for optimal privacy and security. Your favorite browser, but better. |
| Stars | 10991 |
| Forks | 258 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `067172a4b0dc90e78e5b8b94d9abfe6430c6a7be` |
| Retrieved at | 2026-11-14T19:12:27.442716+00:00 |
| Files in this snapshot | 15 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.yml
personal/  (1 files)
  user-overrides.js
waterfox/  (2 files)
  README.md
  user.js
zen/  (1 files)
  user.js
.gitattributes
Fastfox.js
LICENSE
Peskyfox.js
README.md
Securefox.js
Smoothfox.js
install.py
policies.json
user.js
```

## Entry points

- [install.py:215](https://github.com/yokoffing/Betterfox/blob/067172a4b0dc90e78e5b8b94d9abfe6430c6a7be/install.py#L215)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _get_default_firefox_version_and_root, _get_default_profile_folder, _get_firefox_version… |
| personal package | library | Observed | Groups 1 file(s) under personal package (observed from repository paths and static analysis). |
| waterfox package | library | Observed | Groups 1 file(s) under waterfox package (observed from repository paths and static analysis). |
| zen package | library | Observed | Groups 1 file(s) under zen package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `policies.json` (config)

## Top-level layout

- `(root files)` — 10 analysed file(s)
- `waterfox` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `personal` — 1 analysed file(s)
- `zen` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `067172a4b0dc90e78e5b8b94d9abfe6430c6a7be` is the revision these paths and observations refer to.
