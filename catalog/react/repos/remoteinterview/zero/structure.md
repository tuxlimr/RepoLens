# Project structure: remoteinterview/zero

**Analysed commit:** `e6a72ee49e03008a64c86ee5c34e2120a3b52908`

**Commit reference:** [e6a72ee49e03008a64c86ee5c34e2120a3b52908](https://github.com/remoteinterview/zero/commit/e6a72ee49e03008a64c86ee5c34e2120a3b52908)

**Tree at this commit:** [remoteinterview/zero@e6a72ee49e03](https://github.com/remoteinterview/zero/tree/e6a72ee49e03008a64c86ee5c34e2120a3b52908)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | remoteinterview/zero |
| Description | Zero is a web server to simplify web development. |
| Stars | 5802 |
| Forks | 240 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e6a72ee49e03008a64c86ee5c34e2120a3b52908` |
| Retrieved at | 2026-11-14T19:14:13.514860+00:00 |
| Files in this snapshot | 252 |

## Directory tree

```text
.codesandbox/  (1 files)
  ci.json
.github/  (2 files)
  workflows/  (1 files)
    push.yml
  stale.yml
docs/  (14 files)
  deploying/  (1 files)
    README.md
  howitworks/  (1 files)
    README.md
  html/  (1 files)
    README.md
  mdx/  (1 files)
    README.md
  nodejs/  (1 files)
    README.md
  proxy/  (1 files)
    README.md
  python/  (1 files)
    README.md
  react/  (1 files)
    README.md
  routing/  (1 files)
    README.md
  security/  (1 files)
    README.md
  static/  (1 files)
    README.md
  svelte/  (1 files)
    README.md
  vue/  (1 files)
    README.md
  README.md
examples/  (32 files)
  basic-login-nodejs/  (4 files)
    README.md
    index.html
    login.js
    user.js
  express-with-middlewares/  (1 files)
    index.js
  google-login-nodejs/  (5 files)
    README.md
    _passport.js
    callback.js
    index.jsx
    login.js
  markdown/  (2 files)
    code.md
    index.md
  markdown-with-css/  (2 files)
    index.md
    style.css
  mdx-with-jsx/  (2 files)
    button.jsx
    index.mdx
  react-basic-css/  (2 files)
    index.jsx
    style.css
  react-custom-charset/  (1 files)
    index.jsx
  react-fetch/  (1 files)
    index.jsx
  react-head-elements/  (1 files)
    index.jsx
  tailwindcss/  (9 files)
    README.md
    global.scss
    index.html
    package.json
    postcss.config.js
    react.jsx
    svelte.svelte
    tailwind.config.js
    vue.vue
  README.md
  index.jsx
packages/  (101 files)
  babel-plugin-transform-dirname-filename/  (2 files)
    index.js
    package.json
  builder-html/  (3 files)
    bundle.js
    index.js
    package.json
  builder-js/  (4 files)
    babel.config.js
    bundle.js
    index.js
    package.json
  builder-process/  (2 files)
    index.js
    package.json
  builder-react/  (7 files)
    bundler/  (5 files)
      … 5 files under this directory
    index.js
    package.json
  builder-svelte/  (4 files)
    bundler/  (2 files)
      … 2 files under this directory
    index.js
    package.json
  builder-vue/  (5 files)
    bundler/  (3 files)
      … 3 files under this directory
    index.js
    package.json
  builders-map/  (2 files)
    index.js
    package.json
  core/  (20 files)
    bin/  (1 files)
      … 1 files under this directory
    lib/  (17 files)
      … 17 files under this directory
    README.md
    package.json
  dep-tree-js/  (3 files)
    getImports.js
    index.js
    package.json
  express-session/  (3 files)
    index.js
    package.json
    sessionStore.js
  handler-html/  (4 files)
    handler.js
    index.js
    package.json
    process.js
  handler-js/  (4 files)
    handler.js
    index.js
    package.json
    process.js
  handler-proxy/  (5 files)
    expressWrap.js
    handler.js
    index.js
    package.json
    process.js
  handler-python/  (8 files)
    entryfile.py
    expressWrap.js
    firstrun.js
    handler.js
    index.js
    installPip.js
    package.json
    pythonExe.js
  handler-react/  (4 files)
    index.js
    package.json
    process.js
    renderer.js
  handler-static/  (3 files)
    handler.js
    index.js
    package.json
  handler-svelte/  (4 files)
    handler.js
    index.js
    package.json
    process.js
  handler-vue/  (4 files)
    renderer/  (1 files)
      … 1 files under this directory
    index.js
    package.json
    process.js
  handlers-map/  (2 files)
    index.js
    package.json
  parcel-bundler/  (5 files)
    mods/  (2 files)
      … 2 files under this directory
    applyMods.js
    index.js
    package.json
  process/  (3 files)
    globals.js
    index.js
    package.json
test/  (95 files)
  integration/  (12 files)
    dynamicPaths.js
    hmr.codes.js
    hmr.js
    matchPaths.js
    page.html.js
    page.js.js
    page.mdx.js
    page.python.js
    page.react.js
    page.svelte.js
    page.vue.js
    proxyPaths.js
  www/  (77 files)
    _hidden/  (1 files)
      … 1 files under this directory
    api/  (10 files)
      … 10 files under this directory
    dynamicpaths/  (8 files)
      … 8 files under this directory
    html/  (6 files)
      … 6 files under this directory
    ignoredfolder/  (1 files)
      … 1 files under this directory
    mdx/  (5 files)
      … 5 files under this directory
    proxy/  (3 files)
      … 3 files under this directory
    python/  (10 files)
      … 10 files under this directory
    react/  (13 files)
      … 13 files under this directory
    svelte/  (7 files)
      … 7 files under this directory
    vue/  (5 files)
      … 5 files under this directory
    $rootParam.js
    .zeroignore
    404.js
    heading.html
    index.js
    obj.json
    requirements.txt
    text.txt
  jest-global-setup.js
  jest-global-teardown.js
  jest-reporter.js
  jest.setup.js
  request.js
  startServer.js
.gitignore
.prettierignore
CONTRIBUTING.md
LICENSE.md
jest.config.js
lerna.json
package.json
```

## Entry points

- [packages/handler-python/entryfile.py:31](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/handler-python/entryfile.py#L31)
- [packages/babel-plugin-transform-dirname-filename/index.js](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/babel-plugin-transform-dirname-filename/index.js)
- [packages/builder-html/index.js](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/builder-html/index.js)
- [packages/builder-js/index.js](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/builder-js/index.js)
- [packages/builder-process/index.js](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/builder-process/index.js)
- [packages/builder-react/index.js](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/builder-react/index.js)
- [packages/builder-svelte/index.js](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/builder-svelte/index.js)
- [packages/builder-vue/index.js](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/builder-vue/index.js)
- [packages/builders-map/index.js](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/builders-map/index.js)
- [packages/core/lib/index.js](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/core/lib/index.js)
- [packages/core/bin/zero](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/core/bin/zero)
- [packages/dep-tree-js/index.js](https://github.com/remoteinterview/zero/blob/e6a72ee49e03008a64c86ee5c34e2120a3b52908/packages/dep-tree-js/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 24 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE (path not a literal). Observed top-level functio… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 59 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 17 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 95 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: handler, printMsg. |

## Important files

- `.codesandbox/ci.json` (config)
- `.github/stale.yml` (config)
- `.github/workflows/push.yml` (ci)
- `examples/tailwindcss/package.json` (manifest)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/babel-plugin-transform-dirname-filename/package.json` (manifest)
- `packages/builder-html/package.json` (manifest)
- `packages/builder-js/package.json` (manifest)
- `packages/builder-process/package.json` (manifest)
- `packages/builder-react/package.json` (manifest)
- `packages/builder-svelte/package.json` (manifest)
- `packages/builder-vue/package.json` (manifest)
- `packages/builders-map/package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/dep-tree-js/package.json` (manifest)
- `packages/express-session/package.json` (manifest)
- `packages/handler-html/package.json` (manifest)
- `packages/handler-js/package.json` (manifest)
- `packages/handler-proxy/package.json` (manifest)
- `packages/handler-python/package.json` (manifest)
- `packages/handler-react/package.json` (manifest)
- `packages/handler-static/package.json` (manifest)
- `packages/handler-svelte/package.json` (manifest)
- `packages/handler-vue/package.json` (manifest)
- `packages/handlers-map/package.json` (manifest)
- `packages/parcel-bundler/package.json` (manifest)
- `packages/process/package.json` (manifest)

## Top-level layout

- `packages` — 101 analysed file(s)
- `test` — 95 analysed file(s)
- `examples` — 32 analysed file(s)
- `docs` — 14 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 2 analysed file(s)
- `.codesandbox` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 14 file(s) were skipped during inventory (14 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e6a72ee49e03008a64c86ee5c34e2120a3b52908` is the revision these paths and observations refer to.
