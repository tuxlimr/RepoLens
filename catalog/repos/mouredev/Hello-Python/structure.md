# Project structure: mouredev/Hello-Python

**Analysed commit:** `55e1bb457840762b6589ab50a66e605a2cea6457`

**Commit reference:** [55e1bb457840762b6589ab50a66e605a2cea6457](https://github.com/mouredev/Hello-Python/commit/55e1bb457840762b6589ab50a66e605a2cea6457)

**Tree at this commit:** [mouredev/Hello-Python@55e1bb457840](https://github.com/mouredev/Hello-Python/tree/55e1bb457840762b6589ab50a66e605a2cea6457)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mouredev/Hello-Python |
| Description | Curso para aprender el lenguaje de programación Python desde cero y para principiantes. 100 clases, 44 horas en vídeo, código, proyectos y grupo de chat. Fundamentos, frontend, backend, testing, IA... |
| Stars | 38045 |
| Forks | 2352 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `55e1bb457840762b6589ab50a66e605a2cea6457` |
| Retrieved at | 2026-11-14T19:06:47.434197+00:00 |
| Files in this snapshot | 44 |

## Directory tree

```text
Backend/  (12 files)
  FastAPI/  (11 files)
    db/  (3 files)
      … 3 files under this directory
    routers/  (5 files)
      … 5 files under this directory
    main.py
    requirements.txt
    vercel.json
  type_hints.py
Basic/  (15 files)
  00_helloworld.py
  01_variables.py
  02_operators.py
  03_strings.py
  04_lists.py
  05_tuples.py
  06_sets.py
  07_dicts.py
  08_conditionals.py
  09_loops.py
  10_functions.py
  11_classes.py
  12_exceptions.py
  13_modules.py
  my_module.py
Intermediate/  (14 files)
  mypackage/  (2 files)
    __init__.py
    arithmetics.py
  00_dates.py
  01_list_comprehension.py
  02_challenges.py
  03_lambdas.py
  04_higher_order_functions.py
  05_error_types.py
  06_file_handling.py
  07_regular_expressions.py
  08_python_package_manager.py
  my_file.csv
  my_file.json
  my_file.txt
.gitignore
LICENSE
README.md
```

## Entry points

- [Backend/FastAPI/main.py:14](https://github.com/mouredev/Hello-Python/blob/55e1bb457840762b6589ab50a66e605a2cea6457/Backend/FastAPI/main.py#L14)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 5 file(s) under api layer (observed from repository paths and static analysis). Observed routes: POST /login, GET /users/me, POST /login, GET /users/me, GET /. Observed top-level classes: User, UserDB. Observed t… |
| Backend package | library | Observed | Groups 1 file(s) under backend package (observed from repository paths and static analysis). |
| Basic package | library | Observed | Groups 15 file(s) under basic package (observed from repository paths and static analysis). Observed top-level classes: MyEmptyPerson, Person. Observed top-level functions: my_function, printValue, print_name, print_nam… |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: User. Observed top-level functions: user_schema, users_schema. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /, GET /url. Observed top-level functions: root,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Intermediate package | library | Observed | Groups 11 file(s) under intermediate package (observed from repository paths and static analysis). Observed top-level functions: fibonacci, filter_greater_than_ten, fizzbuzz, is_anagram, is_prime, multiply_two. |

## Important files

- `Backend/FastAPI/requirements.txt` (manifest)
- `Backend/FastAPI/vercel.json` (config)
- `Intermediate/my_file.json` (config)

## Top-level layout

- `Basic` — 15 analysed file(s)
- `Intermediate` — 14 analysed file(s)
- `Backend` — 12 analysed file(s)
- `(root files)` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `55e1bb457840762b6589ab50a66e605a2cea6457` is the revision these paths and observations refer to.
