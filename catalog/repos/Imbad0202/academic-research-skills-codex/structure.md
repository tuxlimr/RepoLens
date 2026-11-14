# Project structure: Imbad0202/academic-research-skills-codex

**Analysed commit:** `82725acb393c4410ac6f47634a7f51b40a162fa4`

**Commit reference:** [82725acb393c4410ac6f47634a7f51b40a162fa4](https://github.com/Imbad0202/academic-research-skills-codex/commit/82725acb393c4410ac6f47634a7f51b40a162fa4)

**Tree at this commit:** [Imbad0202/academic-research-skills-codex@82725acb393c](https://github.com/Imbad0202/academic-research-skills-codex/tree/82725acb393c4410ac6f47634a7f51b40a162fa4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Imbad0202/academic-research-skills-codex |
| Description | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| Stars | 14560 |
| Forks | 627 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `82725acb393c4410ac6f47634a7f51b40a162fa4` |
| Retrieved at | 2026-11-14T19:09:26.169125+00:00 |
| Files in this snapshot | 405 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.codex/  (1 files)
  config.toml
.github/  (1 files)
  FUNDING.yml
docs/  (1 files)
  windows-marketplace-recovery.md
examples/  (11 files)
  codex/  (10 files)
    full-pipeline-heqa-scope-transformation/  (10 files)
      … 10 files under this directory
  README.md
plugins/  (375 files)
  ars-codex/  (375 files)
    .codex-plugin/  (1 files)
      … 1 files under this directory
    skills/  (374 files)
      … 374 files under this directory
skills/  (4 files)
  academic-research-suite/  (4 files)
    ars/  (4 files)
      … 4 files under this directory
.gitignore
CHANGELOG.md
CITATION.cff
CODEX_FULL_RUNTIME_ADAPTER.md
LICENSE
README.md
README_JA.md
README_ZH-CN.md
README_ZH-TW.md
SECURITY.md
VERSION
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.codex/config.toml` (config)
- `.github/FUNDING.yml` (config)
- `plugins/ars-codex/.codex-plugin/plugin.json` (config)
- `plugins/ars-codex/skills/academic-research-suite/agents/openai.yaml` (config)
- `plugins/ars-codex/skills/academic-research-suite/ars/.command-invariants.toml` (config)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/FUNDING.yml` (config)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/changelog-covers-merges.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/command-invariants.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/defer-label-gate.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/eval-harness.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/freshness-check.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/harness-retirement-monthly.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/platform-port-reminder.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/pr-closes-issue.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/pytest.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/release-cooldown.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/repository-hygiene.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/spec-consistency.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/tag-version-match.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.github/workflows/test-count-monotonic.yml` (ci)
- `plugins/ars-codex/skills/academic-research-suite/ars/.gitleaks.toml` (config)
- `plugins/ars-codex/skills/academic-research-suite/ars/docs/design/snapshots/2026-05-13-ai-disclosure-discovery/manifest.yaml` (config)
- `plugins/ars-codex/skills/academic-research-suite/ars/evals/gold/citation_extraction/manifest.yaml` (config)

## Top-level layout

- `plugins` — 375 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `examples` — 11 analysed file(s)
- `skills` — 4 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.codex` — 1 analysed file(s)
- `.github` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `82725acb393c4410ac6f47634a7f51b40a162fa4` is the revision these paths and observations refer to.
