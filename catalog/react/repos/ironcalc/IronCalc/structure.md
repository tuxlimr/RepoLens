# Project structure: ironcalc/IronCalc

**Analysed commit:** `53c00566515e3d67bf9b7bd2205db16771ea66e8`

**Commit reference:** [53c00566515e3d67bf9b7bd2205db16771ea66e8](https://github.com/ironcalc/IronCalc/commit/53c00566515e3d67bf9b7bd2205db16771ea66e8)

**Tree at this commit:** [ironcalc/IronCalc@53c00566515e](https://github.com/ironcalc/IronCalc/tree/53c00566515e3d67bf9b7bd2205db16771ea66e8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ironcalc/IronCalc |
| Description | Main engine of the IronCalc ecosystem |
| Stars | 4273 |
| Forks | 240 |
| Licence | Apache-2.0 |
| Language | Rust |
| Default branch | main |
| Analysed commit | `53c00566515e3d67bf9b7bd2205db16771ea66e8` |
| Retrieved at | 2026-11-14T19:14:51.000421+00:00 |
| Files in this snapshot | 796 |

## Directory tree

```text
.github/  (7 files)
  workflows/  (6 files)
    build-test.yaml
    docker.yml
    npm.yml
    publish-crates.yaml
    pypi.yml
    test-coverage.yaml
  FUNDING.yml
assets/  (9 files)
  docs/  (4 files)
    ironcalc-docs-logo-dark.svg
    ironcalc-docs-logo.svg
    ironcalc-logo-dark.svg
    ironcalc-logo.svg
  icon/  (1 files)
    ironcalc_icon.svg
  logo/  (4 files)
    svg/  (4 files)
      … 4 files under this directory
base/  (539 files)
  examples/  (2 files)
    formulas_and_errors.rs
    hello_world.rs
  src/  (530 files)
    expressions/  (48 files)
      … 48 files under this directory
    formatter/  (16 files)
      … 16 files under this directory
    functions/  (111 files)
      … 111 files under this directory
    language/  (1 files)
      … 1 files under this directory
    locale/  (1 files)
      … 1 files under this directory
    sheet_data/  (5 files)
      … 5 files under this directory
    test/  (303 files)
      … 303 files under this directory
    tz/  (3 files)
      … 3 files under this directory
    user_model/  (15 files)
      … 15 files under this directory
    actions.rs
    arithmetic.rs
    builtin_styles.rs
    calc_result.rs
    cast.rs
    cell.rs
    cf_types.rs
    colors.rs
    conditional_formatting.rs
    constants.rs
    cut_paste.rs
    evaluation.rs
    implicit_intersection.rs
    lib.rs
    links.rs
    merged_cells.rs
    mock_time.rs
    model.rs
    new_empty.rs
    number_format.rs
    styles.rs
    themes.rs
    types.rs
    units.rs
    … 3 more files
  .gitignore
  Cargo.toml
  LICENSE-Apache-2.0
  LICENSE-MIT
  README.md
  THIRD-PARTY-NOTICES.md
  build.rs
bindings/  (118 files)
  nodejs/  (49 files)
    .cargo/  (1 files)
      … 1 files under this directory
    __test__/  (1 files)
      … 1 files under this directory
    npm/  (28 files)
      … 28 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    .npmignore
    .yarnrc.yml
    Cargo.toml
    LICENSE-Apache-2.0
    LICENSE-MIT
    README.md
    build.rs
    index.d.ts
    index.js
    main.mjs
    package.json
    rustfmt.toml
    tsconfig.doc.json
    typedoc.json
    types.d.ts
  python/  (49 files)
    docs/  (15 files)
      … 15 files under this directory
    python/  (3 files)
      … 3 files under this directory
    src/  (4 files)
      … 4 files under this directory
    tests/  (17 files)
      … 17 files under this directory
    .gitignore
    Cargo.toml
    LICENSE-Apache-2.0.md
    LICENSE-MIT.md
    README.md
    build.rs
    build_docs.sh
    pyproject.toml
    run_examples.sh
    run_tests.sh
  wasm/  (20 files)
    .cargo/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    tests/  (4 files)
      … 4 files under this directory
    .gitignore
    Cargo.toml
    Makefile
    README.md
    README.pkg-xlsx.md
    README.pkg.md
    fix_package.py
    fix_types.py
    package.json
    test.html
    third_party_notices.py
    tsconfig.doc.json
    typedoc.json
    types.ts
docs/  (109 files)
  docs.ironcalc.com/  (109 files)
    src/  (106 files)
      … 106 files under this directory
    .gitignore
    README.md
    package.json
.dockerignore
.gitattributes
.gitignore
.readthedocs.yaml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Cargo.toml
Dockerfile
LICENSE-Apache-2.0
LICENSE-MIT
Makefile
README.md
codecov.yml
docker-compose.yml
```

## Entry points

- [bindings/wasm/fix_types.py:31](https://github.com/ironcalc/IronCalc/blob/53c00566515e3d67bf9b7bd2205db16771ea66e8/bindings/wasm/fix_types.py#L31)
- [bindings/wasm/third_party_notices.py:212](https://github.com/ironcalc/IronCalc/blob/53c00566515e3d67bf9b7bd2205db16771ea66e8/bindings/wasm/third_party_notices.py#L212)
- [bindings/nodejs/index.js](https://github.com/ironcalc/IronCalc/blob/53c00566515e3d67bf9b7bd2205db16771ea66e8/bindings/nodejs/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| base package | library | Observed | Groups 184 file(s) under base package (observed from repository paths and static analysis). |
| bindings package | library | Observed | Groups 28 file(s) under bindings package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 33 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: fix_types, license_files, linked_packages, main, normalize, package_metadata. |
| Tests | test | Observed | Groups 368 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: rm, sheet_names, test_add_and_retrieve, test_add_update_delete, test_apply_builtin_named_style, test_app… |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/workflows/build-test.yaml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/npm.yml` (ci)
- `.github/workflows/publish-crates.yaml` (ci)
- `.github/workflows/pypi.yml` (ci)
- `.github/workflows/test-coverage.yaml` (ci)
- `.readthedocs.yaml` (config)
- `Cargo.toml` (manifest)
- `Dockerfile` (container)
- `base/Cargo.toml` (manifest)
- `bindings/nodejs/.cargo/config.toml` (config)
- `bindings/nodejs/.yarnrc.yml` (config)
- `bindings/nodejs/Cargo.toml` (manifest)
- `bindings/nodejs/npm/android-arm-eabi/package.json` (manifest)
- `bindings/nodejs/npm/android-arm64/package.json` (manifest)
- `bindings/nodejs/npm/darwin-arm64/package.json` (manifest)
- `bindings/nodejs/npm/darwin-universal/package.json` (manifest)
- `bindings/nodejs/npm/darwin-x64/package.json` (manifest)
- `bindings/nodejs/npm/linux-arm-gnueabihf/package.json` (manifest)
- `bindings/nodejs/npm/linux-arm-musleabihf/package.json` (manifest)
- `bindings/nodejs/npm/linux-arm64-gnu/package.json` (manifest)
- `bindings/nodejs/npm/linux-arm64-musl/package.json` (manifest)
- `bindings/nodejs/npm/linux-riscv64-gnu/package.json` (manifest)
- `bindings/nodejs/npm/linux-x64-gnu/package.json` (manifest)
- `bindings/nodejs/npm/linux-x64-musl/package.json` (manifest)
- `bindings/nodejs/npm/win32-arm64-msvc/package.json` (manifest)
- `bindings/nodejs/npm/win32-x64-msvc/package.json` (manifest)
- `bindings/nodejs/package.json` (manifest)
- `bindings/nodejs/rustfmt.toml` (config)
- `bindings/nodejs/tsconfig.doc.json` (config)
- `bindings/nodejs/typedoc.json` (config)
- `bindings/python/Cargo.toml` (manifest)
- `bindings/python/pyproject.toml` (manifest)
- `bindings/wasm/.cargo/config.toml` (config)
- `bindings/wasm/Cargo.toml` (manifest)
- `bindings/wasm/package.json` (manifest)
- `bindings/wasm/tsconfig.doc.json` (config)
- `bindings/wasm/typedoc.json` (config)
- `codecov.yml` (config)
- `docker-compose.yml` (container)
- `docs/docs.ironcalc.com/package.json` (manifest)

## Top-level layout

- `base` — 539 analysed file(s)
- `bindings` — 118 analysed file(s)
- `docs` — 109 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `assets` — 9 analysed file(s)
- `.github` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `53c00566515e3d67bf9b7bd2205db16771ea66e8` is the revision these paths and observations refer to.
