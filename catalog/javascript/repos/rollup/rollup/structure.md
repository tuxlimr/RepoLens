# Project structure: rollup/rollup

**Analysed commit:** `0c5497fb4d86cc769380d4945574488113e08ac2`

**Commit reference:** [0c5497fb4d86cc769380d4945574488113e08ac2](https://github.com/rollup/rollup/commit/0c5497fb4d86cc769380d4945574488113e08ac2)

**Tree at this commit:** [rollup/rollup@0c5497fb4d86](https://github.com/rollup/rollup/tree/0c5497fb4d86cc769380d4945574488113e08ac2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | rollup/rollup |
| Description | Next-generation ES module bundler |
| Stars | 26305 |
| Forks | 1905 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `0c5497fb4d86cc769380d4945574488113e08ac2` |
| Retrieved at | 2026-11-14T19:10:56.051419+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.agents/  (1 files)
  skills/  (1 files)
    generate-repl-links/  (1 files)
      … 1 files under this directory
.github/  (20 files)
  ISSUE_TEMPLATE/  (5 files)
    SUPPORT.md
    bug.yaml
    docs.yaml
    feature.yaml
    modification.yaml
  actions/  (2 files)
    install-and-cache-node-deps/  (1 files)
      … 1 files under this directory
    prepare-build-artifacts/  (1 files)
      … 1 files under this directory
  scripts/  (1 files)
    install-apt-packages.sh
  workflows/  (7 files)
    build-and-tests.yml
    clean-cache.yml
    copilot-review.yml
    pr-artefacts-authorize.yml
    pr-artefacts-build.yml
    pr-artefacts-publish.yml
    pr-testing-instructions.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  labels.json
.husky/  (1 files)
  pre-commit
.vscode/  (2 files)
  launch.json
  settings.json
browser/  (10 files)
  src/  (8 files)
    error.ts
    fs.ts
    hookActions.ts
    initWasm.ts
    path.ts
    performance.ts
    process.ts
    wasm.ts
  LICENSE.md
  package.json
build-plugins/  (15 files)
  add-cli-entry.ts
  aliases.ts
  chokidar-readdir-throttle-replacement.ts
  clean-before-write.ts
  copy-types.ts
  emit-module-package-file.ts
  emit-native-entry.ts
  emit-wasm-file.ts
  esm-dynamic-import.ts
  external-native-import.ts
  fs-events-replacement.ts
  generate-license-file.ts
  get-banner.ts
  load-cli-help.ts
  replace-browser-modules.ts
cli/  (17 files)
  run/  (14 files)
    batchWarnings.ts
    build.ts
    commandPlugins.ts
    getConfigPath.ts
    index.ts
    loadConfigFile.ts
    loadConfigFileType.d.ts
    loadConfigFromCommand.ts
    resetScreen.ts
    stdin.ts
    timings.ts
    waitForInput.ts
    watch-cli.ts
    watchHooks.ts
  cli.ts
  help.md
  logging.ts
docs/  (97 files)
  .vitepress/  (14 files)
    graphs/  (2 files)
      … 2 files under this directory
    theme/  (2 files)
      … 2 files under this directory
    config.ts
    create-examples.ts
    helpers.ts
    legacy-slugs.json
    mermaid.config.json
    mermaid.ts
    puppeteer-config.json
    replace-path-picomatch.ts
    transpose-tables.ts
    verify-anchors.ts
  browser/  (1 files)
    index.md
  command-line-interface/  (1 files)
    index.md
  configuration-options/  (1 files)
    index.md
  es-module-syntax/  (1 files)
    index.md
  faqs/  (1 files)
    index.md
  guide/  (3 files)
    en/  (2 files)
      … 2 files under this directory
    en.md
  introduction/  (1 files)
    index.md
  javascript-api/  (1 files)
    index.md
  migration/  (1 files)
    index.md
  plugin-development/  (1 files)
    index.md
  public/  (4 files)
    llms.txt
    manifest.json
    rollup-logo.svg
    vitejs-logo.svg
  repl/  (57 files)
    components/  (11 files)
      … 11 files under this directory
    examples/  (30 files)
      … 30 files under this directory
    font/  (1 files)
      … 1 files under this directory
    helpers/  (6 files)
      … 6 files under this directory
    images/  (2 files)
      … 2 files under this directory
    stores/  (6 files)
      … 6 files under this directory
    index.md
  tools/  (1 files)
    index.md
  troubleshooting/  (1 files)
    index.md
  tutorial/  (1 files)
    index.md
  AGENTS.md
  CLAUDE.md
  declarations.d.ts
  index.md
  package.json
  tsconfig.json
  types.d.ts
npm/  (52 files)
  android-arm-eabi/  (2 files)
    README.md
    package.json
  android-arm64/  (2 files)
    README.md
    package.json
  android-x64/  (2 files)
    README.md
    package.json
  darwin-arm64/  (2 files)
    README.md
    package.json
  darwin-x64/  (2 files)
    README.md
    package.json
  freebsd-arm64/  (2 files)
    README.md
    package.json
  freebsd-x64/  (2 files)
    README.md
    package.json
  linux-arm-gnueabihf/  (2 files)
    README.md
    package.json
  linux-arm-musleabihf/  (2 files)
    README.md
    package.json
  linux-arm64-gnu/  (2 files)
    README.md
    package.json
  linux-arm64-musl/  (2 files)
    README.md
    package.json
  linux-loong64-gnu/  (2 files)
    README.md
    package.json
  linux-loong64-musl/  (2 files)
    README.md
    package.json
  linux-ppc64-gnu/  (2 files)
    README.md
    package.json
  linux-ppc64-musl/  (2 files)
    README.md
    package.json
  linux-riscv64-gnu/  (2 files)
    README.md
    package.json
  linux-riscv64-musl/  (2 files)
    README.md
    package.json
  linux-s390x-gnu/  (2 files)
    README.md
    package.json
  linux-x64-gnu/  (2 files)
    README.md
    package.json
  linux-x64-musl/  (2 files)
    README.md
    package.json
  openbsd-x64/  (2 files)
    README.md
    package.json
  openharmony-arm64/  (2 files)
    README.md
    package.json
  win32-arm64-msvc/  (2 files)
    README.md
    package.json
  win32-ia32-msvc/  (2 files)
    README.md
    package.json
  win32-x64-gnu/  (2 files)
    README.md
    package.json
  win32-x64-msvc/  (2 files)
    README.md
    package.json
patches/  (3 files)
  @types+rimraf+3.0.2.patch
  @vueuse+core+12.8.2.patch
  vitepress+1.6.4.patch
rust/  (124 files)
  .cargo/  (1 files)
    config.toml
  bindings_napi/  (4 files)
    .cargo/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    Cargo.toml
    build.rs
  bindings_wasm/  (3 files)
    .cargo/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
    Cargo.toml
  parse_ast/  (110 files)
    src/  (109 files)
      … 109 files under this directory
    Cargo.toml
  xxhash/  (2 files)
    src/  (1 files)
      … 1 files under this directory
    Cargo.toml
  AGENTS.md
  CLAUDE.md
  Cargo.toml
  rustfmt.toml
scripts/  (33 files)
  perf-report/  (3 files)
    index.js
    report-collector.js
    rollup-artefacts.js
  ast-types.js
  check-release.js
  colors.js
  coverage-flush.cjs
  coverage.sh
  declarations.d.ts
  generate-ast-converters.js
  generate-ast-macros.js
  generate-buffer-parsers.js
  generate-buffer-to-ast.js
  generate-child-node-keys.js
  generate-node-index.js
  generate-node-types.js
  generate-rust-constants.js
  generate-string-constants.js
  helpers.js
  lint-native-js.js
  package.json
  postpublish.js
  prepare-release.js
  prepublish.js
  publish-wasm-node-package.js
  release-constants.js
  release-helpers.js
  … 6 more files
src/  (276 files)
  ast/  (155 files)
    nodes/  (116 files)
      … 116 files under this directory
    scopes/  (12 files)
      … 12 files under this directory
    utils/  (7 files)
      … 7 files under this directory
    variables/  (13 files)
      … 13 files under this directory
    DeoptimizableEntity.ts
    Entity.ts
    ExecutionContext.ts
    NodeInteractions.ts
    bufferParsers.ts
    childNodeKeys.ts
    values.ts
  finalisers/  (18 files)
    shared/  (11 files)
      … 11 files under this directory
    amd.ts
    cjs.ts
    es.ts
    iife.ts
    index.ts
    system.ts
    umd.ts
  rollup/  (2 files)
    rollup.ts
    types.d.ts
  utils/  (85 files)
    options/  (4 files)
      … 4 files under this directory
    FileEmitter.ts
    PluginCache.ts
    PluginContext.ts
    PluginDriver.ts
    Queue.ts
    RESERVED_NAMES.ts
    addons.ts
    astConverterHelpers.ts
    asyncFlatten.ts
    base64.ts
    blank.ts
    bufferToAst.ts
    buildPhase.ts
    chunkAssignment.ts
    collapseSourcemaps.ts
    colors.ts
    commondir.ts
    convert-ast-strings.ts
    crypto.ts
    decodedSourcemap.ts
    deconflictChunk.ts
    doNothing.ts
    ensureArray.ts
    escapeId.ts
    … 57 more files
  watch/  (5 files)
    WatchEmitter.ts
    fileWatcher.ts
    fsevents-importer.ts
    watch-proxy.ts
    watch.ts
  AGENTS.md
  Bundle.ts
  CLAUDE.md
  Chunk.ts
  ExternalChunk.ts
  ExternalModule.ts
  Graph.ts
  Module.ts
  ModuleLoader.ts
  browser-entry.ts
  node-entry.ts
test/  (114 files)
  browser/  (40 files)
    samples/  (36 files)
      … 36 files under this directory
    ast-buffer.js
    define.d.ts
    index.js
    tsconfig.json
  chunking-form/  (72 files)
    samples/  (70 files)
      … 70 files under this directory
    define.d.ts
    index.js
  AGENTS.md
  CLAUDE.md
.editorconfig
.gitattributes
.gitignore
.lintstagedrc.js
.nycrc
.prettierignore
.prettierrc.json
.tool-versions
AGENTS.md
ARCHITECTURE.md
CHANGELOG-0.md
CHANGELOG-1.md
CHANGELOG-2.md
CHANGELOG-3.md
CHANGELOG.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
FUNDING.json
LICENSE-CORE.md
LICENSE.md
README.md
SECURITY.md
audit-resolve.json
… 10 more files
```

## Entry points

- [cli/run/index.ts](https://github.com/rollup/rollup/blob/0c5497fb4d86cc769380d4945574488113e08ac2/cli/run/index.ts)
- [scripts/perf-report/index.js](https://github.com/rollup/rollup/blob/0c5497fb4d86cc769380d4945574488113e08ac2/scripts/perf-report/index.js)
- [src/ast/nodes/index.ts](https://github.com/rollup/rollup/blob/0c5497fb4d86cc769380d4945574488113e08ac2/src/ast/nodes/index.ts)
- [src/finalisers/index.ts](https://github.com/rollup/rollup/blob/0c5497fb4d86cc769380d4945574488113e08ac2/src/finalisers/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ast package | library | Observed | Groups 155 file(s) under ast package (observed from repository paths and static analysis). |
| browser package | library | Observed | Groups 8 file(s) under browser package (observed from repository paths and static analysis). |
| browser-entry.ts package | library | Observed | Groups 1 file(s) under browser-entry.ts package (observed from repository paths and static analysis). |
| build-plugins package | library | Observed | Groups 15 file(s) under build-plugins package (observed from repository paths and static analysis). |
| Bundle.ts package | library | Observed | Groups 1 file(s) under bundle.ts package (observed from repository paths and static analysis). |
| Chunk.ts package | library | Observed | Groups 1 file(s) under chunk.ts package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 16 file(s) under cli package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 45 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| ExternalChunk.ts package | library | Observed | Groups 1 file(s) under externalchunk.ts package (observed from repository paths and static analysis). |
| ExternalModule.ts package | library | Observed | Groups 1 file(s) under externalmodule.ts package (observed from repository paths and static analysis). |
| finalisers package | library | Observed | Groups 18 file(s) under finalisers package (observed from repository paths and static analysis). |
| Graph.ts package | library | Observed | Groups 1 file(s) under graph.ts package (observed from repository paths and static analysis). |
| Module.ts package | library | Observed | Groups 1 file(s) under module.ts package (observed from repository paths and static analysis). |
| ModuleLoader.ts package | library | Observed | Groups 1 file(s) under moduleloader.ts package (observed from repository paths and static analysis). |
| node-entry.ts package | library | Observed | Groups 1 file(s) under node-entry.ts package (observed from repository paths and static analysis). |
| rollup package | library | Observed | Groups 2 file(s) under rollup package (observed from repository paths and static analysis). |
| rust package | library | Observed | Groups 113 file(s) under rust package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 31 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 114 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 85 file(s) under utils package (observed from repository paths and static analysis). |
| watch package | library | Observed | Groups 5 file(s) under watch package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug.yaml` (config)
- `.github/ISSUE_TEMPLATE/docs.yaml` (config)
- `.github/ISSUE_TEMPLATE/feature.yaml` (config)
- `.github/ISSUE_TEMPLATE/modification.yaml` (config)
- `.github/actions/install-and-cache-node-deps/action.yml` (config)
- `.github/actions/prepare-build-artifacts/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/labels.json` (config)
- `.github/workflows/build-and-tests.yml` (ci)
- `.github/workflows/clean-cache.yml` (ci)
- `.github/workflows/copilot-review.yml` (ci)
- `.github/workflows/pr-artefacts-authorize.yml` (ci)
- `.github/workflows/pr-artefacts-build.yml` (ci)
- `.github/workflows/pr-artefacts-publish.yml` (ci)
- `.github/workflows/pr-testing-instructions.yml` (ci)
- `.prettierrc.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `FUNDING.json` (config)
- `audit-resolve.json` (config)
- `browser/package.json` (manifest)
- `codecov.yml` (config)
- `docs/.vitepress/legacy-slugs.json` (config)
- `docs/.vitepress/mermaid.config.json` (config)
- `docs/.vitepress/puppeteer-config.json` (config)
- `docs/guide/en/slugs-and-pages-by-legacy-slugs.json` (config)
- `docs/package.json` (manifest)
- `docs/public/manifest.json` (config)
- `docs/repl/examples/00/example.json` (config)
- `docs/repl/examples/01/example.json` (config)
- `docs/repl/examples/02/example.json` (config)
- `docs/repl/examples/03/example.json` (config)
- `docs/repl/examples/04/example.json` (config)
- `docs/repl/examples/05/example.json` (config)
- `docs/repl/examples/06/example.json` (config)
- `docs/repl/examples/07/example.json` (config)
- `docs/repl/examples/08/example.json` (config)
- `docs/tsconfig.json` (config)
- `markdownlint.json` (config)
- `npm/android-arm-eabi/package.json` (manifest)
- `npm/android-arm64/package.json` (manifest)
- `npm/android-x64/package.json` (manifest)
- `npm/darwin-arm64/package.json` (manifest)
- `npm/darwin-x64/package.json` (manifest)
- `npm/freebsd-arm64/package.json` (manifest)
- `npm/freebsd-x64/package.json` (manifest)
- `npm/linux-arm-gnueabihf/package.json` (manifest)
- `npm/linux-arm-musleabihf/package.json` (manifest)
- `npm/linux-arm64-gnu/package.json` (manifest)
- `npm/linux-arm64-musl/package.json` (manifest)
- `npm/linux-loong64-gnu/package.json` (manifest)
- `npm/linux-loong64-musl/package.json` (manifest)
- `npm/linux-ppc64-gnu/package.json` (manifest)
- `npm/linux-ppc64-musl/package.json` (manifest)
- `npm/linux-riscv64-gnu/package.json` (manifest)
- `npm/linux-riscv64-musl/package.json` (manifest)
- `npm/linux-s390x-gnu/package.json` (manifest)
- `npm/linux-x64-gnu/package.json` (manifest)
- `npm/linux-x64-musl/package.json` (manifest)
- `npm/openbsd-x64/package.json` (manifest)
- `npm/openharmony-arm64/package.json` (manifest)
- `npm/win32-arm64-msvc/package.json` (manifest)
- `npm/win32-ia32-msvc/package.json` (manifest)
- `npm/win32-x64-gnu/package.json` (manifest)
- `npm/win32-x64-msvc/package.json` (manifest)
- `package.json` (manifest)
- `renovate.json` (config)
- `rust-toolchain.toml` (config)
- `rust/.cargo/config.toml` (config)
- `rust/Cargo.toml` (manifest)
- `rust/bindings_napi/.cargo/config.toml` (config)
- `rust/bindings_napi/Cargo.toml` (manifest)
- `rust/bindings_wasm/.cargo/config.toml` (config)
- `rust/bindings_wasm/Cargo.toml` (manifest)
- `rust/parse_ast/Cargo.toml` (manifest)
- `rust/rustfmt.toml` (config)
- `rust/xxhash/Cargo.toml` (manifest)
- `scripts/package.json` (manifest)
- `scripts/tsconfig.json` (config)

## Top-level layout

- `src` — 276 analysed file(s)
- `rust` — 124 analysed file(s)
- `test` — 114 analysed file(s)
- `docs` — 97 analysed file(s)
- `npm` — 52 analysed file(s)
- `(root files)` — 34 analysed file(s)
- `scripts` — 33 analysed file(s)
- `.github` — 20 analysed file(s)
- `cli` — 17 analysed file(s)
- `build-plugins` — 15 analysed file(s)
- `browser` — 10 analysed file(s)
- `patches` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0c5497fb4d86cc769380d4945574488113e08ac2` is the revision these paths and observations refer to.
