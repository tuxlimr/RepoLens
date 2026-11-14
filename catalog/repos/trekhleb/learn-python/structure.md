# Project structure: trekhleb/learn-python

**Analysed commit:** `5e4fad5903ce5a76cc1f90838d69a220968e1494`

**Commit reference:** [5e4fad5903ce5a76cc1f90838d69a220968e1494](https://github.com/trekhleb/learn-python/commit/5e4fad5903ce5a76cc1f90838d69a220968e1494)

**Tree at this commit:** [trekhleb/learn-python@5e4fad5903ce](https://github.com/trekhleb/learn-python/tree/5e4fad5903ce5a76cc1f90838d69a220968e1494)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | trekhleb/learn-python |
| Description | 📚 Playground and cheatsheet for learning Python. Collection of Python scripts that are split by topics and contain code examples with explanations. |
| Stars | 18509 |
| Forks | 2996 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `5e4fad5903ce5a76cc1f90838d69a220968e1494` |
| Retrieved at | 2026-11-14T19:08:23.407582+00:00 |
| Files in this snapshot | 82 |

## Directory tree

```text
src/  (69 files)
  additions/  (2 files)
    test_generators.py
    test_pass.py
  classes/  (7 files)
    test_class_and_instance_variables.py
    test_class_definition.py
    test_class_objects.py
    test_inheritance.py
    test_instance_objects.py
    test_method_objects.py
    test_multiple_inheritance.py
  control_flow/  (6 files)
    test_break.py
    test_continue.py
    test_for.py
    test_if.py
    test_try.py
    test_while.py
  data_types/  (7 files)
    test_dictionaries.py
    test_lists.py
    test_numbers.py
    test_sets.py
    test_strings.py
    test_tuples.py
    test_type_casting.py
  exceptions/  (2 files)
    test_handle_exceptions.py
    test_raise_exceptions.py
  files/  (4 files)
    binary_file
    multi_line_file.txt
    test_file_methods.py
    test_file_reading.py
  functions/  (10 files)
    test_function_annotations.py
    test_function_arbitrary_arguments.py
    test_function_decorators.py
    test_function_default_arguments.py
    test_function_definition.py
    test_function_documentation_string.py
    test_function_keyword_arguments.py
    test_function_scopes.py
    test_function_unpacking_arguments.py
    test_lambda_expressions.py
  getting_started/  (5 files)
    python_syntax.md
    python_syntax.uk-UA.md
    test_variables.py
    what_is_python.md
    what_is_python.uk-UA.md
  modules/  (10 files)
    sound_package/  (7 files)
      … 7 files under this directory
    fibonacci_module.py
    test_modules.py
    test_packages.py
  operators/  (7 files)
    test_arithmetic.py
    test_assigment.py
    test_bitwise.py
    test_comparison.py
    test_identity.py
    test_logical.py
    test_membership.py
  standard_libraries/  (8 files)
    glob_files/  (2 files)
      … 2 files under this directory
    test_datetime.py
    test_glob.py
    test_json.py
    test_math.py
    test_re.py
    test_zlib.py
  user_input/  (1 files)
    test_input.py
.flake8
.gitignore
.travis.yml
CODE_OF_CONDUCT.md
LICENSE
README.es-ES.md
README.md
README.pt-BR.md
README.uk-UA.md
README.zh-TW.md
_config.yml
pylintrc
requirements.txt
```

## Entry points

- [src/modules/fibonacci_module.py:41](https://github.com/trekhleb/learn-python/blob/5e4fad5903ce5a76cc1f90838d69a220968e1494/src/modules/fibonacci_module.py#L41)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: fibonacci_at_position, fibonacci_smaller_than. |
| modules package | library | Observed | Groups 7 file(s) under modules package (observed from repository paths and static analysis). Observed top-level functions: aif_read, echo_function, reverse_function, wav_read. |
| Tests | test | Observed | Groups 53 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Employee, MyCounter, MyEmptyClass, Person. Observed top-level functions: breakfast, do_nothing, fibonacci_f… |

## Important files

- `.travis.yml` (ci)
- `_config.yml` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `src` — 69 analysed file(s)
- `(root files)` — 13 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5e4fad5903ce5a76cc1f90838d69a220968e1494` is the revision these paths and observations refer to.
