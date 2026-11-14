# Project structure: ultrafunkamsterdam/undetected-chromedriver

**Analysed commit:** `757ed6a22052f0674bb7c9f765ca884d15dcb780`

**Commit reference:** [757ed6a22052f0674bb7c9f765ca884d15dcb780](https://github.com/ultrafunkamsterdam/undetected-chromedriver/commit/757ed6a22052f0674bb7c9f765ca884d15dcb780)

**Tree at this commit:** [ultrafunkamsterdam/undetected-chromedriver@757ed6a22052](https://github.com/ultrafunkamsterdam/undetected-chromedriver/tree/757ed6a22052f0674bb7c9f765ca884d15dcb780)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ultrafunkamsterdam/undetected-chromedriver |
| Description | Custom Selenium Chromedriver | Zero-Config | Passes ALL bot mitigation systems (like Distil / Imperva/ Datadadome / CloudFlare IUAM) |
| Stars | 12907 |
| Forks | 1345 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `757ed6a22052f0674bb7c9f765ca884d15dcb780` |
| Retrieved at | 2026-11-14T19:09:57.434198+00:00 |
| Files in this snapshot | 15 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    workflow.yml
example/  (2 files)
  example.py
  test_workflow.py
undetected_chromedriver/  (8 files)
  __init__.py
  cdp.py
  devtool.py
  dprocess.py
  options.py
  patcher.py
  reactor.py
  webelement.py
.gitignore
LICENSE
README.md
setup.py
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: main. |
| undetected_chromedriver package | library | Observed | Groups 8 file(s) under undetected_chromedriver package (observed from repository paths and static analysis). Observed top-level classes: CDP, CDPObject, Chrome, ChromeOptions, PageElement, Patcher. Observed top-level fu… |

## Important files

- `.github/workflows/workflow.yml` (ci)
- `setup.py` (manifest)

## Top-level layout

- `undetected_chromedriver` — 8 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `example` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `757ed6a22052f0674bb7c9f765ca884d15dcb780` is the revision these paths and observations refer to.
