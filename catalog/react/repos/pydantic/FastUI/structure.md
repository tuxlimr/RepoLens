# Project structure: pydantic/FastUI

**Analysed commit:** `b5a33bc6e5cdb5175b832568aa778d8589ade4fd`

**Commit reference:** [b5a33bc6e5cdb5175b832568aa778d8589ade4fd](https://github.com/pydantic/FastUI/commit/b5a33bc6e5cdb5175b832568aa778d8589ade4fd)

**Tree at this commit:** [pydantic/FastUI@b5a33bc6e5cd](https://github.com/pydantic/FastUI/tree/b5a33bc6e5cdb5175b832568aa778d8589ade4fd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pydantic/FastUI |
| Description | Build better UIs faster. |
| Stars | 8923 |
| Forks | 340 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `b5a33bc6e5cdb5175b832568aa778d8589ade4fd` |
| Retrieved at | 2026-11-14T19:13:36.874286+00:00 |
| Files in this snapshot | 146 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    ci.yml
  dependabot.yml
demo/  (11 files)
  README.md
  __init__.py
  auth.py
  auth_user.py
  components_list.py
  forms.py
  main.py
  shared.py
  sse.py
  tables.py
  tests.py
docs/  (7 files)
  api/  (2 files)
    python_components.md
    typescript_components.md
  assets/  (1 files)
    logo-white.svg
  extra/  (1 files)
    tweaks.css
  guide.md
  index.md
  plugins.py
requirements/  (2 files)
  docs.in
  docs.txt
src/  (109 files)
  npm-fastui/  (49 files)
    src/  (44 files)
      … 44 files under this directory
    LICENSE
    README.md
    package.json
    tsconfig.json
    typedoc.json
  npm-fastui-bootstrap/  (11 files)
    src/  (6 files)
      … 6 files under this directory
    LICENSE
    README.md
    package.json
    tsconfig.json
    typedoc.json
  npm-fastui-prebuilt/  (12 files)
    src/  (4 files)
      … 4 files under this directory
    LICENSE
    README.md
    index.html
    package.json
    tsconfig.json
    tsconfig.node.json
    typedoc.json
    vite.config.ts
  python-fastui/  (37 files)
    fastui/  (19 files)
      … 19 files under this directory
    requirements/  (7 files)
      … 7 files under this directory
    tests/  (8 files)
      … 8 files under this directory
    LICENSE
    README.md
    pyproject.toml
.eslintrc.cjs
.gitignore
.pre-commit-config.yaml
.prettierignore
LICENSE
Makefile
README.md
build-docs.sh
bump_npm.py
mkdocs.yml
package.json
pyproject.toml
tsconfig.json
typedoc.base.json
typedoc.json
```

## Entry points

- [src/python-fastui/fastui/__main__.py:31](https://github.com/pydantic/FastUI/blob/b5a33bc6e5cdb5175b832568aa778d8589ade4fd/src/python-fastui/fastui/__main__.py#L31)
- [src/python-fastui/fastui/dev.py:18](https://github.com/pydantic/FastUI/blob/b5a33bc6e5cdb5175b832568aa778d8589ade4fd/src/python-fastui/fastui/dev.py#L18)
- [bump_npm.py:57](https://github.com/pydantic/FastUI/blob/b5a33bc6e5cdb5175b832568aa778d8589ade4fd/bump_npm.py#L57)
- [demo/__init__.py:33](https://github.com/pydantic/FastUI/blob/b5a33bc6e5cdb5175b832568aa778d8589ade4fd/demo/__init__.py#L33)
- [demo/sse.py:62](https://github.com/pydantic/FastUI/blob/b5a33bc6e5cdb5175b832568aa778d8589ade4fd/demo/sse.py#L62)
- [src/npm-fastui-bootstrap/src/index.tsx](https://github.com/pydantic/FastUI/blob/b5a33bc6e5cdb5175b832568aa778d8589ade4fd/src/npm-fastui-bootstrap/src/index.tsx)
- [src/npm-fastui-prebuilt/src/App.tsx](https://github.com/pydantic/FastUI/blob/b5a33bc6e5cdb5175b832568aa778d8589ade4fd/src/npm-fastui-prebuilt/src/App.tsx)
- [src/npm-fastui-prebuilt/src/main.tsx](https://github.com/pydantic/FastUI/blob/b5a33bc6e5cdb5175b832568aa778d8589ade4fd/src/npm-fastui-prebuilt/src/main.tsx)
- [src/npm-fastui/src/index.tsx](https://github.com/pydantic/FastUI/blob/b5a33bc6e5cdb5175b832568aa778d8589ade4fd/src/npm-fastui/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). Observed routes: GET /login/{kind}, GET /login/content/{kind}, POST /login, GET /profile, POST /logout. Observed top-level classes:… |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 3 file(s) under demo package (observed from repository paths and static analysis). Observed top-level classes: CustomJsonEncoder, User. Observed top-level functions: client, demo_page, get_menu_links, test_api_ro… |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /robots.txt, GET /favicon.ico, GET /{path:path},… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| npm-fastui package | library | Observed | Groups 44 file(s) under npm-fastui package (observed from repository paths and static analysis). |
| npm-fastui-bootstrap package | library | Observed | Groups 6 file(s) under npm-fastui-bootstrap package (observed from repository paths and static analysis). |
| npm-fastui-prebuilt package | library | Observed | Groups 4 file(s) under npm-fastui-prebuilt package (observed from repository paths and static analysis). |
| python-fastui package | library | Observed | Groups 15 file(s) under python-fastui package (observed from repository paths and static analysis). Observed top-level classes: AuthError, AuthEvent, AuthException, AuthRedirect, BackEvent, BaseForm. Observed top-level… |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: FakeRequest, FixedTuple, FormMultipleFiles, FormSelectMulti… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `mkdocs.yml` (config)
- `package.json` (manifest)
- `pyproject.toml` (manifest)
- `src/npm-fastui-bootstrap/package.json` (manifest)
- `src/npm-fastui-bootstrap/tsconfig.json` (config)
- `src/npm-fastui-bootstrap/typedoc.json` (config)
- `src/npm-fastui-prebuilt/package.json` (manifest)
- `src/npm-fastui-prebuilt/tsconfig.json` (config)
- `src/npm-fastui-prebuilt/tsconfig.node.json` (config)
- `src/npm-fastui-prebuilt/typedoc.json` (config)
- `src/npm-fastui/package.json` (manifest)
- `src/npm-fastui/tsconfig.json` (config)
- `src/npm-fastui/typedoc.json` (config)
- `src/python-fastui/pyproject.toml` (manifest)
- `tsconfig.json` (config)
- `typedoc.base.json` (config)
- `typedoc.json` (config)

## Top-level layout

- `src` — 109 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `demo` — 11 analysed file(s)
- `docs` — 7 analysed file(s)
- `.github` — 2 analysed file(s)
- `requirements` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `b5a33bc6e5cdb5175b832568aa778d8589ade4fd` is the revision these paths and observations refer to.
