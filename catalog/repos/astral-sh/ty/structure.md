# Project structure: astral-sh/ty

**Analysed commit:** `b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551`

**Commit reference:** [b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551](https://github.com/astral-sh/ty/commit/b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551)

**Tree at this commit:** [astral-sh/ty@b4bb5b2c8a62](https://github.com/astral-sh/ty/tree/b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | astral-sh/ty |
| Description | An extremely fast Python type checker and language server, written in Rust. |
| Stars | 20088 |
| Forks | 348 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551` |
| Retrieved at | 2026-11-14T19:08:03.817572+00:00 |
| Files in this snapshot | 89 |

## Directory tree

```text
.github/  (23 files)
  ISSUE_TEMPLATE/  (3 files)
    1_bug_report.yaml
    2_question.yaml
    config.yml
  workflows/  (14 files)
    ai-policy.yml
    build-binaries.yml
    build-docker.yml
    ci.yaml
    daily_property_tests.yml
    notify-dependents.yml
    publish-docs.yml
    publish-mirror.yml
    publish-pypi.yml
    publish-versions.yml
    release-prepare.yml
    release.yml
    sign-release-binaries.yml
    sync-ty-security.yml
  PULL_REQUEST_TEMPLATE.md
  actionlint.yaml
  automations-dispatch.json
  renovate.json5
  secure-token-service.json
  zizmor.yml
agents/  (1 files)
  references/  (1 files)
    repository-threat-model.md
assets/  (1 files)
  badge/  (1 files)
    v0.json
docs/  (32 files)
  .overrides/  (2 files)
    partials/  (1 files)
      … 1 files under this directory
    main.html
  assets/  (3 files)
    logo-letter.svg
    ty-benchmark-cli-light.svg
    ty-benchmark-cli.svg
  features/  (7 files)
    third-party/  (4 files)
      … 4 files under this directory
    diagnostics.md
    language-server.md
    type-system.md
  js/  (1 files)
    extra.js
  reference/  (6 files)
    cli.md
    configuration.md
    editor-settings.md
    environment.md
    exit-codes.md
    typing-faq.md
  stylesheets/  (1 files)
    extra.css
  coming-from-mypy-or-pyright.md
  configuration.md
  editors.md
  exclusions.md
  index.md
  installation.md
  modules.md
  python-version.md
  rules.md
  scripts.md
  suppression.md
  type-checking.md
python/  (4 files)
  ty/  (4 files)
    __init__.py
    __main__.py
    _find_ty.py
    py.typed
scripts/  (9 files)
  autogenerate_files.sh
  build_ty_bolt.py
  build_ty_pgo.py
  build_ty_pgo.py.lock
  patch-dist-manifest-checksums.py
  patch-dist-manifest-checksums.py.lock
  release.sh
  transform_readme.py
  update_schemastore.py
.editorconfig
.gitattributes
.gitignore
.gitmodules
.markdownlint.yaml
.pre-commit-config.yaml
.python-version
AGENTS.md
BENCHMARKS.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
SECURITY.md
_typos.toml
dist-workspace.toml
mkdocs.yml
pyproject.toml
rust-toolchain.toml
```

## Entry points

- [python/ty/__main__.py:26](https://github.com/astral-sh/ty/blob/b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551/python/ty/__main__.py#L26)
- [scripts/build_ty_bolt.py:170](https://github.com/astral-sh/ty/blob/b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551/scripts/build_ty_bolt.py#L170)
- [scripts/build_ty_pgo.py:947](https://github.com/astral-sh/ty/blob/b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551/scripts/build_ty_pgo.py#L947)
- [scripts/patch-dist-manifest-checksums.py:61](https://github.com/astral-sh/ty/blob/b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551/scripts/patch-dist-manifest-checksums.py#L61)
- [scripts/transform_readme.py:69](https://github.com/astral-sh/ty/blob/b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551/scripts/transform_readme.py#L69)
- [scripts/update_schemastore.py:199](https://github.com/astral-sh/ty/blob/b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551/scripts/update_schemastore.py#L199)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: EcosystemProject, GitProtocol, SchemastoreRepos. Observed top-level functions: _run, appen… |
| python package | library | Observed | Groups 2 file(s) under python package (observed from repository paths and static analysis). Observed top-level classes: TyNotFound. Observed top-level functions: _join, _matching_parents, _module_path, _user_scheme, fin… |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/1_bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/2_question.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/actionlint.yaml` (config)
- `.github/automations-dispatch.json` (config)
- `.github/secure-token-service.json` (config)
- `.github/workflows/ai-policy.yml` (ci)
- `.github/workflows/build-binaries.yml` (ci)
- `.github/workflows/build-docker.yml` (ci)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/daily_property_tests.yml` (ci)
- `.github/workflows/notify-dependents.yml` (ci)
- `.github/workflows/publish-docs.yml` (ci)
- `.github/workflows/publish-mirror.yml` (ci)
- `.github/workflows/publish-pypi.yml` (ci)
- `.github/workflows/publish-versions.yml` (ci)
- `.github/workflows/release-prepare.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/sign-release-binaries.yml` (ci)
- `.github/workflows/sync-ty-security.yml` (ci)
- `.github/zizmor.yml` (config)
- `.markdownlint.yaml` (config)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `_typos.toml` (config)
- `assets/badge/v0.json` (config)
- `dist-workspace.toml` (config)
- `mkdocs.yml` (config)
- `pyproject.toml` (manifest)
- `rust-toolchain.toml` (config)

## Top-level layout

- `docs` — 32 analysed file(s)
- `.github` — 23 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `scripts` — 9 analysed file(s)
- `python` — 4 analysed file(s)
- `agents` — 1 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b4bb5b2c8a620db50ad2f4c4e7055c2a4d51a551` is the revision these paths and observations refer to.
