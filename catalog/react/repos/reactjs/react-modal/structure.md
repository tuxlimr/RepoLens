# Project structure: reactjs/react-modal

**Analysed commit:** `e66ab51b65e6c03d9dfa283f026da1c7f9f6c9b0`

**Commit reference:** [e66ab51b65e6c03d9dfa283f026da1c7f9f6c9b0](https://github.com/reactjs/react-modal/commit/e66ab51b65e6c03d9dfa283f026da1c7f9f6c9b0)

**Tree at this commit:** [reactjs/react-modal@e66ab51b65e6](https://github.com/reactjs/react-modal/tree/e66ab51b65e6c03d9dfa283f026da1c7f9f6c9b0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reactjs/react-modal |
| Description | Accessible modal dialog component for React |
| Stars | 7403 |
| Forks | 808 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e66ab51b65e6c03d9dfa283f026da1c7f9f6c9b0` |
| Retrieved at | 2026-11-14T19:13:51.560036+00:00 |
| Files in this snapshot | 83 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    test.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
.log/  (4 files)
  ti-16339.log
  ti-28128.log
  ti-39437.log
  ti-88235.log
docs/  (17 files)
  accessibility/  (1 files)
    index.md
  contributing/  (2 files)
    development.md
    index.md
  examples/  (8 files)
    css_classes.md
    global_overrides.md
    index.md
    inline_styles.md
    minimal.md
    on_request_close.md
    set_app_element.md
    should_close_on_overlay_click.md
  styles/  (3 files)
    classes.md
    index.md
    transitions.md
  testing/  (1 files)
    index.md
  index.md
  pygments.css
examples/  (17 files)
  basic/  (9 files)
    forms/  (1 files)
      … 1 files under this directory
    multiple_modals/  (1 files)
      … 1 files under this directory
    nested_modals/  (1 files)
      … 1 files under this directory
    react-router/  (1 files)
      … 1 files under this directory
    simple_usage/  (2 files)
      … 2 files under this directory
    app.css
    app.js
    index.html
  bootstrap/  (3 files)
    app.css
    app.js
    index.html
  wc/  (3 files)
    app.css
    app.js
    index.html
  base.css
  index.html
scripts/  (7 files)
  changelog.py
  defaultConfig.js
  repo_status
  version
  webpack.config.js
  webpack.dist.config.js
  webpack.test.config.js
specs/  (7 files)
  Modal.events.spec.js
  Modal.helpers.spec.js
  Modal.spec.js
  Modal.style.spec.js
  Modal.testability.spec.js
  helper.js
  index.js
src/  (11 files)
  components/  (2 files)
    Modal.js
    ModalPortal.js
  helpers/  (8 files)
    ariaAppHider.js
    bodyTrap.js
    classList.js
    focusManager.js
    portalOpenInstances.js
    safeHTMLElement.js
    scopeTab.js
    tabbable.js
  index.js
.babelrc
.eslintrc.js
.gitignore
.npmignore
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
UPGRADE_GUIDE.md
bower.json
flake.lock
flake.nix
karma.conf.js
mkdocs.yml
package.json
```

## Entry points

- [scripts/changelog.py:138](https://github.com/reactjs/react-modal/blob/e66ab51b65e6c03d9dfa283f026da1c7f9f6c9b0/scripts/changelog.py#L138)
- [specs/index.js](https://github.com/reactjs/react-modal/blob/e66ab51b65e6c03d9dfa283f026da1c7f9f6c9b0/specs/index.js)
- [src/index.js](https://github.com/reactjs/react-modal/blob/e66ab51b65e6c03d9dfa283f026da1c7f9f6c9b0/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 2 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: adjacents, generate_all, generate_current, get_all_tags, get_tags_date, git_exec. |
| helpers package | library | Observed | Groups 8 file(s) under helpers package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| specs package | library | Observed | Groups 7 file(s) under specs package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/test.yml` (ci)
- `.travis.yml` (ci)
- `bower.json` (config)
- `mkdocs.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 17 analysed file(s)
- `docs` — 17 analysed file(s)
- `examples` — 17 analysed file(s)
- `src` — 11 analysed file(s)
- `scripts` — 7 analysed file(s)
- `specs` — 7 analysed file(s)
- `.log` — 4 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e66ab51b65e6c03d9dfa283f026da1c7f9f6c9b0` is the revision these paths and observations refer to.
