# Project structure: pallets/jinja

**Analysed commit:** `5ef70112a1ff19c05324ff889dd30405b1002044`

**Commit reference:** [5ef70112a1ff19c05324ff889dd30405b1002044](https://github.com/pallets/jinja/commit/5ef70112a1ff19c05324ff889dd30405b1002044)

**Tree at this commit:** [pallets/jinja@5ef70112a1ff](https://github.com/pallets/jinja/tree/5ef70112a1ff19c05324ff889dd30405b1002044)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pallets/jinja |
| Description | A very fast and expressive template engine. |
| Stars | 11817 |
| Forks | 1891 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `5ef70112a1ff19c05324ff889dd30405b1002044` |
| Retrieved at | 2026-11-14T19:10:23.335089+00:00 |
| Files in this snapshot | 105 |

## Directory tree

```text
.devcontainer/  (2 files)
  devcontainer.json
  on-create-command.sh
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    config.yml
    feature-request.md
  workflows/  (4 files)
    lock.yaml
    pre-commit.yaml
    publish.yaml
    tests.yaml
  pull_request_template.md
docs/  (21 files)
  _static/  (3 files)
    jinja-icon.svg
    jinja-logo.svg
    jinja-name.svg
  examples/  (2 files)
    cache_extension.py
    inline_gettext_extension.py
  Makefile
  api.rst
  changes.rst
  conf.py
  extensions.rst
  faq.rst
  index.rst
  integration.rst
  intro.rst
  license.rst
  make.bat
  nativetypes.rst
  sandbox.rst
  switching.rst
  templates.rst
  tricks.rst
examples/  (9 files)
  basic/  (9 files)
    templates/  (2 files)
      … 2 files under this directory
    cycle.py
    debugger.py
    inheritance.py
    test.py
    test_filter_and_linestatements.py
    test_loop_filter.py
    translate.py
scripts/  (1 files)
  generate_identifier_pattern.py
src/  (26 files)
  jinja2/  (26 files)
    __init__.py
    _identifier.py
    async_utils.py
    bccache.py
    compiler.py
    constants.py
    debug.py
    defaults.py
    environment.py
    exceptions.py
    ext.py
    filters.py
    idtracking.py
    lexer.py
    loaders.py
    meta.py
    nativetypes.py
    nodes.py
    optimizer.py
    parser.py
    py.typed
    runtime.py
    sandbox.py
    tests.py
    … 2 more files
tests/  (30 files)
  res/  (7 files)
    templates/  (5 files)
      … 5 files under this directory
    templates2/  (1 files)
      … 1 files under this directory
    __init__.py
  conftest.py
  test_api.py
  test_async.py
  test_async_filters.py
  test_bytecode_cache.py
  test_compile.py
  test_core_tags.py
  test_debug.py
  test_ext.py
  test_filters.py
  test_idtracking.py
  test_imports.py
  test_inheritance.py
  test_lexnparse.py
  test_loader.py
  test_nativetypes.py
  test_nodes.py
  test_pickle.py
  test_regression.py
  test_runtime.py
  test_security.py
  test_tests.py
  test_utils.py
.editorconfig
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
CHANGES.rst
LICENSE.txt
README.md
pyproject.toml
```

## Entry points

- [scripts/generate_identifier_pattern.py:72](https://github.com/pallets/jinja/blob/5ef70112a1ff19c05324ff889dd30405b1002044/scripts/generate_identifier_pattern.py#L72)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: build_pattern, collapse_ranges, get_characters, main. |
| jinja2 package | library | Observed | Groups 25 file(s) under jinja2 package (observed from repository paths and static analysis). Observed top-level classes: Add, And, Assign, AssignBlock, AsyncLoopContext, BaseLoader. Observed top-level functions: __getat… |
| Tests | test | Observed | Groups 32 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: DerivedExampleExtension, ExampleExtension, Magic, Magic2, MockMemcached, MyDict. Observed top-level functio… |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/lock.yaml` (ci)
- `.github/workflows/pre-commit.yaml` (ci)
- `.github/workflows/publish.yaml` (ci)
- `.github/workflows/tests.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 30 analysed file(s)
- `src` — 26 analysed file(s)
- `docs` — 21 analysed file(s)
- `examples` — 9 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 8 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5ef70112a1ff19c05324ff889dd30405b1002044` is the revision these paths and observations refer to.
