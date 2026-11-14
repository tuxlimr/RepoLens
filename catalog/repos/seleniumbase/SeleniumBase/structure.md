# Project structure: seleniumbase/SeleniumBase

**Analysed commit:** `e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5`

**Commit reference:** [e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5](https://github.com/seleniumbase/SeleniumBase/commit/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5)

**Tree at this commit:** [seleniumbase/SeleniumBase@e51d66c1b343](https://github.com/seleniumbase/SeleniumBase/tree/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | seleniumbase/SeleniumBase |
| Description | Python APIs for web automation, e2e testing, and bypassing bot-detection with ease. |
| Stars | 13255 |
| Forks | 1616 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5` |
| Retrieved at | 2026-11-14T19:09:54.031709+00:00 |
| Files in this snapshot | 771 |

## Directory tree

```text
.github/  (8 files)
  workflows/  (6 files)
    pages.yml
    publish-mcp.yml
    python-nightly-mac.yml
    python-nightly-ubuntu.yml
    python-nightly-windows.yml
    python-package.yml
  FUNDING.yml
  Workflows.md
examples/  (496 files)
  behave_bdd/  (16 files)
    features/  (13 files)
      … 13 files under this directory
    ReadMe.md
    __init__.py
    behave.ini
  boilerplates/  (17 files)
    samples/  (10 files)
      … 10 files under this directory
    ReadMe.md
    __init__.py
    base_test_case.py
    boilerplate_test.py
    classic_obj_test.py
    page_objects.py
    sb_fixture_test.py
  capabilities/  (7 files)
    ReadMe.md
    mac_cap_file.py
    sample_cap_file_BS.py
    sample_cap_file_BS.yml
    sample_cap_file_SL.py
    selenoid_cap_file.py
    win10_cap_file.py
  case_plans/  (8 files)
    basic_test.MyTestClass.test_basics.md
    my_first_test.MyTestClass.test_swag_labs.md
    shadow_root_test.ShadowRootTest.test_shadow_root.md
    test_assert_elements.ListAssertTests.test_assert_list_of_elements.md
    test_calculator.CalculatorTests.test_6_times_7_plus_12_equals_54.md
    test_demo_site.DemoSiteTests.test_demo_site.md
    test_login.SwagLabsLoginTests.test_swag_labs_login.md
    test_mfa_login.TestMFALogin.test_mfa_login.md
  cdp_mode/  (186 files)
    playwright/  (37 files)
      … 37 files under this directory
    ReadMe.md
    __init__.py
    raw_ad_blocking.py
    raw_ahrefs.py
    raw_albertsons.py
    raw_amazon.py
    raw_antibot.py
    raw_async.py
    raw_basic_async.py
    raw_basic_cdp.py
    raw_basic_mobile.py
    raw_bestwestern.py
    raw_browserscan.py
    raw_canvas.py
    raw_cdp.py
    raw_cdp_bing_cap.py
    raw_cdp_browserscan.py
    raw_cdp_clearcote.py
    raw_cdp_cloudflare.py
    raw_cdp_downloads.py
    raw_cdp_drivers.py
    raw_cdp_etsy.py
    raw_cdp_extended.py
    raw_cdp_facebook.py
    … 125 more files
  chart_maker/  (9 files)
    ReadMe.md
    chart_presentation.py
    my_chart.py
    pie_charts.py
    test_area_chart.py
    test_display_chart.py
    test_line_chart.py
    test_multi_series.py
    test_save_chart.py
  desktop_apps/  (2 files)
    ReadMe.md
    recorder.py
  dialog_boxes/  (2 files)
    ReadMe.md
    dialog_box_tour.py
  example_logs/  (3 files)
    ReadMe.md
    basic_test_info.txt
    page_source.html
  master_qa/  (5 files)
    ReadMe.md
    __init__.py
    basic_masterqa_test_0.py
    masterqa_test_1.py
    pytest.ini
  migration/  (40 files)
    protractor/  (8 files)
      … 8 files under this directory
    raw_selenium/  (31 files)
      … 31 files under this directory
    __init__.py
  offline_examples/  (8 files)
    __init__.py
    demo_page.html
    load_html_test.py
    test_demo_page.py
    test_extended_driver.py
    test_handle_alerts.py
    test_request_fixture.py
    test_user_agent.py
  presenter/  (13 files)
    ReadMe.md
    core_presentation.py
    edge_presentation.py
    fundamentals.py
    hacking_with_cdp.py
    multi_uc.py
    my_presentation.py
    py_virtual_envs.py
    ua_presentation_4.py
    ua_presentation_5.py
    uc_presentation.py
    uc_presentation_3.py
    web_scraping_on_gha.py
  tour_examples/  (11 files)
    ReadMe.md
    bootstrap_google_tour.py
    bootstrap_xkcd_tour.py
    driverjs_maps_tour.py
    google_tour.py
    hopscotch_google_tour.py
    introjs_google_tour.py
    maps_introjs_tour.py
    octocat_tour.py
    shepherd_google_tour.py
    xkcd_tour.py
  translations/  (12 files)
    ReadMe.md
    chinese_test_1.py
    dutch_test_1.py
    english_test_1.py
    french_test_1.py
    italian_test_1.py
    japanese_test_1.py
    korean_test_1.py
    portuguese_test_1.py
    pytest.ini
    russian_test_1.py
    spanish_test_1.py
  unit_tests/  (3 files)
    ReadMe.md
    pytest.ini
    verify_framework.py
  visual_testing/  (10 files)
    case_plans/  (4 files)
      … 4 files under this directory
    ReadMe.md
    __init__.py
    layout_test.py
    python_home_test.py
    test_layout_fail.py
    xkcd_visual_test.py
  ReadMe.md
  __init__.py
  basic_test.py
  case_summary.md
  coffee_cart_tests.py
  custom_settings.py
  edge_test.py
  example_config.cfg
  github_test.py
  gui_test_runner.py
  hack_the_planet.py
  handle_alert_test.py
  iframe_tests.py
  locale_code_test.py
  multiple_cdp_drivers.py
  my_first_test.py
  nth_child_test.py
  old_wordle_script.py
  parameterized_test.py
  performance_test.py
  proxy_test.py
  pytest.ini
  rate_limiting_test.py
  raw_ahrefs.py
  … 120 more files
help_docs/  (32 files)
  ReadMe.md
  behave_gui.md
  case_plans.md
  cdp_mode_methods.md
  commander.md
  customizing_test_runs.md
  demo_mode.md
  desired_capabilities.md
  features_list.md
  handling_iframes.md
  happy_customers.md
  hidden_files_info.md
  how_it_works.md
  html_inspector.md
  install.md
  install_python_pip_git.md
  js_package_manager.md
  locale_codes.md
  method_summary.md
  mobile_testing.md
  mysql_installation.md
  recorder_mode.md
  shadow_dom.md
  syntax_formats.md
  … 8 more files
integrations/  (42 files)
  azure/  (2 files)
    azure_pipelines/  (1 files)
      … 1 files under this directory
    jenkins/  (1 files)
      … 1 files under this directory
  behave/  (14 files)
    features/  (12 files)
      … 12 files under this directory
    ReadMe.md
    behave.ini
  brython/  (4 files)
    ReadMe.md
    index.html
    index.py
    library.html
  docker/  (3 files)
    ReadMe.md
    docker-entrypoint.sh
    run_docker_test_in_chrome.sh
  github/  (3 files)
    workflows/  (2 files)
      … 2 files under this directory
    ReadMe.md
  google_cloud/  (1 files)
    ReadMe.md
  linux/  (5 files)
    Linuxfile.sh
    ReadMe.md
    Xvfb_launcher.sh
    jenkins_permissions.sh
    tomcat_permissions.sh
  node_js/  (8 files)
    ReadMe.md
    __init__.py
    index.html
    my_first_test.py
    npm-shrinkwrap.json
    package.json
    server.js
    test_demo_site.py
  selenium_grid/  (1 files)
    ReadMe.md
  __init__.py
mcp_servers/  (7 files)
  .mcp.json
  README.md
  __init__.py
  pyproject.toml
  requirements.txt
  server.py
  setup.cfg
mkdocs_build/  (10 files)
  img/  (5 files)
    social/  (5 files)
      … 5 files under this directory
  ReadMe.txt
  docs_instructions.txt
  index.txt
  prepare.py
  requirements.txt
sbase/  (4 files)
  ReadMe.txt
  __init__.py
  __main__.py
  steps.py
seleniumbase/  (144 files)
  behave/  (4 files)
    __init__.py
    behave_helper.py
    behave_sb.py
    steps.py
  common/  (7 files)
    ReadMe.md
    __init__.py
    decorators.py
    encryption.py
    exceptions.py
    obfuscate.py
    unobfuscate.py
  config/  (4 files)
    __init__.py
    ad_block_list.py
    proxy_list.py
    settings.py
  console_scripts/  (17 files)
    ReadMe.md
    __init__.py
    logo_helper.py
    rich_helper.py
    run.py
    sb_behave_gui.py
    sb_caseplans.py
    sb_commander.py
    sb_install.py
    sb_mkchart.py
    sb_mkdir.py
    sb_mkfile.py
    sb_mkpres.py
    sb_mkrec.py
    sb_objectify.py
    sb_print.py
    sb_recorder.py
  core/  (24 files)
    __init__.py
    application_manager.py
    capabilities_parser.py
    colored_traceback.py
    create_db_tables.sql
    detect_b_ver.py
    download_helper.py
    encoded_images.py
    jqc_helper.py
    log_helper.py
    mysql.py
    nest_asyncio.py
    proxy_helper.py
    recorder_helper.py
    report_helper.py
    s3_manager.py
    sb_cdp.py
    sb_driver.py
    session_helper.py
    settings_parser.py
    style_sheet.py
    testcase_manager.py
    tour_helper.py
    visual_helper.py
  drivers/  (8 files)
    brave_drivers/  (1 files)
      … 1 files under this directory
    cft_drivers/  (1 files)
      … 1 files under this directory
    chromium_drivers/  (1 files)
      … 1 files under this directory
    chs_drivers/  (1 files)
      … 1 files under this directory
    comet_drivers/  (1 files)
      … 1 files under this directory
    opera_drivers/  (1 files)
      … 1 files under this directory
    ReadMe.md
    __init__.py
  extensions/  (2 files)
    ReadMe.md
    __init__.py
  fixtures/  (11 files)
    __init__.py
    constants.py
    css_to_xpath.py
    errors.py
    js_utils.py
    page_actions.py
    page_utils.py
    shared_utils.py
    unittest_helper.py
    words.py
    xpath_to_css.py
  js_code/  (4 files)
    __init__.py
    active_css_js.py
    live_js.py
    recorder_js.py
  masterqa/  (3 files)
    ReadMe.md
    __init__.py
    master_qa.py
  plugins/  (11 files)
    __init__.py
    base_plugin.py
    basic_test_info.py
    db_reporting_plugin.py
    driver_manager.py
    page_source.py
    pytest_plugin.py
    s3_logging_plugin.py
    sb_manager.py
    screen_shots.py
    selenium_plugin.py
  resources/  (2 files)
    ReadMe.md
    __init__.py
  translate/  (12 files)
    __init__.py
    chinese.py
    dutch.py
    french.py
    italian.py
    japanese.py
    korean.py
    master_dict.py
    portuguese.py
    russian.py
    spanish.py
    translator.py
  undetected/  (15 files)
    cdp_driver/  (8 files)
      … 8 files under this directory
    __init__.py
    cdp.py
    dprocess.py
    options.py
    patcher.py
    reactor.py
    webelement.py
  utilities/  (16 files)
    selenium_grid/  (12 files)
      … 12 files under this directory
    selenium_ide/  (3 files)
      … 3 files under this directory
    __init__.py
  ReadMe.md
  __init__.py
  __main__.py
  __version__.py
.dockerignore
.gitignore
.mcp.json
AGENTS.md
CHANGELOG.md
CNAME
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
MANIFEST.in
README.md
SECURITY.md
SKILLS.md
_config.yml
azure-pipelines.yml
glama.json
install.sh
mkdocs.yml
pyproject.toml
pytest.ini
requirements.txt
server.json
setup.cfg
… 4 more files
```

## Entry points

- [mcp_servers/server.py](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/mcp_servers/server.py)
- [sbase/__main__.py:14](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/sbase/__main__.py#L14)
- [seleniumbase/__main__.py:14](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/seleniumbase/__main__.py#L14)
- [seleniumbase/common/obfuscate.py:39](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/seleniumbase/common/obfuscate.py#L39)
- [seleniumbase/common/unobfuscate.py:30](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/seleniumbase/common/unobfuscate.py#L30)
- [seleniumbase/console_scripts/run.py](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/seleniumbase/console_scripts/run.py)
- [seleniumbase/console_scripts/run.py](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/seleniumbase/console_scripts/run.py)
- [seleniumbase/console_scripts/sb_behave_gui.py:483](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/seleniumbase/console_scripts/sb_behave_gui.py#L483)
- [seleniumbase/console_scripts/sb_caseplans.py:546](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/seleniumbase/console_scripts/sb_caseplans.py#L546)
- [seleniumbase/console_scripts/sb_commander.py:466](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/seleniumbase/console_scripts/sb_commander.py#L466)
- [seleniumbase/console_scripts/sb_install.py:1513](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/seleniumbase/console_scripts/sb_install.py#L1513)
- [seleniumbase/console_scripts/sb_mkchart.py:273](https://github.com/seleniumbase/SeleniumBase/blob/e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5/seleniumbase/console_scripts/sb_mkchart.py#L273)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 26 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. Observed top-level functions: find_chrome_executable, get_default_preference… |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 23 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _cleanup_browser, _get_sb, assert_condition, check_if_condition, click_element, close_b… |
| External integrations | external | Observed | Groups 17 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: add_item_to_cart, assert_element, assert_exact_text, assert_text, assert_text_in_selector… |
| mcp_servers package | library | Observed | Groups 1 file(s) under mcp_servers package (observed from repository paths and static analysis). |
| mkdocs_build package | library | Observed | Groups 1 file(s) under mkdocs_build package (observed from repository paths and static analysis). Observed top-level functions: main, normalize_path, process_file, read_file. |
| sbase package | library | Observed | Groups 2 file(s) under sbase package (observed from repository paths and static analysis). Observed top-level functions: accept_alert, activate_cdp_mode, activate_demo_mode, add_text, assert_attribute, assert_attribute_… |
| seleniumbase package | library | Observed | Groups 80 file(s) under seleniumbase package (observed from repository paths and static analysis). Observed top-level classes: Backbone, Base, BasicTestInfo, BlockedTest, BootstrapTour, Browser. Observed top-level funct… |
| Service / domain layer | service | Observed | Groups 23 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: ApplicationManager, CDPMethods, Chrome, ChromeType, Colorizer, DatabaseManager. Observed t… |
| Tests | test | Observed | Groups 120 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AngularMaterialInputTests, AngularMaterialPaginatorTests, AppleTests, BrokenLinkTests, CDPNetworkBlockingT… |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/Workflows.md` (ci)
- `.github/workflows/pages.yml` (ci)
- `.github/workflows/publish-mcp.yml` (ci)
- `.github/workflows/python-nightly-mac.yml` (ci)
- `.github/workflows/python-nightly-ubuntu.yml` (ci)
- `.github/workflows/python-nightly-windows.yml` (ci)
- `.github/workflows/python-package.yml` (ci)
- `.mcp.json` (config)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `_config.yml` (config)
- `azure-pipelines.yml` (ci)
- `examples/behave_bdd/behave.ini` (config)
- `examples/behave_bdd/features/behave.ini` (config)
- `examples/capabilities/sample_cap_file_BS.yml` (config)
- `examples/example_config.cfg` (config)
- `examples/master_qa/pytest.ini` (config)
- `examples/migration/raw_selenium/pytest.ini` (config)
- `examples/pytest.ini` (config)
- `examples/setup.cfg` (manifest)
- `examples/translations/pytest.ini` (config)
- `examples/unit_tests/pytest.ini` (config)
- `glama.json` (config)
- `integrations/behave/behave.ini` (config)
- `integrations/behave/features/behave.ini` (config)
- `integrations/node_js/npm-shrinkwrap.json` (config)
- `integrations/node_js/package.json` (manifest)
- `mcp_servers/.mcp.json` (config)
- `mcp_servers/pyproject.toml` (manifest)
- `mcp_servers/requirements.txt` (manifest)
- `mcp_servers/setup.cfg` (manifest)
- `mkdocs.yml` (config)
- `mkdocs_build/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `pytest.ini` (config)
- `requirements.txt` (manifest)
- `server.json` (config)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `examples` — 496 analysed file(s)
- `seleniumbase` — 144 analysed file(s)
- `integrations` — 42 analysed file(s)
- `help_docs` — 32 analysed file(s)
- `(root files)` — 28 analysed file(s)
- `mkdocs_build` — 10 analysed file(s)
- `.github` — 8 analysed file(s)
- `mcp_servers` — 7 analysed file(s)
- `sbase` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e51d66c1b343ec76dbbce7c73bdc5ad8fdce84e5` is the revision these paths and observations refer to.
