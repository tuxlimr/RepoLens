# Project structure: stylus/stylus

**Analysed commit:** `2e11b972a56d6e41c1408254e60e3d6fb76356d8`

**Commit reference:** [2e11b972a56d6e41c1408254e60e3d6fb76356d8](https://github.com/stylus/stylus/commit/2e11b972a56d6e41c1408254e60e3d6fb76356d8)

**Tree at this commit:** [stylus/stylus@2e11b972a56d](https://github.com/stylus/stylus/tree/2e11b972a56d6e41c1408254e60e3d6fb76356d8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | stylus/stylus |
| Description | Expressive, robust, feature-rich CSS language built for nodejs |
| Stars | 11322 |
| Forks | 1138 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | dev |
| Analysed commit | `2e11b972a56d6e41c1408254e60e3d6fb76356d8` |
| Retrieved at | 2026-11-14T19:12:19.233065+00:00 |
| Files in this snapshot | 793 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    bug.md
    config.yml
  workflows/  (1 files)
    ci.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
bin/  (1 files)
  stylus
deno/  (1 files)
  test.ts
docs/  (54 files)
  .vitepress/  (10 files)
    components/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    style/  (2 files)
      … 2 files under this directory
    theme/  (2 files)
      … 2 files under this directory
    components.d.ts
    config.ts
    meta.ts
  docs/  (36 files)
    atrules.md
    bifs.md
    block.md
    comments.md
    compare.md
    conditionals.md
    css-style.md
    error-reporting.md
    escape.md
    executable.md
    extend.md
    firebug.md
    font-face.md
    functions.md
    functions.url.md
    gedit.md
    hashes.md
    import.md
    index.md
    interpolation.md
    introspection.md
    iteration.md
    js.md
    keyframes.md
    … 12 more files
  public/  (2 files)
    logo.svg
    robots.txt
  .gitignore
  index.md
  package.json
  try.md
  tsconfig.json
  vite.config.ts
editors/  (6 files)
  Stylus.tmbundle/  (5 files)
    Commands/  (1 files)
      … 1 files under this directory
    Preferences/  (2 files)
      … 2 files under this directory
    Syntaxes/  (1 files)
      … 1 files under this directory
    info.plist
  gedit/  (1 files)
    styl.lang
graphics/  (3 files)
  Vectors/  (3 files)
    stylus.ai
    stylus.svg
    stylus_icon.svg
lib/  (138 files)
  cache/  (4 files)
    fs.js
    index.js
    memory.js
    null.js
  convert/  (1 files)
    css.js
  functions/  (71 files)
    acos.js
    add-property.js
    adjust.js
    alpha.js
    asin.js
    atan.js
    base-convert.js
    basename.js
    blend.js
    blue.js
    clone.js
    component.js
    contrast.js
    convert-angle.js
    convert.js
    current-media.js
    define.js
    dirname.js
    error.js
    extname.js
    green.js
    hsl.js
    hsla.js
    hue.js
    … 47 more files
  nodes/  (41 files)
    arguments.js
    atblock.js
    atrule.js
    binop.js
    block.js
    boolean.js
    call.js
    charset.js
    comment.js
    each.js
    expression.js
    extend.js
    feature.js
    function.js
    group.js
    hsla.js
    ident.js
    if.js
    import.js
    index.js
    keyframes.js
    literal.js
    media.js
    member.js
    … 17 more files
  stack/  (3 files)
    frame.js
    index.js
    scope.js
  visitor/  (6 files)
    compiler.js
    deps-resolver.js
    evaluator.js
    index.js
    normalizer.js
    sourcemapper.js
  browserify.js
  colors.js
  errors.js
  lexer.js
  middleware.js
  parser.js
  renderer.js
  selector-parser.js
  stylus.js
  token.js
  units.js
  utils.js
test/  (572 files)
  cases/  (572 files)
    extend.block-level/  (2 files)
      … 2 files under this directory
    import.basic/  (5 files)
      … 5 files under this directory
    import.comments/  (1 files)
      … 1 files under this directory
    import.complex/  (4 files)
      … 4 files under this directory
    import.glob/  (3 files)
      … 3 files under this directory
    import.include.complex/  (3 files)
      … 3 files under this directory
    import.include.function/  (4 files)
      … 4 files under this directory
    import.include.in.function/  (2 files)
      … 2 files under this directory
    import.include.megacomplex/  (7 files)
      … 7 files under this directory
    import.include.resolver.css-file/  (1 files)
      … 1 files under this directory
    import.include.resolver.images/  (4 files)
      … 4 files under this directory
    import.include.resolver.nested/  (2 files)
      … 2 files under this directory
    import.json/  (3 files)
      … 3 files under this directory
    import.literal/  (1 files)
      … 1 files under this directory
    import.lookup/  (2 files)
      … 2 files under this directory
    import.loop/  (1 files)
      … 1 files under this directory
    import.namespace/  (1 files)
      … 1 files under this directory
    import.ordering/  (3 files)
      … 3 files under this directory
    mixins/  (2 files)
      … 2 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    arithmetic.color.css
    arithmetic.color.styl
    arithmetic.css
    arithmetic.styl
    arithmetic.unary.css
    arithmetic.unary.styl
    atblock.css
    atblock.styl
    atrules.compressed.css
    atrules.compressed.styl
    atrules.css
    atrules.styl
    atscope.css
    atscope.styl
    bifs.add-property.css
    bifs.add-property.styl
    bifs.base-convert.css
    bifs.base-convert.styl
    bifs.blend.css
    bifs.blend.styl
    bifs.cache.at-media.css
    bifs.cache.at-media.styl
    bifs.cache.css
    bifs.cache.samename.css
    … 496 more files
.gitignore
.npmignore
Changelog.md
Code_of_Conduct.md
Contributing.md
LICENSE
Makefile
Readme.md
SECURITY.md
bm.js
index.js
package.json
```

## Entry points

- [index.js](https://github.com/stylus/stylus/blob/2e11b972a56d6e41c1408254e60e3d6fb76356d8/index.js)
- [bin/stylus](https://github.com/stylus/stylus/blob/2e11b972a56d6e41c1408254e60e3d6fb76356d8/bin/stylus)
- [lib/cache/index.js](https://github.com/stylus/stylus/blob/2e11b972a56d6e41c1408254e60e3d6fb76356d8/lib/cache/index.js)
- [lib/functions/index.js](https://github.com/stylus/stylus/blob/2e11b972a56d6e41c1408254e60e3d6fb76356d8/lib/functions/index.js)
- [lib/nodes/index.js](https://github.com/stylus/stylus/blob/2e11b972a56d6e41c1408254e60e3d6fb76356d8/lib/nodes/index.js)
- [lib/stack/index.js](https://github.com/stylus/stylus/blob/2e11b972a56d6e41c1408254e60e3d6fb76356d8/lib/stack/index.js)
- [lib/visitor/index.js](https://github.com/stylus/stylus/blob/2e11b972a56d6e41c1408254e60e3d6fb76356d8/lib/visitor/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| deno package | library | Observed | Groups 1 file(s) under deno package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 137 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 572 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `docs/package.json` (manifest)
- `docs/tsconfig.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 572 analysed file(s)
- `lib` — 138 analysed file(s)
- `docs` — 54 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 6 analysed file(s)
- `editors` — 6 analysed file(s)
- `graphics` — 3 analysed file(s)
- `bin` — 1 analysed file(s)
- `deno` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (7 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2e11b972a56d6e41c1408254e60e3d6fb76356d8` is the revision these paths and observations refer to.
