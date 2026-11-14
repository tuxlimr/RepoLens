# Project structure: virgiliojr94/book-to-skill

**Analysed commit:** `e7bb659d3261491c8b28793dcb9102fa64a46c22`

**Commit reference:** [e7bb659d3261491c8b28793dcb9102fa64a46c22](https://github.com/virgiliojr94/book-to-skill/commit/e7bb659d3261491c8b28793dcb9102fa64a46c22)

**Tree at this commit:** [virgiliojr94/book-to-skill@e7bb659d3261](https://github.com/virgiliojr94/book-to-skill/tree/e7bb659d3261491c8b28793dcb9102fa64a46c22)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | virgiliojr94/book-to-skill |
| Description | Turn any technical book PDF into a Claude Code skill — ready to study, reference, and use while you work. |
| Stars | 37865 |
| Forks | 4029 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `e7bb659d3261491c8b28793dcb9102fa64a46c22` |
| Retrieved at | 2026-11-14T19:06:47.251900+00:00 |
| Files in this snapshot | 134 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    ci.yml
    codeql.yml
    deploy-docs.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
book_to_skill/  (17 files)
  parsers/  (8 files)
    __init__.py
    calibre.py
    docx.py
    epub.py
    html.py
    pdf.py
    rtf.py
    text.py
  __init__.py
  __main__.py
  cli.py
  config.py
  dependencies.py
  exceptions.py
  pdf_inspector_integration.py
  sanitize.py
  utils.py
docs/  (11 files)
  research/  (1 files)
    progressive-disclosure-evals.md
  404.md
  CNAME
  architecture.md
  faq.md
  how-it-works.md
  index.md
  install.md
  performance.md
  robots.txt
  usage.md
evals/  (4 files)
  fixtures/  (4 files)
    pd00-synthetic-book.txt
    pd03-book.txt
    pd03-metadata.json
    replay_trajectories.json
overrides/  (1 files)
  main.html
scripts/  (1 files)
  extract.py
tests/  (68 files)
  evals/  (5 files)
    test_manifest.py
    test_paper_flat.py
    test_replay.py
    test_score.py
    test_score_robustness.py
  fixtures/  (1 files)
    generate_pdf_page_provenance.py
  test_batch_resilience_unreadable.py
  test_book_to_skill.py
  test_calibre_stale_output.py
  test_chapter_content_split.py
  test_chapter_method_reported.py
  test_chapter_numeric_false_positives.py
  test_cjk_radical_normalization.py
  test_cjk_supplementary_plane.py
  test_code_fence_closers.py
  test_corpus_newlines.py
  test_dependency_install_semantics.py
  test_discovery_tax.py
  test_docling_fallback.py
  test_docs_host_lists.py
  test_epub_container_entities.py
  test_epub_image_reporting.py
  test_epub_utf16.py
  test_fingerprint.py
  test_hermes_host_support.py
  test_html_block_boundaries.py
  test_html_boilerplate_extraction.py
  test_intro_and_support_note.py
  test_isolated_install_hint.py
  test_malformed_text_bom.py
  … 38 more files
tools/  (7 files)
  evals/  (4 files)
    manifest.py
    paper_flat.py
    replay.py
    score.py
  discovery_tax.py
  scan_generated_skill.py
  validate_skill.py
.gitattributes
.gitignore
AGENTS.md
BACKERS.md
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
LICENSE.md
README.md
README.ru.md
README.zh-CN.md
SECURITY-NOTICE.md
SECURITY.md
SKILL.md
cliff.toml
mkdocs.yml
pyproject.toml
```

## Entry points

- [book_to_skill/__main__.py:3](https://github.com/virgiliojr94/book-to-skill/blob/e7bb659d3261491c8b28793dcb9102fa64a46c22/book_to_skill/__main__.py#L3)
- [book_to_skill/cli.py](https://github.com/virgiliojr94/book-to-skill/blob/e7bb659d3261491c8b28793dcb9102fa64a46c22/book_to_skill/cli.py)
- [scripts/extract.py:33](https://github.com/virgiliojr94/book-to-skill/blob/e7bb659d3261491c8b28793dcb9102fa64a46c22/scripts/extract.py#L33)
- [tools/discovery_tax.py:202](https://github.com/virgiliojr94/book-to-skill/blob/e7bb659d3261491c8b28793dcb9102fa64a46c22/tools/discovery_tax.py#L202)
- [tools/evals/manifest.py:195](https://github.com/virgiliojr94/book-to-skill/blob/e7bb659d3261491c8b28793dcb9102fa64a46c22/tools/evals/manifest.py#L195)
- [tools/evals/paper_flat.py:104](https://github.com/virgiliojr94/book-to-skill/blob/e7bb659d3261491c8b28793dcb9102fa64a46c22/tools/evals/paper_flat.py#L104)
- [tools/evals/replay.py:44](https://github.com/virgiliojr94/book-to-skill/blob/e7bb659d3261491c8b28793dcb9102fa64a46c22/tools/evals/replay.py#L44)
- [tools/scan_generated_skill.py:366](https://github.com/virgiliojr94/book-to-skill/blob/e7bb659d3261491c8b28793dcb9102fa64a46c22/tools/scan_generated_skill.py#L366)
- [tools/validate_skill.py:314](https://github.com/virgiliojr94/book-to-skill/blob/e7bb659d3261491c8b28793dcb9102fa64a46c22/tools/validate_skill.py#L314)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| book_to_skill package | library | Observed | Groups 14 file(s) under book_to_skill package (observed from repository paths and static analysis). Observed top-level classes: ExtractionError, _HTMLTextExtractor. Observed top-level functions: _chapter_number, _chapte… |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: default_output_dir, supported_formats_message. |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Finding, ScanError. Observed top-level functions: _budgets, _chunks, _collect_skill_files,… |
| Tests | test | Observed | Groups 68 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: PdfPageSidecarTests, RtfLineBreakTests, TestAcceptedOverCountCost, TestBalancedFencesStillSuppressHeadings,… |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). Observed top-level functions: _count, _state, aggregate, score, score_trajectory. |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/deploy-docs.yml` (ci)
- `cliff.toml` (config)
- `evals/fixtures/pd03-metadata.json` (config)
- `evals/fixtures/replay_trajectories.json` (config)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 68 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `book_to_skill` — 17 analysed file(s)
- `docs` — 11 analysed file(s)
- `.github` — 8 analysed file(s)
- `tools` — 7 analysed file(s)
- `evals` — 4 analysed file(s)
- `overrides` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e7bb659d3261491c8b28793dcb9102fa64a46c22` is the revision these paths and observations refer to.
