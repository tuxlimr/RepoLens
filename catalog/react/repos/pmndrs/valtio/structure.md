# Project structure: pmndrs/valtio

**Analysed commit:** `26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d`

**Commit reference:** [26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d](https://github.com/pmndrs/valtio/commit/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d)

**Tree at this commit:** [pmndrs/valtio@26d8ca8cb6e5](https://github.com/pmndrs/valtio/tree/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pmndrs/valtio |
| Description | 🧙 Valtio makes proxy-state simple  for React and Vanilla |
| Stars | 10245 |
| Forks | 294 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d` |
| Retrieved at | 2026-11-14T19:13:32.157996+00:00 |
| Files in this snapshot | 227 |

## Directory tree

```text
.github/  (12 files)
  DISCUSSION_TEMPLATE/  (1 files)
    bug-report.yml
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (7 files)
    compressed-size.yml
    preview-release.yml
    publish.yml
    test-multiple-builds.yml
    test-multiple-versions.yml
    test-old-typescript.yml
    test.yml
  FUNDING.yml
  pull_request_template.md
docs/  (37 files)
  api/  (16 files)
    advanced/  (4 files)
      … 4 files under this directory
    basic/  (2 files)
      … 2 files under this directory
    hacks/  (2 files)
      … 2 files under this directory
    utils/  (8 files)
      … 8 files under this directory
  guides/  (4 files)
    async.mdx
    component-state.mdx
    computed-properties.mdx
    migrating-to-v2.mdx
  how-tos/  (10 files)
    how-to-avoid-rerenders-manually.mdx
    how-to-easily-access-the-state-from-anywhere-in-the-application.mdx
    how-to-organize-actions.mdx
    how-to-persist-states.mdx
    how-to-reset-state.mdx
    how-to-split-and-compose-states.mdx
    how-to-update-values-inside-arrays.mdx
    how-to-use-with-context.mdx
    how-valtio-works.mdx
    some-gotchas.mdx
  introduction/  (2 files)
    getting-started.mdx
    logo.svg
  resources/  (3 files)
    community.mdx
    learn.mdx
    libraries.mdx
  introduction.mdx
  readme.md
examples/  (63 files)
  counter/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    index.html
    package.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  editor-proxyWithHistory/  (10 files)
    src/  (4 files)
      … 4 files under this directory
    index.html
    package.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  photo-booth-vanillajs/  (4 files)
    src/  (2 files)
      … 2 files under this directory
    index.html
    package.json
  starter/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  subscribe/  (1 files)
    index.html
  todo/  (12 files)
    src/  (6 files)
      … 6 files under this directory
    index.html
    package.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  todo-with-proxyMap/  (15 files)
    src/  (9 files)
      … 9 files under this directory
    index.html
    package.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  README.md
src/  (15 files)
  react/  (2 files)
    utils/  (1 files)
      … 1 files under this directory
    utils.ts
  vanilla/  (8 files)
    utils/  (7 files)
      … 7 files under this directory
    utils.ts
  index.ts
  react.ts
  types.d.ts
  utils.ts
  vanilla.ts
tests/  (42 files)
  perf/  (3 files)
    memoryleaks.test.ts
    performance.test.ts
    proxyMap.bench.ts
  react/  (20 files)
    actions.test.tsx
    array.test.tsx
    arrays.test.tsx
    async.test.tsx
    basic.test.tsx
    circular.test.tsx
    class.test.tsx
    component-state.test.tsx
    computed-properties.test.tsx
    container-tracking.test.tsx
    getter-results.test.tsx
    getter.test.tsx
    gotchas.test.tsx
    mapset.test.tsx
    object.test.tsx
    optimization.test.tsx
    ref.test.tsx
    replacement.test.tsx
    ssr.test.tsx
    useProxy.test.tsx
  regression/  (2 files)
    react.test.tsx
    watch.test.ts
  utils/  (7 files)
    deepClone.test.ts
    deepProxy.test.ts
    devtools.test.tsx
    proxyMap.test.tsx
    proxySet.test.tsx
    subscribeKey.test.ts
    watch.test.ts
  vanilla/  (8 files)
    array-insertion.test.ts
    detachment.test.ts
    entrypoints.test.ts
    proxy.test.ts
    ref.test.ts
    snapshot.test.ts
    subscribe.test.ts
    unstable.test.ts
  setup.ts
  test-utils.ts
website/  (46 files)
  _utils/  (2 files)
    file_helpers.ts
    index.ts
  components/  (18 files)
    LandingPage/  (5 files)
      … 5 files under this directory
    MDXRenderer/  (2 files)
      … 2 files under this directory
    SEO/  (2 files)
      … 2 files under this directory
    ToggleTheme/  (2 files)
      … 2 files under this directory
    layouts/  (7 files)
      … 7 files under this directory
  hooks/  (4 files)
    index.ts
    useCodesandboxTheme.ts
    useIsomorphicLayoutEffect.ts
    useTheme.ts
  lib/  (2 files)
    mdx.ts
    remarkCodeSandboxURLUpdater.ts
  pages/  (4 files)
    docs/  (1 files)
      … 1 files under this directory
    _app.tsx
    _document.tsx
    index.tsx
  public/  (1 files)
    vercel.svg
  state/  (2 files)
    index.ts
    useThemeState.ts
  styles/  (3 files)
    landing-page.css
    prism-theme.css
    tailwind.css
  .eslintrc.json
  .gitignore
  README.md
  next-env.d.ts
  next.config.js
  package.json
  postcss.config.js
  tailwind.config.js
  tsconfig.json
  types.d.ts
.gitignore
.prettierignore
CONTRIBUTING.md
LICENSE
README.md
eslint.config.mjs
logo.svg
package.json
pnpm-workspace.yaml
rollup.config.mjs
tsconfig.json
vitest.config.mts
```

## Entry points

- [src/index.ts](https://github.com/pmndrs/valtio/blob/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d/src/index.ts)
- [website/_utils/index.ts](https://github.com/pmndrs/valtio/blob/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d/website/_utils/index.ts)
- [website/components/MDXRenderer/index.ts](https://github.com/pmndrs/valtio/blob/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d/website/components/MDXRenderer/index.ts)
- [website/components/SEO/index.ts](https://github.com/pmndrs/valtio/blob/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d/website/components/SEO/index.ts)
- [website/components/ToggleTheme/index.ts](https://github.com/pmndrs/valtio/blob/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d/website/components/ToggleTheme/index.ts)
- [website/components/layouts/index.ts](https://github.com/pmndrs/valtio/blob/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d/website/components/layouts/index.ts)
- [website/hooks/index.ts](https://github.com/pmndrs/valtio/blob/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d/website/hooks/index.ts)
- [website/pages/index.tsx](https://github.com/pmndrs/valtio/blob/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d/website/pages/index.tsx)
- [website/state/index.ts](https://github.com/pmndrs/valtio/blob/26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d/website/state/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 2 file(s) under react package (observed from repository paths and static analysis). |
| react.ts package | library | Observed | Groups 1 file(s) under react.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 42 file(s) under tests (observed from repository paths and static analysis). |
| types.d.ts package | library | Observed | Groups 1 file(s) under types.d.ts package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |
| vanilla package | library | Observed | Groups 8 file(s) under vanilla package (observed from repository paths and static analysis). |
| vanilla.ts package | library | Observed | Groups 1 file(s) under vanilla.ts package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 36 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.github/DISCUSSION_TEMPLATE/bug-report.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/compressed-size.yml` (ci)
- `.github/workflows/preview-release.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test-multiple-builds.yml` (ci)
- `.github/workflows/test-multiple-versions.yml` (ci)
- `.github/workflows/test-old-typescript.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `examples/counter/package.json` (manifest)
- `examples/counter/tsconfig.app.json` (config)
- `examples/counter/tsconfig.json` (config)
- `examples/counter/tsconfig.node.json` (config)
- `examples/editor-proxyWithHistory/package.json` (manifest)
- `examples/editor-proxyWithHistory/tsconfig.app.json` (config)
- `examples/editor-proxyWithHistory/tsconfig.json` (config)
- `examples/editor-proxyWithHistory/tsconfig.node.json` (config)
- `examples/photo-booth-vanillajs/package.json` (manifest)
- `examples/starter/package.json` (manifest)
- `examples/starter/tsconfig.json` (config)
- `examples/todo-with-proxyMap/package.json` (manifest)
- `examples/todo-with-proxyMap/tsconfig.app.json` (config)
- `examples/todo-with-proxyMap/tsconfig.json` (config)
- `examples/todo-with-proxyMap/tsconfig.node.json` (config)
- `examples/todo/package.json` (manifest)
- `examples/todo/tsconfig.app.json` (config)
- `examples/todo/tsconfig.json` (config)
- `examples/todo/tsconfig.node.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `website/.eslintrc.json` (config)
- `website/package.json` (manifest)
- `website/tsconfig.json` (config)

## Top-level layout

- `examples` — 63 analysed file(s)
- `website` — 46 analysed file(s)
- `tests` — 42 analysed file(s)
- `docs` — 37 analysed file(s)
- `src` — 15 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 12 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `26d8ca8cb6e5bb3b9516d429e50bc5aab1f42e0d` is the revision these paths and observations refer to.
