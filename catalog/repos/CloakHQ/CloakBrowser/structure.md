# Project structure: CloakHQ/CloakBrowser

**Analysed commit:** `0c110fab97ee98d7d4ba6c4f53d909cee08e92b6`

**Commit reference:** [0c110fab97ee98d7d4ba6c4f53d909cee08e92b6](https://github.com/CloakHQ/CloakBrowser/commit/0c110fab97ee98d7d4ba6c4f53d909cee08e92b6)

**Tree at this commit:** [CloakHQ/CloakBrowser@0c110fab97ee](https://github.com/CloakHQ/CloakBrowser/tree/0c110fab97ee98d7d4ba6c4f53d909cee08e92b6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | CloakHQ/CloakBrowser |
| Description | Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 50+ tests passed. |
| Stars | 32887 |
| Forks | 2730 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `0c110fab97ee98d7d4ba6c4f53d909cee08e92b6` |
| Retrieved at | 2026-11-14T19:07:01.763650+00:00 |
| Files in this snapshot | 241 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (3 files)
    actions.lock
    ci.yml
    publish.yml
  FUNDING.yml
  dependabot.yml
bin/  (4 files)
  cloakserve
  cloaktest
  docker-entrypoint.sh
  fetch-widevine.py
cloakbrowser/  (19 files)
  human/  (10 files)
    __init__.py
    config.py
    engine.py
    errors.py
    fields.py
    injected.py
    keyboard.py
    mouse.py
    patch.py
    world.py
  __init__.py
  __main__.py
  _version.py
  browser.py
  config.py
  download.py
  geoip.py
  license.py
  widevine.py
dotnet/  (86 files)
  examples/  (2 files)
    CloakBrowser.Examples/  (2 files)
      … 2 files under this directory
  src/  (44 files)
    CloakBrowser/  (40 files)
      … 40 files under this directory
    CloakBrowser.Cli/  (2 files)
      … 2 files under this directory
    CloakBrowser.Generators/  (2 files)
      … 2 files under this directory
  tests/  (37 files)
    CloakBrowser.Tests/  (37 files)
      … 37 files under this directory
  .gitignore
  CloakBrowser.sln
  README.md
examples/  (17 files)
  integrations/  (12 files)
    aws_lambda/  (4 files)
      … 4 files under this directory
    agent_browser.sh
    browser_use_example.py
    crawl4ai_example.py
    crawlee_example.py
    langchain_loader.py
    scrapling_example.py
    selenium_example.py
    undetected_chromedriver.py
  basic.py
  fingerprint_scan_test.py
  persistent_context.py
  recaptcha_score.py
  stealth_test.py
js/  (61 files)
  examples/  (5 files)
    basic-playwright.ts
    basic-puppeteer.ts
    persistent-context.ts
    stagehand.ts
    stealth-test.ts
  src/  (28 files)
    human/  (11 files)
      … 11 files under this directory
    human-puppeteer/  (3 files)
      … 3 files under this directory
    args.ts
    cli.ts
    config.ts
    download.ts
    fonts.ts
    geoip.ts
    index.ts
    license.ts
    playwright.ts
    profile-seed.ts
    proxy.ts
    puppeteer.ts
    types.ts
    widevine.ts
  tests/  (24 files)
    claim.test.ts
    cli.test.ts
    config.test.ts
    extension-loading.test.ts
    fonts.test.ts
    geoip.test.ts
    humanize.test.ts
    humanizeEngine.test.ts
    humanizeHarness.ts
    humanizePuppeteer.test.ts
    launch.test.ts
    license.test.ts
    profile-seed.test.ts
    proxy.test.ts
    puppeteer.test.ts
    require.test.ts
    setup.ts
    signature.test.ts
    stealth.puppeteer.test.ts
    stealth.test.ts
    update.test.ts
    welcome.test.ts
    widevine-integration.test.ts
    widevine.test.ts
  README.md
  package.json
  tsconfig.json
  vitest.config.ts
tests/  (36 files)
  __init__.py
  conftest.py
  test_build_args.py
  test_build_launch_options.py
  test_cli.py
  test_cloakserve.py
  test_config.py
  test_extension_loading.py
  test_extract.py
  test_fetch_widevine.py
  test_font_warning.py
  test_free_claim.py
  test_free_version_pin.py
  test_geoip.py
  test_human_visual.mjs
  test_human_visual.py
  test_humanize_engine.py
  test_humanize_unit.mjs
  test_humanize_unit.py
  test_lambda_security.py
  test_launch.py
  test_launch_context.py
  test_license.py
  test_license_error.py
  … 12 more files
.dockerignore
.gitattributes
.gitignore
BINARY-LICENSE.md
CHANGELOG.md
Dockerfile
LICENSE
README.md
flake.lock
flake.nix
pyproject.toml
```

## Entry points

- [bin/fetch-widevine.py:294](https://github.com/CloakHQ/CloakBrowser/blob/0c110fab97ee98d7d4ba6c4f53d909cee08e92b6/bin/fetch-widevine.py#L294)
- [cloakbrowser/__main__.py](https://github.com/CloakHQ/CloakBrowser/blob/0c110fab97ee98d7d4ba6c4f53d909cee08e92b6/cloakbrowser/__main__.py)
- [js/src/human-puppeteer/index.ts](https://github.com/CloakHQ/CloakBrowser/blob/0c110fab97ee98d7d4ba6c4f53d909cee08e92b6/js/src/human-puppeteer/index.ts)
- [js/src/human/index.ts](https://github.com/CloakHQ/CloakBrowser/blob/0c110fab97ee98d7d4ba6c4f53d909cee08e92b6/js/src/human/index.ts)
- [js/src/index.ts](https://github.com/CloakHQ/CloakBrowser/blob/0c110fab97ee98d7d4ba6c4f53d909cee08e92b6/js/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| cloakbrowser package | library | Observed | Groups 16 file(s) under cloakbrowser package (observed from repository paths and static analysis). Observed top-level classes: Action, ActionabilityError, BinaryVerificationError, BoundedCalls, CloakBrowserLicenseError,… |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: HumanConfig, HumanConfigOverrides. Observed top-level functions: _careful_config, _dr… |
| dotnet package | library | Observed | Groups 42 file(s) under dotnet package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _arch, _binary_version, _collect_diagnostics, _console_glyph, _crx_appid, _default_out. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 34 file(s) under js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 99 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH os.path.exists, PATCH os.path.exists, PATCH subprocess.Popen, PATCH cloakbrowser.browser.ensure_binary, PATCH pl… |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/actions.lock` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `Dockerfile` (container)
- `examples/integrations/aws_lambda/Dockerfile` (container)
- `js/package.json` (manifest)
- `js/tsconfig.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `dotnet` — 86 analysed file(s)
- `js` — 61 analysed file(s)
- `tests` — 36 analysed file(s)
- `cloakbrowser` — 19 analysed file(s)
- `examples` — 17 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 7 analysed file(s)
- `bin` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0c110fab97ee98d7d4ba6c4f53d909cee08e92b6` is the revision these paths and observations refer to.
