# Project structure: browserify/browserify

**Analysed commit:** `cd60f059d7a8432f2c3acea7d4dfcb81b97e7a3d`

**Commit reference:** [cd60f059d7a8432f2c3acea7d4dfcb81b97e7a3d](https://github.com/browserify/browserify/commit/cd60f059d7a8432f2c3acea7d4dfcb81b97e7a3d)

**Tree at this commit:** [browserify/browserify@cd60f059d7a8](https://github.com/browserify/browserify/tree/cd60f059d7a8432f2c3acea7d4dfcb81b97e7a3d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | browserify/browserify |
| Description | browser-side require() the node.js way |
| Stars | 14690 |
| Forks | 1201 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `cd60f059d7a8432f2c3acea7d4dfcb81b97e7a3d` |
| Retrieved at | 2026-11-14T19:11:43.535155+00:00 |
| Files in this snapshot | 433 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (6 files)
    node-aught.yml
    node-pretest.yml
    node-tens.yml
    node-twenties.yml
    rebase.yml
    require-allow-edits.yml
bin/  (4 files)
  advanced.txt
  args.js
  cmd.js
  usage.txt
example/  (16 files)
  api/  (4 files)
    browser/  (3 files)
      … 3 files under this directory
    build.js
  multiple_bundles/  (6 files)
    static/  (2 files)
      … 2 files under this directory
    beep.js
    boop.js
    build.sh
    robot.js
  source_maps/  (6 files)
    js/  (3 files)
      … 3 files under this directory
    build.js
    build.sh
    index.html
lib/  (2 files)
  _empty.js
  builtins.js
test/  (394 files)
  array/  (3 files)
    one.js
    three.js
    two.js
  async/  (1 files)
    src.js
  bare/  (2 files)
    dirname-filename.js
    main.js
  bin_tr_error/  (2 files)
    main.js
    tr.js
  bom/  (1 files)
    hello.js
  browser_field_file/  (2 files)
    package.json
    wow.js
  browser_field_resolve/  (33 files)
    a/  (2 files)
      … 2 files under this directory
    b/  (3 files)
      … 3 files under this directory
    c/  (3 files)
      … 3 files under this directory
    d/  (3 files)
      … 3 files under this directory
    e/  (3 files)
      … 3 files under this directory
    f/  (3 files)
      … 3 files under this directory
    g/  (3 files)
      … 3 files under this directory
    h/  (3 files)
      … 3 files under this directory
    i/  (4 files)
      … 4 files under this directory
    j/  (4 files)
      … 4 files under this directory
    k/  (1 files)
      … 1 files under this directory
    l/  (1 files)
      … 1 files under this directory
  bundle-bundle-external/  (3 files)
    bar.js
    baz.js
    foo.js
  bundle_external/  (3 files)
    boop.js
    main.js
    robot.js
  catch/  (1 files)
    main.js
  circular/  (3 files)
    a.js
    b.js
    main.js
  coffee_bin/  (2 files)
    main.coffee
    x.coffee
  coffeeify/  (1 files)
    main.coffee
  comment/  (1 files)
    main.js
  cycle/  (6 files)
    mod1/  (2 files)
      … 2 files under this directory
    mod2/  (2 files)
      … 2 files under this directory
    README.md
    entry.js
  debug_standalone/  (1 files)
    x.js
  delay/  (2 files)
    diverted.js
    main.js
  dollar/  (1 files)
    dollar/  (1 files)
      … 1 files under this directory
  double_buffer/  (3 files)
    explicit.js
    implicit.js
    main.js
  double_bundle_error/  (6 files)
    main.js
    needs_three.js
    one.js
    package.json
    three.js
    two.js
  double_bundle_json/  (3 files)
    a.json
    b.json
    index.js
  dup/  (3 files)
    foo-dup.js
    foo.js
    index.js
  entry/  (6 files)
    main.js
    needs_three.js
    one.js
    package.json
    three.js
    two.js
  entry_exec/  (2 files)
    fail.js
    main.js
  entry_expose/  (1 files)
    main.js
  error_code/  (1 files)
    src.js
  exclude/  (3 files)
    array.js
    skip.js
    skip2.js
  export/  (1 files)
    entry.js
  external/  (2 files)
    main.js
    x.js
  external_args/  (1 files)
    main.js
  external_shim/  (4 files)
    bundle1.js
    bundle2.js
    package.json
    shim.js
  externalize/  (3 files)
    beep.js
    boop.js
    robot.js
  fake/  (2 files)
    fake_fs.js
    main.js
  field/  (4 files)
    miss.js
    object.js
    string.js
    sub.js
  glob/  (3 files)
    lib/  (1 files)
      … 1 files under this directory
    a.js
    b.js
  global/  (4 files)
    buffer.js
    filename.js
    main.js
    tick.js
  global_recorder/  (1 files)
    main.js
  hash/  (5 files)
    foo/  (2 files)
      … 2 files under this directory
    main.js
    one.js
    other.js
  hash_instance_context/  (17 files)
    one/  (4 files)
      … 4 files under this directory
    three/  (6 files)
      … 6 files under this directory
    two/  (6 files)
      … 6 files under this directory
    main.js
  identical/  (3 files)
    main.js
    x.js
    y.js
  identical_different/  (3 files)
    wow/  (1 files)
      … 1 files under this directory
    main.js
    x.js
  ignore/  (11 files)
    double-skip/  (2 files)
      … 2 files under this directory
    ignored/  (1 files)
      … 1 files under this directory
    relative/  (1 files)
      … 1 files under this directory
    array.js
    by-id.js
    by-relative.js
    double-skip.js
    main.js
    skip.js
    skip2.js
  ignore_browser_field/  (1 files)
    main.js
  ignore_missing/  (1 files)
    main.js
  ignore_transform_key/  (1 files)
    main.js
  json/  (6 files)
    beep.json
    evil-chars.json
    evil.js
    invalid.js
    invalid.json
    main.js
  maxlisteners/  (1 files)
    main.js
  multi_bundle/  (4 files)
    _prelude.js
    a.js
    b.js
    c.js
  multi_entry/  (3 files)
    a.js
    b.js
    c.js
  multi_entry_cross_require/  (3 files)
    lib/  (1 files)
      … 1 files under this directory
    a.js
    c.js
  multi_require/  (2 files)
    a.js
    main.js
  multi_symlink/  (2 files)
    main.js
    x.js
  no_builtins/  (4 files)
    extra/  (2 files)
      … 2 files under this directory
    main.js
    x.txt
  noparse/  (4 files)
    dir1/  (2 files)
      … 2 files under this directory
    a.js
    b.js
  paths/  (5 files)
    x/  (2 files)
      … 2 files under this directory
    y/  (2 files)
      … 2 files under this directory
    main.js
  pipeline_deps/  (4 files)
    bar.js
    foo.js
    main.js
    xyz.js
  pkg/  (2 files)
    main.js
    package.json
  pkg_event/  (2 files)
    main.js
    package.json
  plugin/  (1 files)
    main.js
  preserve_symlinks/  (2 files)
    a/  (1 files)
      … 1 files under this directory
    b/  (1 files)
      … 1 files under this directory
  process/  (3 files)
    main.js
    one.js
    two.js
  quotes/  (5 files)
    backtick.js
    main.js
    one.js
    three.js
    two.js
  relative_dedupe/  (8 files)
    a/  (3 files)
      … 3 files under this directory
    b/  (3 files)
      … 3 files under this directory
    index.js
    main.js
  require_expose/  (2 files)
    main.js
    some_dep.js
  resolve_exposed/  (3 files)
    y/  (1 files)
      … 1 files under this directory
    main.js
    x.js
  reverse_multi_bundle/  (4 files)
    app.js
    arbitrary.js
    lazy.js
    shared.js
  shared_symlink/  (3 files)
    app/  (1 files)
      … 1 files under this directory
    shared/  (1 files)
      … 1 files under this directory
    main.js
  shebang/  (2 files)
    foo.js
    main.js
  spread/  (1 files)
    main.js
  standalone/  (3 files)
    main.js
    one.js
    two.js
  stream/  (3 files)
    bar.js
    foo.js
    main.js
  subdep/  (2 files)
    index.js
    package.json
  symlink_dedupe/  (3 files)
    one/  (2 files)
      … 2 files under this directory
    main.js
  syntax_cache/  (2 files)
    invalid.js
    valid.js
  tr/  (4 files)
    subdir/  (1 files)
      … 1 files under this directory
    f.js
    main.js
    package.json
  tr_args/  (2 files)
    main.js
    tr.js
  tr_global/  (1 files)
    main.js
  tr_no_entry/  (1 files)
    main.js
  tr_once/  (1 files)
    main.js
  tr_order/  (2 files)
    replace_aaa.js
    replace_bbb.js
  tr_symlink/  (5 files)
    a-module/  (1 files)
      … 1 files under this directory
    app/  (2 files)
      … 2 files under this directory
    b-module/  (2 files)
      … 2 files under this directory
  unicode/  (3 files)
    main.js
    one.js
    two.js
  yield/  (2 files)
    f.js
    main.js
  _versions.js
  args.js
  array.js
  async.js
  backbone.js
  bare.js
  bare_shebang.js
  bin.js
  bin_entry.js
  bin_tr_error.js
  bom.js
  browser_field_file.js
  browser_field_resolve.js
  buffer.js
  bundle-bundle-external.js
  bundle-stream.js
  bundle.js
  bundle_external.js
  bundle_external_global.js
  bundle_sourcemap.js
  catch.js
  circular.js
  coffee_bin.js
  coffeeify.js
  … 97 more files
.gitignore
.nvmrc
LICENSE
appveyor.yml
changelog.markdown
code-of-conduct.md
eslint.config.mjs
index.js
package.json
readme.markdown
security.md
```

## Entry points

- [index.js](https://github.com/browserify/browserify/blob/cd60f059d7a8432f2c3acea7d4dfcb81b97e7a3d/index.js)
- [bin/cmd.js](https://github.com/browserify/browserify/blob/cd60f059d7a8432f2c3acea7d4dfcb81b97e7a3d/bin/cmd.js)
- [test/subdep/index.js](https://github.com/browserify/browserify/blob/cd60f059d7a8432f2c3acea7d4dfcb81b97e7a3d/test/subdep/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 2 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 394 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/node-aught.yml` (ci)
- `.github/workflows/node-pretest.yml` (ci)
- `.github/workflows/node-tens.yml` (ci)
- `.github/workflows/node-twenties.yml` (ci)
- `.github/workflows/rebase.yml` (ci)
- `.github/workflows/require-allow-edits.yml` (ci)
- `appveyor.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 394 analysed file(s)
- `example` — 16 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 6 analysed file(s)
- `bin` — 4 analysed file(s)
- `lib` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 74 file(s) were skipped during inventory (1 x likely secret file excluded; 73 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `cd60f059d7a8432f2c3acea7d4dfcb81b97e7a3d` is the revision these paths and observations refer to.
