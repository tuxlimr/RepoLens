# Project structure: enyo/dropzone

**Analysed commit:** `a0e896a705c356d4ce427d682041f0f47278237e`

**Commit reference:** [a0e896a705c356d4ce427d682041f0f47278237e](https://github.com/enyo/dropzone/commit/a0e896a705c356d4ce427d682041f0f47278237e)

**Tree at this commit:** [enyo/dropzone@a0e896a705c3](https://github.com/enyo/dropzone/tree/a0e896a705c356d4ce427d682041f0f47278237e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | enyo/dropzone |
| Description | Dropzone is an easy to use drag'n'drop library. It supports image previews and shows nice progress bars. |
| Stars | 18409 |
| Forks | 3225 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `a0e896a705c356d4ce427d682041f0f47278237e` |
| Retrieved at | 2026-11-14T19:11:22.064778+00:00 |
| Files in this snapshot | 134 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    ci.yml
    deploy.yml
    release.yml
  FUNDING.yml
  dependabot.yml
apps/  (69 files)
  docs/  (26 files)
    docs/  (22 files)
      … 22 files under this directory
    src/  (1 files)
      … 1 files under this directory
    docusaurus.config.js
    package.json
    sidebars.js
  website/  (43 files)
    src/  (27 files)
      … 27 files under this directory
    static/  (7 files)
      … 7 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    package.json
    playwright.config.ts
    postcss-linear-clamp.ts
    tsconfig.json
    vite.config.ts
packages/  (42 files)
  dropzone/  (42 files)
    e2e/  (4 files)
      … 4 files under this directory
    src/  (8 files)
      … 8 files under this directory
    test/  (21 files)
      … 21 files under this directory
    CHANGELOG.md
    README.md
    composer.json
    package.json
    playwright.config.mjs
    tsconfig.json
    tsconfig.typecheck.json
    vite.config.global.mjs
    vite.config.mjs
scripts/  (1 files)
  build-site.sh
.git-blame-ignore-revs
.gitignore
.oxfmtignore
.oxfmtrc.json
.oxlintrc.json
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
ROADMAP.md
SECURITY.md
package.json
pnpm-workspace.yaml
```

## Entry points

- [packages/dropzone/src/dropzone.ts](https://github.com/enyo/dropzone/blob/a0e896a705c356d4ce427d682041f0f47278237e/packages/dropzone/src/dropzone.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 23 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 12 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 23 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `apps/docs/package.json` (manifest)
- `apps/website/package.json` (manifest)
- `apps/website/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/dropzone/composer.json` (config)
- `packages/dropzone/package.json` (manifest)
- `packages/dropzone/tsconfig.json` (config)
- `packages/dropzone/tsconfig.typecheck.json` (config)
- `pnpm-workspace.yaml` (config)

## Top-level layout

- `apps` — 69 analysed file(s)
- `packages` — 42 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 7 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a0e896a705c356d4ce427d682041f0f47278237e` is the revision these paths and observations refer to.
