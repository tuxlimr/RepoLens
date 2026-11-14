# Project structure: cookiecutter/cookiecutter

**Analysed commit:** `c88fbe921c97c58b65f1883ba90a0ab53cc91b34`

**Commit reference:** [c88fbe921c97c58b65f1883ba90a0ab53cc91b34](https://github.com/cookiecutter/cookiecutter/commit/c88fbe921c97c58b65f1883ba90a0ab53cc91b34)

**Tree at this commit:** [cookiecutter/cookiecutter@c88fbe921c97](https://github.com/cookiecutter/cookiecutter/tree/c88fbe921c97c58b65f1883ba90a0ab53cc91b34)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cookiecutter/cookiecutter |
| Description | A cross-platform command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, C projects. |
| Stars | 25178 |
| Forks | 2305 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `c88fbe921c97c58b65f1883ba90a0ab53cc91b34` |
| Retrieved at | 2026-11-14T19:07:32.751219+00:00 |
| Files in this snapshot | 314 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.yml
  workflows/  (2 files)
    publish.yml
    tests.yml
  ISSUE_TEMPLATE.md
  dependabot.yml
CHANGELOG/  (41 files)
  0.1.0.md
  0.2.1.md
  0.2.md
  0.3.md
  0.4.md
  0.5.md
  0.6.0.md
  0.6.1.md
  0.6.2.md
  0.6.3.md
  0.6.4.md
  0.7.0.md
  0.7.1.md
  0.7.2.md
  0.8.0.md
  0.9.0.md
  1.0.0.md
  1.1.0.md
  1.2.1.md
  1.3.0.md
  1.4.0.md
  1.5.0.md
  1.5.1.md
  1.6.0.md
  … 17 more files
cookiecutter/  (18 files)
  __init__.py
  __main__.py
  cli.py
  config.py
  environment.py
  exceptions.py
  extensions.py
  find.py
  generate.py
  hooks.py
  log.py
  main.py
  prompt.py
  replay.py
  repository.py
  utils.py
  vcs.py
  zipfile.py
docs/  (36 files)
  _templates/  (1 files)
    package.rst_t
  advanced/  (21 files)
    boolean_variables.rst
    calling_from_python.rst
    choice_variables.rst
    copy_without_render.rst
    dict_variables.rst
    directories.rst
    hooks.rst
    human_readable_prompts.rst
    index.rst
    injecting_context.rst
    jinja_env.rst
    local_extensions.rst
    nested_config_files.rst
    new_line_characters.rst
    private_variables.rst
    replay.rst
    suppressing_prompts.rst
    template_extensions.rst
    templates.rst
    templates_in_context.rst
    user_config.rst
  tutorials/  (3 files)
    index.rst
    tutorial1.rst
    tutorial2.rst
  __init__.py
  case_studies.md
  cli_options.rst
  conf.py
  cookiecutter.rst
  index.rst
  installation.rst
  overview.rst
  requirements.txt
  troubleshooting.rst
  usage.rst
logo/  (1 files)
  cookiecutter-logo.svg
tests/  (195 files)
  fake-nested-templates/  (3 files)
    fake-package/  (1 files)
      … 1 files under this directory
    fake-project/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  fake-nested-templates-old-style/  (2 files)
    fake-package/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  fake-repo/  (2 files)
    fake-project/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  fake-repo-bad/  (1 files)
    no-project-in-here.txt
  fake-repo-bad-json/  (2 files)
    {{cookiecutter.repo_name}}/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  fake-repo-dict/  (2 files)
    {{cookiecutter.project_slug}}/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  fake-repo-dir/  (2 files)
    my-dir/  (2 files)
      … 2 files under this directory
  fake-repo-pre/  (2 files)
    {{cookiecutter.repo_name}}/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  fake-repo-pre2/  (3 files)
    {%{cookiecutter.repo_name}%}/  (1 files)
      … 1 files under this directory
    cookiecutter.json
    whatever.some.thing
  fake-repo-replay/  (2 files)
    {{cookiecutter.repo_name}}/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  fake-repo-tmpl/  (2 files)
    {{cookiecutter.repo_name}}/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  fake-repo-tmpl-_cookiecutter/  (2 files)
    {{cookiecutter.repo_name}}/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  files/  (8 files)
    syntax_error.txt
    unicode.txt
    {% if cookiecutter.generate_file == 'y' %}cheese.txt{% endif %}
    {{cookiecutter.generate_file}}.txt
    {{cookiecutter.generate_file}}_crlf_newlines.txt
    {{cookiecutter.generate_file}}_lf_newlines.txt
    {{cookiecutter.jsonify_file}}.txt
    {{cookiecutter.random_string_file}}.txt
  hooks-abort-render/  (3 files)
    hooks/  (2 files)
      … 2 files under this directory
    {{cookiecutter.repo_dir}}/  (1 files)
      … 1 files under this directory
  replay/  (4 files)
    conftest.py
    test_dump.py
    test_load.py
    test_replay.py
  repository/  (7 files)
    test_abbreviation_expansion.py
    test_determine_repo_dir_clones_repo.py
    test_determine_repo_dir_finds_existing_cookiecutter.py
    test_determine_repo_dir_finds_subdirectories.py
    test_determine_repository_should_use_local_repo.py
    test_is_repo_url.py
    test_repository_has_cookiecutter_json.py
  test-config/  (8 files)
    config-expand-user.yaml
    config-expand-vars.yaml
    empty-config.yaml
    invalid-config-w-array.yaml
    invalid-config-w-multiple-docs.yaml
    invalid-config.yaml
    valid-config.yaml
    valid-partial-config.yaml
  test-extensions/  (17 files)
    custom-extension-post/  (3 files)
      … 3 files under this directory
    custom-extension-pre/  (3 files)
      … 3 files under this directory
    default/  (3 files)
      … 3 files under this directory
    hello_extension/  (2 files)
      … 2 files under this directory
    local_extension/  (4 files)
      … 4 files under this directory
    unknown/  (2 files)
      … 2 files under this directory
  test-generate-binaries/  (2 files)
    input{{cookiecutter.binary_test}}/  (2 files)
      … 2 files under this directory
  test-generate-context/  (6 files)
    choices_template.json
    invalid-syntax.json
    nested_dict.json
    nested_dict_additional.json
    non_ascii.json
    test.json
  test-generate-copy-without-render/  (7 files)
    {{cookiecutter.repo_name}}/  (7 files)
      … 7 files under this directory
  test-generate-copy-without-render-override/  (7 files)
    {{cookiecutter.repo_name}}/  (7 files)
      … 7 files under this directory
  test-generate-files/  (4 files)
    input{{cookiecutter.food}}/  (4 files)
      … 4 files under this directory
  test-generate-files-line-end/  (4 files)
    {{cookiecutter.test_name}}/  (3 files)
      … 3 files under this directory
    cookiecutter.json
  test-generate-files-nontemplated/  (1 files)
    input/  (1 files)
      … 1 files under this directory
  test-generate-files-permissions/  (2 files)
    input{{cookiecutter.permissions}}/  (2 files)
      … 2 files under this directory
  test-output-folder/  (4 files)
    {{cookiecutter.test_name}}/  (3 files)
      … 3 files under this directory
    cookiecutter.json
  test-pyhooks/  (5 files)
    hooks/  (3 files)
      … 3 files under this directory
    input{{cookiecutter.pyhooks}}/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  test-pyshellhooks/  (7 files)
    hooks/  (5 files)
      … 5 files under this directory
    input{{pyshellhooks}}/  (1 files)
      … 1 files under this directory
    cookiecutter.json
  test-replay/  (3 files)
    cookiedozer_load.json
    invalid_replay.json
    valid_replay.json
  test-shellhooks/  (3 files)
    hooks/  (2 files)
      … 2 files under this directory
    input{{cookiecutter.shellhooks}}/  (1 files)
      … 1 files under this directory
  test-shellhooks-empty/  (2 files)
    hooks/  (1 files)
      … 1 files under this directory
    input{{cookiecutter.shellhooks}}/  (1 files)
      … 1 files under this directory
  test-shellhooks-win/  (3 files)
    hooks/  (2 files)
      … 2 files under this directory
    input{{cookiecutter.shellhooks}}/  (1 files)
      … 1 files under this directory
  test-templates/  (16 files)
    extends/  (5 files)
      … 5 files under this directory
    include/  (4 files)
      … 4 files under this directory
    no-templates/  (2 files)
      … 2 files under this directory
    super/  (5 files)
      … 5 files under this directory
  undefined-variable/  (5 files)
    dir-name/  (2 files)
      … 2 files under this directory
    file-content/  (1 files)
      … 1 files under this directory
    file-name/  (2 files)
      … 2 files under this directory
  vcs/  (3 files)
    test_clone.py
    test_identify_repo.py
    test_is_vcs_installed.py
  zipfile/  (1 files)
    test_unzip.py
  __init__.py
  conftest.py
  test_abort_generate_on_hook_error.py
  test_cli.py
  test_cookiecutter_invocation.py
  test_cookiecutter_local_no_input.py
  test_cookiecutter_local_with_input.py
  test_cookiecutter_nested_templates.py
  test_custom_extensions_in_hooks.py
  test_default_extensions.py
  test_environment.py
  test_exceptions.py
  test_find.py
  test_generate_context.py
  test_generate_copy_without_render.py
  test_generate_copy_without_render_override.py
  test_generate_file.py
  test_generate_files.py
  test_generate_hooks.py
  test_get_config.py
  test_get_user_config.py
  test_hooks.py
  test_log.py
  test_main.py
  … 14 more files
.bandit
.gitattributes
.gitignore
.pre-commit-config.yaml.old
.readthedocs.yaml
.safety-policy.yml
AUTHORS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
Makefile
README.md
SECURITY.md
__main__.py
codecov.yml
justfile
pyproject.toml
```

## Entry points

- [__main__.py:5](https://github.com/cookiecutter/cookiecutter/blob/c88fbe921c97c58b65f1883ba90a0ab53cc91b34/__main__.py#L5)
- [cookiecutter/__main__.py](https://github.com/cookiecutter/cookiecutter/blob/c88fbe921c97c58b65f1883ba90a0ab53cc91b34/cookiecutter/__main__.py)
- [cookiecutter/cli.py:171](https://github.com/cookiecutter/cookiecutter/blob/c88fbe921c97c58b65f1883ba90a0ab53cc91b34/cookiecutter/cli.py#L171)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: _expand_path, get_config, get_user_config, merge_configs. |
| cookiecutter package | library | Observed | Groups 14 file(s) under cookiecutter package (observed from repository paths and static analysis). Observed top-level classes: ConfigDoesNotExistException, ContextDecodingException, CookiecutterException, EmptyDirNameEx… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: _patch_import_path_for_repo. Observed top-level functions: cookiecutter, list_installed_te… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 195 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FoobarExtension, HelloExtension, TestExternalHooks, TestFindHooks, TestPrompt, TestPromptChoiceForConfig.… |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.readthedocs.yaml` (config)
- `.safety-policy.yml` (config)
- `MANIFEST.in` (manifest)
- `codecov.yml` (config)
- `docs/requirements.txt` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 195 analysed file(s)
- `CHANGELOG` — 41 analysed file(s)
- `docs` — 36 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `cookiecutter` — 18 analysed file(s)
- `.github` — 5 analysed file(s)
- `logo` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File tests/hooks-abort-render/hooks/post_gen_project.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File tests/hooks-abort-render/hooks/pre_gen_project.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c88fbe921c97c58b65f1883ba90a0ab53cc91b34` is the revision these paths and observations refer to.
