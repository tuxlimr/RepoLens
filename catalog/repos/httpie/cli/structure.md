# Project structure: httpie/cli

**Analysed commit:** `5b604c37c6c67e18e7c3e9aee6c88a8c22b98345`

**Commit reference:** [5b604c37c6c67e18e7c3e9aee6c88a8c22b98345](https://github.com/httpie/cli/commit/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345)

**Tree at this commit:** [httpie/cli@5b604c37c6c6](https://github.com/httpie/cli/tree/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | httpie/cli |
| Description | 🥧 HTTPie CLI  — modern, user-friendly command-line HTTP client for the API era. JSON support, colors, sessions, downloads, plugins & more. |
| Stars | 38715 |
| Forks | 4043 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `5b604c37c6c67e18e7c3e9aee6c88a8c22b98345` |
| Retrieved at | 2026-11-14T19:06:46.383704+00:00 |
| Files in this snapshot | 258 |

## Directory tree

```text
.github/  (19 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    other.md
  workflows/  (15 files)
    benchmark.yml
    code-style.yml
    content.yml
    coverage.yml
    docs-check-markdown.yml
    docs-deploy.yml
    release-brew.yml
    release-choco.yml
    release-linux-standalone.yml
    release-pypi.yml
    release-snap.yml
    stale.yml
    test-package-linux-snap.yml
    test-package-mac-brew.yml
    tests.yml
  dependabot.yml
docs/  (31 files)
  contributors/  (5 files)
    README.md
    fetch.py
    generate.py
    people.json
    snippet.jinja2
  installation/  (4 files)
    README.md
    generate.py
    installation.jinja2
    methods.yml
  packaging/  (18 files)
    brew/  (3 files)
      … 3 files under this directory
    linux-arch/  (2 files)
      … 2 files under this directory
    linux-centos/  (1 files)
      … 1 files under this directory
    linux-debian/  (1 files)
      … 1 files under this directory
    linux-fedora/  (3 files)
      … 3 files under this directory
    mac-ports/  (2 files)
      … 2 files under this directory
    snapcraft/  (1 files)
      … 1 files under this directory
    windows-chocolatey/  (4 files)
      … 4 files under this directory
    README.md
  README.md
  config.json
  httpie-logo.svg
  markdownlint.rb
extras/  (16 files)
  man/  (3 files)
    http.1
    httpie.1
    https.1
  packaging/  (7 files)
    linux/  (7 files)
      … 7 files under this directory
  profiling/  (3 files)
    README.md
    benchmarks.py
    run.py
  scripts/  (1 files)
    generate_man_pages.py
  httpie-completion.bash
  httpie-completion.fish
httpie/  (78 files)
  cli/  (15 files)
    nested_json/  (5 files)
      … 5 files under this directory
    __init__.py
    argparser.py
    argtypes.py
    constants.py
    definition.py
    dicts.py
    exceptions.py
    options.py
    requestitems.py
    utils.py
  internal/  (5 files)
    __build_channel__.py
    __init__.py
    daemon_runner.py
    daemons.py
    update_warnings.py
  legacy/  (3 files)
    __init__.py
    v3_1_0_session_cookie_format.py
    v3_2_0_session_header_format.py
  manager/  (10 files)
    tasks/  (5 files)
      … 5 files under this directory
    __init__.py
    __main__.py
    cli.py
    compat.py
    core.py
  output/  (23 files)
    formatters/  (5 files)
      … 5 files under this directory
    lexers/  (5 files)
      … 5 files under this directory
    ui/  (7 files)
      … 7 files under this directory
    __init__.py
    models.py
    processing.py
    streams.py
    utils.py
    writer.py
  plugins/  (5 files)
    __init__.py
    base.py
    builtin.py
    manager.py
    registry.py
  __init__.py
  __main__.py
  adapters.py
  client.py
  compat.py
  config.py
  context.py
  cookies.py
  core.py
  downloads.py
  encoding.py
  models.py
  sessions.py
  ssl_.py
  status.py
  uploads.py
  utils.py
tests/  (98 files)
  client_certs/  (1 files)
    client.crt
  fixtures/  (53 files)
    session_data/  (22 files)
      … 22 files under this directory
    xmldata/  (26 files)
      … 26 files under this directory
    .editorconfig
    __init__.py
    test.json
    test.txt
    test_with_dupe_keys.json
  utils/  (7 files)
    matching/  (4 files)
      … 4 files under this directory
    __init__.py
    http_server.py
    plugins_cli.py
  README.md
  __init__.py
  conftest.py
  test_auth.py
  test_auth_plugins.py
  test_binary.py
  test_cli.py
  test_cli_ui.py
  test_cli_utils.py
  test_compress.py
  test_config.py
  test_cookie.py
  test_cookie_on_redirects.py
  test_defaults.py
  test_downloads.py
  test_encoding.py
  test_errors.py
  test_exit_status.py
  test_httpie.py
  test_httpie_cli.py
  test_json.py
  test_meta.py
  test_offline.py
  test_output.py
  … 13 more files
.editorconfig
.gitignore
.packit.yaml
AUTHORS.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
Makefile
README.md
SECURITY.md
pytest.ini
setup.cfg
setup.py
snapcraft.yaml
```

## Entry points

- [extras/packaging/linux/build.py:108](https://github.com/httpie/cli/blob/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345/extras/packaging/linux/build.py#L108)
- [extras/packaging/linux/scripts/http_cli.py:3](https://github.com/httpie/cli/blob/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345/extras/packaging/linux/scripts/http_cli.py#L3)
- [extras/packaging/linux/scripts/httpie_cli.py:3](https://github.com/httpie/cli/blob/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345/extras/packaging/linux/scripts/httpie_cli.py#L3)
- [extras/profiling/benchmarks.py:201](https://github.com/httpie/cli/blob/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345/extras/profiling/benchmarks.py#L201)
- [extras/profiling/run.py:286](https://github.com/httpie/cli/blob/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345/extras/profiling/run.py#L286)
- [extras/scripts/generate_man_pages.py:187](https://github.com/httpie/cli/blob/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345/extras/scripts/generate_man_pages.py#L187)
- [httpie/__main__.py:17](https://github.com/httpie/cli/blob/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345/httpie/__main__.py#L17)
- [httpie/cli/options.py:60](https://github.com/httpie/cli/blob/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345/httpie/cli/options.py#L60)
- [httpie/manager/__main__.py:60](https://github.com/httpie/cli/blob/5b604c37c6c67e18e7c3e9aee6c88a8c22b98345/httpie/manager/__main__.py#L60)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BaseConfigDict, Config, ConfigFileError. Observed top-level functions: get_default_co… |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: HTTPMessage, HTTPRequest, HTTPResponse, OutputOptions, ProcessingOptions, RequestsMessageKind. Observed… |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Group. Observed top-level classes: Argument, BaseRunner, CommandRunner, Conte… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: apply_missing_repeated_headers, build_requests_session, collect_messages, dump_request, en… |
| extras package | library | Observed | Groups 2 file(s) under extras package (observed from repository paths and static analysis). Observed top-level functions: hook. |
| httpie package | library | Observed | Groups 70 file(s) under httpie package (observed from repository paths and static analysis). Observed top-level classes: AuthCredentials, AuthCredentialsArgType, AuthPlugin, BaseDisplay, BaseHTTPieArgumentParser, BaseMu… |
| Tests | test | Observed | Groups 98 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH httpie.cli.argtypes.AuthCredentials._getpass, PATCH httpie.cli.argtypes.AuthCredentials._getpass, PATCH httpie.d… |

## Important files

- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/benchmark.yml` (ci)
- `.github/workflows/code-style.yml` (ci)
- `.github/workflows/content.yml` (ci)
- `.github/workflows/coverage.yml` (ci)
- `.github/workflows/docs-check-markdown.yml` (ci)
- `.github/workflows/docs-deploy.yml` (ci)
- `.github/workflows/release-brew.yml` (ci)
- `.github/workflows/release-choco.yml` (ci)
- `.github/workflows/release-linux-standalone.yml` (ci)
- `.github/workflows/release-pypi.yml` (ci)
- `.github/workflows/release-snap.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test-package-linux-snap.yml` (ci)
- `.github/workflows/test-package-mac-brew.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.packit.yaml` (config)
- `MANIFEST.in` (manifest)
- `docs/config.json` (config)
- `docs/contributors/people.json` (config)
- `docs/installation/methods.yml` (config)
- `extras/packaging/linux/Dockerfile` (container)
- `pytest.ini` (config)
- `setup.cfg` (manifest)
- `setup.py` (manifest)
- `snapcraft.yaml` (config)

## Top-level layout

- `tests` — 98 analysed file(s)
- `httpie` — 78 analysed file(s)
- `docs` — 31 analysed file(s)
- `.github` — 19 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `extras` — 16 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5b604c37c6c67e18e7c3e9aee6c88a8c22b98345` is the revision these paths and observations refer to.
