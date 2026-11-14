# Project structure: KKKKhazix/khazix-skills

**Analysed commit:** `71cd50ffe1f1f4d400b54be967dc6b59379aff8f`

**Commit reference:** [71cd50ffe1f1f4d400b54be967dc6b59379aff8f](https://github.com/KKKKhazix/khazix-skills/commit/71cd50ffe1f1f4d400b54be967dc6b59379aff8f)

**Tree at this commit:** [KKKKhazix/khazix-skills@71cd50ffe1f1](https://github.com/KKKKhazix/khazix-skills/tree/71cd50ffe1f1f4d400b54be967dc6b59379aff8f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | KKKKhazix/khazix-skills |
| Description | 数字生命卡兹克开源的 AI Skills 合集 | Agent Skills: leader（帮你定义目标）, neat-freak 洁癖, hv-analysis, khazix-writer & more — Claude Code, Codex & 40+ agents |
| Stars | 22253 |
| Forks | 2338 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `71cd50ffe1f1f4d400b54be967dc6b59379aff8f` |
| Retrieved at | 2026-11-14T19:07:53.071600+00:00 |
| Files in this snapshot | 127 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
.github/  (1 files)
  workflows/  (1 files)
    validate.yml
aihot/  (7 files)
  agents/  (1 files)
    openai.yaml
  .gitignore
  LICENSE
  README.md
  SKILL.md
  install.sh
  manifest.sha256
hv-analysis/  (3 files)
  references/  (1 files)
    schema.json
  scripts/  (1 files)
    md_to_pdf.py
  SKILL.md
khazix-writer/  (4 files)
  references/  (3 files)
    content_methodology.md
    quality-check.md
    style_examples.md
  SKILL.md
leader/  (3 files)
  references/  (2 files)
    anatomy.md
    style.md
  SKILL.md
neat-freak/  (89 files)
  evals/  (83 files)
    fixtures/  (80 files)
      … 80 files under this directory
    evals.json
    trigger-eval.json
    validate.py
  references/  (4 files)
    agent-paths.md
    governance.md
    sync-matrix.md
    verification.md
  scripts/  (1 files)
    audit-inventory.sh
  SKILL.md
scripts/  (1 files)
  validate-package.py
storage-analyzer/  (8 files)
  assets/  (1 files)
    report_template.html
  references/  (3 files)
    linux.md
    macos.md
    windows.md
  scripts/  (3 files)
    build_report.py
    scan.py
    server.py
  SKILL.md
tests/  (3 files)
  test_installer.py
  test_storage.py
  test_storage_actions.py
.gitattributes
.gitignore
AGENTS.md
LICENSE
README.en.md
README.md
STATES.md
```

## Entry points

- [neat-freak/evals/fixtures/eval-5-governance/workspace/pdf-tools/src/app.py:4](https://github.com/KKKKhazix/khazix-skills/blob/71cd50ffe1f1f4d400b54be967dc6b59379aff8f/neat-freak/evals/fixtures/eval-5-governance/workspace/pdf-tools/src/app.py#L4)
- [hv-analysis/scripts/md_to_pdf.py:304](https://github.com/KKKKhazix/khazix-skills/blob/71cd50ffe1f1f4d400b54be967dc6b59379aff8f/hv-analysis/scripts/md_to_pdf.py#L304)
- [neat-freak/evals/fixtures/eval-11-unknown-platform/project/main.py:8](https://github.com/KKKKhazix/khazix-skills/blob/71cd50ffe1f1f4d400b54be967dc6b59379aff8f/neat-freak/evals/fixtures/eval-11-unknown-platform/project/main.py#L8)
- [neat-freak/evals/validate.py:138](https://github.com/KKKKhazix/khazix-skills/blob/71cd50ffe1f1f4d400b54be967dc6b59379aff8f/neat-freak/evals/validate.py#L138)
- [storage-analyzer/scripts/build_report.py:54](https://github.com/KKKKhazix/khazix-skills/blob/71cd50ffe1f1f4d400b54be967dc6b59379aff8f/storage-analyzer/scripts/build_report.py#L54)
- [storage-analyzer/scripts/scan.py:503](https://github.com/KKKKhazix/khazix-skills/blob/71cd50ffe1f1f4d400b54be967dc6b59379aff8f/storage-analyzer/scripts/scan.py#L503)
- [storage-analyzer/scripts/server.py:380](https://github.com/KKKKhazix/khazix-skills/blob/71cd50ffe1f1f4d400b54be967dc6b59379aff8f/storage-analyzer/scripts/server.py#L380)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| aihot package | library | Observed | Groups 1 file(s) under aihot package (observed from repository paths and static analysis). |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI, Flask. Observed routes: GET /notes, POST /notes, GET /export, POST /s… |
| neat-freak package | library | Observed | Groups 12 file(s) under neat-freak package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CleanupState, DuChildrenTests, InstallerTests, LinuxDiskTests, StorageTests. |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.github/workflows/validate.yml` (ci)
- `aihot/agents/openai.yaml` (config)
- `hv-analysis/references/schema.json` (config)
- `neat-freak/evals/evals.json` (config)
- `neat-freak/evals/fixtures/eval-1-routine-dev-sync/workspace/taskflow/package.json` (manifest)
- `neat-freak/evals/fixtures/eval-10-vibe-project/project/data.json` (config)
- `neat-freak/evals/fixtures/eval-10-vibe-project/project/package.json` (manifest)
- `neat-freak/evals/fixtures/eval-11-unknown-platform/project/.agentx/memory.json` (config)
- `neat-freak/evals/fixtures/eval-11-unknown-platform/project/requirements.txt` (manifest)
- `neat-freak/evals/fixtures/eval-3-cold-start/workspace/analytics_dashboard/package.json` (manifest)
- `neat-freak/evals/fixtures/eval-4-cross-project/workspace/auth-center/.env.example` (config)
- `neat-freak/evals/fixtures/eval-5-governance/workspace/Link_Shortener/package.json` (manifest)
- `neat-freak/evals/fixtures/eval-6-scope-boundary/workspace/current-app/package.json` (manifest)
- `neat-freak/evals/fixtures/eval-7-release-terminal/project/release-state.json` (config)
- `neat-freak/evals/trigger-eval.json` (config)

## Top-level layout

- `neat-freak` — 89 analysed file(s)
- `storage-analyzer` — 8 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `aihot` — 7 analysed file(s)
- `khazix-writer` — 4 analysed file(s)
- `hv-analysis` — 3 analysed file(s)
- `leader` — 3 analysed file(s)
- `tests` — 3 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `.github` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `71cd50ffe1f1f4d400b54be967dc6b59379aff8f` is the revision these paths and observations refer to.
