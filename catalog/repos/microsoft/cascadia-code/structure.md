# Project structure: microsoft/cascadia-code

**Analysed commit:** `56bcca3f2c1e4cb19458954f0e2bb4635960df91`

**Commit reference:** [56bcca3f2c1e4cb19458954f0e2bb4635960df91](https://github.com/microsoft/cascadia-code/commit/56bcca3f2c1e4cb19458954f0e2bb4635960df91)

**Tree at this commit:** [microsoft/cascadia-code@56bcca3f2c1e](https://github.com/microsoft/cascadia-code/tree/56bcca3f2c1e4cb19458954f0e2bb4635960df91)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/cascadia-code |
| Description | This is a fun, new monospaced font that includes programming ligatures and is designed to enhance the modern look and feel of the Windows Terminal. |
| Stars | 27962 |
| Forks | 846 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `56bcca3f2c1e4cb19458954f0e2bb4635960df91` |
| Retrieved at | 2026-11-14T19:07:20.403849+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (3 files)
    Bug_Report.yml
    Documentation_Issue.md
    Feature_Request.md
  PULL_REQUEST_TEMPLATE.md
doc/  (1 files)
  CONTRIBUTING.md
pipelines/  (2 files)
  templates/  (1 files)
    steps-esrp-signing.yml
  release.yml
sources/  (782 files)
  CascadiaCode-Bold.ufo/  (782 files)
    glyphs/  (774 files)
      … 774 files under this directory
    glyphs.public.background/  (6 files)
      … 6 files under this directory
    features.fea
    fontinfo.plist
.azure-pipelines.yml
.gitignore
CODE_OF_CONDUCT.md
FONTLOG.txt
LICENSE
OFL-FAQ.txt
README.md
SECURITY.md
build.py
requirements.in
requirements.txt
```

## Entry points

- [build.py:352](https://github.com/microsoft/cascadia-code/blob/56bcca3f2c1e4cb19458954f0e2bb4635960df91/build.py#L352)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: autohint, build_font_static, build_font_variable, compile_static_and_save, compile_varia… |

## Important files

- `.azure-pipelines.yml` (config)
- `.github/ISSUE_TEMPLATE/Bug_Report.yml` (config)
- `pipelines/release.yml` (config)
- `pipelines/templates/steps-esrp-signing.yml` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `sources` — 782 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 4 analysed file(s)
- `pipelines` — 2 analysed file(s)
- `doc` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `56bcca3f2c1e4cb19458954f0e2bb4635960df91` is the revision these paths and observations refer to.
