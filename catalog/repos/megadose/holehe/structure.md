# Project structure: megadose/holehe

**Analysed commit:** `14da70f588538936b20d238783c5e28a0772a2b3`

**Commit reference:** [14da70f588538936b20d238783c5e28a0772a2b3](https://github.com/megadose/holehe/commit/14da70f588538936b20d238783c5e28a0772a2b3)

**Tree at this commit:** [megadose/holehe@14da70f58853](https://github.com/megadose/holehe/tree/14da70f588538936b20d238783c5e28a0772a2b3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | megadose/holehe |
| Description | holehe allows you to check if the mail is used on different sites like twitter, instagram and will retrieve information on sites with the forgotten password function. |
| Stars | 15657 |
| Forks | 2030 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `14da70f588538936b20d238783c5e28a0772a2b3` |
| Retrieved at | 2026-11-14T19:08:59.734442+00:00 |
| Files in this snapshot | 162 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    custom.md
    feature_request.md
  workflows/  (1 files)
    codeql-analysis.yml
  FUNDING.yml
holehe/  (151 files)
  modules/  (147 files)
    cms/  (5 files)
      … 5 files under this directory
    company/  (2 files)
      … 2 files under this directory
    crm/  (11 files)
      … 11 files under this directory
    crowfunding/  (2 files)
      … 2 files under this directory
    forum/  (26 files)
      … 26 files under this directory
    jobs/  (4 files)
      … 4 files under this directory
    learning/  (4 files)
      … 4 files under this directory
    mails/  (6 files)
      … 6 files under this directory
    medias/  (6 files)
      … 6 files under this directory
    medical/  (3 files)
      … 3 files under this directory
    music/  (7 files)
      … 7 files under this directory
    osint/  (2 files)
      … 2 files under this directory
    payment/  (2 files)
      … 2 files under this directory
    porn/  (5 files)
      … 5 files under this directory
    productivity/  (3 files)
      … 3 files under this directory
    products/  (4 files)
      … 4 files under this directory
    programing/  (7 files)
      … 7 files under this directory
    real_estate/  (2 files)
      … 2 files under this directory
    shopping/  (10 files)
      … 10 files under this directory
    social_media/  (23 files)
      … 23 files under this directory
    software/  (8 files)
      … 8 files under this directory
    sport/  (2 files)
      … 2 files under this directory
    transport/  (2 files)
      … 2 files under this directory
    __init__.py
  __init__.py
  core.py
  instruments.py
  localuseragent.py
.gitignore
Dockerfile
FUNDING.yml
LICENSE.md
README.md
setup.py
```

## Entry points

- [holehe/core.py](https://github.com/megadose/holehe/blob/14da70f588538936b20d238783c5e28a0772a2b3/holehe/core.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| holehe package | library | Observed | Groups 151 file(s) under holehe package (observed from repository paths and static analysis). Observed top-level classes: TrioProgress. Observed top-level functions: aboutme, adobe, amazon, amocrm, anydo, archive. |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `Dockerfile` (container)
- `FUNDING.yml` (config)
- `setup.py` (manifest)

## Top-level layout

- `holehe` — 151 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `14da70f588538936b20d238783c5e28a0772a2b3` is the revision these paths and observations refer to.
