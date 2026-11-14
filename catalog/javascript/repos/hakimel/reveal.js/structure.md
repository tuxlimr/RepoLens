# Project structure: hakimel/reveal.js

**Analysed commit:** `e240e175232fa2de660a02bc0d7bf5f655b159bb`

**Commit reference:** [e240e175232fa2de660a02bc0d7bf5f655b159bb](https://github.com/hakimel/reveal.js/commit/e240e175232fa2de660a02bc0d7bf5f655b159bb)

**Tree at this commit:** [hakimel/reveal.js@e240e175232f](https://github.com/hakimel/reveal.js/tree/e240e175232fa2de660a02bc0d7bf5f655b159bb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hakimel/reveal.js |
| Description | The HTML Presentation Framework |
| Stars | 72579 |
| Forks | 17024 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e240e175232fa2de660a02bc0d7bf5f655b159bb` |
| Retrieved at | 2026-11-14T19:10:34.159111+00:00 |
| Files in this snapshot | 172 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (2 files)
    spellcheck.yml
    test.yml
  CONTRIBUTING.md
  FUNDING.yml
css/  (27 files)
  print/  (2 files)
    paper.scss
    pdf.scss
  theme/  (22 files)
    fonts/  (4 files)
      … 4 files under this directory
    template/  (3 files)
      … 3 files under this directory
    README.md
    beige.scss
    black-contrast.scss
    black.scss
    blood.scss
    dracula.scss
    league.scss
    moon.scss
    night.scss
    serif.scss
    simple.scss
    sky.scss
    solarized.scss
    white-contrast.scss
    white.scss
  layout.scss
  reset.css
  reveal.scss
examples/  (14 files)
  assets/  (1 files)
    beeping.txt
  500-slides.html
  auto-animate.html
  backgrounds.html
  barebones.html
  layout-helpers.html
  lightbox.html
  markdown.html
  markdown.md
  math.html
  media.html
  multiple-presentations.html
  scroll.html
  transitions.html
js/  (29 files)
  components/  (1 files)
    playback.js
  controllers/  (19 files)
    autoanimate.js
    backgrounds.js
    controls.js
    focus.js
    fragments.js
    jumptoslide.js
    keyboard.js
    location.js
    notes.js
    overlay.js
    overview.js
    plugins.js
    pointer.js
    printview.js
    progress.js
    scrollview.js
    slidecontent.js
    slidenumber.js
    touch.js
  utils/  (5 files)
    color.ts
    constants.ts
    device.ts
    loader.ts
    util.ts
  config.ts
  index.ts
  reveal.d.ts
  reveal.js
plugin/  (24 files)
  highlight/  (3 files)
    index.ts
    plugin.js
    vite.config.ts
  markdown/  (3 files)
    index.ts
    plugin.js
    vite.config.ts
  math/  (7 files)
    index.ts
    katex.js
    mathjax2.js
    mathjax3.js
    mathjax4.js
    plugin.js
    vite.config.ts
  notes/  (4 files)
    index.ts
    plugin.js
    speaker-view.html
    vite.config.ts
  search/  (3 files)
    index.ts
    plugin.js
    vite.config.ts
  zoom/  (3 files)
    index.ts
    plugin.js
    vite.config.ts
  vite-plugin-dts.ts
public/  (2 files)
  plugin/  (2 files)
    highlight/  (2 files)
      … 2 files under this directory
react/  (31 files)
  demo/  (7 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (2 files)
      … 2 files under this directory
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  src/  (18 files)
    __tests__/  (1 files)
      … 1 files under this directory
    components/  (12 files)
      … 12 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    index.ts
    reveal-context.ts
    types.ts
  AGENTS.md
  README.md
  package.json
  tsconfig.json
  vite.config.ts
  vitest.config.ts
scripts/  (5 files)
  add-banner.js
  banner.js
  build-es5.js
  test.js
  zip.js
test/  (23 files)
  assets/  (4 files)
    external-script-a.js
    external-script-b.js
    external-script-c.js
    external-script-d.js
  types/  (1 files)
    plugin-imports.ts
  simple.md
  test-auto-animate.html
  test-dependencies-async.html
  test-dependencies.html
  test-destroy.html
  test-grid-navigation.html
  test-iframe-backgrounds.html
  test-iframes.html
  test-markdown.html
  test-mathjax4.html
  test-multiple-instances-es5.html
  test-multiple-instances.html
  test-overlays.html
  test-pdf.html
  test-plugins.html
  test-scroll.html
  test-state.html
  test.html
.codespellrc
.gitignore
.prettierignore
.prettierrc
LICENSE
README.md
demo.html
index.html
package.json
tsconfig.json
tsconfig.node.json
vite.config.styles.ts
vite.config.ts
```

## Entry points

- [js/index.ts](https://github.com/hakimel/reveal.js/blob/e240e175232fa2de660a02bc0d7bf5f655b159bb/js/index.ts)
- [plugin/highlight/index.ts](https://github.com/hakimel/reveal.js/blob/e240e175232fa2de660a02bc0d7bf5f655b159bb/plugin/highlight/index.ts)
- [plugin/markdown/index.ts](https://github.com/hakimel/reveal.js/blob/e240e175232fa2de660a02bc0d7bf5f655b159bb/plugin/markdown/index.ts)
- [plugin/math/index.ts](https://github.com/hakimel/reveal.js/blob/e240e175232fa2de660a02bc0d7bf5f655b159bb/plugin/math/index.ts)
- [plugin/notes/index.ts](https://github.com/hakimel/reveal.js/blob/e240e175232fa2de660a02bc0d7bf5f655b159bb/plugin/notes/index.ts)
- [plugin/search/index.ts](https://github.com/hakimel/reveal.js/blob/e240e175232fa2de660a02bc0d7bf5f655b159bb/plugin/search/index.ts)
- [plugin/zoom/index.ts](https://github.com/hakimel/reveal.js/blob/e240e175232fa2de660a02bc0d7bf5f655b159bb/plugin/zoom/index.ts)
- [react/demo/src/main.tsx](https://github.com/hakimel/reveal.js/blob/e240e175232fa2de660a02bc0d7bf5f655b159bb/react/demo/src/main.tsx)
- [react/src/index.ts](https://github.com/hakimel/reveal.js/blob/e240e175232fa2de660a02bc0d7bf5f655b159bb/react/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 19 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 10 file(s) under js package (observed from repository paths and static analysis). |
| plugin package | library | Observed | Groups 23 file(s) under plugin package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 23 file(s) under react package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 23 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/spellcheck.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)
- `react/demo/package.json` (manifest)
- `react/demo/tsconfig.json` (config)
- `react/package.json` (manifest)
- `react/tsconfig.json` (config)
- `tsconfig.json` (config)
- `tsconfig.node.json` (config)

## Top-level layout

- `react` — 31 analysed file(s)
- `js` — 29 analysed file(s)
- `css` — 27 analysed file(s)
- `plugin` — 24 analysed file(s)
- `test` — 23 analysed file(s)
- `examples` — 14 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `public` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 43 file(s) were skipped during inventory (3 x lockfile excluded; 40 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e240e175232fa2de660a02bc0d7bf5f655b159bb` is the revision these paths and observations refer to.
