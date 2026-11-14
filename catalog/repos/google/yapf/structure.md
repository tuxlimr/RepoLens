# Project structure: google/yapf

**Analysed commit:** `12005095296072751e3e4c1f33a047d41b0ce18d`

**Commit reference:** [12005095296072751e3e4c1f33a047d41b0ce18d](https://github.com/google/yapf/commit/12005095296072751e3e4c1f33a047d41b0ce18d)

**Tree at this commit:** [google/yapf@120050952960](https://github.com/google/yapf/tree/12005095296072751e3e4c1f33a047d41b0ce18d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google/yapf |
| Description | A formatter for Python files |
| Stars | 13985 |
| Forks | 913 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `12005095296072751e3e4c1f33a047d41b0ce18d` |
| Retrieved at | 2026-11-14T19:09:35.898979+00:00 |
| Files in this snapshot | 112 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (3 files)
    ci.yml
    pre-commit-autoupdate.yml
    pre-commit.yml
  dependabot.yml
.vscode/  (2 files)
  extensions.json
  settings.default.json
plugins/  (4 files)
  vim/  (2 files)
    autoload/  (1 files)
      … 1 files under this directory
    plugin/  (1 files)
      … 1 files under this directory
  README.md
  pre-commit.sh
third_party/  (24 files)
  yapf_third_party/  (23 files)
    _ylib2to3/  (19 files)
      … 19 files under this directory
    yapf_diff/  (3 files)
      … 3 files under this directory
    __init__.py
  __init__.py
yapf/  (31 files)
  pyparser/  (5 files)
    __init__.py
    pyparser.py
    pyparser_utils.py
    pyparser_visitor.py.tmpl
    split_penalty_visitor.py
  pytree/  (9 files)
    __init__.py
    blank_line_calculator.py
    comment_splicer.py
    continuation_splicer.py
    pytree_unwrapper.py
    pytree_utils.py
    pytree_visitor.py
    split_penalty.py
    subtype_assigner.py
  yapflib/  (14 files)
    __init__.py
    errors.py
    file_resources.py
    format_decision_state.py
    format_token.py
    identify_container.py
    line_joiner.py
    logical_line.py
    object_state.py
    reformatter.py
    split_penalty.py
    style.py
    subtypes.py
    yapf_api.py
  __init__.py
  __main__.py
  _version.py
yapftests/  (24 files)
  __init__.py
  blank_line_calculator_test.py
  comment_splicer_test.py
  file_resources_test.py
  format_decision_state_test.py
  format_token_test.py
  line_joiner_test.py
  logical_line_test.py
  main_test.py
  pytree_unwrapper_test.py
  pytree_utils_test.py
  pytree_visitor_test.py
  reformatter_basic_test.py
  reformatter_buganizer_test.py
  reformatter_facebook_test.py
  reformatter_pep8_test.py
  reformatter_python3_test.py
  reformatter_style_config_test.py
  split_penalty_test.py
  style_test.py
  subtype_assigner_test.py
  utils.py
  yapf_test.py
  yapf_test_helper.py
.coveragerc
.editorconfig
.flake8
.gitattributes
.gitignore
.isort.cfg
.pre-commit-config.yaml
.pre-commit-hooks.yaml
.python-version
.style.yapf
.vimrc
AUTHORS
CHANGELOG.md
CONTRIBUTING.md
CONTRIBUTORS
EDITOR SUPPORT.md
HACKING.md
LICENSE
MANIFEST.in
README.md
pylintrc
pyproject.toml
tox.ini
```

## Entry points

- [third_party/yapf_third_party/_ylib2to3/pgen2/driver.py:295](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/third_party/yapf_third_party/_ylib2to3/pgen2/driver.py#L295)
- [third_party/yapf_third_party/_ylib2to3/pgen2/literals.py:63](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/third_party/yapf_third_party/_ylib2to3/pgen2/literals.py#L63)
- [third_party/yapf_third_party/_ylib2to3/pgen2/tokenize.py:606](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/third_party/yapf_third_party/_ylib2to3/pgen2/tokenize.py#L606)
- [third_party/yapf_third_party/yapf_diff/yapf_diff.py:139](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/third_party/yapf_third_party/yapf_diff/yapf_diff.py#L139)
- [yapf/__init__.py](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/yapf/__init__.py)
- [yapftests/blank_line_calculator_test.py:421](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/yapftests/blank_line_calculator_test.py#L421)
- [yapftests/comment_splicer_test.py:335](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/yapftests/comment_splicer_test.py#L335)
- [yapftests/file_resources_test.py:551](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/yapftests/file_resources_test.py#L551)
- [yapftests/format_decision_state_test.py:144](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/yapftests/format_decision_state_test.py#L144)
- [yapftests/format_token_test.py:95](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/yapftests/format_token_test.py#L95)
- [yapftests/line_joiner_test.py:81](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/yapftests/line_joiner_test.py#L81)
- [yapftests/logical_line_test.py:92](https://github.com/google/yapf/blob/12005095296072751e3e4c1f33a047d41b0ce18d/yapftests/logical_line_test.py#L92)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Driver, ReleaseRange, StopTokenizing, TokenError, TokenProxy, Untokenizer. Observed top-le… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: FormatAST, FormatCode, FormatFile, FormatTree, ReadFile, _DisableYAPF. |
| plugins package | library | Observed | Groups 1 file(s) under plugins package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 21 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AnnotationsTest, BadInputTest, BasicBlankLineCalculatorTest, BasicReformatterTest, BufferedByteStream, Buga… |
| third_party package | library | Observed | Groups 15 file(s) under third_party package (observed from repository paths and static analysis). Observed top-level classes: Base, BaseFix, BasePattern, ConditionalFix, Converter, DFAState. Observed top-level functions… |
| yapf package | library | Observed | Groups 27 file(s) under yapf package (observed from repository paths and static analysis). Observed top-level classes: Annotation, ComprehensionState, FormatDecisionState, FormatToken, LogicalLine, Parameter. Observed t… |
| yapftests package | library | Observed | Groups 3 file(s) under yapftests package (observed from repository paths and static analysis). Observed top-level classes: YAPFTest. Observed top-level functions: NamedTempFile, ParseAndUnwrap, TempFileContents, stdout_… |

## Important files

- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/pre-commit-autoupdate.yml` (ci)
- `.github/workflows/pre-commit.yml` (ci)
- `.isort.cfg` (config)
- `.pre-commit-config.yaml` (config)
- `.pre-commit-hooks.yaml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.default.json` (config)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)
- `tox.ini` (config)

## Top-level layout

- `yapf` — 31 analysed file(s)
- `third_party` — 24 analysed file(s)
- `yapftests` — 24 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `.github` — 4 analysed file(s)
- `plugins` — 4 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `12005095296072751e3e4c1f33a047d41b0ce18d` is the revision these paths and observations refer to.
