# Project structure: mdx-js/mdx

**Analysed commit:** `52285a6758fa078ec57f3d4bd8803d9cbfb12065`

**Commit reference:** [52285a6758fa078ec57f3d4bd8803d9cbfb12065](https://github.com/mdx-js/mdx/commit/52285a6758fa078ec57f3d4bd8803d9cbfb12065)

**Tree at this commit:** [mdx-js/mdx@52285a6758fa](https://github.com/mdx-js/mdx/tree/52285a6758fa078ec57f3d4bd8803d9cbfb12065)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mdx-js/mdx |
| Description | Markdown for the component era |
| Stars | 19861 |
| Forks | 1183 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `52285a6758fa078ec57f3d4bd8803d9cbfb12065` |
| Retrieved at | 2026-11-14T19:13:11.135288+00:00 |
| Files in this snapshot | 166 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    bb.yml
    main.yml
    website.yml
docs/  (53 files)
  _asset/  (3 files)
    editor.jsx
    index.css
    index.js
  _component/  (12 files)
    icon/  (3 files)
      … 3 files under this directory
    blog.jsx
    foot-site.jsx
    home.jsx
    layout.jsx
    nav-site.jsx
    nav.jsx
    note.jsx
    snowfall.jsx
    sort.js
  _static/  (1 files)
    icon.svg
  blog/  (7 files)
    conf.mdx
    custom-pragma.mdx
    index.mdx
    shortcodes.mdx
    v1.mdx
    v2.mdx
    v3.mdx
  community/  (6 files)
    about.mdx
    contribute.mdx
    index.mdx
    projects.mdx
    sponsor.mdx
    support.mdx
  docs/  (6 files)
    extending-mdx.mdx
    getting-started.mdx
    index.mdx
    troubleshooting-mdx.mdx
    using-mdx.mdx
    what-is-mdx.mdx
  guides/  (8 files)
    embed.mdx
    frontmatter.mdx
    gfm.mdx
    index.mdx
    injecting-components.mdx
    math.mdx
    mdx-on-demand.mdx
    syntax-highlighting.mdx
  migrating/  (3 files)
    v1.mdx
    v2.mdx
    v3.mdx
  packages/  (1 files)
    index.mdx
  .remarkrc.js
  404.mdx
  _config.js
  index.mdx
  playground.mdx
  table-of-components.mdx
packages/  (94 files)
  esbuild/  (7 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    license
    package.json
    readme.md
    tsconfig.json
  loader/  (7 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.cjs
    license
    package.json
    readme.md
    tsconfig.json
  mdx/  (35 files)
    lib/  (22 files)
      … 22 files under this directory
    test/  (8 files)
      … 8 files under this directory
    index.js
    license
    package.json
    readme.md
    tsconfig.json
  node-loader/  (9 files)
    lib/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    license
    package.json
    readme.md
    tsconfig.json
  preact/  (7 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    license
    package.json
    readme.md
    tsconfig.json
  react/  (7 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    license
    package.json
    readme.md
    tsconfig.json
  remark-mdx/  (7 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    license
    package.json
    readme.md
    tsconfig.json
  rollup/  (8 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (2 files)
      … 2 files under this directory
    index.js
    license
    package.json
    readme.md
    tsconfig.json
  vue/  (7 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    index.js
    license
    package.json
    readme.md
    tsconfig.json
script/  (1 files)
  jsx-loader.js
website/  (6 files)
  generate.js
  mdx-loader.js
  post.js
  prep.js
  schema-description.js
  types.d.ts
.editorconfig
.gitignore
.prettierignore
changelog.md
license
package.json
readme.md
renovate.json5
tsconfig.json
```

## Entry points

- [packages/esbuild/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/esbuild/index.js)
- [packages/esbuild/lib/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/esbuild/lib/index.js)
- [packages/loader/lib/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/loader/lib/index.js)
- [packages/mdx/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/mdx/index.js)
- [packages/node-loader/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/node-loader/index.js)
- [packages/node-loader/lib/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/node-loader/lib/index.js)
- [packages/preact/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/preact/index.js)
- [packages/preact/lib/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/preact/lib/index.js)
- [packages/react/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/react/index.js)
- [packages/react/lib/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/react/lib/index.js)
- [packages/remark-mdx/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/remark-mdx/index.js)
- [packages/remark-mdx/lib/index.js](https://github.com/mdx-js/mdx/blob/52285a6758fa078ec57f3d4bd8803d9cbfb12065/packages/remark-mdx/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 20 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 41 file(s) under packages package (observed from repository paths and static analysis). |
| script package | library | Observed | Groups 1 file(s) under script package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 17 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 6 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/bb.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/website.yml` (ci)
- `package.json` (manifest)
- `packages/esbuild/package.json` (manifest)
- `packages/esbuild/tsconfig.json` (config)
- `packages/loader/package.json` (manifest)
- `packages/loader/tsconfig.json` (config)
- `packages/mdx/package.json` (manifest)
- `packages/mdx/tsconfig.json` (config)
- `packages/node-loader/package.json` (manifest)
- `packages/node-loader/tsconfig.json` (config)
- `packages/preact/package.json` (manifest)
- `packages/preact/tsconfig.json` (config)
- `packages/react/package.json` (manifest)
- `packages/react/tsconfig.json` (config)
- `packages/remark-mdx/package.json` (manifest)
- `packages/remark-mdx/tsconfig.json` (config)
- `packages/rollup/package.json` (manifest)
- `packages/rollup/tsconfig.json` (config)
- `packages/vue/package.json` (manifest)
- `packages/vue/tsconfig.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 94 analysed file(s)
- `docs` — 53 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `website` — 6 analysed file(s)
- `.github` — 3 analysed file(s)
- `script` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `52285a6758fa078ec57f3d4bd8803d9cbfb12065` is the revision these paths and observations refer to.
