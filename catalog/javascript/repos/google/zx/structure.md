# Project structure: google/zx

**Analysed commit:** `3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5`

**Commit reference:** [3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5](https://github.com/google/zx/commit/3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5)

**Tree at this commit:** [google/zx@3b04a6ae3e34](https://github.com/google/zx/tree/3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google/zx |
| Description | A tool for writing better scripts |
| Stars | 45849 |
| Forks | 1334 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5` |
| Retrieved at | 2026-11-14T19:10:38.157682+00:00 |
| Files in this snapshot | 143 |

## Directory tree

```text
.github/  (15 files)
  ISSUE_TEMPLATE/  (2 files)
    bug.yml
    idea.yml
  codeql/  (1 files)
    codeql-config.yml
  pages/  (1 files)
    index.html
  workflows/  (8 files)
    codeql.yml
    dev-publish.yml
    docs.yml
    jsr-publish.yml
    osv.yml
    publish.yml
    test.yml
    zizmor.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  SECURITY.md
dcr/  (1 files)
  Dockerfile
docs/  (27 files)
  .vitepress/  (5 files)
    theme/  (4 files)
      … 4 files under this directory
    config.mts
  public/  (2 files)
    img/  (2 files)
      … 2 files under this directory
  .gitignore
  api.md
  architecture.md
  cli.md
  configuration.md
  contribution.md
  faq.md
  getting-started.md
  index.md
  known-issues.md
  lite.md
  markdown.md
  migration-from-v7.md
  process-output.md
  process-promise.md
  quotes.md
  setup.md
  shell.md
  typescript.md
  versions.md
examples/  (7 files)
  background-process.mjs
  backup-github.mjs
  fetch-weather.mjs
  hello.mjs
  interactive.mjs
  npm-oidc-enable.mjs
  parallel.mjs
man/  (1 files)
  zx.1
scripts/  (12 files)
  build-clean.mjs
  build-dts.mjs
  build-js.mjs
  build-jsr.mjs
  build-pkgjson-lite.mjs
  build-pkgjson-main.mjs
  build-size-limit.mjs
  build-tests.mjs
  build-versions.mjs
  deno.polyfill.js
  import-meta-url.polyfill.js
  npm-audit.js
src/  (17 files)
  cli.ts
  core.ts
  deps.ts
  error.ts
  globals-jsr.ts
  globals.ts
  goods.ts
  index.ts
  internals.ts
  log.ts
  md.ts
  repl.ts
  util.ts
  vendor-core.ts
  vendor-extra.ts
  vendor.ts
  versions.ts
test/  (47 files)
  bench/  (1 files)
    buf-join.mjs
  fixtures/  (19 files)
    js-project/  (2 files)
      … 2 files under this directory
    ts-project/  (3 files)
      … 3 files under this directory
    argv.mjs
    copyright.txt
    echo.http
    exit-code.mjs
    filename-dirname.mjs
    interactive.mjs
    markdown-crlf.md
    markdown.md
    md.http
    no-extension
    no-extension.mjs
    non-std-ext.zx
    require.mjs
    server.mjs
  it/  (3 files)
    build-dcr.test.js
    build-jsr.test.js
    build-npm.test.js
  smoke/  (10 files)
    bun.test.js
    deno.test.js
    electron.test.cjs
    node.test.cjs
    node.test.mjs
    ts.test.ts
    tsconfig.json
    tsconfig.test.json
    webcontainer.test.mjs
    win32.test.js
  all.test.js
  cli.test.js
  core.test.js
  deps.test.js
  error.test.ts
  export.test.js
  extra.test.js
  global.test.js
  goods.test.ts
  index.test.js
  log.test.ts
  md.test.ts
  util.test.js
  vendor.test.js
test-d/  (3 files)
  core.test-d.ts
  globals.test-d.ts
  goods.test-d.ts
.commitlintrc
.gitattributes
.gitignore
.node_version
.nycrc
.prettierignore
.size-limit.json
LICENSE
README.md
lefthook.yml
package.json
tsconfig.json
zizmor.yml
```

## Entry points

- [src/index.ts](https://github.com/google/zx/blob/3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cli.ts package | library | Observed | Groups 1 file(s) under cli.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| core.ts package | library | Observed | Groups 1 file(s) under core.ts package (observed from repository paths and static analysis). |
| deps.ts package | library | Observed | Groups 1 file(s) under deps.ts package (observed from repository paths and static analysis). |
| error.ts package | library | Observed | Groups 1 file(s) under error.ts package (observed from repository paths and static analysis). |
| globals-jsr.ts package | library | Observed | Groups 1 file(s) under globals-jsr.ts package (observed from repository paths and static analysis). |
| globals.ts package | library | Observed | Groups 1 file(s) under globals.ts package (observed from repository paths and static analysis). |
| goods.ts package | library | Observed | Groups 1 file(s) under goods.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| internals.ts package | library | Observed | Groups 1 file(s) under internals.ts package (observed from repository paths and static analysis). |
| log.ts package | library | Observed | Groups 1 file(s) under log.ts package (observed from repository paths and static analysis). |
| md.ts package | library | Observed | Groups 1 file(s) under md.ts package (observed from repository paths and static analysis). |
| repl.ts package | library | Observed | Groups 1 file(s) under repl.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 12 file(s) under scripts package (observed from repository paths and static analysis). |
| test-d package | library | Observed | Groups 3 file(s) under test-d package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 47 file(s) under tests (observed from repository paths and static analysis). |
| util.ts package | library | Observed | Groups 1 file(s) under util.ts package (observed from repository paths and static analysis). |
| vendor-core.ts package | library | Observed | Groups 1 file(s) under vendor-core.ts package (observed from repository paths and static analysis). |
| vendor-extra.ts package | library | Observed | Groups 1 file(s) under vendor-extra.ts package (observed from repository paths and static analysis). |
| vendor.ts package | library | Observed | Groups 1 file(s) under vendor.ts package (observed from repository paths and static analysis). |
| versions.ts package | library | Observed | Groups 1 file(s) under versions.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/idea.yml` (config)
- `.github/codeql/codeql-config.yml` (config)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/dev-publish.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/jsr-publish.yml` (ci)
- `.github/workflows/osv.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/zizmor.yml` (ci)
- `.size-limit.json` (config)
- `dcr/Dockerfile` (container)
- `lefthook.yml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `zizmor.yml` (config)

## Top-level layout

- `test` — 47 analysed file(s)
- `docs` — 27 analysed file(s)
- `src` — 17 analysed file(s)
- `.github` — 15 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `scripts` — 12 analysed file(s)
- `examples` — 7 analysed file(s)
- `test-d` — 3 analysed file(s)
- `dcr` — 1 analysed file(s)
- `man` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 31 file(s) were skipped during inventory (31 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5` is the revision these paths and observations refer to.
