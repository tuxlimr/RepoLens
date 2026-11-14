# Project structure: borgbackup/borg

**Analysed commit:** `119addc7c0235b1859c9efd74f771c02b1208bcb`

**Commit reference:** [119addc7c0235b1859c9efd74f771c02b1208bcb](https://github.com/borgbackup/borg/commit/119addc7c0235b1859c9efd74f771c02b1208bcb)

**Tree at this commit:** [borgbackup/borg@119addc7c023](https://github.com/borgbackup/borg/tree/119addc7c0235b1859c9efd74f771c02b1208bcb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | borgbackup/borg |
| Description | Deduplicating archiver with compression and authenticated encryption. |
| Stars | 13926 |
| Forks | 883 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `119addc7c0235b1859c9efd74f771c02b1208bcb` |
| Retrieved at | 2026-11-14T19:09:36.554802+00:00 |
| Files in this snapshot | 561 |

## Directory tree

```text
.claude/  (2 files)
  CLAUDE.md
  settings.json
.github/  (16 files)
  workflows/  (11 files)
    32bit.yml
    backport.yml
    bigendian.yml
    black.yaml
    canary.yml
    ci.yml
    codeql-analysis.yml
    docs.yml
    fame.yml
    pypy.yml
    release.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  zizmor.yml
docs/  (214 files)
  3rd_party/  (1 files)
    README
  _static/  (3 files)
    Makefile
    logo.svg
    logo_font.txt
  _templates/  (5 files)
    downloads.html
    globaltoc.html
    layout.html
    logo-text.html
    versionselector.html
  binaries/  (1 files)
    00_README.txt
  borg_theme/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  deployment/  (8 files)
    age.rst
    automated-local.rst
    central-backup-server.rst
    hosting-repositories.rst
    image-backup.rst
    non-root-user.rst
    pull-backup.rst
    yubikey.rst
  internals/  (5 files)
    chunker.rst
    data-structures.rst
    frontends.rst
    packs.rst
    security.rst
  man/  (57 files)
    borg-analyze.1
    borg-benchmark-cpu.1
    borg-benchmark-crud.1
    borg-benchmark.1
    borg-break-lock.1
    borg-check.1
    borg-common.1
    borg-compact.1
    borg-completion.1
    borg-compression.1
    borg-config.1
    borg-copy.1
    borg-create.1
    borg-delete.1
    borg-diff.1
    borg-environment.1
    borg-export-tar.1
    borg-extract.1
    borg-find.1
    borg-import-tar.1
    borg-info.1
    borg-key-add.1
    borg-key-change-algorithm.1
    borg-key-change-location.1
    … 33 more files
  misc/  (17 files)
    asciinema/  (8 files)
      … 8 files under this directory
    joke-issue-10000/  (2 files)
      … 2 files under this directory
    stickers/  (1 files)
      … 1 files under this directory
    benchmark-crud.txt
    create_chunker-params.txt
    internals-picture.txt
    logging.conf
    prune-example-interval.txt
    prune-example.txt
  usage/  (96 files)
    general/  (13 files)
      … 13 files under this directory
    analyze.rst
    analyze.rst.inc
    benchmark.rst
    benchmark_cpu.rst.inc
    benchmark_crud.rst.inc
    break-lock.rst.inc
    check.rst
    check.rst.inc
    common-options.rst.inc
    compact.rst
    compact.rst.inc
    completion.rst
    completion.rst.inc
    copy.rst
    copy.rst.inc
    create.rst
    create.rst.inc
    debug.rst
    delete.rst
    delete.rst.inc
    diff.rst
    diff.rst.inc
    export-tar.rst.inc
    extract.rst
    … 59 more files
  Makefile
  authors.rst
  book.rst
  changes.rst
  changes_0.x.rst
  conf.py
  deployment.rst
  development.rst
  faq.rst
  global.rst.inc
  index.rst
  installation.rst
  internals.rst
  introduction.rst
  man_intro.rst
  quickstart.rst
  quickstart_example.rst.inc
  support.rst
  usage.rst
  usage_general.rst.inc
requirements.d/  (6 files)
  codestyle.txt
  development.lock.txt
  development.txt
  docs.txt
  pyinstaller.txt
  s3-test-server.txt
scripts/  (22 files)
  make-testdata/  (1 files)
    test_transfer_upgrade.sh
  Dockerfile.linux-run
  bench_chunker_kernels.py
  blake3-optimize-mt-threshold.py
  borg.exe.spec
  build-borg-using-nuitka.sh
  build-borg-using-pyinstaller.sh
  chunker_bench.py
  endian_interop_test.py
  errorlist.py
  fame.py
  fetch-binaries
  glibc_check.py
  haiku_mmap_pread_shim.c
  linux-run
  lvm-thin-map.py
  make.py
  msys2-install-deps
  rest_perf_test.sh
  sdist-sign
  sign-binaries
  upload-pypi
src/  (282 files)
  borg/  (282 files)
    archiver/  (37 files)
      … 37 files under this directory
    chunkers/  (35 files)
      … 35 files under this directory
    cockpit/  (7 files)
      … 7 files under this directory
    crypto/  (7 files)
      … 7 files under this directory
    helpers/  (17 files)
      … 17 files under this directory
    legacy/  (13 files)
      … 13 files under this directory
    platform/  (13 files)
      … 13 files under this directory
    testsuite/  (121 files)
      … 121 files under this directory
    __init__.py
    __main__.py
    archive.py
    cache.py
    compress.pyi
    compress.pyx
    conftest.py
    constants.py
    digests.py
    fslocking.py
    fuse.py
    fuse_impl.py
    hashindex.pyi
    hashindex.pyx
    hlfuse.py
    item.pyi
    item.pyx
    logger.py
    manifest.py
    paperkey.html
    patterns.py
    platformflags.py
    repoobj.py
    repository.py
    … 8 more files
.editorconfig
.git-blame-ignore-revs
.gitattributes
.gitignore
.mailmap
.pre-commit-config.yaml
.readthedocs.yaml
AUTHORS
Brewfile
CONTRIBUTING.md
FAME.md
FAME.svg
LICENSE
MANIFEST.in
README.rst
SECURITY.md
Vagrantfile
pyproject.toml
setup.py
```

## Entry points

- [src/borg/archiver/__init__.py](https://github.com/borgbackup/borg/blob/119addc7c0235b1859c9efd74f771c02b1208bcb/src/borg/archiver/__init__.py)
- [src/borg/archiver/__init__.py](https://github.com/borgbackup/borg/blob/119addc7c0235b1859c9efd74f771c02b1208bcb/src/borg/archiver/__init__.py)
- [scripts/bench_chunker_kernels.py:322](https://github.com/borgbackup/borg/blob/119addc7c0235b1859c9efd74f771c02b1208bcb/scripts/bench_chunker_kernels.py#L322)
- [scripts/blake3-optimize-mt-threshold.py:530](https://github.com/borgbackup/borg/blob/119addc7c0235b1859c9efd74f771c02b1208bcb/scripts/blake3-optimize-mt-threshold.py#L530)
- [scripts/chunker_bench.py:323](https://github.com/borgbackup/borg/blob/119addc7c0235b1859c9efd74f771c02b1208bcb/scripts/chunker_bench.py#L323)
- [scripts/endian_interop_test.py:260](https://github.com/borgbackup/borg/blob/119addc7c0235b1859c9efd74f771c02b1208bcb/scripts/endian_interop_test.py#L260)
- [scripts/fame.py:221](https://github.com/borgbackup/borg/blob/119addc7c0235b1859c9efd74f771c02b1208bcb/scripts/fame.py#L221)
- [scripts/glibc_check.py:63](https://github.com/borgbackup/borg/blob/119addc7c0235b1859c9efd74f771c02b1208bcb/scripts/glibc_check.py#L63)
- [scripts/lvm-thin-map.py:165](https://github.com/borgbackup/borg/blob/119addc7c0235b1859c9efd74f771c02b1208bcb/scripts/lvm-thin-map.py#L165)
- [scripts/make.py:657](https://github.com/borgbackup/borg/blob/119addc7c0235b1859c9efd74f771c02b1208bcb/scripts/make.py#L657)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| borg package | library | Observed | Groups 127 file(s) under borg package (observed from repository paths and static analysis). Observed top-level classes: AEADKeyBase, AESCTRKey, AESKeyBase, AESOCBKey, AdHocWithFilesCache, AnalyzeMixIn. Observed top-leve… |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: long_desc_from_readme. |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Archiver, BorgCockpitApp, BuildMan, BuildUsage, Clean. Observed top-level functions: adve… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: subclasses. |
| Tests | test | Observed | Groups 117 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH getpass.getpass. Observed top-level classes: ArchiverSetup, ChunkerBuzHash64TestCase, ChunkerFixedTestCase, Chu… |

## Important files

- `.claude/settings.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/32bit.yml` (ci)
- `.github/workflows/backport.yml` (ci)
- `.github/workflows/bigendian.yml` (ci)
- `.github/workflows/black.yaml` (ci)
- `.github/workflows/canary.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/fame.yml` (ci)
- `.github/workflows/pypy.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/zizmor.yml` (config)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `scripts/Dockerfile.linux-run` (container)
- `setup.py` (manifest)

## Top-level layout

- `src` — 282 analysed file(s)
- `docs` — 214 analysed file(s)
- `scripts` — 22 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 16 analysed file(s)
- `requirements.d` — 6 analysed file(s)
- `.claude` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `119addc7c0235b1859c9efd74f771c02b1208bcb` is the revision these paths and observations refer to.
