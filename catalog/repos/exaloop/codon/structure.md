# Project structure: exaloop/codon

**Analysed commit:** `1aeec848835cb7fba3026c393c72eb73b2399791`

**Commit reference:** [1aeec848835cb7fba3026c393c72eb73b2399791](https://github.com/exaloop/codon/commit/1aeec848835cb7fba3026c393c72eb73b2399791)

**Tree at this commit:** [exaloop/codon@1aeec848835c](https://github.com/exaloop/codon/tree/1aeec848835cb7fba3026c393c72eb73b2399791)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | exaloop/codon |
| Description | A high-performance, zero-overhead, extensible Python compiler with built-in NumPy support |
| Stars | 16861 |
| Forks | 606 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | develop |
| Analysed commit | `1aeec848835cb7fba3026c393c72eb73b2399791` |
| Retrieved at | 2026-11-14T19:08:40.572348+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (9 files)
  ci/  (7 files)
    Dockerfile.linux-aarch64
    Dockerfile.linux-x86_64
    Dockerfile.manylinux2014-aarch64
    Dockerfile.manylinux2014-x86_64
    build-image.sh
    entrypoint.sh
    test.sh
  workflows/  (1 files)
    ci.yml
  dependabot.yml
bench/  (31 files)
  codon/  (26 files)
    binary_trees.codon
    binary_trees.cpp
    binary_trees.py
    chaos.codon
    chaos.py
    fannkuch.codon
    fannkuch.py
    float.py
    go.codon
    go.py
    mandelbrot.codon
    mandelbrot.py
    nbody.cpp
    nbody.py
    npbench.codon
    npbench_lib.codon
    primes.codon
    primes.py
    set_partition.cpp
    set_partition.py
    spectral_norm.py
    sum.py
    taq.cpp
    taq.py
    … 2 more files
  README.md
  export.py
  refresh.py
  run.sh
  test_export.py
cmake/  (9 files)
  CMakeRC.cmake
  UnicodeTables.cmake
  backtrace-config.h.in
  backtrace-supported.h.in
  codon-utf8.manifest
  config.h.in
  config.py.in
  deps.cmake
  windows-builtins.cmake
codon/  (237 files)
  app/  (1 files)
    main.cpp
  cir/  (132 files)
    analyze/  (14 files)
      … 14 files under this directory
    dsl/  (3 files)
      … 3 files under this directory
    llvm/  (15 files)
      … 15 files under this directory
    transform/  (58 files)
      … 58 files under this directory
    util/  (20 files)
      … 20 files under this directory
    attribute.cpp
    attribute.h
    base.cpp
    base.h
    cir.h
    const.cpp
    const.h
    flow.cpp
    flow.h
    func.cpp
    func.h
    instr.cpp
    instr.h
    module.cpp
    module.h
    pyextension.h
    type.cpp
    type.h
    value.cpp
    value.h
    var.cpp
    var.h
  compiler/  (15 files)
    compiler.cpp
    compiler.h
    debug_listener.cpp
    debug_listener.h
    engine.cpp
    engine.h
    error.cpp
    error.h
    jit.cpp
    jit.h
    jit_extern.h
    memory_manager.cpp
    memory_manager.h
    options.cpp
    options.h
  config/  (1 files)
    .gitignore
  dsl/  (3 files)
    dsl.h
    plugins.cpp
    plugins.h
  parser/  (69 files)
    ast/  (24 files)
      … 24 files under this directory
    peg/  (5 files)
      … 5 files under this directory
    visitors/  (30 files)
      … 30 files under this directory
    ast.h
    cache.cpp
    cache.h
    capi.cpp
    capi.h
    common.cpp
    common.h
    ctx.h
    match.cpp
    match.h
  runtime/  (9 files)
    numpy/  (3 files)
      … 3 files under this directory
    emutls.cpp
    exc.cpp
    lib.cpp
    lib.h
    re.cpp
    rtti.h
  util/  (7 files)
    common.cpp
    common.h
    jupyter.cpp
    jupyter.h
    peg2cpp.cpp
    serialize.h
    tser.h
docs/  (504 files)
  data/  (502 files)
    benchmarks/  (502 files)
      … 502 files under this directory
  .gitignore
  README.md
.clang-format
.clang-tidy
.gitattributes
.gitignore
.pre-commit-config.yaml
CMakeLists.txt
CODEOWNERS
CONTRIBUTING.md
LICENSE
README.md
```

## Entry points

- [bench/codon/go.py:453](https://github.com/exaloop/codon/blob/1aeec848835cb7fba3026c393c72eb73b2399791/bench/codon/go.py#L453)
- [bench/export.py:286](https://github.com/exaloop/codon/blob/1aeec848835cb7fba3026c393c72eb73b2399791/bench/export.py#L286)
- [bench/refresh.py:930](https://github.com/exaloop/codon/blob/1aeec848835cb7fba3026c393c72eb73b2399791/bench/refresh.py#L930)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bench package | library | Observed | Groups 18 file(s) under bench package (observed from repository paths and static analysis). Observed top-level classes: Chaosgame, GVector, Node, Point, Spline. Observed top-level functions: advance, bench_spectral_norm… |
| codon package | library | Observed | Groups 234 file(s) under codon package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Board, EmptySet, Square, UCTNode, ZobristHash. Observed top-level functions: application_o… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: SourceStorageTests. |

## Important files

- `.github/ci/Dockerfile.linux-aarch64` (container)
- `.github/ci/Dockerfile.linux-x86_64` (container)
- `.github/ci/Dockerfile.manylinux2014-aarch64` (container)
- `.github/ci/Dockerfile.manylinux2014-x86_64` (container)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.pre-commit-config.yaml` (config)

## Top-level layout

- `docs` — 504 analysed file(s)
- `codon` — 237 analysed file(s)
- `bench` — 31 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 9 analysed file(s)
- `cmake` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1aeec848835cb7fba3026c393c72eb73b2399791` is the revision these paths and observations refer to.
