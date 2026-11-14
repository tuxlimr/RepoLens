# Project structure: mnfst/awesome-free-llm-apis

**Analysed commit:** `8e24de4f149855a75c2cb24e2e5d0155bada240f`

**Commit reference:** [8e24de4f149855a75c2cb24e2e5d0155bada240f](https://github.com/mnfst/awesome-free-llm-apis/commit/8e24de4f149855a75c2cb24e2e5d0155bada240f)

**Tree at this commit:** [mnfst/awesome-free-llm-apis@8e24de4f1498](https://github.com/mnfst/awesome-free-llm-apis/tree/8e24de4f149855a75c2cb24e2e5d0155bada240f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mnfst/awesome-free-llm-apis |
| Description | List of Permanent Free LLM API  (API Keys) |
| Stars | 13187 |
| Forks | 1590 |
| Licence | CC0-1.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `8e24de4f149855a75c2cb24e2e5d0155bada240f` |
| Retrieved at | 2026-11-14T19:12:00.337613+00:00 |
| Files in this snapshot | 38 |

## Directory tree

```text
.claude/  (3 files)
  hooks/  (2 files)
    no-attribution.sh
    no-claude-app-writes.sh
  settings.json
.github/  (4 files)
  workflows/  (3 files)
    ci.yml
    generate-readme.yml
    no-claude-badge.yml
  FUNDING.yml
.verify/  (7 files)
  report-2026-07-29.json
  report-2026-07-30-v2.json
  report-2026-07-30.json
  report-llm7-test.json
  report-ovh-llama-now.json
  report-ovh-test.json
  state.json
agents/  (2 files)
  provider-sync.md
  triage.md
free-llm-apis/  (3 files)
  references/  (2 files)
    inference-providers.md
    provider-apis.md
  SKILL.md
media/  (4 files)
  okapi-logo-dark.svg
  okapi-logo-light.svg
  sponsor-slot-dark.svg
  sponsor-slot-light.svg
scripts/  (7 files)
  check-sources.js
  generate-readme.js
  generate-skill.js
  provider-setup.js
  test-generated-endpoints.js
  validate-data.js
  verify-providers.js
.gitignore
CLAUDE.md
README.md
contributing.md
data.json
license
package.json
sources.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.claude/settings.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/generate-readme.yml` (ci)
- `.github/workflows/no-claude-badge.yml` (ci)
- `.verify/report-2026-07-29.json` (config)
- `.verify/report-2026-07-30-v2.json` (config)
- `.verify/report-2026-07-30.json` (config)
- `.verify/report-llm7-test.json` (config)
- `.verify/report-ovh-llama-now.json` (config)
- `.verify/report-ovh-test.json` (config)
- `.verify/state.json` (config)
- `data.json` (config)
- `package.json` (manifest)
- `sources.json` (config)

## Top-level layout

- `(root files)` — 8 analysed file(s)
- `.verify` — 7 analysed file(s)
- `scripts` — 7 analysed file(s)
- `.github` — 4 analysed file(s)
- `media` — 4 analysed file(s)
- `.claude` — 3 analysed file(s)
- `free-llm-apis` — 3 analysed file(s)
- `agents` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8e24de4f149855a75c2cb24e2e5d0155bada240f` is the revision these paths and observations refer to.
