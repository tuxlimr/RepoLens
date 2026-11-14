# Project structure: Miserlou/Zappa

**Analysed commit:** `5a11c17f5ecf0568bdb73b4baf6fb08ff0184f39`

**Commit reference:** [5a11c17f5ecf0568bdb73b4baf6fb08ff0184f39](https://github.com/Miserlou/Zappa/commit/5a11c17f5ecf0568bdb73b4baf6fb08ff0184f39)

**Tree at this commit:** [Miserlou/Zappa@5a11c17f5ecf](https://github.com/Miserlou/Zappa/tree/5a11c17f5ecf0568bdb73b4baf6fb08ff0184f39)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Miserlou/Zappa |
| Description | Serverless Python |
| Stars | 11811 |
| Forks | 1166 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `5a11c17f5ecf0568bdb73b4baf6fb08ff0184f39` |
| Retrieved at | 2026-11-14T19:10:23.549041+00:00 |
| Files in this snapshot | 475 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
docs/  (2 files)
  domain_with_free_ssl_dns.md
  domain_with_free_ssl_http.md
example/  (7 files)
  policy/  (1 files)
    deploy.json
  README.md
  app.py
  authmodule.py
  mymodule.py
  requirements.txt
  zappa_settings.json
tests/  (436 files)
  data/  (3 files)
    test1/  (1 files)
      … 1 files under this directory
    test2/  (1 files)
      … 1 files under this directory
    test1.py
  placebo/  (405 files)
    TestZappa.test_cli_aws/  (326 files)
      … 326 files under this directory
    TestZappa.test_cli_aws_status/  (9 files)
      … 9 files under this directory
    TestZappa.test_cli_cognito_triggers/  (4 files)
      … 4 files under this directory
    TestZappa.test_cognito_trigger/  (4 files)
      … 4 files under this directory
    TestZappa.test_cognito_trigger_existing/  (4 files)
      … 4 files under this directory
    TestZappa.test_cognito_trigger_existing_UnusedAccountValidityDays/  (4 files)
      … 4 files under this directory
    TestZappa.test_copy_on_s3/  (9 files)
      … 9 files under this directory
    TestZappa.test_create_iam_roles/  (6 files)
      … 6 files under this directory
    TestZappa.test_create_lambda_function_local/  (6 files)
      … 6 files under this directory
    TestZappa.test_create_lambda_function_s3/  (6 files)
      … 6 files under this directory
    TestZappa.test_deploy_api_gateway/  (10 files)
      … 10 files under this directory
    TestZappa.test_fetch_logs/  (2 files)
      … 2 files under this directory
    TestZappa.test_get_api_url/  (1 files)
      … 1 files under this directory
    TestZappa.test_handler/  (1 files)
      … 1 files under this directory
    TestZappa.test_invoke_lambda_function/  (1 files)
      … 1 files under this directory
    TestZappa.test_rollback_lambda_function_version/  (4 files)
      … 4 files under this directory
    TestZappa.test_upload_remove_s3/  (8 files)
      … 8 files under this directory
  README.md
  __init__.py
  name_scenarios.json
  test_app.py
  test_bad_circular_extends_settings.json
  test_bad_environment_vars.json
  test_bad_settings.json
  test_bad_stage_name_settings.json
  test_bot_exception_handler_settings.py
  test_bot_handler_being_triggered.py
  test_event_script_app.py
  test_event_script_settings.py
  test_exception_handler_settings.py
  test_handler.py
  test_non_ascii_environment_var_key.json
  test_one_env.json
  test_settings.toml
  test_settings.yaml
  test_settings.yml
  test_wsgi_script_name_app.py
  test_wsgi_script_name_settings.py
  tests.py
  tests_async.py
  tests_async_old.py
  … 4 more files
zappa/  (13 files)
  ext/  (2 files)
    __init__.py
    django_zappa.py
  __init__.py
  async.py
  asynchronous.py
  cli.py
  core.py
  handler.py
  letsencrypt.py
  middleware.py
  policies.py
  utilities.py
  wsgi.py
.gitignore
.travis.yml
CHANGELOG.md
LICENSE
MANIFEST.in
README.md
requirements.in
requirements.sh
requirements.txt
setup.py
test.sh
test_requirements.in
test_requirements.txt
test_settings.json
test_settings.py
```

## Entry points

- [zappa/cli.py](https://github.com/Miserlou/Zappa/blob/5a11c17f5ecf0568bdb73b4baf6fb08ff0184f39/zappa/cli.py)
- [zappa/cli.py](https://github.com/Miserlou/Zappa/blob/5a11c17f5ecf0568bdb73b4baf6fb08ff0184f39/zappa/cli.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ZappaCLI. Observed top-level functions: common_log, create_wsgi_request, disable_click_col… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 440 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /return/request/url, PATCH zappa.core.find_packages, PATCH os.re… |
| zappa package | library | Observed | Groups 11 file(s) under zappa package (observed from repository paths and static analysis). Observed top-level classes: AsyncException, InvalidAwsLambdaName, LambdaAsyncResponse, LambdaHandler, SnsAsyncResponse, Zappa.… |

## Important files

- `.travis.yml` (ci)
- `MANIFEST.in` (manifest)
- `example/policy/deploy.json` (config)
- `example/requirements.txt` (manifest)
- `example/zappa_settings.json` (config)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `tests` — 436 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `zappa` — 13 analysed file(s)
- `example` — 7 analysed file(s)
- `.github` — 2 analysed file(s)
- `docs` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5a11c17f5ecf0568bdb73b4baf6fb08ff0184f39` is the revision these paths and observations refer to.
