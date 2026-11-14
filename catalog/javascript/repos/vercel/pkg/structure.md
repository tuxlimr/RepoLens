# Project structure: vercel/pkg

**Analysed commit:** `9066ceeb391d9c7ba6aba650109c2fa3f8e088eb`

**Commit reference:** [9066ceeb391d9c7ba6aba650109c2fa3f8e088eb](https://github.com/vercel/pkg/commit/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb)

**Tree at this commit:** [vercel/pkg@9066ceeb391d](https://github.com/vercel/pkg/tree/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vercel/pkg |
| Description | Package your Node.js project into an executable |
| Stars | 24294 |
| Forks | 1074 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `9066ceeb391d9c7ba6aba650109c2fa3f8e088eb` |
| Retrieved at | 2026-11-14T19:11:02.917368+00:00 |
| Files in this snapshot | 703 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    01_bug_report.yml
    02_regression.yml
    config.yml
  workflows/  (2 files)
    ci.yml
    close-stale.yml
dictionary/  (236 files)
  .eslintrc.json
  angular-bridge.js
  any-promise.js
  async.js
  aws-sdk.js
  babel-core.js
  batch.js
  bcrypt.js
  better-sqlite3.js
  bignum.js
  bindings.js
  blessed.js
  body-parser.js
  browserify.js
  bson.js
  buffermaker.js
  bunyan.js
  busboy.js
  bytes.js
  callsites.js
  chokidar.js
  coffee-script.js
  colors.js
  compression.js
  … 212 more files
examples/  (6 files)
  express/  (5 files)
    views/  (2 files)
      … 2 files under this directory
    index.js
    package.json
    readme.md
  .eslintrc.json
lib/  (16 files)
  bin.ts
  chmod.ts
  common.ts
  compress_type.ts
  detector.ts
  fabricator.ts
  follow.ts
  help.ts
  index.ts
  log.js
  mach-o.ts
  packer.ts
  producer.ts
  refiner.ts
  types.ts
  walker.ts
prelude/  (3 files)
  .eslintrc.json
  bootstrap.js
  diagnostic.js
test/  (429 files)
  test-10-pnpm/  (4 files)
    .gitignore
    main.js
    package.json
    test.js
  test-11-pnpm/  (4 files)
    .gitignore
    main.js
    package.json
    test.js
  test-42-fetch-all/  (1 files)
    main.js
  test-42-path-related-values/  (3 files)
    project/  (2 files)
      … 2 files under this directory
    main.js
  test-46-input/  (2 files)
    main.js
    test-x-index
  test-46-input-js/  (2 files)
    main.js
    test-x-index.js
  test-46-input-output/  (2 files)
    main.js
    test-x-index
  test-46-input-output-js/  (2 files)
    main.js
    test-x-index.js
  test-46-input-output-js-exe/  (2 files)
    main.js
    test-x-index.js
  test-46-input-output-target/  (2 files)
    main.js
    test-x-index
  test-46-input-output-target-js/  (2 files)
    main.js
    test-x-index.js
  test-46-input-output-target-js-exe/  (2 files)
    main.js
    test-x-index.js
  test-46-input-output-targets-many/  (2 files)
    main.js
    test-x-index
  test-46-input-output-targets-many-2/  (2 files)
    main.js
    test-x-index
  test-46-input-output-targets-many-3/  (2 files)
    main.js
    test-x-index.js
  test-46-input-output-targets-many-4/  (2 files)
    main.js
    test-x-index.js
  test-46-input-output-targets-many-5/  (2 files)
    main.js
    test-x-index.js
  test-46-input-output-targets-many-6/  (2 files)
    main.js
    test-x-index.js
  test-46-input-package-json/  (3 files)
    main.js
    package.json
    test-x-index.js
  test-46-input-package-json-dir/  (3 files)
    main.js
    package.json
    test-x-index.js
  test-46-input-package-json-dir-scope/  (3 files)
    main.js
    package.json
    test-x-index.js
  test-46-input-package-json-outputdir/  (3 files)
    main.js
    package.json
    test-x-index.js
  test-46-input-package-json-target/  (3 files)
    main.js
    package.json
    test-x-index.js
  test-46-input-target/  (2 files)
    main.js
    test-x-index
  test-46-input-target-js/  (2 files)
    main.js
    test-x-index.js
  test-46-input-target-js-exe/  (2 files)
    main.js
    test-x-index.js
  test-46-input-targets-many/  (2 files)
    main.js
    test-x-index
  test-46-input-targets-many-2/  (2 files)
    main.js
    test-x-index
  test-46-input-targets-many-3/  (2 files)
    main.js
    test-x-index.js
  test-46-input-targets-many-4/  (2 files)
    main.js
    test-x-index.js
  test-46-input-targets-many-5/  (2 files)
    main.js
    test-x-index.js
  test-46-input-targets-many-6/  (2 files)
    main.js
    test-x-index.js
  test-46-multi-arch/  (2 files)
    main.js
    test-x-index.js
  test-46-multi-arch-2/  (2 files)
    main.js
    test-x-index.js
  test-46-outpath/  (2 files)
    main.js
    test-x-index
  test-46-outpath-target/  (2 files)
    main.js
    test-x-index
  test-46-outpath-targets-many/  (2 files)
    main.js
    test-x-index
  test-48-common/  (1 files)
    main.js
  test-50-api/  (2 files)
    main.js
    test-x-index.js
  test-50-arguments/  (2 files)
    main.js
    test-x-index.js
  test-50-ast-parsing/  (3 files)
    main.js
    test-x-index.js
    test-y-data.txt
  test-50-ast-parsing-2/  (2 files)
    main.js
    test-x-index.js
  test-50-bakery/  (2 files)
    main.js
    test-x-index.js
  test-50-bakery-2/  (2 files)
    main.js
    test-x-index.js
  test-50-bakery-3/  (2 files)
    main.js
    test-x-index.js
  test-50-bakery-4/  (2 files)
    main.js
    test-x-index.js
  test-50-bakery-fetch/  (1 files)
    main.js
  test-50-can-include-addon/  (3 files)
    main.js
    test-x-index.js
    time.node
  test-50-cannot-css-script/  (4 files)
    assets/  (1 files)
      … 1 files under this directory
    main.js
    package.json
    test-x-index.js
  test-50-cannot-include-df/  (2 files)
    main.js
    test-x-index.js
  test-50-chdir-env-var/  (2 files)
    source/  (1 files)
      … 1 files under this directory
    main.js
  test-50-class-to-string/  (2 files)
    main.js
    test-x-index.js
  test-50-config-log/  (2 files)
    main.js
    test-x-index.js
  test-50-console-trace/  (2 files)
    main.js
    test-x-index.js
  test-50-corrupt-executable/  (2 files)
    main.js
    test-x-index.js
  test-50-debug/  (2 files)
    main.js
    test-x-index.js
  test-50-error-source-position/  (2 files)
    main.js
    test-x-index.js
  test-50-extensions/  (5 files)
    .eslintrc.json
    main.js
    test-x-index.js
    test-y-esnext.js
    test-z-sub.js
  test-50-for-await-of/  (2 files)
    main.js
    test-x-index.js
  test-50-fs-runtime-layer/  (7 files)
    main.js
    package.json
    test-x-index.js
    test-x1-index.js
    test-x3-index.js
    test-z-asset-A.css
    test-z-asset-B.css
  test-50-fs-runtime-layer-2/  (3 files)
    main.js
    test-x-index.js
    test-z-asset.css
  test-50-fs-runtime-layer-3/  (3 files)
    main.js
    test-x-index.js
    test-z-asset.css
  test-50-global-object/  (5 files)
    main.js
    package.json
    test-x-index.js
    test-y-resolve-A.js
    test-y-resolve-B.js
  test-50-inspect/  (2 files)
    main.js
    test-x-index.js
  test-50-invalid/  (1 files)
    main.js
  test-50-invalid-package-json/  (1 files)
    main.js
  test-50-invalid-package-json-2/  (2 files)
    main.js
    test-x-index.js
  test-50-invalid-package-json-bin/  (2 files)
    main.js
    package.json
  test-50-invalid-package-json-bin-2/  (2 files)
    main.js
    package.json
  test-50-invalid-unknown-token/  (2 files)
    main.js
    test-x-index.js
  test-50-many-arrow-functions/  (3 files)
    main.js
    test-x-index.js
    test-z-creator.js
  test-50-many-callbacks/  (3 files)
    main.js
    test-x-index.js
    test-z-creator.js
  test-50-may-exclude/  (2 files)
    main.js
    test-x-index.js
  test-50-may-exclude-must-exclude/  (3 files)
    main.js
    test-x-index.js
    test-y-index.js
  test-50-module-parent/  (5 files)
    main.js
    test-x-index.js
    test-y-fish-A.js
    test-y-fish-B.js
    test-y-fish-C.js
  test-50-mountpoints/  (5 files)
    plugins-C-int/  (1 files)
      … 1 files under this directory
    plugins-D-ext/  (1 files)
      … 1 files under this directory
    main.js
    test-x-index.js
    test-y-common.js
  test-50-native-addon/  (3 files)
    lib/  (1 files)
      … 1 files under this directory
    main.js
    test-x-index.js
  test-50-native-addon-2/  (2 files)
    main.js
    test-x-index.js
  test-50-native-addon-3/  (7 files)
    lib/  (6 files)
      … 6 files under this directory
    main.js
  test-50-native-addon-4/  (3 files)
    lib/  (1 files)
      … 1 files under this directory
    main.js
    test-x-index.js
  test-50-no-signature/  (2 files)
    main.js
    test-x-index.js
  test-50-no-super-in-constructor/  (2 files)
    main.js
    test-x-index.js
  test-50-node-modules-tree/  (14 files)
    main.js
    test-x-index.js
    test-y-fish-A.js
    test-y-fish-B.js
    test-y-fish-E
    test-y-fish-F
    test-y-fish-G
    test-y-fish-H
    test-y-fish-I
    test-y-fish-J
    test-y-fish-M
    test-y-fish-N
    test-y-fish-O
    test-y-fish-P
  test-50-non-ascii/  (3 files)
    main.js
    test-x-index.js
    test-y-$$.js
  test-50-not-found-wording/  (2 files)
    main.js
    test-x-index.js
  test-50-not-found-wording-2/  (2 files)
    main.js
    test-x-index.js
  test-50-object-spread/  (2 files)
    main.js
    test-x-index.js
  test-50-observe-snapshot-root/  (2 files)
    main.js
    test-x-index.js
  test-50-observe-snapshot-root-2/  (2 files)
    main.js
    test-x-index.js
  test-50-odd-entrypoint/  (2 files)
    main.js
    test-x-index.js
  test-50-package-a-binary/  (2 files)
    main.js
    test-x-index.js
  test-50-package-json/  (6 files)
    main.js
    package.json
    test-x-index.js
    test-y-resolve-A.js
    test-y-resolve-B.txt
    test-y-resolve-C.json
  test-50-package-json-2/  (4 files)
    sub/  (1 files)
      … 1 files under this directory
    main.js
    package.json
    test-y-data.json
  test-50-package-json-3/  (4 files)
    main.js
    package.json
    test-x-index.js
    test-y-data.json
  test-50-package-json-4/  (2 files)
    main.js
    test-x-index.js
  test-50-package-json-5/  (1 files)
    main.js
  test-50-package-json-6/  (2 files)
    main.js
    test-x-index.js
  test-50-package-json-6b/  (1 files)
    main.js
  test-50-package-json-6c/  (4 files)
    beta/  (3 files)
      … 3 files under this directory
    main.js
  test-50-package-json-6d/  (2 files)
    main.js
    test-x-index.js
  test-50-package-json-7/  (3 files)
    main.js
    package.json
    test-x-index.js
  test-50-package-json-7p/  (3 files)
    main.js
    package.json
    test-x-index.js
  test-50-package-json-8/  (6 files)
    sub/  (3 files)
      … 3 files under this directory
    main.js
    package.json
    test-z-data.css
  test-50-package-json-8b/  (6 files)
    sub/  (3 files)
      … 3 files under this directory
    main.js
    package.json
    test-z-data.css
  test-50-package-json-8p/  (6 files)
    sub/  (3 files)
      … 3 files under this directory
    main.js
    package.json
    test-z-data.css
  test-50-package-json-9/  (2 files)
    main.js
    test-x-index.js
  test-50-package-json-9p/  (2 files)
    main.js
    test-x-index.js
  test-50-package-json-A/  (3 files)
    main.js
    package.json
    test-x-index.js
  test-50-path-as-buffer/  (3 files)
    main.js
    test-x-index.js
    test-z-asset.css
  test-50-path-separators/  (5 files)
    sub/  (2 files)
      … 2 files under this directory
    main.js
    package.json
    test-x-index.js
  test-50-promisify/  (2 files)
    main.js
    test-x-index.js
  test-50-public-packages/  (2 files)
    main.js
    test-x-index.js
  test-50-reproducible/  (2 files)
    main.js
    test-x-index.js
  test-50-require-edge-cases/  (5 files)
    main.js
    test-x-index.js
    test-x1-content.js
    test-x2-require-false.js
    test-x3-empty-file.js
  test-50-require-main-parent/  (6 files)
    sub/  (2 files)
      … 2 files under this directory
    main.js
    test-x-index.js
    test-y-require-A.js
    test-y-require-B.js
  test-50-require-resolve/  (13 files)
    main.js
    test-x-index.js
    test-y-resolve.any
    test-z-require-code-1.js
    test-z-require-code-2.js
    test-z-require-code-3.js
    test-z-require-code-4.js
    test-z-require-content.css
    test-z-require-json-1.json
    test-z-require-json-2.json
    test-z-require-json-3.json
    test-z-require-json-4.json
    test-z-require-json-5.json
  test-50-require-resolve-2/  (16 files)
    main.js
    test-x-index.js
    test-y-resolve-A.txt
    test-y-resolve-B.txt
    test-y-resolve-C.txt
    test-y-resolve-D.txt
    test-y-resolve-E.txt
    test-y-resolve-F.txt
    test-y-resolve-G.txt
    test-y-resolve-H.txt
    test-z-require-code-I.js
    test-z-require-code-J.js
    test-z-require-content-K.txt
    test-z-require-content-L.txt
    test-z-require-content-M.txt
    test-z-require-content-N.txt
  test-50-require-with-config/  (17 files)
    main.js
    package.json
    test-x-index.js
    test-y-resolve-A.txt
    test-y-resolve-B.txt
    test-y-resolve-C.txt
    test-y-resolve-D.txt
    test-y-resolve-E.txt
    test-y-resolve-F.txt
    test-y-resolve-G.txt
    test-y-resolve-H.txt
    test-z-require-code-I.js
    test-z-require-code-J.js
    test-z-require-content-K.txt
    test-z-require-content-L.txt
    test-z-require-content-M.txt
    test-z-require-content-N.txt
  test-50-resolve-and-nearby/  (3 files)
    main.js
    test-x-index.js
    test-y-fish
  test-50-should-disclose-package/  (2 files)
    main.js
    test-x-index.js
  test-50-signature/  (2 files)
    main.js
    test-x-index.js
  test-50-sigusr1/  (2 files)
    main.js
    test-x-index.js
  test-50-spawn/  (36 files)
    main.js
    test-cluster-child.js
    test-cluster.js
    test-cpfork-a-1.js
    test-cpfork-a-2.js
    test-cpfork-a-child.js
    test-cpfork-b-1.js
    test-cpfork-b-2.js
    test-cpfork-b-child.js
    test-exec-1.js
    test-exec-2.js
    test-exec-3.js
    test-exec-child.js
    test-execFile-child.js
    test-execFile.js
    test-execFileSync-child.js
    test-execFileSync.js
    test-execSync-1.js
    test-execSync-2.js
    test-execSync-3.js
    test-execSync-child.js
    test-node.js
    test-spawn-a-1.js
    test-spawn-a-2.js
    … 12 more files
  test-50-symlink/  (2 files)
    main.js
    test-x-index.js
  test-50-tamper-core/  (2 files)
    main.js
    test-x-index.js
  test-50-undo-patch/  (3 files)
    main.js
    test-x-index.js
    test-y-index.js
  test-77-compare-dicts-and-tests/  (1 files)
    main.js
  test-78-verify-pkg-version/  (2 files)
    main.js
    test-x-index.js
  test-79-npm/  (11 files)
    angular-bridge/  (2 files)
      … 2 files under this directory
    any-promise/  (3 files)
      … 3 files under this directory
    async/  (2 files)
      … 2 files under this directory
    aws-sdk/  (2 files)
      … 2 files under this directory
    babel-core/  (2 files)
      … 2 files under this directory
  .eslintrc.json
  .gitignore
.eslintignore
.eslintrc
.gitignore
.prettierignore
.yarnrc
LICENSE
README.md
package.json
```

## Entry points

- [examples/express/index.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/examples/express/index.js)
- [test/test-10-pnpm/test.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-10-pnpm/test.js)
- [test/test-11-pnpm/test.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-11-pnpm/test.js)
- [test/test-46-input-package-json-dir-scope/test-x-index.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-46-input-package-json-dir-scope/test-x-index.js)
- [test/test-46-input-package-json-dir/test-x-index.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-46-input-package-json-dir/test-x-index.js)
- [test/test-46-input-package-json-outputdir/test-x-index.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-46-input-package-json-outputdir/test-x-index.js)
- [test/test-46-input-package-json-target/test-x-index.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-46-input-package-json-target/test-x-index.js)
- [test/test-46-input-package-json/test-x-index.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-46-input-package-json/test-x-index.js)
- [test/test-50-cannot-css-script/test-x-index.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-50-cannot-css-script/test-x-index.js)
- [test/test-50-fs-runtime-layer/test-x-index.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-50-fs-runtime-layer/test-x-index.js)
- [test/test-50-global-object/test-x-index.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-50-global-object/test-x-index.js)
- [test/test-50-package-json-2/sub/test-x-index.js](https://github.com/vercel/pkg/blob/9066ceeb391d9c7ba6aba650109c2fa3f8e088eb/test/test-50-package-json-2/sub/test-x-index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dictionary package | library | Observed | Groups 235 file(s) under dictionary package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 16 file(s) under lib package (observed from repository paths and static analysis). |
| prelude package | library | Observed | Groups 2 file(s) under prelude package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 429 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/01_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/02_regression.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/close-stale.yml` (ci)
- `dictionary/.eslintrc.json` (config)
- `examples/.eslintrc.json` (config)
- `examples/express/package.json` (manifest)
- `package.json` (manifest)
- `prelude/.eslintrc.json` (config)

## Top-level layout

- `test` — 429 analysed file(s)
- `dictionary` — 236 analysed file(s)
- `lib` — 16 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `examples` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `prelude` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 97 file(s) were skipped during inventory (97 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `9066ceeb391d9c7ba6aba650109c2fa3f8e088eb` is the revision these paths and observations refer to.
