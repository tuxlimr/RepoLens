# Project structure: evanw/esbuild

**Analysed commit:** `f6058f8364fe7ab91ca57a83e02577ed74c9cae4`

**Commit reference:** [f6058f8364fe7ab91ca57a83e02577ed74c9cae4](https://github.com/evanw/esbuild/commit/f6058f8364fe7ab91ca57a83e02577ed74c9cae4)

**Tree at this commit:** [evanw/esbuild@f6058f8364fe](https://github.com/evanw/esbuild/tree/f6058f8364fe7ab91ca57a83e02577ed74c9cae4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | evanw/esbuild |
| Description | An extremely fast bundler for the web |
| Stars | 40133 |
| Forks | 1380 |
| Licence | MIT |
| Language | Go |
| Default branch | main |
| Analysed commit | `f6058f8364fe7ab91ca57a83e02577ed74c9cae4` |
| Retrieved at | 2026-11-14T19:12:59.974958+00:00 |
| Files in this snapshot | 322 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (1 files)
    new-issue.md
  workflows/  (4 files)
    ci.yml
    e2e.yml
    publish.yml
    validate.yml
cmd/  (7 files)
  esbuild/  (7 files)
    main.go
    main_other.go
    main_wasm.go
    service.go
    service_test.go
    stdio_protocol.go
    version.go
compat-table/  (11 files)
  src/  (7 files)
    caniuse.ts
    compat-table.ts
    css_table.ts
    index.ts
    js_table.ts
    mdn.ts
    types.d.ts
  .gitignore
  README.md
  package.json
  tsconfig.json
docs/  (2 files)
  architecture.md
  development.md
images/  (5 files)
  benchmark-dark.svg
  benchmark-light.svg
  logo.svg
  wordmark-dark.svg
  wordmark-light.svg
internal/  (149 files)
  api_helpers/  (1 files)
    use_timer.go
  ast/  (1 files)
    ast.go
  bundler/  (1 files)
    bundler.go
  bundler_tests/  (28 files)
    snapshots/  (14 files)
      … 14 files under this directory
    bundler_css_test.go
    bundler_dce_test.go
    bundler_glob_test.go
    bundler_importphase_test.go
    bundler_importstar_test.go
    bundler_importstar_ts_test.go
    bundler_loader_test.go
    bundler_lower_test.go
    bundler_packagejson_test.go
    bundler_splitting_test.go
    bundler_test.go
    bundler_ts_test.go
    bundler_tsconfig_test.go
    bundler_yarnpnp_test.go
  cache/  (3 files)
    cache.go
    cache_ast.go
    cache_fs.go
  cli_helpers/  (1 files)
    cli_helpers.go
  compat/  (4 files)
    compat.go
    compat_test.go
    css_table.go
    js_table.go
  config/  (2 files)
    config.go
    globals.go
  css_ast/  (2 files)
    css_ast.go
    css_decl_table.go
  css_lexer/  (2 files)
    css_lexer.go
    css_lexer_test.go
  css_parser/  (20 files)
    css_color_spaces.go
    css_decls.go
    css_decls_animation.go
    css_decls_border_radius.go
    css_decls_box.go
    css_decls_box_shadow.go
    css_decls_color.go
    css_decls_composes.go
    css_decls_container.go
    css_decls_font.go
    css_decls_font_family.go
    css_decls_font_weight.go
    css_decls_gradient.go
    css_decls_list_style.go
    css_decls_transform.go
    css_nesting.go
    css_parser.go
    css_parser_media.go
    css_parser_selector.go
    css_reduce_calc.go
  css_printer/  (2 files)
    css_printer.go
    css_printer_test.go
  fs/  (13 files)
    error_other.go
    error_wasm+windows.go
    filepath.go
    fs.go
    fs_mock.go
    fs_mock_test.go
    fs_real.go
    fs_zip.go
    iswin_other.go
    iswin_wasm.go
    iswin_windows.go
    modkey_other.go
    modkey_unix.go
  graph/  (3 files)
    graph.go
    input.go
    meta.go
  helpers/  (18 files)
    bitset.go
    comment.go
    dataurl.go
    dataurl_test.go
    float.go
    glob.go
    hash.go
    joiner.go
    mime.go
    path.go
    quote.go
    serializer.go
    stack.go
    strings.go
    timer.go
    typos.go
    utf.go
    waitgroup.go
  js_ast/  (5 files)
    js_ast.go
    js_ast_helpers.go
    js_ast_test.go
    js_ident.go
    unicode.go
  js_lexer/  (3 files)
    js_lexer.go
    js_lexer_test.go
    tables.go
  js_parser/  (9 files)
    global_name_parser.go
    js_parser_lower.go
    js_parser_lower_class.go
    js_parser_lower_test.go
    json_parser.go
    json_parser_test.go
    sourcemap_parser.go
    ts_parser.go
    ts_parser_test.go
  js_printer/  (2 files)
    js_printer.go
    js_printer_test.go
  linker/  (1 files)
    debug.go
  logger/  (11 files)
    logger.go
    logger_darwin.go
    logger_linux.go
    logger_other.go
    logger_test.go
    logger_windows.go
    msg_ids.go
    style.go
    style_clang.go
    style_default.go
    style_visualstudio.go
  renamer/  (1 files)
    renamer.go
  resolver/  (7 files)
    dataurl.go
    package_json.go
    resolver.go
    testExpectations.json
    tsconfig_json.go
    yarnpnp.go
    yarnpnp_test.go
  runtime/  (2 files)
    runtime.go
    runtime_test.go
  sourcemap/  (1 files)
    sourcemap.go
  test/  (2 files)
    diff.go
    util.go
  xxhash/  (4 files)
    LICENSE.txt
    README.md
    xxhash.go
    xxhash_other.go
lib/  (15 files)
  npm/  (5 files)
    browser.ts
    node-install.ts
    node-platform.ts
    node-shim.ts
    node.ts
  shared/  (5 files)
    common.ts
    stdio_protocol.ts
    types.ts
    uint8array_json_parser.ts
    worker.ts
  README.md
  package.json
  tsconfig-deno.json
  tsconfig-nolib.json
  tsconfig.json
npm/  (61 files)
  @esbuild/  (54 files)
    aix-ppc64/  (2 files)
      … 2 files under this directory
    android-arm/  (2 files)
      … 2 files under this directory
    android-arm64/  (2 files)
      … 2 files under this directory
    android-x64/  (2 files)
      … 2 files under this directory
    darwin-arm64/  (2 files)
      … 2 files under this directory
    darwin-x64/  (2 files)
      … 2 files under this directory
    freebsd-arm64/  (2 files)
      … 2 files under this directory
    freebsd-x64/  (2 files)
      … 2 files under this directory
    linux-arm/  (2 files)
      … 2 files under this directory
    linux-arm64/  (2 files)
      … 2 files under this directory
    linux-ia32/  (2 files)
      … 2 files under this directory
    linux-loong64/  (2 files)
      … 2 files under this directory
    linux-mips64el/  (2 files)
      … 2 files under this directory
    linux-ppc64/  (2 files)
      … 2 files under this directory
    linux-riscv64/  (2 files)
      … 2 files under this directory
    linux-s390x/  (2 files)
      … 2 files under this directory
    linux-x64/  (2 files)
      … 2 files under this directory
    netbsd-arm64/  (2 files)
      … 2 files under this directory
    netbsd-x64/  (2 files)
      … 2 files under this directory
    openbsd-arm64/  (2 files)
      … 2 files under this directory
    openbsd-x64/  (2 files)
      … 2 files under this directory
    openharmony-arm64/  (2 files)
      … 2 files under this directory
    sunos-x64/  (2 files)
      … 2 files under this directory
    wasi-preview1/  (2 files)
      … 2 files under this directory
    win32-arm64/  (2 files)
      … 2 files under this directory
    win32-ia32/  (2 files)
      … 2 files under this directory
    win32-x64/  (2 files)
      … 2 files under this directory
  esbuild/  (3 files)
    LICENSE.md
    README.md
    package.json
  esbuild-wasm/  (4 files)
    bin/  (1 files)
      … 1 files under this directory
    LICENSE.md
    README.md
    package.json
pkg/  (13 files)
  api/  (9 files)
    api.go
    api_impl.go
    api_impl_test.go
    api_js_table.go
    api_test.go
    favicon.go
    serve_other.go
    serve_wasm.go
    watcher.go
  cli/  (4 files)
    cli.go
    cli_impl.go
    cli_js_table.go
    mangle_cache.go
require/  (13 files)
  old-ts/  (2 files)
    README.md
    package.json
  parcel2/  (2 files)
    .terserrc
    package.json
  rollup/  (1 files)
    package.json
  webpack5/  (1 files)
    package.json
  yarnpnp/  (7 files)
    bar/  (1 files)
      … 1 files under this directory
    foo/  (2 files)
      … 2 files under this directory
    .gitignore
    in.mjs
    package.json
    tsconfig.json
scripts/  (26 files)
  browser/  (3 files)
    browser-tests.js
    index.html
    package.json
  dataurl-escapes.html
  decorator-tests.ts
  destructuring-fuzzer.js
  esbuild.js
  gen-unicode-table.js
  gradient-tests.css
  gradient-tests.html
  graph-debugger.html
  node-unref-tests.js
  package.json
  parse-ts-files.js
  plugin-tests.js
  register-test.js
  terser-tests.js
  test-yarnpnp.js
  test262-async.js
  test262.js
  try.html
  ts-type-tests.js
  tsconfig.json
  uglify-tests.js
  verify-source-map.js
  wasm-tests.js
.editorconfig
.gitignore
CHANGELOG-2024.md
CHANGELOG-2025.md
CHANGELOG.md
LICENSE.md
Makefile
README.md
RUNBOOK.md
dl.sh
go.mod
go.sum
go.version
staticcheck.conf
version.txt
```

## Entry points

- [compat-table/src/index.ts](https://github.com/evanw/esbuild/blob/f6058f8364fe7ab91ca57a83e02577ed74c9cae4/compat-table/src/index.ts)
- [require/yarnpnp/bar/index.js](https://github.com/evanw/esbuild/blob/f6058f8364fe7ab91ca57a83e02577ed74c9cae4/require/yarnpnp/bar/index.js)
- [require/yarnpnp/foo/index.js](https://github.com/evanw/esbuild/blob/f6058f8364fe7ab91ca57a83e02577ed74c9cae4/require/yarnpnp/foo/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). |
| cmd package | library | Observed | Groups 7 file(s) under cmd package (observed from repository paths and static analysis). |
| compat-table package | library | Observed | Groups 7 file(s) under compat-table package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 49 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 128 file(s) under internal package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 10 file(s) under lib package (observed from repository paths and static analysis). |
| pkg package | library | Observed | Groups 4 file(s) under pkg package (observed from repository paths and static analysis). |
| require package | library | Observed | Groups 3 file(s) under require package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 17 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/e2e.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/validate.yml` (ci)
- `compat-table/package.json` (manifest)
- `compat-table/tsconfig.json` (config)
- `go.mod` (manifest)
- `internal/resolver/testExpectations.json` (config)
- `lib/package.json` (manifest)
- `lib/tsconfig-deno.json` (config)
- `lib/tsconfig-nolib.json` (config)
- `lib/tsconfig.json` (config)
- `npm/@esbuild/aix-ppc64/package.json` (manifest)
- `npm/@esbuild/android-arm/package.json` (manifest)
- `npm/@esbuild/android-arm64/package.json` (manifest)
- `npm/@esbuild/android-x64/package.json` (manifest)
- `npm/@esbuild/darwin-arm64/package.json` (manifest)
- `npm/@esbuild/darwin-x64/package.json` (manifest)
- `npm/@esbuild/freebsd-arm64/package.json` (manifest)
- `npm/@esbuild/freebsd-x64/package.json` (manifest)
- `npm/@esbuild/linux-arm/package.json` (manifest)
- `npm/@esbuild/linux-arm64/package.json` (manifest)
- `npm/@esbuild/linux-ia32/package.json` (manifest)
- `npm/@esbuild/linux-loong64/package.json` (manifest)
- `npm/@esbuild/linux-mips64el/package.json` (manifest)
- `npm/@esbuild/linux-ppc64/package.json` (manifest)
- `npm/@esbuild/linux-riscv64/package.json` (manifest)
- `npm/@esbuild/linux-s390x/package.json` (manifest)
- `npm/@esbuild/linux-x64/package.json` (manifest)
- `npm/@esbuild/netbsd-arm64/package.json` (manifest)
- `npm/@esbuild/netbsd-x64/package.json` (manifest)
- `npm/@esbuild/openbsd-arm64/package.json` (manifest)
- `npm/@esbuild/openbsd-x64/package.json` (manifest)
- `npm/@esbuild/openharmony-arm64/package.json` (manifest)
- `npm/@esbuild/sunos-x64/package.json` (manifest)
- `npm/@esbuild/wasi-preview1/package.json` (manifest)
- `npm/@esbuild/win32-arm64/package.json` (manifest)
- `npm/@esbuild/win32-ia32/package.json` (manifest)
- `npm/@esbuild/win32-x64/package.json` (manifest)
- `npm/esbuild-wasm/package.json` (manifest)
- `npm/esbuild/package.json` (manifest)
- `require/old-ts/package.json` (manifest)
- `require/parcel2/package.json` (manifest)
- `require/rollup/package.json` (manifest)
- `require/webpack5/package.json` (manifest)
- `require/yarnpnp/foo/package.json` (manifest)
- `require/yarnpnp/package.json` (manifest)
- `require/yarnpnp/tsconfig.json` (config)
- `scripts/browser/package.json` (manifest)
- `scripts/package.json` (manifest)
- `scripts/tsconfig.json` (config)

## Top-level layout

- `internal` — 149 analysed file(s)
- `npm` — 61 analysed file(s)
- `scripts` — 26 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `lib` — 15 analysed file(s)
- `pkg` — 13 analysed file(s)
- `require` — 13 analysed file(s)
- `compat-table` — 11 analysed file(s)
- `cmd` — 7 analysed file(s)
- `.github` — 5 analysed file(s)
- `images` — 5 analysed file(s)
- `docs` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (8 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f6058f8364fe7ab91ca57a83e02577ed74c9cae4` is the revision these paths and observations refer to.
