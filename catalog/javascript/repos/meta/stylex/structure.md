# Project structure: meta/stylex

**Analysed commit:** `6d7464dee9374f3ab99ddd37ae4de3accdc53ba3`

**Commit reference:** [6d7464dee9374f3ab99ddd37ae4de3accdc53ba3](https://github.com/meta/stylex/commit/6d7464dee9374f3ab99ddd37ae4de3accdc53ba3)

**Tree at this commit:** [meta/stylex@6d7464dee937](https://github.com/meta/stylex/tree/6d7464dee9374f3ab99ddd37ae4de3accdc53ba3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | meta/stylex |
| Description | StyleX is the styling system for ambitious user interfaces. |
| Stars | 10495 |
| Forks | 511 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `6d7464dee9374f3ab99ddd37ae4de3accdc53ba3` |
| Retrieved at | 2026-11-14T19:12:38.745174+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (2 files)
    bug.yml
    feature.yml
  workflows/  (4 files)
    benchmarks.yml
    publish.yml
    tests.yml
    typos.toml
  CODEOWNERS
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
  copilot-instructions.md
  dependabot.yml
.vscode/  (2 files)
  extensions.json
  settings.json
examples/  (214 files)
  example-bun/  (13 files)
    scripts/  (3 files)
      … 3 files under this directory
    src/  (6 files)
      … 6 files under this directory
    .eslintrc.js
    README.md
    bunfig.toml
    package.json
  example-cli/  (13 files)
    source/  (8 files)
      … 8 files under this directory
    .gitignore
    .stylex.json5
    README.md
    package.json
    tsconfig.json
  example-esbuild/  (8 files)
    public/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    .eslintrc.js
    README.md
    package.json
  example-nextjs/  (27 files)
    app/  (12 files)
      … 12 files under this directory
    components/  (5 files)
      … 5 files under this directory
    public/  (2 files)
      … 2 files under this directory
    .eslintrc.js
    .gitignore
    README.md
    babel.config.js
    next.config.js
    package.json
    postcss.config.js
    tsconfig.json
  example-react-router/  (17 files)
    src/  (11 files)
      … 11 files under this directory
    .gitignore
    README.md
    package.json
    server.js
    tsconfig.json
    vite.config.ts
  example-redwoodsdk/  (24 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (11 files)
      … 11 files under this directory
    types/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    eslint.config.cjs
    package.json
    tsconfig.json
    vite.config.mts
    worker-configuration.d.ts
    wrangler.jsonc
  example-rollup/  (8 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    babel.config.mjs
    eslint.config.cjs
    index.html
    package.json
    rollup.config.mjs
  example-rspack/  (8 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    eslint.config.cjs
    package.json
    rspack.config.js
  example-storybook/  (15 files)
    .storybook/  (3 files)
      … 3 files under this directory
    stories/  (5 files)
      … 5 files under this directory
    .babelrc.cjs
    README.md
    eslint.config.mjs
    package.json
    postcss.config.mjs
    vite-storybook.config.ts
    vitest.config.ts
  example-sveltekit/  (14 files)
    src/  (6 files)
      … 6 files under this directory
    static/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    eslint.config.js
    package.json
    svelte.config.js
    tsconfig.json
    vite.config.ts
  example-vite/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    README.md
    eslint.config.cjs
    index.html
    package.json
    vite.config.mjs
  example-vite-react/  (14 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    eslint.config.js
    index.html
    package.json
    tsconfig.app.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  example-vite-rsc/  (16 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    README.md
    eslint.config.cjs
    package.json
    tsconfig.json
    vite.config.ts
  example-waku/  (16 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    README.md
    eslint.config.cjs
    package.json
    tsconfig.json
    waku.config.ts
  example-webpack/  (13 files)
    src/  (7 files)
      … 7 files under this directory
    .babelrc.js
    .eslintrc.js
    README.md
    index.html
    package.json
    webpack.config.js
flow-typed/  (87 files)
  environments/  (7 files)
    bom.js
    cssom.js
    dom.js
    html.js
    jsx.js
    node.js
    streams.js
  npm/  (77 files)
    @babel/  (13 files)
      … 13 files under this directory
    @chromatic-com/  (1 files)
      … 1 files under this directory
    @csstools/  (1 files)
      … 1 files under this directory
    ansis_vx.x.x.js
    autoprefixer_vx.x.x.js
    babel-loader_vx.x.x.js
    benchmark_vx.x.x.js
    brotli-size_vx.x.x.js
    chalk_v4.x.x.js
    clean-css_vx.x.x.js
    clsx_v1.x.x.js
    codemirror_vx.x.x.js
    colors_v1.x.x.js
    cross-env_vx.x.x.js
    css-loader_vx.x.x.js
    css-mediaquery_vx.x.x.js
    css-shorthand-expand_vx.x.x.js
    esbuild_vx.x.x.js
    estree.js
    fast-glob_vx.x.x.js
    fb-watchman_vx.x.x.js
    file-loader_vx.x.x.js
    flow-bin_v0.x.x.js
    flow-enums-runtime_v0.x.x.js
    glob-parent_vx.x.x.js
    html-webpack-plugin_vx.x.x.js
    husky_vx.x.x.js
    … 38 more files
  babel-plugins.js
  flow-api-translator.js
  stubs.js
packages/  (473 files)
  @stylexjs/  (425 files)
    atoms/  (8 files)
      … 8 files under this directory
    babel-plugin/  (137 files)
      … 137 files under this directory
    cli/  (33 files)
      … 33 files under this directory
    create-stylex-app/  (8 files)
      … 8 files under this directory
    devtools-extension/  (85 files)
      … 85 files under this directory
    eslint-plugin/  (60 files)
      … 60 files under this directory
    postcss-plugin/  (21 files)
      … 21 files under this directory
    rollup-plugin/  (10 files)
      … 10 files under this directory
    shared/  (4 files)
      … 4 files under this directory
    stylex/  (29 files)
      … 29 files under this directory
    unplugin/  (30 files)
      … 30 files under this directory
  benchmarks/  (16 files)
    perf/  (10 files)
      … 10 files under this directory
    size/  (4 files)
      … 4 files under this directory
    compare.js
    package.json
  compiler-conformance/  (32 files)
    __tests__/  (1 files)
      … 1 files under this directory
    fixtures/  (25 files)
      … 25 files under this directory
    src/  (3 files)
      … 3 files under this directory
    README.md
    jest.config.cjs
    package.json
.eslintrc.js
.flowconfig
.gitignore
.nvmrc
.prettierignore
.watchmanconfig
CHANGELOG.md
LICENSE
README.md
flow-typed.config.json
package.json
```

## Entry points

- [examples/example-bun/src/App.jsx](https://github.com/meta/stylex/blob/6d7464dee9374f3ab99ddd37ae4de3accdc53ba3/examples/example-bun/src/App.jsx)
- [examples/example-esbuild/src/App.jsx](https://github.com/meta/stylex/blob/6d7464dee9374f3ab99ddd37ae4de3accdc53ba3/examples/example-esbuild/src/App.jsx)
- [packages/@stylexjs/atoms/src/index.js](https://github.com/meta/stylex/blob/6d7464dee9374f3ab99ddd37ae4de3accdc53ba3/packages/%40stylexjs/atoms/src/index.js)
- [packages/@stylexjs/postcss-plugin/src/index.js](https://github.com/meta/stylex/blob/6d7464dee9374f3ab99ddd37ae4de3accdc53ba3/packages/%40stylexjs/postcss-plugin/src/index.js)
- [packages/compiler-conformance/src/index.js](https://github.com/meta/stylex/blob/6d7464dee9374f3ab99ddd37ae4de3accdc53ba3/packages/compiler-conformance/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 38 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 87 file(s) under flow-typed package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 398 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/feature.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/benchmarks.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/typos.toml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `examples/example-bun/bunfig.toml` (config)
- `examples/example-bun/package.json` (manifest)
- `examples/example-cli/package.json` (manifest)
- `examples/example-cli/tsconfig.json` (config)
- `examples/example-esbuild/package.json` (manifest)
- `examples/example-nextjs/package.json` (manifest)
- `examples/example-nextjs/tsconfig.json` (config)
- `examples/example-react-router/package.json` (manifest)
- `examples/example-react-router/tsconfig.json` (config)
- `examples/example-redwoodsdk/package.json` (manifest)
- `examples/example-redwoodsdk/tsconfig.json` (config)
- `examples/example-rollup/package.json` (manifest)
- `examples/example-rspack/package.json` (manifest)
- `examples/example-storybook/package.json` (manifest)
- `examples/example-sveltekit/package.json` (manifest)
- `examples/example-sveltekit/tsconfig.json` (config)
- `examples/example-vite-react/package.json` (manifest)
- `examples/example-vite-react/tsconfig.app.json` (config)
- `examples/example-vite-react/tsconfig.json` (config)
- `examples/example-vite-react/tsconfig.node.json` (config)
- `examples/example-vite-rsc/package.json` (manifest)
- `examples/example-vite-rsc/tsconfig.json` (config)
- `examples/example-vite/package.json` (manifest)
- `examples/example-waku/package.json` (manifest)
- `examples/example-waku/tsconfig.json` (config)
- `examples/example-webpack/package.json` (manifest)
- `flow-typed.config.json` (config)
- `package.json` (manifest)
- `packages/@stylexjs/atoms/package.json` (manifest)
- `packages/@stylexjs/babel-plugin/package.json` (manifest)
- `packages/@stylexjs/cli/package.json` (manifest)
- `packages/@stylexjs/create-stylex-app/package.json` (manifest)
- `packages/@stylexjs/create-stylex-app/templates.json` (config)
- `packages/@stylexjs/devtools-extension/manifests/base.json` (config)
- `packages/@stylexjs/devtools-extension/manifests/chrome.json` (config)
- `packages/@stylexjs/devtools-extension/manifests/firefox.json` (config)
- `packages/@stylexjs/devtools-extension/manifests/safari.json` (config)
- `packages/@stylexjs/devtools-extension/package.json` (manifest)
- `packages/@stylexjs/eslint-plugin/package.json` (manifest)
- `packages/@stylexjs/postcss-plugin/__tests__/__auto_discovery_fixtures__/package.json` (manifest)
- `packages/@stylexjs/postcss-plugin/package.json` (manifest)
- `packages/@stylexjs/rollup-plugin/__tests__/__fixtures__/.babelrc.json` (config)
- `packages/@stylexjs/rollup-plugin/package.json` (manifest)
- `packages/@stylexjs/shared/package.json` (manifest)
- `packages/@stylexjs/stylex/package.json` (manifest)
- `packages/@stylexjs/unplugin/package.json` (manifest)
- `packages/benchmarks/package.json` (manifest)
- `packages/compiler-conformance/fixtures/create-basic/expected.json` (config)
- `packages/compiler-conformance/fixtures/create-basic/manifest.json` (config)
- `packages/compiler-conformance/fixtures/define-vars-theme/expected.json` (config)
- `packages/compiler-conformance/fixtures/define-vars-theme/manifest.json` (config)
- `packages/compiler-conformance/fixtures/keyframes-and-when/expected.json` (config)
- `packages/compiler-conformance/fixtures/keyframes-and-when/manifest.json` (config)
- `packages/compiler-conformance/fixtures/options-warning/expected.json` (config)
- `packages/compiler-conformance/fixtures/options-warning/manifest.json` (config)
- `packages/compiler-conformance/fixtures/props-and-merge/expected.json` (config)
- `packages/compiler-conformance/fixtures/props-and-merge/manifest.json` (config)
- `packages/compiler-conformance/fixtures/runtime-injection/expected.json` (config)
- `packages/compiler-conformance/fixtures/runtime-injection/manifest.json` (config)
- `packages/compiler-conformance/fixtures/strip-stylex-import-extension/expected.json` (config)
- `packages/compiler-conformance/fixtures/strip-stylex-import-extension/manifest.json` (config)
- `packages/compiler-conformance/fixtures/validation-error/expected.json` (config)
- `packages/compiler-conformance/fixtures/validation-error/manifest.json` (config)
- `packages/compiler-conformance/package.json` (manifest)

## Top-level layout

- `packages` — 473 analysed file(s)
- `examples` — 214 analysed file(s)
- `flow-typed` — 87 analysed file(s)
- `.github` — 12 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6d7464dee9374f3ab99ddd37ae4de3accdc53ba3` is the revision these paths and observations refer to.
