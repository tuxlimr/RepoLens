# Project structure: google/python-fire

**Analysed commit:** `716bbc23d7eca949fdb682172283c8d18f742cb6`

**Commit reference:** [716bbc23d7eca949fdb682172283c8d18f742cb6](https://github.com/google/python-fire/commit/716bbc23d7eca949fdb682172283c8d18f742cb6)

**Tree at this commit:** [google/python-fire@716bbc23d7ec](https://github.com/google/python-fire/tree/716bbc23d7eca949fdb682172283c8d18f742cb6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google/python-fire |
| Description | Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object. |
| Stars | 28225 |
| Forks | 1501 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `716bbc23d7eca949fdb682172283c8d18f742cb6` |
| Retrieved at | 2026-11-14T19:07:17.446977+00:00 |
| Files in this snapshot | 79 |

## Directory tree

```text
.github/  (3 files)
  scripts/  (1 files)
    build.sh
  workflows/  (1 files)
    build.yml
  dependabot.yml
docs/  (7 files)
  api.md
  benefits.md
  guide.md
  index.md
  installation.md
  troubleshooting.md
  using-cli.md
examples/  (15 files)
  cipher/  (3 files)
    __init__.py
    cipher.py
    cipher_test.py
  diff/  (4 files)
    __init__.py
    diff.py
    diff_test.py
    difffull.py
  identity/  (2 files)
    __init__.py
    identity.py
  widget/  (5 files)
    __init__.py
    collector.py
    collector_test.py
    widget.py
    widget_test.py
  __init__.py
fire/  (47 files)
  console/  (10 files)
    README.md
    __init__.py
    console_attr.py
    console_attr_os.py
    console_io.py
    console_pager.py
    encoding.py
    files.py
    platforms.py
    text.py
  __init__.py
  __main__.py
  completion.py
  completion_test.py
  core.py
  core_test.py
  custom_descriptions.py
  custom_descriptions_test.py
  decorators.py
  decorators_test.py
  docstrings.py
  docstrings_fuzz_test.py
  docstrings_test.py
  fire_import_test.py
  fire_test.py
  formatting.py
  formatting_test.py
  formatting_windows.py
  helptext.py
  helptext_test.py
  inspectutils.py
  inspectutils_test.py
  interact.py
  interact_test.py
  … 13 more files
.gitignore
CONTRIBUTING.md
LICENSE
README.md
mkdocs.yml
pylintrc
pyproject.toml
```

## Entry points

- [fire/__main__.py:125](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/__main__.py#L125)
- [fire/completion_test.py:187](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/completion_test.py#L187)
- [fire/core_test.py:227](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/core_test.py#L227)
- [fire/custom_descriptions_test.py:68](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/custom_descriptions_test.py#L68)
- [fire/decorators_test.py:169](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/decorators_test.py#L169)
- [fire/docstrings_fuzz_test.py:35](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/docstrings_fuzz_test.py#L35)
- [fire/docstrings_test.py:360](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/docstrings_test.py#L360)
- [fire/fire_import_test.py:39](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/fire_import_test.py#L39)
- [fire/fire_test.py:720](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/fire_test.py#L720)
- [fire/formatting_test.py:77](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/formatting_test.py#L77)
- [fire/helptext_test.py:595](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/helptext_test.py#L595)
- [fire/inspectutils_test.py:129](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/fire/inspectutils_test.py#L129)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: import_from_file_path, import_from_module_name, import_module, main. |
| fire package | library | Observed | Groups 24 file(s) under fire package (observed from repository paths and static analysis). Observed top-level classes: ActionGroup, Architecture, ArgInfo, BaseTestCase, BoxLineCharacters, BoxLineCharactersAscii. Observe… |
| Tests | test | Observed | Groups 25 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH fire.interact.Embed, PATCH fire.interact.Embed, PATCH fire.interact.Embed, PATCH fire.interact.Embed, PATCH (pat… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/build.yml` (ci)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `fire` — 47 analysed file(s)
- `examples` — 15 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `docs` — 7 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `716bbc23d7eca949fdb682172283c8d18f742cb6` is the revision these paths and observations refer to.
