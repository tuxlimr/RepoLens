# Project structure: gka/chroma.js

**Analysed commit:** `c6f893a6e3bb83b3b03d397ceffd326cf818cd02`

**Commit reference:** [c6f893a6e3bb83b3b03d397ceffd326cf818cd02](https://github.com/gka/chroma.js/commit/c6f893a6e3bb83b3b03d397ceffd326cf818cd02)

**Tree at this commit:** [gka/chroma.js@c6f893a6e3bb](https://github.com/gka/chroma.js/tree/c6f893a6e3bb83b3b03d397ceffd326cf818cd02)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gka/chroma.js |
| Description | JavaScript library for all kinds of color manipulations |
| Stars | 10604 |
| Forks | 560 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `c6f893a6e3bb83b3b03d397ceffd326cf818cd02` |
| Retrieved at | 2026-11-14T19:12:36.665058+00:00 |
| Files in this snapshot | 198 |

## Directory tree

```text
.bin/  (1 files)
  update-version.cjs
.changeset/  (2 files)
  README.md
  config.json
.github/  (3 files)
  workflows/  (1 files)
    ci.yml
  CODEOWNERS
  FUNDING.yml
.husky/  (1 files)
  pre-commit
docs/  (17 files)
  bin/  (1 files)
    post-process
  libs/  (11 files)
    codemirror/  (7 files)
      … 7 files under this directory
    chroma-light.cjs
    chroma-light.min.cjs
    chroma.cjs
    chroma.min.cjs
  src/  (3 files)
    footer.inc.html
    index.css
    index.md
  Makefile
  index.html
src/  (103 files)
  colors/  (2 files)
    colorbrewer.js
    w3cx11.js
  generator/  (7 files)
    average.js
    bezier.js
    blend.js
    cubehelix.js
    mix.js
    random.js
    scale.js
  interpolator/  (13 files)
    _hsx.js
    hcg.js
    hsi.js
    hsl.js
    hsv.js
    index.js
    lab.js
    lch.js
    lrgb.js
    num.js
    oklab.js
    oklch.js
    rgb.js
  io/  (54 files)
    cmyk/  (3 files)
      … 3 files under this directory
    css/  (8 files)
      … 8 files under this directory
    gl/  (1 files)
      … 1 files under this directory
    hcg/  (3 files)
      … 3 files under this directory
    hex/  (3 files)
      … 3 files under this directory
    hsi/  (3 files)
      … 3 files under this directory
    hsl/  (3 files)
      … 3 files under this directory
    hsv/  (3 files)
      … 3 files under this directory
    lab/  (4 files)
      … 4 files under this directory
    lch/  (6 files)
      … 6 files under this directory
    named/  (1 files)
      … 1 files under this directory
    num/  (3 files)
      … 3 files under this directory
    oklab/  (3 files)
      … 3 files under this directory
    oklch/  (3 files)
      … 3 files under this directory
    rgb/  (1 files)
      … 1 files under this directory
    temp/  (3 files)
      … 3 files under this directory
    delta-e.coffee
    distance.coffee
    input.js
  ops/  (10 files)
    alpha.js
    clipped.js
    darken.js
    get.js
    luminance.js
    mix.js
    premultiply.js
    saturate.js
    set.js
    shade.js
  utils/  (14 files)
    analyze.js
    clip_rgb.js
    contrast.js
    contrastAPCA.js
    delta-e.js
    distance.js
    index.js
    last.js
    limit.js
    multiply-matrices.js
    scales.js
    type.js
    unpack.js
    valid.js
  Color.js
  chroma.js
  version.js
test/  (56 files)
  docs/  (1 files)
    index.test.js
  html/  (5 files)
    bezier.html
    blend.html
    colorscales.html
    cubehelix.html
    luminance.html
  io/  (24 files)
    cmyk2rgb.test.js
    css2rgb.test.js
    hcg2rgb.test.js
    hex2rgb.test.js
    hsi2rgb.test.js
    hsl2rgb.test.js
    hsv2rgb.test.js
    lab2lch.test.js
    lab2rgb.test.js
    lch2lab.test.js
    lch2rgb.test.js
    num2rgb.test.js
    oklab2rgb.test.js
    oklch2rgb.test.js
    rgb2cmyk.test.js
    rgb2css.test.js
    rgb2hcg.test.js
    rgb2hex.test.js
    rgb2hsi.test.js
    rgb2hsv.test.js
    rgb2lab.test.js
    rgb2lch.test.js
    rgb2oklab.test.js
    rgb2oklch.test.js
  alpha.test.js
  analyze.test.js
  autodetect.test.js
  average.test.js
  bezier.test.js
  blend.test.js
  color.test.js
  colorbrewer.test.js
  contrast.test.js
  converters.test.js
  cubehelix.test.js
  delta-e.test.js
  lch.test.js
  limits.test.js
  luminance.test.js
  manipulate.test.js
  misc.test.js
  mix.test.js
  num.test.js
  premultiply.test.js
  random.test.js
  scale.lcorrection.test.js
  scales.test.js
  temperature2rgb.test.js
  … 2 more files
.gitignore
.npmignore
.travis.yml
CHANGELOG.md
LICENSE
eslint.config.mjs
index-light.js
index.js
index.umd.js
index.umd.light.js
package.json
prettier.config.js
readme.md
rollup.config.js
vitest.config.mjs
```

## Entry points

- [index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/index.js)
- [src/interpolator/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/interpolator/index.js)
- [src/io/cmyk/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/io/cmyk/index.js)
- [src/io/css/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/io/css/index.js)
- [src/io/gl/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/io/gl/index.js)
- [src/io/hcg/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/io/hcg/index.js)
- [src/io/hex/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/io/hex/index.js)
- [src/io/hsi/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/io/hsi/index.js)
- [src/io/hsl/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/io/hsl/index.js)
- [src/io/hsv/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/io/hsv/index.js)
- [src/io/lab/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/io/lab/index.js)
- [src/io/lch/index.js](https://github.com/gka/chroma.js/blob/c6f893a6e3bb83b3b03d397ceffd326cf818cd02/src/io/lch/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| chroma.js package | library | Observed | Groups 1 file(s) under chroma.js package (observed from repository paths and static analysis). |
| Color.js package | library | Observed | Groups 1 file(s) under color.js package (observed from repository paths and static analysis). |
| colors package | library | Observed | Groups 2 file(s) under colors package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| generator package | library | Observed | Groups 7 file(s) under generator package (observed from repository paths and static analysis). |
| interpolator package | library | Observed | Groups 13 file(s) under interpolator package (observed from repository paths and static analysis). |
| io package | library | Observed | Groups 52 file(s) under io package (observed from repository paths and static analysis). |
| ops package | library | Observed | Groups 10 file(s) under ops package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 56 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 14 file(s) under utils package (observed from repository paths and static analysis). |
| version.js package | library | Observed | Groups 1 file(s) under version.js package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 103 analysed file(s)
- `test` — 56 analysed file(s)
- `docs` — 17 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 3 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.bin` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (1 x lockfile excluded; 4 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c6f893a6e3bb83b3b03d397ceffd326cf818cd02` is the revision these paths and observations refer to.
