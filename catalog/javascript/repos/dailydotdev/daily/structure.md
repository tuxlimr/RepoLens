# Project structure: dailydotdev/daily

**Analysed commit:** `07eebd36a8a683ee9f0c28d75545f3824b58f2a8`

**Commit reference:** [07eebd36a8a683ee9f0c28d75545f3824b58f2a8](https://github.com/dailydotdev/daily/commit/07eebd36a8a683ee9f0c28d75545f3824b58f2a8)

**Tree at this commit:** [dailydotdev/daily@07eebd36a8a6](https://github.com/dailydotdev/daily/tree/07eebd36a8a683ee9f0c28d75545f3824b58f2a8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dailydotdev/daily |
| Description | daily.dev is the personalized developer news feed and community. Get the best tech content from all over the web in your browser new tab or on mobile. Free and open source. |
| Stars | 20137 |
| Forks | 575 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `07eebd36a8a683ee9f0c28d75545f3824b58f2a8` |
| Retrieved at | 2026-11-14T19:11:14.665714+00:00 |
| Files in this snapshot | 30 |

## Directory tree

```text
.claude/  (4 files)
  skills/  (4 files)
    daily-dev-growth-routine/  (1 files)
      … 1 files under this directory
    daily-dev-onboarding/  (1 files)
      … 1 files under this directory
    daily-dev-profile/  (1 files)
      … 1 files under this directory
    daily-dev-routine/  (1 files)
      … 1 files under this directory
.claude-plugin/  (12 files)
  plugins/  (11 files)
    daily.dev/  (11 files)
      … 11 files under this directory
  marketplace.json
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    ---bug-report.yml
    ---feature-request.yaml
  workflows/  (1 files)
    close-inactive-tickets.yml
skills/  (8 files)
  daily-dev-ask/  (1 files)
    SKILL.md
  daily-dev-content-ideas/  (1 files)
    SKILL.md
  daily-dev-content-review/  (1 files)
    SKILL.md
  daily-dev-growth-routine/  (1 files)
    SKILL.md
  daily-dev-onboarding/  (1 files)
    SKILL.md
  daily-dev-profile/  (1 files)
    SKILL.md
  daily-dev-routine/  (1 files)
    SKILL.md
  daily.dev/  (1 files)
    SKILL.md
.gitignore
LICENSE
README.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugins/daily.dev/.claude-plugin/plugin.json` (config)
- `.claude-plugin/plugins/daily.dev/hooks/hooks.json` (config)
- `.github/ISSUE_TEMPLATE/---bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/---feature-request.yaml` (config)
- `.github/workflows/close-inactive-tickets.yml` (ci)

## Top-level layout

- `.claude-plugin` — 12 analysed file(s)
- `skills` — 8 analysed file(s)
- `.claude` — 4 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `07eebd36a8a683ee9f0c28d75545f3824b58f2a8` is the revision these paths and observations refer to.
