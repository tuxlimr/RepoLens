# Project structure: pmndrs/jotai

**Analysed commit:** `9de9377d10a5ac01388764b89458e2d7091d29d4`

**Commit reference:** [9de9377d10a5ac01388764b89458e2d7091d29d4](https://github.com/pmndrs/jotai/commit/9de9377d10a5ac01388764b89458e2d7091d29d4)

**Tree at this commit:** [pmndrs/jotai@9de9377d10a5](https://github.com/pmndrs/jotai/tree/9de9377d10a5ac01388764b89458e2d7091d29d4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pmndrs/jotai |
| Description | 👻 Primitive and flexible state management for React |
| Stars | 21320 |
| Forks | 730 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `9de9377d10a5ac01388764b89458e2d7091d29d4` |
| Retrieved at | 2026-11-14T19:13:09.976113+00:00 |
| Files in this snapshot | 326 |

## Directory tree

```text
.github/  (13 files)
  DISCUSSION_TEMPLATE/  (1 files)
    bug-report.yml
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (8 files)
    compressed-size.yml
    ecosystem-ci.yml
    preview-release.yml
    publish.yml
    test-multiple-builds.yml
    test-multiple-versions.yml
    test-old-typescript.yml
    test.yml
  FUNDING.yml
  pull_request_template.md
.livecodes/  (1 files)
  react.json
benchmarks/  (10 files)
  .gitignore
  atom-creation.ts
  computed-read.ts
  derived-chain.ts
  diamond.ts
  read-write.ts
  run-all.ts
  select-atom.ts
  subscription.ts
  wide-fan-out.ts
docs/  (72 files)
  basics/  (4 files)
    comparison.mdx
    concepts.mdx
    functional-programming-and-jotai.mdx
    showcase.mdx
  core/  (4 files)
    atom.mdx
    provider.mdx
    store.mdx
    use-atom.mdx
  extensions/  (14 files)
    cache.mdx
    effect.mdx
    immer.mdx
    location.mdx
    optics.mdx
    query.mdx
    redux.mdx
    relay.mdx
    scope.mdx
    trpc.mdx
    urql.mdx
    valtio.mdx
    xstate.mdx
    zustand.mdx
  guides/  (19 files)
    async.mdx
    atoms-in-atom.mdx
    composing-atoms.mdx
    core-internals.mdx
    debugging.mdx
    initialize-atom-on-render.mdx
    migrating-to-v2-api.mdx
    migrating-to-v3.mdx
    nextjs.mdx
    performance.mdx
    persistence.mdx
    react-native.mdx
    remix.mdx
    resettable.mdx
    testing.mdx
    typescript.mdx
    using-store-outside-react.mdx
    vite.mdx
    waku.mdx
  recipes/  (12 files)
    atom-with-broadcast.mdx
    atom-with-compare.mdx
    atom-with-debounce.mdx
    atom-with-listeners.mdx
    atom-with-refresh-and-default.mdx
    atom-with-refresh.mdx
    atom-with-toggle-and-storage.mdx
    atom-with-toggle.mdx
    custom-useatom-hooks.mdx
    large-objects.mdx
    use-atom-effect.mdx
    use-reducer-atom.mdx
  third-party/  (3 files)
    bunja.mdx
    eager.mdx
    history.mdx
  tools/  (5 files)
    babel.mdx
    devtools.mdx
    rolldown.mdx
    skill.mdx
    swc.mdx
  utilities/  (10 files)
    async.mdx
    callback.mdx
    family.mdx
    lazy.mdx
    reducer.mdx
    resettable.mdx
    select.mdx
    split.mdx
    ssr.mdx
    storage.mdx
  index.mdx
examples/  (71 files)
  hacker_news/  (10 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  hello/  (11 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  mega-form/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (6 files)
      … 6 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  starter/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  text_length/  (10 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  todos/  (10 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  todos_with_atomFamily/  (10 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
img/  (1 files)
  title.svg
src/  (33 files)
  react/  (12 files)
    utils/  (4 files)
      … 4 files under this directory
    Provider.ts
    continuablePromise.ts
    useAtom.ts
    useAtomValue.ts
    useAtomValueRaw.ts
    useAtomValueRawSync.ts
    useSetAtom.ts
    utils.ts
  vanilla/  (17 files)
    utils/  (12 files)
      … 12 files under this directory
    atom.ts
    internals.ts
    store.ts
    typeUtils.ts
    utils.ts
  index.ts
  react.ts
  utils.ts
  vanilla.ts
tests/  (46 files)
  react/  (29 files)
    utils/  (5 files)
      … 5 files under this directory
    vanilla-utils/  (8 files)
      … 8 files under this directory
    abortable.test.tsx
    async.test.tsx
    async2.test.tsx
    basic.test.tsx
    dependency.test.tsx
    error.test.tsx
    items.test.tsx
    onmount.test.tsx
    optimization.test.tsx
    provider.test.tsx
    transition.test.tsx
    types.test.tsx
    useAtomValue.test.tsx
    useAtomValueRaw.test.tsx
    useAtomValueRawSync.test.tsx
    useSetAtom.test.tsx
  vanilla/  (15 files)
    utils/  (6 files)
      … 6 files under this directory
    basic.test.tsx
    dependency.test.tsx
    derive.test.tsx
    effect.test.ts
    internals.test.tsx
    memoryleaks.test.ts
    store.test.tsx
    storedev.test.tsx
    types.test.tsx
  setup.ts
  test-utils.ts
website/  (68 files)
  api/  (1 files)
    contact.js
  public/  (1 files)
    robots.txt
  src/  (49 files)
    api/  (1 files)
      … 1 files under this directory
    atoms/  (1 files)
      … 1 files under this directory
    components/  (35 files)
      … 35 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    styles/  (7 files)
      … 7 files under this directory
    utils/  (1 files)
      … 1 files under this directory
  static/  (3 files)
    favicon.svg
    robots.txt
    search-by-algolia.svg
  .babelrc
  .gitignore
  README.md
  gatsby-browser.js
  gatsby-config.js
  gatsby-node.js
  gatsby-shared.js
  gatsby-ssr.js
  jsconfig.json
  package.json
  postcss.config.js
  reach-router.js
  tailwind.config.js
  vercel.json
.gitignore
.prettierignore
CONTRIBUTING.md
LICENSE
README.md
eslint.config.mjs
package.json
pnpm-workspace.yaml
tsconfig.build.json
tsconfig.json
vitest.config.mts
```

## Entry points

- [src/index.ts](https://github.com/pmndrs/jotai/blob/9de9377d10a5ac01388764b89458e2d7091d29d4/src/index.ts)
- [website/src/atoms/index.js](https://github.com/pmndrs/jotai/blob/9de9377d10a5ac01388764b89458e2d7091d29d4/website/src/atoms/index.js)
- [website/src/components/main.js](https://github.com/pmndrs/jotai/blob/9de9377d10a5ac01388764b89458e2d7091d29d4/website/src/components/main.js)
- [website/src/hooks/index.js](https://github.com/pmndrs/jotai/blob/9de9377d10a5ac01388764b89458e2d7091d29d4/website/src/hooks/index.js)
- [website/src/pages/index.js](https://github.com/pmndrs/jotai/blob/9de9377d10a5ac01388764b89458e2d7091d29d4/website/src/pages/index.js)
- [website/src/utils/index.js](https://github.com/pmndrs/jotai/blob/9de9377d10a5ac01388764b89458e2d7091d29d4/website/src/utils/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| benchmarks package | library | Observed | Groups 9 file(s) under benchmarks package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 12 file(s) under react package (observed from repository paths and static analysis). |
| react.ts package | library | Observed | Groups 1 file(s) under react.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 46 file(s) under tests (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |
| vanilla package | library | Observed | Groups 17 file(s) under vanilla package (observed from repository paths and static analysis). |
| vanilla.ts package | library | Observed | Groups 1 file(s) under vanilla.ts package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 48 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.github/DISCUSSION_TEMPLATE/bug-report.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/compressed-size.yml` (ci)
- `.github/workflows/ecosystem-ci.yml` (ci)
- `.github/workflows/preview-release.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test-multiple-builds.yml` (ci)
- `.github/workflows/test-multiple-versions.yml` (ci)
- `.github/workflows/test-old-typescript.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.livecodes/react.json` (config)
- `examples/hacker_news/package.json` (manifest)
- `examples/hacker_news/tsconfig.json` (config)
- `examples/hello/package.json` (manifest)
- `examples/hello/tsconfig.json` (config)
- `examples/mega-form/package.json` (manifest)
- `examples/mega-form/tsconfig.json` (config)
- `examples/starter/package.json` (manifest)
- `examples/starter/tsconfig.json` (config)
- `examples/text_length/package.json` (manifest)
- `examples/text_length/tsconfig.json` (config)
- `examples/todos/package.json` (manifest)
- `examples/todos/tsconfig.json` (config)
- `examples/todos_with_atomFamily/package.json` (manifest)
- `examples/todos_with_atomFamily/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)
- `website/jsconfig.json` (config)
- `website/package.json` (manifest)
- `website/vercel.json` (config)

## Top-level layout

- `docs` — 72 analysed file(s)
- `examples` — 71 analysed file(s)
- `website` — 68 analysed file(s)
- `tests` — 46 analysed file(s)
- `src` — 33 analysed file(s)
- `.github` — 13 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `benchmarks` — 10 analysed file(s)
- `.livecodes` — 1 analysed file(s)
- `img` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9de9377d10a5ac01388764b89458e2d7091d29d4` is the revision these paths and observations refer to.
