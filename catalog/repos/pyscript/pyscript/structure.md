# Project structure: pyscript/pyscript

**Analysed commit:** `d798c04910b21e5018813b7975ef3e9999e994c5`

**Commit reference:** [d798c04910b21e5018813b7975ef3e9999e994c5](https://github.com/pyscript/pyscript/commit/d798c04910b21e5018813b7975ef3e9999e994c5)

**Tree at this commit:** [pyscript/pyscript@d798c04910b2](https://github.com/pyscript/pyscript/tree/d798c04910b21e5018813b7975ef3e9999e994c5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pyscript/pyscript |
| Description | An open source platform for Python in the browser. https://pyscript.net Docs: https://docs.pyscript.net/ Try it: https://pyscript.com/ Community: https://discord.gg/HxvBtukrg2 |
| Stars | 18676 |
| Forks | 1466 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `d798c04910b21e5018813b7975ef3e9999e994c5` |
| Retrieved at | 2026-11-14T19:08:21.613111+00:00 |
| Files in this snapshot | 316 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.yml
    config.yml
  workflows/  (5 files)
    prepare-release.yml
    publish-release.yml
    publish-snapshot.yml
    publish-unstable.yml
    test.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  release.yml
bridge/  (8 files)
  test/  (5 files)
    remote/  (1 files)
      … 1 files under this directory
    index.html
    sys_version.py
    test.js
    test.py
  README.md
  index.js
  package.json
core/  (284 files)
  rollup/  (7 files)
    3rd-party.cjs
    build_test_index.cjs
    core.config.js
    flatted.cjs
    offline.cjs
    plugins.cjs
    stdlib.cjs
  src/  (63 files)
    3rd-party/  (12 files)
      … 12 files under this directory
    3rd-party-licenses/  (11 files)
      … 11 files under this directory
    plugins/  (9 files)
      … 9 files under this directory
    stdlib/  (15 files)
      … 15 files under this directory
    all-done.js
    config.js
    core.css
    core.js
    exceptions.js
    fetch.js
    fs.js
    hooks.js
    plugins-helper.js
    plugins.js
    service-worker.js
    stdlib.js
    storage.js
    sync.js
    types.js
    zero-redirect.js
  tests/  (170 files)
    javascript/  (47 files)
      … 47 files under this directory
    manual/  (93 files)
      … 93 files under this directory
    python/  (25 files)
      … 25 files under this directory
    README.md
    index.html
    js_tests.spec.js
    py_tests.main.spec.js
    py_tests.worker.spec.js
  types/  (34 files)
    3rd-party/  (11 files)
      … 11 files under this directory
    plugins/  (9 files)
      … 9 files under this directory
    stdlib/  (1 files)
      … 1 files under this directory
    all-done.d.ts
    config.d.ts
    core.d.ts
    exceptions.d.ts
    fetch.d.ts
    fs.d.ts
    hooks.d.ts
    plugins-helper.d.ts
    plugins.d.ts
    stdlib.d.ts
    sync.d.ts
    types.d.ts
    zero-redirect.d.ts
  .oxlintrc.json
  LICENSE
  MAINTENANCE.md
  README.md
  dev.cjs
  index.js
  jsdelivr.js
  package.json
  pyodide.sh
  tsconfig.json
public/  (2 files)
  README.md
  index.html
.gitignore
.pre-commit-config.yaml
.prettierignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
GOVERNANCE.md
LICENSE
MAINTAINERS.md
Makefile
README.md
pyproject.toml
requirements.txt
```

## Entry points

- [bridge/index.js](https://github.com/pyscript/pyscript/blob/d798c04910b21e5018813b7975ef3e9999e994c5/bridge/index.js)
- [core/index.js](https://github.com/pyscript/pyscript/blob/d798c04910b21e5018813b7975ef3e9999e994c5/core/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bridge package | library | Observed | Groups 1 file(s) under bridge package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 94 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: Classes, ContainerElement, Device, Element, ElementCollection, Event. Observed top-level f… |
| Tests | test | Observed | Groups 175 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Group. Observed top-level classes: Alien, BeatSync, Bomb, Explosion, FreqIntensity, Player. Ob… |

## Important files

- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/release.yml` (config)
- `.github/workflows/prepare-release.yml` (ci)
- `.github/workflows/publish-release.yml` (ci)
- `.github/workflows/publish-snapshot.yml` (ci)
- `.github/workflows/publish-unstable.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `bridge/package.json` (manifest)
- `core/.oxlintrc.json` (config)
- `core/package.json` (manifest)
- `core/tsconfig.json` (config)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)

## Top-level layout

- `core` — 284 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 10 analysed file(s)
- `bridge` — 8 analysed file(s)
- `public` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d798c04910b21e5018813b7975ef3e9999e994c5` is the revision these paths and observations refer to.
