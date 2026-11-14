# Project structure: nteract/archived-desktop-app

**Analysed commit:** `7516211c27bad1e5a415505b023e2221bc430d8a`

**Commit reference:** [7516211c27bad1e5a415505b023e2221bc430d8a](https://github.com/nteract/archived-desktop-app/commit/7516211c27bad1e5a415505b023e2221bc430d8a)

**Tree at this commit:** [nteract/archived-desktop-app@7516211c27ba](https://github.com/nteract/archived-desktop-app/tree/7516211c27bad1e5a415505b023e2221bc430d8a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nteract/archived-desktop-app |
| Description | The old electron based nteract notebook |
| Stars | 6238 |
| Forks | 549 |
| Licence | BSD-3-Clause |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `7516211c27bad1e5a415505b023e2221bc430d8a` |
| Retrieved at | 2026-11-14T19:14:08.385792+00:00 |
| Files in this snapshot | 755 |

## Directory tree

```text
.github/  (16 files)
  ISSUE_TEMPLATE/  (3 files)
    ---bug-report.md
    ---feature-request.md
    ---kernel---runtime-issue.md
  workflows/  (4 files)
    ci-workflow.yml
    codeql-analysis.yml
    desktop-release.yml
    npm-release.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  auto-comment.yml
  config.yml
  dependabot.yml
  deploy-component-docs.workflow
  invite-contributors.yml
  lock.yml
  stale.yml
.husky/  (3 files)
  .gitignore
  commit-msg
  pre-commit
.vscode/  (3 files)
  extensions.json
  launch.json
  tasks.json
applications/  (151 files)
  desktop/  (81 files)
    __mocks__/  (5 files)
      … 5 files under this directory
    __tests__/  (9 files)
      … 9 files under this directory
    bin/  (4 files)
      … 4 files under this directory
    src/  (51 files)
      … 51 files under this directory
    static/  (3 files)
      … 3 files under this directory
    .gitignore
    PACKAGING-NOTES.md
    README.md
    package.json
    scientists.txt
    tsconfig.json
    webpack.common.js
    webpack.dev.js
    webpack.prod.js
  jupyter-extension/  (41 files)
    jupyter-config/  (1 files)
      … 1 files under this directory
    nteract_on_jupyter/  (33 files)
      … 33 files under this directory
    .gitignore
    MANIFEST.in
    README.md
    package.json
    pyproject.toml
    requirements-dev.txt
    setup.py
  web/  (29 files)
    components/  (15 files)
      … 15 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    redux/  (1 files)
      … 1 files under this directory
    util/  (3 files)
      … 3 files under this directory
    .babelrc
    README.md
    next-env.d.ts
    next.config.js
    package.json
    tsconfig.json
changelogs/  (31 files)
  01-2021.md
  02-2021.md
  06-2020.md
  07-2020.md
  08-2020.md
  09-2020.md
  10-2020.md
  11-2020.md
  2019-12-16.md
  2019-12-23.md
  2019-12-30.md
  2020-01-06.md
  2020-01-13.md
  2020-01-20.md
  2020-01-27.md
  2020-02-03.md
  2020-02-10.md
  2020-02-17.md
  2020-02-24.md
  2020-03-02.md
  2020-03-09.md
  2020-03-16.md
  2020-03-23.md
  2020-03-30.md
  … 7 more files
docs/  (11 files)
  groups/  (6 files)
    binder-group.md
    components-group.md
    core-group.md
    editors-group.md
    jupyter-group.md
    mythic-group.md
  creating-data-visualizations-in-nteract.md
  desktop-config.md
  getting-started-with-nteract.md
  index.md
  kbd-shortcuts.md
nteract-packages/  (2 files)
  README.md
  now.json
packages/  (478 files)
  actions/  (24 files)
    __tests__/  (1 files)
      … 1 files under this directory
    docs/  (2 files)
      … 2 files under this directory
    src/  (17 files)
      … 17 files under this directory
    README.md
    mkdocs.yml
    package.json
    tsconfig.json
  commutable/  (20 files)
    __tests__/  (6 files)
      … 6 files under this directory
    docs/  (2 files)
      … 2 files under this directory
    src/  (8 files)
      … 8 files under this directory
    README.md
    mkdocs.yml
    package.json
    tsconfig.json
  connected-components/  (21 files)
    __tests__/  (7 files)
      … 7 files under this directory
    src/  (11 files)
      … 11 files under this directory
    README.md
    package.json
    tsconfig.json
  core/  (9 files)
    __mocks__/  (1 files)
      … 1 files under this directory
    docs/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    README.md
    mkdocs.yml
    package.json
    plan.md
    tsconfig.json
  editor/  (19 files)
    __tests__/  (7 files)
      … 7 files under this directory
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
    tsconfig.json
  epics/  (34 files)
    __mocks__/  (1 files)
      … 1 files under this directory
    __tests__/  (11 files)
      … 11 files under this directory
    docs/  (5 files)
      … 5 files under this directory
    src/  (13 files)
      … 13 files under this directory
    README.md
    mkdocs.yml
    package.json
    tsconfig.json
  fixtures/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
    tsconfig.json
  host-cache/  (9 files)
    src/  (6 files)
      … 6 files under this directory
    README.md
    package.json
    tsconfig.json
  messaging/  (9 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (4 files)
      … 4 files under this directory
    README.md
    package.json
    tsconfig.json
  monaco-editor/  (19 files)
    __tests__/  (4 files)
      … 4 files under this directory
    src/  (12 files)
      … 12 files under this directory
    README.md
    package.json
    tsconfig.json
  mythic-configuration/  (15 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (11 files)
      … 11 files under this directory
    README.md
    package.json
    tsconfig.json
  mythic-multiselect/  (8 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    README.md
    package.json
    tsconfig.json
  mythic-notifications/  (11 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (7 files)
      … 7 files under this directory
    README.md
    package.json
    tsconfig.json
  mythic-rtc/  (15 files)
    src/  (12 files)
      … 12 files under this directory
    README.md
    package.json
    tsconfig.json
  mythic-windowing/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    README.md
    package.json
    tsconfig.json
  myths/  (13 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
    tsconfig.json
  notebook-app-component/  (29 files)
    __tests__/  (5 files)
      … 5 files under this directory
    src/  (21 files)
      … 21 files under this directory
    README.md
    package.json
    tsconfig.json
  presentational-components/  (44 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (39 files)
      … 39 files under this directory
    README.md
    package.json
    tsconfig.json
  reducers/  (31 files)
    __tests__/  (12 files)
      … 12 files under this directory
    src/  (16 files)
      … 16 files under this directory
    README.md
    package.json
    tsconfig.json
  rx-binder/  (5 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    tsconfig.json
  rx-jupyter/  (18 files)
    __tests__/  (7 files)
      … 7 files under this directory
    src/  (8 files)
      … 8 files under this directory
    README.md
    package.json
    tsconfig.json
  selectors/  (15 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (11 files)
      … 11 files under this directory
    README.md
    package.json
    tsconfig.json
  stateful-components/  (41 files)
    __tests__/  (9 files)
      … 9 files under this directory
    docs/  (4 files)
      … 4 files under this directory
    src/  (24 files)
      … 24 files under this directory
    README.md
    mkdocs.yml
    package.json
    tsconfig.json
  styles/  (16 files)
    markdown/  (1 files)
      … 1 files under this directory
    monaco/  (1 files)
      … 1 files under this directory
    themes/  (2 files)
      … 2 files under this directory
    app.css
    cell-menu.css
    command-palette.css
    editor-overrides.css
    global-variables.css
    index.d.ts
    index.js
    package.json
    sidebar.css
    toggle-switch.css
    toolbar.css
    tsconfig.json
  types/  (31 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (27 files)
      … 27 files under this directory
    README.md
    package.json
    tsconfig.json
  webpack-configurator/  (5 files)
    README.md
    aliases.js
    index.js
    monorepo.js
    package.json
  README.md
  tsconfig.json
scripts/  (6 files)
  evaluate-tests.ipynb
  kernelspecs-diagnostics.js
  make_icons.sh
  noop-module.ts
  test-setup.ts
  test-shim.ts
styleguide/  (1 files)
  now.json
styleguide-components/  (3 files)
  README.md
  intro.md
  logo.tsx
types/  (20 files)
  jmp/  (1 files)
    index.d.ts
  jupyter-paths/  (1 files)
    index.d.ts
  kernelspecs/  (1 files)
    index.d.ts
  load-script/  (1 files)
    index.d.ts
  mathjax-electron/  (1 files)
    index.d.ts
  node/  (1 files)
    index.d.ts
  nteract__vega-embed-v2/  (1 files)
    index.d.ts
  nteract__vega-embed-v3/  (1 files)
    index.d.ts
  react-katex/  (1 files)
    index.d.ts
  react-table-hoc-fixed-columns/  (1 files)
    index.d.ts
  redux-electron-store/  (1 files)
    index.d.ts
  rehype-katex/  (1 files)
    index.d.ts
  rehype-stringify/  (1 files)
    index.d.ts
  remark-math/  (1 files)
    index.d.ts
  remark-rehype/  (1 files)
    index.d.ts
  semiotic/  (1 files)
    index.d.ts
  spawnteract/  (1 files)
    index.d.ts
  trim-trailing-lines/  (1 files)
    index.d.ts
  yargs/  (1 files)
    index.d.ts
  readme.md
.eslintignore
.eslintrc.js
.gitattributes
.gitignore
.npmignore
.pre-commit-config.yaml
.prettierignore
.prettierrc.js
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
RELEASING.md
SECURITY.md
TEST_PLAN.md
USER_GUIDE.md
babel.config.js
codecov.yml
commitlint.config.js
lerna.json
mkdocs.yml
package.json
renovate.json
… 6 more files
```

## Entry points

- [applications/jupyter-extension/nteract_on_jupyter/nteractapp.py:99](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/applications/jupyter-extension/nteract_on_jupyter/nteractapp.py#L99)
- [packages/styles/index.js](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/packages/styles/index.js)
- [packages/webpack-configurator/index.js](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/packages/webpack-configurator/index.js)
- [applications/web/pages/index.tsx](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/applications/web/pages/index.tsx)
- [packages/actions/src/index.ts](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/packages/actions/src/index.ts)
- [packages/commutable/src/index.ts](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/packages/commutable/src/index.ts)
- [packages/connected-components/src/index.tsx](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/packages/connected-components/src/index.tsx)
- [packages/core/src/index.ts](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/packages/core/src/index.ts)
- [packages/editor/src/index.tsx](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/packages/editor/src/index.tsx)
- [packages/epics/src/index.ts](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/packages/epics/src/index.ts)
- [packages/fixtures/src/index.ts](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/packages/fixtures/src/index.ts)
- [packages/host-cache/src/index.ts](https://github.com/nteract/archived-desktop-app/blob/7516211c27bad1e5a415505b023e2221bc430d8a/packages/host-cache/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| applications package | library | Observed | Groups 119 file(s) under applications package (observed from repository paths and static analysis). Observed top-level classes: Comparator, Extendlist, NAppHandler, Range, SemVer, _R. Observed top-level functions: _jupy… |
| Configuration and deployment | config | Observed | Groups 83 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: NteractConfig. |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: NteractApp. |
| packages package | library | Observed | Groups 318 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 36 file(s) under service / domain layer (observed from repository paths and static analysis). |
| styleguide-components package | library | Observed | Groups 1 file(s) under styleguide-components package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 19 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/auto-comment.yml` (config)
- `.github/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/invite-contributors.yml` (config)
- `.github/lock.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/ci-workflow.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/desktop-release.yml` (ci)
- `.github/workflows/npm-release.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/tasks.json` (config)
- `applications/desktop/package.json` (manifest)
- `applications/desktop/static/default-map.json` (config)
- `applications/desktop/tsconfig.json` (config)
- `applications/jupyter-extension/MANIFEST.in` (manifest)
- `applications/jupyter-extension/jupyter-config/jupyter_notebook_config.d/nteract_on_jupyter.json` (config)
- `applications/jupyter-extension/nteract_on_jupyter/package.json` (manifest)
- `applications/jupyter-extension/nteract_on_jupyter/tsconfig.json` (config)
- `applications/jupyter-extension/package.json` (manifest)
- `applications/jupyter-extension/pyproject.toml` (manifest)
- `applications/jupyter-extension/requirements-dev.txt` (manifest)
- `applications/jupyter-extension/setup.py` (manifest)
- `applications/web/package.json` (manifest)
- `applications/web/tsconfig.json` (config)
- `codecov.yml` (config)
- `lerna.json` (config)
- `mkdocs.yml` (config)
- `nteract-packages/now.json` (config)
- `package.json` (manifest)
- `packages/actions/mkdocs.yml` (config)
- `packages/actions/package.json` (manifest)
- `packages/actions/tsconfig.json` (config)
- `packages/commutable/mkdocs.yml` (config)
- `packages/commutable/package.json` (manifest)
- `packages/commutable/tsconfig.json` (config)
- `packages/connected-components/package.json` (manifest)
- `packages/connected-components/tsconfig.json` (config)
- `packages/core/mkdocs.yml` (config)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/editor/package.json` (manifest)
- `packages/editor/tsconfig.json` (config)
- `packages/epics/mkdocs.yml` (config)
- `packages/epics/package.json` (manifest)
- `packages/epics/tsconfig.json` (config)
- `packages/fixtures/package.json` (manifest)
- `packages/fixtures/tsconfig.json` (config)
- `packages/host-cache/package.json` (manifest)
- `packages/host-cache/tsconfig.json` (config)
- `packages/messaging/package.json` (manifest)
- `packages/messaging/tsconfig.json` (config)
- `packages/monaco-editor/package.json` (manifest)
- `packages/monaco-editor/tsconfig.json` (config)
- `packages/mythic-configuration/package.json` (manifest)
- `packages/mythic-configuration/tsconfig.json` (config)
- `packages/mythic-multiselect/package.json` (manifest)
- `packages/mythic-multiselect/tsconfig.json` (config)
- `packages/mythic-notifications/package.json` (manifest)
- `packages/mythic-notifications/tsconfig.json` (config)
- `packages/mythic-rtc/package.json` (manifest)
- `packages/mythic-rtc/tsconfig.json` (config)
- `packages/mythic-windowing/package.json` (manifest)
- `packages/mythic-windowing/tsconfig.json` (config)
- `packages/myths/package.json` (manifest)
- `packages/myths/tsconfig.json` (config)
- `packages/notebook-app-component/package.json` (manifest)
- `packages/notebook-app-component/tsconfig.json` (config)
- `packages/presentational-components/__tests__/tsconfig.json` (config)
- `packages/presentational-components/package.json` (manifest)
- `packages/presentational-components/tsconfig.json` (config)
- `packages/reducers/package.json` (manifest)
- `packages/reducers/tsconfig.json` (config)
- `packages/rx-binder/package.json` (manifest)
- `packages/rx-binder/tsconfig.json` (config)
- `packages/rx-jupyter/package.json` (manifest)
- `packages/rx-jupyter/tsconfig.json` (config)
- `packages/selectors/package.json` (manifest)
- `packages/selectors/tsconfig.json` (config)
- `packages/stateful-components/mkdocs.yml` (config)
- `packages/stateful-components/package.json` (manifest)
- `packages/stateful-components/tsconfig.json` (config)
- `packages/styles/package.json` (manifest)
- `packages/styles/tsconfig.json` (config)
- `packages/tsconfig.json` (config)
- `packages/types/package.json` (manifest)
- `packages/types/tsconfig.json` (config)
- `packages/webpack-configurator/package.json` (manifest)
- `renovate.json` (config)
- `requirements.txt` (manifest)
- `styleguide/now.json` (config)
- `tsconfig.base.json` (config)
- `tsconfig.jest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 478 analysed file(s)
- `applications` — 151 analysed file(s)
- `changelogs` — 31 analysed file(s)
- `(root files)` — 30 analysed file(s)
- `types` — 20 analysed file(s)
- `.github` — 16 analysed file(s)
- `docs` — 11 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.husky` — 3 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `styleguide-components` — 3 analysed file(s)
- `nteract-packages` — 2 analysed file(s)
- `styleguide` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (1 x likely secret file excluded; 2 x lockfile excluded; 4 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `7516211c27bad1e5a415505b023e2221bc430d8a` is the revision these paths and observations refer to.
