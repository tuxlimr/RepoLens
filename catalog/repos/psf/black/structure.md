# Project structure: psf/black

**Analysed commit:** `b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd`

**Commit reference:** [b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd](https://github.com/psf/black/commit/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd)

**Tree at this commit:** [psf/black@b10cbe43b816](https://github.com/psf/black/tree/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | psf/black |
| Description | The uncompromising Python code formatter |
| Stars | 42172 |
| Forks | 2991 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd` |
| Retrieved at | 2026-11-14T19:06:40.250824+00:00 |
| Files in this snapshot | 572 |

## Directory tree

```text
.github/  (22 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.md
    config.yml
    docs-issue.md
    feature_request.md
    style_issue.md
  workflows/  (13 files)
    changelog.yml
    cut_release.yml
    diff_shades.yml
    diff_shades_comment.yml
    docker.yml
    docs.yml
    fuzz.yml
    lint.yml
    prepare_release.yml
    pypi_upload.yml
    release_tests.yml
    test.yml
    zizmor.yml
  CODE_OF_CONDUCT.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  zizmor.yml
action/  (1 files)
  main.py
autoload/  (1 files)
  black.vim
docs/  (46 files)
  _static/  (2 files)
    license.svg
    pypi_template.svg
  compatible_configs/  (13 files)
    flake8/  (3 files)
      … 3 files under this directory
    isort/  (4 files)
      … 4 files under this directory
    pycodestyle/  (3 files)
      … 3 files under this directory
    pylint/  (3 files)
      … 3 files under this directory
  contributing/  (5 files)
    gauging_changes.md
    index.md
    issue_triage.md
    release_process.md
    the_basics.md
  guides/  (4 files)
    index.md
    introducing_black_to_your_project.md
    using_black_with_jupyter_notebooks.md
    using_black_with_other_tools.md
  integrations/  (5 files)
    doctest_formatting.md
    editors.md
    github_actions.md
    index.md
    pre-commit.md
  the_black_code_style/  (3 files)
    current_style.md
    future_style.md
    index.md
  usage_and_configuration/  (5 files)
    black_as_a_server.md
    black_docker_image.md
    file_collection_and_discovery.md
    index.md
    the_basics.md
  Makefile
  authors.md
  change_log.md
  conf.py
  faq.md
  getting_started.md
  index.md
  license.md
  make.bat
plugin/  (1 files)
  black.vim
profiling/  (3 files)
  list_big.py
  mix_big.py
  mix_small.py
scripts/  (7 files)
  __init__.py
  diff_shades_gha_helper.py
  fuzz.py
  generate_schema.py
  make_width_table.py
  release.py
  release_tests.py
src/  (47 files)
  black/  (27 files)
    resources/  (2 files)
      … 2 files under this directory
    __init__.py
    __main__.py
    _width_table.py
    brackets.py
    cache.py
    comments.py
    concurrency.py
    const.py
    debug.py
    files.py
    handle_ipynb_magics.py
    linegen.py
    lines.py
    mode.py
    nodes.py
    numerics.py
    output.py
    parsing.py
    py.typed
    ranges.py
    report.py
    rusty.py
    schema.py
    strings.py
    … 1 more files
  blackd/  (4 files)
    __init__.py
    __main__.py
    client.py
    middlewares.py
  blib2to3/  (15 files)
    pgen2/  (8 files)
      … 8 files under this directory
    Grammar.txt
    LICENSE
    PatternGrammar.txt
    README
    __init__.py
    pygram.py
    pytree.py
  _black_version.pyi
tests/  (425 files)
  data/  (405 files)
    cases/  (323 files)
      … 323 files under this directory
    gitignore_used_on_multiple_sources/  (5 files)
      … 5 files under this directory
    ignore_directory_gitignore_tests/  (7 files)
      … 7 files under this directory
    ignore_subfolders_gitignore_tests/  (4 files)
      … 4 files under this directory
    include_exclude_tests/  (14 files)
      … 14 files under this directory
    invalid_gitignore_tests/  (3 files)
      … 3 files under this directory
    invalid_nested_gitignore_tests/  (4 files)
      … 4 files under this directory
    jupyter/  (6 files)
      … 6 files under this directory
    line_ranges_formatted/  (6 files)
      … 6 files under this directory
    miscellaneous/  (16 files)
      … 16 files under this directory
    nested_gitignore_tests/  (10 files)
      … 10 files under this directory
    project_metadata/  (4 files)
      … 4 files under this directory
    empty_pyproject.toml
    incorrect_spelling.toml
    invalid_line_ranges.toml
  __init__.py
  conftest.py
  empty.toml
  optional.py
  test.toml
  test_action.py
  test_black.py
  test_blackd.py
  test_concurrency_manager_shutdown.py
  test_docs.py
  test_format.py
  test_github_action.py
  test_ipynb.py
  test_no_ipynb.py
  test_ranges.py
  test_schedule_formatting.py
  test_schema.py
  test_tokenize.py
  test_trans.py
  util.py
.flake8
.git_archival.txt
.gitattributes
.gitignore
.pre-commit-config.yaml
.pre-commit-hooks.yaml
.prettierrc.yaml
.readthedocs.yaml
AUTHORS.md
CHANGES.md
CITATION.cff
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
SECURITY.md
action.yml
pyproject.toml
tox.ini
```

## Entry points

- [src/black/__init__.py](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/src/black/__init__.py)
- [src/blackd/__init__.py](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/src/blackd/__init__.py)
- [src/blib2to3/pgen2/driver.py:312](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/src/blib2to3/pgen2/driver.py#L312)
- [src/blib2to3/pgen2/literals.py:64](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/src/blib2to3/pgen2/literals.py#L64)
- [src/blib2to3/pgen2/tokenize.py:278](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/src/blib2to3/pgen2/tokenize.py#L278)
- [scripts/diff_shades_gha_helper.py:112](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/scripts/diff_shades_gha_helper.py#L112)
- [scripts/fuzz.py:55](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/scripts/fuzz.py#L55)
- [scripts/generate_schema.py:50](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/scripts/generate_schema.py#L50)
- [scripts/make_width_table.py:65](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/scripts/make_width_table.py#L65)
- [scripts/release.py:323](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/scripts/release.py#L323)
- [scripts/release_tests.py:103](https://github.com/psf/black/blob/b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd/scripts/release_tests.py#L103)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| black package | library | Observed | Groups 23 file(s) under black package (observed from repository paths and static analysis). Observed top-level classes: ASTSafetyError, BaseStringSplitter, BracketMatchError, BracketTracker, Cache, CannotSplit. Observed… |
| blackd package | library | Observed | Groups 1 file(s) under blackd package (observed from repository paths and static analysis). Observed top-level functions: cors. |
| blib2to3 package | library | Observed | Groups 8 file(s) under blib2to3 package (observed from repository paths and static analysis). Observed top-level classes: Base, DFAState, Grammar, Leaf, NFAState, Node. Observed top-level functions: convert, generate_gr… |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Driver, HeaderError, InvalidVariantHeader, NoGitTagsError, ReleaseRange, SourceFiles. Obs… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: BlackDClient. |
| profiling package | library | Observed | Groups 3 file(s) under profiling package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 426 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH release.get_git_tags, PATCH release.get_git_tags, PATCH release.datetime, PATCH release.get_git_tags, PATCH rel… |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/changelog.yml` (ci)
- `.github/workflows/cut_release.yml` (ci)
- `.github/workflows/diff_shades.yml` (ci)
- `.github/workflows/diff_shades_comment.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/fuzz.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/prepare_release.yml` (ci)
- `.github/workflows/pypi_upload.yml` (ci)
- `.github/workflows/release_tests.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.github/zizmor.yml` (config)
- `.pre-commit-config.yaml` (config)
- `.pre-commit-hooks.yaml` (config)
- `.prettierrc.yaml` (config)
- `.readthedocs.yaml` (config)
- `Dockerfile` (container)
- `action.yml` (config)
- `docs/compatible_configs/flake8/setup.cfg` (manifest)
- `docs/compatible_configs/flake8/tox.ini` (config)
- `docs/compatible_configs/isort/.editorconfig` (config)
- `docs/compatible_configs/isort/.isort.cfg` (config)
- `docs/compatible_configs/isort/pyproject.toml` (manifest)
- `docs/compatible_configs/isort/setup.cfg` (manifest)
- `docs/compatible_configs/pycodestyle/setup.cfg` (manifest)
- `docs/compatible_configs/pycodestyle/tox.ini` (config)
- `docs/compatible_configs/pylint/pyproject.toml` (manifest)
- `docs/compatible_configs/pylint/setup.cfg` (manifest)
- `pyproject.toml` (manifest)
- `src/black/resources/black.schema.json` (config)
- `tox.ini` (config)

## Top-level layout

- `tests` — 425 analysed file(s)
- `src` — 47 analysed file(s)
- `docs` — 46 analysed file(s)
- `.github` — 22 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `scripts` — 7 analysed file(s)
- `profiling` — 3 analysed file(s)
- `action` — 1 analysed file(s)
- `autoload` — 1 analysed file(s)
- `plugin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File tests/data/cases/pep_572_do_not_remove_parens.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File tests/data/cases/python315.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File tests/data/miscellaneous/async_as_identifier.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File tests/data/miscellaneous/invalid_header.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File tests/data/miscellaneous/pattern_matching_invalid.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File tests/data/miscellaneous/python2_detection.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b10cbe43b8169e688ab86989ddcc8ad2a53ff2cd` is the revision these paths and observations refer to.
