# Project structure: faif/python-patterns

**Analysed commit:** `0712925f8a4b3129e6e54f8ab3580c6f996aa359`

**Commit reference:** [0712925f8a4b3129e6e54f8ab3580c6f996aa359](https://github.com/faif/python-patterns/commit/0712925f8a4b3129e6e54f8ab3580c6f996aa359)

**Tree at this commit:** [faif/python-patterns@0712925f8a4b](https://github.com/faif/python-patterns/tree/0712925f8a4b3129e6e54f8ab3580c6f996aa359)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | faif/python-patterns |
| Description | A collection of design patterns/idioms in Python |
| Stars | 43102 |
| Forks | 6960 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `0712925f8a4b3129e6e54f8ab3580c6f996aa359` |
| Retrieved at | 2026-11-14T19:06:38.926711+00:00 |
| Files in this snapshot | 89 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    lint_python.yml
  dependabot.yml
config_backup/  (3 files)
  .coveragerc
  setup.cfg
  tox.ini
patterns/  (47 files)
  behavioral/  (18 files)
    __init__.py
    catalog.py
    chain_of_responsibility.py
    chaining_method.py
    command.py
    iterator.py
    iterator_alt.py
    mediator.py
    memento.py
    observer.py
    publish_subscribe.py
    registry.py
    servant.py
    specification.py
    state.py
    strategy.py
    template.py
    visitor.py
  creational/  (8 files)
    __init__.py
    abstract_factory.py
    borg.py
    builder.py
    factory.py
    lazy_evaluation.py
    pool.py
    prototype.py
  fundamental/  (2 files)
    __init__.py
    delegation_pattern.py
  other/  (5 files)
    hsm/  (2 files)
      … 2 files under this directory
    __init__.py
    blackboard.py
    graph_search.py
  structural/  (12 files)
    3-tier.py
    __init__.py
    adapter.py
    bridge.py
    composite.py
    decorator.py
    facade.py
    flyweight.py
    flyweight_with_metaclass.py
    front_controller.py
    mvc.py
    proxy.py
  __init__.py
  dependency_injection.py
tests/  (28 files)
  behavioral/  (9 files)
    test_catalog.py
    test_mediator.py
    test_memento.py
    test_observer.py
    test_publish_subscribe.py
    test_servant.py
    test_state.py
    test_strategy.py
    test_visitor.py
  creational/  (7 files)
    test_abstract_factory.py
    test_borg.py
    test_builder.py
    test_factory.py
    test_lazy.py
    test_pool.py
    test_prototype.py
  fundamental/  (1 files)
    test_delegation.py
  structural/  (8 files)
    test_adapter.py
    test_bridge.py
    test_decorator.py
    test_facade.py
    test_flyweight.py
    test_flyweight_with_metaclass.py
    test_mvc.py
    test_proxy.py
  __init__.py
  test_graph_search.py
  test_hsm.py
.codespellignore
.gitignore
.travis.yml
Makefile
Pipfile
README.md
lint.sh
pyproject.toml
pytest_local.ini
```

## Entry points

- [patterns/behavioral/catalog.py:170](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/catalog.py#L170)
- [patterns/behavioral/chain_of_responsibility.py:120](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/chain_of_responsibility.py#L120)
- [patterns/behavioral/chaining_method.py:34](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/chaining_method.py#L34)
- [patterns/behavioral/command.py:102](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/command.py#L102)
- [patterns/behavioral/iterator.py:44](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/iterator.py#L44)
- [patterns/behavioral/iterator_alt.py:59](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/iterator_alt.py#L59)
- [patterns/behavioral/mediator.py:50](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/mediator.py#L50)
- [patterns/behavioral/memento.py:143](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/memento.py#L143)
- [patterns/behavioral/observer.py:132](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/observer.py#L132)
- [patterns/behavioral/publish_subscribe.py:92](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/publish_subscribe.py#L92)
- [patterns/behavioral/registry.py:42](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/registry.py#L42)
- [patterns/behavioral/servant.py:128](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/patterns/behavioral/servant.py#L128)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 39 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: A, AbstractExpert, Action, Adapter, AmState, AndSpecification. Observed top-level functio… |
| patterns package | library | Observed | Groups 8 file(s) under patterns package (observed from repository paths and static analysis). Observed top-level classes: Active, Failed, HierachicalStateMachine, Inservice, OutOfService, Standby. |
| Tests | test | Observed | Groups 28 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestAdapter, TestBorg, TestBridge, TestClass, TestComplex, TestDispatcherFeatures. Observed top-level funct… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/lint_python.yml` (ci)
- `.travis.yml` (ci)
- `Pipfile` (manifest)
- `config_backup/setup.cfg` (manifest)
- `config_backup/tox.ini` (config)
- `pyproject.toml` (manifest)
- `pytest_local.ini` (config)

## Top-level layout

- `patterns` — 47 analysed file(s)
- `tests` — 28 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `config_backup` — 3 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0712925f8a4b3129e6e54f8ab3580c6f996aa359` is the revision these paths and observations refer to.
