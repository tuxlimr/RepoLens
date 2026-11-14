# Project structure: mikf/gallery-dl

**Analysed commit:** `26dfd4eea885577fef45e9b614538e5a7d24583a`

**Commit reference:** [26dfd4eea885577fef45e9b614538e5a7d24583a](https://github.com/mikf/gallery-dl/commit/26dfd4eea885577fef45e9b614538e5a7d24583a)

**Tree at this commit:** [mikf/gallery-dl@26dfd4eea885](https://github.com/mikf/gallery-dl/tree/26dfd4eea885577fef45e9b614538e5a7d24583a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mikf/gallery-dl |
| Description | Command-line program to download image galleries and collections from several image hosting sites |
| Stars | 20503 |
| Forks | 1530 |
| Licence | GPL-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `26dfd4eea885577fef45e9b614538e5a7d24583a` |
| Retrieved at | 2026-11-14T19:08:02.076200+00:00 |
| Files in this snapshot | 761 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (4 files)
    docker.yml
    executables.yml
    pages.yml
    tests.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
bin/  (1 files)
  gallery-dl
docs/  (9 files)
  _layouts/  (1 files)
    default.html
  formatting.md
  gallery-dl-example.conf
  gallery-dl.conf
  index.md
  links.js
  oauth-redirect.html
  options.md
  supportedsites.md
gallery_dl/  (312 files)
  downloader/  (5 files)
    __init__.py
    common.py
    http.py
    text.py
    ytdl.py
  extractor/  (272 files)
    utils/  (15 files)
      … 15 files under this directory
    2ch.py
    2chan.py
    2chen.py
    35photo.py
    3dbooru.py
    4archive.py
    4chan.py
    4chanarchives.py
    500px.py
    8chan.py
    8muses.py
    __init__.py
    adultempire.py
    agnph.py
    ahottie.py
    allporncomic.py
    ao3.py
    arcalive.py
    architizer.py
    arena.py
    artstation.py
    aryion.py
    audiochan.py
    bbc.py
    … 233 more files
  postprocessor/  (14 files)
    __init__.py
    actions.py
    classify.py
    common.py
    compare.py
    directory.py
    exec.py
    hash.py
    metadata.py
    mtime.py
    python.py
    rename.py
    ugoira.py
    zip.py
  __init__.py
  __main__.py
  actions.py
  aes.py
  archive.py
  cache.py
  config.py
  cookies.py
  dt.py
  exception.py
  formatter.py
  job.py
  oauth.py
  option.py
  output.py
  path.py
  text.py
  update.py
  util.py
  version.py
  ytdl.py
requirements/  (10 files)
  brotli
  docker
  jinja2
  pip
  pycryptodomex
  pyyaml
  requests
  truststore
  versions
  yt-dlp
scripts/  (20 files)
  build_testresult_db.py
  completion_bash.py
  completion_fish.py
  completion_zsh.py
  docs_compare.py
  generate_test_result.py
  hook-gallery_dl.py
  init.py
  man.py
  options.py
  pre-commit
  pull-request
  pyinstaller.py
  pyprint.py
  release.sh
  requirements.py
  rm.py
  run_tests.py
  supportedsites.py
  util.py
snap/  (3 files)
  local/  (2 files)
    launchers/  (1 files)
      … 1 files under this directory
    scriptlets/  (1 files)
      … 1 files under this directory
  snapcraft.yaml
test/  (388 files)
  results/  (371 files)
    2ch.py
    2chan.py
    35photo.py
    3dbooru.py
    4archive.py
    4chan.py
    4chanarchives.py
    4plebs.py
    500px.py
    8chan.py
    8kun.py
    8muses.py
    94chan.py
    __init__.py
    acidimg.py
    adultempire.py
    agnph.py
    ahottie.py
    aibooru.py
    allgirlbooru.py
    allporncomic.py
    animereactor.py
    ao3.py
    arcalive.py
    … 347 more files
  __init__.py
  test_cache.py
  test_config.py
  test_cookies.py
  test_downloader.py
  test_dt.py
  test_extractor.py
  test_formatter.py
  test_job.py
  test_oauth.py
  test_output.py
  test_path.py
  test_postprocessor.py
  test_results.py
  test_text.py
  test_util.py
  test_ytdl.py
.editorconfig
.gitignore
CONTRIBUTING.md
Dockerfile
LICENSE
MANIFEST.in
Makefile
README.rst
pyproject.toml
requirements.txt
setup.cfg
setup.py
```

## Entry points

- [gallery_dl/__init__.py](https://github.com/mikf/gallery-dl/blob/26dfd4eea885577fef45e9b614538e5a7d24583a/gallery_dl/__init__.py)
- [gallery_dl/__main__.py:19](https://github.com/mikf/gallery-dl/blob/26dfd4eea885577fef45e9b614538e5a7d24583a/gallery_dl/__main__.py#L19)
- [scripts/generate_test_result.py:266](https://github.com/mikf/gallery-dl/blob/26dfd4eea885577fef45e9b614538e5a7d24583a/scripts/generate_test_result.py#L266)
- [scripts/init.py:398](https://github.com/mikf/gallery-dl/blob/26dfd4eea885577fef45e9b614538e5a7d24583a/scripts/init.py#L398)
- [scripts/man.py:309](https://github.com/mikf/gallery-dl/blob/26dfd4eea885577fef45e9b614538e5a7d24583a/scripts/man.py#L309)
- [scripts/pyinstaller.py:58](https://github.com/mikf/gallery-dl/blob/26dfd4eea885577fef45e9b614538e5a7d24583a/scripts/pyinstaller.py#L58)
- [scripts/requirements.py:255](https://github.com/mikf/gallery-dl/blob/26dfd4eea885577fef45e9b614538e5a7d24583a/scripts/requirements.py#L255)
- [scripts/rm.py:136](https://github.com/mikf/gallery-dl/blob/26dfd4eea885577fef45e9b614538e5a7d24583a/scripts/rm.py#L136)
- [scripts/run_tests.py:43](https://github.com/mikf/gallery-dl/blob/26dfd4eea885577fef45e9b614538e5a7d24583a/scripts/run_tests.py#L43)
- [scripts/supportedsites.py:816](https://github.com/mikf/gallery-dl/blob/26dfd4eea885577fef45e9b614538e5a7d24583a/scripts/supportedsites.py#L816)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: apply. Observed top-level functions: accumulate, build_py2exe, build_setuptools, chec… |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: LoggingCapture. Observed top-level functions: build_base_pattern, build_extractor_list, bu… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| gallery_dl package | library | Observed | Groups 310 file(s) under gallery_dl package (observed from repository paths and static analysis). Observed top-level classes: AbortExtraction, AcidimgImageExtractor, ActionsPP, AdultempireGalleryExtractor, AgnphExtracto… |
| scripts package | library | Observed | Groups 10 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: Formatter, lazy, lines. Observed top-level functions: git, open, opts_category, opts_general, pat… |
| Tests | test | Observed | Groups 389 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH builtins.__import__, PATCH builtins.__import__, PATCH builtins.__import__, PATCH os.sep, PATCH gallery_dl.path.… |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/executables.yml` (ci)
- `.github/workflows/pages.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `snap/snapcraft.yaml` (config)

## Top-level layout

- `test` — 388 analysed file(s)
- `gallery_dl` — 312 analysed file(s)
- `scripts` — 20 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `requirements` — 10 analysed file(s)
- `docs` — 9 analysed file(s)
- `.github` — 6 analysed file(s)
- `snap` — 3 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `26dfd4eea885577fef45e9b614538e5a7d24583a` is the revision these paths and observations refer to.
