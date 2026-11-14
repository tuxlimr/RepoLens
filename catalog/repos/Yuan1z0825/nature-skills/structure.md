# Project structure: Yuan1z0825/nature-skills

**Analysed commit:** `7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8`

**Commit reference:** [7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8](https://github.com/Yuan1z0825/nature-skills/commit/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8)

**Tree at this commit:** [Yuan1z0825/nature-skills@7bff1d0539c0](https://github.com/Yuan1z0825/nature-skills/tree/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Yuan1z0825/nature-skills |
| Description | 符合nature论文学术表达和科研绘图的Skill |
| Stars | 53545 |
| Forks | 2783 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8` |
| Retrieved at | 2026-11-14T19:06:31.449381+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.codex-plugin/  (1 files)
  plugin.json
.github/  (10 files)
  workflows/  (9 files)
    test-content-contracts.yml
    test-paper-trans.yml
    test-skill-tooling.yml
    update-star-history.yml
    validate-readme-mirror.yml
    validate-repository.yml
    validate-skill-index.yml
    validate-skill-metadata.yml
    validate-workflows.yml
  requirements-ci.txt
RDA-results/  (3 files)
  README.md
  SHA256SUMS.txt
  analysis.R
assets/  (3 files)
  star-history-20261113T022420Z.svg
  star-history-data.json
  star-history.svg
docs/  (5 files)
  nature-paper-card-tutorial.md
  nature-paper-card-tutorial_EN.md
  open-source-agent-frameworks.md
  open-source-agent-frameworks_EN.md
  skill-scope-smoke-evaluation.md
scripts/  (36 files)
  tests/  (26 files)
    test-autoupdate-dest-tilde.sh
    test-autoupdate-state-isolation.sh
    test-update-codex-skills-dest-tilde.sh
    test-update-codex-skills-safety.sh
    test_academic_search_openalex_key.py
    test_discussion_argument_language.py
    test_generate_star_history.py
    test_main_text_discipline.py
    test_nature_abstract_guidance.py
    test_nature_figure_ai_graphical_abstract.py
    test_nature_figure_collision_audit.py
    test_nature_figure_multipanel_evidence.py
    test_nature_figure_openrouter_errors.py
    test_nature_figure_panel_alignment.py
    test_nature_figure_pdf_text_audit.py
    test_nature_figure_script_regressions.py
    test_nature_figure_svg_audit.py
    test_nature_introduction_guidance.py
    test_nature_results_discussion_guidance.py
    test_nature_social_science.py
    test_nature_submission_requirements.py
    test_nmi_submission_requirements.py
    test_paper2ppt_group_bounds.py
    test_update_reference_tocs.py
    … 2 more files
  autoupdate-skills.sh
  generate-star-history.py
  update-codex-skills.sh
  update-reference-tocs.py
  validate-readme-mirror.py
  validate-readmes.py
  validate-repository.py
  validate-skill-index.py
  validate-skill-metadata.py
  validate-workflows.py
skills/  (731 files)
  nature-academic-search/  (54 files)
    agents/  (1 files)
      … 1 files under this directory
    config/  (3 files)
      … 3 files under this directory
    mcp-server/  (25 files)
      … 25 files under this directory
    references/  (14 files)
      … 14 files under this directory
    scripts/  (4 files)
      … 4 files under this directory
    static/  (2 files)
      … 2 files under this directory
    README.md
    README_EN.md
    SKILL.md
    install.sh
    manifest.yaml
  nature-citation/  (17 files)
    agents/  (1 files)
      … 1 files under this directory
    data/  (1 files)
      … 1 files under this directory
    evals/  (1 files)
      … 1 files under this directory
    references/  (4 files)
      … 4 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    static/  (3 files)
      … 3 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-data/  (15 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (7 files)
      … 7 files under this directory
    static/  (3 files)
      … 3 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-downloader/  (70 files)
    agents/  (1 files)
      … 1 files under this directory
    data/  (3 files)
      … 3 files under this directory
    docs/  (2 files)
      … 2 files under this directory
    examples/  (3 files)
      … 3 files under this directory
    references/  (2 files)
      … 2 files under this directory
    scripts/  (25 files)
      … 25 files under this directory
    src/  (5 files)
      … 5 files under this directory
    tests/  (21 files)
      … 21 files under this directory
    .gitattributes
    .gitignore
    LICENSE
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
    requirements.txt
  nature-experiment-log/  (11 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    templates/  (3 files)
      … 3 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-figure/  (73 files)
    agents/  (1 files)
      … 1 files under this directory
    assets/  (28 files)
      … 28 files under this directory
    evals/  (1 files)
      … 1 files under this directory
    references/  (21 files)
      … 21 files under this directory
    scripts/  (10 files)
      … 10 files under this directory
    static/  (4 files)
      … 4 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
    requirements.txt
  nature-image2ppt/  (91 files)
    agents/  (1 files)
      … 1 files under this directory
    cli/  (29 files)
      … 29 files under this directory
    prompts/  (2 files)
      … 2 files under this directory
    references/  (11 files)
      … 11 files under this directory
    schemas/  (1 files)
      … 1 files under this directory
    scripts/  (9 files)
      … 9 files under this directory
    tests/  (30 files)
      … 30 files under this directory
    .gitignore
    LICENSE
    README.md
    README_EN.md
    SKILL.md
    config.example.yaml
    manifest.yaml
    requirements.txt
  nature-literature-pipeline/  (12 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (6 files)
      … 6 files under this directory
    templates/  (1 files)
      … 1 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-paper-card/  (22 files)
    agents/  (1 files)
      … 1 files under this directory
    evals/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    static/  (9 files)
      … 9 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-paper-to-patent/  (68 files)
    agents/  (1 files)
      … 1 files under this directory
    evals/  (1 files)
      … 1 files under this directory
    references/  (18 files)
      … 18 files under this directory
    scripts/  (19 files)
      … 19 files under this directory
    static/  (17 files)
      … 17 files under this directory
    tests/  (7 files)
      … 7 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
    requirements.txt
  nature-paper-trans/  (12 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    tests/  (4 files)
      … 4 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
    requirements.txt
  nature-paper-xray/  (7 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-paper2ppt/  (19 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    static/  (10 files)
      … 10 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-paper2word/  (10 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    README_EN.md
    SKILL.md
    UPSTREAM-LICENSE.txt
    manifest.yaml
  nature-polishing/  (33 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (7 files)
      … 7 files under this directory
    static/  (21 files)
      … 21 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-proposal-writer/  (36 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (20 files)
      … 20 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    templates/  (8 files)
      … 8 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-reader/  (20 files)
    agents/  (1 files)
      … 1 files under this directory
    evals/  (1 files)
      … 1 files under this directory
    references/  (5 files)
      … 5 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    static/  (8 files)
      … 8 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-ref-verifier/  (6 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (1 files)
      … 1 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-response/  (38 files)
    agents/  (1 files)
      … 1 files under this directory
    examples/  (3 files)
      … 3 files under this directory
    references/  (11 files)
      … 11 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    static/  (2 files)
      … 2 files under this directory
    templates/  (3 files)
      … 3 files under this directory
    tests/  (13 files)
      … 13 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-reviewer/  (21 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (10 files)
      … 10 files under this directory
    tests/  (5 files)
      … 5 files under this directory
    CHANGELOG.md
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-shared/  (21 files)
    agents/  (1 files)
      … 1 files under this directory
    core/  (11 files)
      … 11 files under this directory
    journal-formats/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-social-science/  (14 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (9 files)
      … 9 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-statistics/  (11 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (6 files)
      … 6 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
  nature-writing/  (50 files)
    agents/  (1 files)
      … 1 files under this directory
    references/  (42 files)
      … 42 files under this directory
    static/  (3 files)
      … 3 files under this directory
    README.md
    README_EN.md
    SKILL.md
    manifest.yaml
.gitattributes
.gitignore
LICENSE
README.md
README_EN.md
index.html
pr-body-readme-mirror.md
pr-body-skill-index.md
pr-body-workflow.md
```

## Entry points

- [skills/nature-downloader/src/config.py:158](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/skills/nature-downloader/src/config.py#L158)
- [skills/nature-downloader/src/health_check.py:148](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/skills/nature-downloader/src/health_check.py#L148)
- [skills/nature-downloader/src/schools_loader.py:126](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/skills/nature-downloader/src/schools_loader.py#L126)
- [skills/nature-downloader/src/validators.py:186](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/skills/nature-downloader/src/validators.py#L186)
- [skills/nature-downloader/src/wizard.py:573](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/skills/nature-downloader/src/wizard.py#L573)
- [scripts/generate-star-history.py:804](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/scripts/generate-star-history.py#L804)
- [scripts/update-reference-tocs.py:79](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/scripts/update-reference-tocs.py#L79)
- [scripts/validate-readme-mirror.py:88](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/scripts/validate-readme-mirror.py#L88)
- [scripts/validate-readmes.py:83](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/scripts/validate-readmes.py#L83)
- [scripts/validate-repository.py:162](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/scripts/validate-repository.py#L162)
- [scripts/validate-skill-index.py:95](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/scripts/validate-skill-index.py#L95)
- [scripts/validate-skill-metadata.py:286](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/scripts/validate-skill-metadata.py#L286)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 74 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. Observed top-level functions: get_config. |
| Application entry point | entrypoint | Observed | Groups 106 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Arrow3D, Candidate, CollisionFinding, EpubSearchHit, FilledRegion, Finding. Observed top… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 48 file(s) under skills package (observed from repository paths and static analysis). Observed top-level classes: AcademicSearchError, ArxivSource, ConfigError, CrossRefSource, DataSourceError, FormulaRenderError… |
| Tests | test | Observed | Groups 126 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH sources.crossref.get_config, PATCH sources.crossref.requests.get, PATCH academic_search_server._crossref, PATCH… |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.github/requirements-ci.txt` (manifest)
- `.github/workflows/test-content-contracts.yml` (ci)
- `.github/workflows/test-paper-trans.yml` (ci)
- `.github/workflows/test-skill-tooling.yml` (ci)
- `.github/workflows/update-star-history.yml` (ci)
- `.github/workflows/validate-readme-mirror.yml` (ci)
- `.github/workflows/validate-repository.yml` (ci)
- `.github/workflows/validate-skill-index.yml` (ci)
- `.github/workflows/validate-skill-metadata.yml` (ci)
- `.github/workflows/validate-workflows.yml` (ci)
- `assets/star-history-data.json` (config)
- `skills/nature-academic-search/agents/openai.yaml` (config)
- `skills/nature-academic-search/config/mcp-snippet.json` (config)
- `skills/nature-academic-search/config/settings-snippet.json` (config)
- `skills/nature-academic-search/config/triggers-academic-search.toml` (config)
- `skills/nature-academic-search/manifest.yaml` (config)
- `skills/nature-academic-search/mcp-server/config.toml` (config)
- `skills/nature-academic-search/mcp-server/requirements.txt` (manifest)
- `skills/nature-citation/agents/openai.yaml` (config)
- `skills/nature-citation/data/npj-journals.json` (config)
- `skills/nature-citation/evals/evals.json` (config)
- `skills/nature-citation/manifest.yaml` (config)
- `skills/nature-data/agents/openai.yaml` (config)
- `skills/nature-data/manifest.yaml` (config)
- `skills/nature-downloader/agents/openai.yaml` (config)
- `skills/nature-downloader/data/publishers.json` (config)
- `skills/nature-downloader/data/school.schema.json` (config)
- `skills/nature-downloader/data/schools.yaml` (config)
- `skills/nature-downloader/manifest.yaml` (config)
- `skills/nature-downloader/requirements.txt` (manifest)
- `skills/nature-experiment-log/agents/openai.yaml` (config)
- `skills/nature-experiment-log/manifest.yaml` (config)
- `skills/nature-figure/agents/openai.yaml` (config)
- `skills/nature-figure/evals/evals.json` (config)
- `skills/nature-figure/manifest.yaml` (config)
- `skills/nature-figure/requirements.txt` (manifest)
- `skills/nature-image2ppt/agents/openai.yaml` (config)
- `skills/nature-image2ppt/cli/pyproject.toml` (manifest)
- `skills/nature-image2ppt/config.example.yaml` (config)
- `skills/nature-image2ppt/manifest.yaml` (config)
- `skills/nature-image2ppt/requirements.txt` (manifest)
- `skills/nature-image2ppt/schemas/page-manifest-v2.schema.json` (config)
- `skills/nature-literature-pipeline/agents/openai.yaml` (config)
- `skills/nature-literature-pipeline/manifest.yaml` (config)
- `skills/nature-paper-card/agents/openai.yaml` (config)
- `skills/nature-paper-card/evals/evals.json` (config)
- `skills/nature-paper-card/manifest.yaml` (config)
- `skills/nature-paper-to-patent/agents/openai.yaml` (config)
- `skills/nature-paper-to-patent/evals/evals.json` (config)
- `skills/nature-paper-to-patent/manifest.yaml` (config)
- `skills/nature-paper-to-patent/requirements.txt` (manifest)
- `skills/nature-paper-to-patent/scripts/disclosure/package.json` (manifest)
- `skills/nature-paper-to-patent/scripts/disclosure/requirements-cnipa.txt` (manifest)
- `skills/nature-paper-trans/agents/openai.yaml` (config)
- `skills/nature-paper-trans/manifest.yaml` (config)
- `skills/nature-paper-trans/requirements.txt` (manifest)
- `skills/nature-paper-xray/agents/openai.yaml` (config)
- `skills/nature-paper-xray/manifest.yaml` (config)
- `skills/nature-paper2ppt/agents/openai.yaml` (config)
- `skills/nature-paper2ppt/manifest.yaml` (config)
- `skills/nature-paper2word/agents/openai.yaml` (config)
- `skills/nature-paper2word/manifest.yaml` (config)
- `skills/nature-polishing/agents/openai.yaml` (config)
- `skills/nature-polishing/manifest.yaml` (config)
- `skills/nature-proposal-writer/agents/openai.yaml` (config)
- `skills/nature-proposal-writer/manifest.yaml` (config)
- `skills/nature-reader/agents/openai.yaml` (config)
- `skills/nature-reader/evals/evals.json` (config)
- `skills/nature-reader/manifest.yaml` (config)
- `skills/nature-ref-verifier/agents/openai.yaml` (config)
- `skills/nature-ref-verifier/manifest.yaml` (config)
- `skills/nature-response/agents/openai.yaml` (config)
- `skills/nature-response/manifest.yaml` (config)
- `skills/nature-reviewer/agents/openai.yaml` (config)
- `skills/nature-reviewer/manifest.yaml` (config)
- `skills/nature-shared/agents/openai.yaml` (config)
- `skills/nature-shared/manifest.yaml` (config)
- `skills/nature-social-science/agents/openai.yaml` (config)
- `skills/nature-social-science/manifest.yaml` (config)
- `skills/nature-statistics/agents/openai.yaml` (config)
- `skills/nature-statistics/manifest.yaml` (config)
- `skills/nature-writing/agents/openai.yaml` (config)
- `skills/nature-writing/manifest.yaml` (config)

## Top-level layout

- `skills` — 731 analysed file(s)
- `scripts` — 36 analysed file(s)
- `.github` — 10 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `docs` — 5 analysed file(s)
- `RDA-results` — 3 analysed file(s)
- `assets` — 3 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8` is the revision these paths and observations refer to.
