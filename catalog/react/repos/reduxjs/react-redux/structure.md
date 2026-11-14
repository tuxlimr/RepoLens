# Project structure: reduxjs/react-redux

**Analysed commit:** `8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd`

**Commit reference:** [8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd](https://github.com/reduxjs/react-redux/commit/8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd)

**Tree at this commit:** [reduxjs/react-redux@8e54f5b9dbbd](https://github.com/reduxjs/react-redux/tree/8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reduxjs/react-redux |
| Description | Official React bindings for Redux |
| Stars | 23423 |
| Forks | 3319 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd` |
| Retrieved at | 2026-11-14T19:13:07.384904+00:00 |
| Files in this snapshot | 113 |

## Directory tree

```text
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (5 files)
    publish.yml
    rebuild-docs-site.yml
    release-commit.yml
    size.yaml
    test.yml
  FUNDING.yml
  dependabot.yml
.vscode/  (1 files)
  settings.json
docs/  (14 files)
  api/  (4 files)
    Provider.md
    batch.md
    connect.md
    hooks.md
  introduction/  (2 files)
    getting-started.md
    why-use-react-redux.md
  tutorials/  (1 files)
    connect.md
  using-react-redux/  (4 files)
    accessing-store.md
    connect-dispatching-actions-with-mapDispatchToProps.md
    connect-extracting-data-with-mapStateToProps.md
    usage-with-typescript.md
  README.md
  sidebars.ts
  tsconfig.json
examples/  (12 files)
  publish-ci/  (12 files)
    rr-rsc-context/  (12 files)
      … 12 files under this directory
scripts/  (1 files)
  stripSourcemapFileField.mts
src/  (30 files)
  components/  (3 files)
    Context.ts
    Provider.tsx
    connect.tsx
  connect/  (7 files)
    invalidArgFactory.ts
    mapDispatchToProps.ts
    mapStateToProps.ts
    mergeProps.ts
    selectorFactory.ts
    verifySubselectors.ts
    wrapMapToProps.ts
  hooks/  (4 files)
    useDispatch.ts
    useReduxContext.ts
    useSelector.ts
    useStore.ts
  utils/  (12 files)
    Subscription.ts
    batch.ts
    bindActionCreators.ts
    hoistStatics.ts
    isPlainObject.ts
    react-is.ts
    react.ts
    shallowEqual.ts
    useIsomorphicLayoutEffect.ts
    useSyncExternalStore.ts
    verifyPlainObject.ts
    warning.ts
  exports.ts
  index-rsc.ts
  index.ts
  types.ts
test/  (24 files)
  components/  (4 files)
    Provider-rsc.spec.tsx
    Provider.spec.tsx
    connect.spec.tsx
    hooks.spec.tsx
  connect/  (1 files)
    wrapMapToProps.spec.ts
  hooks/  (4 files)
    hooks.withTypes.test.tsx
    useDispatch.spec.tsx
    useReduxContext.spec.tsx
    useSelector.spec.tsx
  integration/  (3 files)
    dynamic-reducers.spec.tsx
    server-rendering.spec.tsx
    ssr.spec.tsx
  typetests/  (8 files)
    connect-mapstate-mapdispatch.test-d.tsx
    connect-options-and-issues.test-d.tsx
    connect-union-ordering.test-d.tsx
    counterApp.ts
    hooks.test-d.tsx
    hooks.withTypes.test-d.tsx
    provider.test-d.tsx
    react-redux-types.test-d.tsx
  utils/  (3 files)
    Subscription.spec.ts
    isPlainObject.spec.ts
    shallowEqual.spec.ts
  setup.ts
.gitattributes
.gitignore
.oxfmtrc.json
.oxlintrc.json
.release-it.json
CHANGELOG.md
CNAME
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
README.md
codecov.yml
netlify.toml
package.json
pnpm-workspace.yaml
tsconfig.base.json
tsconfig.build.json
tsconfig.json
tsconfig.test.json
tsdown.config.mts
vitest.config.mts
```

## Entry points

- [src/index.ts](https://github.com/reduxjs/react-redux/blob/8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 3 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| connect package | library | Observed | Groups 7 file(s) under connect package (observed from repository paths and static analysis). |
| exports.ts package | library | Observed | Groups 1 file(s) under exports.ts package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 4 file(s) under hooks package (observed from repository paths and static analysis). |
| index-rsc.ts package | library | Observed | Groups 1 file(s) under index-rsc.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 24 file(s) under tests (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 12 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/rebuild-docs-site.yml` (ci)
- `.github/workflows/release-commit.yml` (ci)
- `.github/workflows/size.yaml` (ci)
- `.github/workflows/test.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `.release-it.json` (config)
- `.vscode/settings.json` (config)
- `codecov.yml` (config)
- `docs/tsconfig.json` (config)
- `examples/publish-ci/rr-rsc-context/package.json` (manifest)
- `examples/publish-ci/rr-rsc-context/pnpm-workspace.yaml` (config)
- `examples/publish-ci/rr-rsc-context/tsconfig.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.base.json` (config)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)
- `tsconfig.test.json` (config)

## Top-level layout

- `src` — 30 analysed file(s)
- `test` — 24 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `docs` — 14 analysed file(s)
- `examples` — 12 analysed file(s)
- `.github` — 10 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd` is the revision these paths and observations refer to.
