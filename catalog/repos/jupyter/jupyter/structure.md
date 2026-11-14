# Project structure: jupyter/jupyter

**Analysed commit:** `6b5eb0f469c7bc3ea43d6d2a0ba1057853c9a3a5`

**Commit reference:** [6b5eb0f469c7bc3ea43d6d2a0ba1057853c9a3a5](https://github.com/jupyter/jupyter/commit/6b5eb0f469c7bc3ea43d6d2a0ba1057853c9a3a5)

**Tree at this commit:** [jupyter/jupyter@6b5eb0f469c7](https://github.com/jupyter/jupyter/tree/6b5eb0f469c7bc3ea43d6d2a0ba1057853c9a3a5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jupyter/jupyter |
| Description | Jupyter metapackage for installation and documentation |
| Stars | 15348 |
| Forks | 4565 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `6b5eb0f469c7bc3ea43d6d2a0ba1057853c9a3a5` |
| Retrieved at | 2026-11-14T19:09:04.047097+00:00 |
| Files in this snapshot | 200 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    config.yml
    doc_suggestion.md
  workflows/  (1 files)
    release.yaml
docs/  (181 files)
  .tx/  (1 files)
    config
  source/  (176 files)
    _static/  (4 files)
      … 4 files under this directory
    community/  (43 files)
      … 43 files under this directory
    contributing/  (35 files)
      … 35 files under this directory
    install/  (2 files)
      … 2 files under this directory
    locale/  (49 files)
      … 49 files under this directory
    projects/  (17 files)
      … 17 files under this directory
    reference/  (3 files)
      … 3 files under this directory
    start/  (1 files)
      … 1 files under this directory
    use/  (15 files)
      … 15 files under this directory
    conf.py
    glossary.rst
    index.md
    install.rst
    releases.rst
    running.rst
    what_is_jupyter.md
  Makefile
  doc-requirements.txt
  environment.yml
  make.bat
.gitattributes
.gitignore
.readthedocs.yaml
.travis.yml
LICENSE
MANIFEST.in
README.es-ES.md
README.fr-FR.md
README.md
README.pt-BR.md
SECURITY.md
long_description.md
noxfile.py
setup.cfg
setup.py
tbump.toml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: docs, docs_live. |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/release.yaml` (ci)
- `.readthedocs.yaml` (config)
- `.travis.yml` (ci)
- `MANIFEST.in` (manifest)
- `docs/environment.yml` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `tbump.toml` (config)

## Top-level layout

- `docs` — 181 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `6b5eb0f469c7bc3ea43d6d2a0ba1057853c9a3a5` is the revision these paths and observations refer to.
