# Project structure: emotion-js/emotion

**Analysed commit:** `b882bcba85132554992e4bd49e94c95939bbf810`

**Commit reference:** [b882bcba85132554992e4bd49e94c95939bbf810](https://github.com/emotion-js/emotion/commit/b882bcba85132554992e4bd49e94c95939bbf810)

**Tree at this commit:** [emotion-js/emotion@b882bcba8513](https://github.com/emotion-js/emotion/tree/b882bcba85132554992e4bd49e94c95939bbf810)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | emotion-js/emotion |
| Description | 👩‍🎤 CSS-in-JS library designed for high performance style composition |
| Stars | 18025 |
| Forks | 1137 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `b882bcba85132554992e4bd49e94c95939bbf810` |
| Retrieved at | 2026-11-14T19:11:23.301591+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.codesandbox/  (1 files)
  ci.json
.github/  (11 files)
  ISSUE_TEMPLATE/  (4 files)
    --bug-report.md
    --documentation-issue.md
    --feature-request.md
    config.yml
  actions/  (1 files)
    ci-setup/  (1 files)
      … 1 files under this directory
  workflows/  (2 files)
    main.yml
    release.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  no-response.yml
  stale.yml
.yarn/  (2 files)
  patches/  (1 files)
    @definitelytyped-dtslint-npm-0.0.112-1e6b842976.patch
  plugins/  (1 files)
    @yarnpkg/  (1 files)
      … 1 files under this directory
__mocks__/  (2 files)
  react-native.js
  react-primitives.js
docs/  (32 files)
  README.md
  babel-macros.mdx
  babel.mdx
  best-practices.mdx
  cache-provider.mdx
  class-names.mdx
  community.mdx
  composition.mdx
  css-prop.mdx
  docs.yaml
  emotion-11.mdx
  eslint-plugin-react.mdx
  extract-static.mdx
  for-library-authors.mdx
  globals.mdx
  install.mdx
  introduction.mdx
  keyframes.mdx
  labels.mdx
  media-queries.mdx
  migrating-to-emotion-10.mdx
  nested.mdx
  object-styles.mdx
  package-summary.mdx
  … 8 more files
flow-typed/  (1 files)
  npm/  (1 files)
    vitest_vx.x.x.js
packages/  (618 files)
  babel-plugin/  (165 files)
    __tests__/  (144 files)
      … 144 files under this directory
    src/  (17 files)
      … 17 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  babel-plugin-jsx-pragmatic/  (11 files)
    __tests__/  (5 files)
      … 5 files under this directory
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    babel__plugin-syntax-jsx.d.ts
    package.json
  babel-preset-css-prop/  (11 files)
    __tests__/  (6 files)
      … 6 files under this directory
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  cache/  (20 files)
    __tests__/  (4 files)
      … 4 files under this directory
    src/  (7 files)
      … 7 files under this directory
    types/  (5 files)
      … 5 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  css/  (49 files)
    create-instance/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    test/  (31 files)
      … 31 files under this directory
    types/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    macro.d.mts
    macro.d.ts
    macro.js
    package.json
  css-prettifier/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  eslint-plugin/  (24 files)
    docs/  (5 files)
      … 5 files under this directory
    src/  (8 files)
      … 8 files under this directory
    test/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  hash/  (10 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    types/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  is-prop-valid/  (10 files)
    src/  (2 files)
      … 2 files under this directory
    types/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  jest/  (35 files)
    enzyme/  (1 files)
      … 1 files under this directory
    enzyme-serializer/  (1 files)
      … 1 files under this directory
    serializer/  (1 files)
      … 1 files under this directory
    src/  (14 files)
      … 14 files under this directory
    test/  (7 files)
      … 7 files under this directory
    types/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  memoize/  (8 files)
    src/  (1 files)
      … 1 files under this directory
    types/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    LICENSE
    package.json
  native/  (20 files)
    src/  (3 files)
      … 3 files under this directory
    test/  (3 files)
      … 3 files under this directory
    types/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    macro.d.mts
    macro.d.ts
    macro.js
    package.json
    tsconfig.json
  primitives/  (17 files)
    examples/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    test/  (6 files)
      … 6 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    macro.js
    package.json
  primitives-core/  (11 files)
    src/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  react/  (86 files)
    __tests__/  (49 files)
      … 49 files under this directory
    _isolated-hnrs/  (1 files)
      … 1 files under this directory
    jsx-dev-runtime/  (1 files)
      … 1 files under this directory
    jsx-runtime/  (1 files)
      … 1 files under this directory
    src/  (19 files)
      … 19 files under this directory
    types/  (8 files)
      … 8 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    macro.d.mts
    macro.d.ts
    macro.js
    package.json
  serialize/  (10 files)
    src/  (3 files)
      … 3 files under this directory
    types/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    LICENSE
    package.json
  server/  (31 files)
    create-instance/  (1 files)
      … 1 files under this directory
    src/  (12 files)
      … 12 files under this directory
    test/  (7 files)
      … 7 files under this directory
    types/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  sheet/  (13 files)
    __tests__/  (2 files)
      … 2 files under this directory
    src/  (3 files)
      … 3 files under this directory
    types/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  styled/  (46 files)
    __tests__/  (7 files)
      … 7 files under this directory
    base/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    test/  (15 files)
      … 15 files under this directory
    types/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    macro.d.mts
    macro.d.ts
    macro.js
    package.json
  unitless/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  use-insertion-effect-with-fallbacks/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  utils/  (13 files)
    src/  (5 files)
      … 5 files under this directory
    types/  (5 files)
      … 5 files under this directory
    CHANGELOG.md
    LICENSE
    package.json
  weak-memoize/  (10 files)
    __tests__/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    types/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    LICENSE
    README.md
    package.json
playgrounds/  (15 files)
  cra/  (6 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    package.json
  nextjs/  (8 files)
    pages/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    .babelrc.js
    .gitignore
    README.md
    next.config.js
    package.json
  README.md
scripts/  (58 files)
  babel-preset-emotion-dev/  (2 files)
    src/  (1 files)
      … 1 files under this directory
    package.json
  babel-tester/  (3 files)
    src/  (1 files)
      … 1 files under this directory
    babel-check-duplicated-nodes.d.ts
    package.json
  benchmarks/  (36 files)
    src/  (31 files)
      … 31 files under this directory
    .babelrc
    CHANGELOG.md
    README.md
    package.json
    run.js
  ssr-benchmarks/  (5 files)
    .babelrc
    basic.js
    bench.js
    package.json
    triangle.js
  test-utils/  (10 files)
    resolved-conditions/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    enzyme-env.js
    index.d.ts
    legacy-env.js
    next-env.js
    package.json
    pretty-css.js
    testSetup.js
  ensure-yarn.js
  replace-slack-link.js
site/  (34 files)
  components/  (25 files)
    live-editor/  (16 files)
      … 16 files under this directory
    carbon-ads.tsx
    container.tsx
    doc-wrapper.tsx
    global-styles.tsx
    index.ts
    markdown-css.tsx
    search.tsx
    site-header.tsx
    title.tsx
  module-stubs/  (4 files)
    README.md
    cosmiconfig.cjs
    find-root.cjs
    resolve.cjs
  .babelrc.js
  README.md
  misc.d.ts
  next-env.d.ts
  next.config.js
.editorconfig
.eslintignore
.gitattributes
.gitignore
.nvmrc
.prettierignore
.prettierrc.yaml
.yarnrc.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
RELEASING.md
SECURITY.md
babel.config.js
codecov.yml
jest-react18.config.js
jest.config.js
jest.dist.js
jest.prod.js
netlify.toml
package.json
```

## Entry points

- [scripts/babel-tester/src/index.ts](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/scripts/babel-tester/src/index.ts)
- [packages/babel-plugin-jsx-pragmatic/src/index.ts](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/babel-plugin-jsx-pragmatic/src/index.ts)
- [packages/babel-plugin/src/index.js](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/babel-plugin/src/index.js)
- [packages/babel-preset-css-prop/src/index.js](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/babel-preset-css-prop/src/index.js)
- [packages/cache/src/index.ts](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/cache/src/index.ts)
- [packages/css-prettifier/src/index.ts](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/css-prettifier/src/index.ts)
- [packages/css/src/index.ts](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/css/src/index.ts)
- [packages/eslint-plugin/src/index.ts](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/eslint-plugin/src/index.ts)
- [packages/hash/src/index.ts](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/hash/src/index.ts)
- [packages/is-prop-valid/src/index.ts](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/is-prop-valid/src/index.ts)
- [packages/jest/src/index.js](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/jest/src/index.js)
- [packages/memoize/src/index.ts](https://github.com/emotion-js/emotion/blob/b882bcba85132554992e4bd49e94c95939bbf810/packages/memoize/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 71 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 1 file(s) under flow-typed package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 2 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 364 file(s) under packages package (observed from repository paths and static analysis). |
| playgrounds package | library | Observed | Groups 6 file(s) under playgrounds package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 48 file(s) under scripts package (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 31 file(s) under site package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 76 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.codesandbox/ci.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/actions/ci-setup/action.yml` (config)
- `.github/no-response.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.prettierrc.yaml` (config)
- `.yarnrc.yml` (config)
- `codecov.yml` (config)
- `docs/docs.yaml` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `packages/babel-plugin-jsx-pragmatic/package.json` (manifest)
- `packages/babel-plugin/package.json` (manifest)
- `packages/babel-preset-css-prop/package.json` (manifest)
- `packages/cache/package.json` (manifest)
- `packages/cache/types/tsconfig.json` (config)
- `packages/cache/types/tslint.json` (config)
- `packages/css-prettifier/package.json` (manifest)
- `packages/css/create-instance/package.json` (manifest)
- `packages/css/package.json` (manifest)
- `packages/css/types/tsconfig.json` (config)
- `packages/css/types/tslint.json` (config)
- `packages/eslint-plugin/package.json` (manifest)
- `packages/hash/package.json` (manifest)
- `packages/hash/types/tsconfig.json` (config)
- `packages/hash/types/tslint.json` (config)
- `packages/is-prop-valid/package.json` (manifest)
- `packages/is-prop-valid/types/tsconfig.json` (config)
- `packages/is-prop-valid/types/tslint.json` (config)
- `packages/jest/enzyme-serializer/package.json` (manifest)
- `packages/jest/enzyme/package.json` (manifest)
- `packages/jest/package.json` (manifest)
- `packages/jest/serializer/package.json` (manifest)
- `packages/jest/types/tsconfig.json` (config)
- `packages/jest/types/tslint.json` (config)
- `packages/memoize/package.json` (manifest)
- `packages/memoize/types/tsconfig.json` (config)
- `packages/memoize/types/tslint.json` (config)
- `packages/native/package.json` (manifest)
- `packages/native/tsconfig.json` (config)
- `packages/native/types/tsconfig.json` (config)
- `packages/native/types/tslint.json` (config)
- `packages/primitives-core/package.json` (manifest)
- `packages/primitives/package.json` (manifest)
- `packages/react/_isolated-hnrs/package.json` (manifest)
- `packages/react/jsx-dev-runtime/package.json` (manifest)
- `packages/react/jsx-runtime/package.json` (manifest)
- `packages/react/package.json` (manifest)
- `packages/react/types/tsconfig.json` (config)
- `packages/react/types/tslint.json` (config)
- `packages/serialize/package.json` (manifest)
- `packages/serialize/types/tsconfig.json` (config)
- `packages/serialize/types/tslint.json` (config)
- `packages/server/create-instance/package.json` (manifest)
- `packages/server/package.json` (manifest)
- `packages/server/types/tsconfig.json` (config)
- `packages/server/types/tslint.json` (config)
- `packages/sheet/package.json` (manifest)
- `packages/sheet/types/tsconfig.json` (config)
- `packages/sheet/types/tslint.json` (config)
- `packages/styled/base/package.json` (manifest)
- `packages/styled/package.json` (manifest)
- `packages/styled/types/tsconfig.json` (config)
- `packages/styled/types/tslint.json` (config)
- `packages/unitless/package.json` (manifest)
- `packages/use-insertion-effect-with-fallbacks/package.json` (manifest)
- `packages/utils/package.json` (manifest)
- `packages/utils/types/tsconfig.json` (config)
- `packages/utils/types/tslint.json` (config)
- `packages/weak-memoize/package.json` (manifest)
- `packages/weak-memoize/types/tsconfig.json` (config)
- `packages/weak-memoize/types/tslint.json` (config)
- `playgrounds/cra/package.json` (manifest)
- `playgrounds/nextjs/package.json` (manifest)
- `scripts/babel-preset-emotion-dev/package.json` (manifest)
- `scripts/babel-tester/package.json` (manifest)
- `scripts/benchmarks/package.json` (manifest)
- `scripts/ssr-benchmarks/package.json` (manifest)
- `scripts/test-utils/package.json` (manifest)

## Top-level layout

- `packages` — 618 analysed file(s)
- `scripts` — 58 analysed file(s)
- `site` — 34 analysed file(s)
- `docs` — 32 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `playgrounds` — 15 analysed file(s)
- `.github` — 11 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.yarn` — 2 analysed file(s)
- `__mocks__` — 2 analysed file(s)
- `.codesandbox` — 1 analysed file(s)
- `flow-typed` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b882bcba85132554992e4bd49e94c95939bbf810` is the revision these paths and observations refer to.
