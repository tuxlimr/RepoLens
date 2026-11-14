# Project structure: vercel/ncc

**Analysed commit:** `cb1f1f058bfa7de4cb63f2411e14a724e714e260`

**Commit reference:** [cb1f1f058bfa7de4cb63f2411e14a724e714e260](https://github.com/vercel/ncc/commit/cb1f1f058bfa7de4cb63f2411e14a724e714e260)

**Tree at this commit:** [vercel/ncc@cb1f1f058bfa](https://github.com/vercel/ncc/tree/cb1f1f058bfa7de4cb63f2411e14a724e714e260)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vercel/ncc |
| Description | Compile a Node.js project into a single file. Supports TypeScript, binary addons, dynamic requires. |
| Stars | 9844 |
| Forks | 328 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `cb1f1f058bfa7de4cb63f2411e14a724e714e260` |
| Retrieved at | 2026-11-14T19:12:48.952930+00:00 |
| Files in this snapshot | 285 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    ci.yml
    pr.yml
  dependabot.yml
examples/  (20 files)
  hello-world/  (3 files)
    README.md
    index.js
    package.json
  multiple-bundles/  (5 files)
    README.md
    cli.js
    main.js
    main.test.js
    package.json
  programmatic/  (8 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (5 files)
      … 5 files under this directory
    README.md
    package.json
  typescript/  (4 files)
    README.md
    index.ts
    package.json
    tsconfig.json
patches/  (1 files)
  unfetch@5.0.0.patch
publish/  (1 files)
  package.json
scripts/  (1 files)
  build.js
src/  (15 files)
  loaders/  (7 files)
    empty-loader.js
    notfound-loader.js
    relocate-loader.js
    shebang-loader.js
    stringify-loader.js
    ts-loader.js
    uncacheable.js
  utils/  (4 files)
    get-package-base.js
    has-type-module.js
    ncc-cache-dir.js
    shebang.js
  @@notfound.js
  cli.js
  index.js
  typescript.js
test/  (234 files)
  binary/  (2 files)
    binding.gyp
    hello.cc
  fixtures/  (21 files)
    sourcemap-resource-path/  (3 files)
      … 3 files under this directory
    ts-error1/  (2 files)
      … 2 files under this directory
    ts-error2/  (2 files)
      … 2 files under this directory
    ts-interop/  (2 files)
      … 2 files under this directory
    type-module/  (2 files)
      … 2 files under this directory
    with-type-errors/  (2 files)
      … 2 files under this directory
    error.js
    index.html
    interop-test.mjs
    interop.cjs
    module.cjs
    no-dep.js
    test.cjs
    test.mjs
  integration/  (77 files)
    create-require-runtime/  (2 files)
      … 2 files under this directory
    include/  (1 files)
      … 1 files under this directory
    node-path/  (1 files)
      … 1 files under this directory
    analytics-node.js
    apollo.js
    auth0.js
    aws-sdk.js
    axios.js
    azure-cosmos.js
    azure-storage.js
    binary-require.js
    browserify-middleware.js
    bugsnag-js.js
    canvas.js
    chromeless.js
    core-js.js
    cowsay.js
    create-require-runtime.mjs
    create-require-runtime.mjs.stdout
    env-var.js
    es-module.js
    esm.js
    express-consolidate.js
    express.js
    fetch-h2.js
    ffmpeg.js
    firebase-admin.js
    … 49 more files
  unit/  (129 files)
    browser-mainfield/  (4 files)
      … 4 files under this directory
    bundle-subasset/  (6 files)
      … 6 files under this directory
    bundle-subasset2/  (6 files)
      … 6 files under this directory
    custom-emit/  (4 files)
      … 4 files under this directory
    double-nested-builds/  (3 files)
      … 3 files under this directory
    exports-nomodule/  (6 files)
      … 6 files under this directory
    exports-wildcard/  (6 files)
      … 6 files under this directory
    externals/  (3 files)
      … 3 files under this directory
    import-meta-cjs/  (3 files)
      … 3 files under this directory
    import-meta-esm/  (4 files)
      … 4 files under this directory
    imports/  (6 files)
      … 6 files under this directory
    minify/  (4 files)
      … 4 files under this directory
    minify-err/  (4 files)
      … 4 files under this directory
    minify-sourcemap-register/  (4 files)
      … 4 files under this directory
    minify-v8cache-sourcemap-register/  (4 files)
      … 4 files under this directory
    nested-builds/  (3 files)
      … 3 files under this directory
    runtime-notfound/  (3 files)
      … 3 files under this directory
    shebang/  (3 files)
      … 3 files under this directory
    ts-decl/  (5 files)
      … 5 files under this directory
    ts-decl-dir/  (5 files)
      … 5 files under this directory
    ts-exts/  (6 files)
      … 6 files under this directory
    ts-json-resolve/  (6 files)
      … 6 files under this directory
    ts-mixed-modules/  (5 files)
      … 5 files under this directory
    ts-target-es2018/  (4 files)
      … 4 files under this directory
    tsconfig-paths/  (5 files)
      … 5 files under this directory
    tsconfig-paths-allowjs/  (5 files)
      … 5 files under this directory
    tsconfig-paths-array-extends/  (7 files)
      … 7 files under this directory
    tsconfig-paths-conflicting-external/  (5 files)
      … 5 files under this directory
  cli.js
  cli.test.js
  integration.test.js
  unit.test.js
  watcher.test.js
.gitignore
CODE_OF_CONDUCT.md
LICENSE
jest.config.js
package-support.md
package.json
pnpm-workspace.yaml
readme.md
release.config.js
update-fixtures.sh
```

## Entry points

- [src/index.js](https://github.com/vercel/ncc/blob/cb1f1f058bfa7de4cb63f2411e14a724e714e260/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cli.js package | library | Observed | Groups 1 file(s) under cli.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| loaders package | library | Observed | Groups 7 file(s) under loaders package (observed from repository paths and static analysis). |
| @@notfound.js package | library | Observed | Groups 1 file(s) under @@notfound.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 234 file(s) under tests (observed from repository paths and static analysis). |
| typescript.js package | library | Observed | Groups 1 file(s) under typescript.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/pr.yml` (ci)
- `examples/hello-world/package.json` (manifest)
- `examples/multiple-bundles/package.json` (manifest)
- `examples/programmatic/package.json` (manifest)
- `examples/typescript/package.json` (manifest)
- `examples/typescript/tsconfig.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `publish/package.json` (manifest)

## Top-level layout

- `test` — 234 analysed file(s)
- `examples` — 20 analysed file(s)
- `src` — 15 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 3 analysed file(s)
- `patches` — 1 analysed file(s)
- `publish` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 10 file(s) were skipped during inventory (1 x lockfile excluded; 9 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `cb1f1f058bfa7de4cb63f2411e14a724e714e260` is the revision these paths and observations refer to.
