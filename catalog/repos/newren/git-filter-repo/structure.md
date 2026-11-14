# Project structure: newren/git-filter-repo

**Analysed commit:** `d7b75aca907380f608892cc289e616f195427b99`

**Commit reference:** [d7b75aca907380f608892cc289e616f195427b99](https://github.com/newren/git-filter-repo/commit/d7b75aca907380f608892cc289e616f195427b99)

**Tree at this commit:** [newren/git-filter-repo@d7b75aca9073](https://github.com/newren/git-filter-repo/tree/d7b75aca907380f608892cc289e616f195427b99)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | newren/git-filter-repo |
| Description | Quickly rewrite git repository history (filter-branch replacement) |
| Stars | 13521 |
| Forks | 1023 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `d7b75aca907380f608892cc289e616f195427b99` |
| Retrieved at | 2026-11-14T19:09:48.425445+00:00 |
| Files in this snapshot | 72 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    test.yml
  dependabot.yml
Documentation/  (6 files)
  Contributing.md
  FAQ.md
  converting-from-bfg-repo-cleaner.md
  converting-from-filter-branch.md
  examples-from-user-filed-issues.md
  git-filter-repo.txt
contrib/  (9 files)
  filter-repo-demos/  (9 files)
    README.md
    barebones-example
    bfg-ish
    clean-ignore
    convert-svnexternals
    filter-lamely
    insert-beginning
    lint-history
    signed-off-by
t/  (46 files)
  t9390/  (24 files)
    basic
    basic-filename
    basic-mailmap
    basic-message
    basic-numbers
    basic-replace
    basic-ten
    basic-twenty
    degenerate
    degenerate-evil-merge
    degenerate-globme
    degenerate-keepme
    degenerate-keepme-noff
    degenerate-moduleA
    empty
    empty-keepme
    less-empty-keepme
    more-empty-keepme
    sample-mailmap
    sample-message
    sample-replace
    unusual
    unusual-filtered
    unusual-mailmap
  t9391/  (10 files)
    commit_info.py
    create_fast_export_output.py
    emoji-repo
    erroneous.py
    file_filter.py
    print_progress.py
    rename-master-to-develop.py
    splice_repos.py
    strip-cvs-keywords.py
    unusual.py
  t9393/  (2 files)
    lfs
    simple
  t9394/  (1 files)
    date-order
  run_coverage
  run_tests
  t9390-filter-repo-basics.sh
  t9391-filter-repo-lib-usage.sh
  t9392-filter-repo-python-callback.sh
  t9393-filter-repo-rerun.sh
  t9394-filter-repo-sanity-checks-and-bigger-repo-setup.sh
  test-lib-functions.sh
  test-lib.sh
.gitattributes
.gitignore
COPYING
COPYING.gpl
COPYING.mit
INSTALL.md
Makefile
README.md
pyproject.toml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| t package | library | Observed | Groups 16 file(s) under t package (observed from repository paths and static analysis). Observed top-level classes: InterleaveRepositories. Observed top-level functions: change_up_them_commits, drop_file_by_contents, dr… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/test.yml` (ci)
- `pyproject.toml` (manifest)

## Top-level layout

- `t` — 46 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `contrib` — 9 analysed file(s)
- `Documentation` — 6 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d7b75aca907380f608892cc289e616f195427b99` is the revision these paths and observations refer to.
