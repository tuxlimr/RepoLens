# Project structure: vercel/hyper

**Analysed commit:** `890a332ed9c35ed87343647d3ec6611b8045b157`

**Commit reference:** [890a332ed9c35ed87343647d3ec6611b8045b157](https://github.com/vercel/hyper/commit/890a332ed9c35ed87343647d3ec6611b8045b157)

**Tree at this commit:** [vercel/hyper@890a332ed9c3](https://github.com/vercel/hyper/tree/890a332ed9c35ed87343647d3ec6611b8045b157)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vercel/hyper |
| Description | A terminal built on web technologies |
| Stars | 44753 |
| Forks | 3571 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | canary |
| Analysed commit | `890a332ed9c35ed87343647d3ec6611b8045b157` |
| Retrieved at | 2026-11-14T19:12:58.542626+00:00 |
| Files in this snapshot | 153 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    codeql-analysis.yml
    nodejs.yml
  dependabot.yml
  pull_request_template.md
.husky/  (2 files)
  .gitignore
  pre-push
.vscode/  (1 files)
  launch.json
app/  (47 files)
  config/  (8 files)
    config-default.json
    import.ts
    init.ts
    migrate.ts
    open.ts
    paths.ts
    schema.json
    windows.ts
  keymaps/  (3 files)
    darwin.json
    linux.json
    win32.json
  menus/  (8 files)
    menus/  (7 files)
      … 7 files under this directory
    menu.ts
  patches/  (1 files)
    node-pty+1.0.0.patch
  plugins/  (2 files)
    extensions.ts
    install.ts
  ui/  (2 files)
    contextmenu.ts
    window.ts
  utils/  (9 files)
    cli-install.ts
    colors.ts
    map-keys.ts
    renderer-utils.ts
    shell-fallback.ts
    ssh-url.ts
    system-context-menu.ts
    to-electron-background-color.ts
    window-utils.ts
  auto-updater-linux.ts
  commands.ts
  config.ts
  index.html
  index.ts
  notifications.ts
  notify.ts
  package.json
  plugins.ts
  pnpm-workspace.yaml
  rpc.ts
  session.ts
  tsconfig.json
  updater.ts
assets/  (1 files)
  icons.svg
bin/  (6 files)
  cp-snapshot.js
  download-mksnapshot.js
  mk-snapshot.js
  notarize.js
  rimraf-standalone.js
  snapshot-libs.js
cli/  (2 files)
  api.ts
  index.ts
lib/  (49 files)
  actions/  (8 files)
    config.ts
    header.ts
    index.ts
    notifications.ts
    sessions.ts
    term-groups.ts
    ui.ts
    updater.ts
  components/  (12 files)
    header.tsx
    new-tab.tsx
    notification.tsx
    notifications.tsx
    searchBox.tsx
    split-pane.tsx
    style-sheet.tsx
    tab.tsx
    tabs.tsx
    term-group.tsx
    term.tsx
    terms.tsx
  containers/  (4 files)
    header.ts
    hyper.tsx
    notifications.ts
    terms.ts
  reducers/  (4 files)
    index.ts
    sessions.ts
    term-groups.ts
    ui.ts
  store/  (4 files)
    configure-store.dev.ts
    configure-store.prod.ts
    configure-store.ts
    write-middleware.ts
  utils/  (11 files)
    config.ts
    effects.ts
    file.ts
    ipc-child-process.ts
    ipc.ts
    notify.ts
    object.ts
    paste.ts
    plugins.ts
    rpc.ts
    term-groups.ts
  command-registry.ts
  index.tsx
  rpc.ts
  selectors.ts
  terms.ts
  v8-snapshot-util.ts
test/  (6 files)
  testUtils/  (1 files)
    is-hex-color.ts
  unit/  (4 files)
    cli-api.test.ts
    ssh-url.test.ts
    to-electron-background-color.test.ts
    window-utils.test.ts
  index.ts
typings/  (13 files)
  constants/  (8 files)
    config.d.ts
    index.d.ts
    notifications.d.ts
    sessions.d.ts
    tabs.d.ts
    term-groups.d.ts
    ui.d.ts
    updater.d.ts
  common.d.ts
  config.d.ts
  ext-modules.d.ts
  extend-electron.d.ts
  hyper.d.ts
.editorconfig
.eslintignore
.eslintrc.json
.gitattributes
.gitignore
LICENSE
PLUGINS.md
README.md
ava-e2e.config.js
ava.config.js
babel.config.json
electron-builder-linux-ci.json
electron-builder.json
package.json
pnpm-workspace.yaml
release.js
tsconfig.base.json
tsconfig.eslint.json
tsconfig.json
webpack.config.ts
```

## Entry points

- [app/index.ts](https://github.com/vercel/hyper/blob/890a332ed9c35ed87343647d3ec6611b8045b157/app/index.ts)
- [cli/index.ts](https://github.com/vercel/hyper/blob/890a332ed9c35ed87343647d3ec6611b8045b157/cli/index.ts)
- [lib/actions/index.ts](https://github.com/vercel/hyper/blob/890a332ed9c35ed87343647d3ec6611b8045b157/lib/actions/index.ts)
- [lib/index.tsx](https://github.com/vercel/hyper/blob/890a332ed9c35ed87343647d3ec6611b8045b157/lib/index.tsx)
- [lib/reducers/index.ts](https://github.com/vercel/hyper/blob/890a332ed9c35ed87343647d3ec6611b8045b157/lib/reducers/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 31 file(s) under app package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 6 file(s) under bin package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 2 file(s) under cli package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 22 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 49 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 13 file(s) under typings package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/nodejs.yml` (ci)
- `.vscode/launch.json` (config)
- `app/config/config-default.json` (config)
- `app/config/schema.json` (config)
- `app/keymaps/darwin.json` (config)
- `app/keymaps/linux.json` (config)
- `app/keymaps/win32.json` (config)
- `app/package.json` (manifest)
- `app/pnpm-workspace.yaml` (config)
- `app/tsconfig.json` (config)
- `babel.config.json` (config)
- `electron-builder-linux-ci.json` (config)
- `electron-builder.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.base.json` (config)
- `tsconfig.eslint.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `lib` — 49 analysed file(s)
- `app` — 47 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `typings` — 13 analysed file(s)
- `.github` — 6 analysed file(s)
- `bin` — 6 analysed file(s)
- `test` — 6 analysed file(s)
- `.husky` — 2 analysed file(s)
- `cli` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 10 file(s) were skipped during inventory (2 x likely secret file excluded; 1 x lockfile excluded; 7 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `890a332ed9c35ed87343647d3ec6611b8045b157` is the revision these paths and observations refer to.
