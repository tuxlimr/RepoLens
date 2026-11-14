# Project structure: donnemartin/awesome-aws

**Analysed commit:** `5a49af5f118cef44bd91cdcb7aafe045ef31ad60`

**Commit reference:** [5a49af5f118cef44bd91cdcb7aafe045ef31ad60](https://github.com/donnemartin/awesome-aws/commit/5a49af5f118cef44bd91cdcb7aafe045ef31ad60)

**Tree at this commit:** [donnemartin/awesome-aws@5a49af5f118c](https://github.com/donnemartin/awesome-aws/tree/5a49af5f118cef44bd91cdcb7aafe045ef31ad60)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | donnemartin/awesome-aws |
| Description | A curated list of awesome Amazon Web Services (AWS) libraries, open source repos, guides, blogs, and other resources.  Featuring the Fiery Meter of AWSome. |
| Stars | 14200 |
| Forks | 1912 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `5a49af5f118cef44bd91cdcb7aafe045ef31ad60` |
| Retrieved at | 2026-11-14T19:09:30.987209+00:00 |
| Files in this snapshot | 37 |

## Directory tree

```text
.github/  (1 files)
  PULL_REQUEST_TEMPLATE.md
awesome/  (5 files)
  lib/  (2 files)
    __init__.py
    github.py
  __init__.py
  awesome.py
  awesome_cli.py
scripts/  (7 files)
  create_changelog.sh
  create_readme_rst.sh
  run_code_checks.sh
  set_changelog_as_readme.sh
  set_changelog_as_readme_undo.sh
  update_docs.sh
  upload_pypi.sh
tests/  (10 files)
  data/  (4 files)
    README.md
    README_RESULT.md
    __init__.py
    readme_expected.py
  __init__.py
  mock_github.py
  run_tests.py
  test_awesome.py
  test_awesome_cli.py
  test_cli.py
.gitignore
.travis.yml
CHANGELOG.md
CHANGELOG.rst
CHECKLIST.md
CONTRIBUTING.md
CREDITS.md
LICENSE.md
README.md
codecov.yml
requirements-dev.txt
setup.cfg
setup.py
tox.ini
```

## Entry points

- [awesome/awesome_cli.py:22](https://github.com/donnemartin/awesome-aws/blob/5a49af5f118cef44bd91cdcb7aafe045ef31ad60/awesome/awesome_cli.py#L22)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| awesome package | library | Observed | Groups 5 file(s) under awesome package (observed from repository paths and static analysis). Observed top-level classes: Awesome, AwesomeCli, GitHub. |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH awesome.awesome.click. Observed top-level classes: AwesomeCliTest, AwesomeTest, CliTest, MockGitHub, MockGitHubA… |

## Important files

- `.travis.yml` (ci)
- `codecov.yml` (config)
- `requirements-dev.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `(root files)` — 14 analysed file(s)
- `tests` — 10 analysed file(s)
- `scripts` — 7 analysed file(s)
- `awesome` — 5 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5a49af5f118cef44bd91cdcb7aafe045ef31ad60` is the revision these paths and observations refer to.
