# Project structure: handsomestWei/patent-disclosure-skill

**Analysed commit:** `b4bbec6f0a1c3c32a904faabeb249639c0b30d98`

**Commit reference:** [b4bbec6f0a1c3c32a904faabeb249639c0b30d98](https://github.com/handsomestWei/patent-disclosure-skill/commit/b4bbec6f0a1c3c32a904faabeb249639c0b30d98)

**Tree at this commit:** [handsomestWei/patent-disclosure-skill@b4bbec6f0a1c](https://github.com/handsomestWei/patent-disclosure-skill/tree/b4bbec6f0a1c3c32a904faabeb249639c0b30d98)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | handsomestWei/patent-disclosure-skill |
| Description | 中国专利.skill：专利点挖掘与交底书（发明/实用/外观）编写，通俗解读专利，嗅探政策动向，辅助审查答复。 |
| Stars | 13448 |
| Forks | 1453 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `b4bbec6f0a1c3c32a904faabeb249639c0b30d98` |
| Retrieved at | 2026-11-14T19:09:49.565966+00:00 |
| Files in this snapshot | 513 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    update-star-history.yml
scripts/  (1 files)
  generate-star-history.py
skills/  (505 files)
  patent-application/  (55 files)
    prompts/  (16 files)
      … 16 files under this directory
    references/  (10 files)
      … 10 files under this directory
    tests/  (10 files)
      … 10 files under this directory
    tools/  (17 files)
      … 17 files under this directory
    README.md
    SKILL.md
  patent-chart/  (15 files)
    examples/  (1 files)
      … 1 files under this directory
    prompts/  (4 files)
      … 4 files under this directory
    references/  (1 files)
      … 1 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    tools/  (4 files)
      … 4 files under this directory
    README.md
    SKILL.md
  patent-disclosure/  (153 files)
    examples/  (17 files)
      … 17 files under this directory
    prompts/  (32 files)
      … 32 files under this directory
    references/  (20 files)
      … 20 files under this directory
    tests/  (32 files)
      … 32 files under this directory
    tools/  (50 files)
      … 50 files under this directory
    README.md
    SKILL.md
  patent-docket/  (32 files)
    assets/  (1 files)
      … 1 files under this directory
    examples/  (1 files)
      … 1 files under this directory
    prompts/  (10 files)
      … 10 files under this directory
    references/  (7 files)
      … 7 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    tools/  (8 files)
      … 8 files under this directory
    README.md
    SKILL.md
    config.yaml
  patent-exam-policy/  (12 files)
    docs/  (1 files)
      … 1 files under this directory
    prompts/  (6 files)
      … 6 files under this directory
    references/  (3 files)
      … 3 files under this directory
    README.md
    SKILL.md
  patent-map/  (41 files)
    data/  (1 files)
      … 1 files under this directory
    prompts/  (2 files)
      … 2 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    tools/  (21 files)
      … 21 files under this directory
    web/  (14 files)
      … 14 files under this directory
    README.md
    SKILL.md
  patent-oa/  (45 files)
    assets/  (2 files)
      … 2 files under this directory
    docs/  (3 files)
      … 3 files under this directory
    examples/  (4 files)
      … 4 files under this directory
    prompts/  (7 files)
      … 7 files under this directory
    references/  (1 files)
      … 1 files under this directory
    tests/  (4 files)
      … 4 files under this directory
    tools/  (22 files)
      … 22 files under this directory
    README.md
    SKILL.md
  patent-reader/  (115 files)
    assets/  (7 files)
      … 7 files under this directory
    docs/  (1 files)
      … 1 files under this directory
    examples/  (1 files)
      … 1 files under this directory
    prompts/  (7 files)
      … 7 files under this directory
    references/  (10 files)
      … 10 files under this directory
    tests/  (21 files)
      … 21 files under this directory
    tools/  (66 files)
      … 66 files under this directory
    README.md
    SKILL.md
  patent-search/  (37 files)
    prompts/  (4 files)
      … 4 files under this directory
    references/  (1 files)
      … 1 files under this directory
    tests/  (9 files)
      … 9 files under this directory
    tools/  (20 files)
      … 20 files under this directory
    README.md
    SKILL.md
    config.yaml
.gitignore
INSTALL.md
LICENSE
README.md
SKILL.md
requirements.txt
```

## Entry points

- [scripts/generate-star-history.py:449](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/scripts/generate-star-history.py#L449)
- [skills/patent-application/tools/audit_claims.py:211](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/audit_claims.py#L211)
- [skills/patent-application/tools/check_design_views.py:350](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/check_design_views.py#L350)
- [skills/patent-application/tools/check_numeral_register.py:331](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/check_numeral_register.py#L331)
- [skills/patent-application/tools/check_support.py:338](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/check_support.py#L338)
- [skills/patent-application/tools/compose_application_figure.py:132](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/compose_application_figure.py#L132)
- [skills/patent-application/tools/emit_application_docx.py:102](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/emit_application_docx.py#L102)
- [skills/patent-application/tools/iteration_dialog_log.py:88](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/iteration_dialog_log.py#L88)
- [skills/patent-application/tools/latex_delimiters.py:185](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/latex_delimiters.py#L185)
- [skills/patent-application/tools/material_gate.py:299](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/material_gate.py#L299)
- [skills/patent-application/tools/md_to_docx.py:1429](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/md_to_docx.py#L1429)
- [skills/patent-application/tools/plan_figures.py:298](https://github.com/handsomestWei/patent-disclosure-skill/blob/b4bbec6f0a1c3c32a904faabeb249639c0b30d98/skills/patent-application/tools/plan_figures.py#L298)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 58 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: _clue_link, _clue_stem, _conf_rank, _region_text, _table_wikilink, agent_fits_for. |
| Application entry point | entrypoint | Observed | Groups 94 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BareParenHit, EpubSearchHit, Finding, LatexDelimError, MapHandler, MapServer. Observed to… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: fetch_text, looks_blocked. |
| skills package | library | Observed | Groups 107 file(s) under skills package (observed from repository paths and static analysis). Observed top-level classes: Claim, EmbedError, Embedder, EpubNavError, EpubSubmitError, GooglePatentsBadResponse. Observed to… |
| Tests | test | Observed | Groups 82 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AbstractFieldTests, AdvancedInventorSearchTests, AdvancedTypeFilterTests, ApplyTypeFilterTests, AuditClaims… |

## Important files

- `.github/workflows/update-star-history.yml` (ci)
- `requirements.txt` (manifest)
- `skills/patent-application/references/promo_terms.yaml` (config)
- `skills/patent-application/references/schemas/application_figure_plan.schema.yaml` (config)
- `skills/patent-application/references/schemas/application_plan.schema.yaml` (config)
- `skills/patent-application/references/schemas/invention_figures.schema.yaml` (config)
- `skills/patent-application/references/schemas/numeral_register.schema.yaml` (config)
- `skills/patent-disclosure/references/formulas/paradigms.yaml` (config)
- `skills/patent-disclosure/references/patent_type_search.yaml` (config)
- `skills/patent-disclosure/references/schemas/appearance.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/decompose.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/design_around.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/design_lineart_brief.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/family_plan.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/figure_plan.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/formula_plan.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/matrix.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/scorecard.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/structure.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/structure_callout_anchors.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/structure_lineart_brief.schema.yaml` (config)
- `skills/patent-disclosure/references/schemas/structure_lineart_compose.schema.yaml` (config)
- `skills/patent-disclosure/references/scorecards/gbt42748_fence.yaml` (config)
- `skills/patent-disclosure/tools/crawl/cnipa_epub_wait.yaml` (config)
- `skills/patent-disclosure/tools/crawl/requirements-cnipa.txt` (manifest)
- `skills/patent-disclosure/tools/package.json` (manifest)
- `skills/patent-disclosure/tools/requirements-pdf.txt` (manifest)
- `skills/patent-disclosure/tools/requirements-step.txt` (manifest)
- `skills/patent-docket/config.yaml` (config)
- `skills/patent-docket/references/dispositions.yaml` (config)
- `skills/patent-docket/references/docket.schema.yaml` (config)
- `skills/patent-docket/references/phases.yaml` (config)
- `skills/patent-exam-policy/references/schemas/exam_policy_backlog.schema.yaml` (config)
- `skills/patent-exam-policy/references/sources.yaml` (config)
- `skills/patent-map/tools/ipc_scheme/requirements.txt` (manifest)
- `skills/patent-map/tools/ipc_scheme/testdata/sample_ipcpub.json` (config)
- `skills/patent-map/tools/requirements.txt` (manifest)
- `skills/patent-oa/assets/obsidian/oa.base.yaml` (config)
- `skills/patent-oa/docs/embedding.config.yaml` (config)
- `skills/patent-oa/references/schemas/oa_case.schema.yaml` (config)
- `skills/patent-oa/tools/requirements-oa.txt` (manifest)
- `skills/patent-reader/assets/obsidian/glossary.base.yaml` (config)
- `skills/patent-reader/assets/obsidian/graph_color_groups.json` (config)
- `skills/patent-reader/assets/obsidian/patents.base.yaml` (config)
- `skills/patent-reader/references/clue_vocab.yaml` (config)
- `skills/patent-reader/references/ipc_application_hints.yaml` (config)
- `skills/patent-reader/references/patent_domain_rules.yaml` (config)
- `skills/patent-reader/references/patent_pdf_sources.yaml` (config)
- `skills/patent-reader/references/schemas/appearance.schema.yaml` (config)
- `skills/patent-reader/references/schemas/claim_features.schema.yaml` (config)
- `skills/patent-reader/references/schemas/structure.schema.yaml` (config)
- `skills/patent-reader/references/tech_effect_hints.yaml` (config)
- `skills/patent-reader/references/text_vocab.yaml` (config)
- `skills/patent-reader/tools/crawl/requirements-cnipa.txt` (manifest)
- `skills/patent-reader/tools/requirements.txt` (manifest)
- `skills/patent-search/config.yaml` (config)
- `skills/patent-search/references/patent_type_search.yaml` (config)
- `skills/patent-search/tools/requirements-cnipa.txt` (manifest)

## Top-level layout

- `skills` — 505 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (1 x lockfile excluded; 3 x vendored/generated directory excluded).
- File skills/patent-disclosure/tests/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File skills/patent-reader/tests/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File skills/patent-reader/tools/analyze/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File skills/patent-reader/tools/extract/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File skills/patent-reader/tools/shared/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File skills/patent-reader/tools/vault/__init__.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b4bbec6f0a1c3c32a904faabeb249639c0b30d98` is the revision these paths and observations refer to.
