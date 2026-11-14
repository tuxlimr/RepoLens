# Project structure: icloud-photos-downloader/icloud_photos_downloader

**Analysed commit:** `3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3`

**Commit reference:** [3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3](https://github.com/icloud-photos-downloader/icloud_photos_downloader/commit/3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3)

**Tree at this commit:** [icloud-photos-downloader/icloud_photos_downloader@3caeae584c3d](https://github.com/icloud-photos-downloader/icloud_photos_downloader/tree/3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | icloud-photos-downloader/icloud_photos_downloader |
| Description | A command-line tool to download photos from iCloud |
| Stars | 12424 |
| Forks | 872 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3` |
| Retrieved at | 2026-11-14T19:10:09.678785+00:00 |
| Files in this snapshot | 221 |

## Directory tree

```text
.devcontainer/  (2 files)
  node/  (1 files)
    devcontainer.json
  python/  (1 files)
    devcontainer.json
.github/  (17 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    feature-request.md
    generic.md
  workflows/  (13 files)
    README.md
    build-docs.yml
    build-package.yml
    codeql-analysis.yml
    compile-notes.yml
    create-release.yml
    extract-changelog.yml
    patch-version.yml
    produce-artifacts.yml
    publish-docs.yml
    publish.yml
    quality-checks.yml
    refresh-docs.yml
  dependabot.yml
.vscode/  (1 files)
  settings.json
binary_dist/  (5 files)
  src/  (4 files)
    icloud/  (2 files)
      … 2 files under this directory
    icloudpd/  (2 files)
      … 2 files under this directory
  pyproject.toml
docs/  (11 files)
  authentication.md
  conf.py
  index.md
  install.md
  mode.md
  naming.md
  nas.md
  raw.md
  reference.md
  size.md
  webui.md
examples/  (1 files)
  cron_script.sh.example
jq/  (1 files)
  version.jq
npm/  (15 files)
  @icloudpd/  (12 files)
    darwin-arm64/  (2 files)
      … 2 files under this directory
    darwin-x64/  (2 files)
      … 2 files under this directory
    linux-arm/  (2 files)
      … 2 files under this directory
    linux-arm64/  (2 files)
      … 2 files under this directory
    linux-x64/  (2 files)
      … 2 files under this directory
    win32-x64/  (2 files)
      … 2 files under this directory
  icloudpd/  (3 files)
    bin/  (1 files)
      … 1 files under this directory
    package.json
    preinstall.js
scripts/  (27 files)
  build_bin1
  build_binary_dist_macos
  build_binary_dist_windows
  build_npm
  build_static
  build_whl
  clean
  clone_whl_version
  compat_test
  compile_compatibility.py
  compile_matrix.py
  compile_tzlc.py
  extract_releasenotes
  format
  get_version
  install_deps
  lint
  npx_optional
  npx_optional_touch
  patch_version
  publish_npm
  publish_pypi
  run_all_checks
  test
  … 3 more files
src/  (63 files)
  foundation/  (9 files)
    core/  (2 files)
      … 2 files under this directory
    __init__.py
    http.py
    json.py
    predicates.py
    py.typed
    string.py
    string_utils.py
  icloudpd/  (35 files)
    server/  (12 files)
      … 12 files under this directory
    __init__.py
    authentication.py
    autodelete.py
    base.py
    cli.py
    config.py
    constants.py
    counter.py
    download.py
    email_notifications.py
    exif_datetime.py
    filename_policies.py
    log_level.py
    logger.py
    mfa_provider.py
    password_provider.py
    paths.py
    progress.py
    prune.py
    py.typed
    status.py
    string_helpers.py
    xmp_sidecar.py
  pyicloud_ipd/  (16 files)
    services/  (2 files)
      … 2 files under this directory
    __init__.py
    asset_version.py
    base.py
    cmdline.py
    exceptions.py
    file_match.py
    item_type.py
    live_photo_mov_filename_policy.py
    py.typed
    raw_policy.py
    session.py
    sms.py
    utils.py
    version_size.py
  starters/  (3 files)
    __init__.py
    icloud.py
    icloudpd.py
tests/  (58 files)
  cookie/  (2 files)
    jdoegmailcom
    jdoegmailcom.session
  data/  (1 files)
    parse_trusted_phone_numbers_payload_valid.html
  helpers/  (1 files)
    __init__.py
  vcr_cassettes/  (13 files)
    2fa_flow_invalid_code.yml
    2fa_flow_valid_code.yml
    2fa_flow_valid_code_zero_lead.yml
    2sa_flow_invalid_code.yml
    2sa_flow_valid_code.yml
    auth_invalid_session_421.yml
    auth_non_2fa.yml
    auth_requires_2fa.yml
    failed_auth.yml
    failed_auth_503.yml
    fallback_raw_password.yml
    listing_albums.yml
    successful_auth.yml
  __init__.py
  conftest.py
  test_adp_web_access.py
  test_album_pagination.py
  test_albums_in_folders.py
  test_authentication.py
  test_autodelete_photos.py
  test_cli.py
  test_download_live_photos.py
  test_download_live_photos_id.py
  test_download_photos.py
  test_download_photos_id.py
  test_download_videos.py
  test_email_notifications.py
  test_exif_datetime.py
  test_filenames.py
  test_folder_structure.py
  test_http.py
  test_icloud_cmdline.py
  test_incomplete_listing.py
  test_issue_1220_only_print_filenames_dedup_bug.py
  test_issue_1355_xmp_only_print_filenames.py
  test_issue_1387_indexing_state_retry.py
  test_item_type.py
  … 17 more files
.dockerignore
.gitattributes
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
Dockerfile.build
Dockerfile.build-doc
Dockerfile.build-musl
EXPERIMENTAL.md
LICENSE.md
README.md
README_AUR.md
README_DOCKER.md
README_NPM.md
README_PYPI.md
help_current.txt
pyproject.toml
requirements-pip.txt
```

## Entry points

- [src/icloudpd/cli.py](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3/src/icloudpd/cli.py)
- [src/icloudpd/server/__init__.py:12](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3/src/icloudpd/server/__init__.py#L12)
- [src/pyicloud_ipd/cmdline.py](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3/src/pyicloud_ipd/cmdline.py)
- [src/starters/icloud.py:4](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3/src/starters/icloud.py#L4)
- [src/starters/icloudpd.py:6](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3/src/starters/icloudpd.py#L6)
- [scripts/compile_compatibility.py:14](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3/scripts/compile_compatibility.py#L14)
- [scripts/compile_tzlc.py:22](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3/scripts/compile_tzlc.py#L22)
- [npm/icloudpd/bin/icloudpd.js](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3/npm/icloudpd/bin/icloudpd.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| binary_dist package | library | Observed | Groups 2 file(s) under binary_dist package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: GlobalConfig, UserConfig, _DefaultConfig. |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed top-level functions: add_global_options, add_options_for_user,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| foundation package | library | Observed | Groups 6 file(s) under foundation package (observed from repository paths and static analysis). Observed top-level classes: VersionInfo. Observed top-level functions: _, _apply_rules_internal, always_false, always_true,… |
| icloudpd package | library | Observed | Groups 21 file(s) under icloudpd package (observed from repository paths and static analysis). Observed top-level classes: Counter, DownloadResult, FileRecord, IPDLogger, LogLevel, MFAProvider. Observed top-level functi… |
| npm package | library | Observed | Groups 2 file(s) under npm package (observed from repository paths and static analysis). |
| pyicloud_ipd package | library | Observed | Groups 12 file(s) under pyicloud_ipd package (observed from repository paths and static analysis). Observed top-level classes: AssetItemType, AssetVersion, AssetVersionSize, AuthenticatedSession, FileMatchPolicy, LivePh… |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: _matrix, _stats, print_breakdowns. |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: PhotoAlbum, PhotoAsset, PhotoLibrary, PhotosService. Observed top-level functions: apply_fi… |
| starters package | library | Observed | Groups 1 file(s) under starters package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 60 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH pyicloud_ipd.services.photos.time.sleep, PATCH pyicloud_ipd.services.photos.time.sleep, PATCH pyicloud_ipd.servi… |

## Important files

- `.devcontainer/node/devcontainer.json` (config)
- `.devcontainer/python/devcontainer.json` (config)
- `.dockerignore` (container)
- `.github/dependabot.yml` (config)
- `.github/workflows/README.md` (ci)
- `.github/workflows/build-docs.yml` (ci)
- `.github/workflows/build-package.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/compile-notes.yml` (ci)
- `.github/workflows/create-release.yml` (ci)
- `.github/workflows/extract-changelog.yml` (ci)
- `.github/workflows/patch-version.yml` (ci)
- `.github/workflows/produce-artifacts.yml` (ci)
- `.github/workflows/publish-docs.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/quality-checks.yml` (ci)
- `.github/workflows/refresh-docs.yml` (ci)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `Dockerfile.build` (container)
- `Dockerfile.build-doc` (container)
- `Dockerfile.build-musl` (container)
- `binary_dist/pyproject.toml` (manifest)
- `npm/@icloudpd/darwin-arm64/package.json` (manifest)
- `npm/@icloudpd/darwin-x64/package.json` (manifest)
- `npm/@icloudpd/linux-arm/package.json` (manifest)
- `npm/@icloudpd/linux-arm64/package.json` (manifest)
- `npm/@icloudpd/linux-x64/package.json` (manifest)
- `npm/@icloudpd/win32-x64/package.json` (manifest)
- `npm/icloudpd/package.json` (manifest)
- `pyproject.toml` (manifest)
- `requirements-pip.txt` (manifest)
- `src/icloudpd/server/static/manifest.json` (config)

## Top-level layout

- `src` — 63 analysed file(s)
- `tests` — 58 analysed file(s)
- `scripts` — 27 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 17 analysed file(s)
- `npm` — 15 analysed file(s)
- `docs` — 11 analysed file(s)
- `binary_dist` — 5 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `examples` — 1 analysed file(s)
- `jq` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (6 x generated/minified file excluded; 1 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3caeae584c3d8bc6fcc51a1c9f7e5413b1422fd3` is the revision these paths and observations refer to.
