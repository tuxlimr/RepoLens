# Project structure: vercel/swr

**Analysed commit:** `8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f`

**Commit reference:** [8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f](https://github.com/vercel/swr/commit/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f)

**Tree at this commit:** [vercel/swr@8148ef012fd5](https://github.com/vercel/swr/tree/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vercel/swr |
| Description | React Hooks for Data Fetching |
| Stars | 32491 |
| Forks | 1407 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f` |
| Retrieved at | 2026-11-14T19:13:02.680112+00:00 |
| Files in this snapshot | 341 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (5 files)
    install/  (1 files)
      … 1 files under this directory
    test-canary.yml
    test-legacy-react.yml
    test.yml
    trigger-release.yml
  CODEOWNERS
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  SECURITY.md
.husky/  (1 files)
  pre-commit
_internal/  (1 files)
  package.json
examples/  (129 files)
  api-hooks/  (8 files)
    hooks/  (2 files)
      … 2 files under this directory
    libs/  (1 files)
      … 1 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  autocomplete-suggestions/  (5 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    README.md
    package.json
  basic/  (6 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  basic-typescript/  (8 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    README.md
    next-env.d.ts
    package.json
    tsconfig.json
  focus-revalidate/  (7 files)
    components/  (1 files)
      … 1 files under this directory
    libs/  (2 files)
      … 2 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    README.md
    package.json
  global-fetcher/  (7 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    README.md
    package.json
  infinite/  (4 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  infinite-scroll/  (5 files)
    hooks/  (1 files)
      … 1 files under this directory
    libs/  (1 files)
      … 1 files under this directory
    pages/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  local-state-sharing/  (4 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  optimistic-ui/  (7 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    README.md
    package.json
    styles.css
  optimistic-ui-immer/  (5 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    README.md
    package.json
  prefetch-preload/  (6 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    README.md
    package.json
  refetch-interval/  (6 files)
    components/  (1 files)
      … 1 files under this directory
    libs/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    README.md
    package.json
  server-render/  (5 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    README.md
    package.json
  storage-tab-sync/  (4 files)
    libs/  (1 files)
      … 1 files under this directory
    pages/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  subscription/  (3 files)
    pages/  (1 files)
      … 1 files under this directory
    README.md
    package.json
  suspense/  (16 files)
    app/  (8 files)
      … 8 files under this directory
    components/  (1 files)
      … 1 files under this directory
    libs/  (1 files)
      … 1 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    README.md
    next-env.d.ts
    package.json
  suspense-global/  (13 files)
    components/  (1 files)
      … 1 files under this directory
    libs/  (1 files)
      … 1 files under this directory
    pages/  (6 files)
      … 6 files under this directory
    README.md
    global-swr-config.tsx
    next-env.d.ts
    package.json
    tsconfig.json
  suspense-retry/  (10 files)
    app/  (5 files)
      … 5 files under this directory
    pages/  (1 files)
      … 1 files under this directory
    next-env.d.ts
    next.config.js
    package.json
    tsconfig.json
immutable/  (1 files)
  package.json
infinite/  (1 files)
  package.json
mutation/  (1 files)
  package.json
scripts/  (1 files)
  bump-next-version.js
src/  (42 files)
  _internal/  (27 files)
    utils/  (22 files)
      … 22 files under this directory
    constants.ts
    events.ts
    index.react-server.ts
    index.ts
    types.ts
  immutable/  (1 files)
    index.ts
  index/  (5 files)
    config.ts
    index.react-server.ts
    index.ts
    serialize.ts
    use-swr.ts
  infinite/  (4 files)
    index.react-server.ts
    index.ts
    serialize.ts
    types.ts
  mutation/  (3 files)
    index.ts
    state.ts
    types.ts
  subscription/  (2 files)
    index.ts
    types.ts
subscription/  (1 files)
  package.json
test/  (139 files)
  e2e/  (85 files)
    site/  (69 files)
      … 69 files under this directory
    cache-tags.test.ts
    concurrent-transition.test.ts
    initial-render.test.ts
    issue-2702-too-many-hooks.ts
    mutate-server-action.test.ts
    perf.test.ts
    playwright.config.ts
    preload-scenarios.test.ts
    promise-scenarios.test.ts
    server-prefetch-warning.test.ts
    stream-ssr.test.ts
    suspense-fallback.test.ts
    suspense-scenarios.test.ts
    suspense-undefined-key.test.ts
    tsconfig.json
    warmup.setup.ts
  type/  (15 files)
    suspense/  (3 files)
      … 3 files under this directory
    config.tsx
    fetcher.ts
    helper-types.tsx
    internal.tsx
    mutate.ts
    mutation.ts
    option-fetcher.ts
    preload.ts
    subscription.ts
    trigger.ts
    tsconfig.json
    utils.ts
  unit/  (3 files)
    serialize.test.ts
    utils.test.tsx
    web-preset.test.ts
  jest-setup.ts
  tsconfig.json
  use-swr-cache.test.tsx
  use-swr-concurrent-rendering.test.tsx
  use-swr-config-callbacks.test.tsx
  use-swr-config.test.tsx
  use-swr-context-config.test.tsx
  use-swr-devtools.test.tsx
  use-swr-error.test.tsx
  use-swr-fetcher.test.tsx
  use-swr-focus.test.tsx
  use-swr-immutable.test.tsx
  use-swr-infinite-preload.test.tsx
  use-swr-infinite.test.tsx
  use-swr-integration.test.tsx
  use-swr-key.test.tsx
  use-swr-laggy.test.tsx
  use-swr-legacy-react.test.tsx
  use-swr-loading.test.tsx
  use-swr-local-mutation.test.tsx
  use-swr-middlewares.test.tsx
  use-swr-node-env.test.tsx
  use-swr-offline.test.tsx
  use-swr-preload.test.tsx
  … 12 more files
.editorconfig
.gitignore
.oxfmtrc.json
.oxlintrc.json
.swcrc
LICENSE
README.md
jest.config.build.js
jest.config.js
package.json
pnpm-workspace.yaml
tsconfig.json
vercel.json
```

## Entry points

- [src/_internal/index.ts](https://github.com/vercel/swr/blob/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f/src/_internal/index.ts)
- [src/immutable/index.ts](https://github.com/vercel/swr/blob/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f/src/immutable/index.ts)
- [src/index/index.ts](https://github.com/vercel/swr/blob/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f/src/index/index.ts)
- [src/infinite/index.ts](https://github.com/vercel/swr/blob/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f/src/infinite/index.ts)
- [src/mutation/index.ts](https://github.com/vercel/swr/blob/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f/src/mutation/index.ts)
- [src/subscription/index.ts](https://github.com/vercel/swr/blob/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f/src/subscription/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| immutable package | library | Observed | Groups 1 file(s) under immutable package (observed from repository paths and static analysis). |
| index package | library | Observed | Groups 5 file(s) under index package (observed from repository paths and static analysis). |
| infinite package | library | Observed | Groups 4 file(s) under infinite package (observed from repository paths and static analysis). |
| _internal package | library | Observed | Groups 27 file(s) under _internal package (observed from repository paths and static analysis). |
| mutation package | library | Observed | Groups 3 file(s) under mutation package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| subscription package | library | Observed | Groups 2 file(s) under subscription package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 139 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/install/action.yml` (ci)
- `.github/workflows/test-canary.yml` (ci)
- `.github/workflows/test-legacy-react.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/trigger-release.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `_internal/package.json` (manifest)
- `examples/api-hooks/package.json` (manifest)
- `examples/autocomplete-suggestions/package.json` (manifest)
- `examples/basic-typescript/package.json` (manifest)
- `examples/basic-typescript/tsconfig.json` (config)
- `examples/basic/package.json` (manifest)
- `examples/focus-revalidate/package.json` (manifest)
- `examples/global-fetcher/package.json` (manifest)
- `examples/infinite-scroll/package.json` (manifest)
- `examples/infinite/package.json` (manifest)
- `examples/local-state-sharing/package.json` (manifest)
- `examples/optimistic-ui-immer/package.json` (manifest)
- `examples/optimistic-ui/package.json` (manifest)
- `examples/prefetch-preload/package.json` (manifest)
- `examples/refetch-interval/package.json` (manifest)
- `examples/server-render/package.json` (manifest)
- `examples/storage-tab-sync/package.json` (manifest)
- `examples/subscription/package.json` (manifest)
- `examples/suspense-global/package.json` (manifest)
- `examples/suspense-global/tsconfig.json` (config)
- `examples/suspense-retry/package.json` (manifest)
- `examples/suspense-retry/tsconfig.json` (config)
- `examples/suspense/package.json` (manifest)
- `immutable/package.json` (manifest)
- `infinite/package.json` (manifest)
- `mutation/package.json` (manifest)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `subscription/package.json` (manifest)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `test` — 139 analysed file(s)
- `examples` — 129 analysed file(s)
- `src` — 42 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 11 analysed file(s)
- `.husky` — 1 analysed file(s)
- `_internal` — 1 analysed file(s)
- `immutable` — 1 analysed file(s)
- `infinite` — 1 analysed file(s)
- `mutation` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)
- `subscription` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f` is the revision these paths and observations refer to.
