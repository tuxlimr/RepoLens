# Project structure: alibaba/hooks

**Analysed commit:** `a0c33c21caefda40753fe4b3cbb3b1efbabd1a79`

**Commit reference:** [a0c33c21caefda40753fe4b3cbb3b1efbabd1a79](https://github.com/alibaba/hooks/commit/a0c33c21caefda40753fe4b3cbb3b1efbabd1a79)

**Tree at this commit:** [alibaba/hooks@a0c33c21caef](https://github.com/alibaba/hooks/tree/a0c33c21caefda40753fe4b3cbb3b1efbabd1a79)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alibaba/hooks |
| Description | A high-quality & reliable React Hooks library.   https://alibaba.github.io/hooks/ |
| Stars | 14979 |
| Forks | 2756 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `a0c33c21caefda40753fe4b3cbb3b1efbabd1a79` |
| Retrieved at | 2026-11-14T19:13:16.365071+00:00 |
| Files in this snapshot | 664 |

## Directory tree

```text
.cursor/  (6 files)
  rules/  (6 files)
    demo.mdc
    docs.mdc
    git.mdc
    project.mdc
    testing.mdc
    typescript.mdc
.github/  (9 files)
  PULL_REQUEST_TEMPLATE/  (1 files)
    pr_cn.md
  workflows/  (7 files)
    comment-when-needs-more-info.yml
    gitleaks.yml
    issue-close-require.yml
    issue-reply.yml
    pkg.pr.new.yml
    static.yml
    test.yml
  PULL_REQUEST_TEMPLATE.md
.husky/  (2 files)
  commit-msg
  pre-commit
config/  (2 files)
  config.ts
  hooks.ts
docs/  (16 files)
  guide/  (14 files)
    blog/  (8 files)
      … 8 files under this directory
    dom.en-US.md
    dom.zh-CN.md
    index.en-US.md
    index.zh-CN.md
    upgrade.en-US.md
    upgrade.zh-CN.md
  index.en-US.md
  index.zh-CN.md
example/  (1 files)
  .gitkeep
packages/  (598 files)
  hooks/  (581 files)
    src/  (575 files)
      … 575 files under this directory
    gulpfile.js
    package.json
    tsconfig.json
    tsconfig.pro.json
    vitest.config.ts
    webpack.config.ts
  use-url-state/  (17 files)
    __tests__/  (3 files)
      … 3 files under this directory
    demo/  (4 files)
      … 4 files under this directory
    src/  (1 files)
      … 1 files under this directory
    README.md
    gulpfile.js
    package.json
    tsconfig.json
    tsconfig.pro.json
    use-url-state.en-US.md
    use-url-state.zh-CN.md
    vitest.config.ts
    webpack.config.ts
public/  (5 files)
  useExternal/  (2 files)
    bootstrap-badge.css
    test-external-script.js
  logo.svg
  simple-logo.svg
  style.css
scripts/  (1 files)
  build-with-relative-paths.js
.babelrc
.coveralls.yml
.editorconfig
.gitignore
.gitleaks.toml
.travis.yml
AGENTS.md
CLAUDE.md
CONTRIBUTING.MD
CONTRIBUTING.zh-CN.MD
LICENSE
README.md
README.zh-CN.md
RELEASING.md
SECURITY.md
biome.json
gulpfile.js
package.json
pnpm-workspace.yaml
tsconfig.base.json
tsconfig.pro.json
umd.html
vitest.config.ts
webpack.common.ts
```

## Entry points

- [packages/hooks/src/index.ts](https://github.com/alibaba/hooks/blob/a0c33c21caefda40753fe4b3cbb3b1efbabd1a79/packages/hooks/src/index.ts)
- [packages/use-url-state/src/index.ts](https://github.com/alibaba/hooks/blob/a0c33c21caefda40753fe4b3cbb3b1efbabd1a79/packages/use-url-state/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 416 file(s) under packages package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.coveralls.yml` (config)
- `.editorconfig` (config)
- `.github/workflows/comment-when-needs-more-info.yml` (ci)
- `.github/workflows/gitleaks.yml` (ci)
- `.github/workflows/issue-close-require.yml` (ci)
- `.github/workflows/issue-reply.yml` (ci)
- `.github/workflows/pkg.pr.new.yml` (ci)
- `.github/workflows/static.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.gitleaks.toml` (config)
- `.travis.yml` (ci)
- `biome.json` (config)
- `package.json` (manifest)
- `packages/hooks/package.json` (manifest)
- `packages/hooks/tsconfig.json` (config)
- `packages/hooks/tsconfig.pro.json` (config)
- `packages/use-url-state/package.json` (manifest)
- `packages/use-url-state/tsconfig.json` (config)
- `packages/use-url-state/tsconfig.pro.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.base.json` (config)
- `tsconfig.pro.json` (config)

## Top-level layout

- `packages` — 598 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `docs` — 16 analysed file(s)
- `.github` — 9 analysed file(s)
- `.cursor` — 6 analysed file(s)
- `public` — 5 analysed file(s)
- `.husky` — 2 analysed file(s)
- `config` — 2 analysed file(s)
- `example` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a0c33c21caefda40753fe4b3cbb3b1efbabd1a79` is the revision these paths and observations refer to.
