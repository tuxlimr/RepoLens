# Project structure: codelucas/newspaper

**Analysed commit:** `745dfe3abe9ef5608461d335163c93c9e6c172fa`

**Commit reference:** [745dfe3abe9ef5608461d335163c93c9e6c172fa](https://github.com/codelucas/newspaper/commit/745dfe3abe9ef5608461d335163c93c9e6c172fa)

**Tree at this commit:** [codelucas/newspaper@745dfe3abe9e](https://github.com/codelucas/newspaper/tree/745dfe3abe9ef5608461d335163c93c9e6c172fa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | codelucas/newspaper |
| Description | newspaper3k is a news, full-text, and article metadata extraction in Python 3. Advanced docs: |
| Stars | 15187 |
| Forks | 2102 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `745dfe3abe9ef5608461d335163c93c9e6c172fa` |
| Retrieved at | 2026-11-14T19:09:08.102342+00:00 |
| Files in this snapshot | 206 |

## Directory tree

```text
docs/  (21 files)
  _templates/  (2 files)
    sidebarintro.html
    sidebarlogo.html
  _themes/  (11 files)
    kr/  (4 files)
      … 4 files under this directory
    kr_small/  (3 files)
      … 3 files under this directory
    .gitignore
    LICENSE
    README.rst
    flask_theme_support.py
  user_guide/  (4 files)
    advanced.rst
    api.rst
    contributors.rst
    quickstart.rst
  Makefile
  conf.py
  index.rst
  make.bat
newspaper/  (62 files)
  resources/  (41 files)
    misc/  (3 files)
      … 3 files under this directory
    text/  (38 files)
      … 38 files under this directory
  videos/  (3 files)
    __init__.py
    extractors.py
    videos.py
  __init__.py
  api.py
  article.py
  cleaners.py
  configuration.py
  extractors.py
  images.py
  mthreading.py
  network.py
  nlp.py
  outputformatters.py
  parsers.py
  settings.py
  source.py
  text.py
  urls.py
  utils.py
  version.py
tests/  (111 files)
  data/  (109 files)
    html/  (100 files)
      … 100 files under this directory
    text/  (5 files)
      … 5 files under this directory
    fulltext_domain_list.txt
    fulltext_url_list.txt
    test_prepare_urls.txt
    test_urls.txt
  __init__.py
  benchmarks.py
.gitattributes
.gitignore
.readthedocs.yaml
.travis.yml
CHANGELOG.md
GOOSE-LICENSE.txt
LICENSE
MANIFEST.in
README.rst
download_corpora.py
requirements.txt
setup.py
```

## Entry points

- [download_corpora.py:23](https://github.com/codelucas/newspaper/blob/745dfe3abe9ef5608461d335163c93c9e6c172fa/download_corpora.py#L23)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| newspaper package | library | Observed | Groups 20 file(s) under newspaper package (observed from repository paths and static analysis). Observed top-level classes: Article, ArticleConfiguration, ArticleDownloadState, ArticleException, Category, ConcurrencyExc… |
| Tests | test | Observed | Groups 111 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: asyncio_run, benchmark, mthread_run, naive_run. |

## Important files

- `.readthedocs.yaml` (config)
- `.travis.yml` (ci)
- `MANIFEST.in` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `tests` — 111 analysed file(s)
- `newspaper` — 62 analysed file(s)
- `docs` — 21 analysed file(s)
- `(root files)` — 12 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `745dfe3abe9ef5608461d335163c93c9e6c172fa` is the revision these paths and observations refer to.
