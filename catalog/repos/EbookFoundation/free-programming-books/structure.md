# Project structure: EbookFoundation/free-programming-books

**Analysed commit:** `10e33dd516cc53864e6bece7e6bd51f2a035d06c`

**Commit reference:** [10e33dd516cc53864e6bece7e6bd51f2a035d06c](https://github.com/EbookFoundation/free-programming-books/commit/10e33dd516cc53864e6bece7e6bd51f2a035d06c)

**Tree at this commit:** [EbookFoundation/free-programming-books@10e33dd516cc](https://github.com/EbookFoundation/free-programming-books/tree/10e33dd516cc53864e6bece7e6bd51f2a035d06c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | EbookFoundation/free-programming-books |
| Description | :books: Freely available programming books |
| Stars | 401591 |
| Forks | 67849 |
| Licence | CC-BY-4.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `10e33dd516cc53864e6bece7e6bd51f2a035d06c` |
| Retrieved at | 2026-11-14T19:05:59.279380+00:00 |
| Files in this snapshot | 233 |

## Directory tree

```text
.github/  (10 files)
  actions/  (1 files)
    awesomebot-gh-summary-action/  (1 files)
      … 1 files under this directory
  workflows/  (7 files)
    check-urls.yml
    comment-pr.yml
    detect-conflicting-prs.yml
    fpb-lint.yml
    issues-pinner.yml
    rtl-ltr-linter.yml
    stale.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
_includes/  (1 files)
  head-custom.html
books/  (48 files)
  free-programming-books-ar.md
  free-programming-books-az.md
  free-programming-books-bg.md
  free-programming-books-bn.md
  free-programming-books-ca.md
  free-programming-books-cs-cp.md
  free-programming-books-cs.md
  free-programming-books-da.md
  free-programming-books-de.md
  free-programming-books-el.md
  free-programming-books-en.md
  free-programming-books-es.md
  free-programming-books-et.md
  free-programming-books-fa_IR.md
  free-programming-books-fi.md
  free-programming-books-fr.md
  free-programming-books-he.md
  free-programming-books-hi.md
  free-programming-books-hu.md
  free-programming-books-hy.md
  free-programming-books-id.md
  free-programming-books-it.md
  free-programming-books-ja.md
  free-programming-books-ko.md
  … 24 more files
casts/  (21 files)
  free-podcasts-screencasts-ar.md
  free-podcasts-screencasts-cs.md
  free-podcasts-screencasts-de.md
  free-podcasts-screencasts-en.md
  free-podcasts-screencasts-es.md
  free-podcasts-screencasts-fa_IR.md
  free-podcasts-screencasts-fi.md
  free-podcasts-screencasts-fr.md
  free-podcasts-screencasts-he.md
  free-podcasts-screencasts-id.md
  free-podcasts-screencasts-my.md
  free-podcasts-screencasts-nl.md
  free-podcasts-screencasts-pl.md
  free-podcasts-screencasts-pt_BR.md
  free-podcasts-screencasts-pt_PT.md
  free-podcasts-screencasts-ru.md
  free-podcasts-screencasts-si.md
  free-podcasts-screencasts-sv.md
  free-podcasts-screencasts-tr.md
  free-podcasts-screencasts-uk.md
  free-podcasts-screencasts-zh.md
courses/  (41 files)
  free-courses-ar.md
  free-courses-bg.md
  free-courses-bn.md
  free-courses-de.md
  free-courses-el.md
  free-courses-en.md
  free-courses-es.md
  free-courses-fa_IR.md
  free-courses-fi.md
  free-courses-fr.md
  free-courses-he.md
  free-courses-hi.md
  free-courses-id.md
  free-courses-it.md
  free-courses-ja.md
  free-courses-kk.md
  free-courses-km.md
  free-courses-kn.md
  free-courses-ko.md
  free-courses-ml.md
  free-courses-mr.md
  free-courses-my.md
  free-courses-ne.md
  free-courses-no.md
  … 17 more files
docs/  (94 files)
  CODE_OF_CONDUCT-bn.md
  CODE_OF_CONDUCT-bs.md
  CODE_OF_CONDUCT-de.md
  CODE_OF_CONDUCT-el.md
  CODE_OF_CONDUCT-es.md
  CODE_OF_CONDUCT-fa_IR.md
  CODE_OF_CONDUCT-fil.md
  CODE_OF_CONDUCT-fr.md
  CODE_OF_CONDUCT-hi.md
  CODE_OF_CONDUCT-id.md
  CODE_OF_CONDUCT-it.md
  CODE_OF_CONDUCT-ja.md
  CODE_OF_CONDUCT-km.md
  CODE_OF_CONDUCT-kn.md
  CODE_OF_CONDUCT-ko.md
  CODE_OF_CONDUCT-ml.md
  CODE_OF_CONDUCT-mr.md
  CODE_OF_CONDUCT-no.md
  CODE_OF_CONDUCT-np.md
  CODE_OF_CONDUCT-pl.md
  CODE_OF_CONDUCT-pt_BR.md
  CODE_OF_CONDUCT-ru.md
  CODE_OF_CONDUCT-si.md
  CODE_OF_CONDUCT-sl.md
  … 70 more files
more/  (11 files)
  free-programming-cheatsheets.md
  free-programming-interactive-tutorials-de.md
  free-programming-interactive-tutorials-en.md
  free-programming-interactive-tutorials-ja.md
  free-programming-interactive-tutorials-ru.md
  free-programming-interactive-tutorials-zh.md
  free-programming-playgrounds-de.md
  free-programming-playgrounds-ru.md
  free-programming-playgrounds-zh.md
  free-programming-playgrounds.md
  problem-sets-competitive-programming.md
scripts/  (2 files)
  rtl_ltr_linter.py
  rtl_ltr_linter_config.yml
.editorconfig
.gitignore
LICENSE
README.md
_config.yml
```

## Entry points

- [scripts/rtl_ltr_linter.py:604](https://github.com/EbookFoundation/free-programming-books/blob/10e33dd516cc53864e6bece7e6bd51f2a035d06c/scripts/rtl_ltr_linter.py#L604)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: get_changed_lines_for_file, is_rtl_filename, lint_file, load_config, main, split_by_span. |

## Important files

- `.editorconfig` (config)
- `.github/actions/awesomebot-gh-summary-action/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/check-urls.yml` (ci)
- `.github/workflows/comment-pr.yml` (ci)
- `.github/workflows/detect-conflicting-prs.yml` (ci)
- `.github/workflows/fpb-lint.yml` (ci)
- `.github/workflows/issues-pinner.yml` (ci)
- `.github/workflows/rtl-ltr-linter.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `_config.yml` (config)
- `scripts/rtl_ltr_linter_config.yml` (config)

## Top-level layout

- `docs` — 94 analysed file(s)
- `books` — 48 analysed file(s)
- `courses` — 41 analysed file(s)
- `casts` — 21 analysed file(s)
- `more` — 11 analysed file(s)
- `.github` — 10 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `scripts` — 2 analysed file(s)
- `_includes` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `10e33dd516cc53864e6bece7e6bd51f2a035d06c` is the revision these paths and observations refer to.
