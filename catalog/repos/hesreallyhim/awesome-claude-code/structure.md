# Project structure: hesreallyhim/awesome-claude-code

**Analysed commit:** `04fa0f3b9070a63d7a8a97cad6074daaf536959e`

**Commit reference:** [04fa0f3b9070a63d7a8a97cad6074daaf536959e](https://github.com/hesreallyhim/awesome-claude-code/commit/04fa0f3b9070a63d7a8a97cad6074daaf536959e)

**Tree at this commit:** [hesreallyhim/awesome-claude-code@04fa0f3b9070](https://github.com/hesreallyhim/awesome-claude-code/tree/04fa0f3b9070a63d7a8a97cad6074daaf536959e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hesreallyhim/awesome-claude-code |
| Description | A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC (no affiliation). A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top… |
| Stars | 57989 |
| Forks | 4957 |
| Licence | Other |
| Language | Python |
| Default branch | main |
| Analysed commit | `04fa0f3b9070a63d7a8a97cad6074daaf536959e` |
| Retrieved at | 2026-11-14T19:06:25.662919+00:00 |
| Files in this snapshot | 52 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (1 files)
    recommend-resource.yml
  workflows/  (5 files)
    handle-resource-submission-commands.yml
    notify-on-merge.yml
    regenerate-readme.yml
    update-repo-ticker.yml
    validate-new-issue.yml
README_ALTERNATIVES/  (2 files)
  README_AWESOME.md
  README_CLASSIC.md
assets/  (3 files)
  recently-added-light.svg
  recently-added.svg
  repo-ticker.svg
data/  (2 files)
  repo-ticker-previous.csv
  repo-ticker.csv
resources/  (11 files)
  __init__.py
  add_resource.py
  awesome-list-entry-formatter.py
  categories.py
  create_resource_pr.py
  ids.py
  move_resource.py
  parse_issue_form.py
  resource_utils.py
  submit_resource_issue.py
  update_resource.py
scripts/  (5 files)
  badges/  (2 files)
    __init__.py
    badge_notification.py
  __init__.py
  manage_categories.py
  sync_issue_form.py
templates/  (1 files)
  README.template.md
tests/  (6 files)
  test_badge_notification.py
  test_fetch_repo_ticker_data.py
  test_generate.py
  test_generate_ticker_svg.py
  test_manage_categories.py
  test_resources.py
ticker/  (4 files)
  fetch_repo_ticker_data.py
  generate_recently_added_svg.py
  generate_ticker_svg.py
  ticker_filters.py
.gitignore
.pre-commit-config.yaml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
Makefile
SECURITY.md
THE_RESOURCES_TABLE_NEW.csv
config.yaml
generate_readme.py
requirements-dev.txt
requirements.txt
```

## Entry points

- [generate_readme.py:273](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/generate_readme.py#L273)
- [resources/add_resource.py:130](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/resources/add_resource.py#L130)
- [resources/create_resource_pr.py:143](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/resources/create_resource_pr.py#L143)
- [resources/move_resource.py:120](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/resources/move_resource.py#L120)
- [resources/parse_issue_form.py:152](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/resources/parse_issue_form.py#L152)
- [resources/submit_resource_issue.py:169](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/resources/submit_resource_issue.py#L169)
- [resources/update_resource.py:133](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/resources/update_resource.py#L133)
- [scripts/badges/badge_notification.py:156](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/scripts/badges/badge_notification.py#L156)
- [scripts/manage_categories.py:628](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/scripts/manage_categories.py#L628)
- [scripts/sync_issue_form.py:61](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/scripts/sync_issue_form.py#L61)
- [ticker/fetch_repo_ticker_data.py:215](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/ticker/fetch_repo_ticker_data.py#L215)
- [ticker/generate_recently_added_svg.py:205](https://github.com/hesreallyhim/awesome-claude-code/blob/04fa0f3b9070a63d7a8a97cad6074daaf536959e/ticker/generate_recently_added_svg.py#L205)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ConfigEditError. Observed top-level functions: _apply, _block_end, _build_parser, _catego… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| resources package | library | Observed | Groups 5 file(s) under resources package (observed from repository paths and static analysis). Observed top-level functions: _author_md, _categories, _md_text, _value_map, append_to_csv, category_names. |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: DummyResponse. Observed top-level functions: _load, _load_formatter, _move_csv, _names, _subs, _update_csv. |
| ticker package | library | Observed | Groups 1 file(s) under ticker package (observed from repository paths and static analysis). Observed top-level functions: filter_repos, keep_repo. |

## Important files

- `.github/ISSUE_TEMPLATE/recommend-resource.yml` (config)
- `.github/workflows/handle-resource-submission-commands.yml` (ci)
- `.github/workflows/notify-on-merge.yml` (ci)
- `.github/workflows/regenerate-readme.yml` (ci)
- `.github/workflows/update-repo-ticker.yml` (ci)
- `.github/workflows/validate-new-issue.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `config.yaml` (config)
- `requirements-dev.txt` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 12 analysed file(s)
- `resources` — 11 analysed file(s)
- `.github` — 6 analysed file(s)
- `tests` — 6 analysed file(s)
- `scripts` — 5 analysed file(s)
- `ticker` — 4 analysed file(s)
- `assets` — 3 analysed file(s)
- `README_ALTERNATIVES` — 2 analysed file(s)
- `data` — 2 analysed file(s)
- `templates` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `04fa0f3b9070a63d7a8a97cad6074daaf536959e` is the revision these paths and observations refer to.
