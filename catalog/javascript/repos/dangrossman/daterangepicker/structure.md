# Project structure: dangrossman/daterangepicker

**Analysed commit:** `5df13653dc85dc46784950e4c4e00b8663cb7970`

**Commit reference:** [5df13653dc85dc46784950e4c4e00b8663cb7970](https://github.com/dangrossman/daterangepicker/commit/5df13653dc85dc46784950e4c4e00b8663cb7970)

**Tree at this commit:** [dangrossman/daterangepicker@5df13653dc85](https://github.com/dangrossman/daterangepicker/tree/5df13653dc85dc46784950e4c4e00b8663cb7970)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dangrossman/daterangepicker |
| Description | JavaScript Date Range, Date and Time Picker Component |
| Stars | 10971 |
| Forks | 3236 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5df13653dc85dc46784950e4c4e00b8663cb7970` |
| Retrieved at | 2026-11-14T19:12:27.598409+00:00 |
| Files in this snapshot | 66 |

## Directory tree

```text
example/  (19 files)
  amd/  (3 files)
    index.html
    main.js
    require.js
  browserify/  (4 files)
    README.md
    bundle.js
    index.html
    main.js
  integrations/  (12 files)
    angular/  (2 files)
      … 2 files under this directory
    commonjs/  (1 files)
      … 1 files under this directory
    esm/  (1 files)
      … 1 files under this directory
    react/  (1 files)
      … 1 files under this directory
    svelte/  (2 files)
      … 2 files under this directory
    vue/  (2 files)
      … 2 files under this directory
    README.md
    build.mjs
    package.json
scripts/  (2 files)
  build-docs.mjs
  build.mjs
src/  (2 files)
  dates.js
  picker.js
tests/  (1 files)
  picker.test.cjs
website/  (28 files)
  examples/  (12 files)
    angular/  (1 files)
      … 1 files under this directory
    assets/  (5 files)
      … 5 files under this directory
    commonjs/  (1 files)
      … 1 files under this directory
    esm/  (1 files)
      … 1 files under this directory
    react/  (1 files)
      … 1 files under this directory
    svelte/  (1 files)
      … 1 files under this directory
    vue/  (1 files)
      … 1 files under this directory
    examples.css
  native/  (6 files)
    amd.html
    classic.html
    guide.css
    jquery.html
    module.html
    source.js
  config.html
  config.js
  daterangepicker.css
  daterangepicker.js
  daterangepicker.mjs
  index.html
  reference.html
  upgrade.html
  website.css
  website.js
.gitignore
README.md
bower.json
daterangepicker.css
daterangepicker.d.mts
daterangepicker.d.ts
daterangepicker.js
daterangepicker.mjs
demo.html
package.js
package.json
test.html
website.css
website.js
```

## Entry points

- [daterangepicker.js](https://github.com/dangrossman/daterangepicker/blob/5df13653dc85dc46784950e4c4e00b8663cb7970/daterangepicker.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| dates.js package | library | Observed | Groups 1 file(s) under dates.js package (observed from repository paths and static analysis). |
| picker.js package | library | Observed | Groups 1 file(s) under picker.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 9 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `bower.json` (config)
- `example/integrations/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `website` — 28 analysed file(s)
- `example` — 19 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `scripts` — 2 analysed file(s)
- `src` — 2 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (1 x lockfile excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5df13653dc85dc46784950e4c4e00b8663cb7970` is the revision these paths and observations refer to.
