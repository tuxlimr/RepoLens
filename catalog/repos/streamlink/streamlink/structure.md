# Project structure: streamlink/streamlink

**Analysed commit:** `5896d42b0066295d6305c39df0d36f9feb27e483`

**Commit reference:** [5896d42b0066295d6305c39df0d36f9feb27e483](https://github.com/streamlink/streamlink/commit/5896d42b0066295d6305c39df0d36f9feb27e483)

**Tree at this commit:** [streamlink/streamlink@5896d42b0066](https://github.com/streamlink/streamlink/tree/5896d42b0066295d6305c39df0d36f9feb27e483)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | streamlink/streamlink |
| Description | Streamlink is a CLI utility which pipes video streams from various services into a video player |
| Stars | 11921 |
| Forks | 1212 |
| Licence | BSD-2-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `5896d42b0066295d6305c39df0d36f9feb27e483` |
| Retrieved at | 2026-11-14T19:10:20.771499+00:00 |
| Files in this snapshot | 664 |

## Directory tree

```text
.github/  (22 files)
  DISCUSSION_TEMPLATE/  (2 files)
    general.yml
    q-a.yml
  ISSUE_TEMPLATE/  (5 files)
    1_plugin_issue.yml
    2_bug_report.yml
    3_plugin_request.yml
    4_feature_request.yml
    config.yml
  workflows/  (11 files)
    scripts/  (5 files)
      … 5 files under this directory
    docs.yml
    lint.yml
    preview-build.yml
    release.yml
    test.yml
    useragents.yml
  FUNDING.yml
  dependabot.yml
  pull_request_template.md
  release_template.md
build_backend/  (7 files)
  __init__.py
  commands.py
  onbuild.py
  plugins_json.py
  test_build_backend.py
  test_onbuild.py
  test_plugins_json.py
docs/  (54 files)
  _static/  (8 files)
    styles/  (1 files)
      … 1 files under this directory
    github-lockup-dark.svg
    github-lockup-light.svg
    icon-ffmpeg.svg
    icon-python.svg
    jetbrains-mono-black.svg
    jetbrains-mono-white.svg
    site.webmanifest
  _templates/  (4 files)
    sidebar/  (2 files)
      … 2 files under this directory
    base.html
    page.html
  api/  (9 files)
    cache.rst
    exceptions.rst
    options.rst
    plugin.rst
    session.rst
    stream.rst
    streamlink.rst
    validate.rst
    webbrowser.rst
  api_guide/  (2 files)
    quickstart.rst
    validate.rst
  cli/  (8 files)
    plugins/  (1 files)
      … 1 files under this directory
    config.rst
    metadata.rst
    plugin-sideloading.rst
    plugins.rst
    protocols.rst
    proxy.rst
    tutorial.rst
  sphinxext/  (5 files)
    ext_argparse.py
    ext_github.py
    ext_html_template_vars.py
    ext_plugins.py
    ext_releaseref.py
  Makefile
  _man.rst
  acknowledgements.rst
  api.rst
  api_guide.rst
  applications.rst
  cli.rst
  conf.py
  deprecations.rst
  developing.rst
  docutils.conf
  index.rst
  install.rst
  migrations.rst
  players.rst
  plugins.rst
  support.rst
  thirdparty.rst
script/  (7 files)
  build-and-sign.sh
  build-shell-completions.py
  deploy-docs.sh
  generate-cdp.py
  github-release.py
  test-plugin-urls.py
  update-user-agents.py
src/  (262 files)
  streamlink/  (231 files)
    packages/  (2 files)
      … 2 files under this directory
    plugin/  (8 files)
      … 8 files under this directory
    plugins/  (136 files)
      … 136 files under this directory
    session/  (7 files)
      … 7 files under this directory
    stream/  (18 files)
      … 18 files under this directory
    utils/  (20 files)
      … 20 files under this directory
    validate/  (5 files)
      … 5 files under this directory
    webbrowser/  (23 files)
      … 23 files under this directory
    __init__.py
    __main__.py
    _version.py
    api.py
    buffers.py
    cache.py
    compat.py
    exceptions.py
    logger.py
    options.py
    py.typed
    user_input.py
  streamlink_cli/  (31 files)
    console/  (9 files)
      … 9 files under this directory
    output/  (5 files)
      … 5 files under this directory
    utils/  (5 files)
      … 5 files under this directory
    __init__.py
    __main__.py
    _parser.py
    argparser.py
    compat.py
    constants.py
    exceptions.py
    main.py
    py.typed
    setup_args.py
    show_matchers.py
    streamrunner.py
tests/  (294 files)
  cli/  (38 files)
    console/  (7 files)
      … 7 files under this directory
    main/  (19 files)
      … 19 files under this directory
    output/  (3 files)
      … 3 files under this directory
    utils/  (5 files)
      … 5 files under this directory
    __init__.py
    test_argparser.py
    test_compat.py
    test_streamrunner.py
  mixins/  (2 files)
    __init__.py
    stream_hls.py
  plugin/  (5 files)
    override/  (1 files)
      … 1 files under this directory
    __init__.py
    testplugin.py
    testplugin_invalid.py
    testplugin_missing.py
  plugins/  (137 files)
    __init__.py
    conftest.py
    test_abematv.py
    test_adultswim.py
    test_albavision.py
    test_aloula.py
    test_app17.py
    test_ard_mediathek.py
    test_artetv.py
    test_atpchallenger.py
    test_atresplayer.py
    test_bbciplayer.py
    test_bfmtv.py
    test_bigo.py
    test_bilibili.py
    test_blasttv.py
    test_blazetv.py
    test_bloomberg.py
    test_brightcove.py
    test_btv.py
    test_cbsnews.py
    test_cdnbg.py
    test_ceskatelevize.py
    test_chzzk.py
    … 113 more files
  resources/  (47 files)
    cli/  (5 files)
      … 5 files under this directory
    dash/  (32 files)
      … 32 files under this directory
    hls/  (9 files)
      … 9 files under this directory
    __init__.py
  session/  (5 files)
    __init__.py
    test_http.py
    test_options.py
    test_plugins.py
    test_session.py
  stream/  (16 files)
    dash/  (3 files)
      … 3 files under this directory
    hls/  (4 files)
      … 4 files under this directory
    __init__.py
    conftest.py
    test_ffmpegmux.py
    test_file.py
    test_init.py
    test_segmented.py
    test_stream_json.py
    test_stream_to_url.py
    test_stream_wrappers.py
  testutils/  (3 files)
    __init__.py
    handshake.py
    test_handshake.py
  utils/  (20 files)
    __init__.py
    test_args.py
    test_cache.py
    test_crypto.py
    test_data.py
    test_dataclass.py
    test_formatter.py
    test_id3v2.py
    test_init.py
    test_l10n.py
    test_module.py
    test_named_pipe.py
    test_num.py
    test_parse.py
    test_path.py
    test_processoutput.py
    test_random.py
    test_thread.py
    test_times.py
    test_url.py
  webbrowser/  (8 files)
    cdp/  (4 files)
      … 4 files under this directory
    __init__.py
    conftest.py
    test_chromium.py
    test_webbrowser.py
  __init__.py
  conftest.py
  test_api_websocket.py
  test_buffers.py
  test_cache.py
  test_compat.py
  test_logger.py
  test_options.py
  test_plugin.py
  test_plugin_userinput.py
  test_plugins.py
  test_streamlink_api.py
  test_validate.py
.codecov.yml
.editorconfig
.git-blame-ignore-revs
.gitattributes
.gitignore
.readthedocs.yml
AUTHORS
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
SECURITY.md
icon.svg
pyproject.toml
setup.py
signing.key.enc
```

## Entry points

- [src/streamlink/__main__.py:1](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/src/streamlink/__main__.py#L1)
- [src/streamlink_cli/__main__.py:1](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/src/streamlink_cli/__main__.py#L1)
- [src/streamlink_cli/main.py](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/src/streamlink_cli/main.py)
- [src/streamlink_cli/main.py](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/src/streamlink_cli/main.py)
- [build_backend/plugins_json.py:491](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/build_backend/plugins_json.py#L491)
- [script/build-shell-completions.py:73](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/script/build-shell-completions.py#L73)
- [script/generate-cdp.py:1056](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/script/generate-cdp.py#L1056)
- [script/github-release.py:578](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/script/github-release.py#L578)
- [script/test-plugin-urls.py:248](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/script/test-plugin-urls.py#L248)
- [script/update-user-agents.py:126](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/script/update-user-agents.py#L126)
- [setup.py:76](https://github.com/streamlink/streamlink/blob/5896d42b0066295d6305c39df0d36f9feb27e483/setup.py#L76)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 6 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: AWSWAF, WebsocketClient. |
| build_backend package | library | Observed | Groups 3 file(s) under build_backend package (observed from repository paths and static analysis). Observed top-level classes: Proxy, StreamlinkBuildPyCommand. Observed top-level functions: _filter_cmd_option_args, get_… |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: is_wheel_for_windows. |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Author, CdpCommand, CdpDomain, CdpEvent, CdpItems, CdpParameter. Observed top-level functi… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: CDPClient, CDPClientSession, CMRequestProxy, RequestPausedHandler. |
| script package | library | Observed | Groups 2 file(s) under script package (observed from repository paths and static analysis). |
| streamlink package | library | Observed | Groups 221 file(s) under streamlink package (observed from repository paths and static analysis). Observed top-level classes: ARDMediathek, AbemaTV, AbemaTVHLSStream, AbemaTVHLSStreamReader, AbemaTVHLSStreamWriter, Abem… |
| streamlink_cli package | library | Observed | Groups 27 file(s) under streamlink_cli package (observed from repository paths and static analysis). Observed top-level classes: ArgumentParser, CONSOLE_SCREEN_BUFFER_INFO, COORD, ConsoleOutput, ConsoleOutputStream, Con… |
| Tests | test | Observed | Groups 297 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH streamlink.plugins.kick.log, PATCH streamlink.plugins.kick.log, PATCH streamlink.plugins.kick.log, PATCH stream… |

## Important files

- `.codecov.yml` (config)
- `.editorconfig` (config)
- `.github/DISCUSSION_TEMPLATE/general.yml` (config)
- `.github/DISCUSSION_TEMPLATE/q-a.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/1_plugin_issue.yml` (config)
- `.github/ISSUE_TEMPLATE/2_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/3_plugin_request.yml` (config)
- `.github/ISSUE_TEMPLATE/4_feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/preview-build.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/scripts/fetch-tags.sh` (ci)
- `.github/workflows/scripts/install-temp-dependencies.sh` (ci)
- `.github/workflows/scripts/lint-git-commit-msg-format.awk` (ci)
- `.github/workflows/scripts/lint-git-common.awk` (ci)
- `.github/workflows/scripts/lint-git-linear-history.awk` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/useragents.yml` (ci)
- `.readthedocs.yml` (config)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `tests` — 294 analysed file(s)
- `src` — 262 analysed file(s)
- `docs` — 54 analysed file(s)
- `.github` — 22 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `build_backend` — 7 analysed file(s)
- `script` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5896d42b0066295d6305c39df0d36f9feb27e483` is the revision these paths and observations refer to.
