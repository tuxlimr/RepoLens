# Project structure: callstack/react-native-testing-library

**Analysed commit:** `564a84294717d8e4b0831f3e3a5e115cc3832e01`

**Commit reference:** [564a84294717d8e4b0831f3e3a5e115cc3832e01](https://github.com/callstack/react-native-testing-library/commit/564a84294717d8e4b0831f3e3a5e115cc3832e01)

**Tree at this commit:** [callstack/react-native-testing-library@564a84294717](https://github.com/callstack/react-native-testing-library/tree/564a84294717d8e4b0831f3e3a5e115cc3832e01)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | callstack/react-native-testing-library |
| Description | 🦉 Simple and complete React Native testing utilities that encourage good testing practices. |
| Stars | 3429 |
| Forks | 281 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `564a84294717d8e4b0831f3e3a5e115cc3832e01` |
| Retrieved at | 2026-11-14T19:15:19.465836+00:00 |
| Files in this snapshot | 630 |

## Directory tree

```text
.gemini/  (1 files)
  settings.json
.github/  (17 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    question.md
  actions/  (7 files)
    setup-deps/  (1 files)
      … 1 files under this directory
    setup-deps-react-18/  (1 files)
      … 1 files under this directory
    setup-deps-rn-latest/  (1 files)
      … 1 files under this directory
    setup-deps-rn-next/  (1 files)
      … 1 files under this directory
    setup-deps-rn-nightly/  (1 files)
      … 1 files under this directory
    setup-website-deps/  (1 files)
      … 1 files under this directory
    typecheck-react-19_2-if-supported/  (1 files)
      … 1 files under this directory
  workflows/  (5 files)
    ci.yml
    example-apps.yml
    nightly-v13.yaml
    nightly.yaml
    website.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.vscode/  (1 files)
  settings.json
codemods/  (105 files)
  v14-async-functions/  (73 files)
    scripts/  (1 files)
      … 1 files under this directory
    tests/  (66 files)
      … 66 files under this directory
    .gitignore
    README.md
    codemod.yaml
    package.json
    tsconfig.json
    workflow.yaml
  v14-update-deps/  (32 files)
    scripts/  (2 files)
      … 2 files under this directory
    tests/  (24 files)
      … 24 files under this directory
    .gitignore
    README.md
    codemod.yaml
    package.json
    tsconfig.json
    workflow.yaml
contributing/  (11 files)
  accessibility.md
  architecture.md
  async-and-timers.md
  build-and-validation.md
  code-style.md
  event-dispatch.md
  example-apps.md
  git-workflow.md
  native-events.md
  native-state.md
  testing.md
docs/  (24 files)
  api/  (12 files)
    accessibility.md
    async-utilities.md
    configuration.md
    fire-event.md
    jest-matchers.md
    other-helpers.md
    overview.md
    queries.md
    render-hook.md
    render.md
    screen.md
    user-event.md
  cookbook/  (3 files)
    async-events.md
    custom-render.md
    network-requests.md
  guides/  (8 files)
    common-mistakes.md
    how-to-query.md
    llm-guidelines.md
    migration-v14.md
    quick-start.md
    testing-environment.md
    troubleshooting.md
    understanding-act.md
  README.md
examples/  (65 files)
  basic/  (19 files)
    .expo-shared/  (1 files)
      … 1 files under this directory
    __tests__/  (1 files)
      … 1 files under this directory
    components/  (4 files)
      … 4 files under this directory
    .gitignore
    AGENTS.md
    App.tsx
    README.md
    app.json
    babel.config.js
    eslint.config.mjs
    index.ts
    jest-setup.ts
    jest.config.js
    package.json
    theme.ts
    tsconfig.json
  cookbook/  (46 files)
    .expo-shared/  (1 files)
      … 1 files under this directory
    app/  (23 files)
      … 23 files under this directory
    basics-tutorial/  (6 files)
      … 6 files under this directory
    basics-tutorial-react-strict-dom/  (5 files)
      … 5 files under this directory
    .gitignore
    AGENTS.md
    README.md
    app.json
    babel.config.js
    eslint.config.mjs
    jest-setup.ts
    jest.config.js
    package.json
    theme.ts
    tsconfig.json
experiments-app/  (17 files)
  src/  (10 files)
    screens/  (7 files)
      … 7 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    MainScreen.tsx
    experiments.ts
  .gitignore
  App.tsx
  app.json
  babel.config.js
  index.ts
  package.json
  tsconfig.json
scripts/  (2 files)
  generate-package-docs.mjs
  test-codemods.mjs
skills/  (4 files)
  react-native-testing/  (4 files)
    references/  (3 files)
      … 3 files under this directory
    SKILL.md
src/  (204 files)
  __tests__/  (22 files)
    __snapshots__/  (1 files)
      … 1 files under this directory
    react-19_2/  (1 files)
      … 1 files under this directory
    act.test.tsx
    auto-cleanup-skip.test.tsx
    auto-cleanup.test.tsx
    cleanup.test.tsx
    config.test.ts
    host-component-names.test.tsx
    host-text-nesting.test.tsx
    questionsBoard.test.tsx
    react-native-animated.test.tsx
    react-native-api.test.tsx
    render-debug.test.tsx
    render-hook.test.tsx
    render.test.tsx
    screen.test.tsx
    suspense-fake-timers.test.tsx
    suspense.test.tsx
    timers.test.ts
    wait-for-element-to-be-removed.test.tsx
    wait-for.test.tsx
    within.test.tsx
  events/  (25 files)
    __tests__/  (3 files)
      … 3 files under this directory
    builders/  (12 files)
      … 12 files under this directory
    dispatch.ts
    fire-event.ts
    handler.ts
    index.ts
    is-enabled.ts
    native-state.ts
    propagation.ts
    types.ts
    update-native-state.ts
    warnings.ts
  helpers/  (36 files)
    __tests__/  (11 files)
      … 11 files under this directory
    matchers/  (10 files)
      … 10 files under this directory
    accessibility.ts
    component-tree.ts
    debug.ts
    errors.ts
    find-all.ts
    format-element.ts
    host-component-names.ts
    logger.ts
    map-props.ts
    object.ts
    text-content.ts
    text-input.ts
    timers.ts
    validate-options.ts
    wrap-async.ts
  matchers/  (37 files)
    __tests__/  (17 files)
      … 17 files under this directory
    extend-expect.ts
    index.ts
    to-be-busy.ts
    to-be-checked.ts
    to-be-disabled.ts
    to-be-empty-element.ts
    to-be-expanded.ts
    to-be-on-the-screen.ts
    to-be-partially-checked.ts
    to-be-selected.ts
    to-be-visible.ts
    to-contain-element.ts
    to-have-accessibility-value.ts
    to-have-accessible-name.ts
    to-have-display-value.ts
    to-have-prop.ts
    to-have-style.ts
    to-have-text-content.ts
    types.ts
    utils.ts
  queries/  (19 files)
    __tests__/  (10 files)
      … 10 files under this directory
    display-value.ts
    hint-text.ts
    label-text.ts
    make-queries.ts
    options.ts
    placeholder-text.ts
    role.ts
    test-id.ts
    text.ts
  test-utils/  (6 files)
    console.ts
    events.ts
    json.ts
    react-version-gates.ts
    timers.ts
    version.ts
  user-event/  (45 files)
    __tests__/  (5 files)
      … 5 files under this directory
    accessibility-action/  (3 files)
      … 3 files under this directory
    press/  (8 files)
      … 8 files under this directory
    scroll/  (9 files)
      … 9 files under this directory
    setup/  (3 files)
      … 3 files under this directory
    type/  (8 files)
      … 8 files under this directory
    utils/  (6 files)
      … 6 files under this directory
    clear.ts
    index.ts
    paste.ts
  act.ts
  cleanup.ts
  config.ts
  flush-micro-tasks.ts
  index.ts
  matches.ts
  pure.ts
  render-hook.tsx
  render.tsx
  screen.ts
  types.ts
  wait-for-element-to-be-removed.ts
  wait-for.ts
  within.ts
website/  (151 files)
  docs/  (146 files)
    12.x/  (46 files)
      … 46 files under this directory
    13.x/  (51 files)
      … 51 files under this directory
    14.x/  (42 files)
      … 42 files under this directory
    public/  (5 files)
      … 5 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    404.mdx
  theme/  (1 files)
    index.tsx
  .gitignore
  package.json
  rspress.config.ts
  tsconfig.json
.codecov.yml
.editorconfig
.gitignore
.gitmodules
.nvmrc
.oxfmtrc.json
.release-it.json
.yarnrc.yml
AGENTS.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README-v13.md
README.md
babel.config.js
dont-cleanup-after-each.js
eslint.config.mjs
jest-setup.ts
jest.config.js
matchers.d.ts
matchers.js
package.json
pure.d.ts
… 4 more files
```

## Entry points

- [examples/basic/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/examples/basic/index.ts)
- [experiments-app/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/experiments-app/index.ts)
- [experiments-app/App.tsx](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/experiments-app/App.tsx)
- [src/events/builders/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/src/events/builders/index.ts)
- [src/events/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/src/events/index.ts)
- [src/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/src/index.ts)
- [src/matchers/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/src/matchers/index.ts)
- [src/user-event/accessibility-action/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/src/user-event/accessibility-action/index.ts)
- [src/user-event/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/src/user-event/index.ts)
- [src/user-event/press/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/src/user-event/press/index.ts)
- [src/user-event/scroll/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/src/user-event/scroll/index.ts)
- [src/user-event/setup/index.ts](https://github.com/callstack/react-native-testing-library/blob/564a84294717d8e4b0831f3e3a5e115cc3832e01/src/user-event/setup/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| act.ts package | library | Observed | Groups 1 file(s) under act.ts package (observed from repository paths and static analysis). |
| cleanup.ts package | library | Observed | Groups 1 file(s) under cleanup.ts package (observed from repository paths and static analysis). |
| codemods package | library | Observed | Groups 3 file(s) under codemods package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 57 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.ts package | library | Observed | Groups 1 file(s) under config.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 9 file(s) under core modules (observed from repository paths and static analysis). |
| events package | library | Observed | Groups 25 file(s) under events package (observed from repository paths and static analysis). |
| experiments-app package | library | Observed | Groups 13 file(s) under experiments-app package (observed from repository paths and static analysis). |
| flush-micro-tasks.ts package | library | Observed | Groups 1 file(s) under flush-micro-tasks.ts package (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 36 file(s) under helpers package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| matchers package | library | Observed | Groups 37 file(s) under matchers package (observed from repository paths and static analysis). |
| matches.ts package | library | Observed | Groups 1 file(s) under matches.ts package (observed from repository paths and static analysis). |
| pure.ts package | library | Observed | Groups 1 file(s) under pure.ts package (observed from repository paths and static analysis). |
| queries package | library | Observed | Groups 19 file(s) under queries package (observed from repository paths and static analysis). |
| render-hook.tsx package | library | Observed | Groups 1 file(s) under render-hook.tsx package (observed from repository paths and static analysis). |
| render.tsx package | library | Observed | Groups 1 file(s) under render.tsx package (observed from repository paths and static analysis). |
| screen.ts package | library | Observed | Groups 1 file(s) under screen.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| test-utils package | library | Observed | Groups 6 file(s) under test-utils package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 111 file(s) under tests (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| user-event package | library | Observed | Groups 37 file(s) under user-event package (observed from repository paths and static analysis). |
| wait-for-element-to-be-removed.ts package | library | Observed | Groups 1 file(s) under wait-for-element-to-be-removed.ts package (observed from repository paths and static analysis). |
| wait-for.ts package | library | Observed | Groups 1 file(s) under wait-for.ts package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 2 file(s) under website package (observed from repository paths and static analysis). |
| within.ts package | library | Observed | Groups 1 file(s) under within.ts package (observed from repository paths and static analysis). |

## Important files

- `.codecov.yml` (config)
- `.editorconfig` (config)
- `.gemini/settings.json` (config)
- `.github/actions/setup-deps-react-18/action.yml` (config)
- `.github/actions/setup-deps-rn-latest/action.yml` (config)
- `.github/actions/setup-deps-rn-next/action.yml` (config)
- `.github/actions/setup-deps-rn-nightly/action.yml` (config)
- `.github/actions/setup-deps/action.yml` (config)
- `.github/actions/setup-website-deps/action.yml` (config)
- `.github/actions/typecheck-react-19_2-if-supported/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/example-apps.yml` (ci)
- `.github/workflows/nightly-v13.yaml` (ci)
- `.github/workflows/nightly.yaml` (ci)
- `.github/workflows/website.yml` (ci)
- `.oxfmtrc.json` (config)
- `.release-it.json` (config)
- `.vscode/settings.json` (config)
- `.yarnrc.yml` (config)
- `codemods/v14-async-functions/codemod.yaml` (config)
- `codemods/v14-async-functions/package.json` (manifest)
- `codemods/v14-async-functions/tsconfig.json` (config)
- `codemods/v14-async-functions/workflow.yaml` (config)
- `codemods/v14-update-deps/codemod.yaml` (config)
- `codemods/v14-update-deps/package.json` (manifest)
- `codemods/v14-update-deps/tsconfig.json` (config)
- `codemods/v14-update-deps/workflow.yaml` (config)
- `examples/basic/.expo-shared/assets.json` (config)
- `examples/basic/app.json` (config)
- `examples/basic/package.json` (manifest)
- `examples/basic/tsconfig.json` (config)
- `examples/cookbook/.expo-shared/assets.json` (config)
- `examples/cookbook/app.json` (config)
- `examples/cookbook/package.json` (manifest)
- `examples/cookbook/tsconfig.json` (config)
- `experiments-app/app.json` (config)
- `experiments-app/package.json` (manifest)
- `experiments-app/tsconfig.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tsconfig.react-19_2.json` (config)
- `tsconfig.release.json` (config)
- `website/docs/12.x/_nav.json` (config)
- `website/docs/12.x/cookbook/_meta.json` (config)
- `website/docs/12.x/cookbook/advanced/_meta.json` (config)
- `website/docs/12.x/cookbook/basics/_meta.json` (config)
- `website/docs/12.x/cookbook/state-management/_meta.json` (config)
- `website/docs/12.x/docs/_meta.json` (config)
- `website/docs/12.x/docs/advanced/_meta.json` (config)
- `website/docs/12.x/docs/api/_meta.json` (config)
- `website/docs/12.x/docs/api/events/_meta.json` (config)
- `website/docs/12.x/docs/api/misc/_meta.json` (config)
- `website/docs/12.x/docs/guides/_meta.json` (config)
- `website/docs/12.x/docs/migration/_meta.json` (config)
- `website/docs/12.x/docs/migration/previous/_meta.json` (config)
- `website/docs/12.x/docs/start/_meta.json` (config)
- `website/docs/13.x/_nav.json` (config)
- `website/docs/13.x/cookbook/_meta.json` (config)
- `website/docs/13.x/cookbook/advanced/_meta.json` (config)
- `website/docs/13.x/cookbook/basics/_meta.json` (config)
- `website/docs/13.x/cookbook/state-management/_meta.json` (config)
- `website/docs/13.x/docs/_meta.json` (config)
- `website/docs/13.x/docs/advanced/_meta.json` (config)
- `website/docs/13.x/docs/api/_meta.json` (config)
- `website/docs/13.x/docs/api/events/_meta.json` (config)
- `website/docs/13.x/docs/api/misc/_meta.json` (config)
- `website/docs/13.x/docs/guides/_meta.json` (config)
- `website/docs/13.x/docs/migration/_meta.json` (config)
- `website/docs/13.x/docs/migration/previous/_meta.json` (config)
- `website/docs/13.x/docs/start/_meta.json` (config)
- `website/docs/14.x/_nav.json` (config)
- `website/docs/14.x/cookbook/_meta.json` (config)
- `website/docs/14.x/cookbook/advanced/_meta.json` (config)
- `website/docs/14.x/cookbook/basics/_meta.json` (config)
- `website/docs/14.x/cookbook/state-management/_meta.json` (config)
- `website/docs/14.x/docs/_meta.json` (config)
- `website/docs/14.x/docs/advanced/_meta.json` (config)
- `website/docs/14.x/docs/api/_meta.json` (config)
- `website/docs/14.x/docs/api/events/_meta.json` (config)
- `website/docs/14.x/docs/api/misc/_meta.json` (config)
- `website/docs/14.x/docs/guides/_meta.json` (config)
- `website/docs/14.x/docs/start/_meta.json` (config)
- `website/package.json` (manifest)
- `website/tsconfig.json` (config)

## Top-level layout

- `src` — 204 analysed file(s)
- `website` — 151 analysed file(s)
- `codemods` — 105 analysed file(s)
- `examples` — 65 analysed file(s)
- `(root files)` — 28 analysed file(s)
- `docs` — 24 analysed file(s)
- `.github` — 17 analysed file(s)
- `experiments-app` — 17 analysed file(s)
- `contributing` — 11 analysed file(s)
- `skills` — 4 analysed file(s)
- `scripts` — 2 analysed file(s)
- `.gemini` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `564a84294717d8e4b0831f3e3a5e115cc3832e01` is the revision these paths and observations refer to.
