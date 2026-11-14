# Project structure: philc/vimium

**Analysed commit:** `4046615ae4128d485fce3335fc1032e6f87c630a`

**Commit reference:** [4046615ae4128d485fce3335fc1032e6f87c630a](https://github.com/philc/vimium/commit/4046615ae4128d485fce3335fc1032e6f87c630a)

**Tree at this commit:** [philc/vimium@4046615ae412](https://github.com/philc/vimium/tree/4046615ae4128d485fce3335fc1032e6f87c630a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | philc/vimium |
| Description | The hacker's browser. |
| Stars | 27126 |
| Forks | 2630 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `4046615ae4128d485fce3335fc1032e6f87c630a` |
| Retrieved at | 2026-11-14T19:10:54.299137+00:00 |
| Files in this snapshot | 130 |

## Directory tree

```text
.githooks/  (1 files)
  pre-push
.github/  (2 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  pull_request_template.md
background_scripts/  (14 files)
  completion/  (4 files)
    completers.js
    ranking.js
    search_engines.js
    search_wrapper.js
  all_commands.js
  bg_utils.js
  commands.js
  exclusions.js
  main.js
  marks.js
  reload.js
  tab_operations.js
  tab_recency.js
  user_search_engines.js
build_scripts/  (1 files)
  write_command_listing_page.js
content_scripts/  (15 files)
  file_urls.css
  hud.js
  link_hints.js
  marks.js
  mode.js
  mode_find.js
  mode_insert.js
  mode_key_handler.js
  mode_normal.js
  mode_visual.js
  scroller.js
  ui_component.js
  vimium.css
  vimium_frontend.js
  vomnibar.js
icons/  (4 files)
  action_disabled.svg
  action_enabled.svg
  action_partial.svg
  icon.svg
lib/  (10 files)
  chrome_api_stubs.js
  dom_utils.js
  find_mode_history.js
  handler_stack.js
  keyboard_utils.js
  rect.js
  settings.js
  types.js
  url_utils.js
  utils.js
pages/  (26 files)
  action.css
  action.html
  action.js
  all_content_scripts.js
  command_listing.css
  command_listing.html
  command_listing.js
  doc.css
  doc_search_completion.html
  doc_search_completion.js
  exclusion_rules_editor.js
  help_dialog_page.css
  help_dialog_page.html
  help_dialog_page.js
  hud_page.css
  hud_page.html
  hud_page.js
  key_mappings.css
  options.css
  options.html
  options.js
  reload.html
  ui_component_messenger.js
  vomnibar_page.css
  … 2 more files
resources/  (1 files)
  tlds.txt
test_harnesses/  (9 files)
  cross_origin_iframe.html
  event_capture.html
  form.html
  has_popup_and_link_hud.html
  iframe.html
  page_with_links.html
  visibility_test.html
  vomnibar_harness.html
  vomnibar_harness.js
tests/  (36 files)
  dom_tests/  (4 files)
    dom_test_setup.js
    dom_tests.html
    dom_tests.js
    dom_utils_test.js
  e2e_tests/  (6 files)
    fixtures/  (1 files)
      … 1 files under this directory
    find_mode_test.js
    harness.js
    link_hints_test.js
    normal_mode_test.js
    vomnibar_test.js
  unit_tests/  (26 files)
    completion/  (3 files)
      … 3 files under this directory
    bg_utils_test.js
    command_listing_test.js
    commands_test.js
    doc_search_completion_test.js
    exclusion_test.js
    handler_stack_test.js
    help_dialog_test.js
    hud_page_test.js
    link_hints_test.js
    main_test.js
    marks_test.js
    options_page_test.js
    rect_test.js
    settings_test.js
    tab_operations_test.js
    tab_recency_test.js
    test_chrome_stubs.js
    test_helper.js
    ui_component_test.js
    url_utils_test.js
    user_search_engines_test.js
    utils_test.js
    vomnibar_page_test.js
.gitignore
CHANGELOG.md
CONTRIBUTING.md
CREDITS
MIT-LICENSE.txt
README.md
deno.json
deno.lock
dprint.json
make.js
manifest.json
```

## Entry points

- [background_scripts/main.js](https://github.com/philc/vimium/blob/4046615ae4128d485fce3335fc1032e6f87c630a/background_scripts/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| background_scripts package | library | Observed | Groups 14 file(s) under background_scripts package (observed from repository paths and static analysis). |
| build_scripts package | library | Observed | Groups 1 file(s) under build_scripts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| content_scripts package | library | Observed | Groups 13 file(s) under content_scripts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 10 file(s) under lib package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 10 file(s) under pages package (observed from repository paths and static analysis). |
| test_harnesses package | library | Observed | Groups 1 file(s) under test_harnesses package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 36 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `deno.json` (config)
- `dprint.json` (config)
- `manifest.json` (config)

## Top-level layout

- `tests` — 36 analysed file(s)
- `pages` — 26 analysed file(s)
- `content_scripts` — 15 analysed file(s)
- `background_scripts` — 14 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `lib` — 10 analysed file(s)
- `test_harnesses` — 9 analysed file(s)
- `icons` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `.githooks` — 1 analysed file(s)
- `build_scripts` — 1 analysed file(s)
- `resources` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4046615ae4128d485fce3335fc1032e6f87c630a` is the revision these paths and observations refer to.
