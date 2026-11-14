# Project structure: ungoogled-software/ungoogled-chromium

**Analysed commit:** `8c886dffc6ade39d8f7df5d64ace5a8824b455e1`

**Commit reference:** [8c886dffc6ade39d8f7df5d64ace5a8824b455e1](https://github.com/ungoogled-software/ungoogled-chromium/commit/8c886dffc6ade39d8f7df5d64ace5a8824b455e1)

**Tree at this commit:** [ungoogled-software/ungoogled-chromium@8c886dffc6ad](https://github.com/ungoogled-software/ungoogled-chromium/tree/8c886dffc6ade39d8f7df5d64ace5a8824b455e1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ungoogled-software/ungoogled-chromium |
| Description | Google Chromium, sans integration with Google |
| Stars | 28248 |
| Forks | 1291 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `8c886dffc6ade39d8f7df5d64ace5a8824b455e1` |
| Retrieved at | 2026-11-14T19:07:16.773047+00:00 |
| Files in this snapshot | 193 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bugreport.yml
    create-an--updating-to-chromium-x-x-x-x-.md
    feature_request.yml
  actions/  (1 files)
    ci-setup/  (1 files)
      … 1 files under this directory
  workflows/  (4 files)
    ci.yml
    new_version_check.yml
    release-on-tag.yml
    stale.yml
  PULL_REQUEST_TEMPLATE.md
devutils/  (34 files)
  tests/  (3 files)
    __init__.py
    test_check_patch_files.py
    test_validate_patches.py
  third_party/  (7 files)
    unidiff/  (5 files)
      … 5 files under this directory
    README.md
    __init__.py
  .coveragerc
  README.md
  __init__.py
  check_all_code.sh
  check_downloads_ini.py
  check_files_exist.py
  check_gn_flags.py
  check_patch_files.py
  print_tag_version.sh
  pytest.ini
  run_devutils_pylint.py
  run_devutils_tests.sh
  run_devutils_yapf.sh
  run_other_pylint.py
  run_other_yapf.sh
  run_utils_pylint.py
  run_utils_tests.sh
  run_utils_yapf.sh
  set_quilt_vars.fish
  set_quilt_vars.sh
  update_lists.py
  update_platform_patches.py
  validate_config.py
  validate_patches.py
docs/  (8 files)
  building.md
  contributing.md
  default_settings.md
  design.md
  developing.md
  flags.md
  platforms.md
  repo_management.md
patches/  (108 files)
  core/  (34 files)
    bromite/  (1 files)
      … 1 files under this directory
    inox-patchset/  (5 files)
      … 5 files under this directory
    iridium-browser/  (2 files)
      … 2 files under this directory
    ungoogled-chromium/  (26 files)
      … 26 files under this directory
  extra/  (72 files)
    bromite/  (3 files)
      … 3 files under this directory
    debian/  (1 files)
      … 1 files under this directory
    inox-patchset/  (5 files)
      … 5 files under this directory
    iridium-browser/  (5 files)
      … 5 files under this directory
    ungoogled-chromium/  (58 files)
      … 58 files under this directory
  upstream-fixes/  (1 files)
    missing-dependencies.patch
  series
utils/  (20 files)
  tests/  (3 files)
    __init__.py
    test_domain_substitution.py
    test_patches.py
  third_party/  (3 files)
    README.md
    __init__.py
    schema.py
  .coveragerc
  __init__.py
  _common.py
  _extraction.py
  clone.py
  depot_tools.patch
  domain_substitution.py
  downloads.py
  filescfg.py
  gsutil.patch
  make_domsub_script.py
  patches.py
  prune_binaries.py
  pytest.ini
.gitignore
.python-version
.requirements.txt
.style.yapf
CODEOWNERS
LICENSE
README.md
SUPPORT.md
chromium_version.txt
domain_regex.list
downloads.ini
flags.gn
revision.txt
shell.nix
```

## Entry points

- [devutils/check_downloads_ini.py:63](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/check_downloads_ini.py#L63)
- [devutils/check_files_exist.py:35](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/check_files_exist.py#L35)
- [devutils/check_gn_flags.py:79](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/check_gn_flags.py#L79)
- [devutils/check_patch_files.py:139](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/check_patch_files.py#L139)
- [devutils/run_devutils_pylint.py:60](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/run_devutils_pylint.py#L60)
- [devutils/run_other_pylint.py:103](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/run_other_pylint.py#L103)
- [devutils/run_utils_pylint.py:55](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/run_utils_pylint.py#L55)
- [devutils/update_lists.py:408](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/update_lists.py#L408)
- [devutils/update_platform_patches.py:187](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/update_platform_patches.py#L187)
- [devutils/validate_config.py:57](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/validate_config.py#L57)
- [devutils/validate_patches.py:707](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/devutils/validate_patches.py#L707)
- [utils/clone.py:287](https://github.com/ungoogled-software/ungoogled-chromium/blob/8c886dffc6ade39d8f7df5d64ace5a8824b455e1/utils/clone.py#L287)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| devutils package | library | Observed | Groups 15 file(s) under devutils package (observed from repository paths and static analysis). Observed top-level classes: Hunk, Line, PatchInfo, PatchSet, PatchedFile, UnidiffParseError. |
| Application entry point | entrypoint | Observed | Groups 18 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ChangeDir, DomainRegexList, DownloadInfo, HashMismatchError, HashesURLEnum, UnusedPattern… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: test_check_series_duplicates, test_find_and_check_patch, test_patch_from_env, test_patch_from_which, test_… |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). Observed top-level classes: And, Const, ExtractorEnum, Forbidden, Optional, Or. Observed top-level functions: _callable_str, _ex… |

## Important files

- `.github/ISSUE_TEMPLATE/bugreport.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/actions/ci-setup/action.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/new_version_check.yml` (ci)
- `.github/workflows/release-on-tag.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `devutils/pytest.ini` (config)
- `downloads.ini` (config)
- `utils/pytest.ini` (config)

## Top-level layout

- `patches` — 108 analysed file(s)
- `devutils` — 34 analysed file(s)
- `utils` — 20 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 9 analysed file(s)
- `docs` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8c886dffc6ade39d8f7df5d64ace5a8824b455e1` is the revision these paths and observations refer to.
