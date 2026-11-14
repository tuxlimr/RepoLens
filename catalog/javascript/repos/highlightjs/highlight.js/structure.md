# Project structure: highlightjs/highlight.js

**Analysed commit:** `35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c`

**Commit reference:** [35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c](https://github.com/highlightjs/highlight.js/commit/35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c)

**Tree at this commit:** [highlightjs/highlight.js@35f98874f935](https://github.com/highlightjs/highlight.js/tree/35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | highlightjs/highlight.js |
| Description | JavaScript syntax highlighter with language auto-detection and zero dependencies. |
| Stars | 25016 |
| Forks | 3757 |
| Licence | BSD-3-Clause |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c` |
| Retrieved at | 2026-11-14T19:11:02.494660+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (4 files)
    1_incorrect-syntax-highlighting.md
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (5 files)
    lint.yml
    release.yml
    size_report_comment.yml
    size_report_create.yml
    tests.js.yml
  dependabot.yml
  pull_request_template.md
demo/  (4 files)
  demo.js
  index.html
  readme.md
  style.css
docs/  (20 files)
  _build/  (1 files)
    .gitkeep
  _static/  (2 files)
    .gitkeep
    custom.css
  _templates/  (1 files)
    .gitkeep
  Makefile
  ai-contributions.md
  api.rst
  building-testing.rst
  conf.py
  css-classes-reference.rst
  index.rst
  language-contribution.rst
  language-guide.rst
  language-requests.rst
  line-numbers.rst
  mode-reference.rst
  plugin-api.rst
  plugin-recipes.rst
  requirements.txt
  theme-guide.rst
extra/  (2 files)
  .keep
  3RD_PARTY_QUICK_START.md
src/  (481 files)
  languages/  (199 files)
    lib/  (5 files)
      … 5 files under this directory
    1c.js
    abnf.js
    accesslog.js
    actionscript.js
    ada.js
    angelscript.js
    apache.js
    applescript.js
    arcade.js
    arduino.js
    armasm.js
    asciidoc.js
    aspectj.js
    autohotkey.js
    autoit.js
    avrasm.js
    awk.js
    axapta.js
    bash.js
    basic.js
    bnf.js
    brainfuck.js
    c.js
    cal.js
    … 170 more files
  lib/  (13 files)
    ext/  (1 files)
      … 1 files under this directory
    exts/  (1 files)
      … 1 files under this directory
    compile_keywords.js
    compiler_extensions.js
    html_injection_error.js
    html_renderer.js
    logger.js
    mode_compiler.js
    modes.js
    regex.js
    response.js
    token_tree.js
    utils.js
  styles/  (266 files)
    base16/  (176 files)
      … 176 files under this directory
    1c-light.css
    a11y-dark.css
    a11y-light.css
    agate.css
    an-old-hope.css
    androidstudio.css
    arduino-light.css
    arta.css
    ascetic.css
    atom-one-dark-reasonable.css
    atom-one-dark.css
    atom-one-light.css
    brown-paper.css
    codepen-embed.css
    color-brewer.css
    cybertopia-cherry.css
    cybertopia-dimmer.css
    cybertopia-icecap.css
    cybertopia-saturated.css
    dark.css
    default.css
    devibeans.css
    docco.css
    equinox.css
    … 66 more files
  core.d.ts
  highlight.js
  stub.js
test/  (256 files)
  api/  (15 files)
    autoDetection.js
    beginKeywords.js
    binaryNumber.js
    cNumber.js
    getLanguage.js
    highlight.js
    ident.js
    index.js
    keywords.js
    multiClassMatch.js
    number.js
    registerAlias.js
    starters.js
    underscoreIdent.js
    unregisterLanguage.js
  browser/  (5 files)
    highlight_block_callbacks.js
    index.js
    plain.js
    test_case.js
    worker.js
  builds/  (7 files)
    browser_build_as_commonjs.js
    cdn_build_as_esm.mjs
    node_build_as_esm.mjs
    package.js
    rollup_import_cdn_build_esm.mjs
    rollup_import_node_build_esm.mjs
    rollup_import_via_commonjs.mjs
  detect/  (200 files)
    1c/  (1 files)
      … 1 files under this directory
    abnf/  (1 files)
      … 1 files under this directory
    accesslog/  (1 files)
      … 1 files under this directory
    actionscript/  (1 files)
      … 1 files under this directory
    ada/  (1 files)
      … 1 files under this directory
    angelscript/  (1 files)
      … 1 files under this directory
    apache/  (1 files)
      … 1 files under this directory
    applescript/  (1 files)
      … 1 files under this directory
    arcade/  (1 files)
      … 1 files under this directory
    arduino/  (1 files)
      … 1 files under this directory
    armasm/  (1 files)
      … 1 files under this directory
    asciidoc/  (1 files)
      … 1 files under this directory
    aspectj/  (1 files)
      … 1 files under this directory
    autohotkey/  (1 files)
      … 1 files under this directory
    autoit/  (1 files)
      … 1 files under this directory
    avrasm/  (1 files)
      … 1 files under this directory
    awk/  (1 files)
      … 1 files under this directory
    axapta/  (1 files)
      … 1 files under this directory
    bash/  (1 files)
      … 1 files under this directory
    basic/  (1 files)
      … 1 files under this directory
    bnf/  (1 files)
      … 1 files under this directory
    brainfuck/  (1 files)
      … 1 files under this directory
    cal/  (1 files)
      … 1 files under this directory
    capnproto/  (1 files)
      … 1 files under this directory
    ceylon/  (1 files)
      … 1 files under this directory
    clean/  (1 files)
      … 1 files under this directory
    clojure/  (1 files)
      … 1 files under this directory
    clojure-repl/  (1 files)
      … 1 files under this directory
    cmake/  (1 files)
      … 1 files under this directory
    coffeescript/  (1 files)
      … 1 files under this directory
    coq/  (1 files)
      … 1 files under this directory
    cos/  (1 files)
      … 1 files under this directory
    cpp/  (1 files)
      … 1 files under this directory
    crmsh/  (1 files)
      … 1 files under this directory
    crystal/  (1 files)
      … 1 files under this directory
    csharp/  (1 files)
      … 1 files under this directory
    csp/  (1 files)
      … 1 files under this directory
    css/  (1 files)
      … 1 files under this directory
    d/  (1 files)
      … 1 files under this directory
    dart/  (1 files)
      … 1 files under this directory
    delphi/  (1 files)
      … 1 files under this directory
    diff/  (1 files)
      … 1 files under this directory
    django/  (1 files)
      … 1 files under this directory
    dns/  (1 files)
      … 1 files under this directory
    dockerfile/  (1 files)
      … 1 files under this directory
    dos/  (1 files)
      … 1 files under this directory
    dsconfig/  (1 files)
      … 1 files under this directory
    dts/  (1 files)
      … 1 files under this directory
    dust/  (1 files)
      … 1 files under this directory
    ebnf/  (1 files)
      … 1 files under this directory
    elixir/  (1 files)
      … 1 files under this directory
    elm/  (1 files)
      … 1 files under this directory
    erb/  (1 files)
      … 1 files under this directory
    erlang/  (1 files)
      … 1 files under this directory
    erlang-repl/  (1 files)
      … 1 files under this directory
    excel/  (1 files)
      … 1 files under this directory
    fix/  (1 files)
      … 1 files under this directory
    flix/  (1 files)
      … 1 files under this directory
    fortran/  (1 files)
      … 1 files under this directory
    fsharp/  (1 files)
      … 1 files under this directory
    gams/  (1 files)
      … 1 files under this directory
    gauss/  (1 files)
      … 1 files under this directory
    gcode/  (1 files)
      … 1 files under this directory
    gherkin/  (1 files)
      … 1 files under this directory
    glsl/  (1 files)
      … 1 files under this directory
    gml/  (1 files)
      … 1 files under this directory
    go/  (2 files)
      … 2 files under this directory
    golo/  (1 files)
      … 1 files under this directory
    gradle/  (1 files)
      … 1 files under this directory
    graphql/  (1 files)
      … 1 files under this directory
    groovy/  (1 files)
      … 1 files under this directory
    haml/  (1 files)
      … 1 files under this directory
    handlebars/  (1 files)
      … 1 files under this directory
    haskell/  (1 files)
      … 1 files under this directory
    haxe/  (1 files)
      … 1 files under this directory
    hsp/  (1 files)
      … 1 files under this directory
    http/  (1 files)
      … 1 files under this directory
    hy/  (1 files)
      … 1 files under this directory
    inform7/  (1 files)
      … 1 files under this directory
    ini/  (1 files)
      … 1 files under this directory
    irpf90/  (1 files)
      … 1 files under this directory
    isbl/  (1 files)
      … 1 files under this directory
    java/  (1 files)
      … 1 files under this directory
    javascript/  (3 files)
      … 3 files under this directory
    jboss-cli/  (1 files)
      … 1 files under this directory
    json/  (1 files)
      … 1 files under this directory
    json5/  (1 files)
      … 1 files under this directory
    julia/  (1 files)
      … 1 files under this directory
    julia-repl/  (1 files)
      … 1 files under this directory
    kotlin/  (1 files)
      … 1 files under this directory
    lasso/  (1 files)
      … 1 files under this directory
    latex/  (1 files)
      … 1 files under this directory
    ldif/  (1 files)
      … 1 files under this directory
    leaf/  (1 files)
      … 1 files under this directory
    less/  (1 files)
      … 1 files under this directory
    lisp/  (1 files)
      … 1 files under this directory
    livecodeserver/  (1 files)
      … 1 files under this directory
    livescript/  (1 files)
      … 1 files under this directory
    llvm/  (1 files)
      … 1 files under this directory
    lsl/  (1 files)
      … 1 files under this directory
    lua/  (1 files)
      … 1 files under this directory
    makefile/  (1 files)
      … 1 files under this directory
    markdown/  (1 files)
      … 1 files under this directory
    mathematica/  (1 files)
      … 1 files under this directory
    matlab/  (1 files)
      … 1 files under this directory
    maxima/  (1 files)
      … 1 files under this directory
    mel/  (1 files)
      … 1 files under this directory
    mercury/  (1 files)
      … 1 files under this directory
    mipsasm/  (1 files)
      … 1 files under this directory
    mizar/  (1 files)
      … 1 files under this directory
    mojolicious/  (1 files)
      … 1 files under this directory
    monkey/  (1 files)
      … 1 files under this directory
    moonscript/  (1 files)
      … 1 files under this directory
    n1ql/  (1 files)
      … 1 files under this directory
    nestedtext/  (1 files)
      … 1 files under this directory
    nginx/  (1 files)
      … 1 files under this directory
    nim/  (1 files)
      … 1 files under this directory
    nix/  (1 files)
      … 1 files under this directory
    node-repl/  (1 files)
      … 1 files under this directory
    nsis/  (1 files)
      … 1 files under this directory
    objectivec/  (1 files)
      … 1 files under this directory
    ocaml/  (1 files)
      … 1 files under this directory
    odin/  (1 files)
      … 1 files under this directory
    openscad/  (1 files)
      … 1 files under this directory
    oxygene/  (1 files)
      … 1 files under this directory
    parser3/  (1 files)
      … 1 files under this directory
    perl/  (1 files)
      … 1 files under this directory
    pf/  (1 files)
      … 1 files under this directory
    pgsql/  (1 files)
      … 1 files under this directory
    php/  (1 files)
      … 1 files under this directory
    php-template/  (1 files)
      … 1 files under this directory
    plaintext/  (1 files)
      … 1 files under this directory
    pony/  (1 files)
      … 1 files under this directory
    powershell/  (1 files)
      … 1 files under this directory
    processing/  (1 files)
      … 1 files under this directory
    profile/  (1 files)
      … 1 files under this directory
    prolog/  (1 files)
      … 1 files under this directory
    properties/  (1 files)
      … 1 files under this directory
    protobuf/  (1 files)
      … 1 files under this directory
    puppet/  (1 files)
      … 1 files under this directory
    purebasic/  (1 files)
      … 1 files under this directory
    python/  (1 files)
      … 1 files under this directory
    python-repl/  (1 files)
      … 1 files under this directory
    q/  (1 files)
      … 1 files under this directory
    qml/  (1 files)
      … 1 files under this directory
    r/  (1 files)
      … 1 files under this directory
    reasonml/  (1 files)
      … 1 files under this directory
    rib/  (1 files)
      … 1 files under this directory
    roboconf/  (1 files)
      … 1 files under this directory
    routeros/  (1 files)
      … 1 files under this directory
    rsl/  (1 files)
      … 1 files under this directory
    ruby/  (2 files)
      … 2 files under this directory
    ruleslanguage/  (1 files)
      … 1 files under this directory
    rust/  (1 files)
      … 1 files under this directory
    sas/  (1 files)
      … 1 files under this directory
    scala/  (1 files)
      … 1 files under this directory
    scheme/  (1 files)
      … 1 files under this directory
    scilab/  (1 files)
      … 1 files under this directory
    scss/  (1 files)
      … 1 files under this directory
    shell/  (1 files)
      … 1 files under this directory
    smali/  (1 files)
      … 1 files under this directory
    smalltalk/  (1 files)
      … 1 files under this directory
    sml/  (1 files)
      … 1 files under this directory
    sqf/  (1 files)
      … 1 files under this directory
    sql/  (1 files)
      … 1 files under this directory
    stan/  (1 files)
      … 1 files under this directory
    stata/  (1 files)
      … 1 files under this directory
    step21/  (1 files)
      … 1 files under this directory
    stylus/  (1 files)
      … 1 files under this directory
    subunit/  (1 files)
      … 1 files under this directory
    swift/  (1 files)
      … 1 files under this directory
    taggerscript/  (1 files)
      … 1 files under this directory
    tap/  (1 files)
      … 1 files under this directory
    tcl/  (1 files)
      … 1 files under this directory
    thrift/  (1 files)
      … 1 files under this directory
    tp/  (1 files)
      … 1 files under this directory
    twig/  (1 files)
      … 1 files under this directory
    typescript/  (1 files)
      … 1 files under this directory
    vala/  (1 files)
      … 1 files under this directory
    vbnet/  (1 files)
      … 1 files under this directory
    vbscript/  (1 files)
      … 1 files under this directory
    vbscript-html/  (1 files)
      … 1 files under this directory
    verilog/  (1 files)
      … 1 files under this directory
    vhdl/  (1 files)
      … 1 files under this directory
    vim/  (1 files)
      … 1 files under this directory
    wasm/  (1 files)
      … 1 files under this directory
    wren/  (1 files)
      … 1 files under this directory
    x86asm/  (1 files)
      … 1 files under this directory
    xl/  (1 files)
      … 1 files under this directory
    xml/  (3 files)
      … 3 files under this directory
    xquery/  (1 files)
      … 1 files under this directory
    yaml/  (1 files)
      … 1 files under this directory
    zephir/  (1 files)
      … 1 files under this directory
    index.js
  fixtures/  (8 files)
    expect/  (6 files)
      … 6 files under this directory
    index.html
    nested.js
  markup/  (20 files)
    1c/  (4 files)
      … 4 files under this directory
    abnf/  (2 files)
      … 2 files under this directory
    accesslog/  (2 files)
      … 2 files under this directory
    actionscript/  (2 files)
      … 2 files under this directory
    ada/  (2 files)
      … 2 files under this directory
    angelscript/  (2 files)
      … 2 files under this directory
    apache/  (2 files)
      … 2 files under this directory
    applescript/  (2 files)
      … 2 files under this directory
    arcade/  (2 files)
      … 2 files under this directory
  index.js
.dockerignore
.editorconfig
.eslintrc.js
.eslintrc.lang.js
.git-blame-ignore-revs
.gitattributes
.gitignore
.mocharc.json
.readthedocs.yaml
.tokeignore
AGENTS.md
CHANGES.md
CONTRIBUTING.md
CONTRIBUTORS.md
Dockerfile
LICENSE
MAINTAINERS_GUIDE.md
NOTICE.txt
README.CDN.md
README.md
SECURITY.md
SUPPORTED_LANGUAGES.md
VERSION_10_BREAKING_CHANGES.md
VERSION_10_UPGRADE.md
… 2 more files
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| core.d.ts package | library | Observed | Groups 1 file(s) under core.d.ts package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 1 file(s) under demo package (observed from repository paths and static analysis). |
| highlight.js package | library | Observed | Groups 1 file(s) under highlight.js package (observed from repository paths and static analysis). |
| languages package | library | Observed | Groups 198 file(s) under languages package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 13 file(s) under lib package (observed from repository paths and static analysis). |
| stub.js package | library | Observed | Groups 1 file(s) under stub.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 256 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/size_report_comment.yml` (ci)
- `.github/workflows/size_report_create.yml` (ci)
- `.github/workflows/tests.js.yml` (ci)
- `.mocharc.json` (config)
- `.readthedocs.yaml` (config)
- `Dockerfile` (container)
- `docs/requirements.txt` (manifest)
- `package.json` (manifest)
- `src/languages/dockerfile.js` (container)

## Top-level layout

- `src` — 481 analysed file(s)
- `test` — 256 analysed file(s)
- `(root files)` — 26 analysed file(s)
- `docs` — 20 analysed file(s)
- `.github` — 11 analysed file(s)
- `demo` — 4 analysed file(s)
- `extra` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c` is the revision these paths and observations refer to.
